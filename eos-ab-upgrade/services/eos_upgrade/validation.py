from __future__ import annotations

from .models import Device, DeviceBrokerClient, Side, ValidationResult


def confirm_target_version(client: DeviceBrokerClient, device: Device, target_version: str) -> bool:
    return client.get_facts(device).get("version", "").startswith(target_version)


def confirm_redundancy_healthy(client: DeviceBrokerClient, device: Device, peer: Device) -> bool:
    return client.get_peer_state(device, peer).get("healthy", False)


def confirm_interfaces_reestablished(client: DeviceBrokerClient, device: Device) -> bool:
    return client.get_facts(device).get("interfaces_down", 1) == 0


def confirm_pair_versions_match(client: DeviceBrokerClient, side_a: Device, side_b: Device) -> bool:
    return client.get_facts(side_a).get("version") == client.get_facts(side_b).get("version")


def validate_side(
    client: DeviceBrokerClient,
    device: Device,
    peer: Device,
    target_version: str,
    side: Side,
    check_peer_match: bool = False,
) -> ValidationResult:
    peer_matches = confirm_pair_versions_match(client, device, peer) if check_peer_match else None
    return ValidationResult(
        side=side,
        target_version_confirmed=confirm_target_version(client, device, target_version),
        redundancy_state_healthy=confirm_redundancy_healthy(client, device, peer),
        interfaces_reestablished=confirm_interfaces_reestablished(client, device),
        peer_matches=peer_matches,
    )
