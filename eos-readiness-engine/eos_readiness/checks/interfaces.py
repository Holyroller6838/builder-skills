from __future__ import annotations

from ..models import CheckResult, CommandFailed, CommandMissing, NormalizedPairData
from ..status import Status, worst_of


def check_interfaces(normalized: NormalizedPairData, critical_interfaces: dict[str, list[str]]) -> CheckResult:
    fail_reasons: list[str] = []
    for host in normalized.hosts():
        if isinstance(host.interfaces, CommandFailed):
            fail_reasons.append(f"interfaces failed on {host.hostname}: {host.interfaces.error}")
        elif isinstance(host.interfaces, CommandMissing):
            fail_reasons.append(f"interfaces data missing on {host.hostname}")
    if fail_reasons:
        return CheckResult(Status.FAIL, fail_reasons)

    host_statuses: list[Status] = []
    reasons: list[str] = []

    for host in normalized.hosts():
        interfaces = host.interfaces.parsed.interfaces

        if len(interfaces) == 0:
            host_statuses.append(Status.FAIL)
            reasons.append(f"no interfaces reported on {host.hostname}")
            continue

        critical = critical_interfaces.get(host.hostname)
        if critical is None:
            host_statuses.append(Status.WARNING)
            reasons.append(
                f"no critical interface list configured for {host.hostname} — informational only"
            )
            down = [i.name for i in interfaces if not i.up]
            if down:
                reasons.append(f"{host.hostname}: interfaces down: {', '.join(down)}")
            continue

        iface_by_name = {i.name: i for i in interfaces}
        host_fail_reasons = []
        for critical_iface in critical:
            found = iface_by_name.get(critical_iface)
            if found is None:
                host_fail_reasons.append(f"critical interface {critical_iface} not found on {host.hostname}")
            elif not found.up:
                host_fail_reasons.append(f"critical interface {critical_iface} is down on {host.hostname}")

        if host_fail_reasons:
            host_statuses.append(Status.FAIL)
            reasons.extend(host_fail_reasons)
        else:
            host_statuses.append(Status.PASS)

    return CheckResult(worst_of(host_statuses), reasons)
