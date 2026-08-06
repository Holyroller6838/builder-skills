# Python Action Map

Maps each `services/eos_upgrade` module to the workflow phase(s) that invoke it as a Python Action, and what it returns.

| Module | Function(s) | Invoked from | Phase | Returns |
|---|---|---|---|---|
| `precheck.py` | `run_pre_check()` | `eos-precheck.json` | Pre-Check | `(passed: bool, details: dict)` — reachability, source version, redundancy health, GSHUT eligibility, backup IDs |
| `maintenance.py` | `drain_side()`, `restore_side()` | `eos-upgrade-single-device.json`, `eos-upgrade-orchestrator.json` | GSHUT Drain (A/B), Restore | `DrainResult` (converged, route counts, duration, timed_out) |
| `upgrade.py` | `stage_and_reload()`, `rollback_side()`, `upgrade_one_side()` | `eos-upgrade-single-device.json`, `eos-upgrade-orchestrator.json` | Upgrade (A/B), Rollback | `UpgradeResult` / `RollbackResult` |
| `validation.py` | `validate_side()` | `eos-postcheck.json` | Post-Validate (A/B) | `ValidationResult` (version, redundancy, interfaces, peer match, `.passed`) |
| `reporting.py` | `to_dict()`, `to_json()`, `to_markdown()` | `eos-upgrade-orchestrator.json` | Reporting / Close Out | Serialized evidence report |
| `upgrade.py` | `run_pair_upgrade()` | — (not called from a workflow) | — | Full-pair orchestration in pure Python — reference implementation of the orchestrator's control flow, used for local dry runs and as the spec the orchestrator workflow is built against. Not itself a Python Action; the workflow re-implements this control flow as a task graph so the Approval Gate can actually pause for a human. |

## Interface contract

Every function above takes a `DeviceBrokerClient` as its first argument (see `docs/device-broker-map.md`). The Python Action task wraps a concrete implementation of that interface — built against the live platform's Device Broker — and passes it in. None of `services/eos_upgrade`'s business logic changes when the underlying adapter changes; only the `DeviceBrokerClient` implementation does.

## Testing without a platform connection

`tests/fixtures/fake_broker.py` provides an in-memory `FakeDeviceBrokerClient` so every function in this map is unit-tested (see `tests/test_precheck.py`, `test_maintenance.py`, `test_validation.py`, `test_reporting.py`) without a live platform. This is what `docs/acceptance-test-plan.md` calls the "static" test layer — acceptance tests still require the live platform and real devices.
