from __future__ import annotations

from .models import Device

REQUIRED_DEVICE_FIELDS = ("hostname", "management_ip", "adapter_id")


def device_from_record(record: dict) -> Device:
    # Our own payload contract, not a mapping of Itential's real device schema — see docs/device-broker-map.md
    missing = [f for f in REQUIRED_DEVICE_FIELDS if not record.get(f)]
    if missing:
        raise ValueError(f"device record missing required field(s): {missing}")
    return Device(
        hostname=record["hostname"],
        management_ip=record["management_ip"],
        adapter_id=record["adapter_id"],
        source_version=record.get("source_version"),
    )


class CollectedFactsDeviceBrokerClient:
    # Built from pre-collected data (push model), not live calls — see docs/architecture.md
    def __init__(self, facts: dict[str, dict], peer_states: dict[str, dict]):
        self._facts = facts
        self._peer_states = peer_states

    def get_facts(self, device: Device) -> dict:
        return self._facts.get(device.hostname, {})

    def get_peer_state(self, device: Device, peer: Device) -> dict:
        return self._peer_states.get(device.hostname, {})

    def run_show(self, device: Device, command: str) -> str:
        raise NotImplementedError("run_show is not available in MVP1 read-only mode")

    def push_config(self, device: Device, config: str) -> None:
        raise NotImplementedError("push_config is not available in MVP1 read-only mode")

    def backup_config(self, device: Device) -> str:
        raise NotImplementedError("backup_config is not available in MVP1 read-only mode")

    def stage_image(self, device: Device, image_filename: str) -> bool:
        raise NotImplementedError("stage_image is not available in MVP1 read-only mode")

    def activate_and_reload(self, device: Device) -> bool:
        raise NotImplementedError("activate_and_reload is not available in MVP1 read-only mode")

    def wait_for_online(self, device: Device, timeout: int) -> bool:
        raise NotImplementedError("wait_for_online is not available in MVP1 read-only mode")

    def apply_gshut(self, device: Device) -> None:
        raise NotImplementedError("apply_gshut is not available in MVP1 read-only mode")

    def remove_gshut(self, device: Device) -> None:
        raise NotImplementedError("remove_gshut is not available in MVP1 read-only mode")

    def get_route_count(self, device: Device) -> int:
        raise NotImplementedError("get_route_count is not available in MVP1 read-only mode")
