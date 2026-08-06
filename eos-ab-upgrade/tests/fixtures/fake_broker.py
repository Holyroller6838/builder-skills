from __future__ import annotations

from services.eos_upgrade.models import Device


class FakeDeviceBrokerClient:
    def __init__(self):
        self.facts: dict[str, dict] = {}
        self.route_counts: dict[str, int | list[int]] = {}
        self.peer_states: dict[str, dict] = {}
        self.online: dict[str, bool] = {}
        self.gshut_applied: dict[str, bool] = {}
        self.backups: dict[str, str] = {}

    def get_facts(self, device: Device) -> dict:
        return self.facts.get(device.hostname, {})

    def run_show(self, device: Device, command: str) -> str:
        return ""

    def push_config(self, device: Device, config: str) -> None:
        pass

    def backup_config(self, device: Device) -> str:
        backup_id = f"backup-{device.hostname}"
        self.backups[device.hostname] = backup_id
        return backup_id

    def stage_image(self, device: Device, image_filename: str) -> bool:
        return True

    def activate_and_reload(self, device: Device) -> bool:
        return True

    def wait_for_online(self, device: Device, timeout: int) -> bool:
        return self.online.get(device.hostname, True)

    def apply_gshut(self, device: Device) -> None:
        self.gshut_applied[device.hostname] = True

    def remove_gshut(self, device: Device) -> None:
        self.gshut_applied[device.hostname] = False

    def get_route_count(self, device: Device) -> int:
        seq = self.route_counts.get(device.hostname)
        if isinstance(seq, list):
            return seq.pop(0) if len(seq) > 1 else seq[0]
        return seq or 0

    def get_peer_state(self, device: Device, peer: Device) -> dict:
        return self.peer_states.get(device.hostname, {"healthy": True})
