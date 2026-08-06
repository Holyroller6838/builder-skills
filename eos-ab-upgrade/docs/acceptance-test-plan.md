# Acceptance Test Plan

Derived from `specs/spec-arista-eos-ab-upgrade.md` §9. Each criterion below becomes a test case at the Test stage (`/qa-agent`). "Static" cases are covered today by `tests/` against `FakeDeviceBrokerClient`; "Live" cases require a real platform connection and lab devices and are drafted here for `/qa-agent` to execute against the built workflows.

| # | Acceptance Criterion | Test Layer | Covered by |
|---|---|---|---|
| 1 | Side B upgrade never starts until Side A post-validation passes **and** operator approval is recorded | Static + Live | `tests/test_reporting.py` (report shape), live: orchestrator halts at Approval Gate with no auto-proceed |
| 2 | GSHUT drain is confirmed (route/neighbor convergence) before either side is reloaded | Static + Live | `tests/test_maintenance.py::test_wait_for_drain_convergence_detects_convergence`, `..._times_out` |
| 3 | Each side runs the target EOS version after its upgrade | Static + Live | `tests/test_validation.py::test_validate_side_passes_when_all_checks_clear` |
| 4 | Peer/MLAG redundancy state is healthy and matches expected state after each side's post-validation | Static + Live | `tests/test_validation.py::test_validate_side_checks_peer_version_match_when_requested` |
| 5 | Config backup exists before and after each side's upgrade; diff shows only expected changes | Live only | Requires live Configuration Manager backup/diff — no static equivalent |
| 6 | Restore (un-GSHUT) is executed and confirmed on both sides before the run is marked complete | Static + Live | `tests/test_maintenance.py::test_restore_side_removes_gshut`; live: orchestrator's unconditional Restore phase |
| 7 | Rollback restores the affected side to its prior version and prior GSHUT/routing state on post-validation failure, without touching the other side | Static + Live | `services/eos_upgrade/upgrade.py::rollback_side()` unit coverage (add `test_upgrade.py` at Build time once orchestrator wiring is final); live: induced failure on one side only |
| 8 | Evidence report is generated for every run — complete, rolled back, or halted awaiting approval | Static | `tests/test_reporting.py` (all three `Outcome` values serialize correctly) |
| 9 | Operator approval event is captured with approver identity and timestamp in the evidence report | Static | `tests/test_reporting.py::test_to_dict_serializes_enums_to_values` (approval block) |
| 10 | Batch runs respect the configured pair concurrency and failure-rate threshold across multiple pairs | Live only | Out of scope for `services/eos_upgrade` (single-pair logic) — validated at the batch-orchestration layer once Batch Strategy (spec §8) is implemented |

## Live test prerequisites

- Lab pair of Arista EOS devices in a real MLAG or dual-homed topology, with GSHUT policy already configured on both (per Discovery Question 2)
- Target image staged in the configured image repository
- A test engineer available to act as approver for the Approval Gate
- Non-critical maintenance window — Post-Validate and Rollback tests intentionally exercise a reload cycle

## Failure-injection cases (for Rollback coverage)

| Scenario | Expected outcome |
|---|---|
| Side A reload succeeds but lands on the wrong version | Post-Validate A fails → Rollback A only → `Outcome.ROLLED_BACK`, Side B never touched |
| Side A validates clean, Side B fails post-validation | Rollback B only → Side A remains on target version, untouched |
| Rollback itself fails (device doesn't return on prior image) | `RollbackResult.escalated = True`, no retry loop, evidence report reflects actual current state of both sides |
