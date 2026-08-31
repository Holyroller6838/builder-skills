# Builder Skills Repository Transfer — Part 011 of 011

**Git commit:** `982d97c1573ca7ea892b39acced9b0d15955c4a9` on branch `main`  
**Generated:** 2026-08-31 21:28:30 UTC  
**See also:** `builder-skills-transfer-manifest.md` for the full repository manifest, directory tree, and complete checksum index across all parts.

This part contains **21** file(s):

- `spec-files/spec-bgp-peer-provisioning.md`
- `spec-files/spec-change-management.md`
- `spec-files/spec-circuit-provisioning.md`
- `spec-files/spec-cloud-security-groups.md`
- `spec-files/spec-config-backup-compliance.md`
- `spec-files/spec-config-drift-remediation.md`
- `spec-files/spec-device-decommissioning.md`
- `spec-files/spec-device-onboarding.md`
- `spec-files/spec-dns-record-management.md`
- `spec-files/spec-firewall-rule-lifecycle.md`
- `spec-files/spec-incident-auto-remediation.md`
- `spec-files/spec-ipam-lifecycle.md`
- `spec-files/spec-load-balancer-vip.md`
- `spec-files/spec-network-compliance-audit.md`
- `spec-files/spec-network-health-check.md`
- `spec-files/spec-port-turn-up.md`
- `spec-files/spec-software-upgrade.md`
- `spec-files/spec-ssl-certificate-lifecycle.md`
- `spec-files/spec-vlan-provisioning.md`
- `spec-files/spec-vpn-tunnel-provisioning.md`
- `spec-files/spec-wan-bandwidth-modification.md`

---

============================================================
FILE: spec-files/spec-bgp-peer-provisioning.md
DIRECTORY: spec-files/
FILENAME: spec-bgp-peer-provisioning.md
============================================================
SHA256: 0f75286627a07359afe86635d446f8eaa5169937fb0a2f91f8b4bf97c75ef151

````markdown
# Use Case: BGP Peer Provisioning

## 1. Problem Statement

Adding a BGP peering session requires precise coordination between two routers, often managed by different teams or organizations. Engineers must agree on AS numbers, peer IPs, route policies, and prefix limits — then configure both sides correctly and verify the session establishes. A typo in an AS number or a missing route-map on one side means the session never comes up, and troubleshooting is a back-and-forth between teams. For service providers managing hundreds of peering sessions, this manual process does not scale.

**Goal:** Automate the full BGP peer lifecycle — validate inputs, deploy config to both sides, verify session establishment and route exchange — with rollback if the session fails to come up.

---

## 2. High-Level Flow

```
Validate     →  Pre-Flight   →  Deploy       →  Deploy      →  Verify     →  Post-Flight  →  Close
Inputs          Checks          Near Side       Far Side       Session       Checks          Out
   │               │               │               │              │              │              │
   │               │               │               │              │              │              │
 AS numbers,    Check both      Apply BGP      Apply BGP     Wait for       Confirm        Update
 peer IPs,      devices are     config to      config to     session to     routes are     ticket,
 route policy,  reachable,      the local      the remote    reach          exchanged,     generate
 prefix         backup          router         router        Established    prefix         evidence
 limits         configs                                      state          counts         report
                                                                │            match
                                                           FAIL? → Rollback both sides
```

---

## 3. Phases

### Validate Inputs
Validate all peering parameters before touching any device. Confirm the AS numbers are valid (1-4294967295 for 4-byte ASN). Confirm the peer IP addresses are valid and in the correct address family (IPv4 or IPv6). Confirm the route policy names are provided for both sides. If prefix limits are specified, confirm they are reasonable. If any input is invalid, **stop with a clear error — do not deploy bad config**.

### Pre-Flight Checks
Verify both devices are reachable and healthy. Backup the running config on both sides. Check that the peer IP addresses are routable between the two devices (a ping or traceroute from near side to far side). Confirm the BGP process is running on both devices. Check that the proposed peer does not already exist — if it does, **stop and ask if this is a modify operation instead**.

### Deploy Near Side
Generate and apply the BGP neighbor configuration to the local router. This includes the neighbor statement, remote AS, route-map references (inbound and outbound), prefix limits, timers, and any authentication (MD5 or TCP-AO). Verify the config was applied by reading it back. If the apply fails, **stop — do not configure the far side**.

### Deploy Far Side
Generate and apply the mirror BGP configuration to the remote router. The far side config uses the near side's IP as the neighbor address and the near side's AS as the remote AS. Same route-map, prefix limit, and authentication settings (matched to the near side). Verify the config was applied by reading it back. If the apply fails, **rollback the near side**.

### Verify Session
Wait for the BGP session to reach the Established state. Poll the BGP neighbor status on both devices with a configurable timeout (default: 3 minutes). If the session does not establish, capture the current state on both sides (Idle, Active, OpenSent, OpenConfirm) and the last reset reason. If verification fails and auto-rollback is enabled, **rollback both sides**.

### Post-Flight Checks
Confirm routes are being exchanged. Check that the near side is receiving prefixes from the far side and vice versa. Verify prefix counts are within the expected range. If route exchange looks healthy, save the running config on both devices to make the change persistent.

### Close Out
Update the change ticket with the peering details: local and remote AS, peer IPs, session state, prefix counts, and timing. Generate an evidence report with before/after BGP neighbor tables. If the peering was part of a larger provisioning request, update the parent record.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Input validation is a hard gate | Reject bad AS numbers, IPs, or missing policies | A misconfigured BGP peer can leak routes or black-hole traffic |
| Near side deploys first | If it fails, nothing to roll back on far side | Reduces the blast radius of a failed deploy |
| Both sides must be rolled back together | Partial config is worse than no config | A one-sided BGP config will never establish and creates confusion |
| Session verification has a timeout | BGP can take time to negotiate | But it should not take more than a few minutes in most cases |
| Config is saved only after verification | Not immediately after deploy | Ensures a reload will clear a bad peering if something goes wrong later |
| Duplicate peer check before deploy | Stop if peer already exists | Prevents accidental overwrite of existing sessions |

---

## 5. Scope

**In scope:** eBGP and iBGP peer addition, peer modification (update route policy, prefix limits, timers), peer removal, session verification, route exchange validation, config backup/rollback, evidence generation.

**Out of scope:** Route policy design and creation (input to this process). BGP route reflector topology design. Internet peering exchange (IX) port provisioning. BGP security (RPKI, ROA validation) setup. Traffic engineering and path manipulation. Full mesh or confederation design.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Config applied to wrong device | Peering with unintended neighbor | Validate device identity and peer IPs before deploy |
| Session never establishes | No traffic flow on new peer | Timeout with detailed state capture, auto-rollback |
| Route leak due to missing or wrong policy | Unintended traffic paths, potential outage | Validate route-map exists on both devices before deploy |
| Prefix limit exceeded immediately | Session torn down right after establishing | Check current prefix count against limit before applying |
| Far side managed by another team | Cannot deploy both sides automatically | Support "near side only" mode with instructions for far side |
| Authentication mismatch | Session stuck in Active state | Ensure both sides use the same auth config, verify in template |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on network devices | Yes | Cannot proceed |
| Generate device config from templates with variables | Yes | Cannot proceed |
| Apply config and read it back for verification | Yes | Cannot proceed |
| Backup and restore device configurations | Yes | Cannot proceed |
| Poll device state with timeout | Yes | Cannot proceed |
| Orchestrate multi-step processes with conditional rollback | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| Near-side router | Apply BGP config, verify session | Yes | Cannot proceed |
| Far-side router | Apply mirror BGP config, verify session | Depends | "Near side only" mode if not accessible |
| ITSM / ticketing (e.g., ServiceNow) | Track the change | No | Engineer tracks manually |
| IPAM (e.g., Infoblox, NetBox) | Validate peer IPs, allocate link addresses | No | Engineer provides IPs manually |
| Route policy repository | Validate route-map names exist | No | Engineer confirms policies exist |

### Discovery Questions

Ask the engineer before designing the solution:

1. Is this eBGP (between different AS) or iBGP (within the same AS)?
2. What are the local and remote AS numbers?
3. What are the peer IP addresses on both sides? IPv4, IPv6, or both?
4. What route policies (route-maps) should be applied inbound and outbound?
5. What are the prefix limits for each direction?
6. Is MD5 or TCP-AO authentication required?
7. Do you have access to configure both sides, or only the near side?
8. What device OS are the routers running? (IOS, IOS-XR, NX-OS, Junos, EOS, etc.)
9. Should the session use BFD for fast failure detection?
10. Is this a single peer addition, or do you need to provision multiple peers in batch?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One peering session at a time, verify each before moving on | Mixed device types, first-time peers |
| Grouped by router | All peers on one router at once, then verify all sessions together | Adding multiple peers to a single device |
| Parallel | Multiple independent peering sessions simultaneously | Large-scale peering buildout, IX provisioning |

For batch runs, abort if any session fails to establish and auto-rollback is enabled. Generate a summary showing per-peer status: established with prefix counts, failed with state and reason, or rolled back.

---

## 9. Acceptance Criteria

1. Invalid inputs (bad AS numbers, unreachable IPs, missing policies) are rejected before any config is deployed
2. Both devices have a config backup before any changes are made
3. BGP config is applied to both sides and verified by reading it back
4. BGP session reaches Established state within the configured timeout
5. Routes are exchanged and prefix counts are within expected range
6. If the session fails to establish, both sides are rolled back cleanly
7. Running config is saved to startup only after successful verification
8. Evidence report includes peering parameters, before/after BGP tables, session state, and prefix counts

````

============================================================
FILE: spec-files/spec-change-management.md
DIRECTORY: spec-files/
FILENAME: spec-change-management.md
============================================================
SHA256: 57dfee2c929fd1daa0c3fcbc72c412e4bb4427394142756559c284d20f13231f

````markdown
# Use Case: Change Management / Maintenance Window Orchestration

## 1. Problem Statement

Change windows are the most stressful hours in network operations. Engineers manually create tickets, wait for approvals over email, SSH into monitoring tools to suppress alerts, execute the change, check if things broke, re-enable monitoring, and update the ticket. Steps get skipped under pressure. Monitoring stays suppressed for hours after the window closes. Tickets sit in "In Progress" for days.

**Goal:** Automate the full change window lifecycle — ticket creation through close-out — so the engineer focuses on the change itself while everything around it happens reliably and in order. The actual change is pluggable: this is a wrapper that orchestrates before, during, and after.

---

## 2. High-Level Flow

```
Create/Update  →  Get Approval  →  Suppress     →  Execute    →  Verify   →  Restore     →  Close
Ticket              Gate           Monitoring      Change        Change     Monitoring     Ticket
    │                 │                │              │             │            │             │
    │                 │                │              │             │            │             │
 Open ticket,     Wait for        Put devices     Call the      Run post-   Re-enable      Update
 populate         approval or     in maint        pluggable     change      alerts,        ticket with
 details,         timeout         mode, ack       change        checks,     verify         results,
 attach plan                      suppression     process       compare     alerts are     attach
                                                                to pre-     firing         evidence
                                                                change
                                                                   │
                                                              FAIL? → Rollback + Escalate
```

---

## 3. Phases

### Ticket Creation
Create or update the change ticket with all required fields: affected devices, change type, scheduled window, risk level, and the change plan. If a ticket ID is provided as input, update the existing ticket instead of creating a new one.

### Approval Gate
Wait for the ticket to reach an approved state. Poll the ticketing system on an interval. If approval is not received within a configurable timeout (default: 4 hours), **abort and notify the engineer**. If the ticket is rejected, abort and update the ticket with the rejection reason.

### Suppress Monitoring
Place all affected devices into maintenance mode in the monitoring system. Confirm the suppression took effect. Record the suppression start time. If suppression fails, **pause and ask the engineer** — proceeding without suppression risks a flood of false alerts.

### Execute Change
Call the pluggable change process, passing it the device list, variables, and any change-specific inputs. This process is a black box to the orchestrator — it could be a software upgrade, a config push, a BGP peer addition, anything. Wait for it to complete. Capture its success/failure status and any outputs.

### Verify Change
Run post-change validation checks. These should mirror whatever pre-change checks the change process performed. Compare results. If verification fails and auto-rollback is enabled, trigger rollback within the change process. If rollback is not available, **escalate immediately**.

### Restore Monitoring
Remove maintenance mode from all affected devices. Verify alerts are flowing again. Record the suppression end time and total duration. If restore fails, **alert the engineer** — silent monitoring is dangerous.

### Close Ticket
Update the ticket with the outcome (success, failure, rolled back), attach the evidence report (timing, pre/post comparison, any errors), and transition the ticket to its final state. Calculate and record the actual change window duration.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Approval is a hard gate | Never proceed without approval | Change management compliance requires it |
| The change itself is pluggable | Orchestrator calls any change process | One wrapper handles all change types |
| Monitoring suppression is verified | Confirm maint mode before proceeding | Prevents alert storms during work |
| Monitoring restore is verified | Confirm alerts resume after work | Silent monitoring is worse than no monitoring |
| Ticket is updated at every phase | Not just at open and close | Creates a real-time audit trail |
| Timeout on every wait | Approval, change execution, reboot waits | Prevents jobs from hanging indefinitely |

---

## 5. Scope

**In scope:** Ticket lifecycle (create, update, close), approval polling, monitoring suppression and restoration, pluggable change execution, post-change verification, evidence generation, single-device and batch change windows.

**Out of scope:** The change itself (that is the pluggable process). Ticket workflow design within the ITSM tool. Approval routing rules. Monitoring tool configuration. Calendar/scheduling integration.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Approval never arrives | Change window missed | Configurable timeout with notification |
| Monitoring suppression fails silently | Alert storm during change | Verify suppression before proceeding |
| Change process hangs indefinitely | Window overruns, monitoring stays suppressed | Execution timeout, auto-restore monitoring on timeout |
| Monitoring not restored after failure | Ongoing silent monitoring | Restore monitoring in all exit paths (success, failure, abort) |
| Ticket left in wrong state | Audit trail broken | Close/update ticket in all exit paths |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Orchestrate multi-step processes with conditional logic | Yes | Cannot proceed |
| Call external processes and wait for completion | Yes | Cannot proceed |
| Poll an external system on an interval with timeout | Yes | Cannot proceed |
| Generate reports from structured data | Yes | Cannot proceed |
| Handle errors and route to different paths | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing (e.g., ServiceNow) | Ticket lifecycle, approval tracking | Yes | Cannot proceed — ticket is the audit trail |
| Monitoring (e.g., SolarWinds, PRTG, Datadog) | Suppress and restore alerts | No | Engineer manages alerts manually |
| The change process itself | Perform the actual network change | Yes | Nothing to orchestrate |

### Discovery Questions

Ask the engineer before designing the solution:

1. What ticketing system do you use? What fields are required on a change ticket?
2. How does approval work? Is it a status field on the ticket, or a separate approval record?
3. What monitoring system do you use? Does it support API-driven maintenance windows?
4. What types of changes will this orchestrate? (upgrades, config pushes, provisioning?)
5. Do you need pre-change validation, or does the pluggable change process handle that?
6. Should rollback be automatic on failure, or should it pause for engineer review?
7. What is your maximum acceptable change window duration?
8. Do you need batch support — multiple devices in one change window?
9. Are there blackout periods when changes cannot proceed even with approval?
10. What evidence do auditors require? (timing, before/after state, approval records?)

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Single window | All devices in one ticket, one suppression, one change process call | Small batch, tightly coupled devices |
| Sequential windows | Separate ticket per device, changes executed one at a time | Risk-averse, independent devices |
| Rolling | N devices at a time within one ticket, abort if failure rate > threshold | Production environments, large batches |

---

## 9. Acceptance Criteria

1. Change does not proceed without an approved ticket
2. Monitoring is confirmed suppressed before the change begins
3. The pluggable change process receives all required inputs and its outcome is captured
4. Post-change verification runs and results are recorded
5. Monitoring is restored in all exit paths — success, failure, rollback, and timeout
6. Ticket is updated with outcome and evidence in all exit paths
7. Approval timeout aborts cleanly without leaving orphaned suppression or open tickets
8. Change window duration is recorded on the ticket

````

============================================================
FILE: spec-files/spec-circuit-provisioning.md
DIRECTORY: spec-files/
FILENAME: spec-circuit-provisioning.md
============================================================
SHA256: 91acdba64031fa30cb79e867f280734b4be0c52d2e312c2dde5e73304a9636b1

````markdown
# Use Case: Circuit Provisioning (Service Turn-Up)

## 1. Problem Statement

Circuit provisioning requires coordinated configuration across two endpoints (A-side and Z-side) that must both succeed for traffic to flow. Engineers manually configure each side, test connectivity, and troubleshoot failures with no structured rollback plan. When one side fails, the other is left half-configured.

**Goal:** Automate the full circuit turn-up lifecycle — validate both endpoints, configure sequentially, verify end-to-end traffic, and roll back cleanly if anything fails — producing auditable evidence at every step.

---

## 2. High-Level Flow

```
Pre-Flight     →  Configure   →  Configure   →  Traffic        →  Close Out
(Both Sides)       A-Side         Z-Side         Verification       │
    │                │              │                │            Evidence
    │                │              │                │            report,
 Validate         Apply          Apply           Verify          update
 both devices     config,        config,          end-to-end     ticket
 are healthy,     verify         verify           data plane
 backup           A-side         Z-side
 configs          operational    operational
                                                     │
                                                FAIL? → Rollback
                                                   (Z first, then A)
```

---

## 3. Phases

### Pre-Flight (Both Sides)
Validate that both the A-side and Z-side devices are reachable, healthy, and ready for configuration. Backup the running config on each device. Confirm the target interfaces exist and are in the expected state. If either device fails pre-flight, **stop — do not configure anything**.

### Configure A-Side
Apply the circuit configuration to the A-side device. Verify the configuration was accepted and the interface is operationally correct. If A-side configuration fails, **stop — do not touch Z-side**. Roll back A-side and exit.

### Configure Z-Side
Apply the circuit configuration to the Z-side device. Verify the configuration was accepted and the interface is operationally correct. If Z-side configuration fails, **roll back Z-side first, then roll back A-side**.

### Traffic Verification
Prove end-to-end connectivity across the circuit. This means data-plane verification (ping, traceroute, or protocol neighbor adjacency), not just checking that config was applied. Compare against expected values. If traffic verification fails and retries are exhausted, **trigger rollback of both sides**.

### Rollback (conditional)
Undo configuration in reverse order: Z-side first, then A-side. Restore each device to its pre-change config. Verify each device returns to its original state. If rollback itself fails on either side, **escalate immediately**.

### Close Out
Generate an evidence report covering pre-state, applied config, post-state, and traffic test results for both sides. Update the change ticket with outcome and evidence. Report succeeds regardless of whether the circuit was provisioned or rolled back.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| A-side before Z-side (sequential) | Never configure both in parallel | If A-side fails, Z-side is untouched — simpler recovery |
| Pre-flight gates both sides | Abort if either device fails | Never half-provision a circuit |
| Rollback unwinds in reverse order | Z-side first, then A-side | Matches the order of configuration to avoid transient loops |
| Traffic verification proves data plane | Ping/traceroute/protocol adjacency, not just config check | Config can be applied correctly and still not pass traffic |
| Both sides must succeed or both roll back | No partial circuits left behind | A half-configured circuit is worse than no circuit |
| Config backup is mandatory | No backup = no provisioning | Must have a restore point for each device |
| Evidence is generated on every outcome | Success, failure, and rollback all produce reports | Audit trail is non-negotiable |

---

## 5. Scope

**In scope:** Single circuit turn-up across two endpoints, pre/post validation on both sides, sequential configuration with rollback, end-to-end traffic verification, config backup/diff, evidence generation, ITSM integration, batch provisioning of multiple circuits.

**Out of scope:** Circuit design and IP address planning (inputs to this workflow). Physical layer turn-up (fiber, cross-connects). Provider-side configuration for WAN circuits. Capacity planning. Multi-hop or multi-segment circuits requiring more than two endpoints (separate use case).

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| A-side succeeds but Z-side fails | Half-configured circuit, potential traffic black-hole | Automatic rollback of both sides in reverse order |
| Traffic verification fails despite correct config | Circuit appears down, possible physical issue | Retry with backoff; if still failing, rollback and escalate for physical investigation |
| Rollback fails on one side | One device stuck in changed state | Alert engineer immediately; do not retry indefinitely |
| Wrong interface configured | Traffic disruption on unrelated circuit | Pre-flight validates target interface state before applying config |
| Batch provisioning cascading failure | Multiple circuits left half-configured | Abort batch if failure rate exceeds threshold |
| Device unreachable mid-change | Partial config applied, unknown state | Timeout and escalate; do not attempt blind rollback |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on devices | Yes | Cannot proceed |
| Backup and diff device configurations | Yes | Cannot proceed |
| Orchestrate multi-step workflows with conditions | Yes | Cannot proceed |
| Test device reachability | Yes | Cannot proceed |
| Generate reports from templates | Yes | Cannot proceed |
| Support sequential task execution with rollback logic | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing | Track the change, audit trail | No | Engineer tracks manually |
| IPAM | Source of truth for IP addressing | No | Engineer provides addresses as input |
| Monitoring | Suppress alerts during change, restore after | No | Engineer handles manually or add a pause |
| Order management | Source of circuit parameters | No | Engineer provides parameters as input |

### Discovery Questions

Ask the engineer before designing the solution:

1. What devices are on the A-side and Z-side? What OS do they run?
2. What type of circuit is this? (point-to-point L2, L3 routed, MPLS, VXLAN, etc.)
3. What interfaces are being configured on each side?
4. Where do the circuit parameters come from? (order system, spreadsheet, manual input?)
5. What does "traffic is working" mean for this circuit? (ping, BGP neighbor up, LLDP adjacency, etc.)
6. Do you use a ticketing system? Which one?
7. Should the workflow auto-rollback on failure, or pause for engineer review?
8. Are there existing templates or automations to reuse? (config templates, backup workflows, etc.)
9. Single circuit or batch? If batch, sequential or rolling?
10. Are there maintenance window constraints or approval gates?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One circuit at a time, stop on first failure | Small batch, conservative |
| Rolling | N circuits at a time, stop if failure rate > threshold | Medium batch, production |
| Parallel | All circuits at once | Lab/non-prod only |

Each circuit is independent (its own A-side/Z-side pair), so batch orchestration is at the circuit level, not the device level.

---

## 9. Acceptance Criteria

1. Provisioning only proceeds if both A-side and Z-side pass pre-flight checks
2. A-side is configured and verified before Z-side is touched
3. Z-side is only configured if A-side succeeds
4. End-to-end traffic verification confirms data-plane connectivity, not just config presence
5. If any step fails, both sides are rolled back to pre-change state (Z first, then A)
6. Config backup exists for both devices before and after the change
7. Evidence report is generated for every run — success, failure, or rollback
8. Batch mode respects configured concurrency and aborts if failure rate exceeds threshold
9. No partial circuits are left behind — both sides succeed or both revert

````

============================================================
FILE: spec-files/spec-cloud-security-groups.md
DIRECTORY: spec-files/
FILENAME: spec-cloud-security-groups.md
============================================================
SHA256: 4e4474b384b85014a4bce1d15f15b74bd7e8c8cb25ae4a92dbceed5db6d61537

````markdown
# Use Case: Cloud Security Group Management

## 1. Problem Statement

Cloud security group rules are the perimeter firewall of every cloud workload, but they're managed through tickets and manual console clicks. Engineers copy-paste rules from spreadsheets, mistype CIDR blocks, open ports too broadly, and create conflicting or redundant rules. There's no blast-radius analysis before a change — one overly permissive rule can expose an entire subnet. Cleanup never happens, so rule sets grow until nobody understands what's allowed and why. Auditors ask for evidence and get screenshots.

**Goal:** Automate the lifecycle of cloud security group rules — create, update, and delete rules with conflict detection, blast-radius analysis, and post-change verification — across AWS Security Groups, Azure NSGs, and GCP firewall rules, producing auditable evidence for every change.

---

## 2. High-Level Flow

```
Request        →  Analyze       →  Deploy        →  Verify        →  Close Out
    │                 │                │                │                │
    │                 │                │                │                │
 Parse rule        Check for       Apply rule      Confirm rule     Update
 request:          conflicts,      change to       is active,       ticket,
 action, CIDR,     overlaps,       the cloud       test traffic     record
 port, protocol,   blast-radius    provider        flow matches     evidence,
 direction,        assessment,     API, tag        expected         notify
 target group      approval gate   the rule        behavior         requestor
                       │                                │
                  CONFLICT? →                      FAIL? → Rollback
                  Flag + pause                     rule change
```

---

## 3. Phases

### Request
Parse the incoming rule change: action (create, update, delete), target security group or NSG, rule direction (ingress/egress), protocol, port range, source/destination CIDR or security group reference, and justification. Validate the inputs — reject malformed CIDRs, invalid port ranges, or rules that reference non-existent groups. If the request is incomplete, **stop and ask for clarification**.

### Analyze
Evaluate the proposed change against the existing rule set. Detect conflicts: does this rule overlap with an existing rule? Does it contradict a deny rule? Does it widen access beyond what's intended? Perform blast-radius analysis: how many instances or workloads are affected by this security group? What other groups reference this one? Present findings to the requestor. If the blast radius exceeds a defined threshold or a conflict is detected, **require explicit approval before proceeding**.

### Deploy
Apply the rule change through the cloud provider's API. For creates, add the rule with proper tagging (owner, ticket, expiration date). For updates, modify in place or replace the rule. For deletes, remove the rule. Capture the before and after state of the security group. If the API call fails, **retry once, then abort and report**.

### Verify
Confirm the rule is active in the cloud provider's state. Query the security group and validate the rule exists (or was removed) with the correct parameters. Optionally run a connectivity test — attempt traffic on the affected port/CIDR and confirm it's allowed or denied as expected. If verification fails and auto-rollback is enabled, **revert the rule change**.

### Close Out
Generate an evidence report: the before-state, the change made, the after-state, blast-radius summary, and verification results. Update the change ticket. Notify the requestor. If the rule has an expiration date, schedule a future review or auto-deletion.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Blast-radius analysis before every change | Mandatory, not optional | One rule can affect hundreds of instances silently |
| Conflict detection flags, does not auto-resolve | Human decides on conflicts | Conflicts often indicate a design misunderstanding |
| Rules are tagged with owner, ticket, and expiration | Every rule has metadata | Enables cleanup, audit, and accountability |
| Before/after state captured for every change | Snapshot the full security group | Enables diff, rollback, and evidence |
| Expiration dates trigger automatic review | Schedule future cleanup | Prevents rule sprawl over time |

---

## 5. Scope

**In scope:** Create, update, and delete rules on AWS Security Groups, Azure NSGs, and GCP firewall rules. Conflict detection. Blast-radius analysis (instance count, cross-group references). Rule tagging. Post-change verification. Rollback on failure. Evidence generation. Expiration-based lifecycle.

**Out of scope:** Web application firewall (WAF) rules. Network ACLs (AWS) or route table changes. Cross-account or cross-subscription rule management (requires additional trust setup). Firewall-as-a-service (Palo Alto, Fortinet cloud). Security group creation/deletion (this manages rules within existing groups). Policy-as-code authoring (rules are provided as input, not generated).

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Overly permissive rule deployed (0.0.0.0/0) | Workload exposed to internet | Flag broad CIDRs, require explicit approval for /0 rules |
| Rule conflicts create unpredictable behavior | Traffic allowed or denied unexpectedly | Pre-deploy conflict detection against existing rules |
| Blast radius larger than expected | Change affects production workloads | Blast-radius threshold triggers approval gate |
| Cloud API rate limiting during batch changes | Partial rule set deployed | Implement backoff and retry, rollback partial on abort |
| Stale rules accumulate over months | Security posture degrades | Expiration tags, scheduled review reminders |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Call cloud provider APIs (AWS, Azure, GCP) | Yes | Cannot proceed |
| Query existing security group rules | Yes | Cannot proceed |
| Determine which instances are bound to a security group | Yes (for blast-radius) | Skip blast-radius analysis, proceed with warning |
| Tag cloud resources with metadata | Yes | Rules created without traceability tags |
| Orchestrate multi-step workflows with approval gates | Yes | Cannot proceed |
| Test network connectivity on specific ports | No | Skip connectivity verification, rely on API state only |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| Cloud provider API (AWS, Azure, GCP) | Apply and query security group rules | Yes | Cannot proceed |
| ITSM / ticketing (e.g., ServiceNow) | Track change request, audit trail | No | Evidence report returned directly |
| CMDB / cloud inventory (e.g., ServiceNow, CloudHealth) | Identify affected workloads for blast-radius | No | Blast-radius based on cloud API instance query only |
| Approval system | Gate high-risk changes | No | Manual approval via pause/resume |

### Discovery Questions

Ask the engineer before designing the solution:

1. Which cloud provider and account/subscription/project is the target?
2. What is the action? (Create a new rule, modify an existing rule, delete a rule?)
3. What is the target security group or NSG name/ID?
4. What is the rule? (Direction, protocol, port range, source/destination CIDR or group reference?)
5. What is the justification or ticket number for this change?
6. Should the rule have an expiration date? If so, when?
7. What blast-radius threshold should require approval? (e.g., more than 10 instances affected?)
8. Should broad rules (0.0.0.0/0, ::/0) be allowed, or always flagged?
9. Should the workflow auto-rollback on verification failure, or pause for review?
10. Are there existing security policies or naming conventions to follow for rule tags?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One rule change at a time, stop on first failure | Default for production changes |
| Grouped | All rules for one security group at once, atomic rollback | Application onboarding with multiple rules |
| Parallel | Rules across independent security groups simultaneously | Multi-application deployment, no shared groups |

---

## 9. Acceptance Criteria

1. Rule is created, updated, or deleted as requested with correct parameters
2. Conflict detection identifies overlapping or contradictory rules before deploy
3. Blast-radius analysis reports the number of affected instances and cross-group references
4. Changes exceeding the blast-radius threshold require explicit approval
5. Broad CIDR rules (0.0.0.0/0) are flagged and require explicit approval
6. Every rule is tagged with owner, ticket, and expiration date
7. Before and after security group state is captured for every change
8. Verification confirms the rule is active (or removed) in the cloud provider's state
9. Evidence report is generated for every change, regardless of outcome

````

============================================================
FILE: spec-files/spec-config-backup-compliance.md
DIRECTORY: spec-files/
FILENAME: spec-config-backup-compliance.md
============================================================
SHA256: b914ea07952b29a203d20963e8daa3d8d843c4e0d964cb9c66290b942c86ce77

````markdown
# Use Case: Device Configuration Backup & Compliance

## 1. Problem Statement

Network device configurations change constantly — planned maintenance, emergency fixes, undocumented tweaks at 2 AM. Most teams have no reliable way to know what changed, when it changed, or whether the current config still meets their standards. Config backups are ad hoc. Drift detection is manual diffing. Unauthorized changes go unnoticed until something breaks.

**Goal:** Automate scheduled and on-demand config backups across multi-vendor devices, maintain versioned config history, detect drift from a defined baseline, and alert when configurations deviate from compliance standards.

---

## 2. High-Level Flow

```
Schedule/Trigger  →  Collect Configs  →  Store & Version  →  Compliance Check  →  Report & Alert
       │                   │                   │                    │                    │
       │                   │                   │                    │                    │
   Cron, on-demand,    Connect to          Save config          Compare current      Generate drift
   or change-event     each device,        with timestamp,      config against       report, alert
   trigger             pull running        detect if changed    baseline/standard,   on violations,
                       config              since last backup    grade compliance     update ticket
                                                                    │
                                                               DRIFT? → Flag & Notify
```

---

## 3. Phases

### Trigger
Backups run on a schedule (daily, weekly), on demand, or triggered by an external event (e.g., change ticket closed, syslog config-change trap). The trigger determines which devices to target — all devices, a device group, or a specific list.

### Collect Configurations
Connect to each target device and retrieve the running configuration. Handle multi-vendor differences — different commands, different output formats. If a device is unreachable, **log the failure and continue with the rest**. Do not let one unreachable device block the entire batch.

### Store & Version
Save each collected config with a timestamp. Compare against the previously stored version. If the config has changed, store the new version and record a diff. If unchanged, skip — do not create duplicate entries. Maintain a configurable retention window (e.g., 90 days, 50 versions).

### Compliance Check
Compare the current config against a defined compliance baseline. The baseline is a set of rules — required lines that must be present, forbidden lines that must not exist, patterns that must match. Grade each device: compliant, non-compliant, or partially compliant. Flag specific violations with line-level detail.

### Report & Alert
Generate a summary report: devices backed up, devices unreachable, configs changed since last run, compliance scores. Alert on drift (config changed outside a change window), alert on compliance violations. Optionally update a ticket or CMDB record.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Unreachable devices do not block the batch | Log failure, continue | One down device should not prevent backing up the other 500 |
| Only store configs that changed | Compare before writing | Avoids bloated storage and makes change history meaningful |
| Compliance is a separate phase from backup | Decouple collection from evaluation | Backups are useful even without compliance; compliance can run independently against stored configs |
| Baseline is defined as rules, not a golden config file | Rules are composable and partial | Different device roles need different rules; a monolithic golden config is too rigid |
| Drift alerting is time-aware | Distinguish planned vs unplanned changes | A config change during a change window is expected; the same change at 3 AM is not |

---

## 5. Scope

**In scope:** Scheduled and on-demand backup of running configs, versioned storage with diff, compliance checking against a rule-based baseline, drift detection and alerting, summary reporting, multi-vendor support.

**Out of scope:** Config remediation (separate use case — this detects, it does not fix). Startup config vs running config reconciliation. Configuration deployment or push. Backup of non-network devices (servers, cloud resources).

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Device unreachable during backup window | Missing config snapshot | Retry once after delay, log failure, include in report |
| Credentials expired or rotated | Backup fails for all devices using that credential | Validate credentials before starting batch, fail fast with clear error |
| Large device count overwhelms collection | Timeouts, partial results | Batch with concurrency limits, stagger collection |
| Compliance baseline is stale or incomplete | False positives/negatives | Review and version baselines alongside config changes |
| Storage grows unbounded | Disk/DB pressure | Enforce retention policy, prune old versions automatically |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on multi-vendor devices | Yes | Cannot proceed |
| Store and retrieve versioned configuration text | Yes | Cannot proceed |
| Compare two config versions and produce a diff | Yes | Cannot proceed |
| Evaluate config text against a set of compliance rules | Yes | Manual compliance review |
| Schedule recurring jobs | Yes | Engineer triggers manually each time |
| Send notifications (email, webhook, chat) | No | Engineer checks reports manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing | Log backup results, flag drift as incidents | No | Engineer reviews reports manually |
| CMDB | Record last-known config state per device | No | Config history lives only in backup store |
| Monitoring / alerting | Receive drift and compliance alerts | No | Engineer checks reports on schedule |
| Syslog / event collector | Trigger backup on config-change events | No | Rely on scheduled backups only |

### Discovery Questions

Ask the engineer before designing the solution:

1. How many devices need to be backed up? What vendors and OS types?
2. How often should backups run? (daily, weekly, after every change?)
3. Is there an existing config repository or should we start fresh?
4. What does your compliance baseline look like today? Written rules, a reference config, tribal knowledge?
5. Do you need to distinguish between planned changes (during a change window) and unplanned drift?
6. How long should config history be retained?
7. Where should alerts go — email, Slack/Teams, ticketing system?
8. Are there device groups with different compliance standards? (e.g., core routers vs access switches)
9. Do you have a syslog or event source that signals config changes in real time?
10. Are there existing backup scripts or processes to replace or integrate with?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One device at a time | Small inventory, conservative |
| Parallel (throttled) | N devices at a time (e.g., 20 concurrent) | Large inventory, production — most common |
| Group-based | Backup one device group at a time | Different groups have different schedules or compliance baselines |

---

## 9. Acceptance Criteria

1. Running configs are collected from all reachable devices in the target scope
2. Unreachable devices are logged and reported, not silently skipped
3. Configs are only stored when they differ from the previous version
4. A diff is available for every config change
5. Compliance check produces a per-device pass/fail with specific violation details
6. Drift outside a change window triggers an alert
7. Summary report is generated for every backup run
8. Retention policy is enforced — old versions are pruned automatically

````

============================================================
FILE: spec-files/spec-config-drift-remediation.md
DIRECTORY: spec-files/
FILENAME: spec-config-drift-remediation.md
============================================================
SHA256: 2685952de631fb7e039283c117e769f2723fef14b3d75dbd5996fa749c70cc4b

````markdown
# Use Case: Multi-Vendor Config Drift Detection & Remediation

## 1. Problem Statement

Device configurations drift from their intended state constantly — ad-hoc changes, emergency fixes, copy-paste errors, and forgotten temporary rules accumulate until the running config no longer matches what it should be. Teams discover drift only when something breaks or an audit flags it. Remediating drift manually across hundreds of multi-vendor devices is slow, inconsistent, and risky. There's no systematic way to know *what* drifted, *how bad* it is, and *whether it's safe to fix automatically*.

**Goal:** Automate scheduled scanning of device configs against a golden/intended standard, classify deviations by severity, auto-remediate low-risk drift, and ticket high-risk drift for human review — keeping the network in a known-good state continuously.

---

## 2. High-Level Flow

```
Scan  →  Compare  →  Classify  →  Decide  →  Remediate / Ticket  →  Report
  │          │           │           │               │                  │
  │          │           │           │               │                  │
Collect    Diff        Tag each    Low-risk:      Apply fix,         Drift
running    against     deviation   auto-fix.      verify config.     summary,
config     golden/     as low,     High-risk:     Or create          score,
from all   intended    medium,     create         ticket with        trending,
devices    standard    or high     ticket for     drift details      evidence
                       severity    review         for engineer
                                                      │
                                                 FAIL? → Rollback, escalate
```

---

## 3. Phases

### Scan
Collect the running configuration from every device in scope — routers, switches, firewalls, load balancers, across all vendors. Organize results by device group, site, or role. If a device is unreachable, **log it, skip it, and continue** — one unreachable device should not block the entire scan.

### Compare
Diff each device's running config against its golden/intended standard. The standard may be a full config template, a set of required config sections, or a set of rules (e.g., "NTP servers must be X and Y", "SNMP community must not be 'public'"). Produce a structured diff: what's missing, what's extra, what's wrong.

### Classify
Tag each deviation with a severity level. **Low** — cosmetic or operational preference (description mismatch, logging level). **Medium** — functional but non-critical (suboptimal timer, missing secondary NTP). **High** — security or stability risk (wrong ACL, SNMP community 'public', missing route-map, unauthorized user account). Classification rules are defined in the standard, not guessed at runtime.

### Decide
Route each deviation based on severity. Low-risk deviations go to auto-remediation. Medium-risk deviations go to auto-remediation if a confidence flag is set, otherwise to a ticket. High-risk deviations **always go to a ticket for human review** — never auto-remediate high-risk drift.

### Remediate
For deviations approved for auto-remediation: generate the corrective config, apply it to the device, and verify the drift is resolved by re-scanning that section. If remediation fails or introduces new errors, **rollback the change and escalate to a ticket**.

### Ticket
For deviations routed to human review: create a ticket with the device name, the specific drift, the expected vs. actual config, the severity, and the suggested fix. Group related deviations into a single ticket per device to avoid ticket flood.

### Report
Produce a drift report: how many devices scanned, how many had drift, breakdown by severity, what was auto-remediated, what was ticketed, overall compliance score, and trend vs. previous scan. Store the report for audit purposes.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| High-risk drift is never auto-remediated | Always routed to human review | Security and stability changes demand human judgment |
| One unreachable device does not block the scan | Log and continue | Partial visibility is better than no visibility |
| Classification is defined in the standard, not runtime | Severity baked into golden config rules | Consistent, auditable, not subject to runtime judgment |
| Remediation is verified by re-scan | Apply fix then re-diff that section | Confirms the fix actually resolved the drift |
| Tickets are grouped per device | One ticket per device, multiple deviations | Avoids ticket flood; gives engineer full device context |

---

## 5. Scope

**In scope:** Routers, switches, firewalls, load balancers. Multi-vendor (Cisco, Arista, Juniper, Palo Alto, F5, etc.). Scheduled and on-demand scanning. Config diff against golden/intended standard. Severity classification. Auto-remediation for low-risk drift. Ticketing for high-risk drift. Compliance scoring and trending. Rollback on failed remediation.

**Out of scope:** Defining the golden config standard itself (input to this workflow — assumed to exist). Firmware/OS-level compliance (separate use case). Physical layer checks (cabling, optics). Real-time config change detection via syslog/streaming (this is scheduled scanning, not event-driven).

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Auto-remediation introduces a new issue | Service disruption | Verify by re-scan after fix; rollback if new drift appears |
| Golden standard has errors | False positives, unnecessary changes | Standard is versioned and reviewed; deviations flagged as exceptions |
| Large-scale drift overwhelms ticketing | Ticket flood, alert fatigue | Group deviations per device; summarize in a single drift report |
| Remediation on a firewall disrupts traffic | Security or connectivity outage | Firewalls classified as high-risk by default; no auto-remediation |
| Drift re-introduced by manual changes after remediation | Wasted effort, repeat drift | Trend reports highlight repeat offenders; feed back into change control |

---

## 7. Requirements

### What the automation must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Collect running config from multi-vendor devices | Yes | Cannot proceed |
| Diff config against a golden/intended standard | Yes | Cannot proceed |
| Apply corrective config commands to devices | Yes | All drift is ticketed (no auto-remediation) |
| Roll back config changes on failure | Yes | Engineer rolls back manually |
| Classify deviations by severity | Yes | All drift treated as high-risk (ticket everything) |
| Generate reports with compliance scores | Yes | Cannot proceed |
| Schedule scans on a recurring basis | Yes | Engineer triggers manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| Golden config / standards repository | Source of intended config | Yes | Cannot proceed |
| ITSM / ticketing | Create tickets for high-risk drift | No | Engineer reviews drift report manually |
| CMDB / inventory | Device list, groups, roles, sites | No | Engineer provides device list manually |
| Monitoring / alerting | Notify on scan completion or drift detected | No | Engineer checks reports manually |

### Discovery Questions

Ask the engineer before designing the solution:

1. What device types are in scope? (Routers, switches, firewalls, load balancers?)
2. What vendors and OS types? (Cisco IOS/NX-OS, Arista EOS, Juniper Junos, Palo Alto PAN-OS, F5?)
3. Do you have a golden config or intended config standard defined today?
4. How is the standard structured? (Full config templates, section-based rules, line-by-line checks?)
5. How should severity be classified? Do you have existing severity definitions?
6. Which categories of drift are safe to auto-remediate? Which require human review?
7. How often should scans run? (Daily, weekly, on-demand?)
8. What ticketing system should receive high-risk drift?
9. How many devices are in scope? Are they grouped by site, role, or region?
10. Do you want compliance scores and trending over time?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Full scan | All devices in scope, sequential or parallel collection | Scheduled weekly/daily scan |
| By device group | Scan one group at a time (e.g., by site or role) | Large environments, staggered scanning |
| Single device | Scan and remediate one device on demand | Ad-hoc checks or post-change validation |

---

## 9. Acceptance Criteria

1. Running config is collected from all reachable devices in scope
2. Config diff correctly identifies deviations from the golden standard
3. Each deviation is classified by severity (low, medium, high)
4. Low-risk deviations are auto-remediated and verified by re-scan
5. High-risk deviations are routed to a ticket with full context (device, deviation, expected vs. actual, suggested fix)
6. Failed remediation triggers rollback and escalation
7. Compliance score is calculated per device and across the fleet
8. Drift report is generated for every scan with trending vs. previous scans
9. Unreachable devices are logged but do not block the scan

````

============================================================
FILE: spec-files/spec-device-decommissioning.md
DIRECTORY: spec-files/
FILENAME: spec-device-decommissioning.md
============================================================
SHA256: 581ce951d165ebaee15c5eeb27c32384f165098ba169a6494f15126bee71ab1b

````markdown
# Use Case: Device Decommissioning

## 1. Problem Statement

When a network device reaches end-of-life or is replaced, engineers must remove it from every system that knows about it: monitoring, IPAM, CMDB, inventory, device groups, and more. This is done manually, system by system, and steps get missed. The result is orphaned records — monitoring alerts for devices that no longer exist, stale IPAM reservations blocking new allocations, CMDB entries that erode trust in the inventory. Months later, someone discovers the ghost and has to figure out what happened.

**Goal:** Automate the full decommissioning lifecycle — final backup, systematic removal from all systems, archive, and close-out — ensuring no orphaned references survive.

---

## 2. High-Level Flow

```
Validate    →  Final     →  Remove from   →  Remove from  →  Remove from  →  Archive   →  Close
Device        Backup       Monitoring       IPAM            Inventory       & Cleanup     Out
   │            │               │               │               │               │           │
   │            │               │               │               │               │           │
 Confirm     Take final      Remove          Release         Remove from    Archive       Update
 device      config &        device from     all IP          CMDB, remove   configs,      ticket,
 exists,     state           monitoring,     addresses,      from device    record        generate
 get all     backup,         confirm no      subnets,        groups, mark   final         evidence
 current     record          active alerts   DNS records     as decom'd     state         report
 refs        serial/asset    remain          remain
```

---

## 3. Phases

### Validate Device
Confirm the device exists in inventory and is the correct device (match hostname, serial number, or asset tag). Gather all current references: which monitoring groups include it, what IPs are assigned, what device groups it belongs to, what CMDB records exist. This reference list drives the removal phases. If the device cannot be found, **stop — do not guess**.

### Final Backup
Take a final configuration backup and capture the device state (interfaces, routing table, inventory/serial info). This is the last known good state and must be preserved for audit purposes. Label this backup explicitly as "decommission final." If backup fails because the device is already unreachable, **log the failure but continue** — the device may already be powered off.

### Remove from Monitoring
Remove the device from the monitoring system. Confirm it is no longer being polled. Verify no active alerts remain for this device. If removal fails, **retry once, then flag for manual cleanup** — do not leave a device being monitored that no longer exists.

### Remove from IPAM
Release all IP address reservations associated with the device. Remove any DNS records pointing to the device. Confirm the addresses are returned to the available pool. If partial removal occurs (some IPs released, some not), **log what succeeded and what failed** — do not leave ambiguous state.

### Remove from Inventory
Remove the device from the CMDB or inventory system. Remove it from all device groups it belongs to. If the organization's policy is to mark as decommissioned rather than delete, update the status instead. Confirm no active references remain in any group.

### Archive and Cleanup
Move all configuration backups to long-term archive storage. Record the decommission date, the engineer who authorized it, and the final device state. Remove any temporary files or staging data created during the process.

### Close Out
Update or close the decommission ticket. Generate an evidence report listing every system the device was removed from, what was archived, and any items that require manual follow-up. Include the full reference list from the validate phase and the removal confirmation from each phase.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Validate collects all references first | Build a removal checklist before starting | Ensures nothing is missed |
| Final backup is attempted but not a hard gate | Continue if device is unreachable | Device may already be powered down |
| Each removal phase confirms success | Not just fire-and-forget | Orphaned references are the core problem to solve |
| Partial failures are logged, not hidden | Report shows what succeeded and what needs manual cleanup | Transparency over silent failure |
| Archive before delete | Configs preserved in long-term storage | Audit and forensic needs |
| Device groups cleaned up explicitly | Not just CMDB removal | Group membership is often a separate system |

---

## 5. Scope

**In scope:** Device validation, final config/state backup, removal from monitoring, IPAM, DNS, CMDB/inventory, device groups. Config archival, evidence generation, ticket management.

**Out of scope:** Physical decommissioning (rack-and-stack removal). Cable management updates. License reclamation. Circuit decommissioning (separate use case). Asset disposal tracking. Power and cooling adjustments.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Wrong device decommissioned | Production outage | Validate with serial number or asset tag, not just hostname |
| Removal from one system fails | Orphaned reference persists | Per-system confirmation, clear report of what failed |
| Device still handling traffic | Service interruption | Pre-check for active sessions, routing adjacencies, or traffic counters |
| IPAM records not fully released | Address space leak | Enumerate all IPs from device before removal, verify each is released |
| Backup fails, no archive | Audit gap | Attempt backup, log failure, check if recent backups exist in archive |
| Device group membership missed | Stale group references | Enumerate all group memberships during validate phase |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Query device inventory and retrieve device details | Yes | Cannot proceed |
| Backup device configurations | Yes | Cannot proceed (attempt is mandatory even if it fails) |
| Remove or update records in external systems via API | Yes | Cannot proceed |
| Orchestrate multi-step processes with error handling | Yes | Cannot proceed |
| Generate reports from structured data | Yes | Cannot proceed |
| Archive files to long-term storage | No | Engineer archives manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| CMDB / inventory | Remove device record or mark as decommissioned | Yes | Cannot ensure clean decommission |
| Monitoring (e.g., Nagios, Zabbix, SolarWinds) | Remove device from polling | No | Engineer removes manually, log as follow-up |
| IPAM (e.g., Infoblox, NetBox) | Release IP reservations, remove DNS | No | Engineer releases manually, log as follow-up |
| ITSM / ticketing (e.g., ServiceNow) | Track the decommission request | No | Engineer tracks manually |
| Archive storage | Long-term config backup retention | No | Configs remain in primary backup system |

### Discovery Questions

Ask the engineer before designing the solution:

1. What systems does this device exist in? (monitoring, IPAM, CMDB, others?)
2. How do you identify the device uniquely? Hostname, serial number, asset tag?
3. Is the device still reachable, or has it already been powered off?
4. Should the device record be deleted or marked as decommissioned in the CMDB?
5. Are there DNS records that need to be removed?
6. What device groups does this device belong to?
7. Where should archived configs be stored? How long must they be retained?
8. Is there an active ticket, or should one be created?
9. Is this a single device or a batch decommission?
10. Are there dependent devices or circuits that must be decommissioned together?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One device at a time, full lifecycle per device | Small batch, careful audit trail per device |
| Grouped | Batch devices by site or role, process each group together | Site decommission, hardware refresh |
| Parallel | Multiple devices simultaneously, independent removal | Lab teardown, large-scale decommission |

For batch runs, generate a summary report showing per-device status: fully decommissioned, partially decommissioned (with details of what remains), or failed.

---

## 9. Acceptance Criteria

1. Device identity is confirmed before any removal begins
2. Final configuration backup is attempted and result is recorded
3. Device is removed from monitoring and no active alerts remain for it
4. All IP addresses are released and DNS records are removed
5. Device is removed from CMDB/inventory or marked as decommissioned per policy
6. Device is removed from all device groups
7. Configs are archived to long-term storage
8. Evidence report lists every system touched, every action taken, and any manual follow-ups required
9. No orphaned references remain in any integrated system

````

============================================================
FILE: spec-files/spec-device-onboarding.md
DIRECTORY: spec-files/
FILENAME: spec-device-onboarding.md
============================================================
SHA256: 33715efbb82531b9c8efaf3f7bd45d303c578f24dbcf078c82d7a85787c0f10f

````markdown
# Use Case: Device Onboarding (Day-0 / Day-1)

## 1. Problem Statement

Adding a new device to the network is a multi-team, multi-system process. Engineers manually configure base settings (NTP, AAA, SNMP, syslog, DNS, banners), then update IPAM, monitoring, and inventory systems one at a time. Each step is a different tool, a different login, a different ticket. Devices sit in limbo for hours or days between racking and being fully operational. Mistakes in base config lead to security gaps or blind spots in monitoring.

**Goal:** Automate the full onboarding lifecycle — from initial reachability through base configuration, system registration, and verification — so that a device goes from powered-on to production-ready in minutes with zero manual touch.

---

## 2. High-Level Flow

```
Discovery  →  Base Config  →  Register  →  Enable Monitoring  →  Verify  →  Close Out
    |              |              |               |                  |            |
    |              |              |               |                  |            |
 Confirm        Apply          Add to          Add device        Ping,        Update
 device is      NTP, AAA,      IPAM,           to monitoring     SSH,         ticket,
 reachable,     SNMP, DNS,     update          system,           validate     generate
 identify       syslog,        inventory       configure         AAA login,   evidence
 platform/      banner,        system          alert             check SNMP   report
 OS type        save config                    thresholds        response
                    |
               FAIL? → Quarantine & alert
```

---

## 3. Phases

### Discovery
Confirm the device is reachable over the management network. Identify the platform type and OS version (e.g., IOS-XE, NX-OS, EOS, JunOS). Collect baseline facts: hostname, serial number, management IP, model. If the device is unreachable, **stop — flag for physical layer troubleshooting**.

### Base Configuration (Day-1)
Apply the standard configuration template for the identified platform. This includes NTP servers, AAA (TACACS+/RADIUS), SNMP communities/v3 users, syslog destinations, DNS resolvers, and login banners. Save the configuration. If any section fails to apply, **stop and quarantine the device** — do not proceed with a partially configured device.

### Register
Add the device to IPAM with the assigned management IP, subnet, and site metadata. Create or update the device record in the network inventory system with hostname, model, serial, OS version, and site. If IPAM or inventory registration fails, retry once, then flag for manual review.

### Enable Monitoring
Add the device to the monitoring platform. Configure standard alert thresholds (CPU, memory, interface utilization, reachability). Suppress initial burn-in alerts for a configurable window (default 15 minutes) to avoid noise during settling.

### Verify
Run end-to-end validation: ping the management IP, SSH into the device, authenticate via AAA (not local credentials), poll SNMP, confirm syslog messages are arriving at the collector, and verify NTP is synchronized. If any check fails, **flag the device as partially onboarded and alert the engineer**.

### Close Out
Generate an onboarding evidence report: device facts, config applied, systems registered, verification results. Update the change ticket with the outcome. Mark the device as production-ready in inventory.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Platform auto-detection before config push | Identify OS type first, select matching template | One workflow handles all vendors |
| Base config is all-or-nothing | Abort on partial failure | A half-configured device is worse than an unconfigured one |
| IPAM and inventory registration before monitoring | Device must have proper records before alerting starts | Prevents orphaned alerts |
| Post-onboarding verification is mandatory | Must prove every system integration works | Catches silent failures (e.g., wrong SNMP community) |
| Evidence report generated for every device | Success or failure | Audit trail for every onboarding |

---

## 5. Scope

**In scope:** Physical and virtual device onboarding across vendors. Base config application (Day-1). IPAM registration. Inventory registration. Monitoring enrollment. End-to-end verification. Evidence generation. Batch onboarding of multiple devices.

**Out of scope:** Physical racking and cabling (Day-0 physical). ZTP/DHCP bootstrap (separate process that feeds into this workflow). Advanced service configuration (Day-2). Firewall rule provisioning. Certificate enrollment. License activation.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Device unreachable after racking | Onboarding blocked | Auto-detect and flag immediately, don't queue silently |
| Wrong platform detected | Incorrect config template applied | Verify platform facts against expected values before pushing config |
| AAA server unreachable during config push | Device locked out | Ensure local fallback credentials exist in base template |
| IPAM record conflict (IP already assigned) | Registration fails | Check for conflicts before creating, flag for resolution |
| Monitoring floods with alerts on new device | Alert fatigue | Suppress alerts during configurable burn-in window |

---

## 7. Requirements

### What the automation must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Connect to devices via SSH/NETCONF | Yes | Cannot proceed |
| Detect device platform and OS type | Yes | Engineer provides platform manually |
| Render and apply config templates per platform | Yes | Cannot proceed |
| Register records in external systems via API | Yes | Engineer registers manually |
| Validate device reachability and management plane | Yes | Cannot proceed |
| Generate reports from collected data | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| IPAM (e.g., Infoblox, NetBox) | IP address registration and management | Yes | Engineer updates manually |
| Inventory / CMDB (e.g., ServiceNow, Nautobot) | Device record of truth | Yes | Engineer updates manually |
| Monitoring (e.g., Datadog, Zabbix, SolarWinds) | Add device to alerting | No | Engineer adds device manually |
| ITSM / ticketing | Track the onboarding change | No | Engineer tracks manually |
| AAA server (TACACS+/RADIUS) | Validate authentication works | Yes | Verification step is incomplete |

### Discovery Questions

Ask the engineer before designing the solution:

1. What types of devices are you onboarding? What OS families?
2. Do you have standard base config templates per platform, or do they need to be created?
3. What IPAM system do you use? Is there an API available?
4. What is your inventory system of record?
5. What monitoring platform do you use?
6. Do you use TACACS+ or RADIUS for AAA?
7. Should the workflow handle both physical and virtual devices?
8. Is there an existing ZTP process that precedes this workflow?
9. Single device or batch? If batch, are they typically the same platform?
10. What ticketing system should be updated on completion?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One device at a time, stop on first failure | Small batch, first-time rollout |
| Rolling | N devices at a time, continue on individual failure | Medium batch, mixed platforms |
| Parallel | All at once | Large batch of identical devices (same model, same site) |

---

## 9. Acceptance Criteria

1. Device platform and OS are correctly identified before config is applied
2. Base configuration (NTP, AAA, SNMP, syslog, DNS, banner) is fully applied and saved
3. Device is registered in IPAM with correct IP and metadata
4. Device record exists in inventory with hostname, model, serial, and OS version
5. Device is enrolled in monitoring with standard alert thresholds
6. Post-onboarding verification confirms SSH, AAA, SNMP, syslog, and NTP all work
7. Evidence report is generated for every device (success or failure)
8. Batch mode respects concurrency limits and handles individual failures without blocking the batch

````

============================================================
FILE: spec-files/spec-dns-record-management.md
DIRECTORY: spec-files/
FILENAME: spec-dns-record-management.md
============================================================
SHA256: 0c199f7a44c580804c60b92dec9e1942ce684b47ce6cd7fdf123d69bbb1d30f5

````markdown
# Use Case: DNS Record Management

## 1. Problem Statement

DNS record changes are error-prone and invisible. Engineers make changes through provider consoles or scripts with no conflict checking, no propagation verification, and no audit trail. A bad record can take down services, and nobody knows who changed what or when. Rollback means finding the old value in someone's notes.

**Goal:** Automate DNS record CRUD with conflict detection, propagation verification, optional TTL orchestration, and automatic rollback on failure -- producing a complete audit trail of every change.

---

## 2. High-Level Flow

```
Pre-Flight  →  Approval  →  TTL Staging  →  Execute  →  Verify  →  Restore TTL  →  Close Out
    │          (prod only)   (optional)      Change     Propagation   (optional)        │
    │                                          │            │                            │
 Validate                                   Apply        Query                       Evidence
 zone exists,                               record       resolvers                   report,
 no conflicts,                              change,      to confirm,                 update
 format checks,                             sync PTR     configurable                ticket
 snapshot existing                          (optional)   max wait
                                                            │
                                                       FAIL? → Rollback
                                                               (restore snapshot)
```

---

## 3. Phases

### Pre-Flight
Validate the requested change before touching DNS. Confirm the zone exists and the provider is reachable. Check for conflicts: does a record already exist (for creates)? Does it exist (for updates/deletes)? Enforce CNAME exclusivity per RFC 1034 -- no CNAME where other types exist, no CNAME at the zone apex. Validate IP format for A/AAAA records. If reverse record sync is requested, confirm the reverse zone exists. Snapshot the existing record for rollback. If any critical check fails, **stop**.

### Approval
Production zone changes require human approval before proceeding. Non-production zones skip this gate entirely. The approver sees the pre-check report and change summary.

### TTL Staging (optional, best-effort)
Lower the TTL on the existing record to a short value (e.g., 300s) so caches drain faster before the actual change. This is best-effort: if it fails, proceed with a warning. **Never block the workflow waiting for the old TTL to expire.** Ideally, TTL lowering happens well in advance of the change window as a separate pre-staging step. Skipped for create operations (no existing record).

### Execute Change
Apply the DNS record change (create, update, or delete) via the provider API. If reverse record sync is enabled and this is an A/AAAA record, create or update the corresponding PTR record. If IPAM sync is enabled, update the IPAM system. Trigger DNSSEC re-signing if the zone is signed (the provider handles signing; the workflow just triggers it).

### Propagation Verification
Query DNS resolvers to confirm the change is live. Check the authoritative nameservers first (must pass), then recursive resolvers (best-effort). Poll at intervals up to a configurable maximum wait time (default 10 minutes). **Verification works by querying resolvers, not by sleeping for a fixed duration.** If the authoritative check fails after the timeout, trigger rollback.

### TTL Restoration (optional)
After successful verification, restore the TTL to the desired long-term value. Verify the TTL update took effect.

### Rollback (conditional)
If verification fails and rollback is enabled, restore the previous record value from the snapshot taken during pre-flight. For creates, delete the new record. Re-verify the rollback succeeded. If reverse or IPAM sync was done, revert those too. If rollback itself fails, **escalate immediately**.

### Close Out
Generate an evidence report with before/after snapshots, propagation results, and timing. Update the change ticket. Write an immutable audit log entry.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Conflict detection before any change | Pre-flight checks for existing records, CNAME exclusivity, IP format | Prevent DNS corruption; catch mistakes before they propagate |
| TTL staging is optional and best-effort | Never blocks for full old TTL; proceeds with warning if lowering fails | Old TTLs can be hours or days; blocking is impractical |
| Propagation verified by querying resolvers | Polls authoritative + recursive resolvers, not a fixed sleep | Actual confirmation, not a guess based on TTL math |
| Rollback reverts to snapshot | Previous record value captured before change | Guaranteed known-good state to restore |
| Production zones require approval | Non-prod auto-proceeds | Matches change management discipline without slowing dev |
| Reverse record sync is non-blocking | PTR failure logs a warning and creates a follow-up ticket | Don't roll back a successful forward record for a PTR failure |
| IPAM sync is non-blocking | IPAM failure logs a warning and creates a follow-up ticket | DNS change is the primary objective |
| Batch records have independent success/failure | One bad record doesn't kill the batch | Maximizes throughput; failures are individually reported |
| Evidence is generated regardless of outcome | Success, failure, and rollback all produce a report | Audit trail is non-negotiable |

---

## 5. Scope

**In scope:** CRUD operations for A, AAAA, CNAME, MX, TXT, SRV, PTR, NS records. Multi-provider support (Infoblox, Route53, Cloudflare, Azure DNS, BIND, Windows DNS). Conflict detection. TTL staging. Propagation verification. Rollback. Forward/reverse record sync. IPAM sync. Approval for production zones. Audit trail. Bulk operations (CSV import, provider migration).

**Out of scope:** Zone creation and delegation. DNSSEC key management and rotation. DNS server installation or patching. Resolver/cache configuration. Domain registration and renewal. SSL/TLS certificate management.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Propagation takes longer than expected | Stale records served to clients | Poll resolvers up to configurable max wait; don't rely on fixed sleep |
| Provider API unavailable during change | Change cannot be applied | Retry with backoff, abort if still down; no partial state since change hasn't been applied |
| Rollback fails | Bad record persists | Critical alert, immediate escalation; never retry indefinitely |
| CNAME conflict not detected | DNS resolution breaks for the name | Pre-flight enforces RFC 1034 exclusivity before any change |
| Batch operation overwhelms provider | Rate limiting, throttled API calls | Enforce per-provider rate limits; configurable batch abort threshold |
| Split-horizon DNS targets wrong view | Change applied to wrong internal/external view | Discovery question captures which view; provider adapter targets explicitly |
| DNSSEC re-sign fails after change | Validating resolvers return SERVFAIL | Alert engineer; record is correct but unsigned |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Create/update/delete DNS records via provider API | Yes | Cannot proceed |
| Query existing DNS records for conflict detection | Yes | Cannot proceed |
| Perform DNS lookups from multiple vantage points | Yes | Cannot proceed -- no propagation verification |
| Orchestrate multi-step workflows with conditions and loops | Yes | Cannot proceed |
| Render templates for reports and PTR name derivation | Yes | Cannot proceed |
| Parse CSV for bulk operations | No | Batch mode unavailable; single-record still works |
| Manual approval gate | No | All changes auto-proceed; add controls outside the workflow |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| DNS provider (Infoblox, Route53, Cloudflare, etc.) | Authoritative source for zone data; receives CRUD calls | Yes | Cannot proceed |
| IPAM system (NetBox, Infoblox IPAM, etc.) | IP validation and forward/reverse sync | No | Skip IPAM checks; engineer manages manually |
| ITSM / ticketing | Track changes, audit trail, production approvals | No | Engineer tracks manually |
| Monitoring / alerting | Notify on DNS changes or failures | No | Engineer monitors manually |

### Discovery Questions

1. What DNS provider do you use? (Infoblox, Route53, Cloudflare, Azure DNS, BIND, Windows DNS?)
2. What zone are you modifying? Does it already exist?
3. What record types do you need to manage? (A, AAAA, CNAME, MX, TXT, SRV, PTR, NS?)
4. Is this a production or non-production zone? Do you need an approval step?
5. Is DNSSEC enabled on this zone?
6. Do you need reverse (PTR) record synchronization for A/AAAA changes?
7. Do you have an IPAM system? Which one?
8. Is this a single record change or a bulk operation?
9. Do you want to pre-stage TTL lowering before the change window?
10. What are your propagation verification requirements? (Authoritative only? Specific resolvers?)
11. Do you use split-horizon DNS (internal vs external views)?
12. Do you use a ticketing system? Which one?
13. Are there existing automations you'd like to reuse? (DNS workflows, IPAM sync, ticket creation?)

---

## 8. Bulk Operations

Bulk mode accepts a list of records (directly or via CSV import) and runs each through the single-record workflow independently. Records are grouped by zone and provider. Each record succeeds or fails on its own -- one failure does not kill the batch. Rate limits are respected per provider. If the failure rate exceeds a configurable threshold (default 20%), the batch aborts.

For provider migrations (moving all records from one provider to another), the workflow exports records from the source, validates them against the destination, executes the import, and verifies each record. NS delegation cutover is out of scope and flagged for manual action.

---

## 9. Acceptance Criteria

1. Pre-flight detects and blocks conflicting record creates (e.g., CNAME where A record exists)
2. Pre-flight validates IP format and rejects invalid addresses
3. Create, update, and delete operations produce the correct DNS state verified by authoritative query
4. Propagation is verified by querying resolvers, not by sleeping for a fixed duration
5. Rollback restores the previous record value when propagation verification fails
6. TTL staging lowers TTL before the change and restores it after -- without blocking for the old TTL
7. Reverse (PTR) record is created when forward A record is created with sync enabled
8. Production zone changes are blocked until approval is granted
9. Evidence report is generated for every run (success, failure, or rollback)
10. Batch mode processes records independently, respects rate limits, and aborts on configurable failure threshold

````

============================================================
FILE: spec-files/spec-firewall-rule-lifecycle.md
DIRECTORY: spec-files/
FILENAME: spec-firewall-rule-lifecycle.md
============================================================
SHA256: dd4a7d3fd6674ba12f24096a734cf4a6678de41a859ad37fc6d74425a7e420d7

````markdown
# Use Case: Firewall Rule Lifecycle

## 1. Problem Statement

Firewall rules accumulate. Teams request new rules urgently, security reviews them in a spreadsheet, engineers deploy them manually, and nobody cleans them up. Over time, rule bases become bloated with shadowed rules, expired exceptions, and conflicting entries. Recertification is a quarterly nightmare of chasing down rule owners. Decommissioning a rule takes as long as creating one.

**Goal:** Automate the full firewall rule lifecycle — request, validate, deploy, verify, recertify, and decommission — across network firewalls, ensuring every rule is conflict-free, auditable, and has an expiration date.

---

## 2. High-Level Flow

```
Request  →  Validate  →  Approve  →  Deploy  →  Verify  →  Recertify  →  Decommission
   │            │           │           │           │            │              │
   │            │           │           │           │            │              │
 Source,     Check for    Security    Push rule   Confirm      Periodic       Remove
 dest, port, conflicts,   review,    to target   rule is      review:        expired
 protocol,  shadowed     approve/    firewall,   active,      owner          rules,
 justifi-   rules,       reject     commit       traffic      confirms       verify
 cation,    syntax                               matches      still needed   removal,
 expiry     valid                                expected     or expire      audit log
                │
           CONFLICT? → Reject with details
```

---

## 3. Phases

### Request Intake
Accept the rule request: source, destination, port/protocol, action (permit/deny), justification, requested duration, and rule owner. Every rule must have an owner and an expiration date — no permanent rules without explicit exception approval.

### Validate
Check the proposed rule against the existing rule base. Detect conflicts: does this rule contradict an existing rule? Is it shadowed by a broader rule that already permits/denies the same traffic? Is the syntax valid for the target firewall? Check that source and destination objects exist in the firewall's address book. If conflicts are found, **reject the request with a detailed explanation of what conflicts and why**.

### Approve
Route the validated request to the security team for review. Include the validation results, conflict analysis, and risk assessment. The approver can approve, reject, or request modification. No rule deploys without approval.

### Deploy
Push the approved rule to the target firewall. Insert it at the correct position in the rule base (order matters — firewalls evaluate rules top-down). Commit the change. If the firewall rejects the rule, **capture the error and report it — do not retry blindly**.

### Verify
Confirm the rule is active in the firewall's running rule base. Optionally, generate test traffic or check logs to confirm the rule permits/blocks as expected. Compare the deployed rule against the approved request to ensure nothing was altered during deployment.

### Recertify (periodic)
On a schedule (e.g., every 90 days), notify rule owners that their rules are approaching expiration. The owner must confirm the rule is still needed. If confirmed, extend the expiration. If not confirmed within the grace period, **mark the rule for decommission**.

### Decommission
Remove expired or rejected rules from the firewall. Disable the rule first (if the platform supports it), wait a monitoring period to catch unexpected traffic drops, then delete. Generate an audit record of the removal. If disabling the rule causes alerts or traffic issues, **re-enable and escalate**.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Every rule has an expiration date | No permanent rules by default | Prevents rule base bloat; exceptions require explicit approval |
| Conflict detection before approval | Reject shadowed/conflicting rules early | Saves security team from reviewing rules that cannot work |
| Rule position matters | Insert at specified position, not just append | Firewall rule order determines match behavior — appending may never match |
| Decommission uses disable-then-delete | Two-step removal with monitoring period | Catches dependencies before permanent removal |
| Recertification is automated | System notifies owners, auto-expires unconfirmed rules | Removes the quarterly manual audit burden |

---

## 5. Scope

**In scope:** Rule request and validation, conflict and shadow detection, approval workflow, deployment to network firewalls, post-deploy verification, periodic recertification, rule decommission, audit trail.

**Out of scope:** Cloud security groups and NACLs (similar concept, different mechanics — separate use case). Firewall policy design or architecture. URL filtering and application-layer rules. NAT rule management. Firewall firmware upgrades.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Rule deployed at wrong position | Traffic permitted or denied incorrectly | Validate position before deploy, verify post-deploy |
| Conflict detection misses a shadowed rule | Redundant or ineffective rule deployed | Use firewall-native conflict analysis where available, supplement with custom checks |
| Rule decommission breaks production traffic | Outage for dependent applications | Disable-then-delete with monitoring period; re-enable on alert |
| Rule owner unreachable during recertification | Rule expires, potentially dropping needed traffic | Grace period with escalation to owner's manager and security team |
| Firewall commit fails after rule push | Rule in candidate config but not active | Detect commit failure, remove uncommitted rule, report clearly |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Push configuration to network firewalls | Yes | Cannot proceed |
| Read the current rule base from firewalls | Yes | Cannot proceed |
| Detect conflicts and shadowed rules | Yes | Security team reviews manually (high risk) |
| Orchestrate multi-step workflows with approvals | Yes | Cannot proceed |
| Schedule recurring jobs (recertification) | Yes | Manual recertification process |
| Send notifications to rule owners | Yes | Manual outreach for recertification |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing | Track rule requests, approvals, audit trail | No | Approval tracked via email or internal process |
| IPAM / address management | Validate source/destination objects exist | No | Engineer validates addresses manually |
| CMDB | Map firewalls to network zones and applications | No | Engineer identifies the correct firewall manually |
| Monitoring / SIEM | Detect traffic impact after rule changes | No | Disable-then-delete monitoring period is manual |

### Discovery Questions

Ask the engineer before designing the solution:

1. What firewall vendors are in scope? (Palo Alto, Fortinet, Check Point, Cisco ASA/FTD, Juniper SRX, etc.)
2. How is the rule base organized today — zones, policies, contexts?
3. Does the firewall support candidate configs and commits, or are changes immediate?
4. Is there an existing approval process? Where does it live — ticketing system, email, manual?
5. What is the desired rule expiration policy? (e.g., 90 days default, 1 year max)
6. How do you handle rule recertification today?
7. Are there rules that should never be auto-decommissioned? (e.g., infrastructure rules)
8. Do you use address objects/groups, or raw IPs in rules?
9. What is the acceptable monitoring period before deleting a disabled rule?
10. How many firewalls and how many rules per firewall are we managing?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Single rule | One rule request through the full lifecycle | Standard operational requests |
| Batch deploy | Multiple approved rules deployed to the same firewall in one commit | Bulk changes from a project or migration |
| Batch recertification | All rules expiring within a window reviewed together | Quarterly or monthly recertification cycles |

---

## 9. Acceptance Criteria

1. Rule requests are validated for conflicts and shadows before reaching approval
2. Conflicting rules are rejected with a clear explanation of the conflict
3. No rule is deployed without documented approval
4. Deployed rules are verified as active in the firewall's running rule base
5. Rules are inserted at the correct position, not blindly appended
6. Every rule has an owner and an expiration date
7. Owners are notified before rule expiration and given a window to recertify
8. Unconfirmed rules are disabled, monitored, then removed
9. Decommissioned rules are re-enabled if disabling causes traffic issues
10. Full audit trail exists for every rule: request, approval, deploy, recertify, decommission

````

============================================================
FILE: spec-files/spec-incident-auto-remediation.md
DIRECTORY: spec-files/
FILENAME: spec-incident-auto-remediation.md
============================================================
SHA256: 859078bca74e99a43ec64c25520e05550766ab26c142d8e5a5413e6fc3cf372a

````markdown
# Use Case: Incident Auto-Remediation

## 1. Problem Statement

When a monitoring alert fires at 2 AM, the on-call engineer wakes up, VPNs in, reads the alert, SSHes into the device, runs the same diagnostic commands they always run, applies the same fix they applied last time, and closes the ticket. Most network incidents fall into a handful of well-known categories — interface flaps, high CPU, memory exhaustion, BGP neighbor down — and the remediation steps are documented in runbooks that engineers follow manually. This is slow, error-prone, and expensive.

**Goal:** Automatically detect, classify, and remediate common network incidents using predefined playbooks — fixing known issues in seconds instead of hours, and escalating unknown or failed remediations to humans with full diagnostic context.

---

## 2. High-Level Flow

```
Alert Ingestion  →  Classify  →  Match Playbook  →  Remediate  →  Verify  →  Close Out
      |                |               |                 |            |            |
      |                |               |                 |            |            |
   Receive          Determine       Look up          Execute       Re-check     Update
   alert from       incident        known fix        remediation   the alert    ticket,
   monitoring,      type,           for this         steps from    condition,   generate
   create/update    severity,       category         the matched   confirm      evidence
   ticket           affected        and context      playbook      resolved     report
                    device
                         |                                |
                    No match? →  Escalate           FAIL? → Escalate
```

---

## 3. Phases

### Alert Ingestion
Receive the alert from the monitoring system (webhook, event bus, or polling). Extract key fields: device, alert type, severity, timestamp, and any included metrics. Create or update an incident ticket. If the alert is a duplicate of an already-open incident, **correlate and skip — do not spawn parallel remediations for the same issue**.

### Classify
Determine the incident category from the alert data. Common categories: interface flap, high CPU, high memory, BGP neighbor down, OSPF adjacency lost, link down, device unreachable, certificate expiring. Identify the affected device, interface, or protocol session. Assign a severity level.

### Match Playbook
Look up a remediation playbook for the classified incident type and device platform. A playbook defines the diagnostic commands, the remediation steps, and the verification checks. If no playbook matches, **escalate to a human immediately with the classification details and raw alert data**. Do not attempt to improvise a fix.

### Remediate
Execute the playbook steps on the affected device. This might be clearing a BGP neighbor, bouncing an interface, freeing memory by restarting a process, or adjusting a threshold. Capture the output of every command. If the remediation step fails to execute, **stop and escalate — do not retry destructive commands blindly**.

### Verify
Re-check the original alert condition. Is the interface stable? Has CPU dropped below threshold? Is the BGP session re-established? Compare against the alert trigger criteria. If the condition persists after remediation, **escalate to a human with the full diagnostic output and remediation log**.

### Close Out
Update the incident ticket with the timeline: alert received, classification, playbook executed, verification result. Generate an evidence report with before/after state, commands executed, and output. Close the ticket if verified. If escalated, attach all context and assign to the appropriate team.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| No playbook = no action | Escalate immediately if unrecognized | Never guess at a fix on production devices |
| Deduplication before classification | Correlate alerts to avoid parallel fixes | Two alerts for the same BGP drop should not trigger two remediations |
| Remediation is single-attempt by default | Do not retry failed fixes automatically | Retrying a failed fix can make things worse |
| Verification uses the same criteria as the alert | Re-check the original trigger condition | Proves the specific problem is resolved, not just that the device responds |
| Every incident produces a report | Success, failure, and escalation all documented | Post-incident review and audit trail |

---

## 5. Scope

**In scope:** Alert ingestion from monitoring. Incident classification. Playbook matching and execution. Single-device remediation. Post-remediation verification. Ticket creation/update/closure. Evidence generation. Escalation path for unknown or failed remediations.

**Out of scope:** Playbook authoring and approval (input to this process). Multi-device correlated incidents (e.g., upstream router failure causing downstream alerts). Root cause analysis across incidents. Capacity planning. Monitoring system configuration.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Alert storm triggers dozens of remediations simultaneously | Device overload, conflicting fixes | Deduplicate and throttle — one active remediation per device at a time |
| Misclassification leads to wrong playbook | Incorrect fix applied | Classify conservatively; escalate if confidence is low |
| Remediation causes a secondary outage | Wider impact than original alert | Capture device state before remediation; keep rollback context |
| Monitoring system goes down | Alerts stop flowing | Health-check the alert ingestion pipeline; alert on silence |
| Playbook becomes stale after OS upgrade | Remediation commands fail | Version-tag playbooks by platform and OS; fail gracefully on command errors |

---

## 7. Requirements

### What the automation must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Receive and parse alerts from monitoring systems | Yes | Cannot proceed |
| Execute CLI commands on network devices | Yes | Cannot proceed |
| Match incidents against a playbook catalog | Yes | Cannot proceed |
| Orchestrate multi-step conditional workflows | Yes | Cannot proceed |
| Create and update tickets in a ticketing system | No | Engineer tracks manually |
| Generate reports from templates | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| Monitoring (e.g., Datadog, PagerDuty, Zabbix) | Source of alerts | Yes | No alerts to process |
| ITSM / ticketing (e.g., ServiceNow, Jira) | Incident tracking and audit trail | No | Engineer tracks manually |
| Playbook catalog / knowledge base | Stores remediation procedures per incident type | Yes | Cannot match or execute fixes |
| CMDB / inventory | Device context (platform, OS, site, criticality) | No | Classification relies solely on alert data |

### Discovery Questions

Ask the engineer before designing the solution:

1. What monitoring system generates the alerts? How are they delivered (webhook, email, API)?
2. What are the top 5-10 incident types you see most often?
3. Do you have documented runbooks for those incident types today?
4. What ticketing system do you use for incident management?
5. What device platforms and OS families are in scope?
6. Are there devices or environments that should never be auto-remediated (e.g., core routers)?
7. What is the escalation path when automation cannot fix the issue?
8. Should the system attempt remediation on critical-severity alerts, or only medium/low?
9. Do you want a human approval gate before remediation, or fully automatic?
10. How do you want to be notified of escalations? (page, email, chat, ticket assignment)

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Per-device serialized | One remediation at a time per device, queue others | Always — prevents conflicting fixes on the same device |
| Cross-device parallel | Remediate different devices concurrently | Default for unrelated alerts across different devices |
| Throttled | Cap total concurrent remediations at N | Alert storms, large-scale events |

---

## 9. Acceptance Criteria

1. Alerts are received and deduplicated — no parallel remediations for the same incident
2. Incidents are classified by type, device, and severity
3. Matching playbook is selected and executed for known incident types
4. Unknown incident types are escalated immediately with full alert context
5. Remediation failure triggers escalation — no silent failures
6. Verification confirms the original alert condition is resolved
7. Incident ticket is created, updated throughout, and closed (or escalated) with full timeline
8. Evidence report is generated for every incident (resolved, failed, or escalated)

````

============================================================
FILE: spec-files/spec-ipam-lifecycle.md
DIRECTORY: spec-files/
FILENAME: spec-ipam-lifecycle.md
============================================================
SHA256: 8cf66014d0468b2e8f1c91f3b2a24dcf2298ee8a6632f57ea641b9af3168f4a8

````markdown
# Use Case: IP Address Management Lifecycle

## 1. Problem Statement

IP address management is tracked in spreadsheets, scattered across IPAM tools, and never reconciled against what is actually configured on the network. Addresses are allocated but never reclaimed. Subnets run out while stale entries sit unused. DNS records drift from reality. Duplicate IPs cause outages that take hours to diagnose because nobody has a single source of truth.

**Goal:** Automate the full IP lifecycle — allocate, assign, track, and reclaim — integrated with DNS and DHCP, validated against live network state, so that the IPAM system always reflects reality and conflicts are caught before they cause outages.

---

## 2. High-Level Flow

```
Allocate     →  Assign     →  Track      →  Reclaim     →  Close Out
    │              │             │              │              │
    │              │             │              │              │
 Reserve        Create        Periodic       Detect         Release
 next           DNS           scan:          stale/unused   IP in IPAM,
 available      records,      verify IP      addresses,     remove DNS
 IP/subnet      update        in use,        confirm        records,
 in IPAM,       DHCP          check DNS      not in use,    update
 validate       scope,        matches,       notify         DHCP,
 no conflict    configure     detect         owner          generate
                device        conflicts                     report
```

---

## 3. Phases

### Allocate
Receive a request for an IP address or subnet (size, site, VLAN, purpose). Query the IPAM system for the next available address in the appropriate scope. Validate the candidate IP is not already in use — ping sweep and ARP check on the network segment. If a conflict is detected, **skip that address and try the next**. Reserve the address in IPAM with requestor, date, and purpose metadata.

### Assign
Create the corresponding DNS records: forward (A/AAAA) and reverse (PTR). If DHCP is involved, create or update the DHCP reservation/scope. Apply the IP configuration to the target network device interface if applicable. Verify the assignment is consistent: IPAM record matches DNS matches device config.

### Track
Run periodic reconciliation scans. For every allocated IP: is it responding on the network? Does the DNS record still resolve correctly? Does the device config match IPAM? Flag discrepancies: IP allocated in IPAM but not found on network (potentially stale), IP found on network but not in IPAM (rogue/shadow IT), DNS record pointing to wrong IP (drift). Generate a reconciliation report.

### Reclaim
Identify addresses that have been unused beyond a configurable threshold (default 90 days). Notify the owner/requestor with a grace period. If no response or confirmation of non-use, release the IP: remove DNS records (forward and reverse), remove DHCP reservation, update IPAM status to available. If the address IS still in use but was flagged, update the last-seen timestamp and keep it.

### Close Out
Generate a lifecycle report: what was allocated, when, to whom, current state. Update any tickets or CMDBs. For subnet-level operations, update utilization metrics.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Ping + ARP check before allocation | Always verify, even if IPAM says available | IPAM may be stale — the network is the source of truth for conflicts |
| DNS records created with the allocation | Not deferred to later | Prevents DNS gaps that cause troubleshooting headaches |
| Reclamation requires owner notification | No silent deletion | Avoids pulling an IP out from under a running service |
| IPv4 and IPv6 handled by the same process | Unified lifecycle regardless of version | Prevents two parallel manual processes |
| Conflict detection runs continuously, not just at allocation | Periodic scan catches drift | Conflicts introduced outside the process are still detected |

---

## 5. Scope

**In scope:** IPv4 and IPv6 address allocation, subnet allocation, DNS record management (forward and reverse), DHCP scope/reservation management, conflict detection (duplicate IP), stale address reclamation, reconciliation reporting, IPAM system integration.

**Out of scope:** IPAM system installation or migration. DHCP server deployment. DNS server deployment. Layer 2 VLAN provisioning (separate use case). BGP/OSPF route management for new subnets. NAT/PAT configuration. IP planning and subnet design (input to this process).

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Allocating a duplicate IP | Service outage for existing device | Ping sweep + ARP check before committing; never trust IPAM alone |
| Reclaiming an IP that is actually in use | Service outage | Owner notification with grace period; verify via network scan before release |
| DNS record drift from actual IP assignments | Name resolution failures, misdirected traffic | Periodic reconciliation scan catches drift; alert on mismatches |
| IPAM system unavailable during allocation | Cannot allocate IPs | Queue requests and retry; fallback to manual allocation with post-sync |
| Subnet exhaustion not detected early | Emergency requests cannot be fulfilled | Track utilization metrics; alert when subnet crosses threshold (e.g., 80%) |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Query and update IPAM records via API | Yes | Cannot proceed |
| Create and delete DNS records (A, AAAA, PTR) | Yes | Engineer manages DNS manually |
| Execute network scans (ping, ARP) on target subnets | Yes | Cannot validate — conflict detection disabled |
| Orchestrate multi-step workflows with conditions | Yes | Cannot proceed |
| Schedule periodic jobs (reconciliation scans) | Yes | Engineer triggers scans manually |
| Generate reports from templates | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| IPAM (Infoblox, NetBox, BlueCat, phpIPAM, etc.) | Source of truth for IP allocation | Yes | Cannot proceed |
| DNS server (BIND, Windows DNS, Infoblox DNS, etc.) | Forward and reverse record management | Yes | Engineer manages DNS manually |
| DHCP server (ISC DHCP, Infoblox, Windows, etc.) | Reservation and scope management | No | Static assignments only |
| Network devices (routers, switches) | Verify IPs on the wire, apply interface configs | No | Allocation only, no device config |
| ITSM / ticketing (ServiceNow, etc.) | Track requests and changes | No | Engineer tracks manually |
| CMDB | Update asset records with IP assignments | No | IPAM serves as record |

### Discovery Questions

Ask the engineer before designing the solution:

1. Which IPAM system do you use? (Infoblox, NetBox, BlueCat, phpIPAM, other?)
2. Do you manage both IPv4 and IPv6, or just one?
3. How are DNS records managed today? Same system as IPAM or separate?
4. Do you use DHCP reservations, or are assignments purely static?
5. What metadata do you track per IP? (owner, purpose, site, VLAN, expiration?)
6. How do you handle IP requests today? Tickets, email, self-service portal?
7. What is your threshold for "stale" addresses? (30 days, 90 days, custom?)
8. Are there subnets that should be excluded from automated reclamation? (infrastructure, management, etc.)
9. Do you need conflict detection for existing allocations, or only for new requests?
10. Do you use a ticketing system? Which one?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One IP/subnet at a time, stop on first conflict | On-demand allocation requests |
| Bulk allocation | Allocate a range of IPs from a subnet, validate batch, commit all at once | New site/VLAN provisioning |
| Scheduled scan | Sweep all allocated IPs in a subnet, report discrepancies | Periodic reconciliation (daily/weekly) |
| Stale reclamation | Process all candidates past threshold, notify in batch, reclaim after grace period | Monthly hygiene cycle |

For reconciliation scans, process one subnet at a time to avoid overwhelming the network with scan traffic. For bulk allocation, validate the entire batch for conflicts before committing any.

---

## 9. Acceptance Criteria

1. No IP is allocated without a conflict check (ping + ARP) against the live network
2. IPAM record, DNS record, and device config are consistent after assignment
3. Forward (A/AAAA) and reverse (PTR) DNS records are created with every allocation
4. Duplicate IPs detected on the network are flagged and reported immediately
5. Stale addresses are only reclaimed after owner notification and grace period
6. Reclamation removes IPAM reservation, DNS records, and DHCP entries
7. Reconciliation report identifies IPAM-vs-network discrepancies for every scanned subnet
8. Subnet utilization alerts fire when usage crosses the configured threshold
9. IPv4 and IPv6 addresses follow the same lifecycle process
10. Evidence report is generated for every allocation, reclamation, and reconciliation run

````

============================================================
FILE: spec-files/spec-load-balancer-vip.md
DIRECTORY: spec-files/
FILENAME: spec-load-balancer-vip.md
============================================================
SHA256: 043db32838c7bcdec7c8334ac22a89c2a61d2e813b61ed20a00bf2ce06dce7d2

````markdown
# Use Case: Load Balancer VIP Provisioning

## 1. Problem Statement

Provisioning a new Virtual IP (VIP) on a load balancer is a multi-step, error-prone process. Engineers must create the VIP, define a server pool, add pool members with correct ports, attach health monitors, configure persistence profiles, and bind it all together. Every load balancer platform has different terminology and workflows. Mistakes — wrong port, missing health monitor, typo in a pool member IP — cause outages for the application team waiting on the VIP. There's no consistency between requests, and no verification that the VIP actually works before handing it off.

**Goal:** Automate end-to-end VIP provisioning across any load balancer platform — define the VIP, pool, members, health monitor, and persistence profile from a single request, verify the VIP is serving traffic, and produce evidence for the application team.

---

## 2. High-Level Flow

```
Validate       →  Build         →  Deploy        →  Verify        →  Close Out
    │                 │                │                │                │
    │                 │                │                │                │
 Check inputs,     Assemble        Push config      Test VIP        Update
 resolve IPs,      VIP, pool,      to the load      responds,       ticket,
 confirm pool      members,        balancer,        health          notify
 members are       monitor,        activate         monitors        requestor,
 reachable,        persistence                      pass, pool      record
 no IP             into a                           members         evidence
 conflicts         config set                       healthy
                                                        │
                                                   FAIL? → Rollback VIP
```

---

## 3. Phases

### Validate
Confirm all inputs are complete and consistent. Resolve hostnames to IPs if needed. Verify pool member IPs are reachable from the load balancer network. Check for IP conflicts — is the requested VIP address already in use? Verify the target load balancer is reachable and the requested partition/tenant exists. If any critical validation fails, **stop — do not push partial config**.

### Build
Assemble the full configuration set: VIP (address, port, protocol), server pool (name, load balancing method), pool members (IP, port, weight, priority group), health monitor (type, interval, timeout, expected response), and persistence profile (source-IP, cookie, SSL session). The configuration is platform-neutral at this stage — a standard input format that gets translated to platform-specific syntax during deploy.

### Deploy
Push the assembled configuration to the target load balancer. Create objects in dependency order: health monitor first, then pool with monitor attached, then pool members, then VIP bound to the pool with persistence. If any step fails mid-deploy, **roll back all objects created so far** to avoid orphaned config.

### Verify
Confirm the VIP is functional. Check that the VIP is active and listening. Check that pool members show as healthy according to the attached monitor. Optionally send a synthetic test request through the VIP and verify the response. If verification fails and auto-rollback is enabled, **remove the VIP and all associated objects**.

### Close Out
Record the provisioned VIP details (address, port, pool members, monitor type). Update the service request or change ticket. Notify the application team with connection details. Generate evidence showing the VIP is live and healthy.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Platform-neutral input format | Single request schema for all LB platforms | Requestors don't need to know LB internals |
| Deploy in dependency order | Monitor → Pool → Members → VIP | Avoids broken references during creation |
| Rollback on partial deploy failure | Remove all objects created in this run | No orphaned config left behind |
| Verification includes synthetic test | Optional health probe through VIP | Proves end-to-end path, not just config exists |
| IP conflict check before deploy | Query LB and IPAM for existing VIPs | Prevents silent conflicts that cause outages |

---

## 5. Scope

**In scope:** VIP creation with pool, members, health monitor, and persistence profile. Platform-specific translation for F5, Citrix ADC, NSX-ALB, HAProxy, and cloud ALBs (AWS ALB/NLB, Azure LB, GCP LB). IP conflict detection. Post-deploy verification. Rollback on failure. ITSM ticket update. Evidence report.

**Out of scope:** SSL certificate management (separate lifecycle). DNS record creation for the VIP (separate use case). WAF policy attachment. Global server load balancing (GSLB) across sites. Capacity planning or LB selection. Modifying existing VIPs (update/delete is a separate workflow).

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| VIP IP conflict with existing entry | Traffic blackholed or split | Pre-deploy check against LB config and IPAM |
| Pool member unreachable | VIP active but no healthy backends | Pre-validate member reachability, flag before deploy |
| Health monitor misconfigured | Members marked down incorrectly | Verify monitor parameters match application protocol |
| Partial deploy leaves orphaned objects | Config drift, confusing cleanup | Rollback all objects on any mid-deploy failure |
| Platform API unavailable during deploy | Incomplete provisioning | Retry with backoff, abort and rollback after max retries |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Configure load balancer objects via API or CLI | Yes | Cannot proceed |
| Query existing LB config for conflict detection | Yes | Cannot proceed |
| Test network reachability to pool member IPs | Yes | Skip pre-validation, risk deploying to unreachable members |
| Orchestrate multi-step workflows with rollback | Yes | Cannot proceed |
| Translate platform-neutral input to vendor-specific config | Yes | Cannot proceed |
| Send synthetic HTTP/TCP requests for verification | No | Skip synthetic test, rely on LB health status only |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| IPAM (e.g., Infoblox, NetBox) | IP conflict check, VIP address allocation | No | Manual IP provided, conflict check limited to LB only |
| ITSM / ticketing (e.g., ServiceNow) | Track service request, audit trail | No | Evidence report returned to requestor directly |
| DNS (e.g., Infoblox, Route53) | Create A/CNAME record for VIP | No | DNS handled separately |
| CMDB | Resolve application-to-server mappings for pool members | No | Pool members provided explicitly in request |

### Discovery Questions

Ask the engineer before designing the solution:

1. Which load balancer platform and version? (F5 BIG-IP, Citrix ADC, NSX-ALB, cloud?)
2. What partition, tenant, or virtual server group should the VIP be created in?
3. What is the VIP address and port? Is the IP pre-allocated or should it be requested from IPAM?
4. What protocol does the application use? (HTTP, HTTPS, TCP, UDP?)
5. What are the pool members? (IP:port pairs, weights, priority groups?)
6. What load balancing method? (round-robin, least-connections, IP-hash?)
7. What health monitor type? (HTTP 200 check, TCP connect, custom URI?)
8. Do you need session persistence? What type? (source-IP, cookie, SSL session?)
9. Should the workflow auto-rollback the VIP on verification failure, or pause for review?
10. Is there a service request or change ticket to update?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One VIP at a time, stop on first failure | Default for production, safest |
| Parallel | Multiple VIPs simultaneously on different LBs | Multi-site deployments, independent targets |
| Rolling | N VIPs at a time, pause between batches | Large application rollout across shared LBs |

---

## 9. Acceptance Criteria

1. VIP is created with the correct address, port, and protocol
2. Server pool is created with the correct load balancing method
3. All pool members are added with correct IP, port, and weight
4. Health monitor is attached and pool members show as healthy
5. Persistence profile is configured as requested
6. No IP conflicts exist with pre-existing VIPs
7. Synthetic test through the VIP returns an expected response (if enabled)
8. Partial deploy failure results in full rollback with no orphaned objects
9. Evidence report is generated with VIP details, pool member status, and verification results

````

============================================================
FILE: spec-files/spec-network-compliance-audit.md
DIRECTORY: spec-files/
FILENAME: spec-network-compliance-audit.md
============================================================
SHA256: 0bcd0f3ea9e878c4a1bc3760c0081f6f3ff46c8b6384779592a340e04c7a368b

````markdown
# Use Case: Network Compliance Audit

## 1. Problem Statement

Network teams must prove their devices meet security baselines and regulatory standards (PCI-DSS, SOX, HIPAA, NIST, CIS benchmarks). Today this means an engineer manually pulls configs from hundreds of devices, eyeballs them against a spreadsheet of required settings, writes up exceptions, and produces a report for the auditor. It takes weeks, it's inconsistent, and by the time the report is done, configs have already drifted. Violations discovered late in the audit cycle are expensive to remediate under time pressure.

**Goal:** Continuously scan device configurations against defined compliance standards, grade every device, produce audit-ready reports, and optionally auto-remediate violations — turning compliance from a quarterly fire drill into an always-current posture.

---

## 2. High-Level Flow

```
Define Standards  →  Collect Configs  →  Evaluate  →  Grade  →  Report  →  Remediate
      |                    |                |           |           |            |
      |                    |                |           |           |            |
   Build or            Pull running     Compare      Score       Generate    Optionally
   import              config from      each         each        audit-      push fixes
   compliance          every device     config       device      ready       for
   rules per           in scope         against      (pass /     report      violations,
   standard                             applicable   partial /   with        re-scan
   and platform                         rules        fail)       drill-down  to confirm
                                                                    |
                                                               VIOLATIONS? → Flag or auto-fix
```

---

## 3. Phases

### Define Standards
Express each compliance requirement as a machine-evaluable rule. Group rules into standards (e.g., "PCI Baseline," "Corporate Security Standard," "SOX Network Controls"). Rules specify what must be present, what must be absent, and what values are acceptable. Standards are versioned — changing a rule creates a new version so historical audits remain valid.

### Collect Configs
Pull the running configuration from every device in scope. Scope can be defined by device group, site, platform, or ad-hoc list. Configs must be collected as close to simultaneously as practical to represent a consistent point-in-time snapshot. Store the raw configs for audit evidence.

### Evaluate
Compare each device's config against every applicable rule in the standard. Rules are matched by platform and context (a rule about BGP only applies to devices running BGP). Each rule produces a result: compliant, non-compliant, or not-applicable. Capture the specific config lines that pass or fail each rule.

### Grade
Score each device based on its evaluation results. A device with all rules passing is fully compliant. A device with critical violations is non-compliant. Devices in between receive a partial score. Aggregate scores by site, platform, region, or standard to produce executive-level summaries.

### Report
Generate audit-ready reports at multiple levels: executive summary (overall posture, trend over time), standard-level detail (which rules pass/fail across the fleet), device-level detail (specific violations with config excerpts). Reports must be exportable in formats auditors accept (PDF, CSV, structured data). Include timestamps, standard version, and device list for reproducibility.

### Remediate (optional)
For violations with known fixes, optionally push the corrective config to the device. Remediation follows the same pattern as any config change: backup first, apply fix, verify fix took effect by re-evaluating the specific rule. If remediation fails, flag the device and do not retry. Remediation can be automatic or gated behind approval.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Standards are versioned | Changing a rule creates a new version | Historical audit results must remain valid against the standard that was active at the time |
| Evaluation is per-rule, not pass/fail per device | Granular results for each rule | Auditors need to see exactly which controls pass and which fail |
| Remediation is optional and off by default | Must be explicitly enabled per standard or per run | Compliance scanning should be safe to run anytime without changing anything |
| Point-in-time snapshot | Configs collected at audit start, not live during evaluation | Ensures consistent comparison — no drift mid-scan |
| Reports include raw evidence | Config excerpts and rule match details | Auditors must be able to verify findings independently |

---

## 5. Scope

**In scope:** Compliance standard definition (rules, grouping, versioning). Config collection from devices. Rule evaluation against configs. Device and fleet grading. Audit-ready report generation. Optional auto-remediation of violations. Scheduled and on-demand scans. Trend tracking over time.

**Out of scope:** Defining what the compliance rules should be (input from security/compliance team). Firmware or OS-level compliance (this covers configuration only). Physical security audits. User access reviews. Policy exceptions and waiver management.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Rules are too broad and generate false positives | Alert fatigue, audit noise | Scope rules by platform and context; allow not-applicable results |
| Config collection fails on some devices | Incomplete audit | Report which devices were unreachable; do not mark them as compliant |
| Standard changes mid-audit | Inconsistent results | Lock standard version at scan start; evaluate against that version |
| Auto-remediation introduces a config error | Service impact | Backup before fix, verify after, disable auto-remediate by default |
| Large fleet makes scanning slow | Audit window exceeded | Parallelize config collection; evaluate locally after collection |

---

## 7. Requirements

### What the automation must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Pull running config from network devices | Yes | Cannot proceed |
| Evaluate config text against pattern-based rules | Yes | Cannot proceed |
| Score and aggregate results across devices | Yes | Cannot proceed |
| Generate formatted reports (PDF, CSV) | Yes | Cannot proceed |
| Apply config changes to devices (for remediation) | No | Remediation is manual |
| Schedule recurring scans | No | Engineer triggers manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| CMDB / inventory (e.g., ServiceNow, NetBox) | Device list, platform info, site grouping | No | Engineer provides device list manually |
| Compliance / GRC platform | Store standards, track posture over time | No | Standards defined locally, reports exported |
| ITSM / ticketing (e.g., ServiceNow, Jira) | Track remediation tasks for violations | No | Engineer tracks manually |
| Report storage (e.g., SharePoint, S3) | Archive audit reports for retention | No | Reports stored locally |

### Discovery Questions

Ask the engineer before designing the solution:

1. What compliance standards do you need to audit against? (PCI, SOX, HIPAA, internal policy, CIS benchmarks?)
2. Do you have the rules documented today, or do they need to be defined from scratch?
3. What device platforms are in scope? (IOS, NX-OS, EOS, JunOS, PAN-OS, etc.)
4. How many devices are in the audit scope?
5. Should the scan run on a schedule or on-demand?
6. Do you want auto-remediation for any violation categories, or scan-only?
7. If auto-remediation, does it need an approval gate?
8. What report format does your audit team require? (PDF, CSV, both?)
9. Do you need to track compliance posture over time (trend reporting)?
10. Is there an existing GRC platform where results should be sent?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Full sweep | Scan all devices in scope in one run | Quarterly or annual audit, on-demand assessment |
| Rolling | Scan a subset of devices each day, cover full fleet over N days | Continuous compliance posture for large fleets |
| Targeted | Scan a specific device group, site, or platform | Post-change verification, incident response |

---

## 9. Acceptance Criteria

1. Compliance standards are defined with versioned, platform-aware rules
2. Running configs are collected from all in-scope devices (unreachable devices are flagged, not skipped silently)
3. Every device is evaluated against every applicable rule with a clear pass/fail/not-applicable result
4. Devices are graded and scores are aggregated by site, platform, and standard
5. Audit-ready report is generated with executive summary and device-level detail
6. Reports include timestamps, standard version, device list, and config evidence
7. Optional remediation applies fixes only with backup and post-fix verification
8. Scan can run on-demand or on a recurring schedule without manual intervention

````

============================================================
FILE: spec-files/spec-network-health-check.md
DIRECTORY: spec-files/
FILENAME: spec-network-health-check.md
============================================================
SHA256: 8703004d9ab631187a1ac83d35ae702696008002df71a7de78d94ca79c44d4ed

````markdown
# Use Case: Network Health Check / Pre-Change Validation

## 1. Problem Statement

Network health checks are performed inconsistently. One engineer checks BGP neighbors, another checks interfaces, a third checks nothing. When used as pre/post validation for change windows, the checks are ad hoc, results aren't recorded, and there's no objective comparison between "before" and "after." If a change breaks something subtle — a single BGP peer drops, error counters spike — it goes unnoticed until users complain.

**Goal:** Define a standardized, repeatable health check that collects device metrics (CPU, memory, interfaces, routing neighbors, error counters, reachability), compares them against baselines or thresholds, and produces a clear pass/fail report. This check should work standalone and as a reusable building block for any change workflow.

---

## 2. High-Level Flow

```
Collect         →  Normalize     →  Evaluate      →  Report
    │                  │                │                │
    │                  │                │                │
 Run check          Parse raw        Compare          Build
 commands on        output into      against          pass/fail
 each device,       structured       thresholds       summary per
 gather CPU,        key-value        or baseline      device,
 memory,            metrics          snapshot,        flag failures,
 interfaces,                         flag any         attach to
 neighbors,                          deviation        ticket or
 counters,                                            parent job
 reachability                             │
                                     FAIL? → Stop parent workflow
```

---

## 3. Phases

### Collect
Run a defined set of check commands against each device in scope. The check catalog is standardized per device OS: CPU utilization, memory utilization, interface admin/oper status, routing neighbor count and state, interface error/discard counters, and reachability to critical next-hops. If a device is unreachable, **mark it as failed immediately — do not skip it silently**.

### Normalize
Parse raw command output into structured metrics. Each metric becomes a named key-value pair (e.g., "cpu_percent: 42", "bgp_neighbors_established: 12"). Normalization must handle vendor-specific output differences so that the evaluation phase works against a common schema regardless of device OS.

### Evaluate
Compare each metric against its threshold or baseline. Two modes:

- **Threshold mode:** Compare against static limits (e.g., CPU < 80%, memory < 85%, zero critical interface errors). Used for standalone health checks.
- **Baseline mode:** Compare against a previously captured snapshot (e.g., same BGP neighbor count, same interfaces up). Used for pre/post change validation.

If any critical metric fails, the overall device result is **FAIL**. If only warning-level metrics deviate, the result is **WARN**.

### Report
Produce a structured report: one row per device, one column per metric, color-coded pass/warn/fail. Include raw values, thresholds or baseline values, and the delta. Attach to the change ticket if one exists, or return to the calling workflow.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Check catalog is per-OS, not per-device | Standardize by OS family | Maintainable, consistent checks across fleet |
| Two evaluation modes (threshold vs baseline) | Support both standalone and pre/post use | One check definition, two contexts |
| Critical failure = hard stop | FAIL blocks the parent workflow | Never proceed with a change on an unhealthy device |
| Warning = proceed with flag | WARN does not block, but is recorded | Avoids false-positive gate on minor deviations |
| Report is always generated | Even if all devices pass | Evidence trail for audit and troubleshooting |

---

## 5. Scope

**In scope:** Standardized check catalog per OS family, CLI-based metric collection, structured parsing, threshold evaluation, baseline snapshot capture and comparison, per-device pass/warn/fail grading, summary report generation, integration as a reusable pre/post check for other workflows.

**Out of scope:** Streaming telemetry or SNMP-based collection (different data path). Remediation of failed checks (that's the parent workflow's job). Monitoring system integration beyond report generation. Custom per-device check overrides (use device groups instead).

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Device unreachable during check | No data collected, false pass if skipped | Treat unreachable as FAIL, never skip |
| Parsing fails on unexpected output format | Metric missing, incorrect evaluation | Treat parse failure as FAIL for that metric |
| Thresholds too strict | Excessive false failures blocking changes | Separate critical vs warning thresholds, tune over time |
| Baseline snapshot is stale | Comparison against outdated state | Capture baseline immediately before the change, not days ahead |
| Check commands impact device performance | CPU spike on already stressed device | Use non-intensive show commands, avoid debug or trace |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on devices | Yes | Cannot proceed |
| Parse unstructured command output into structured data | Yes | Cannot proceed |
| Compare values against thresholds or baseline snapshots | Yes | Cannot proceed |
| Store and retrieve baseline snapshots | Yes (for baseline mode) | Threshold mode only |
| Generate reports from structured data | Yes | Cannot proceed |
| Expose results to a parent workflow | Yes (for pre/post use) | Standalone only |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing (e.g., ServiceNow) | Attach report to change ticket | No | Report saved locally or returned to caller |
| CMDB / inventory (e.g., ServiceNow, NetBox) | Resolve device list and OS type | No | Device list provided as input |
| Monitoring (e.g., Datadog, PRTG) | Cross-reference alerts during check | No | Check runs independently |

### Discovery Questions

Ask the engineer before designing the solution:

1. What devices are in scope? Provide a list, a device group, or a CMDB query.
2. What OS families are represented? (IOS, IOS-XE, NX-OS, EOS, Junos, etc.)
3. Is this a standalone health check or a pre/post check for a change workflow?
4. If pre/post: what change is this validating? (upgrade, config push, migration?)
5. What are the critical thresholds? (CPU %, memory %, acceptable error counter delta?)
6. Which routing protocols matter? (BGP, OSPF, ISIS, static?)
7. Are there interfaces expected to be down? (so they don't flag as failures)
8. Do you want to store the baseline for future comparison or discard after use?
9. Should results be attached to a change ticket? Which ticketing system?
10. Are there existing check templates or command sets you already use?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One device at a time, stop on first failure | Pre-change validation where any failure aborts the change |
| Parallel | All devices at once, collect all results | Standalone fleet health check, need full picture |
| Rolling | N devices at a time, aggregate pass/fail | Large-scale pre-check where partial results are useful |

---

## 9. Acceptance Criteria

1. All defined check commands execute successfully on reachable devices
2. Unreachable devices are marked FAIL, never silently skipped
3. Raw output is parsed into structured metrics for every check
4. Threshold mode correctly flags metrics outside defined limits
5. Baseline mode correctly detects deviations from the captured snapshot
6. Each device receives an overall PASS, WARN, or FAIL grade
7. A summary report is generated for every run, regardless of outcome
8. When used as a pre-check, a FAIL result prevents the parent workflow from proceeding
9. When used as a post-check, a FAIL result triggers rollback or escalation in the parent workflow

````

============================================================
FILE: spec-files/spec-port-turn-up.md
DIRECTORY: spec-files/
FILENAME: spec-port-turn-up.md
============================================================
SHA256: 551a28d4d8b2e7cbc40cbd7a3e93be9c08fb656f2c4a37d4decefd21ccc0daed

````markdown
# Use Case: Port Turn-Up

## 1. Problem Statement

Port turn-up — provisioning a switch port for a new server, workstation, or appliance — is the most frequent hands-on network change in enterprise environments. Engineers receive a request (ticket, email, spreadsheet row), walk to the closet or log into the switch, configure the port, then manually update three or four systems: the ticket, the IPAM, the cable database, the monitoring tool. The configuration itself takes two minutes; the paperwork takes twenty. Mistakes happen when the port is configured correctly but the records don't match, or when the wrong port is configured because the patch panel label was misread.

**Goal:** Automate the full port turn-up lifecycle — validate the request, configure the port, verify the result, and update all surrounding systems — so the engineer submits a request and gets a working, documented port back.

---

## 2. High-Level Flow

```
Request  →  Validate  →  Pre-Check  →  Configure  →  Post-Check  →  Update Systems  →  Close Out
   │            │            │             │              │                │                 │
   │            │            │             │              │                │                 │
 Port,       Confirm      Device is     Apply L2/L3    Confirm port    Update IPAM,      Evidence
 VLAN,       port exists,  reachable,   config via     is in correct   DCIM/cable DB,    report,
 IP (if L3), VLAN valid,   capture      template,      VLAN, link up,  monitoring,       close
 device,     IP available  baseline     save config    IP responds     ticketing          ticket
 speed/duplex (if L3)                                  (if L3)
                                                           │
                                                      FAIL? → Rollback
```

---

## 3. Phases

### Request Intake
Accept the port turn-up request: target device, port name, VLAN assignment, port mode (access or trunk), speed/duplex (or auto), description. If Layer 3, include IP address and subnet. The request can come from a ticket, a form, or a CSV for bulk turn-ups. Determine if this is a new turn-up, a modification, or a decommission (port shutdown + VLAN removal).

### Validate Input
Confirm the target device exists in inventory. Confirm the port exists on the device. For access mode: confirm the VLAN exists on the device (or will be created as part of the request). For L3: confirm the IP address is available in IPAM — not assigned, not responding to ping. Reject invalid requests before touching any device.

### Pre-Check
Connect to the device. Verify reachability. Capture the current port state (admin status, operational status, VLAN assignment, speed/duplex, description, error counters). This snapshot is the rollback baseline. If the port is already in use (link up, non-default VLAN, active MAC addresses), **warn the engineer — this port may be serving another connection**.

### Configure Port
Apply the port configuration via rendered template. For access: set VLAN, description, speed/duplex, enable port. For trunk: set native VLAN, allowed VLAN list (additive), description, enable port. For L3: set IP address, subnet, description, enable port. Save the running config after changes.

### Post-Check
Verify the port configuration matches the request: correct VLAN, correct mode, correct description, link status. For L3: verify IP is reachable (ping from the device or from a test source). Check for interface errors that appeared after turn-up. If post-check fails, **rollback**.

### Rollback (conditional)
Restore the pre-check port configuration. Re-verify the port returns to its baseline state. If rollback fails, **escalate to the engineer**.

### Update External Systems
After successful post-check, update all connected systems:
- **ITSM**: update the change ticket with results and evidence
- **IPAM**: mark the IP as assigned (L3) or update the VLAN-to-port mapping
- **DCIM / cable database**: update the port record with the new connection details
- **Monitoring**: add the port to monitoring or update thresholds

Each external system update is independent — one failure does not roll back the network change or block other updates. Failed updates create follow-up tickets.

### Close Out
Generate an evidence report: request details, pre/post port state, configuration applied, external system updates, pass/fail. Close the change ticket.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Validate before touching the device | Reject bad requests early | Prevents partial deployments from invalid data |
| Warn on in-use ports, don't block | Engineer decides whether to proceed | Automation can't know if the existing connection is decommissioned but not cleaned up |
| External system updates are non-blocking | One IPAM failure doesn't roll back the port | The port config is the primary objective; record-keeping failures create follow-up tickets |
| Config rendered from template, not raw CLI | Template per device OS/role | Consistent config across the fleet, testable before deployment |
| IP availability checked via IPAM + ping | Belt and suspenders | IPAM may be stale; ping catches IPs in use but not in IPAM |
| Port decommission is the same workflow in reverse | Shutdown port, remove VLAN, release IP | One workflow handles turn-up and tear-down |

---

## 5. Scope

**In scope:** L2 access port turn-up. L2 trunk port turn-up. L3 routed port turn-up. Port modification (change VLAN, change mode). Port decommission (shutdown + cleanup). Multi-vendor (IOS, NX-OS, EOS, Junos). ITSM integration. IPAM integration. DCIM/cable DB integration. Monitoring integration. Bulk turn-up via CSV. Evidence generation.

**Out of scope:** VLAN creation (separate use case — see `spec-vlan-provisioning.md`). Physical cabling and patch panel work. PoE configuration. Port-channel / LAG provisioning (separate use case). 802.1X / NAC policy assignment. QoS policy assignment.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Wrong port configured | Disrupts existing service | Pre-check warns if port is in use (link up, active MACs) |
| VLAN doesn't exist on the device | Port goes to VLAN but no traffic flows | Validate VLAN exists during input validation |
| IP conflict (L3) | Duplicate IP, both hosts intermittent | Check IPAM + ping before assigning |
| External system update fails | Records out of sync | Non-blocking updates, follow-up tickets for failures |
| Port shows link-down after config | Physical layer issue (cable, SFP) | Post-check reports link status; not a config problem, escalate |
| Bulk turn-up cascading failure | Many ports misconfigured | Per-port success/failure tracking, abort batch on threshold |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on multi-vendor switches | Yes | Cannot proceed |
| Retrieve port status and VLAN assignments | Yes | Cannot proceed |
| Push configuration to devices via template | Yes | Cannot proceed |
| Orchestrate multi-step workflows with conditions | Yes | Cannot proceed |
| Generate reports from templates | No | Engineer documents manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing | Source of request, audit trail, change tracking | No | Request comes via direct input, engineer tracks manually |
| IPAM | Validate IP availability, record assignments, track VLAN-to-port mappings | No | Engineer validates IP manually, records in spreadsheet |
| DCIM / cable management | Update port-to-device mapping, track physical connections | No | Engineer updates cable DB manually |
| Monitoring | Add port to monitoring, set thresholds, alert on errors | No | Engineer adds to monitoring manually |

### Discovery Questions

Ask the engineer before designing the solution:

1. What switch vendors and OS types are in scope? (IOS, NX-OS, EOS, Junos?)
2. What port modes do you need? (access only, trunk, L3 routed, all three?)
3. Do you have an IPAM system? Which one? Should the workflow check IP availability there?
4. Do you have a DCIM or cable management system? Should the workflow update it?
5. Do you use a ticketing system? Should the workflow create/update tickets?
6. Should the workflow add ports to monitoring after turn-up?
7. What does your port naming/description convention look like?
8. Should in-use ports block the turn-up, or just warn?
9. Do you need port decommission (reverse turn-up) in the same workflow?
10. Single port or bulk? If bulk, where does the list come from? (CSV, ticket, API?)

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One port at a time, stop on first failure | Small batch, high-risk environment |
| Parallel (per-port) | All ports at once, track per-port results | Standard — ports are independent |
| Grouped by device | All ports on one switch first, then next switch | Reduces device connections, faster for multi-port-per-switch changes |

Each port is independent — one failure does not affect other ports, even on the same device.

---

## 9. Acceptance Criteria

1. Port is in the correct VLAN and mode after turn-up
2. Port description matches the request
3. Port link status is reported (up/down — automation can't fix physical layer)
4. L3 port responds to ping after turn-up (when applicable)
5. Pre-check captures baseline state for rollback
6. Post-check confirms requested state matches actual state
7. Rollback restores baseline on any port where post-check fails
8. ITSM ticket is updated with results (when ITSM is available)
9. IPAM is updated with IP/VLAN assignment (when IPAM is available)
10. External system update failures create follow-up tickets, not rollbacks
11. Evidence report documents request, changes, verification, and external system updates
12. Bulk mode tracks per-port success/failure independently

````

============================================================
FILE: spec-files/spec-software-upgrade.md
DIRECTORY: spec-files/
FILENAME: spec-software-upgrade.md
============================================================
SHA256: 00370ddcb15a2dedabe9f6d4e6e4c6f30f20fdc17a9ddb5d90c105a4bd1758c9

````markdown
# Use Case: Network Device Software Upgrade

## 1. Problem Statement

Network device software upgrades are high-risk, time-consuming change windows performed manually. Engineers SSH into devices, run commands, wait for reboots, and hope nothing breaks. If something goes wrong, rollback is manual and stressful. There's no consistent evidence trail.

**Goal:** Automate the full upgrade lifecycle — validate before, upgrade, validate after, rollback if needed, and produce auditable evidence — reducing the change window and eliminating manual errors.

---

## 2. High-Level Flow

```
Pre-Flight  →  Stage Image  →  Upgrade  →  Post-Flight  →  Close Out
    │               │             │              │              │
    │               │             │              │              │
 Validate        Transfer      Activate       Validate      Evidence
 device is       image to      new image,     device is     report,
 healthy,        device,       reload,        healthy,      update
 backup          verify        wait for       version       ticket,
 config          integrity     reboot         correct,      restore
                                              neighbors     monitoring
                                              back
                                                 │
                                            FAIL? → Rollback
```

---

## 3. Phases

### Pre-Flight
Confirm the device is ready. Check health (CPU, memory, interfaces, routing neighbors), verify disk space for the new image, backup the running config. If any critical check fails, **stop — do not proceed**.

### Stage Image
Transfer the software image to the device. Verify the file arrived intact (checksum). If transfer fails, retry once, then abort.

### Upgrade
Set the boot variable to the new image, save config, reload the device. Wait for it to come back online (configurable timeout, default 10 min). If the device doesn't come back, **alert the engineer — this requires console access**.

### Post-Flight
Verify the device is running the target version. Re-run the same health checks from pre-flight and compare: are all interfaces still up? Are all routing neighbors re-established? Is the config intact? If post-flight fails and rollback is enabled, **auto-rollback**.

### Rollback (conditional)
Restore the boot variable to the previous image, reload. Verify the device comes back on the old version. If rollback itself fails, **escalate immediately**.

### Close Out
Generate an evidence report (pre vs post state, config diff, timing). Update the change ticket. Restore monitoring alerts.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Pre-flight is a hard gate | Abort if critical checks fail | Never upgrade an unhealthy device |
| Config backup is mandatory | No backup = no upgrade | Must have a restore point |
| Post-flight compares against pre-flight | Same checks, compare counts | Detects regressions objectively |
| Rollback is automatic by default | Can be overridden to manual review | Speed matters when a device is down |
| Evidence is generated regardless of outcome | Success or failure both produce a report | Audit trail is non-negotiable |

---

## 5. Scope

**In scope:** Single device upgrade, batch upgrade (sequential/rolling/parallel), pre/post validation, config backup/diff, rollback, evidence generation, ITSM integration.

**Out of scope:** Image selection and approval (input to this workflow). Physical console recovery. HA/stack-specific upgrade choreography (separate use case). Image repository management.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Device doesn't come back after reload | Service outage | Configurable reboot timeout + immediate alerting |
| Post-upgrade routing neighbors don't re-establish | Traffic loss | Wait with timeout, compare against pre-flight baseline |
| Wrong image staged | Bricked device | Checksum verification before activating |
| Rollback fails | Extended outage | Alert engineer, do not retry indefinitely |
| Batch upgrade cascading failure | Wide-scale outage | Abort batch if failure rate exceeds threshold |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on devices | Yes | Cannot proceed |
| Backup and diff device configurations | Yes | Cannot proceed |
| Transfer files to devices | Yes | Engineer pre-stages image manually |
| Orchestrate multi-step workflows with conditions | Yes | Cannot proceed |
| Test device reachability after reboot | Yes | Cannot proceed |
| Generate reports from templates | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing | Track the change, audit trail | No | Engineer tracks manually |
| Monitoring | Suppress alerts during upgrade, restore after | No | Engineer handles manually or add a pause |
| Image repository | Source for software images | Yes | Engineer pre-stages the image |

### Discovery Questions

Ask the engineer before designing the solution:

1. Which devices are you upgrading? What OS do they run?
2. What is the target version and image filename?
3. Where is the image stored? (URL, file server, already on device?)
4. What routing protocols do these devices run? (BGP, OSPF, static?)
5. Do you use a ticketing system? Which one?
6. Do you want to suppress monitoring alerts during the upgrade?
7. Should the workflow auto-rollback on failure, or pause for review?
8. Single device or batch? If batch, sequential or rolling?
9. Is there an approval step, or should it auto-proceed after pre-flight?
10. Are there existing automations you'd like to reuse? (backup workflows, check templates, etc.)

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One device at a time, stop on first failure | Small batch, conservative |
| Rolling | N devices at a time, stop if failure rate > threshold | Medium batch, production |
| Parallel | All at once | Lab/non-prod only |

---

## 9. Acceptance Criteria

1. Upgrade only proceeds if all critical pre-flight checks pass
2. Device runs the target version after upgrade
3. All interfaces and routing neighbors match pre-flight state
4. Config backup exists before and after the upgrade
5. Config diff shows only expected changes
6. Rollback restores the previous version when post-flight fails
7. Evidence report is generated for every run (success or failure)
8. Batch mode respects the configured concurrency and failure threshold

````

============================================================
FILE: spec-files/spec-ssl-certificate-lifecycle.md
DIRECTORY: spec-files/
FILENAME: spec-ssl-certificate-lifecycle.md
============================================================
SHA256: a668e2f92d68a45848f708c134e66b9f9a968afcb2058e0ab70e93c7f55d9eec

````markdown
# Use Case: SSL/TLS Certificate Lifecycle Management

## 1. Problem Statement

SSL/TLS certificate management is reactive and error-prone. Teams lose track of expiration dates, scramble to renew at the last minute, and manually deploy certificates across dozens of endpoints — load balancers, web servers, reverse proxies, WAFs. Expired certificates cause outages, browser warnings, and broken API integrations. There's no single source of truth for what's deployed where.

**Goal:** Automate the full certificate lifecycle — request, obtain from CA, deploy to all endpoints, verify deployment, monitor expiry, and auto-renew before expiration — eliminating certificate-related outages and manual toil.

---

## 2. High-Level Flow

```
Request  →  Obtain Cert  →  Deploy  →  Verify  →  Monitor  →  Renew
   │             │             │           │           │          │
   │             │             │           │           │          │
 Validate     Generate      Push cert   Confirm    Track      Auto-renew
 domain,      CSR, submit   to load     TLS        expiry     before
 SAN list,    to CA,        balancers,  handshake  dates,     deadline,
 key type,    retrieve      web         returns    alert on   loop back
 approval     signed cert   servers,    correct    threshold  to Obtain
              + chain       proxies,    cert +
                            WAFs        full chain
                                           │
                                      FAIL? → Rollback to previous cert
```

---

## 3. Phases

### Request & Validation
Collect the certificate request details: domain name(s), Subject Alternative Names (SANs), key type (RSA/ECDSA), key size, and intended endpoints. Validate that the requestor is authorized for those domains. If an approval gate is configured, **wait for approval before proceeding**.

### Obtain Certificate
Generate a private key and Certificate Signing Request (CSR). Submit the CSR to the appropriate Certificate Authority — internal CA for internal services, public CA for external-facing services. Retrieve the signed certificate and full chain. Store the certificate, key, and chain in the designated secrets store or vault. If CA issuance fails, **alert the requestor and stop**.

### Deploy
Push the certificate, key, and chain to every target endpoint — load balancers, web servers, reverse proxies, WAFs. Each endpoint type has its own deployment method. Deploy sequentially or in rolling fashion for redundant endpoints. If deployment to a critical endpoint fails, **rollback that endpoint to the previous certificate**.

### Verify
For each endpoint, perform a TLS handshake and confirm: the correct certificate is served, the chain is complete, the expiration date matches, and no mixed-content or protocol errors exist. If verification fails, **retry deployment once, then escalate**.

### Monitor & Renew
Record the certificate's expiration date. When it approaches a configurable threshold (default 30 days before expiry), trigger an automatic renewal. Renewal loops back to the Obtain phase with the same parameters. If auto-renewal fails, **alert the team with enough lead time to intervene manually**.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Private keys never leave the secrets store | Keys retrieved at deploy time only | Minimizes exposure of key material |
| Verification is a hard gate after deploy | Rollback if TLS handshake fails | Never leave a broken cert in production |
| Renewal triggers at configurable threshold | Default 30 days, adjustable per cert | Enough lead time for manual intervention if auto-renew fails |
| Deploy is per-endpoint, not all-or-nothing | Rolling deployment with per-endpoint rollback | One bad endpoint shouldn't block the rest |
| Both internal and public CA supported | CA selection based on cert purpose | Internal services don't need public trust; external ones do |

---

## 5. Scope

**In scope:** Certificate request intake, CSR generation, CA submission (internal and public), deployment to load balancers/web servers/proxies/WAFs, TLS verification, expiry monitoring, auto-renewal, rollback on failed deployment, secrets store integration, audit trail.

**Out of scope:** CA infrastructure setup and management. DNS validation for public CAs (assumed handled externally or as a separate workflow). Client certificate / mTLS provisioning (separate use case). Code signing certificates. Certificate pinning policy management.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| CA issuance delayed or rejected | Service runs on expiring cert | Trigger renewal early enough to allow manual fallback |
| Deployment fails on a subset of endpoints | Inconsistent certs across infrastructure | Per-endpoint rollback + alerting; retry before escalating |
| Private key compromised during transit | Security breach | Keys stored in vault, retrieved only at deploy time, never logged |
| Auto-renewal loop fails silently | Certificate expires unnoticed | Monitoring alerts at multiple thresholds (30, 14, 7, 1 day) |
| Wildcard cert deployed too broadly | Larger blast radius if compromised | Track all endpoints per cert; flag overly broad wildcard usage |

---

## 7. Requirements

### What the automation must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Generate private keys and CSRs | Yes | Cannot proceed |
| Submit CSR to internal and public CAs | Yes | Cannot proceed |
| Deploy certificates to network/server endpoints | Yes | Cannot proceed |
| Perform TLS handshake verification | Yes | Engineer verifies manually |
| Store and retrieve secrets (keys, certs) | Yes | Cannot proceed securely |
| Schedule and trigger renewal based on expiry | Yes | Engineer monitors manually |
| Roll back to a previous certificate on failure | Yes | Engineer rolls back manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| Certificate Authority (internal) | Issue certs for internal services | Conditional | Only if internal certs needed |
| Certificate Authority (public) | Issue certs for external services | Conditional | Only if public certs needed |
| Secrets / vault | Store private keys and certificates | Yes | Cannot proceed securely |
| ITSM / ticketing | Track requests, approvals, audit trail | No | Engineer tracks manually |
| CMDB / inventory | Identify endpoints for a given domain | No | Engineer provides endpoint list |

### Discovery Questions

Ask the engineer before designing the solution:

1. Which domains and SANs need certificates?
2. Are these internal-only or public-facing services?
3. What CA do you use? Internal CA, Let's Encrypt, DigiCert, or other?
4. Where are private keys stored today? Do you have a secrets vault?
5. What endpoint types need certs? (Load balancers, web servers, proxies, WAFs?)
6. How many endpoints per certificate?
7. What is your desired renewal lead time before expiry?
8. Is there an approval process for new certificate requests?
9. Do you need to support both RSA and ECDSA key types?
10. Are there existing certificates to import and start monitoring?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Per-certificate | One certificate lifecycle at a time | Default for new requests |
| Rolling endpoints | Deploy to N endpoints at a time per cert | Production deployments behind redundant endpoints |
| Bulk renewal | Renew all expiring certs in a scheduled window | Monthly renewal sweep |

---

## 9. Acceptance Criteria

1. Certificate is only obtained after request validation and approval (if configured)
2. Private keys are generated and stored in the secrets vault, never exposed in logs
3. Certificate, key, and full chain are deployed to all specified endpoints
4. TLS handshake verification confirms the correct cert is served on every endpoint
5. Failed deployment triggers rollback to the previous certificate on that endpoint
6. Expiry monitoring alerts at configurable thresholds before expiration
7. Auto-renewal obtains and deploys a new certificate before the old one expires
8. Audit trail records every action: request, issuance, deployment, verification, renewal

````

============================================================
FILE: spec-files/spec-vlan-provisioning.md
DIRECTORY: spec-files/
FILENAME: spec-vlan-provisioning.md
============================================================
SHA256: b0f2b76b6963e0331d5c7a2a1bf659145d7e2a4660181660c67b770f7f08182f

````markdown
# Use Case: VLAN Provisioning

## 1. Problem Statement

VLAN changes are the most common network change in enterprise environments. Engineers create tickets, log into switches one by one, type commands, and hope they got the trunk list right. A single VLAN provisioning request can touch dozens of switches across campus and data center fabrics. The work is repetitive, error-prone, and slow. Mistakes cause outages — a wrong trunk config drops an entire floor.

**Goal:** Automate the creation, modification, and deletion of VLANs across multi-vendor switches, including trunk and access port assignment, with pre/post validation to confirm the VLAN is active and reachable end-to-end.

---

## 2. High-Level Flow

```
Request  →  Validate Input  →  Pre-Check  →  Deploy Config  →  Post-Check  →  Close Out
   │              │                │               │                │              │
   │              │                │               │                │              │
 VLAN ID,      Check VLAN ID    Verify target   Push VLAN        Confirm VLAN   Update ticket,
 name,         not conflicting,  switches are    config to        exists on all  generate
 switches,     ports exist,      reachable,      each device:     targets,       evidence
 port          adapters are      capture         create VLAN,     trunks carry   report
 assignments   healthy           current state   assign ports     it, ports are
                                                                  in correct VLAN
                                                                      │
                                                                 FAIL? → Rollback
```

---

## 3. Phases

### Request Intake
Accept the VLAN provisioning request: VLAN ID, VLAN name, target switches, port assignments (access ports and trunk ports). The request can come from a ticket, a form, or direct input. Determine the operation type — create, modify, or delete.

### Validate Input
Check that the VLAN ID is valid (1-4094, not reserved). For create: confirm the VLAN does not already exist on the target switches. For modify/delete: confirm it does exist. Verify that the specified ports exist on the target switches. If any input is invalid, **reject the request with a clear reason before touching any device**.

### Pre-Check
Connect to each target switch. Confirm reachability. Capture the current VLAN table and port assignments as a baseline. This snapshot is the rollback reference. If a switch is unreachable, **stop for that switch** — do not partially provision a VLAN across half the fabric.

### Deploy Configuration
Push the VLAN configuration to each target switch. For create: add the VLAN, assign it to access ports, add it to trunk allowed lists. For modify: update the VLAN name or port assignments. For delete: remove port assignments first, then remove the VLAN. Save the running config after changes.

### Post-Check
Verify the VLAN exists in the VLAN table on every target switch. Verify access ports are assigned to the correct VLAN. Verify trunk ports carry the new VLAN. Optionally, run an end-to-end reachability test (ping across the VLAN). If post-check fails, **rollback the changes on the failed device**.

### Rollback (conditional)
Restore the pre-check configuration snapshot on any device where post-check failed. Re-verify that the rollback succeeded. If rollback itself fails, **escalate to an engineer**.

### Close Out
Generate an evidence report: what was requested, what was configured, pre vs post state, any failures. Update the change ticket. Notify the requestor.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Input validation before any device contact | Reject bad requests early | Prevents partial deployments from invalid data |
| Per-device rollback, not all-or-nothing | Only roll back the device that failed | A working VLAN on 9 of 10 switches is better than rolling back all 10 |
| Trunk and access port assignment in same workflow | Single request, single execution | Engineers think of VLAN provisioning as one task, not three |
| Delete removes port assignments before VLAN | Ports first, VLAN second | Deleting a VLAN with active ports causes traffic drops |
| Config save after each device | Persist changes immediately | Prevents config loss on reboot |

---

## 5. Scope

**In scope:** VLAN create, modify, delete. Access port assignment. Trunk allowed-list update. Multi-switch deployment. Pre/post validation. Rollback on failure. Evidence report. ITSM integration.

**Out of scope:** SVI / Layer 3 interface creation (separate use case). Spanning tree tuning. VTP/GVRP propagation (relies on device-native protocol, not automation). QoS policy assignment to VLANs. VLAN design or IP address planning.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| VLAN ID conflict with existing VLAN | Overwrite or error | Validate VLAN does not exist before creating |
| Trunk allowed-list overwritten instead of appended | Other VLANs dropped from trunk | Use additive commands, not replace — verify syntax per vendor |
| Partial deployment across fabric | VLAN works on some switches, not others | Track per-device success, report partial state clearly |
| Port assigned to wrong VLAN | User traffic on wrong segment | Post-check verifies port VLAN assignment matches request |
| Switch unreachable mid-deployment | Inconsistent state | Pre-check reachability, abort that device if it drops |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on multi-vendor switches | Yes | Cannot proceed |
| Retrieve VLAN table and port assignments | Yes | Cannot proceed |
| Push configuration changes to devices | Yes | Cannot proceed |
| Orchestrate multi-step workflows with per-device tracking | Yes | Cannot proceed |
| Compare pre and post device state | Yes | Manual verification |
| Generate reports from collected data | No | Engineer documents manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| ITSM / ticketing | Source of change request, audit trail | No | Request comes via direct input |
| IPAM | Validate VLAN ID availability, reserve subnets | No | Engineer confirms VLAN ID is free manually |
| CMDB | Record VLAN-to-switch mapping | No | Mapping tracked manually or in spreadsheet |

### Discovery Questions

Ask the engineer before designing the solution:

1. What switch vendors and OS types are in scope? (IOS, NX-OS, EOS, Junos, etc.)
2. How do you manage trunk allowed lists today — additive or full replace?
3. Do you use VTP, GVRP, or manage VLANs statically per switch?
4. Is there an IPAM system that tracks VLAN assignments?
5. Do VLAN changes require a change ticket, or can they be self-service?
6. Should the workflow handle Layer 3 SVI creation, or is that a separate request?
7. What does your VLAN naming convention look like?
8. How many switches does a typical VLAN change touch?
9. Are there switches that should never be modified automatically? (e.g., core, spine)
10. Do you need end-to-end reachability testing after provisioning, or is VLAN table verification enough?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One switch at a time, stop on first failure | Small change, high-risk environment |
| Parallel (per-device) | All switches at once, track per-device results | Standard provisioning — most common for VLANs |
| Fabric-aware | Deploy to distribution/aggregation first, then access | Hierarchical campus designs where order matters |

---

## 9. Acceptance Criteria

1. VLAN exists in the VLAN table on every target switch after create
2. VLAN is removed from every target switch after delete
3. Access ports are assigned to the correct VLAN
4. Trunk ports include the VLAN in their allowed list (additive, not replacing)
5. Pre-check captures baseline state for rollback
6. Post-check confirms the requested state matches the actual state
7. Rollback restores pre-check state on any device where deployment failed
8. Evidence report documents the request, changes, and verification results
9. Invalid requests are rejected before any device is contacted

````

============================================================
FILE: spec-files/spec-vpn-tunnel-provisioning.md
DIRECTORY: spec-files/
FILENAME: spec-vpn-tunnel-provisioning.md
============================================================
SHA256: 33295cbfb51e9336087c1bb0c91377a58e2d06e2f96a7a8ab5cb7be3304a36ec

````markdown
# Use Case: VPN Tunnel Provisioning (IPsec/GRE)

## 1. Problem Statement

Provisioning site-to-site VPN tunnels is a coordination-heavy, error-prone process. An engineer must configure both endpoints with matching crypto parameters, matching tunnel addresses, matching ACLs — and a single mismatch means the tunnel never comes up. Multiply that by hub-and-spoke or full-mesh topologies and you get hours of tedious, symmetric configuration work with no guarantee of first-time success.

**Goal:** Automate the end-to-end tunnel provisioning lifecycle — parameter generation, both-endpoint configuration, tunnel verification, and traffic validation — so that tunnels come up correctly on the first attempt every time.

---

## 2. High-Level Flow

```
Request     →  Design     →  Configure     →  Verify     →  Close Out
  │               │              │               │              │
  │               │              │               │              │
Validate        Generate      Apply           Tunnel UP?     Evidence
inputs,         crypto        config to       Ping across    report,
resolve         params,       Endpoint A      tunnel,        update
endpoints,      tunnel IPs,   and             check          ticket,
check           build         Endpoint B      routing,       update
reachability    configs       (both sides)    traffic        IPAM
                                              passes
                                                 │
                                            FAIL? → Rollback
```

---

## 3. Phases

### Request Validation
Validate the tunnel request: source site, destination site, tunnel type (IPsec, GRE, GRE-over-IPsec), topology (point-to-point, hub-and-spoke). Resolve device hostnames to management IPs. Confirm both endpoints are reachable and healthy. If either endpoint is unreachable or unhealthy, **stop — do not proceed**.

### Tunnel Design
Generate the matching parameter set for both sides: crypto algorithm, hash, DH group, SA lifetime, pre-shared key (or certificate reference), tunnel source/destination IPs, tunnel interface addresses. For GRE-over-IPsec, generate both the GRE and IPsec parameters. Allocate tunnel interface IPs from IPAM if available. Every parameter must be symmetric — what one side proposes, the other must accept.

### Configuration
Build device-specific configs for both endpoints. Apply configuration to Endpoint A, then Endpoint B. Config backup is taken on both devices before any changes are applied. If configuration fails on either endpoint, **rollback the changes already applied and stop**.

### Verification
Confirm the tunnel is operationally up: tunnel interface status is up/up, IKE SA is established (IPsec), GRE keepalives are passing (GRE). Ping across the tunnel from each side. If routing is involved (BGP/OSPF over tunnel), verify neighbor adjacency forms. If the tunnel does not come up within a configurable timeout (default 5 min), **trigger rollback**.

### Rollback (conditional)
Remove the tunnel configuration from both endpoints in reverse order (Endpoint B first, then Endpoint A). Restore original configs from backup. Verify the rollback did not impact existing services. If rollback fails, **escalate immediately**.

### Close Out
Generate an evidence report: tunnel parameters, config diffs (both sides), verification results, timing. Update the change ticket. Update IPAM with allocated tunnel IPs. Record the tunnel in inventory for lifecycle tracking.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Both endpoints configured in same workflow | Single orchestrated job | A half-configured tunnel is useless and confusing |
| Config backup is mandatory on both sides | No backup = no provisioning | Must have restore points for rollback |
| Crypto parameters are generated, not manually entered | Engineer selects a policy tier (e.g., "high", "standard") | Prevents mismatches and enforces security standards |
| Tunnel IPs allocated from IPAM when available | Falls back to manual input if no IPAM | Prevents IP conflicts across tunnels |
| Verification includes traffic test, not just state check | Ping across tunnel is required | Interface up does not guarantee end-to-end connectivity |

---

## 5. Scope

**In scope:** IPsec (IKEv1/IKEv2), GRE, GRE-over-IPsec tunnel provisioning. Point-to-point, hub-and-spoke, and full-mesh topologies. Pre-shared key and certificate-based authentication. Tunnel verification (state + traffic). Rollback. Evidence generation. ITSM and IPAM integration.

**Out of scope:** DMVPN/NHRP setup (separate use case). SD-WAN overlay provisioning. Firewall rule/ACL changes on intermediate devices. Certificate generation and PKI management. QoS policy over tunnels.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Crypto parameter mismatch | Tunnel never establishes | Generate both configs from a single parameter set — never configure independently |
| One endpoint configured, other fails | Dangling half-tunnel, possible routing issues | Rollback Endpoint A if Endpoint B config fails |
| Tunnel IP conflicts | Overlapping addresses across tunnels | Allocate from IPAM; if manual, validate uniqueness before applying |
| Existing services disrupted by tunnel config | Traffic loss on production device | Pre-flight health check, config backup, post-change service verification |
| Hub device overloaded in hub-and-spoke | Hub becomes bottleneck | Limit concurrent spoke provisioning; check hub resource utilization before adding tunnels |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on devices | Yes | Cannot proceed |
| Backup and diff device configurations | Yes | Cannot proceed |
| Apply configuration to multiple devices in sequence | Yes | Cannot proceed |
| Orchestrate multi-step workflows with conditions | Yes | Cannot proceed |
| Test device reachability (ping from device) | Yes | Manual verification by engineer |
| Generate reports from templates | Yes | Cannot proceed |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| IPAM (Infoblox, NetBox, etc.) | Allocate tunnel interface IPs | No | Engineer provides IPs manually |
| ITSM / ticketing (ServiceNow, etc.) | Track the change, audit trail | No | Engineer tracks manually |
| Configuration repository / source of truth | Store tunnel parameters for lifecycle tracking | No | Evidence report serves as record |
| Certificate authority / PKI | Provide certificates for IKEv2 cert-based auth | No | Use pre-shared key instead |

### Discovery Questions

Ask the engineer before designing the solution:

1. What type of tunnel? IPsec only, GRE only, or GRE-over-IPsec?
2. What is the topology? Point-to-point, hub-and-spoke, or full mesh?
3. What are the endpoint devices and what OS do they run?
4. What are the public (or WAN) IPs for each tunnel endpoint?
5. Do you have an IPAM system for allocating tunnel interface IPs?
6. What crypto policy do you require? (algorithm, hash, DH group, lifetime)
7. Pre-shared key or certificate-based authentication?
8. Will you run a routing protocol over the tunnel? Which one?
9. Do you use a ticketing system? Which one?
10. For hub-and-spoke or mesh: how many tunnels total? Can they be provisioned in parallel?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Sequential | One tunnel (both endpoints) at a time, stop on first failure | Small batch, shared hub device |
| Rolling | N tunnels at a time, stop if failure rate > threshold | Medium/large hub-and-spoke deployments |
| Parallel | All tunnels at once | Full mesh in lab/non-prod, no shared devices |

For hub-and-spoke: the hub is a shared resource. Limit concurrency to avoid overloading it. For full mesh, each tunnel pair is independent and can be parallelized.

---

## 9. Acceptance Criteria

1. Tunnel only provisioned if both endpoints are reachable and healthy
2. Crypto parameters are identical on both sides (generated from single source)
3. Configuration is applied to both endpoints — never just one
4. Tunnel interface is operationally up on both endpoints
5. Traffic passes across the tunnel (ping succeeds from both sides)
6. Routing adjacency forms if a routing protocol is configured over the tunnel
7. Config backup exists for both devices before and after changes
8. Rollback removes tunnel config from both sides if verification fails
9. Evidence report is generated for every tunnel (success or failure)
10. Batch mode respects concurrency limits and stops on threshold breach

````

============================================================
FILE: spec-files/spec-wan-bandwidth-modification.md
DIRECTORY: spec-files/
FILENAME: spec-wan-bandwidth-modification.md
============================================================
SHA256: 4dcc7cab6cb81fe5a02a0989a3469f669bdd3b1f435eeefa710db20bd08041dc

````markdown
# Use Case: WAN Circuit Bandwidth Modification

## 1. Problem Statement

Changing WAN circuit bandwidth — upgrading or downgrading — is a multi-step coordination exercise that touches the service provider, both endpoint routers, QoS policies, monitoring thresholds, and the CMDB. Today, engineers manually update QoS on each end, hope the SP has already provisioned the new rate, and discover mismatches only when users complain about packet loss or throttling. There's no consistent verification that the actual throughput matches the contracted rate.

**Goal:** Automate the end-to-end bandwidth modification — coordinate with the SP, update QoS policies on both endpoints, verify traffic shaping matches the new rate, update records — reducing misconfigurations and ensuring the circuit performs as contracted.

---

## 2. High-Level Flow

```
Validate  →  Pre-Change  →  SP Coordination  →  Apply QoS  →  Verify  →  Close Out
   │              │                │                 │            │            │
   │              │                │                 │            │            │
 Confirm       Capture          Confirm SP         Update       Test        Update
 circuit       current          has provisioned    shaper,      throughput  CMDB,
 exists,       QoS policies,    the new rate       policer,     matches     ticket,
 endpoints     interface        (or trigger        queuing on   new rate,   monitoring
 reachable,    counters,        SP workflow)       both         no drops,   thresholds
 new rate      baseline                            circuit      counters
 valid         throughput                          endpoints    clean
                                                      │
                                                 FAIL? → Rollback QoS to previous values
```

---

## 3. Phases

### Validate
Confirm the circuit exists in inventory. Identify both endpoint devices and interfaces. Verify the target bandwidth is valid for the circuit type (MPLS, internet, point-to-point). Confirm both devices are reachable. If any validation fails, **stop and report the issue**.

### Pre-Change Snapshot
Capture the current state on both endpoints: running QoS policy, interface bandwidth setting, shaper/policer rates, queue counters, interface error counters, and a baseline throughput measurement if possible. This snapshot is the rollback reference.

### SP Coordination
Confirm the service provider has provisioned (or will provision) the new bandwidth on their side. This may be a manual confirmation step (wait for SP ticket closure), an API call to the SP portal, or simply a gate where the engineer confirms readiness. **Do not apply QoS changes until the SP side is confirmed.**

### Apply QoS
Update the QoS policy on both circuit endpoints to match the new bandwidth. This includes: interface bandwidth statement, shaper rate, policer rate, and any class-based queue allocations that reference the circuit speed. Apply to the A-side first, verify, then the Z-side. If the A-side fails, **stop and rollback**.

### Verify
Confirm the changes took effect. Check that the interface bandwidth reflects the new rate, shaper/policer values are correct, and queue allocations are proportional. Run a throughput test if the circuit supports it. Compare interface counters — there should be no unexpected drops or errors. If verification fails, **rollback both endpoints to the pre-change QoS**.

### Close Out
Update the CMDB with the new circuit bandwidth. Update monitoring thresholds (utilization alerts should reference the new rate). Close the change ticket with evidence of pre/post state.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| SP confirmation is a hard gate | No QoS change until SP is ready | Applying new QoS before SP provisions causes drops |
| A-side before Z-side | Sequential, not simultaneous | If A-side fails, Z-side is untouched and rollback is simpler |
| Pre-change snapshot is mandatory | No snapshot = no modification | Must have a rollback reference |
| Verification includes counter checks | Not just config — actual behavior | Config can be correct but not applied (pending commit, etc.) |
| Monitoring thresholds updated automatically | Part of close-out, not manual | Stale thresholds cause false alerts on every bandwidth change |

---

## 5. Scope

**In scope:** MPLS circuits, internet circuits, point-to-point circuits. QoS policy updates on both endpoints. Shaper, policer, and queue adjustments. SP coordination gate. Throughput verification. CMDB and monitoring updates. Rollback on failure.

**Out of scope:** SP-side provisioning (that's the provider's responsibility or a separate integration). Circuit turn-up or decommission (separate use cases). Routing protocol changes. Physical interface upgrades (e.g., swapping a 1G SFP for a 10G). Multi-path/ECMP rebalancing.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| QoS applied before SP provisions new rate | Packet loss — shaper exceeds SP policer | Hard gate on SP confirmation before applying |
| A-side and Z-side mismatch | Asymmetric shaping, one direction throttled | Sequential apply with verification after each side |
| Rollback fails on one endpoint | One side on old policy, other on new | Alert engineer; capture both states for manual remediation |
| Throughput test disrupts production traffic | Brief service impact | Use non-intrusive measurement where possible; schedule in change window |
| CMDB not updated after change | Stale records, future changes use wrong baseline | CMDB update is part of the automated close-out, not a manual step |

---

## 7. Requirements

### What the automation must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Execute CLI commands on network devices | Yes | Cannot proceed |
| Read and modify QoS policies on devices | Yes | Cannot proceed |
| Capture interface counters and statistics | Yes | Verification is limited to config only |
| Orchestrate multi-step workflows with gates | Yes | Cannot proceed |
| Roll back configuration changes | Yes | Engineer rolls back manually |
| Run throughput or bandwidth tests | No | Verify via counters and config only |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| CMDB / circuit inventory | Identify circuit, endpoints, current rate | Yes | Engineer provides details manually |
| ITSM / ticketing | Track the change, SP coordination | No | Engineer coordinates manually |
| SP portal / API | Confirm SP-side provisioning | No | Engineer confirms manually (gate becomes a pause) |
| Monitoring | Update utilization thresholds | No | Engineer updates thresholds manually |

### Discovery Questions

Ask the engineer before designing the solution:

1. What circuit types are in scope? (MPLS, internet, point-to-point, all?)
2. What is the current bandwidth and target bandwidth?
3. How do you coordinate with the service provider? (Ticket, portal, API, phone call?)
4. What QoS model do you use? (Flat shaper, hierarchical, class-based?)
5. Are both endpoints managed by your team, or is one SP-managed?
6. Do QoS class allocations change proportionally with bandwidth, or are they fixed?
7. Do you have a way to test throughput non-disruptively?
8. What CMDB or inventory system tracks circuit bandwidth?
9. What monitoring system needs threshold updates?
10. Should this run during a change window, or can it be done live?

---

## 8. Batch Strategy

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| Single circuit | One circuit, both endpoints, sequential | Default for ad-hoc changes |
| Sequential batch | One circuit at a time from a list | Planned bandwidth refresh across multiple circuits |
| Grouped by site | All circuits at a site, then move to next site | Site-level bandwidth upgrade coordinated with SP |

---

## 9. Acceptance Criteria

1. Bandwidth modification only proceeds after SP-side provisioning is confirmed
2. QoS policies on both endpoints reflect the new bandwidth (shaper, policer, queues)
3. Interface bandwidth setting matches the new contracted rate
4. Pre-change and post-change snapshots are captured and stored
5. Rollback restores both endpoints to the original QoS policy if verification fails
6. No unexpected packet drops or errors after the change
7. CMDB reflects the updated circuit bandwidth
8. Monitoring thresholds are updated to reference the new rate

````
