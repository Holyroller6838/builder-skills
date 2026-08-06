from services.eos_upgrade import precheck
from services.eos_upgrade.models import Device, RedundantPair
from tests.fixtures.fake_broker import FakeDeviceBrokerClient


def make_pair() -> RedundantPair:
    side_a = Device(hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos", source_version="4.29.2")
    side_b = Device(hostname="leaf-b", management_ip="10.0.0.2", adapter_id="arista-eos", source_version="4.29.2")
    return RedundantPair(pair_id="pair-01", side_a=side_a, side_b=side_b, redundancy_type="mlag")


def test_run_pre_check_passes_when_all_checks_pass():
    pair = make_pair()
    client = FakeDeviceBrokerClient()
    for device in (pair.side_a, pair.side_b):
        client.facts[device.hostname] = {"version": "4.29.2", "interface_capacity_headroom_pct": 100}
        client.peer_states[device.hostname] = {"healthy": True}

    passed, details = precheck.run_pre_check(client, pair, target_version="4.31.1")

    assert passed is True
    assert details["side_a_reachable"] is True
    assert "backups" in details


def test_run_pre_check_fails_on_unhealthy_redundancy():
    pair = make_pair()
    client = FakeDeviceBrokerClient()
    for device in (pair.side_a, pair.side_b):
        client.facts[device.hostname] = {"version": "4.29.2", "interface_capacity_headroom_pct": 100}
    client.peer_states[pair.side_a.hostname] = {"healthy": False}
    client.peer_states[pair.side_b.hostname] = {"healthy": True}

    passed, details = precheck.run_pre_check(client, pair, target_version="4.31.1")

    assert passed is False
    assert "backups" not in details


def test_check_gshut_eligibility_requires_full_headroom():
    pair = make_pair()
    client = FakeDeviceBrokerClient()
    client.facts[pair.side_b.hostname] = {"interface_capacity_headroom_pct": 60}

    assert precheck.check_gshut_eligibility(client, pair.side_a, pair.side_b) is False
