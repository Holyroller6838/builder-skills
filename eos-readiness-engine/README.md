# EOS Readiness Engine

A profile-driven Arista EOS upgrade-readiness decision engine, called from Itential. One engine handles every A/B pair topology instead of a separate workflow per topology — the caller passes a `profile` (`mlag_bgp`, `bgp_only`, `mlag_only`, `basic_pair`) and the engine evaluates only the checks that topology requires.

**MVP1 is strictly read-only.** This package never implements configuration changes, software upgrades, reboots, BGP shutdowns, or MLAG changes — it only assesses readiness and returns a decision.

## Status

**Built:** `models.py` (the normalized domain contract), the profile framework (`profiles/`), all five checks (`checks/`), the decision contract (`engine.py:evaluate_normalized`), the raw normalization layer (`raw/` — grouping by device name, `sh mlag`/`show mlag` aliasing, success-based failure detection, all against the confirmed real GatewayManager `sendCommand` envelope contract), the full `evaluate_pair(payload: dict)` entrypoint, and a draft IAG service wrapper (`iag_entrypoint.py`, `iag/eos-readiness-service.yaml`). 98/98 tests passing.

**Partially built — read before trusting a result:** only `parse_show_version` is a real, fixture-verified parser. `parse_show_mlag`, `parse_show_bgp_summary`, and `parse_show_interfaces_status` are explicit `NotImplementedError` stubs — no real captured output exists yet for `sh mlag`, `show ip bgp summary`, or `show interfaces status`, and none is invented. This means **`evaluate_pair()` currently returns `status: FAIL` for every profile** (even `basic_pair`, since `interfaces` is a base check) — not a bug, an honest reflection of what's actually implemented. Only `version` genuinely passes/fails correctly end-to-end today. Provide real captured fixtures for the other three commands to unblock them.

**Also not yet built:** per-pair `critical_interfaces`/`critical_bgp_peers` wiring into `evaluate_pair()` — the current 4-field payload contract (`pair_id`, `target_version`, `profile`, `command_results`) doesn't carry them, so once mlag/bgp/interfaces parsing exists, those checks will default to their no-critical-list `WARNING` fallback rather than `PASS`, until this is added. No IAG service is actually registered on any live platform yet — `iag/eos-readiness-service.yaml` is a draft.

## Architecture

```
Itential (collects commands via GatewayManager sendCommand, owns devices/creds)
        │  raw command_results[] — confirmed real envelope:
        │  {command, elapsed_time, end_time, host, name, output, start_time, success}
        ▼
┌───────────────────────────────────────────────┐
│  RAW NORMALIZATION (raw/)                       │
│  group by device name + sh/show aliasing        │
│  (collectors.py) → per-command parse            │
│  (parsers.py — version real, mlag/bgp/           │
│  interfaces explicit NotImplementedError)        │
└───────────────────────────────────────────────┘
        │  NormalizedPairData (our own contract, see models.py)
        ▼
┌───────────────────────────────────────────────┐
│  PROFILE RESOLUTION (profiles/)                │
│  profile name → which checks are applicable    │
├───────────────────────────────────────────────┤
│  CHECKS (checks/)                               │
│  collection, version, mlag, bgp, interfaces —   │
│  pure functions, PASS/WARNING/FAIL              │
├───────────────────────────────────────────────┤
│  DECISION (engine.py:evaluate_normalized)       │
│  worst-of roll-up, strict ready = (status==PASS)│
└───────────────────────────────────────────────┘
        │  {pair, profile, ready, status, checks, reasons}
        ▼
Itential (branches workflow on `ready`/`status`)
```

Every dataclass in `models.py` is **our own invented contract**, not a mapping of any real EOS/CVP/Torero/Itential payload field — documented inline. `raw/` is the only layer that ever touches real vendor field names — and even there, only the *envelope* fields (`command`/`name`/`output`/`success`) and `show version`'s CLI text are confirmed real; `sh mlag`/`show ip bgp summary`/`show interfaces status` CLI parsing is not invented, it's simply not implemented yet.

## Decision rules

- **Strict readiness**: `ready = (status == "PASS")`. A `WARNING` pair is `ready: false` — WARNING does not automatically qualify as ready in MVP1. Any future override of that belongs in Itential's orchestration/approval layer, not this engine.
- **NOT_APPLICABLE never fails a pair.** It's excluded from the status roll-up entirely — a `bgp_only` pair with `mlag: NOT_APPLICABLE` and everything else `PASS` is `ready: true`.
- **Fail-closed on missing/failed device data.** A command that failed, or a host with no data at all, fails the checks that depend on it — never silently passes, never raises past the check/engine boundary.
- **Output is plain, JSON-serializable data** — no dataclasses or enums leak into the returned dict — ready for a future Torero/Itential wrapper to hand back as-is.

## Quickstart

```bash
cd eos-readiness-engine
pip install -e ".[dev]"
pytest -v
ruff check eos_readiness tests
```
