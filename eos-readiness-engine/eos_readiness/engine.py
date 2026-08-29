from __future__ import annotations

from .checks import check_bgp, check_collection, check_interfaces, check_mlag, check_version
from .models import CheckResult, NormalizedPairData
from .profiles import resolve_profile
from .status import Status, worst_of

# evaluate_pair(payload: dict) -> dict — the raw-Itential-payload-facing wrapper
# that will call the (not yet built) raw normalization layer, then this
# function — comes once a real fixture from the lab pair is available. Do not
# add it as a stub here; a stub would imply more completeness than exists.


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
