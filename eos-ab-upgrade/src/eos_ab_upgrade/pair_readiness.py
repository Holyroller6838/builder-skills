"""Pair readiness checks for EOS A/B upgrade decisions."""

from __future__ import annotations

from typing import Any

REQUIRED_TOP_LEVEL_KEYS = ("side_a", "side_b", "policy")

REQUIRED_SIDE_FIELDS = (
    "device_name",
    "reachable",
    "version",
    "mlag_state",
    "mlag_peer_state",
    "bgp_established",
    "bgp_expected",
    "critical_interfaces_up",
    "critical_interfaces_expected",
)

REQUIRED_POLICY_FIELDS = (
    "supported_source_versions",
    "require_mlag_active",
    "minimum_bgp_health_percent",
    "minimum_interface_health_percent",
)

# Normalized Device Broker values treated as healthy.
_ACTIVE_MLAG_STATES = frozenset({"active"})
_CONNECTED_PEER_STATES = frozenset({"connected"})


def evaluate_pair_readiness(data: dict) -> dict:
    """Evaluate normalized Device Broker pair data for A/B upgrade readiness.

    This function performs pure decision logic only. It does not connect to
    devices, run EOS commands, or call Itential APIs.
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


def _evaluate_side(
    side_label: str,
    side: dict[str, Any],
    policy: dict[str, Any],
) -> tuple[dict[str, Any], list[str], list[str]]:
    blocking: list[str] = []
    warnings: list[str] = []

    missing_fields = [field for field in REQUIRED_SIDE_FIELDS if field not in side]
    if missing_fields:
        blocking.append(
            f"{side_label}: missing required data: "
            + ", ".join(f"'{field}'" for field in missing_fields)
        )
        return (
            {
                "device_name": side.get("device_name"),
                "status": "failed",
            },
            blocking,
            warnings,
        )

    device_name = side["device_name"]
    reachable = bool(side["reachable"])
    version = str(side["version"])
    mlag_state = str(side["mlag_state"]).lower()
    mlag_peer_state = str(side["mlag_peer_state"]).lower()

    try:
        bgp_established = _as_non_negative_number(side["bgp_established"], "bgp_established")
        bgp_expected = _as_non_negative_number(side["bgp_expected"], "bgp_expected")
        interfaces_up = _as_non_negative_number(
            side["critical_interfaces_up"], "critical_interfaces_up"
        )
        interfaces_expected = _as_non_negative_number(
            side["critical_interfaces_expected"], "critical_interfaces_expected"
        )
    except ValueError as exc:
        blocking.append(f"{side_label} ({device_name}): {exc}")
        return (
            {
                "device_name": device_name,
                "reachable": reachable,
                "version": version,
                "status": "failed",
            },
            blocking,
            warnings,
        )

    bgp_health_percent = _health_percent(bgp_established, bgp_expected)
    interface_health_percent = _health_percent(interfaces_up, interfaces_expected)

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

    if require_mlag_active and mlag_state not in _ACTIVE_MLAG_STATES:
        blocking.append(
            f"{side_label} ({device_name}): unhealthy MLAG state '{side['mlag_state']}'"
        )
        side_degraded = True

    if require_mlag_active and mlag_peer_state not in _CONNECTED_PEER_STATES:
        blocking.append(
            f"{side_label} ({device_name}): unhealthy MLAG peer state "
            f"'{side['mlag_peer_state']}'"
        )
        side_degraded = True

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
            f"{interface_health_percent:.1f}% is below 100% but meets policy threshold"
        )
        side_degraded = True

    if side_failed:
        status = "failed"
    elif side_degraded:
        status = "degraded"
    else:
        status = "healthy"

    baseline = {
        "device_name": device_name,
        "reachable": reachable,
        "version": version,
        "version_supported": version_supported,
        "mlag_state": side["mlag_state"],
        "mlag_peer_state": side["mlag_peer_state"],
        "bgp_established": bgp_established,
        "bgp_expected": bgp_expected,
        "bgp_health_percent": bgp_health_percent,
        "critical_interfaces_up": interfaces_up,
        "critical_interfaces_expected": interfaces_expected,
        "interface_health_percent": interface_health_percent,
        "status": status,
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
        raise ValueError(f"invalid numeric value for '{field_name}'")
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
