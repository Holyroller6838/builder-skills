from __future__ import annotations

import time

from .models import Device, DeviceBrokerClient, DrainResult, Side

DEFAULT_POLL_INTERVAL_SECONDS = 5
DEFAULT_DRAIN_TIMEOUT_SECONDS = 300
CONVERGENCE_ROUTE_THRESHOLD_PCT = 0.95


def apply_gshut(client: DeviceBrokerClient, device: Device) -> None:
    client.apply_gshut(device)


def remove_gshut(client: DeviceBrokerClient, device: Device) -> None:
    client.remove_gshut(device)


def wait_for_drain_convergence(
    client: DeviceBrokerClient,
    device: Device,
    side: Side,
    timeout_seconds: int = DEFAULT_DRAIN_TIMEOUT_SECONDS,
    poll_interval_seconds: int = DEFAULT_POLL_INTERVAL_SECONDS,
) -> DrainResult:
    route_count_before = client.get_route_count(device)
    drop_threshold = route_count_before * (1 - CONVERGENCE_ROUTE_THRESHOLD_PCT)
    elapsed = 0
    while elapsed < timeout_seconds:
        route_count_now = client.get_route_count(device)
        if route_count_before == 0 or route_count_now <= drop_threshold:
            return DrainResult(
                side=side,
                converged=True,
                route_count_before=route_count_before,
                route_count_after=route_count_now,
                duration_seconds=elapsed,
            )
        time.sleep(poll_interval_seconds)
        elapsed += poll_interval_seconds
    return DrainResult(
        side=side,
        converged=False,
        route_count_before=route_count_before,
        route_count_after=client.get_route_count(device),
        duration_seconds=elapsed,
        timed_out=True,
    )


def drain_side(
    client: DeviceBrokerClient,
    device: Device,
    side: Side,
    timeout_seconds: int = DEFAULT_DRAIN_TIMEOUT_SECONDS,
) -> DrainResult:
    apply_gshut(client, device)
    return wait_for_drain_convergence(client, device, side, timeout_seconds=timeout_seconds)


def restore_side(client: DeviceBrokerClient, device: Device) -> None:
    remove_gshut(client, device)
