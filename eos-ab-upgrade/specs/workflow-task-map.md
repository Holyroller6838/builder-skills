# Workflow → Service Map

Maps each phase of the spec ([`spec-arista-eos-ab-upgrade.md`](spec-arista-eos-ab-upgrade.md) §3) to the workflow that implements it and the `services/eos_upgrade` module backing its logic. This is the top-level index; see `docs/itential-task-map.md` for platform task detail and `docs/python-action-map.md` for service-module detail.

| Spec Phase | Workflow | Service Module | Notes |
|---|---|---|---|
| Pre-Check | `workflows/eos-precheck.json` | `precheck.py` | Called once per pair, before either side is touched |
| GSHUT Drain — Side A | `workflows/eos-upgrade-single-device.json` (side=A) | `maintenance.py` | `drain_side()` |
| Upgrade — Side A | `workflows/eos-upgrade-single-device.json` (side=A) | `upgrade.py` | `stage_and_reload()` |
| Post-Validate — Side A | `workflows/eos-postcheck.json` (side=A) | `validation.py` | `validate_side()`, `check_peer_match=False` |
| Approval Gate | `workflows/eos-upgrade-orchestrator.json` | — | Manual/approval task inside the orchestrator; no service logic, just a pause + record capture |
| GSHUT Drain — Side B | `workflows/eos-upgrade-single-device.json` (side=B) | `maintenance.py` | Same function, opposite side |
| Upgrade — Side B | `workflows/eos-upgrade-single-device.json` (side=B) | `upgrade.py` | Same function, opposite side |
| Post-Validate — Side B | `workflows/eos-postcheck.json` (side=B) | `validation.py` | `check_peer_match=True` — confirms both sides match |
| Restore | `workflows/eos-upgrade-orchestrator.json` | `maintenance.py` | `restore_side()` called for both sides, unconditional on the success path |
| Rollback (per side) | `workflows/eos-upgrade-orchestrator.json` | `upgrade.py` | `rollback_side()`, triggered only by the side that failed post-validation |
| Reporting / Close Out | `workflows/eos-upgrade-orchestrator.json` | `reporting.py` | `to_markdown()` / `to_json()` |

`eos-upgrade-single-device.json` and `eos-postcheck.json` are generic, reusable subworkflows — the orchestrator calls each twice (once per side) via `childJob`, passing `side` as an input rather than duplicating the workflow.

`services/eos_upgrade/upgrade.py`'s `run_pair_upgrade()` mirrors this entire call graph in Python, for use in local testing, dry runs, and as the reference the Python Actions in each workflow are built against.
