# MVP 1 Integration Audit — Read-Only EOS Pre-Check

Scope: what it takes to execute `eos-precheck.json` from Itential against a lab Arista A/B pair, read-only. No GSHUT, reload, image staging, backup, or config push.

**Status: integration layer implemented + canonical readiness contract reconciled.** Device collection remains push-model (workflow Collect/Check nodes). Evaluation is `normalize_pair_readiness()` → `evaluate_pair_readiness()` against **one** input schema: `schemas/pair_readiness.canonical.json`. What's still unconfirmed against a live platform is called out inline.

## Bottom line

**Resolved:** there is exactly **one** Python input contract for pair readiness — the canonical schema. Raw Itential / CVP / Device Broker payloads are never fed to the evaluator; they pass through `eos_ab_upgrade.normalize` first.

**Resolved:** config backup remains **out of scope for MVP 1**. The legacy `CollectedFactsDeviceBrokerClient` still raises `NotImplementedError` on write methods for the older `services/eos_upgrade/precheck.py` unit-test path.

**Still open:** live Device Broker task names; live MLAG / BGP / interface operational-command response captures (those field groups stay `field_status: unverified` until captured); IAG stdin vs `argument_order`; real `clusterId`.

---

## 1. Which Python functions are ready to execute

### Canonical decision path (MVP1 IAG / CLI)

| Function | Module | Status | Notes |
|---|---|---|---|
| `normalize_pair_readiness()` | `eos_ab_upgrade.normalize` | Ready | Maps CVP inventory, collected side records, or already-canonical input → canonical schema |
| `normalize_side()` | `eos_ab_upgrade.normalize` | Ready | Per-device mapper; LAB01A-style CVP fixtures covered in `tests/test_normalize.py` |
| `evaluate_pair_readiness()` | `eos_ab_upgrade.pair_readiness` | Ready | Pure decision logic on **canonical input only** — no vendor/platform response parsing |

### Legacy DeviceBrokerClient helpers (unit-tested, not the IAG contract)

`services/eos_upgrade/precheck.py` (`check_reachable`, `run_pre_check`, `run_pre_check_from_payload`, …) remains for broker-client unit tests. **It is not a second input contract** — do not wire new integrations to it. IAG and `eos-upgrade precheck` use normalize → evaluate.

## 2. Which functions are currently mocks/stubs

- **Resolved:** `CollectedFactsDeviceBrokerClient` is a real push-model client for the legacy helper tests.
- **Resolved:** `eos-precheck.json` has 13 task nodes; only `Evaluate pair readiness` uses a verified `GatewayManager`/`runService` pattern. Other Collect/Check nodes remain `INTEGRATION_PLACEHOLDER`.
- **Resolved:** CLI `precheck` and `iag_entrypoint.py` both call `normalize_pair_readiness` → `evaluate_pair_readiness`.

## 3. Which Itential tasks must call Device Broker

Six placeholder nodes in `eos-precheck.json` (`Resolve Side A/B`, `Check Side A/B connectivity`, `Collect EOS versions`, `Collect MLAG status`, `Collect BGP summaries`, `Collect interface status`) are meant to call Device Broker. Until those return **live operational-command** payloads, the normalizer labels:

| Field group | Canonical fields | Status until live capture |
|---|---|---|
| identity | `device_name` | verified from CVP / resolve |
| reachability | `reachable` | verified from CVP `streamingStatus` (or connectivity collect) |
| version | `version` | verified from CVP `version` / `softwareVersion` |
| **mlag** | `mlag_state`, `mlag_peer_state` | **unverified** |
| **bgp** | `bgp_established`, `bgp_expected` | **unverified** |
| **interfaces** | `critical_interfaces_up`, `critical_interfaces_expected` | **unverified** |

Unverified groups are skipped by the evaluator (warning emitted), not guessed from invented shapes.

## 4. Which tasks invoke the Python service

One: `Evaluate pair readiness` (`000a`) in `eos-precheck.json`, via `GatewayManager`/`runService` → IAG `eos-precheck` → `iag_entrypoint.py`. Still unconfirmed: real `clusterId`, and whether a merge/makeData task is needed upstream to assemble nested `params` (`AGENTS.md` Key Rule 8).

## 5. Exact input/output JSON at every boundary

### THE single input contract (canonical)

Source of truth: `schemas/pair_readiness.canonical.json`.

```json
{
  "side_a": {
    "device_name": "LAB01A",
    "reachable": true,
    "version": "4.29.2F",
    "mlag_state": null,
    "mlag_peer_state": null,
    "bgp_established": null,
    "bgp_expected": null,
    "critical_interfaces_up": null,
    "critical_interfaces_expected": null,
    "field_status": {
      "identity": "verified",
      "reachability": "verified",
      "version": "verified",
      "mlag": "unverified",
      "bgp": "unverified",
      "interfaces": "unverified"
    }
  },
  "side_b": { "...same shape..." },
  "policy": {
    "supported_source_versions": ["4.28", "4.29", "4.30", "4.31"],
    "require_mlag_active": true,
    "minimum_bgp_health_percent": 100,
    "minimum_interface_health_percent": 100
  }
}
```

**Normalization layer:** `normalize_pair_readiness(raw)` accepts:

1. Already-canonical input (pass-through + defaults)
2. Pair envelope with LAB01A-style **CVP inventory** devices under `side_a` / `side_b` (see `tests/fixtures/lab01_cvp_pair.json`)
3. Pair envelope with collected Device Broker / legacy hostname+facts side records

The evaluator **never** sees CVP `streamingStatus`, `softwareVersion`, or adapter wrappers.

### Workflow boundary (`eos-precheck.json`)

```
in:  { "side_a_device": string, "side_b_device": string, "target_version": string, "pair_id"?: string }
out: { "evidence": object }   // maps to evaluate_pair_readiness() result once wired
```

### Output (`evaluate_pair_readiness`)

```json
{
  "eligible": true,
  "blocking_reasons": [],
  "warnings": [
    "side_a: mlag fields are unverified — pending live operational-command responses; check skipped",
    "side_a: bgp fields are unverified — pending live operational-command responses; check skipped",
    "side_a: interfaces fields are unverified — pending live operational-command responses; check skipped"
  ],
  "baseline": {
    "pair_health": "healthy",
    "side_a": { "device_name": "LAB01A", "status": "healthy", "field_status": { "...": "..." } },
    "side_b": { "...": "..." }
  }
}
```

## 6. Environment variables / secrets required

**None for MVP1 evaluation.** Normalization and evaluation are pure functions over already-collected JSON.

## 7. How the Python package should run from IAG/Torero

`iag/eos-precheck-service.yaml` → `services/eos_upgrade/iag_entrypoint.py` (stdin JSON → normalize → evaluate → stdout). Decorator describes a flexible pair envelope; **canonical schema is still the only evaluator contract**.

**Still unverified:** IAG stdin vs `argument_order` CLI args — highest remaining integration risk.

## 8. Which workflow JSON artifacts can actually be imported into Itential

**None, still — by design.** Placeholder `app: "INTEGRATION_PLACEHOLDER"` nodes fail platform validation. Intentional design draft.

## 9. Task names / schemas that are assumptions and must be verified

- Device Broker generic-action task name/schema for Collect/Check nodes
- EOS adapter `app` type vs instance name
- Real `clusterId` + merge/makeData for nested params
- IAG stdin vs `argument_order`
- Workflow import endpoint
- **Live operational-command response shapes for MLAG / BGP / interfaces** — until captured, those canonical fields stay `unverified`

## 10. Exact test sequence for MVP 1

1. **Static baseline:** `cd eos-ab-upgrade && pytest -v` — includes `test_pair_readiness.py` and `test_normalize.py` (LAB01A CVP fixtures).
2. **Local CLI dry run:** `eos-upgrade precheck tests/fixtures/lab01_cvp_pair.json` — expects `eligible: true` with unverified MLAG/BGP/interface warnings.
3. Platform discovery (tasks/apps/adapters) — not yet done.
4. Confirm IAG invocation mechanism — not yet done.
5. Import IAG service after fixing repository URL placeholder.
6. Resolve Device Broker tasks; capture live MLAG/BGP/interface responses; flip `field_status` to `verified` in the normalizer once shapes are known.
7. Replace every `INTEGRATION_PLACEHOLDER`.
8. Confirm workflow import endpoint and import.
9. Run against lab pair; compare job output to `evaluate_pair_readiness` shape.
10. Confirm zero device state changed (read-only bar).
