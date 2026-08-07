# MVP1 Deployment Checklist — Read-Only EOS Precheck

Companion to `MVP1-INTEGRATION.md`: a review of the completed MVP1 implementation, framed as what's needed to actually deploy and test it against a lab Arista pair.

## 1. Files that must be deployed/imported

| File | Deployed to | How |
|---|---|---|
| `services/eos_upgrade/` package | IAG-accessible git repo | IAG clones the `repositories[].url` in the service YAML — see §3 |
| `iag/eos-precheck-service.yaml` | IAG/Torero | `iagctl db import` |
| `workflows/eos-precheck.json` | Itential Automation Studio | **Not deployable as-is** — see §2 |

`cli.py` isn't deployed anywhere — it's a local dev tool for dry runs (§7), never invoked by the platform.

## 2. What `eos-precheck.json` represents

**A reference scaffold, not an importable workflow.** It's structurally valid (13 hex-ID nodes, all transitions resolve), but 11 of 13 non-start/end nodes carry the literal sentinel `app: "INTEGRATION_PLACEHOLDER"` — that will fail Itential's import-time validation, and the file's own top-level `description` says so. Only `Evaluate pair readiness` (`000a`) uses a real, verified task shape (`GatewayManager`/`runService`). Treat this as a design document showing intended sequencing and per-node data contracts, not something to click "import" on.

Two things still open inside `000a` itself: `clusterId` is a placeholder string, and `params.side_a`/`side_b` need a merge/makeData task immediately upstream (per `AGENTS.md` Key Rule 8 — `$var` refs don't resolve inside nested objects).

## 3. How `iag/eos-precheck-service.yaml` is deployed

```bash
iagctl db import iag/eos-precheck-service.yaml --validate
iagctl db import iag/eos-precheck-service.yaml --check
iagctl db import iag/eos-precheck-service.yaml
```

**Blocking issue:** `repositories[0].url` is a literal placeholder string, not a real git URL — IAG needs somewhere real to clone `services/eos_upgrade/` from. Fix this before any import attempt. No `secrets` block is needed or defined — the service never touches a device or Device Broker.

## 4. How `iag_entrypoint.py` is invoked

Via the service YAML (`filename: services/eos_upgrade/iag_entrypoint.py`). **This is the single biggest unverified assumption in the whole build.** It reads its full payload from stdin and writes evidence JSON to stdout (exit 0/1). That's a guess — the decorator schema also supports `argument_order`, implying IAG might instead pass fields as ordered CLI args to a `filename`-based script, a different contract entirely. Both the YAML and the entrypoint flag this by name. **Test this first**, before anything else (§7 step 3).

## 5. Exact inputs/outputs

**Input** (identical for CLI, IAG, and the payload function):

```json
{
  "pair_id": "optional",
  "target_version": "4.31.1",
  "side_a": {
    "hostname": "required", "management_ip": "required", "adapter_id": "required",
    "facts": {"version": "...", "interface_capacity_headroom_pct": 100, "interfaces_down": 0},
    "peer_state": {"healthy": true}
  },
  "side_b": { "...same shape..." }
}
```

Missing `side_a`/`side_b`/`target_version` → `ValueError`. Missing `hostname`/`management_ip`/`adapter_id` inside a side → `ValueError`. Missing `facts`/`peer_state` don't error — they just make checks fail closed.

**Output** (always this shape, never raises on a failed precheck):

```json
{
  "pair_id": "...", "side_a_hostname": "...", "side_b_hostname": "...",
  "target_version": "4.31.1", "passed": true,
  "details": {"side_a_reachable": true, "...six more booleans..."},
  "generated_at": "2026-08-07T00:00:00+00:00"
}
```

No `backups` key ever appears — hardcoded off, and the client's `backup_config()` raises if anything tried anyway.

## 6. Device Broker operations still needing ID in your Dev environment

| Node | Needs to become |
|---|---|
| `0001` Validate Request | Maybe nothing — check if `inputSchema.required` alone suffices |
| `0002`/`0003` Resolve Side A/B | Inventory/Device Broker lookup → `{hostname, management_ip, adapter_id, source_version}` |
| `0004`/`0005` Check connectivity | Device Broker generic-dispatch, reachability |
| `0006` Collect EOS versions | → `version`, `interface_capacity_headroom_pct` |
| `0007` Collect MLAG status | → `healthy` |
| `0008` Collect BGP summaries | Evidence-only, doesn't gate pass/fail |
| `0009` Collect interface status | → `interfaces_down` |
| `000a` Evaluate pair readiness | Resolved — only `clusterId` + upstream merge task remain |
| `000b` Generate evidence | Confirm if a dedicated task is needed or plain variable mapping suffices |
| `000c` Handle Pre-Check Error | Error-status task producing a halted evidence shape |

Also unresolved: the EOS adapter's real `app` type name vs. instance name (never the same string), and whether the adapter's actual response field names match this implementation's assumed contract (`version`, `interface_capacity_headroom_pct`, `interfaces_down`, `healthy`) — none of these are verified against a live response.

## 7. Smallest possible test against one Arista lab device

1. **Already done, zero platform needed:** `pytest -v` (31/31 passing) + manual CLI run against a synthetic payload.
2. **Smallest real-device test:** run one existing Device Broker "get facts" task against one lab device, compare its real response fields to this implementation's assumed names. Cheapest possible signal — no IAG, no workflow, no second device.
3. **Confirm the IAG invocation mechanism** (§4), still with synthetic data: import the service YAML (after fixing the repo URL), invoke `eos-precheck` directly via `iagctl` or a throwaway one-node `runService` workflow, using one device's data duplicated as both `side_a`/`side_b`.
4. **Only once 2 and 3 both pass:** combine them — real facts from step 2, through step 3's confirmed path, still one device standing in for both sides.

A real A/B pair only becomes necessary once you're testing `check_redundancy_healthy()`'s cross-device logic — everything before that works with one device or synthetic peer data.
