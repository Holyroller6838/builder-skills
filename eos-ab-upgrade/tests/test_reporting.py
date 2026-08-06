import json
from datetime import datetime, timezone

from services.eos_upgrade import reporting
from services.eos_upgrade.models import (
    ApprovalRecord,
    Device,
    DrainResult,
    Outcome,
    PairUpgradeReport,
    RedundantPair,
    Side,
    UpgradeResult,
    ValidationResult,
)


def make_report() -> PairUpgradeReport:
    side_a = Device(hostname="leaf-a", management_ip="10.0.0.1", adapter_id="arista-eos", source_version="4.29.2")
    side_b = Device(hostname="leaf-b", management_ip="10.0.0.2", adapter_id="arista-eos", source_version="4.29.2")
    pair = RedundantPair(pair_id="pair-01", side_a=side_a, side_b=side_b, redundancy_type="mlag")

    report = PairUpgradeReport(
        pair=pair,
        target_version="4.31.1",
        outcome=Outcome.COMPLETE,
        pre_check_passed=True,
        started_at=datetime(2026, 8, 6, 2, 0, 0, tzinfo=timezone.utc),
        finished_at=datetime(2026, 8, 6, 2, 45, 0, tzinfo=timezone.utc),
    )
    report.drains.append(
        DrainResult(side=Side.A, converged=True, route_count_before=1000, route_count_after=10, duration_seconds=25)
    )
    report.upgrades.append(
        UpgradeResult(
            side=Side.A, staged=True, reloaded=True, version_confirmed=True, came_back_online=True, duration_seconds=310
        )
    )
    report.validations.append(
        ValidationResult(
            side=Side.A, target_version_confirmed=True, redundancy_state_healthy=True, interfaces_reestablished=True
        )
    )
    report.approval = ApprovalRecord(approver="jdoe", timestamp=datetime(2026, 8, 6, 2, 20, 0, tzinfo=timezone.utc))
    return report


def test_to_dict_serializes_enums_to_values():
    report = make_report()

    d = reporting.to_dict(report)

    assert d["outcome"] == "complete"
    assert d["drains"][0]["side"] == "A"
    assert d["approval"]["approver"] == "jdoe"


def test_to_json_round_trips_through_json_loads():
    report = make_report()

    parsed = json.loads(reporting.to_json(report))

    assert parsed["pair_id"] == "pair-01"


def test_to_markdown_includes_key_sections():
    report = make_report()

    md = reporting.to_markdown(report)

    assert "# Upgrade Evidence Report" in md
    assert "## Approval" in md
    assert "jdoe" in md
