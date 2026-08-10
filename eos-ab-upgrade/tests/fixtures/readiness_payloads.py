DEVICE = {
    "hostname": "lab-leaf-a",
    "management_ip": "10.10.10.1",
    "adapter_id": "arista-eos-lab",
    "source_version": "4.29.2",
}

CONNECTIVITY_UP = {"reachable": True}
CONNECTIVITY_DOWN = {"reachable": False}

FACTS_SUPPORTED_VERSION = {"version": "4.31.1"}
FACTS_UNSUPPORTED_VERSION = {"version": "4.20.9"}

MLAG_HEALTHY = {"healthy": True}
MLAG_UNHEALTHY = {"healthy": False}

BGP_SUMMARY_SAMPLE = {"established_peers": 4, "total_peers": 4}

INTERFACES_CLEAN = {"down_count": 0}
INTERFACES_DEGRADED = {"down_count": 2}

PASSING_PAYLOAD = {
    "device": DEVICE,
    "target_version": "4.31.1",
    "connectivity": CONNECTIVITY_UP,
    "facts": FACTS_SUPPORTED_VERSION,
    "mlag_status": MLAG_HEALTHY,
    "bgp_summary": BGP_SUMMARY_SAMPLE,
    "interfaces": INTERFACES_CLEAN,
}


def payload_with(**overrides) -> dict:
    payload = {k: dict(v) if isinstance(v, dict) else v for k, v in PASSING_PAYLOAD.items()}
    payload.update(overrides)
    return payload
