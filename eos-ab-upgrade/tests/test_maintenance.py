from services.eos_upgrade import maintenance
from services.eos_upgrade.models import Device, Side
from tests.fixtures.fake_broker import FakeDeviceBrokerClient


def make_device() -> Device:
    return Device(hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos")


def test_wait_for_drain_convergence_detects_convergence(monkeypatch):
    monkeypatch.setattr(maintenance.time, "sleep", lambda s: None)
    device = make_device()
    client = FakeDeviceBrokerClient()
    client.route_counts[device.hostname] = [1000, 1000, 40]

    result = maintenance.wait_for_drain_convergence(
        client, device, Side.A, timeout_seconds=60, poll_interval_seconds=5
    )

    assert result.converged is True
    assert result.timed_out is False


def test_wait_for_drain_convergence_times_out(monkeypatch):
    monkeypatch.setattr(maintenance.time, "sleep", lambda s: None)
    device = make_device()
    client = FakeDeviceBrokerClient()
    client.route_counts[device.hostname] = 1000

    result = maintenance.wait_for_drain_convergence(
        client, device, Side.A, timeout_seconds=10, poll_interval_seconds=5
    )

    assert result.converged is False
    assert result.timed_out is True


def test_drain_side_applies_gshut_before_polling(monkeypatch):
    monkeypatch.setattr(maintenance.time, "sleep", lambda s: None)
    device = make_device()
    client = FakeDeviceBrokerClient()
    client.route_counts[device.hostname] = [1000, 20]

    maintenance.drain_side(client, device, Side.A, timeout_seconds=60)

    assert client.gshut_applied[device.hostname] is True


def test_restore_side_removes_gshut():
    device = make_device()
    client = FakeDeviceBrokerClient()
    client.gshut_applied[device.hostname] = True

    maintenance.restore_side(client, device)

    assert client.gshut_applied[device.hostname] is False
