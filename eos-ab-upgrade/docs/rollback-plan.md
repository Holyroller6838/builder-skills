# Rollback Plan

Implements spec §3 "Rollback (conditional, per side)" and §6 risk "Rollback fails on the side being upgraded."

## Trigger

Rollback for a side runs **only** when that side's Post-Validate phase fails (`ValidationResult.passed == False`). It never runs pre-emptively and never runs for the untouched side.

## Procedure (per side)

1. Stage the side's prior image (`source_version`, captured during Pre-Check) via Device Broker.
2. Activate and reload on the prior image.
3. Wait for the device to come back online within the standard reload timeout.
4. Confirm the returned version matches the prior version.
5. Remove GSHUT from that side (`maintenance.restore_side()`) — a rolled-back device must not be left drained.
6. Record the result as a `RollbackResult` (`restored_version`, `restored_gshut_state`, `escalated`).

Implemented in `services/eos_upgrade/upgrade.py::rollback_side()`.

## Blast radius

| Side mid-upgrade | What gets rolled back | What's left alone |
|---|---|---|
| A | Side A only | Side B (not yet touched) |
| B | Side B only | Side A (already upgraded and validated healthy) |

The pair is never rolled back as a unit — a side that already validated healthy is not undone, per spec §4 "Rollback is per-side, not whole-pair."

## Escalation

If rollback itself fails (the device doesn't return on the prior image, or GSHUT can't be removed), `rollback_side()` sets `RollbackResult.escalated = True` and returns immediately — it does **not** retry indefinitely. The evidence report must reflect the actual confirmed state of both sides, not an assumed one. Escalation in the live workflow means alerting the engineer for console access, per spec §3 Upgrade phase's existing "device doesn't come back" handling.

## What Rollback does not do

- It does not attempt Side B if Side A's rollback fails — the run halts at `Outcome.FAILED` or with `escalated = True` surfaced in the report.
- It does not silently retry a failed reload — repeated reload attempts against a device that isn't coming back risks masking a hardware/console issue behind automation.
- It does not touch the other side's GSHUT state.
