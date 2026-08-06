import pytest

from services.eos_upgrade.device_broker import CollectedFactsDeviceBrokerClient, device_from_record
from services.eos_upgrade.models import Device

WRITE_METHODS = (
    "run_show",
    "push_config",
    "backup_config",
    "stage_image",
    "activate_and_reload",
    "wait_for_online",
    "apply_gshut",
    "remove_gshut",
    "get_route_count",
)


def test_device_from_record_builds_device():
    record = {
        "hostname": "leaf-a",
        "management_ip": "10.0.0.1",
        "adapter_id": "arista-eos",
        "source_version": "4.29.2",
    }

    device = device_from_record(record)

    assert device == Device(
        hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos", source_version="4.29.2"
    )


def test_device_from_record_raises_on_missing_required_field():
    record = {"hostname": "leaf-a", "management_ip": "10.0.0.1"}

    with pytest.raises(ValueError, match="adapter_id"):
        device_from_record(record)


def test_get_facts_and_peer_state_return_collected_data():
    side_a = Device(hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos")
    side_b = Device(hostname="leaf-b", management_ip="10.0.0.2", adapter_id="arista-eos")
    client = CollectedFactsDeviceBrokerClient(
        facts={
            "leaf-a": {"version": "4.31.1"},
            "leaf-b": {"version": "4.29.2"},
        },
        peer_states={
            "leaf-a": {"healthy": True},
            "leaf-b": {"healthy": False},
        },
    )

    assert client.get_facts(side_a) == {"version": "4.31.1"}
    assert client.get_peer_state(side_a, side_b) == {"healthy": True}


def test_get_facts_indexed_by_hostname_when_called_with_the_peer():
    # precheck.check_gshut_eligibility() calls get_facts() on the *peer* device,
    # not just "the device being checked" — this must resolve to the peer's own data.
    side_a = Device(hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos")
    side_b = Device(hostname="leaf-b", management_ip="10.0.0.2", adapter_id="arista-eos")
    client = CollectedFactsDeviceBrokerClient(
        facts={
            "leaf-a": {"interface_capacity_headroom_pct": 100},
            "leaf-b": {"interface_capacity_headroom_pct": 60},
        },
        peer_states={},
    )

    assert client.get_facts(side_b) == {"interface_capacity_headroom_pct": 60}
    assert client.get_facts(side_a) == {"interface_capacity_headroom_pct": 100}


@pytest.mark.parametrize("method_name", WRITE_METHODS)
def test_write_methods_raise_not_implemented(method_name):
    device = Device(hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos")
    client = CollectedFactsDeviceBrokerClient(facts={}, peer_states={})
    method = getattr(client, method_name)

    with pytest.raises(NotImplementedError):
        if method_name == "run_show":
            method(device, "show version")
        elif method_name == "push_config":
            method(device, "some config")
        elif method_name == "stage_image":
            method(device, "eos-4.31.1.swi")
        elif method_name == "wait_for_online":
            method(device, timeout=60)
        else:
            method(device)
