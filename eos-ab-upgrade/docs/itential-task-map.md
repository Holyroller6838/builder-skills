# Itential Task Map

> **Placeholder — confirm before Build.** Per `AGENTS.md` Key Rule 1 ("never invent task names"), nothing below is a confirmed task name. This table maps each phase to the *category* of platform capability required; the actual task to drop into the workflow canvas must be looked up from the live platform's `tasks.json` / `apps.json` during `/builder-agent`'s Build stage, per `AGENTS.md`'s "Look Up Before You Act" rule. Update this table with real task names once confirmed — that's the point of keeping it in version control next to the workflows.

| Phase | Capability category | Likely task family (to confirm) | Wired in |
|---|---|---|---|
| Pre-Check | Device Broker: get facts | Device Broker generic action task | `eos-precheck.json` |
| Pre-Check | Device Broker: config backup | Configuration Manager backup task | `eos-precheck.json` |
| Pre-Check | Python Action: GSHUT eligibility | Python Action / IAG Python service task | `eos-precheck.json` |
| GSHUT Drain (A/B) | Device Broker: push GSHUT config | Device Broker generic action task | `eos-upgrade-single-device.json` |
| GSHUT Drain (A/B) | Python Action: convergence polling | Python Action / IAG Python service task | `eos-upgrade-single-device.json` |
| Upgrade (A/B) | Device Broker: stage image, set boot, reload | Device Broker generic action task(s) | `eos-upgrade-single-device.json` |
| Upgrade (A/B) | Wait-for-online | Device Broker generic action task, polled, or a native wait/poll task | `eos-upgrade-single-device.json` |
| Post-Validate (A/B) | Device Broker: get facts, peer/MLAG state | Device Broker generic action task | `eos-postcheck.json` |
| Post-Validate (A/B) | Python Action: comparison against baseline | Python Action / IAG Python service task | `eos-postcheck.json` |
| Approval Gate | Manual approval / pause | Ops Manager manual trigger or workflow manual task | `eos-upgrade-orchestrator.json` |
| Restore | Device Broker: remove GSHUT config | Device Broker generic action task | `eos-upgrade-orchestrator.json` |
| Rollback (per side) | Device Broker: restore prior image/config, reload | Device Broker generic action task(s) | `eos-upgrade-orchestrator.json` |
| Reporting | Template render or Python Action | Template task, or `reporting.py` via Python Action | `eos-upgrade-orchestrator.json` |
| Reporting | ITSM ticket update (optional) | ServiceNow/ITSM adapter task | `eos-upgrade-orchestrator.json` |

## Lookup checklist for `/builder-agent`

1. `jq '.paths["/workflow_builder/tasks/list"]' platform/openapi.json` (or the use-case-local `tasks.json`) to enumerate available tasks.
2. Confirm the registered EOS adapter's `app` type name from `apps.json` and instance name from `adapters.json` — do not assume `Arista` or `EOS` naming.
3. Confirm whether GSHUT drain convergence and eligibility logic run as an IAG Python service (see `helpers/iag/example-python-service.yaml`) or a native Python Action task — this determines the exact task family in the "Wired in" column above.
4. Fetch schemas for every task above via `multipleTaskDetails?dereferenceSchemas=true` and cache to the use-case's `task-schemas.json` before wiring.
5. Replace the "to confirm" placeholders in this file with the real task names once verified, so this document stays accurate for future maintainers.
