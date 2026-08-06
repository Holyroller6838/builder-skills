# Use Case: Arista EOS A/B Software Upgrade

## 1. Problem Statement

Arista EOS switches are commonly deployed in redundant pairs — MLAG peers, dual-homed leaf pairs, or any topology where two devices share the same traffic path. Upgrading EOS on these pairs safely means taking only one side out of service at a time ("A/B" upgrade): drain traffic off the device being upgraded, upgrade it, confirm it's healthy, then repeat on the other side. Done manually, this requires an engineer to track BGP/MLAG state across two terminal sessions, decide by eye whether traffic has actually drained before reloading, and remember to restore normal routing afterward. There's no consistent evidence trail, and a mistimed cutover to Side B can take the entire pair down at once.

**Goal:** Automate the full A/B EOS upgrade lifecycle — pre-check, graceful traffic drain (GSHUT) on Side A, upgrade and validate Side A, gate the cutover on operator approval, drain and upgrade Side B, validate, restore normal routing on both sides, roll back on failure, and produce auditable evidence — using the platform's Device Broker for OS-agnostic device dispatch and Python Actions for the drain-confirmation and eligibility logic that off-the-shelf tasks can't express.

---

## 2. High-Level Flow

```
Pre-Check   →  GSHUT A    →  Upgrade A   →  Validate A   →  Approval Gate  →  GSHUT B     →  Upgrade B   →  Validate B   →  Restore      →  Report
    │              │             │              │                │               │              │              │              │              │
 Confirm        Drain BGP/    Stage +        Confirm peer     Engineer         Drain           Stage +       Confirm both    Un-GSHUT      Evidence
 pair health,   IGP traffic   activate       (Side B) is      confirms Side    traffic off     activate      sides on       both sides,    report,
 identify       off Side A    image,         carrying full    A is healthy     Side B (Side    image on      target         normal         update
 which side     via GSHUT,    reload         traffic, Side    before Side B    A now back      Side B,       version,       routing        ticket,
 is A / B,      confirm                      A on target      is touched      and carrying    reload        MLAG/peer      restored,      close
 backup both    convergence                  version                                          traffic)                     state healthy   evidence
 devices                                                                                                                                   captured
                                                                                                                                     │
                                                                                                                          FAIL (either side)? → Rollback that
                                                                                                                          side only, restore its GSHUT state,
                                                                                                                          alert — other side is left untouched
```

---

## 3. Phases

### Pre-Check
Use Device Broker to pull facts and health state from both devices in the pair (generic action dispatch — no hardcoded EOS adapter, so the same workflow works regardless of which adapter is registered for that device type). Confirm both devices are reachable, running a supported source version, and that the pair's redundancy state (MLAG, dual-homing) is currently healthy. Run a Python Action to determine GSHUT eligibility — e.g., confirm the peer can absorb full traffic before any drain begins. Back up the running config on both devices. If any critical check fails, **stop — do not begin draining either side**.

### GSHUT Drain — Side A
Apply the GSHUT mechanism to Side A (advertise the well-known GSHUT community / adjust local-preference per the environment's existing policy — this workflow triggers the drain, it does not design the policy). A Python Action polls route/neighbor state on Side A and confirms traffic has actually shifted to Side B — not just that the command was issued. If drain doesn't converge within the configured timeout, **abort — do not reload a device that hasn't actually drained**.

### Upgrade — Side A
Stage the target image on Side A via Device Broker, verify integrity, set boot config, save, and reload. Wait for Side A to come back online within a configurable timeout. If it doesn't return, **alert the engineer — this requires console access**.

### Post-Validate — Side A
Confirm Side A is running the target version, its MLAG/peer state is healthy, and its interfaces/neighbors have re-established. Compare against the Pre-Check baseline. This is the gate that determines whether Side B is allowed to start — **Side B never begins on a failed Side A validation.**

### Approval Gate
Pause the workflow and present the Side A results to the operator. **Side B only starts on an explicit, recorded operator approval** — this transition is never fully automatic, because Side B is the only remaining active path for the pair. Capture the approver's identity and timestamp for the evidence report.

### GSHUT Drain — Side B
Same as GSHUT Drain — Side A, applied to Side B, now that Side A is back in service and able to carry full traffic. Same Python Action convergence check and timeout/abort behavior.

### Upgrade — Side B
Same as Upgrade — Side A, applied to Side B.

### Post-Validate — Side B
Same as Post-Validate — Side A, applied to Side B. Additionally confirms both sides now report matching target versions and healthy mutual redundancy state (both members of the pair, not just Side B in isolation).

### Restore
Remove the GSHUT condition from both sides and confirm normal routing/traffic distribution has resumed on both. This phase runs unconditionally on the success path — a successful upgrade that leaves a device in a drained state is not considered complete.

### Rollback (conditional, per side)
Triggered only by the side currently mid-upgrade failing its post-validation. Restores that side's previous image/boot config, reloads, re-verifies it returns on the prior version, and restores its GSHUT state to normal. **The other side of the pair — whether already upgraded and validated, or not yet touched — is left alone.** If rollback itself fails, **escalate immediately**.

### Reporting / Close Out
Generate an evidence report covering both sides: pre/post state, config diffs, GSHUT drain confirmation and timing for each side, the operator approval record, and final outcome (complete / rolled back / halted). Update the change ticket and restore monitoring on both devices.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Device Broker for all device actions | Dispatch facts, CLI, and config-push through Device Broker rather than a hardcoded EOS adapter | Same workflow works across any adapter registered for the device's OS/type; avoids per-vendor hardcoding |
| Never upgrade both sides of a pair concurrently | Strict A-then-B sequencing; Side B does not start until Side A is validated and approved | Guarantees one side of every redundant pair is always in service |
| GSHUT before every reload | Drain traffic off the side being upgraded and confirm convergence before it reloads | A hard reload without draining first causes a traffic drop instead of a graceful cutover |
| GSHUT eligibility and drain confirmation via Python Actions | Custom Python logic checks route/neighbor counts pre- and post-GSHUT, not a static wait | Drain convergence isn't reliably expressible as a single fixed-duration wait or one off-the-shelf task |
| Mandatory operator approval between Side A and Side B | Workflow pauses after Side A validation; engineer must explicitly approve before Side B starts | Side B is the pair's only remaining active path — this cutover is never left to unattended automation |
| Rollback is per-side, not whole-pair | Only the side currently mid-upgrade is rolled back | Minimizes blast radius; a side that already validated healthy is not undone |
| Restore (un-GSHUT) is unconditional on success | Both sides' GSHUT state is cleared before the run is marked complete | A "successful" upgrade that leaves a device permanently drained is a silent failure |
| Evidence generated regardless of outcome | Report produced for success, rollback, and halted-for-approval states alike | Audit trail is non-negotiable |

---

## 5. Scope

**In scope:** A/B upgrade of Arista EOS redundant pairs (MLAG peers or equivalent dual-homed pairs), pre-checks, GSHUT drain and restore per side, image staging and activation via Device Broker, custom drain/eligibility logic via Python Actions, post-validation per side and pair-wide, mandatory operator approval gate between sides, per-side rollback, evidence generation, ITSM integration.

**Out of scope:** Upgrading a single non-redundant device (see the general Software Upgrade use case). Designing or configuring the GSHUT/BGP policy itself — this workflow triggers an existing policy, it does not author one. Initial MLAG/pair topology design. Image selection and approval (input to this workflow). Physical console recovery. Orchestration across more than one pair in a single run beyond what's defined in Batch Strategy below.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| GSHUT drain doesn't converge before reload | Traffic loss/blackhole instead of a graceful cutover | Python Action polls route/neighbor counts with a timeout; abort the upgrade if drain hasn't converged |
| Side B starts before Side A is confirmed fully healthy | Both sides down at once — full outage for the pair | Operator approval gate is a hard stop with no auto-proceed option for this specific transition |
| New image incompatible with peer's current version mid-upgrade | MLAG/redundancy protocol mismatch, split-brain risk | Post-Validate — Side A explicitly checks MLAG/peer compatibility before Side B is allowed to begin |
| Device doesn't come back after reload | Extended single-sided operation, pair left with no redundancy | Configurable reload timeout, immediate alert requiring console access |
| Rollback fails on the side being upgraded | Pair left in a mismatched or degraded state | Escalate immediately, do not retry indefinitely, report the confirmed current state of both sides |
| Un-GSHUT forgotten after a successful upgrade | Device stays in a drained, artificially low-preference state indefinitely | Restore is an unconditional phase on every success path, always verified before Close Out |
| Approval identity not captured | No accountable record of who authorized the Side B cutover | Approval Gate always records approver identity and timestamp into the evidence report |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Dispatch generic device actions (facts, CLI, config push) through Device Broker | Yes | Cannot proceed generically — would require a hardcoded EOS-specific adapter per device |
| Run custom Python Actions for GSHUT drain-confirmation and upgrade-eligibility logic | Yes | Cannot proceed — drain convergence and pair-health checks require logic beyond a static task |
| Execute CLI/config commands on EOS devices (image staging, boot config, reload) | Yes | Cannot proceed |
| Backup and diff device configuration before and after each side's upgrade | Yes | Cannot proceed |
| Orchestrate multi-step workflows with a manual approval/pause step | Yes | Cannot proceed |
| Test device and peer/MLAG state after reload | Yes | Cannot proceed |
| Generate reports from templates | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing | Track the change, record the operator approval event | No | Approval captured in the workflow only; ticket updated manually |
| Monitoring | Suppress alerts per side during its maintenance window, restore after | No | Engineer handles manually or adds a pause |
| Image repository | Source for the target EOS image | Yes | Engineer pre-stages the image |

### Discovery Questions

Ask the engineer before designing the solution:

1. How are redundant pairs defined and discovered? (MLAG domain, dual-homed leaf pair, other?) Is pairing data sourced from inventory tags, an LCM resource instance, or a manual list?
2. What GSHUT mechanism is already in use? (BGP well-known community 65535:0, local-preference adjustment, IGP metric change?) Is the policy already configured on devices, or does the workflow also need to apply it?
3. What counts as "drained enough" to proceed with a reload — a route/neighbor count threshold, a fixed wait, or both?
4. Who is the approving operator for the Side A → Side B cutover? Is a specific role or group required, or any on-call engineer?
5. What is the target EOS version and image filename? Where is the image stored?
6. Should Restore (un-GSHUT) happen automatically after successful post-validation, or does it also require operator approval?
7. Should rollback be automatic on failure, or pause for review — and does that answer differ for Side A vs. Side B?
8. Do you use a ticketing system for change records? Which one?
9. How many redundant pairs are in scope for a single run — one pair, or a fleet of pairs run under a batch strategy?
10. Are there existing automations to reuse (backup workflows, health-check templates, GSHUT trigger scripts)?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Single pair | One A/B pair per run, full choreography start to finish | Default, safest — first production runs |
| Sequential pairs | One pair at a time; a pair's full cycle (including approval and Restore) completes before the next pair starts | Small-to-medium fleet, conservative |
| Rolling pairs | N pairs in flight at once, each independently gated by its own approval step; stop launching new pairs if the failure rate exceeds threshold | Larger fleet, production |
| Parallel pairs | All pairs simultaneously | Lab/non-prod only — never for pairs sharing upstream/spine capacity |

**Note:** Batch Strategy governs how many independent pairs run concurrently. It never changes the A/B order *within* a pair — Side A and Side B are always strictly sequential, regardless of batch strategy.

---

## 9. Acceptance Criteria

1. Side B upgrade never starts until Side A post-validation passes **and** operator approval is recorded
2. GSHUT drain is confirmed (route/neighbor convergence) before either side is reloaded
3. Each side runs the target EOS version after its upgrade
4. Peer/MLAG redundancy state is healthy and matches the expected state after each side's post-validation
5. Config backup exists before and after each side's upgrade; the diff shows only expected changes
6. Restore (un-GSHUT) is executed and confirmed on both sides before the run is marked complete
7. Rollback restores the affected side to its prior version and prior GSHUT/routing state when post-validation fails, without touching the other side
8. Evidence report is generated for every run — complete, rolled back, or halted awaiting approval
9. The operator approval event is captured with approver identity and timestamp in the evidence report
10. Batch runs respect the configured pair concurrency and failure-rate threshold across multiple pairs
