"""Pair readiness checks for EOS A/B upgrade decisions.

Consumes ONLY the canonical readiness schema
(schemas/pair_readiness.canonical.json). Raw Itential / CVP / Device Broker
payloads must pass through eos_ab_upgrade.normalize first.
"""

from __future__ import annotations

from typing import Any

REQUIRED_TOP_LEVEL_KEYS = ("side_a", "side_b", "policy")

# Always required on every side (identity / reachability / version).
REQUIRED_CORE_SIDE_FIELDS = ("device_name", "reachable", "version")

# Operational groups — required only when field_status.<group> is verified
# (or when field_status is omitted and the group fields are expected).
OPERATIONAL_GROUPS: dict[str, tuple[str, ...]] = {
    "mlag": ("mlag_state", "mlag_peer_state"),
    "bgp": ("bgp_established", "bgp_expected"),
    "interfaces": ("critical_interfaces_up", "critical_interfaces_expected"),
}

REQUIRED_POLICY_FIELDS = (
    "supported_source_versions",
    "require_mlag_active",
    "minimum_bgp_health_percent",
    "minimum_interface_health_percent",
)

# Normalized Device Broker values treated as healthy.
_ACTIVE_MLAG_STATES = frozenset({"active"})
_CONNECTED_PEER_STATES = frozenset({"connected"})

_UNVERIFIED = "unverified"
_VERIFIED = "verified"


def evaluate_pair_readiness(data: dict) -> dict:
    """Evaluate canonical pair readiness data for A/B upgrade readiness.

    This function performs pure decision logic only. It does not connect to
    devices, run EOS commands, or call Itential APIs. It does not interpret
    vendor- or platform-specific response formats — feed it canonical input
    from normalize_pair_readiness().
    """
    blocking_reasons: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        return _result(
            eligible=False,
            blocking_reasons=["missing required data: input must be a dict"],
            warnings=[],
            pair_health="failed",
            side_a={},
            side_b={},
        )

    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in data or not isinstance(data.get(key), dict):
            blocking_reasons.append(f"missing required data: '{key}'")

    if blocking_reasons:
        return _result(
            eligible=False,
            blocking_reasons=blocking_reasons,
            warnings=[],
            pair_health="failed",
            side_a={},
            side_b={},
        )

    policy = data["policy"]
    policy_missing = [field for field in REQUIRED_POLICY_FIELDS if field not in policy]
    if policy_missing:
        blocking_reasons.append(
            "missing required data: policy fields "
            + ", ".join(f"'{field}'" for field in policy_missing)
        )
        return _result(
            eligible=False,
            blocking_reasons=blocking_reasons,
            warnings=[],
            pair_health="failed",
            side_a={},
            side_b={},
        )

    side_a_baseline, side_a_blocking, side_a_warnings = _evaluate_side(
        side_label="side_a",
        side=data["side_a"],
        policy=policy,
    )
    side_b_baseline, side_b_blocking, side_b_warnings = _evaluate_side(
        side_label="side_b",
        side=data["side_b"],
        policy=policy,
    )

    blocking_reasons.extend(side_a_blocking)
    blocking_reasons.extend(side_b_blocking)
    warnings.extend(side_a_warnings)
    warnings.extend(side_b_warnings)

    pair_health = _pair_health(
        side_a_status=side_a_baseline.get("status", "failed"),
        side_b_status=side_b_baseline.get("status", "failed"),
        blocking_reasons=blocking_reasons,
    )

    return _result(
        eligible=len(blocking_reasons) == 0,
        blocking_reasons=blocking_reasons,
        warnings=warnings,
        pair_health=pair_health,
        side_a=side_a_baseline,
        side_b=side_b_baseline,
    )


def _field_status(side: dict[str, Any]) -> dict[str, str]:
    """Return per-group verification status.

    When field_status is omitted (legacy canonical fixtures), operational groups
    default to verified so existing fully-populated tests keep working.
    Explicit 'unverified' labels from the normalizer are honored.
    """
    raw = side.get("field_status")
    if not isinstance(raw, dict):
        return {
            "identity": _VERIFIED,
            "reachability": _VERIFIED,
            "version": _VERIFIED,
            "mlag": _VERIFIED,
            "bgp": _VERIFIED,
            "interfaces": _VERIFIED,
        }
    status = {
        "identity": _VERIFIED,
        "reachability": _VERIFIED,
        "version": _VERIFIED,
        "mlag": _VERIFIED,
        "bgp": _VERIFIED,
        "interfaces": _VERIFIED,
    }
    for key, value in raw.items():
        if key in status and value in (_VERIFIED, _UNVERIFIED):
            status[key] = value
    return status


def _evaluate_side(
    side_label: str,
    side: dict[str, Any],
    policy: dict[str, Any],
) -> tuple[dict[str, Any], list[str], list[str]]:
    blocking: list[str] = []
    warnings: list[str] = []
    status = _field_status(side)

    missing_core = [field for field in REQUIRED_CORE_SIDE_FIELDS if field not in side]
    if missing_core:
        blocking.append(
            f"{side_label}: missing required data: "
            + ", ".join(f"'{field}'" for field in missing_core)
        )
        return (
            {
                "device_name": side.get("device_name"),
                "status": "failed",
                "field_status": status,
            },
            blocking,
            warnings,
        )

    # Require operational fields only for verified groups.
    missing_ops: list[str] = []
    for group, fields in OPERATIONAL_GROUPS.items():
        if status[group] == _VERIFIED:
            for field in fields:
                if field not in side or side[field] is None:
                    missing_ops.append(field)

    if missing_ops:
        blocking.append(
            f"{side_label}: missing required data: "
            + ", ".join(f"'{field}'" for field in missing_ops)
        )
        return (
            {
                "device_name": side.get("device_name"),
                "status": "failed",
                "field_status": status,
            },
            blocking,
            warnings,
        )

    for group in ("mlag", "bgp", "interfaces"):
        if status[group] == _UNVERIFIED:
            warnings.append(
                f"{side_label}: {group} fields are unverified — pending live "
                "operational-command responses; check skipped"
            )

    device_name = side["device_name"]
    reachable = bool(side["reachable"])
    version = str(side["version"])

    version_supported = _version_supported(
        version, policy["supported_source_versions"]
    )
    min_bgp = float(policy["minimum_bgp_health_percent"])
    min_interfaces = float(policy["minimum_interface_health_percent"])
    require_mlag_active = bool(policy["require_mlag_active"])

    side_failed = False
    side_degraded = False

    if not reachable:
        blocking.append(f"{side_label} ({device_name}): device unreachable")
        side_failed = True

    if not version_supported:
        blocking.append(
            f"{side_label} ({device_name}): unsupported EOS version '{version}'"
        )
        side_failed = True

    mlag_state = side.get("mlag_state")
    mlag_peer_state = side.get("mlag_peer_state")
    bgp_established = side.get("bgp_established")
    bgp_expected = side.get("bgp_expected")
    interfaces_up = side.get("critical_interfaces_up")
    interfaces_expected = side.get("critical_interfaces_expected")
    bgp_health_percent: float | None = None
    interface_health_percent: float | None = None

    if status["mlag"] == _VERIFIED:
        mlag_state_s = str(mlag_state).lower()
        mlag_peer_state_s = str(mlag_peer_state).lower()
        if require_mlag_active and mlag_state_s not in _ACTIVE_MLAG_STATES:
            blocking.append(
                f"{side_label} ({device_name}): unhealthy MLAG state '{mlag_state}'"
            )
            side_degraded = True
        if require_mlag_active and mlag_peer_state_s not in _CONNECTED_PEER_STATES:
            blocking.append(
                f"{side_label} ({device_name}): unhealthy MLAG peer state "
                f"'{mlag_peer_state}'"
            )
            side_degraded = True

    if status["bgp"] == _VERIFIED:
        try:
            bgp_established_n = _as_non_negative_number(bgp_established, "bgp_established")
            bgp_expected_n = _as_non_negative_number(bgp_expected, "bgp_expected")
        except (TypeError, ValueError) as exc:
            blocking.append(f"{side_label} ({device_name}): {exc}")
            return (
                {
                    "device_name": device_name,
                    "reachable": reachable,
                    "version": version,
                    "status": "failed",
                    "field_status": status,
                },
                blocking,
                warnings,
            )
        bgp_established = bgp_established_n
        bgp_expected = bgp_expected_n
        bgp_health_percent = _health_percent(bgp_established_n, bgp_expected_n)
        if bgp_health_percent < min_bgp:
            blocking.append(
                f"{side_label} ({device_name}): BGP health "
                f"{bgp_health_percent:.1f}% below policy threshold {min_bgp:.1f}%"
            )
            side_degraded = True
        elif bgp_health_percent < 100.0:
            warnings.append(
                f"{side_label} ({device_name}): BGP health "
                f"{bgp_health_percent:.1f}% is below 100% but meets policy threshold"
            )
            side_degraded = True

    if status["interfaces"] == _VERIFIED:
        try:
            interfaces_up_n = _as_non_negative_number(
                interfaces_up, "critical_interfaces_up"
            )
            interfaces_expected_n = _as_non_negative_number(
                interfaces_expected, "critical_interfaces_expected"
            )
        except (TypeError, ValueError) as exc:
            blocking.append(f"{side_label} ({device_name}): {exc}")
            return (
                {
                    "device_name": device_name,
                    "reachable": reachable,
                    "version": version,
                    "status": "failed",
                    "field_status": status,
                },
                blocking,
                warnings,
            )
        interfaces_up = interfaces_up_n
        interfaces_expected = interfaces_expected_n
        interface_health_percent = _health_percent(
            interfaces_up_n, interfaces_expected_n
        )
        if interface_health_percent < min_interfaces:
            blocking.append(
                f"{side_label} ({device_name}): critical interface health "
                f"{interface_health_percent:.1f}% below policy threshold "
                f"{min_interfaces:.1f}%"
            )
            side_degraded = True
        elif interface_health_percent < 100.0:
            warnings.append(
                f"{side_label} ({device_name}): critical interface health "
                f"{interface_health_percent:.1f}% is below 100% but meets policy "
                "threshold"
            )
            side_degraded = True

    if side_failed:
        side_status = "failed"
    elif side_degraded:
        side_status = "degraded"
    else:
        side_status = "healthy"

    baseline = {
        "device_name": device_name,
        "reachable": reachable,
        "version": version,
        "version_supported": version_supported,
        "mlag_state": mlag_state,
        "mlag_peer_state": mlag_peer_state,
        "bgp_established": bgp_established,
        "bgp_expected": bgp_expected,
        "bgp_health_percent": bgp_health_percent,
        "critical_interfaces_up": interfaces_up,
        "critical_interfaces_expected": interfaces_expected,
        "interface_health_percent": interface_health_percent,
        "field_status": status,
        "status": side_status,
    }
    return baseline, blocking, warnings


def _health_percent(actual: float, expected: float) -> float:
    """Return health as a percentage of expected count."""
    if expected == 0:
        return 100.0 if actual == 0 else 0.0
    return (actual / expected) * 100.0


def _version_supported(version: str, supported_source_versions: Any) -> bool:
    if not isinstance(supported_source_versions, (list, tuple, set)):
        return False
    return any(
        version == str(supported) or version.startswith(f"{supported}.")
        for supported in supported_source_versions
    )


def _as_non_negative_number(value: Any, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"invalid numeric value for '{field_name}'")
    number = float(value)
    if number < 0:
        raise ValueError(f"'{field_name}' must be non-negative")
    return number


def _pair_health(
    side_a_status: str,
    side_b_status: str,
    blocking_reasons: list[str],
) -> str:
    statuses = {side_a_status, side_b_status}
    if "failed" in statuses:
        return "failed"
    if "degraded" in statuses or blocking_reasons:
        return "degraded"
    return "healthy"


def _result(
    *,
    eligible: bool,
    blocking_reasons: list[str],
    warnings: list[str],
    pair_health: str,
    side_a: dict[str, Any],
    side_b: dict[str, Any],
) -> dict[str, Any]:
    return {
        "eligible": eligible,
        "blocking_reasons": blocking_reasons,
        "warnings": warnings,
        "baseline": {
            "pair_health": pair_health,
            "side_a": side_a,
            "side_b": side_b,
        },
    }
