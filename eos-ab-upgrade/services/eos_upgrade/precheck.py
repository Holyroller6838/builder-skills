from __future__ import annotations

from .models import Device, DeviceBrokerClient, RedundantPair

SUPPORTED_SOURCE_VERSIONS = {"4.28", "4.29", "4.30", "4.31"}
FULL_HEADROOM_PCT = 100


def check_reachable(client: DeviceBrokerClient, device: Device) -> bool:
    return bool(client.get_facts(device))


def check_source_version(
    client: DeviceBrokerClient, device: Device, supported: set[str] = SUPPORTED_SOURCE_VERSIONS
) -> bool:
    version = client.get_facts(device).get("version", "")
    return any(version.startswith(v) for v in supported)


def check_redundancy_healthy(client: DeviceBrokerClient, pair: RedundantPair) -> bool:
    state_a = client.get_peer_state(pair.side_a, pair.side_b)
    state_b = client.get_peer_state(pair.side_b, pair.side_a)
    return state_a.get("healthy", False) and state_b.get("healthy", False)


def check_gshut_eligibility(client: DeviceBrokerClient, side: Device, peer: Device) -> bool:
    peer_facts = client.get_facts(peer)
    return peer_facts.get("interface_capacity_headroom_pct", 0) >= FULL_HEADROOM_PCT


def backup_pair(client: DeviceBrokerClient, pair: RedundantPair) -> dict[str, str]:
    return {
        pair.side_a.hostname: client.backup_config(pair.side_a),
        pair.side_b.hostname: client.backup_config(pair.side_b),
    }


def run_pre_check(client: DeviceBrokerClient, pair: RedundantPair, target_version: str) -> tuple[bool, dict]:
    results = {
        "side_a_reachable": check_reachable(client, pair.side_a),
        "side_b_reachable": check_reachable(client, pair.side_b),
        "side_a_source_version_supported": check_source_version(client, pair.side_a),
        "side_b_source_version_supported": check_source_version(client, pair.side_b),
        "redundancy_healthy": check_redundancy_healthy(client, pair),
        "side_a_gshut_eligible": check_gshut_eligibility(client, pair.side_a, pair.side_b),
        "side_b_gshut_eligible": check_gshut_eligibility(client, pair.side_b, pair.side_a),
    }
    passed = all(results.values())
    if passed:
        results["backups"] = backup_pair(client, pair)
    return passed, results
