# Architecture

## Two layers

**Workflow layer** (Itential Automation Studio) — owns orchestration, sequencing, the human approval gate, and childJob composition. Lives in `workflows/`.

**Service layer** (`services/eos_upgrade`) — owns the logic that a static task graph can't express: drain-convergence polling, eligibility checks, validation comparisons, and evidence report assembly. Invoked from workflow tasks as Python Actions (via IAG or the platform's native Python Action task, confirmed at build time — see `docs/python-action-map.md`).

Device access itself is abstracted behind a `DeviceBrokerClient` interface (`services/eos_upgrade/models.py`) so the service layer never talks to EOS directly — in production, the Python Action's implementation of that interface calls the platform's Device Broker.

## Call graph

```
eos-upgrade-orchestrator
 │
 ├─ childJob → eos-precheck (pair)
 │
 ├─ childJob → eos-upgrade-single-device (side=A)   [GSHUT drain A → stage/reload A]
 ├─ childJob → eos-postcheck (side=A)
 │
 ├─ ▶ Approval Gate (manual task, pauses for operator)
 │
 ├─ childJob → eos-upgrade-single-device (side=B)   [GSHUT drain B → stage/reload B]
 ├─ childJob → eos-postcheck (side=B, check_peer_match=true)
 │
 ├─ Restore (both sides, unconditional on success path)
 ├─ Rollback (conditional — only the side that failed post-validation)
 └─ Reporting / Close Out
```

`eos-upgrade-single-device` and `eos-postcheck` are generic subworkflows, parameterized by `side` — the orchestrator calls each twice rather than duplicating the workflow per side.

## Platform components (by category)

| Component | Role | Confirm at build time against |
|---|---|---|
| Device Broker | Generic, adapter-agnostic dispatch for facts, CLI/config push, image staging, reload | live `tasks.json` / `apps.json` for the registered EOS adapter |
| Python Actions (IAG or native) | Runs `services/eos_upgrade` functions: drain confirmation, eligibility, validation, report rendering | IAG service definition or native Python Action task schema |
| Configuration Manager | Backup + diff of running config, before and after each side's upgrade | `openapi.json` config-manager endpoints |
| Approval / manual task | Pauses the orchestrator between Side A and Side B; records approver identity + timestamp | Ops Manager manual trigger or workflow manual task, per `/itential-mop`-style patterns |
| Templates | Renders the evidence report (or delegates to `reporting.to_markdown()`) | template engine task |

Per this repo's `AGENTS.md` Key Rule 1, none of the above are wired to specific task names here — that happens during Build (`/builder-agent`), against the live platform. See `docs/itential-task-map.md`.

## Why the service layer is separate from the workflow

Drain convergence isn't a fixed wait — it's "poll until route/neighbor counts show the peer absorbed full traffic, or time out." That control flow (loop, threshold check, timeout) is native to Python and awkward to express as a workflow task graph. Keeping it in `services/eos_upgrade/maintenance.py` makes it independently unit-testable (see `tests/test_maintenance.py`) without needing a live platform connection, and it's the same code path whether invoked from a workflow's Python Action or run standalone via `services/eos_upgrade/cli.py`.
