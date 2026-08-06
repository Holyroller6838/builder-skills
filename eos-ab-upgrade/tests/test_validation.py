from services.eos_upgrade import validation
from services.eos_upgrade.models import Device, Side
from tests.fixtures.fake_broker import FakeDeviceBrokerClient


def make_devices() -> tuple[Device, Device]:
    device = Device(hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos")
    peer = Device(hostname="leaf-b", management_ip="10.0.0.2", adapter_id="arista-eos")
    return device, peer


def test_validate_side_passes_when_all_checks_clear():
    device, peer = make_devices()
    client = FakeDeviceBrokerClient()
    client.facts[device.hostname] = {"version": "4.31.1", "interfaces_down": 0}
    client.peer_states[device.hostname] = {"healthy": True}

    result = validation.validate_side(client, device, peer, target_version="4.31.1", side=Side.A)

    assert result.passed is True


def test_validate_side_fails_on_version_mismatch():
    device, peer = make_devices()
    client = FakeDeviceBrokerClient()
    client.facts[device.hostname] = {"version": "4.29.2", "interfaces_down": 0}
    client.peer_states[device.hostname] = {"healthy": True}

    result = validation.validate_side(client, device, peer, target_version="4.31.1", side=Side.A)

    assert result.passed is False
    assert result.target_version_confirmed is False


def test_validate_side_checks_peer_version_match_when_requested():
    device, peer = make_devices()
    client = FakeDeviceBrokerClient()
    client.facts[device.hostname] = {"version": "4.31.1", "interfaces_down": 0}
    client.facts[peer.hostname] = {"version": "4.29.2"}
    client.peer_states[device.hostname] = {"healthy": True}

    result = validation.validate_side(
        client, device, peer, target_version="4.31.1", side=Side.B, check_peer_match=True
    )

    assert result.peer_matches is False
    assert result.passed is False
