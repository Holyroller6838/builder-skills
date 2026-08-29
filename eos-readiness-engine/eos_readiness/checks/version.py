from __future__ import annotations

from ..models import CheckResult, CommandFailed, CommandMissing, NormalizedPairData
from ..status import Status


def check_version(normalized: NormalizedPairData, target_version: str | None) -> CheckResult:
    fail_reasons: list[str] = []
    for host in normalized.hosts():
        if isinstance(host.version, CommandFailed):
            fail_reasons.append(f"version failed on {host.hostname}: {host.version.error}")
        elif isinstance(host.version, CommandMissing):
            fail_reasons.append(f"version data missing on {host.hostname}")

    if fail_reasons:
        return CheckResult(Status.FAIL, fail_reasons)

    if target_version is None:
        return CheckResult(
            Status.WARNING,
            ["no target_version configured — version comparison skipped, informational only"],
        )

    mismatch_reasons: list[str] = []
    for host in normalized.hosts():
        reported = host.version.parsed.version
        if not reported.startswith(target_version):
            mismatch_reasons.append(
                f"{host.hostname} reports version {reported!r}, expected {target_version!r}"
            )

    return CheckResult(Status.FAIL, mismatch_reasons) if mismatch_reasons else CheckResult(Status.PASS)
