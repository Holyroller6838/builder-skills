# EOS Readiness Engine

A profile-driven Arista EOS upgrade-readiness decision engine, called from Itential. One engine handles every A/B pair topology instead of a separate workflow per topology — the caller passes a `profile` (`mlag_bgp`, `bgp_only`, `mlag_only`, `basic_pair`) and the engine evaluates only the checks that topology requires.

**MVP1 is strictly read-only.** This package never implements configuration changes, software upgrades, reboots, BGP shutdowns, or MLAG changes — it only assesses readiness and returns a decision.

## Status

**Built:** `models.py` (the normalized domain contract), the profile framework (`profiles/`), all five checks (`checks/`), and the decision contract (`engine.py:evaluate_normalized`) — fully tested, zero dependency on real Itential/EOS/CVP payload shapes.

**Deferred, not started:** raw payload normalization (`raw/` — doesn't exist yet), the `evaluate_pair(payload: dict)` wrapper that will call it, and any CLI/IAG entrypoint. All of this is blocked on a real, unmodified JSON payload from the `USILD001LAB01A`/`USILD001LAB01B` lab pair — every field name a parser would touch is currently unverified, so none of that code has been written, not even as a stub.

## Architecture

```
Itential (collects commands, owns devices/creds — outside this package)
        │  raw command_results[] — NOT yet consumed here
        ▼
[ raw normalization — DEFERRED, pending real fixture ]
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

Every dataclass in `models.py` is **our own invented contract**, not a mapping of any real EOS/CVP/Torero/Itential payload field — documented inline. The (not yet built) `raw/` layer is the only place that will ever need to know real vendor field names.

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
