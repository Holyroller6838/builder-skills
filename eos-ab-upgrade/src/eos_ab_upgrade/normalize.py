"""Normalize raw Itential / CVP / Device Broker data into the canonical readiness schema.

evaluate_pair_readiness() ONLY accepts the canonical schema defined in
schemas/pair_readiness.canonical.json. Vendor- and platform-specific response
shapes are handled exclusively here — never inside the evaluator.

Operational field groups (mlag, bgp, interfaces) are labeled field_status=*unverified*
until live operational-command responses are captured in lab. CVP inventory data
can verify identity, reachability, and version only.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

# Default policy used when raw payloads omit one (e.g. inventory-only CVP fixtures).
DEFAULT_POLICY: dict[str, Any] = {
    "supported_source_versions": ["4.28", "4.29", "4.30", "4.31"],
    "require_mlag_active": True,
    "minimum_bgp_health_percent": 100,
    "minimum_interface_health_percent": 100,
}

# CVP streamingStatus values treated as reachable.
_CVP_REACHABLE_STATUSES = frozenset({"active"})

# Canonical field_status template — operational groups start unverified.
_UNVERIFIED_OPERATIONAL_STATUS: dict[str, str] = {
    "identity": "unverified",
    "reachability": "unverified",
    "version": "unverified",
    "mlag": "unverified",
    "bgp": "unverified",
    "interfaces": "unverified",
}


def normalize_pair_readiness(raw: dict) -> dict:
    """Convert raw platform/vendor payloads into the canonical pair-readiness input.

    Accepted shapes (detected, never guessed beyond documented keys):
    1. Already-canonical: has side_a/side_b with device_name + field_status
    2. Pair envelope with two device records under side_a/side_b (CVP or MVP1 side)
    3. CVP inventory envelope: {"data": [device, ...]} or a bare CVP device object
       (requires side mapping via raw["side_a"] / raw["side_b"] or pair keys)

    Raises ValueError when the payload cannot be mapped into two sides.
    """
    if not isinstance(raw, dict):
        raise TypeError("normalize_pair_readiness expects a dict payload")

    if _looks_canonical(raw):
        return _ensure_canonical_defaults(deepcopy(raw))

    if "side_a" in raw and "side_b" in raw:
        policy = _policy_from_raw(raw)
        return {
            "side_a": normalize_side(raw["side_a"]),
            "side_b": normalize_side(raw["side_b"]),
            "policy": policy,
        }

    raise ValueError(
        "cannot normalize payload: expected canonical pair readiness input, "
        "or an object with 'side_a' and 'side_b' device records"
    )


def normalize_side(raw_side: Any) -> dict[str, Any]:
    """Normalize one device-side record into the canonical side object."""
    if not isinstance(raw_side, dict):
        raise TypeError("side record must be a dict")

    if _side_looks_canonical(raw_side):
        return _ensure_side_defaults(deepcopy(raw_side))

    if _looks_cvp_device(raw_side):
        return _normalize_cvp_device(raw_side)

    if _looks_mvp1_side(raw_side):
        return _normalize_mvp1_side(raw_side)

    if _looks_device_broker_facts(raw_side):
        return _normalize_device_broker_side(raw_side)

    raise ValueError(
        "unrecognized side record shape; expected CVP device inventory, "
        "MVP1 side record (hostname/facts/peer_state), Device Broker collected "
        "facts, or a canonical readiness side"
    )


def _looks_canonical(raw: dict) -> bool:
    if not isinstance(raw.get("side_a"), dict) or not isinstance(raw.get("side_b"), dict):
        return False
    return _side_looks_canonical(raw["side_a"]) and _side_looks_canonical(raw["side_b"])


def _side_looks_canonical(side: dict) -> bool:
    return "device_name" in side and "field_status" in side and "reachable" in side


def _looks_cvp_device(side: dict) -> bool:
    # Real CVP inventory devices expose streamingStatus + version/softwareVersion
    # and hostname (LAB01A-style). systemMacAddress is common but not required.
    has_name = "hostname" in side or "fqdn" in side
    has_stream = "streamingStatus" in side
    has_version = "version" in side or "softwareVersion" in side or "internalVersion" in side
    return bool(has_name and (has_stream or has_version) and "facts" not in side)


def _looks_mvp1_side(side: dict) -> bool:
    return "hostname" in side and ("facts" in side or "peer_state" in side or "management_ip" in side)


def _looks_device_broker_facts(side: dict) -> bool:
    # Collected Device Broker blob without hostname wrapper — rare; require device_name or hostname.
    return ("device_name" in side or "hostname" in side) and (
        "reachable" in side or "version" in side or "mlag_state" in side
    )


def _normalize_cvp_device(device: dict) -> dict[str, Any]:
    """Map a LAB01A-style CVP inventory device into canonical form.

    Verified from CVP inventory: identity, reachability (streamingStatus), version.
    UNVERIFIED (null): mlag_*, bgp_*, critical_interfaces_* — pending live
    operational-command responses (show mlag, show ip bgp summary, show interfaces).
    """
    hostname = str(device.get("hostname") or device.get("fqdn") or "").strip()
    if not hostname:
        raise ValueError("CVP device record missing hostname/fqdn")

    version = (
        device.get("version")
        or device.get("softwareVersion")
        or device.get("internalVersion")
        or ""
    )
    version = str(version).strip()
    if not version:
        raise ValueError(f"CVP device '{hostname}' missing version/softwareVersion")

    streaming = str(device.get("streamingStatus", "")).strip().lower()
    # Absent streamingStatus → unreachable (fail closed); only "active" is reachable.
    reachable = streaming in _CVP_REACHABLE_STATUSES if streaming else False

    field_status = {
        "identity": "verified",
        "reachability": "verified" if streaming else "unverified",
        "version": "verified",
        # Explicitly unverified until live operational-command responses are captured.
        "mlag": "unverified",
        "bgp": "unverified",
        "interfaces": "unverified",
    }

    return {
        "device_name": hostname,
        "reachable": reachable,
        "version": version,
        "mlag_state": None,
        "mlag_peer_state": None,
        "bgp_established": None,
        "bgp_expected": None,
        "critical_interfaces_up": None,
        "critical_interfaces_expected": None,
        "field_status": field_status,
    }


def _normalize_mvp1_side(side: dict) -> dict[str, Any]:
    """Map the legacy MVP1 collected-facts side record into canonical form.

    hostname / facts.version / reachability-from-facts are treated as verified
    collection outputs. MLAG/BGP/interface counts remain unverified unless the
    side already carries explicit canonical operational fields from a live
    operational-command collect step.
    """
    hostname = str(side.get("hostname") or "").strip()
    if not hostname:
        raise ValueError("MVP1 side record missing hostname")

    facts = side.get("facts") if isinstance(side.get("facts"), dict) else {}
    version = str(facts.get("version") or side.get("source_version") or "").strip()
    reachable = bool(facts) if "facts" in side else bool(side.get("reachable", False))

    field_status = {
        "identity": "verified",
        "reachability": "verified" if ("facts" in side or "reachable" in side) else "unverified",
        "version": "verified" if version else "unverified",
        "mlag": "unverified",
        "bgp": "unverified",
        "interfaces": "unverified",
    }

    # Optional already-canonical operational overlays (from a future Collect node).
    mlag_state = side.get("mlag_state")
    mlag_peer_state = side.get("mlag_peer_state")
    bgp_established = side.get("bgp_established")
    bgp_expected = side.get("bgp_expected")
    interfaces_up = side.get("critical_interfaces_up")
    interfaces_expected = side.get("critical_interfaces_expected")

    if mlag_state is not None and mlag_peer_state is not None:
        field_status["mlag"] = "verified"
    if bgp_established is not None and bgp_expected is not None:
        field_status["bgp"] = "verified"
    if interfaces_up is not None and interfaces_expected is not None:
        field_status["interfaces"] = "verified"

    # peer_state.healthy is an invented MVP1 abstraction — NOT a live show mlag
    # capture. Do not promote it to verified operational MLAG fields.
    return {
        "device_name": hostname,
        "reachable": reachable,
        "version": version,
        "mlag_state": mlag_state if field_status["mlag"] == "verified" else None,
        "mlag_peer_state": mlag_peer_state if field_status["mlag"] == "verified" else None,
        "bgp_established": bgp_established if field_status["bgp"] == "verified" else None,
        "bgp_expected": bgp_expected if field_status["bgp"] == "verified" else None,
        "critical_interfaces_up": interfaces_up if field_status["interfaces"] == "verified" else None,
        "critical_interfaces_expected": (
            interfaces_expected if field_status["interfaces"] == "verified" else None
        ),
        "field_status": field_status,
    }


def _normalize_device_broker_side(side: dict) -> dict[str, Any]:
    """Normalize a partial Device Broker / already-flat side into canonical form."""
    device_name = str(side.get("device_name") or side.get("hostname") or "").strip()
    if not device_name:
        raise ValueError("Device Broker side record missing device_name/hostname")

    field_status = dict(_UNVERIFIED_OPERATIONAL_STATUS)
    field_status["identity"] = "verified"

    reachable = bool(side.get("reachable", False))
    field_status["reachability"] = "verified" if "reachable" in side else "unverified"

    version = str(side.get("version") or "").strip()
    field_status["version"] = "verified" if version else "unverified"

    result = {
        "device_name": device_name,
        "reachable": reachable,
        "version": version,
        "mlag_state": None,
        "mlag_peer_state": None,
        "bgp_established": None,
        "bgp_expected": None,
        "critical_interfaces_up": None,
        "critical_interfaces_expected": None,
        "field_status": field_status,
    }

    if side.get("mlag_state") is not None and side.get("mlag_peer_state") is not None:
        result["mlag_state"] = side["mlag_state"]
        result["mlag_peer_state"] = side["mlag_peer_state"]
        field_status["mlag"] = "verified"

    if side.get("bgp_established") is not None and side.get("bgp_expected") is not None:
        result["bgp_established"] = side["bgp_established"]
        result["bgp_expected"] = side["bgp_expected"]
        field_status["bgp"] = "verified"

    if (
        side.get("critical_interfaces_up") is not None
        and side.get("critical_interfaces_expected") is not None
    ):
        result["critical_interfaces_up"] = side["critical_interfaces_up"]
        result["critical_interfaces_expected"] = side["critical_interfaces_expected"]
        field_status["interfaces"] = "verified"

    return result


def _policy_from_raw(raw: dict) -> dict[str, Any]:
    policy = raw.get("policy")
    if isinstance(policy, dict):
        merged = dict(DEFAULT_POLICY)
        merged.update(policy)
        return merged
    return dict(DEFAULT_POLICY)


def _ensure_canonical_defaults(data: dict) -> dict:
    data["side_a"] = _ensure_side_defaults(data["side_a"])
    data["side_b"] = _ensure_side_defaults(data["side_b"])
    if "policy" not in data or not isinstance(data["policy"], dict):
        data["policy"] = dict(DEFAULT_POLICY)
    else:
        merged = dict(DEFAULT_POLICY)
        merged.update(data["policy"])
        data["policy"] = merged
    return data


def _ensure_side_defaults(side: dict) -> dict:
    status = dict(_UNVERIFIED_OPERATIONAL_STATUS)
    incoming = side.get("field_status") if isinstance(side.get("field_status"), dict) else {}
    status.update(incoming)
    side["field_status"] = status
    for key in (
        "mlag_state",
        "mlag_peer_state",
        "bgp_established",
        "bgp_expected",
        "critical_interfaces_up",
        "critical_interfaces_expected",
    ):
        side.setdefault(key, None)
    return side
