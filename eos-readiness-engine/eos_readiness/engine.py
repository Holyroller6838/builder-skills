from __future__ import annotations

from .checks import check_bgp, check_collection, check_interfaces, check_mlag, check_version
from .errors import MalformedPayloadError
from .models import CheckResult, NormalizedPairData
from .profiles import resolve_profile
from .raw import group_by_device_and_command, normalize_pair_data
from .status import Status, worst_of


def evaluate_normalized(
    normalized: NormalizedPairData,
    profile_name: str,
    *,
    target_version: str | None = None,
    critical_interfaces: dict[str, list[str]] | None = None,
    critical_bgp_peers: dict[str, list[str]] | None = None,
) -> dict:
    profile = resolve_profile(profile_name)

    results: dict[str, CheckResult] = {
        "collection": check_collection(normalized, profile.checks_enabled),
        "version": check_version(normalized, target_version),
        "interfaces": check_interfaces(normalized, critical_interfaces or {}),
    }

    results["mlag"] = (
        check_mlag(normalized)
        if "mlag" in profile.checks_enabled
        else CheckResult(Status.NOT_APPLICABLE)
    )
    results["bgp"] = (
        check_bgp(normalized, critical_bgp_peers or {})
        if "bgp" in profile.checks_enabled
        else CheckResult(Status.NOT_APPLICABLE)
    )

    overall_status = worst_of(r.status for r in results.values())
    ready = overall_status == Status.PASS

    return {
        "pair": {
            "device_a": normalized.device_a.hostname,
            "device_b": normalized.device_b.hostname,
        },
        "profile": profile_name,
        "ready": ready,
        "status": overall_status.value,
        "checks": {name: result.status.value for name, result in results.items()},
        "reasons": [reason for result in results.values() for reason in result.reasons],
    }


REQUIRED_PAYLOAD_KEYS = ("pair_id", "target_version", "profile", "command_results")


def evaluate_pair(payload: dict) -> dict:
    missing = [k for k in REQUIRED_PAYLOAD_KEYS if k not in payload]
    if missing:
        raise MalformedPayloadError(f"payload missing required key(s): {missing}")

    pair_id = payload["pair_id"]
    target_version = payload["target_version"]
    profile_name = payload["profile"]
    command_results = payload["command_results"]

    profile = resolve_profile(profile_name)

    grouped = group_by_device_and_command(command_results)
    device_names = sorted(grouped.keys())

    if len(device_names) != 2:
        return {
            "pair_id": pair_id,
            "profile": profile_name,
            "ready": False,
            "status": Status.FAIL.value,
            "checks": {},
            "reasons": [
                (
                    "expected exactly 2 distinct devices in command_results (grouped by each "
                    f"result's 'name' field), found {len(device_names)}: {device_names}"
                )
            ],
        }

    device_a_name, device_b_name = device_names
    normalized = normalize_pair_data(grouped, device_a_name, device_b_name, profile.checks_enabled)

    result = evaluate_normalized(normalized, profile_name, target_version=target_version)
    result["pair_id"] = pair_id
    return result
