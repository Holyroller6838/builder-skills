# MVP 1 Integration Audit — Read-Only EOS Pre-Check

Scope: what it takes to execute `eos-precheck.json` from Itential against a lab Arista A/B pair, read-only. No GSHUT, reload, image staging, backup, or config push.

**Status: integration layer implemented.** This document started as a read-only audit (§1–§10 below are mostly unchanged from that pass) and now also records what closed the gaps it found: `services/eos_upgrade/device_broker.py` (production `DeviceBrokerClient`), the `precheck`/`iag_entrypoint.py` CLI entrypoints, `iag/eos-precheck-service.yaml`, and `workflows/eos-precheck.json`'s 13-node MVP1 structure. What's still unconfirmed against a live platform is called out inline — everything else here reflects the current, committed code.

## Bottom line

**Resolved:** config backup is confirmed **out of scope for MVP 1** — `run_pre_check()` now defaults to `include_backup=False` and never calls `backup_pair()` in the payload-driven path (`run_pre_check_from_payload()` hardcodes `include_backup=False`). The production `CollectedFactsDeviceBrokerClient` additionally raises `NotImplementedError` on every write-capable method (`backup_config` included) as a structural guarantee, not just a default.

**Still open:** every Device Broker/Inventory task name and field-name mapping is unverified against a live platform (§3, §5, §9 below) — `eos-precheck.json`'s placeholder nodes and `device_broker.py`'s comments both flag exactly where.

---

## 1. Which Python functions are ready to execute

All of `services/eos_upgrade/precheck.py` is implemented and covered by passing unit tests (`tests/test_precheck.py`, `tests/test_device_broker.py` — 31/31 passing across the whole suite):

| Function | Status | Notes |
|---|---|---|
| `check_reachable()` | Ready | `bool(client.get_facts(device))` |
| `check_source_version()` | Ready | String-prefix match against `SUPPORTED_SOURCE_VERSIONS = {"4.28", "4.29", "4.30", "4.31"}` |
| `check_redundancy_healthy()` | Ready | Reads `.get("healthy")` from both sides' `get_peer_state()` |
| `check_gshut_eligibility()` | Ready | Reads `.get("interface_capacity_headroom_pct")` from the peer's facts, requires `>= 100` |
| `backup_pair()` | Implemented, **excluded from MVP1** | Only called when `include_backup=True`; MVP1's payload path always passes `False`. Kept for a later phase. |
| `run_pre_check()` | Ready | Now takes `include_backup: bool = False`. Returns `(passed: bool, details: dict)` |
| `run_pre_check_from_payload()` | Ready — new | Validates a JSON payload, builds `Device`/`RedundantPair` + `CollectedFactsDeviceBrokerClient`, calls `run_pre_check(..., include_backup=False)`, returns evidence via `build_precheck_evidence()` |
| `build_precheck_evidence()` | Ready — new | `{pair_id, side_a_hostname, side_b_hostname, target_version, passed, details, generated_at}` |

`services/eos_upgrade/reporting.py` (`to_dict`, `to_json`, `to_markdown`) still isn't used for precheck — it renders a `PairUpgradeReport`/`Outcome`, which has no "precheck-only" concept. `build_precheck_evidence()` (above) is the MVP1-scoped alternative, deliberately kept separate rather than extending `Outcome`.

Everything in `maintenance.py`, `upgrade.py`, and `validation.py` is implemented and tested but is **out of scope for MVP 1** by the terms of this task (GSHUT, reload, image, post-upgrade validation) and is not wired into `eos-precheck.json`.

## 2. Which functions are currently mocks/stubs

- **Resolved:** `services/eos_upgrade/device_broker.py` now provides a production `DeviceBrokerClient` implementation, `CollectedFactsDeviceBrokerClient`. It's not a live-calling client — see the push/collected-facts model in §4 and `docs/architecture.md` — but it's real, tested code, not a test-only fake. `tests/fixtures/fake_broker.py`'s `FakeDeviceBrokerClient` remains test-only and is unchanged.
- **Resolved:** `eos-precheck.json` now has 13 task nodes (was start/end only). Only one, `Evaluate pair readiness`, uses a verified real task pattern (`GatewayManager`/`runService`); the other 11 use an explicit `INTEGRATION_PLACEHOLDER` sentinel because no generic Device Broker dispatch task is verified anywhere in this repo (§3, §9). **The workflow will not import into a real Itential platform as-is** — the placeholder `app` values will fail platform-side validation. `eos-upgrade-orchestrator.json`, `eos-upgrade-single-device.json`, and `eos-postcheck.json` remain untouched start/end scaffolds — out of scope for MVP1.
- **Resolved:** `services/eos_upgrade/cli.py` now has a `precheck` subcommand (`eos-upgrade precheck <payload.json|->`), and a separate minimal `services/eos_upgrade/iag_entrypoint.py` (stdin-only) is what the IAG service actually invokes. Both call the same `run_pre_check_from_payload()`. Manually verified against a hand-built payload fixture: correct evidence JSON and exit code (0/1) for both a passing and failing case.

## 3. Which Itential tasks must call Device Broker

Six placeholder nodes in `eos-precheck.json` (`Resolve Side A/B`, `Check Side A/B connectivity`, `Collect EOS versions`, `Collect MLAG status`, `Collect BGP summaries`, `Collect interface status`) are meant to call Device Broker, but none has a verified task name — every one carries `app: "INTEGRATION_PLACEHOLDER"` and a `description` explaining what it should become. Backup is **not** among them — it's excluded from MVP1 (§Bottom line). No task node, task name, or Device Broker endpoint has been created or confirmed against a live platform.

## 4. Which tasks invoke the Python service

One: `Evaluate pair readiness` (`000a`) in `eos-precheck.json`, using the verified real `GatewayManager`/`runService` task shape (reused from `helpers/assets/vendor-juniper-junos.json`, not invented). **Resolved architecture decision** (was open in §9's earlier draft): the workflow's own structure settles "IAG vs. native Python Action" for Pre-Check specifically — collection happens in native Device Broker tasks upstream (§3), and this node only *evaluates* already-collected facts via the `eos-precheck` IAG service (`iag/eos-precheck-service.yaml` → `services/eos_upgrade/iag_entrypoint.py`). It never calls Device Broker itself. Still unconfirmed: the real `clusterId`, and — per `AGENTS.md` Key Rule 8 — a merge/makeData task is likely needed immediately upstream of this node to assemble the nested `params.side_a`/`side_b` objects, since `$var` references don't resolve inside nested object values.

## 5. Exact input/output JSON at every boundary

**Workflow boundary** (`eos-precheck.json`, as committed):

```
in:  { "side_a_device": string, "side_b_device": string, "target_version": string, "pair_id"?: string }
out: { "evidence": object }
```

`side_a_device`/`side_b_device` are still bare strings — that gap is now pushed explicitly onto the `Resolve Side A`/`Resolve Side B` placeholder nodes, whose job is to resolve an identifier into the full record shape below before anything else runs. This wasn't solved by adding Python code; it's a workflow-side responsibility now clearly marked as unverified in both the workflow JSON and here.

**Payload contract** (our own, not Itential's) — this is what `run_pre_check_from_payload()`, the CLI's `precheck` subcommand, and the IAG entrypoint all consume identically:

```json
{
  "pair_id": "lab-pair-01",
  "target_version": "4.31.1",
  "side_a": {
    "hostname": "...", "management_ip": "...", "adapter_id": "...", "source_version": "...",
    "facts": { "version": "...", "interface_capacity_headroom_pct": 100, "interfaces_down": 0 },
    "peer_state": { "healthy": true }
  },
  "side_b": { "...same shape..." }
}
```

`facts`/`peer_state` per side are expected to already be populated by the workflow's Collect/Check nodes (§3, §4) before `Evaluate pair readiness` runs — the Python layer never fetches them itself. `device_broker.device_from_record()` requires exact keys `hostname`, `management_ip`, `adapter_id` and raises `ValueError` naming whatever's missing; it does not guess at Itential's real field names (see §9).

**`build_precheck_evidence()` output** (verified via manual CLI run, both passing and failing cases):

```json
{
  "pair_id": "lab-pair-01",
  "side_a_hostname": "...",
  "side_b_hostname": "...",
  "target_version": "4.31.1",
  "passed": true,
  "details": {
    "side_a_reachable": true,
    "side_b_reachable": true,
    "side_a_source_version_supported": true,
    "side_b_source_version_supported": true,
    "redundancy_healthy": true,
    "side_a_gshut_eligible": true,
    "side_b_gshut_eligible": true
  },
  "generated_at": "2026-08-06T22:19:29.573820+00:00"
}
```

**Resolved:** `details` never contains a `backups` key in the MVP1 path — `run_pre_check_from_payload()` hardcodes `include_backup=False`. The old "KeyError trap" this section used to warn about no longer applies to the payload-driven path (it would still apply if someone called `run_pre_check(..., include_backup=True)` directly and then failed the pass, since `backups` is still conditional on `passed and include_backup` — same shape, just opt-in now).

**`CollectedFactsDeviceBrokerClient` contract** (what upstream Collect/Check nodes must ultimately populate — still our own invented field names, still unverified against a real adapter response):

| Method | Expected return shape | Consumed by |
|---|---|---|
| `get_facts(device)` | `dict` with keys `version` (str), `interface_capacity_headroom_pct` (int/float), `interfaces_down` (int) | `check_reachable`, `check_source_version`, `check_gshut_eligibility` |
| `get_peer_state(device, peer)` | `dict` with key `healthy` (bool) | `check_redundancy_healthy` |

`backup_config` and every other write method are implemented to raise `NotImplementedError` — see `device_broker.py`. Per `AGENTS.md` rule 20, these field names must still be checked against the live adapter's actual output before the Collect/Check placeholder nodes are wired for real.

## 6. Environment variables / secrets required

**Resolved for MVP1: none.** `CollectedFactsDeviceBrokerClient` never authenticates to Device Broker or a device — it only reads pre-collected data handed to it — so `services/eos_upgrade`'s Pre-Check path needs zero device credentials, confirmed by design (§4) and still zero grep hits for `os.environ`/`os.getenv`. `iag/eos-precheck-service.yaml` correspondingly has no `secrets:` block. This will change once a later phase needs a client that makes live calls (GSHUT, upgrade) — out of scope here.

Platform credentials (`PLATFORM_URL`, `CLIENT_ID`, `CLIENT_SECRET` in `.env`, per `scripts/use_case_init.py`'s convention) remain irrelevant to this Python layer; they'd only matter for a script that calls Itential's own REST API directly, which nothing here does.

## 7. How the Python package should run from IAG/Torero

**Resolved, pending lab confirmation.** `iag/eos-precheck-service.yaml` now exists: one decorator (`eos-precheck-input`, JSON Schema matching §5's payload contract), one `python-script` service pointing at `services/eos_upgrade/iag_entrypoint.py` (chosen over `cli.py`'s `precheck` subcommand or `runtime.pyproj-script` — a minimal, single-purpose, stdin-only entrypoint has less surface for IAG's invocation mechanism to trip over).

**Still unverified — the single biggest integration risk found in this whole exercise:** how IAG hands decorator-validated input to a `filename`-based python-script. `iag_entrypoint.py` assumes IAG pipes the full JSON payload to stdin. But `helpers/iag/service-file-schema.md`'s decorator spec also defines `argument_order` ("optional: ordered arg list"), which implies IAG's `python-script` path may instead pass validated fields as **CLI arguments**, not a stdin blob — a materially different invocation contract. Both the YAML and the entrypoint file flag this by name. **First thing to test in the lab**, before anything else in §10's sequence past step 1.

No `requirements.txt` needed yet — `iag_entrypoint.py` and everything it calls is pure stdlib.

## 8. Which workflow JSON artifacts can actually be imported into Itential

**None, still — by design.** `eos-precheck.json` is now a 13-node structure (`python3 -m json.tool` and a hex-task-ID/transition-integrity check both pass), but 11 of those nodes carry the sentinel `app: "INTEGRATION_PLACEHOLDER"`, which will fail platform-side validation on import. This is intentional and stated in the workflow's own top-level `description` field — it's a structurally correct design draft for the lab session, not an import-ready artifact. The other three workflows (`eos-upgrade-orchestrator.json`, `eos-upgrade-single-device.json`, `eos-postcheck.json`) remain untouched start/end scaffolds — still out of scope.

**Unconfirmed:** which import endpoint any of these are meant for. The `{"automation": {...}}` shape matches an individual workflow create/import call, not the `{"project": {...}}` wrapper `POST /automation-studio/projects/import` expects (per `AGENTS.md` rule 11). Confirm the exact endpoint and body wrapper against `openapi.json` before attempting an import.

## 9. Task names / schemas that are assumptions and must be verified

**Resolved since the first audit pass:** the IAG-vs-native-Python-Action architecture fork — `Evaluate pair readiness` now uses a verified `GatewayManager`/`runService` pattern, settling this for Pre-Check specifically (§4).

**Still open** — every one of these is called out inline in `eos-precheck.json`'s node `description` fields, not just here:

- The Device Broker generic-action task name/schema for the six Collect/Check/Resolve nodes (§3) — `AGENTS.md` Key Rule 10's `genericAdapterRequest` is the only documented (not lab-verified) lead
- The registered EOS adapter's `app` type name (`apps.json`) and instance name (`adapters.json`) — per `AGENTS.md` rule 3/23, these are never the same string
- The real `clusterId` for the `runService` call, and whether a merge/makeData task is needed upstream to assemble `params.side_a`/`side_b` (§4, `AGENTS.md` Key Rule 8)
- Whether IAG passes decorator input via stdin or `argument_order` CLI args (§7) — the single highest-risk item in this list
- The exact workflow import endpoint (§8)
- The real field names returned by Device Broker's get-facts / get-peer-state actions (§5)

## 10. Exact test sequence for MVP 1

Backup scope question is resolved — no step below touches it.

1. **Static baseline — done.** `pytest -v` from `eos-ab-upgrade/` — 31/31 passing, including `test_device_broker.py`'s coverage of hostname/peer-keying and every write method raising `NotImplementedError`. `ruff check services tests` — clean. Confirms the business logic is internally correct; proves nothing about the platform yet.
2. **Local CLI dry run — done, against a synthetic payload, not the lab pair.** `eos-upgrade precheck <payload.json>` and `... precheck -` (stdin) both verified manually: correct evidence JSON, exit 0 on pass, exit 1 on fail (unhealthy redundancy case), no `backups` key present. **Next:** re-run this same command with a payload built from *real* lab device data once §3's Collect/Check nodes exist to produce it.
3. **Platform discovery (not yet done):** pull/read the lab environment's `tasks.json`, `apps.json`, `adapters.json`. Confirm the EOS adapter is registered, resolve its `app` type name and instance name.
4. **Confirm the IAG invocation mechanism (not yet done — do this before anything else below):** stdin vs. `argument_order` CLI args (§7). This determines whether `iag_entrypoint.py` needs rework before it's worth importing the service YAML at all.
5. **Import the IAG service (not yet done):** `iagctl db import iag/eos-precheck-service.yaml --validate`, then `--check`, then real import (after fixing the repository URL placeholder). Confirm `eos-precheck` is callable via GatewayManager from a throwaway test workflow before touching `eos-precheck.json`.
6. **Resolve the Device Broker task name/schema (not yet done)** for the six Collect/Check/Resolve placeholder nodes (§3, §9), and the merge/makeData task needed to assemble `Evaluate pair readiness`'s nested `params` (§4).
7. **Replace every `INTEGRATION_PLACEHOLDER`** in `eos-precheck.json` with the confirmed real task nodes from steps 3–6.
8. **Confirm the workflow import endpoint (§8)** and import `eos-precheck.json` into Automation Studio. Patch project membership per `AGENTS.md` rule 11a if it's inside a project.
9. **Run the workflow against the lab pair.** Compare the actual job output to `build_precheck_evidence()`'s shape (§5). Iterate on any field-name mismatches between what Device Broker actually returns and what `precheck.py`/`device_broker.py` expect.
10. **Confirm zero device state changed** — config diff on both lab devices before and after the run, verify it's empty. This is the actual acceptance bar for "read-only," and it's now structurally reinforced: `CollectedFactsDeviceBrokerClient` has no working write path even if something upstream tried to use one.
