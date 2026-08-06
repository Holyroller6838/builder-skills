from __future__ import annotations

import json

from .models import PairUpgradeReport


def to_dict(report: PairUpgradeReport) -> dict:
    return {
        "pair_id": report.pair.pair_id,
        "target_version": report.target_version,
        "outcome": report.outcome.value,
        "pre_check_passed": report.pre_check_passed,
        "drains": [{**d.__dict__, "side": d.side.value} for d in report.drains],
        "upgrades": [{**u.__dict__, "side": u.side.value} for u in report.upgrades],
        "validations": [{**v.__dict__, "side": v.side.value} for v in report.validations],
        "approval": (
            {
                "approver": report.approval.approver,
                "timestamp": report.approval.timestamp.isoformat(),
                "notes": report.approval.notes,
            }
            if report.approval
            else None
        ),
        "rollbacks": [{**r.__dict__, "side": r.side.value} for r in report.rollbacks],
        "config_diffs": report.config_diffs,
        "started_at": report.started_at.isoformat(),
        "finished_at": report.finished_at.isoformat() if report.finished_at else None,
    }


def to_json(report: PairUpgradeReport, indent: int = 2) -> str:
    return json.dumps(to_dict(report), indent=indent)


def to_markdown(report: PairUpgradeReport) -> str:
    d = to_dict(report)
    lines = [
        f"# Upgrade Evidence Report — {d['pair_id']}",
        "",
        f"**Outcome:** {d['outcome']}",
        f"**Target version:** {d['target_version']}",
        f"**Started:** {d['started_at']}",
        f"**Finished:** {d['finished_at']}",
        "",
        "## Pre-Check",
        f"- Passed: {d['pre_check_passed']}",
        "",
        "## Drain",
    ]
    for drain in d["drains"]:
        lines.append(
            f"- Side {drain['side']}: converged={drain['converged']} "
            f"({drain['route_count_before']} -> {drain['route_count_after']} routes, "
            f"{drain['duration_seconds']}s)"
        )
    lines += ["", "## Upgrade"]
    for up in d["upgrades"]:
        lines.append(
            f"- Side {up['side']}: staged={up['staged']} reloaded={up['reloaded']} "
            f"online={up['came_back_online']} version_confirmed={up['version_confirmed']}"
        )
    lines += ["", "## Validation"]
    for v in d["validations"]:
        lines.append(
            f"- Side {v['side']}: version={v['target_version_confirmed']} "
            f"redundancy={v['redundancy_state_healthy']} "
            f"interfaces={v['interfaces_reestablished']} peer_match={v['peer_matches']}"
        )
    if d["approval"]:
        lines += [
            "",
            "## Approval",
            f"- Approver: {d['approval']['approver']}",
            f"- Timestamp: {d['approval']['timestamp']}",
        ]
    if d["rollbacks"]:
        lines += ["", "## Rollback"]
        for r in d["rollbacks"]:
            lines.append(
                f"- Side {r['side']}: version_restored={r['restored_version']} "
                f"gshut_restored={r['restored_gshut_state']} escalated={r['escalated']}"
            )
    return "\n".join(lines)
