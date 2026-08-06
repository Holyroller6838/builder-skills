from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Protocol


class Side(str, Enum):
    A = "A"
    B = "B"


class Outcome(str, Enum):
    COMPLETE = "complete"
    ROLLED_BACK = "rolled_back"
    HALTED_AWAITING_APPROVAL = "halted_awaiting_approval"
    FAILED = "failed"


@dataclass
class Device:
    hostname: str
    management_ip: str
    adapter_id: str
    source_version: str | None = None


@dataclass
class RedundantPair:
    pair_id: str
    side_a: Device
    side_b: Device
    redundancy_type: str


class DeviceBrokerClient(Protocol):
    def get_facts(self, device: Device) -> dict: ...
    def run_show(self, device: Device, command: str) -> str: ...
    def push_config(self, device: Device, config: str) -> None: ...
    def backup_config(self, device: Device) -> str: ...
    def stage_image(self, device: Device, image_filename: str) -> bool: ...
    def activate_and_reload(self, device: Device) -> bool: ...
    def wait_for_online(self, device: Device, timeout: int) -> bool: ...
    def apply_gshut(self, device: Device) -> None: ...
    def remove_gshut(self, device: Device) -> None: ...
    def get_route_count(self, device: Device) -> int: ...
    def get_peer_state(self, device: Device, peer: Device) -> dict: ...


@dataclass
class DrainResult:
    side: Side
    converged: bool
    route_count_before: int
    route_count_after: int
    duration_seconds: float
    timed_out: bool = False


@dataclass
class UpgradeResult:
    side: Side
    staged: bool
    reloaded: bool
    version_confirmed: bool
    came_back_online: bool
    duration_seconds: float


@dataclass
class ValidationResult:
    side: Side
    target_version_confirmed: bool
    redundancy_state_healthy: bool
    interfaces_reestablished: bool
    peer_matches: bool | None = None

    @property
    def passed(self) -> bool:
        checks = [
            self.target_version_confirmed,
            self.redundancy_state_healthy,
            self.interfaces_reestablished,
        ]
        if self.peer_matches is not None:
            checks.append(self.peer_matches)
        return all(checks)


@dataclass
class ApprovalRecord:
    approver: str
    timestamp: datetime
    notes: str = ""


@dataclass
class RollbackResult:
    side: Side
    restored_version: bool
    restored_gshut_state: bool
    escalated: bool = False


@dataclass
class PairUpgradeReport:
    pair: RedundantPair
    target_version: str
    outcome: Outcome
    pre_check_passed: bool
    drains: list[DrainResult] = field(default_factory=list)
    upgrades: list[UpgradeResult] = field(default_factory=list)
    validations: list[ValidationResult] = field(default_factory=list)
    approval: ApprovalRecord | None = None
    rollbacks: list[RollbackResult] = field(default_factory=list)
    config_diffs: dict[str, str] = field(default_factory=dict)
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    finished_at: datetime | None = None
