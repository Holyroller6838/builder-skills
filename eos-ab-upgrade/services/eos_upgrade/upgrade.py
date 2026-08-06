from __future__ import annotations

import time
from collections.abc import Callable
from datetime import datetime, timezone

from . import maintenance, precheck, validation
from .models import (
    ApprovalRecord,
    Device,
    DeviceBrokerClient,
    Outcome,
    PairUpgradeReport,
    RedundantPair,
    RollbackResult,
    Side,
    UpgradeResult,
)

DEFAULT_RELOAD_TIMEOUT_SECONDS = 900


class UpgradeAborted(Exception):
    pass


def stage_and_reload(
    client: DeviceBrokerClient,
    device: Device,
    side: Side,
    image_filename: str,
    reload_timeout_seconds: int = DEFAULT_RELOAD_TIMEOUT_SECONDS,
) -> UpgradeResult:
    start = time.monotonic()
    staged = client.stage_image(device, image_filename)
    reloaded = client.activate_and_reload(device)
    came_back = client.wait_for_online(device, timeout=reload_timeout_seconds)
    facts = client.get_facts(device) if came_back else {}
    return UpgradeResult(
        side=side,
        staged=staged,
        reloaded=reloaded,
        version_confirmed=bool(facts.get("version")),
        came_back_online=came_back,
        duration_seconds=time.monotonic() - start,
    )


def rollback_side(client: DeviceBrokerClient, device: Device, side: Side, prior_version: str) -> RollbackResult:
    try:
        client.stage_image(device, f"{prior_version}.swi")
        client.activate_and_reload(device)
        came_back = client.wait_for_online(device, timeout=DEFAULT_RELOAD_TIMEOUT_SECONDS)
        facts = client.get_facts(device) if came_back else {}
        restored_version = facts.get("version", "").startswith(prior_version)
        maintenance.restore_side(client, device)
        return RollbackResult(side=side, restored_version=restored_version, restored_gshut_state=True)
    except Exception:  # noqa: BLE001 -- any device-broker failure during rollback must escalate, not crash
        return RollbackResult(side=side, restored_version=False, restored_gshut_state=False, escalated=True)


def upgrade_one_side(
    client: DeviceBrokerClient,
    device: Device,
    peer: Device,
    side: Side,
    target_version: str,
    image_filename: str,
    check_peer_match: bool = False,
) -> tuple[UpgradeResult, validation.ValidationResult]:
    drain = maintenance.drain_side(client, device, side)
    if not drain.converged:
        raise UpgradeAborted(f"GSHUT drain did not converge on side {side.value}")

    upgrade_result = stage_and_reload(client, device, side, image_filename)
    if not upgrade_result.came_back_online:
        raise UpgradeAborted(f"Side {side.value} did not come back online after reload")

    result = validation.validate_side(
        client, device, peer, target_version, side, check_peer_match=check_peer_match
    )
    return upgrade_result, result


def run_pair_upgrade(
    client: DeviceBrokerClient,
    pair: RedundantPair,
    target_version: str,
    image_filename: str,
    approve_side_b: Callable[[PairUpgradeReport], ApprovalRecord | None],
) -> PairUpgradeReport:
    report = PairUpgradeReport(
        pair=pair, target_version=target_version, outcome=Outcome.FAILED, pre_check_passed=False
    )

    passed, pre_check_details = precheck.run_pre_check(client, pair, target_version)
    report.pre_check_passed = passed
    report.config_diffs.update(pre_check_details.get("backups", {}))
    if not passed:
        report.outcome = Outcome.HALTED_AWAITING_APPROVAL
        report.finished_at = datetime.now(timezone.utc)
        return report

    try:
        upgrade_a, validate_a = upgrade_one_side(
            client, pair.side_a, pair.side_b, Side.A, target_version, image_filename
        )
        report.upgrades.append(upgrade_a)
        report.validations.append(validate_a)
        if not validate_a.passed:
            report.rollbacks.append(rollback_side(client, pair.side_a, Side.A, pair.side_a.source_version or ""))
            report.outcome = Outcome.ROLLED_BACK
            report.finished_at = datetime.now(timezone.utc)
            return report
    except UpgradeAborted:
        report.outcome = Outcome.FAILED
        report.finished_at = datetime.now(timezone.utc)
        return report

    approval = approve_side_b(report)
    report.approval = approval
    if approval is None:
        report.outcome = Outcome.HALTED_AWAITING_APPROVAL
        report.finished_at = datetime.now(timezone.utc)
        return report

    try:
        upgrade_b, validate_b = upgrade_one_side(
            client, pair.side_b, pair.side_a, Side.B, target_version, image_filename, check_peer_match=True
        )
        report.upgrades.append(upgrade_b)
        report.validations.append(validate_b)
        if not validate_b.passed:
            report.rollbacks.append(rollback_side(client, pair.side_b, Side.B, pair.side_b.source_version or ""))
            report.outcome = Outcome.ROLLED_BACK
            report.finished_at = datetime.now(timezone.utc)
            return report
    except UpgradeAborted:
        report.outcome = Outcome.FAILED
        report.finished_at = datetime.now(timezone.utc)
        return report

    maintenance.restore_side(client, pair.side_a)
    maintenance.restore_side(client, pair.side_b)
    report.outcome = Outcome.COMPLETE
    report.finished_at = datetime.now(timezone.utc)
    return report
