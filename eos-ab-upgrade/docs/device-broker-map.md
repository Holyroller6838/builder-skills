# Device Broker Map

The spec requires all device dispatch to go through Device Broker rather than a hardcoded EOS adapter, so the same workflow works against whichever adapter is registered for a given device's OS/type (spec §4, "Device Broker for all device actions"). This document maps the generic `DeviceBrokerClient` interface used throughout `services/eos_upgrade` (see `models.py`) to the Device Broker action each method stands in for.

| `DeviceBrokerClient` method | Device Broker action | Used by |
|---|---|---|
| `get_facts(device)` | Get device facts (version, interfaces, capacity) | `precheck.py`, `validation.py` |
| `run_show(device, command)` | Run a CLI show command | ad hoc diagnostics, not on the critical path |
| `push_config(device, config)` | Push a config change | GSHUT policy application (if not pre-configured) |
| `backup_config(device)` | Backup running config | `precheck.py` (pre-upgrade), orchestrator (post-upgrade, for diff) |
| `stage_image(device, image_filename)` | Stage/transfer target image | `upgrade.py` |
| `activate_and_reload(device)` | Set boot image, save, reload | `upgrade.py` |
| `wait_for_online(device, timeout)` | Poll reachability until the device returns | `upgrade.py` |
| `apply_gshut(device)` | Apply the GSHUT drain mechanism (community/local-pref per existing policy) | `maintenance.py` |
| `remove_gshut(device)` | Remove the GSHUT condition | `maintenance.py` |
| `get_route_count(device)` | Route/neighbor count, for drain convergence polling | `maintenance.py` |
| `get_peer_state(device, peer)` | MLAG/redundancy state relative to peer | `precheck.py`, `validation.py` |

## What this workflow does *not* assume

- **No hardcoded adapter name.** The Python Action's real implementation of `DeviceBrokerClient` resolves the adapter instance/type from `apps.json`/`adapters.json` at runtime — this interface only defines the contract, not the binding.
- **No GSHUT policy authoring.** `apply_gshut()`/`remove_gshut()` trigger an existing BGP community or local-preference policy already configured on the device; they don't push new routing policy. See spec §5 (Out of Scope) and Discovery Question 2.
- **Route/neighbor threshold is configurable, not fixed.** `maintenance.py`'s `CONVERGENCE_ROUTE_THRESHOLD_PCT` and timeout constants are defaults — confirm the real threshold with the engineer per Discovery Question 3 before Build.

## Confirming the real binding

Before Build, resolve against the live platform (see root `AGENTS.md` §"Key Rule: Look Up Before You Act"):

1. `apps.json` → the EOS adapter's type name (`app` field for adapter tasks).
2. `adapters.json` → the specific adapter instance name (`adapter_id` field).
3. `openapi.json` → the exact Device Broker generic-action endpoint(s) and request/response schema for each row above.
