from __future__ import annotations

from datetime import datetime, timezone

from .device_broker import device_from_record
from .models import Device

SUPPORTED_SOURCE_VERSIONS = {"4.28", "4.29", "4.30", "4.31"}


def check_reachable(connectivity: dict) -> bool:
    return bool(connectivity.get("reachable"))


def check_source_version_supported(facts: dict, supported: set[str] = SUPPORTED_SOURCE_VERSIONS) -> bool:
    version = facts.get("version", "")
    return any(version.startswith(v) for v in supported)


def check_mlag_healthy(mlag_status: dict) -> bool:
    return bool(mlag_status.get("healthy"))


def check_interfaces_healthy(interfaces: dict) -> bool:
    return interfaces.get("down_count", 1) == 0


def evaluate_readiness(
    device: Device,
    target_version: str,
    connectivity: dict,
    facts: dict,
    mlag_status: dict,
    interfaces: dict,
) -> tuple[bool, dict]:
    results = {
        "reachable": check_reachable(connectivity),
        "source_version_supported": check_source_version_supported(facts),
        "mlag_healthy": check_mlag_healthy(mlag_status),
        "interfaces_healthy": check_interfaces_healthy(interfaces),
    }
    passed = all(results.values())
    return passed, results


def build_readiness_evidence(
    device: Device, target_version: str, passed: bool, details: dict, bgp_summary: dict
) -> dict:
    return {
        "device_hostname": device.hostname,
        "target_version": target_version,
        "passed": passed,
        "details": details,
        "bgp_summary": bgp_summary,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def run_readiness_check_from_payload(payload: dict) -> dict:
    required = ("device", "target_version", "connectivity", "facts", "mlag_status", "bgp_summary", "interfaces")
    missing = [k for k in required if k not in payload]
    if missing:
        raise ValueError(f"readiness payload missing required key(s): {missing}")

    device = device_from_record(payload["device"])
    target_version = payload["target_version"]
    passed, details = evaluate_readiness(
        device,
        target_version,
        payload["connectivity"],
        payload["facts"],
        payload["mlag_status"],
        payload["interfaces"],
    )
    return build_readiness_evidence(device, target_version, passed, details, payload["bgp_summary"])
