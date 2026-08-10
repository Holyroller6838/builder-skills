# Integration Contracts — MVP Track 1 (EOS Upgrade Readiness)

This document is the single source of truth for every unresolved Itential platform integration boundary in `workflows/eos-upgrade-readiness.json`. It exists because this build was done **offline, with no live platform connection** (see "How this was built" below) — every input/output shape below is **our own invented contract**, not a verified Itential schema, unless explicitly marked otherwise.

**No task name or schema for CloudVision, Device Broker, Inventory Manager, or GatewayManager is invented in this document or in the workflow JSON**, except where a task is cited as a real, verified example pulled from `helpers/assets/` (only `GatewayManager`'s `runService` task qualifies — see §4). Everywhere else, the workflow uses the literal sentinel `app: "INTEGRATION_PLACEHOLDER"` and this doc states the data contract that whatever real task replaces it must satisfy.

## How this was built

No `.auth.json`, `.env` with real credentials, `tasks.json`, `apps.json`, `adapters.json`, or `solution-design.md` exist for this track — confirmed by checking the repo directly, not assumed. `/builder-agent` correctly refused to build without a workspace contract; `/solution-arch-agent`'s Feasibility stage got as far as authentication and found `environments/cloud-lab.env` unfilled. The engineer chose to proceed offline rather than wait on real credentials. Every contract below is therefore a design placeholder for Design-stage confirmation, not a Feasibility-verified fact.

## Workflow sequence (as built)

```
Validate Request → Resolve Device → Connectivity Check → EOS Version → MLAG Status
→ BGP Summary → Interface Status → Evaluate Readiness → Generate Report
```

Nine named phases, matching `workflows/eos-precheck.json`'s proven granular collection pattern (pair-based → collapsed to a single device here). A tenth node, `Handle Readiness Check Error`, exists beyond the requested nine — added per `AGENTS.md` Key Rule 19/21: every external/adapter-calling task needs an error transition or the job gets permanently stuck.

## CloudVision — unresolved gap, not represented by any node

**This is the most important open item in this document.** The original request for this track asked for a "retrieve CloudVision state" step. CloudVision appears **zero times anywhere in this repo** — no adapter, no task, no doc, confirmed by a full-repo search before this build started. There is no evidence a CloudVision adapter is even registered on any target platform.

Per the engineer's explicit instruction ("Preserve the workflow sequence: Validate Request → Resolve Device → Connectivity Check → EOS Version → MLAG Status → BGP Summary → Interface Status → Evaluate Readiness → Generate Report"), **the built workflow has no CloudVision node** — that sequence doesn't include one. This document records that gap rather than silently resolving it either way. Two real options exist for Design to choose between, neither implemented here:

1. Fold CloudVision-sourced attributes into `Resolve Device` (§2) — if CloudVision is the system of record for device identity/inventory in the target environment, its data could enrich the device record there.
2. Add a dedicated `Retrieve CloudVision State` node back into the sequence, if CloudVision provides data that `Connectivity Check` / `EOS Version` / `MLAG Status` / `Interface Status` don't already cover from Device Broker.

**Before Design starts on this track, confirm with the engineer:** does the target platform have a CloudVision adapter registered at all? If not, this entire requirement may need to be dropped or replaced with a different data source, not just re-routed to a different node.

## 1. Validate Request

**Node:** `0001` — `INTEGRATION_PLACEHOLDER`

No integration boundary — likely resolved by the workflow's own `inputSchema.required` (already declares `device_identifier` and `target_version` as required) rather than a dedicated task. Confirm during Design whether a separate condition/validation task is actually needed, or whether this node can be eliminated.

## 2. Resolve Device — Inventory Manager / Device Broker

**Node:** `0002` — `INTEGRATION_PLACEHOLDER`

**Input:** `device_identifier` (string) — same open question as `eos-precheck.json` had for `side_a_device`/`side_b_device`: is this a bare hostname, or does Itential's real inventory boundary expect something richer at this point?

**Output contract (ours, unverified):**
```json
{
  "hostname": "string, required",
  "management_ip": "string, required",
  "adapter_id": "string, required",
  "source_version": "string, optional"
}
```
Matches `services/eos_upgrade/device_broker.py:device_from_record()`'s exact required-field set — that function raises `ValueError` naming whatever's missing. This contract is deliberately our own, not a guess at Itential's real device schema.

**What to verify in the lab:** whether device resolution goes through Inventory Manager, Device Broker, or both — see the `/itential-inventory` skill for the real task catalog. Neither task name is invented here.

## 3. Connectivity Check — Device Broker

**Node:** `0003` — `INTEGRATION_PLACEHOLDER`

**Input:** the device record from §2.

**Output contract (ours, unverified):**
```json
{ "reachable": true }
```
Consumed by `services/eos_upgrade/readiness.py:check_reachable()`.

**What to verify:** the real Device Broker generic-dispatch task. `AGENTS.md` Key Rule 10's `genericAdapterRequest` is the only documented (not lab-verified) lead. Resolve the adapter `app` type name and `adapter_id` instance name from the lab's `apps.json`/`adapters.json` — never assume `Arista` or `EOS` naming (Key Rule 3/23).

## 4. EOS Version — Device Broker

**Node:** `0004` — `INTEGRATION_PLACEHOLDER`

**Input:** the device record from §2.

**Output contract (ours, unverified):**
```json
{ "version": "4.31.1" }
```
Consumed by `check_source_version_supported()` — string-prefix match against `SUPPORTED_SOURCE_VERSIONS = {"4.28", "4.29", "4.30", "4.31"}`.

**What to verify:** same Device Broker generic-dispatch task family as §3 (likely a "get facts" style call). Confirm the real response field name — `version` is our contract, not a proven adapter response shape (per `AGENTS.md` Key Rule 20: adapters reshape upstream responses).

## 5. MLAG Status — Device Broker

**Node:** `0005` — `INTEGRATION_PLACEHOLDER`

**Input:** the device record from §2.

**Output contract (ours, unverified):**
```json
{ "healthy": true }
```
Consumed by `check_mlag_healthy()`.

**Important scope note:** because this track is single-device, this reports the device's *own* MLAG/peer-link state — not a cross-device pair comparison like `eos-precheck.json`'s `check_redundancy_healthy()`, which checks both sides of a redundant pair. Don't reuse that pair-based function here; the semantics differ.

## 6. BGP Summary — Device Broker (evidence-only)

**Node:** `0006` — `INTEGRATION_PLACEHOLDER`

**Input:** the device record from §2.

**Output contract (ours, unverified):** any object — passed through unmodified into the final report's `bgp_summary` field, never inspected by `evaluate_readiness()`. No requirement in this track defines a BGP-summary gating rule, so none is invented. Same evidence-only treatment `eos-precheck.json` gave its BGP Summary node.

## 7. Interface Status — Device Broker

**Node:** `0007` — `INTEGRATION_PLACEHOLDER`

**Input:** the device record from §2.

**Output contract (ours, unverified):**
```json
{ "down_count": 0 }
```
Consumed by `check_interfaces_healthy()` — passes when `down_count == 0`.

## 8. Evaluate Readiness — GatewayManager (verified real pattern)

**Node:** `0008` — `runService`, `app: "GatewayManager"`

**This is the one node in this workflow built from a verified, real task** — the exact `runService` shape confirmed from `helpers/assets/vendor-juniper-junos.json`'s live-exported project JSON (fields: `serviceName`, `clusterId`, `params`, `inventory`; outgoing `result`). Nothing about the task name or schema is invented.

**What's still unresolved:**
- `clusterId` — a literal placeholder string; needs the real registered Gateway cluster ID from the lab.
- `params.device`/`connectivity`/`facts`/`mlag_status`/`bgp_summary`/`interfaces` — placeholder strings noting that an upstream merge/makeData task is required, per `AGENTS.md` Key Rule 8 (`$var` references don't resolve inside nested object values).

**Engineer decision on record:** the original request asked for GatewayManager specifically for "read-only EOS health commands" as its own step. During planning, research confirmed no Arista asset file in this repo uses GatewayManager for device commands — the real, verified Arista pattern for read-only health commands is MOP command templates (`Show Version`, `Software Upgrade Checks` in `helpers/assets/vendor-arista-eos.json`). The engineer was asked and chose to keep GatewayManager per their original instruction. This build resolved that by using GatewayManager only for the evaluation step (a legitimate, verified use of `runService` — see the identical pattern in `eos-precheck.json`'s `Evaluate pair readiness` node) and treating the five data-collection nodes (§3–§7) as generic `INTEGRATION_PLACEHOLDER` rather than guessing at a GatewayManager `runCode` schema for raw device commands that no Arista asset attests to. **If Design instead wants GatewayManager `runCode` executing device commands directly** (the literal original ask), or wants to switch §3–§7 to the more-grounded MOP pattern, both are live options — neither is built here, and this doc exists so that choice can be made deliberately instead of by default.

**Python contract:** the service calls `services/eos_upgrade/readiness.py:run_readiness_check_from_payload()`, which requires exactly the payload shape below (validated, raises `ValueError` naming any missing top-level key):
```json
{
  "device": { "hostname": "...", "management_ip": "...", "adapter_id": "...", "source_version": "..." },
  "target_version": "4.31.1",
  "connectivity": { "reachable": true },
  "facts": { "version": "4.31.1" },
  "mlag_status": { "healthy": true },
  "bgp_summary": { "...any shape..." },
  "interfaces": { "down_count": 0 }
}
```

**Output** — `build_readiness_evidence()`'s shape, always returned, never raises on a failed readiness check:
```json
{
  "device_hostname": "lab-leaf-a",
  "target_version": "4.31.1",
  "passed": true,
  "details": {
    "reachable": true,
    "source_version_supported": true,
    "mlag_healthy": true,
    "interfaces_healthy": true
  },
  "bgp_summary": { "...whatever §6 collected..." },
  "generated_at": "2026-08-10T17:30:22.187450+00:00"
}
```
Verified via manual CLI run (`eos-upgrade readiness <payload.json>`) against both a passing and failing synthetic payload — see `tests/fixtures/readiness_payloads.py`.

## 9. Generate Report

**Node:** `0009` — `INTEGRATION_PLACEHOLDER`

`0008`'s result is already the complete report — this node's only job is exposing it as the workflow's `outputSchema.report`. Confirm during Design whether that needs a dedicated task or is a plain variable mapping.

## IAG invocation mechanism — unresolved, highest-risk item for Build

`iag/eos-readiness-service.yaml` → `services/eos_upgrade/readiness_entrypoint.py` reads its full payload from **stdin** and writes evidence JSON to stdout (exit 0/1). This is an assumption, carried over unchanged from the same open question in the precheck track (`MVP1-DEPLOYMENT-CHECKLIST.md` §4): the decorator schema also supports `argument_order`, implying IAG might instead pass fields as ordered CLI arguments to a `filename`-based script. Confirm which mechanism the real IAG install uses before relying on this.

## Read-only guarantee

`services/eos_upgrade/readiness.py` has no live-call surface at all — unlike `precheck.py`, it doesn't take a `DeviceBrokerClient`; every function operates directly on already-collected dicts passed in from the workflow. There is no write path to disable, because none exists. This is a stronger structural guarantee than the precheck track's `CollectedFactsDeviceBrokerClient` (which has to raise `NotImplementedError` on write methods it defines) — here, those methods were never defined in the first place.

## Environment variables / secrets

None. Same rationale as the precheck track: the IAG service only evaluates already-collected data and never authenticates to a device, Device Broker, Inventory Manager, CloudVision, or any adapter.
