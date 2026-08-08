# MVP1 Deployment Checklist — Read-Only EOS Precheck

Companion to `MVP1-INTEGRATION.md`: what to deploy and test against a lab Arista pair.

**Single input contract:** `schemas/pair_readiness.canonical.json`. Raw CVP / Device Broker / legacy side records are normalized first — do not document or implement a second evaluator payload.

## 1. Files that must be deployed/imported

| File | Deployed to | How |
|---|---|---|
| `src/eos_ab_upgrade/` + `services/eos_upgrade/` | IAG-accessible git repo | IAG clones `repositories[].url` in the service YAML |
| `schemas/pair_readiness.canonical.json` | with the package | Contract reference (consumed by docs + normalizer design) |
| `iag/eos-precheck-service.yaml` | IAG/Torero | `iagctl db import` |
| `workflows/eos-precheck.json` | Itential Automation Studio | **Not deployable as-is** — see §2 |

`cli.py` is a local dry-run tool (`eos-upgrade precheck`), not invoked by the platform.

## 2. What `eos-precheck.json` represents

**A reference scaffold, not an importable workflow.** 11 of 13 non-start/end nodes use `app: "INTEGRATION_PLACEHOLDER"`. Only `Evaluate pair readiness` (`000a`) uses verified `GatewayManager`/`runService`. Open on `000a`: real `clusterId`, and upstream merge/makeData for nested params (`AGENTS.md` Key Rule 8).

## 3. How `iag/eos-precheck-service.yaml` is deployed

```bash
iagctl db import iag/eos-precheck-service.yaml --validate
iagctl db import iag/eos-precheck-service.yaml --check
iagctl db import iag/eos-precheck-service.yaml
```

**Blocking issue:** `repositories[0].url` is a placeholder. Fix before import. No `secrets` block — service never touches devices.

## 4. How `iag_entrypoint.py` is invoked

`filename: services/eos_upgrade/iag_entrypoint.py` reads stdin JSON, runs:

```text
raw payload → normalize_pair_readiness() → evaluate_pair_readiness() → stdout
```

**Unverified:** stdin vs decorator `argument_order` CLI args. Test this before relying on import.

## 5. Exact inputs/outputs — one contract

### Evaluator input (canonical only)

```json
{
  "side_a": {
    "device_name": "required",
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

**MLAG / BGP / interface fields are unverified** until live operational-command responses are captured. The normalizer sets them to `null` + `field_status.<group> = "unverified"` for CVP inventory (see `tests/fixtures/lab01a_cvp_device.json`). The evaluator skips those checks and emits warnings.

### Accepted raw inputs (normalizer only — not a second contract)

| Raw shape | Example fixture | What becomes verified |
|---|---|---|
| CVP inventory device pair | `tests/fixtures/lab01_cvp_pair.json` | identity, reachability (`streamingStatus`), version |
| Collected hostname/facts side records | (workflow Collect nodes) | identity, reachability, version; ops stay unverified unless explicit canonical ops fields are present |
| Already-canonical | any full readiness payload | as labeled in `field_status` |

### Output

```json
{
  "eligible": true,
  "blocking_reasons": [],
  "warnings": ["…unverified mlag/bgp/interfaces…"],
  "baseline": {
    "pair_health": "healthy|degraded|failed",
    "side_a": {},
    "side_b": {}
  }
}
```

## 6. Device Broker operations still needing ID in your Dev environment

| Node | Needs to become |
|---|---|
| `0001` Validate Request | Maybe nothing — check `inputSchema.required` |
| `0002`/`0003` Resolve Side A/B | Inventory/Device Broker → device identity |
| `0004`/`0005` Check connectivity | Reachability collect → feeds `reachable` |
| `0006` Collect EOS versions | → canonical `version` |
| `0007` Collect MLAG status | → `mlag_state` / `mlag_peer_state` + flip `field_status.mlag` to **verified** |
| `0008` Collect BGP summaries | → `bgp_*` + flip `field_status.bgp` to **verified** |
| `0009` Collect interface status | → `critical_interfaces_*` + flip `field_status.interfaces` to **verified** |
| `000a` Evaluate pair readiness | Resolved pattern — `clusterId` + upstream merge remain |
| `000b` Generate evidence | Confirm dedicated task vs variable mapping |
| `000c` Handle Pre-Check Error | Error-status / halted evidence shape |

Also unresolved: EOS adapter `app` type vs instance name.

## 7. Smallest possible test against one Arista lab device

1. **Already done, zero platform needed:** `pytest -v` (includes LAB01A CVP normalization tests) + `eos-upgrade precheck tests/fixtures/lab01_cvp_pair.json`.
2. **Smallest real-device test:** one Device Broker / CVP inventory pull for one lab device; feed through normalizer; confirm identity/version/reachability; confirm mlag/bgp/interfaces still `unverified`.
3. **Confirm IAG invocation** (§4) with that normalized path.
4. **Only once 2 and 3 pass:** combine them. Capture live `show mlag` / BGP / interface outputs next — then extend the normalizer and mark those groups verified.

A real A/B pair is required before treating MLAG peer checks as verified.
