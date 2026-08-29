from __future__ import annotations

from ..models import CheckResult, CommandFailed, CommandMissing, NormalizedPairData
from ..status import Status, worst_of


def check_bgp(normalized: NormalizedPairData, critical_bgp_peers: dict[str, list[str]]) -> CheckResult:
    fail_reasons: list[str] = []
    for host in normalized.hosts():
        if isinstance(host.bgp, CommandFailed):
            fail_reasons.append(f"bgp failed on {host.hostname}: {host.bgp.error}")
        elif isinstance(host.bgp, CommandMissing):
            fail_reasons.append(f"bgp data missing on {host.hostname}")
    if fail_reasons:
        return CheckResult(Status.FAIL, fail_reasons)

    host_statuses: list[Status] = []
    reasons: list[str] = []

    for host in normalized.hosts():
        peers = host.bgp.parsed.peers

        if len(peers) == 0:
            host_statuses.append(Status.FAIL)
            reasons.append(f"no BGP peers found on {host.hostname}, but profile requires BGP")
            continue

        critical = critical_bgp_peers.get(host.hostname)
        if critical is None:
            host_statuses.append(Status.WARNING)
            reasons.append(f"no critical BGP peer list configured for {host.hostname} — informational only")
            not_established = [p.peer for p in peers if not p.established]
            if not_established:
                reasons.append(f"{host.hostname}: peers not Established: {', '.join(not_established)}")
            continue

        peer_by_id = {p.peer: p for p in peers}
        host_fail_reasons = []
        for critical_peer in critical:
            found = peer_by_id.get(critical_peer)
            if found is None:
                host_fail_reasons.append(f"critical BGP peer {critical_peer} not found on {host.hostname}")
            elif not found.established:
                host_fail_reasons.append(f"critical BGP peer {critical_peer} not Established on {host.hostname}")

        if host_fail_reasons:
            host_statuses.append(Status.FAIL)
            reasons.extend(host_fail_reasons)
        else:
            host_statuses.append(Status.PASS)

    return CheckResult(worst_of(host_statuses), reasons)
