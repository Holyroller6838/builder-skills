from __future__ import annotations

from ..models import CheckResult, CommandFailed, CommandMissing, NormalizedPairData
from ..status import Status

# Normalized state vocabulary owned by this check, not derived from any real
# EOS/CVP payload field. The (deferred) raw normalization layer is responsible
# for mapping real device output onto these two known values; anything else
# it produces is treated as ambiguous.
STATE_ACTIVE = "active"
STATE_DISABLED = "disabled"


def check_mlag(normalized: NormalizedPairData) -> CheckResult:
    fail_reasons: list[str] = []
    for host in normalized.hosts():
        if isinstance(host.mlag, CommandFailed):
            fail_reasons.append(f"mlag failed on {host.hostname}: {host.mlag.error}")
        elif isinstance(host.mlag, CommandMissing):
            fail_reasons.append(f"mlag data missing on {host.hostname}")

    if fail_reasons:
        return CheckResult(Status.FAIL, fail_reasons)

    device_a, device_b = normalized.device_a, normalized.device_b
    state_a = device_a.mlag.parsed.state
    state_b = device_b.mlag.parsed.state

    disabled_reasons = []
    if state_a == STATE_DISABLED:
        disabled_reasons.append(f"MLAG required by profile but reported disabled on {device_a.hostname}")
    if state_b == STATE_DISABLED:
        disabled_reasons.append(f"MLAG required by profile but reported disabled on {device_b.hostname}")
    if disabled_reasons:
        return CheckResult(Status.FAIL, disabled_reasons)

    if state_a == STATE_ACTIVE and state_b == STATE_ACTIVE:
        return CheckResult(Status.PASS)

    if state_a != state_b:
        return CheckResult(
            Status.WARNING,
            [f"MLAG state disagreement between hosts: {device_a.hostname}={state_a}, {device_b.hostname}={state_b}"],
        )

    return CheckResult(Status.WARNING, [f"ambiguous MLAG state reported by both hosts: {state_a!r}"])
