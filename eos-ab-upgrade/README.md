# EOS A/B Software Upgrade

Automated A/B software upgrade for Arista EOS redundant pairs (MLAG peers, dual-homed leaf pairs) on the Itential Platform: pre-check → GSHUT drain → upgrade → validate → operator approval → repeat on the peer → restore → evidence report, with per-side rollback on failure.

See [`specs/spec-arista-eos-ab-upgrade.md`](specs/spec-arista-eos-ab-upgrade.md) for the full use case spec this project implements.

## Structure

| Path | Contents |
|---|---|
| `specs/` | Use case spec and the phase → workflow → service map |
| `docs/` | Architecture, platform task mapping, Device Broker mapping, Python Action mapping, acceptance test plan, rollback runbook |
| `workflows/` | Itential Automation Studio workflow scaffolds (orchestrator + 3 subworkflows) |
| `services/eos_upgrade/` | Python reference implementation of the drain-confirmation, validation, and reporting logic — the business logic Python Actions in the workflows call into |
| `tests/` | Unit tests for `services/eos_upgrade` against a fake Device Broker client |

## Status

The workflow JSON files in `workflows/` are scaffolds (start/end + input/output schema only). Per this repo's [AGENTS.md](../AGENTS.md) Key Rule 1, task names are never invented — the actual task graph inside each workflow gets wired during the Build stage (`/builder-agent`) against the live platform's `tasks.json`, using `docs/itential-task-map.md` and `docs/device-broker-map.md` as the design reference.

The `services/eos_upgrade` package, by contrast, is a real, testable implementation — it doesn't depend on any specific Itential task names, only on a generic `DeviceBrokerClient` interface (see `services/eos_upgrade/models.py`) that a Device Broker-backed Python Action implements at build time.

## Quickstart

```bash
cd eos-ab-upgrade
pip install -e ".[dev]"
pytest -v
ruff check services tests
```

## Delivery Lifecycle

This project follows the standard spec-driven delivery lifecycle (see root `AGENTS.md`):

```
Requirements → Feasibility → Design → Build → Test → As-Built
     spec-agent    solution-arch-agent   builder-agent   qa-agent
```

`specs/spec-arista-eos-ab-upgrade.md` is the approved Requirements deliverable. `docs/` covers the Design-stage detail. `workflows/` and `services/` are the Build-stage assets. `docs/acceptance-test-plan.md` feeds the Test stage.
