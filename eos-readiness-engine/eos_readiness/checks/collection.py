from __future__ import annotations

from ..models import CheckResult, CommandFailed, CommandMissing, CommandOutcome, NormalizedPairData
from ..status import Status

ALWAYS_REQUIRED = ("version", "interfaces")
OPTIONAL_BY_PROFILE = ("mlag", "bgp")


def _describe_failure(outcome: CommandOutcome, check_name: str, hostname: str) -> str | None:
    if isinstance(outcome, CommandFailed):
        return f"{check_name} failed on {hostname}: {outcome.error}"
    if isinstance(outcome, CommandMissing):
        return f"{check_name} data missing on {hostname}"
    return None


def check_collection(normalized: NormalizedPairData, required_checks: frozenset[str]) -> CheckResult:
    reasons: list[str] = []
    for host in normalized.hosts():
        for check_name in ALWAYS_REQUIRED:
            reason = _describe_failure(getattr(host, check_name), check_name, host.hostname)
            if reason:
                reasons.append(reason)
        for check_name in OPTIONAL_BY_PROFILE:
            if check_name not in required_checks:
                continue
            reason = _describe_failure(getattr(host, check_name), check_name, host.hostname)
            if reason:
                reasons.append(reason)

    return CheckResult(Status.FAIL, reasons) if reasons else CheckResult(Status.PASS)
