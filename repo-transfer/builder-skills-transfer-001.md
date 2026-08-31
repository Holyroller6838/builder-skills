# Builder Skills Repository Transfer — Part 001 of 011

**Git commit:** `982d97c1573ca7ea892b39acced9b0d15955c4a9` on branch `main`  
**Generated:** 2026-08-31 21:28:30 UTC  
**See also:** `builder-skills-transfer-manifest.md` for the full repository manifest, directory tree, and complete checksum index across all parts.

This part contains **30** file(s):

- `.claude-plugin/marketplace.json`
- `.claude-plugin/plugin.json`
- `.claude/skills/builder-agent/SKILL.md`
- `.claude/skills/documentation/SKILL.md`
- `.claude/skills/explore/SKILL.md`
- `.claude/skills/flowagent-to-spec/SKILL.md`
- `.claude/skills/flowagent/SKILL.md`
- `.claude/skills/iag/SKILL.md`
- `.claude/skills/itential-devices/SKILL.md`
- `.claude/skills/itential-golden-config/SKILL.md`
- `.claude/skills/itential-inventory/SKILL.md`
- `.claude/skills/itential-json-forms/SKILL.md`
- `.claude/skills/itential-lcm/SKILL.md`
- `.claude/skills/itential-mop/SKILL.md`
- `.claude/skills/project-to-spec/SKILL.md`
- `.claude/skills/qa-agent/SKILL.md`
- `.claude/skills/solution-arch-agent/SKILL.md`
- `.claude/skills/solution-arch-agent/pull-platform-data.py`
- `.claude/skills/spec-agent/SKILL.md`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/pull_request_template.md`
- `.github/workflows/pr-compliance.yml`
- `.gitignore`
- `AGENTS.md`
- `CLA.md`
- `CLAUDE.md`
- `CODEOWNERS`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`

---

============================================================
FILE: .claude-plugin/marketplace.json
DIRECTORY: .claude-plugin/
FILENAME: marketplace.json
============================================================
SHA256: 1bba898b36cc04b2d58112a1b7d839f67435993f591064a57b5ca84e69d8df22

````json
{
  "name": "itential-builder",
  "owner": {
    "name": "Itential",
    "email": "support@itential.com"
  },
  "metadata": {
    "description": "AI agent skills for the Itential Platform — deliver infrastructure automation from spec through acceptance testing and as-built documentation.",
    "version": "1.5.0"
  },
  "plugins": [
    {
      "name": "itential-builder",
      "source": {
        "source": "github",
        "repo": "itential/builder-skills"
      },
      "description": "AI agent skills for the Itential Platform — deliver infrastructure automation from spec through acceptance testing and as-built documentation. Covers requirements, feasibility, design, build, QA/acceptance testing, FlowAgent, IAG, and MOP.",
      "version": "1.5.0",
      "author": {
        "name": "Itential"
      },
      "homepage": "https://github.com/itential/builder-skills",
      "repository": "https://github.com/itential/builder-skills",
      "license": "GPL-3.0-or-later",
      "keywords": ["itential", "network-automation", "infrastructure", "flowagent", "iag"],
      "category": "automation"
    }
  ]
}

````

============================================================
FILE: .claude-plugin/plugin.json
DIRECTORY: .claude-plugin/
FILENAME: plugin.json
============================================================
SHA256: d0bab506a58971d7ce9b645aed610a238e0e67e85fa69d73a4577a345992e97e

````json
{
  "name": "itential-builder",
  "description": "AI agent skills for the Itential Platform — deliver infrastructure automation from spec through acceptance testing and as-built documentation. Covers requirements, feasibility, design, build, QA/acceptance testing, FlowAgent, IAG, and MOP.",
  "version": "1.5.0",
  "author": {
    "name": "Itential"
  },
  "homepage": "https://github.com/itential/builder-skills",
  "repository": "https://github.com/itential/builder-skills",
  "license": "GPL-3.0-or-later",
  "keywords": ["itential", "network-automation", "infrastructure", "flowagent", "iag"],
  "commands": "./.claude/skills"
}

````

============================================================
FILE: .claude/skills/builder-agent/SKILL.md
DIRECTORY: .claude/skills/builder-agent/
FILENAME: SKILL.md
============================================================
SHA256: 8c76a60f6cff60386035916f3f806b82e43e3d72c7cef56a7e41713d2ce04eb9

````markdown
---
name: builder-agent
description: Use this skill when someone has an approved solution design and is ready to build. Trigger it for phrases like "solution design is approved", "go ahead and build", "implement the design", "create the workflows", "build everything per the design", or "the design is locked — implement it". Also trigger it when a build is failing mid-way and needs debugging, or when /qa-agent hands back a failing test case for a fix. This skill implements the approved solution-design.md end-to-end — creating all workflows, templates, projects, and configs, and testing each component individually. If the user has a solution-design.md and wants to turn it into working automation, this is the right skill. Invoke after /solution-arch-agent produces an approved solution-design.md. Hands off to /qa-agent once the build is complete — /qa-agent owns acceptance testing and the as-built record.
---

# Builder Agent

**Stage:** Build
**Owns:** Implementing the approved design.
**Receives from:** `/solution-architecture` (approved `solution-design.md` + complete workspace)
**Produces:** Deployed assets (workflows, templates, projects)
**Hands off to:** `/qa-agent` (acceptance testing + as-built record)

---

## Stage Expectations

### Build

| | |
|--|--|
| **Engineer provides** | Approved `solution-design.md` (all platform data already present in workspace) |
| **Agent does** | Builds all components per design, tests each piece individually, reports delivery outcomes |
| **Engineer action** | Reviews delivery and resolves open build questions |
| **Deliverable** | Deployed assets (workflows, templates, projects) |
| **Customer receives** | Delivered project — all workflows, templates, and configs individually tested, packaged, and access granted. Formal acceptance testing and sign-off happen next, in `/qa-agent`. |

Build implements the approved plan. The builder never re-pulls discovery data — it uses what the Solution Architecture Agent left in the workspace. If any required file is missing, stop and surface as an upstream failure.

**Testing during Build is component-level, not acceptance-level.** "Test each piece" here means confirming a task or workflow runs without error and wires variables correctly — not verifying the delivered solution satisfies the customer's stated acceptance criteria end-to-end. That's `/qa-agent`'s job, running against the completed build with real test data the engineer confirms. Don't skip component testing because "QA will catch it" — a structurally broken workflow wastes a live acceptance-test run.

---

This skill covers everything needed to build and test Itential automation assets: projects, workflows, templates, and command templates.

## Workspace Contract

**The builder receives a complete workspace. All discovery data is already present.** Solution-design (or setup for explore mode) has already pulled everything.

**Required files (must exist before build starts):**
```
{use-case}/
  .auth.json              ← auth token
  .env                    ← credentials (for re-auth if token expires)
  openapi.json            ← API reference (pulled by solution-arch-agent or explore)
  tasks.json              ← task catalog (pulled by solution-arch-agent or explore)
  apps.json               ← app/adapter type names (pulled by solution-arch-agent or explore)
  adapters.json           ← adapter instances (pulled by solution-arch-agent or explore)
  applications.json       ← app health (pulled by solution-arch-agent or explore)
```

**May also exist (spec-contingent):**
```
  use-case-memory.md      ← living context: IDs, decisions, gotchas, open items — READ THIS FIRST
  customer-spec.md        ← approved HLD (Requirements)
  feasibility.md          ← approved feasibility assessment
  customer-context.md     ← business rules (if provided)
  solution-design.md      ← approved Solution Design / LLD
  devices.json            ← device inventory
  workflows.json          ← existing workflows
  device-groups.json      ← device groups
  task-schemas.json       ← fetched on demand during build (append-only, never pre-populated)
  test-report.md          ← if returning from /qa-agent with a failing test case — has the exact case ID, expected vs actual, and evidence
```

**The builder NEVER re-pulls bootstrap or discovery data.** If `tasks.json`, `apps.json`, or `adapters.json` is missing, stop and tell the user — that's an upstream failure, not something to silently fix.

**Exception — `.auth.json` bootstrap:** If `.auth.json` is missing but `.env` exists with `AUTH_METHOD=oauth`, `CLIENT_ID`, and `CLIENT_SECRET`, the builder MUST authenticate and create `.auth.json` before proceeding — do NOT stop and report an upstream failure. See the **Bootstrap Authentication** section below.

**The only API calls the builder makes are:**
- **Auth bootstrap** — POST /oauth/token when `.auth.json` is missing (see below)
- **Create** — POST workflows, templates, projects
- **Update** — PUT to edit assets
- **Test** — POST jobs/start, GET job status
- **Schema fetch** — task schemas not yet in `task-schemas.json` (append to file after fetching)
- **Re-auth** — if token expires, use `.env` to refresh `.auth.json`

### Bootstrap Authentication

When `.auth.json` is missing but `.env` has `AUTH_METHOD=oauth` with `CLIENT_ID` and `CLIENT_SECRET`, authenticate automatically before proceeding.

**The correct Itential SaaS/Cloud OAuth endpoint is:**
```
POST {PLATFORM_URL}/oauth/token
Content-Type: application/x-www-form-urlencoded
```

**Body (form-encoded, NOT JSON — JSON returns 415):**
```
grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}
```

**Critical:**
- Content-Type MUST be `application/x-www-form-urlencoded` — NOT `application/json`. Sending JSON returns HTTP 415.
- The `/login` endpoint does NOT support OAuth client credentials on SaaS instances — always use `/oauth/token`.
- On success, write `.auth.json` with the token so all subsequent API calls just work.

**Helper script:** `${CLAUDE_PLUGIN_ROOT}/scripts/oauth_bootstrap.py` — reads `.env`, POSTs to `/oauth/token`, writes `.auth.json`. The builder should run this automatically when `.auth.json` is missing and `.env` has `AUTH_METHOD=oauth`.

---

## Build Lifecycle

```
0. Memory file              → create or read use-cases/{name}/use-case-memory.md
1. Decompose                → identify parent/child split before writing any code
2. Create project           → container for all assets
3. Discover tasks           → search tasks.json, fetch schemas
4. Build children first     → each child workflow independently testable
5. Build templates          → Jinja2 (config gen) or TextFSM (output parsing)
6. Build command templates  → MOP pre/post checks with validation rules
7. Build orchestrator last  → parent wires tested children via childJob
8. Add assets to project    → move/copy into the project
9. Set project membership   → resolve spec members, PATCH immediately after import
10. Test each component     → jobs/start, check results (component-level, not acceptance-level)
11. Debug                   → check job.error, filesystem-first
12. Reconcile               → diff built vs designed, update artifacts
13. Update memory file      → record IDs, decisions, gotchas, test results, open items
14. Update this skill       → if you hit a platform behavior not documented here, add it before closing out
15. Hand off to /qa-agent   → build is complete; real IDs are in solution-design.md §D
```

**Step 0 — memory file:**

At the start of every session, check for `use-cases/{use-case}/use-case-memory.md`:
- **Exists** → read it before doing anything else. It tells you the platform, project ID, what's already built, decisions made, and open items. Don't re-discover what's already documented.
- **Missing** → create it now from `${CLAUDE_PLUGIN_ROOT}/helpers/use-case-memory.md` template. Fill in Platform URL, `Stage: build`, `Status: active` immediately.

**Step 13 — update memory file after every session:**

Before closing out any build session, update `use-case-memory.md` with:
- Any new asset IDs (project ID, workflow UUIDs, transformation IDs, adapter names)
- Any architectural decisions made and **why**
- Any gotchas hit and how they were fixed
- Test results (date, what was tested, outcome)
- Updated open items list
- `Stage` and `Status` if they changed — mid-build, `Stage` stays `build`; only update it to `test` at the Step 15 handoff

The memory file is what makes it possible to pick up a use-case after weeks without re-discovering everything from scratch.

**Step 14 — how to update this skill:**
- New platform behavior (error shape, field constraint, task gotcha) → add detail to the relevant body section (`### query`, `### childJob`, `### Projects`, etc.), then add a one-liner to the Gotchas pre-flight list under the right category.
- New pattern or workflow recipe → add to `## Workflow Patterns` and, if the pattern is reusable, export the project from the platform and save it to `${CLAUDE_PLUGIN_ROOT}/helpers/assets/`. Add a row to the Helper Templates table in this file pointing to it.
- Do NOT create a new top-level section for a single finding — put it where a builder would look when working on that topic.

**Step 15 — hand off to `/qa-agent`:** Once every component has been individually tested and `solution-design.md` Section D has real IDs (project ID, workflow IDs) instead of placeholders, the build is complete. Update `use-case-memory.md` to `Stage: test` before ending the session. Tell the engineer the build is done and route to `/qa-agent` for acceptance testing and the as-built record — don't write `as-built.md` here.

**If `/qa-agent` hands back a failing test case:** fix the specific issue it identifies (it gives you the case ID, expected vs. actual, and evidence — a job ID or static-check output). Don't re-examine the whole build; the failure report tells you exactly what broke. Once fixed, tell the engineer so `/qa-agent` can re-run just that case.

---

## Guides

### Guide 1: Build a workflow end-to-end

Follow these steps in order. Do not skip any step.

---

> **STOP. Before writing a single line of task JSON — run these commands.**
>
> The asset projects in `helpers/assets/` are real, production-tested imports. Read them first.
> Do not guess task structure from memory. Do not copy from `helpers/create/` for task bodies.
> `helpers/create/` is for API wrappers (project/workflow creation endpoints) only — not task JSON.
>
> ```bash
> # 1. Find which asset project matches your use case
> ls ${CLAUDE_PLUGIN_ROOT}/helpers/assets/
>
> # 2. Extract the workflow most similar to what you're building
> jq '[.components[] | select(.type=="workflow")] | .[].document.name' \
>   ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-servicenow.json
>
> # 3. Read its full task map — this is your reference
> jq '[.components[] | select(.type=="workflow") | select(.document.name | test("WORKFLOW_NAME"; "i"))] | first | .document | {tasks, transitions}' \
>   ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-servicenow.json
>
> # 4. Extract the specific task type you need
> jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "TASK_NAME")] | first | .value' \
>   ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-servicenow.json
> ```
>
> Replace `vendor-servicenow.json` with whichever asset file best matches your use case:
> - Adapter tasks (ServiceNow, Infoblox) → `vendor-servicenow.json`, `vendor-infoblox-nios-ddi.json`
> - Network device tasks (CLI, MOP) → `vendor-cisco-ios.json`, `vendor-arista-eos.json`, `vendor-juniper-junos.json`
> - IPAM/inventory → `vendor-netbox.json`
> - Data transformations → `itential-platform-data-manipulation.json`
> - Config management (RunCommandTemplate, itential_cli) → `itential-platform-configuration-management.json`
> - LCM action workflows → `helpers/assets/lcm/lcm-vxlan-fabric-services-project.json`

---

**Step 0: Decompose before you build.**

Before writing any JSON, identify the parent/child split from the solution design. Ask for each phase:

- Can this phase be run and tested on its own? → **Child workflow**
- Does it loop over multiple items (devices, records)? → **Child workflow with `loopType`**
- Is it reusable across other use cases? → **Child workflow**
- Is it a simple sequential step with no independent test value? → **Task in orchestrator**

Build order is always: **children first, orchestrator last.** The orchestrator is just childJob calls to tested children — it should not contain raw adapter tasks unless there is no logical way to split.

**Read a full workflow from asset projects before building any multi-workflow solution:**
```bash
# Parent → childJob → evaluation pattern
jq '[.components[] | select(.type=="workflow") | select(.document.name | test("Upgrade|Runner"))] | first | .document | {name,tasks,transitions}' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json

# childJob loop with data_array
jq '[.components[] | select(.type=="workflow") | select(.document.name | test("Chunk|Loop"))] | first | .document | {name,tasks,transitions}' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/itential-platform-configuration-management.json
```

**Step 1: Find tasks.** Search `tasks.json` for the tasks you need:
```bash
jq '.[] | select(.name | test("keyword"; "i")) | {name, app, type, location, canvasName, displayName}' {use-case}/tasks.json
```

**Step 2: Resolve adapter app names.** For adapter tasks, the `app` in tasks.json is WRONG. Look up the correct name:
```bash
jq '.[] | select(.name | test("keyword"; "i")) | {name, type}' {use-case}/apps.json
```
Also get the adapter instance name:
```bash
jq '.results[] | select(.package_id | test("keyword"; "i")) | {id, state}' {use-case}/adapters.json
```
You now have three values: `app` (from apps.json), `adapter_id` (from adapters.json `.id`), and `displayName` (from tasks.json).

**Step 3: Fetch task schemas.** Get the full input/output schema for every task you'll use:
```
POST /automation-studio/multipleTaskDetails?dereferenceSchemas=true
```
```json
{
  "inputsArray": [
    {"location": "Adapter", "pckg": "Servicenow", "method": "createChangeRequest"},
    {"location": "Application", "pckg": "WorkFlowEngine", "method": "query"}
  ]
}
```
Use the `pckg` value from apps.json (Step 2), NOT tasks.json. Save the response to `{use-case}/task-schemas.json`.

**Step 4: Map schema to workflow task JSON.** For each task, transform the schema into a workflow task:

Schema response:
```json
{
  "name": "createChangeRequest",
  "variables": {
    "incoming": {
      "body": {"type": "object", "description": "Request body"}
    },
    "outgoing": {
      "result": {"type": "object", "description": "Response"}
    }
  }
}
```

Becomes this workflow task (extract a real adapter task from an asset project first — e.g. `jq '[.components[].document.tasks // {} | to_entries[] | select(.value.location == "Adapter")] | first | .value' ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-servicenow.json`):
```json
{
  "a1b2": {
    "name": "createChangeRequest",
    "canvasName": "createChangeRequest",
    "summary": "Create Change Ticket",
    "description": "Creates a ServiceNow change request",
    "location": "Adapter",
    "locationType": "Servicenow",
    "app": "Servicenow",
    "type": "automatic",
    "displayName": "ServiceNow",
    "variables": {
      "incoming": {
        "body": "$var.e1a1.merged_object",
        "adapter_id": "$var.job.adapter_id"
      },
      "outgoing": {
        "result": null
      },
      "error": "",
      "decorators": []
    },
    "groups": [],
    "actor": "Pronghorn",
    "scheduled": false,
    "nodeLocation": {"x": 700, "y": 600}
  }
}
```

**Mapping rules:**
- `name`, `canvasName` → from tasks.json
- `app`, `locationType` → from apps.json (NOT tasks.json)
- `displayName` → from tasks.json
- `location` → `"Adapter"` or `"Application"` (from tasks.json)
- `type` → from tasks.json directly — do not guess. It is per-task, not per-app. Read it alongside name, app, location, and canvasName: `jq '.[] | select(.name == "taskName") | {name, app, type, canvasName, location}' tasks.json`
- `actor` → `"Pronghorn"` for all tasks except childJob (which uses `"job"`)
- `incoming` → each schema key becomes a variable. Wire with `$var` for top-level values
- `outgoing` → set to `null` (capture later with `$var.taskId.outVar`)
- **Add `adapter_id`** to incoming for adapter tasks (not in schema, always required)
- **Add `error` and `decorators`** to variables block

**Step 5: Handle object inputs.** If a task's incoming variable is `type: "object"` (like `body`), you CANNOT put `$var` references inside it — they won't resolve. Use a `merge` task before it:

```json
{
  "e1a1": {
    "name": "merge",
    "canvasName": "merge",
    "summary": "Build Request Body",
    "app": "WorkFlowEngine",
    "type": "operation",
    "variables": {
      "incoming": {
        "data_to_merge": [
          {"key": "short_description", "value": {"task": "job", "variable": "short_description"}},
          {"key": "description", "value": {"task": "job", "variable": "description"}}
        ]
      },
      "outgoing": {"merged_object": null}
    },
    "actor": "Pronghorn"
  }
}
```
Then wire the adapter task's `body` to `"$var.e1a1.merged_object"`.

**Step 6: Handle opaque schemas.** Some task schemas show `body: {type: "object"}` with no inner field details. The adapter validates internally. To discover required fields:
1. Try creating with minimal fields — the error message lists what's missing (e.g., `"must have required property 'summary'"`)
2. Check `openapi.json` for the adapter's endpoint schema
3. Call the adapter directly: `POST /{adapter_id}/{method}` with `{}` body — read the validation error

**Step 7: Wire transitions.** Every adapter task needs BOTH success and error transitions:
```json
"transitions": {
  "a1b2": {
    "b2c3": {"type": "standard", "state": "success"},
    "ef01": {"type": "standard", "state": "error"}
  }
}
```
If both success and error need to reach `workflow_end`, route error to an intermediate `newVariable` task first (JSON can't have duplicate keys).

**Step 8: Add inputSchema/outputSchema.** List all job variables the workflow expects as input and produces as output.

**Step 9: Pre-submit checklist.**
- [ ] Task IDs are hex-only (`[0-9a-f]{1,4}`)
- [ ] `app` and `locationType` values come from apps.json `.name`, NOT tasks.json and NOT the adapter instance name (e.g., `EmailOpensource` not `email`)
- [ ] `adapter_id` is the adapter **instance** name (e.g., `email`), NOT the type name
- [ ] `adapter_id` values come from `adapters.json` `.results[].id` — NEVER from the spec's adapter identity table. The spec is a design document; `adapters.json` is the source of truth for the target environment.
- [ ] `canvasName` values come from tasks.json `canvasName` field
- [ ] Every adapter task has `adapter_id` in incoming
- [ ] Every adapter task has an error transition
- [ ] `evaluation` tasks have both success AND failure transitions
- [ ] `evaluation` operators are from the closed enum (`contains, !contains, <, <=, >, >=, ==, !=`) — no others exist
- [ ] `evaluation` `operand_2` literal values containing regex metacharacters (`.`, `(`, `)`, `[`, `]`, `?`, `+`, `*`, `|`) are properly escaped, OR stored in a `newVariable` constant-holder task to avoid `incomingRefs` cache issues after API PUT
- [ ] No `$var.<taskId>.<out>` references inside nested forEach bodies — use `$var.job.<varName>` instead
- [ ] Incoming variable types match task schema exactly (arrays for `to`/`cc`/`bcc`, numbers for `page`/`pageSize`, etc.)
- [ ] No `$var` references inside nested objects (use merge/makeData)
- [ ] merge uses `"variable"`, childJob uses `"value"`
- [ ] No `{task:"job", variable:"x"}` in merge/childJob for workflow-internal variables — `{task:"job"}` refs add `x` to `inputSchema.required`, prompting operators for values that should be internal. Use the producing task ref instead (query→`return_data`, newVariable→`value`, makeData→`output`, merge→`merged_object`)
- [ ] If a `query` downstream of a `childJob` returns null despite the child succeeding: check whether `"obj": "$var.<childJobId>.job_details"` is resolving — on some platform versions it is treated as a literal string. Fix: insert a `merge` task between childJob and query using `{"task": "<childJobId>", "variable": "job_details"}` in `data_to_merge`, then point `obj` to `$var.<mergeId>.merged_object` (see Guide 4)
- [ ] childJob has `actor: "job"`, all others have `actor: "Pronghorn"`
- [ ] `workflow_end` transition is empty `{}`
- [ ] Canvas layout follows the vertical spacing convention — non-forked sequences on a constant-x spine, fork branches offset to `spine±264` and stay in their own column until convergence
- [ ] No transition lines cross task nodes (the spine column is empty between a fork and its convergence point)
- [ ] Sequential y-delta ~108px (tight grid)
- [ ] **LCM Create actions only:** the instance-write merge task's `data_to_merge` covers every field in the resource model's `schema.required` array — missing even one field causes an instance write failure after provisioning (resources are orphaned from LCM). Read the model's `schema.required` before building the merge task: `jq '.schema.required' helpers/assets/lcm/<model>.json`
- [ ] **ViewData manual tasks:** `view` is a top-level field; `incoming.variables` is present (even if `{}`); `displayName: "Tools"`, no `actor` field
- [ ] **restCall downstream query:** path targets body field directly (e.g., `"access_token"`) — NOT `"response.access_token"` (restCall has no wrapper, unlike adapter tasks)
- [ ] **childJob loop:** if child workflow has `inputSchema.required` fields beyond what each `data_array` element contains, use the forEach enrichment pattern (forEach → merge → arrayPush) to add shared fields into each element before the childJob loop; set `variables: {}` on the childJob
- [ ] **forEach body:** `incoming` contains ONLY `data_array` (no `job_id`); loop body tasks have no external error transitions; last body task has an empty `{}` transition; `$var.job.<varName>` inside loop body instead of `$var.<taskId>.<output>`
- [ ] **makeData with childJob-sourced merge:** if a merge task references a childJob variable, do NOT wire that merge's `merged_object` into `makeData.incoming.variables` — use `query` to extract individual values first

**Complete working example:** Read the ServiceNow "Create Change Request" workflow before building — it demonstrates merge → adapter create → query → adapter update with error transitions:
```bash
jq '[.components[] | select(.type=="workflow") | select(.document.name | test("Create Change"))] | first | .document' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-servicenow.json
```

**How the example works — what each task does and why:**

```
workflow_start → e1a1 (merge) → a1b2 (createChangeRequest) → b2c3 (query) → c3d4 (updateChangeRequest) → workflow_end
                                  ↓ error                                      ↓ error
                                ef01 (newVariable) ────────────────────────────→ workflow_end
```

| Task ID | Task | Why it's there | Key fields |
|---------|------|----------------|------------|
| `e1a1` | `merge` | Builds the `body` object. `$var` can't resolve inside nested objects, so merge assembles the object from individual variables. | `data_to_merge` uses `"variable"` (NOT `"value"`). Needs at least 2 items. |
| `a1b2` | `createChangeRequest` | Adapter call. `body` wired to `$var.e1a1.merged_object` (merge output). | `app`/`locationType` from apps.json (`Servicenow`), NOT tasks.json (`ServiceNow`). `adapter_id` added manually (not in schema). `type: "automatic"`. |
| `b2c3` | `query` | Extracts the change ID from the adapter response. | `query: "response.id"` — adapters transform responses, don't assume native API shape. |
| `c3d4` | `updateChangeRequest` | Second adapter call using the extracted ID. | `changeId` wired from `$var.job.changeId` (set by query's outgoing). |
| `ef01` | `newVariable` | Error handler. Adapter error transitions route here. | Exists because JSON can't have duplicate keys — can't route both success and error to `workflow_end` from the same task. |

**Field mapping — where each value comes from:**

| Workflow task field | Source | Example |
|---------------------|--------|---------|
| `name` | tasks.json `.name` | `createChangeRequest` |
| `canvasName` | tasks.json `.canvasName` | `createChangeRequest` (can differ: `arrayPush`→`push`) |
| `app` | **apps.json** `.name` (adapter **type** name) | `Servicenow`, `EmailOpensource` (NOT `email`, NOT `ServiceNow` from tasks.json) |
| `locationType` | Same as `app` for adapters, `null` for applications | `Servicenow`, `EmailOpensource` |
| `displayName` | tasks.json `.displayName` | `ServiceNow`, `email` |
| `location` | tasks.json `.location` | `Adapter` or `Application` |
| `type` | tasks.json `.type` — read directly, do not guess (per-task, not per-app) | varies |
| `actor` | `"Pronghorn"` always, except childJob which uses `"job"` | `Pronghorn` |
| `adapter_id` | adapters.json `.results[].id` (adapter **instance** name) | `servicenow-prod`, `email` — this goes in `incoming`, NOT in the task-level `app` field |
| incoming vars | From task schema (multipleTaskDetails) | `body`, `changeId` |
| outgoing vars | From task schema, set to `null` | `result` |

### Guide 2: Debug a failed job

**Step 1:** Get the job:
```
GET /operations-manager/jobs/{jobId}
```

**Step 2:** Check `data.status`. If `"error"`, read `data.error[]`:
```
data.error[].task → failing task ID
data.error[].message.IAPerror.displayString → human-readable error
```

**Step 3:** Match the error to a fix:

| Error message | Cause | Fix |
|---------------|-------|-----|
| "Schema validation failed on must have required property 'X'" | Missing field in adapter body | Add the field to merge task |
| "Method not found" | Wrong task name or app | Check tasks.json and apps.json |
| "No available transitions" | Missing error transition | Add `"state": "error"` transition |
| "Cannot find workflow" | childJob ref broken after project move | Update `workflow` field with `@projectId:` prefix |
| "Referenced job variable: undefined" | merge uses `"value"` instead of `"variable"` | Change to `"variable"` in `data_to_merge` |
| Job stuck in `"running"` | No error transition on failed task | Add error transition |

**Step 4:** Fix locally, PUT to update, re-run. Don't recreate — updating preserves the ID.

### Guide 2b: Work with any unfamiliar adapter task

Follow Guide 1 Steps 1-6 for discovery. Quick reference for the lookup commands:

```bash
# Step 1 — find the task
jq '.[] | select(.app | test("meraki";"i")) | {name, app, displayName}' {use-case}/tasks.json

# Step 2 — get the correct app name (tasks.json app field is often wrong for adapters)
jq '.[] | select(.name | test("meraki";"i")) | {name, type}' {use-case}/apps.json

# Step 2 — get the adapter instance name
jq '.results[] | select(.package_id | test("meraki";"i")) | {id, state}' {use-case}/adapters.json

# Step 3 — fetch the task schema
# POST /automation-studio/multipleTaskDetails?dereferenceSchemas=true
# {"inputsArray": [{"location": "Adapter", "pckg": "<app from apps.json>", "method": "<task name>"}]}
```

You now have three values: `app` (from apps.json), `adapter_id` (from adapters.json `.id`), `displayName` (from tasks.json). Two things to pay extra attention to beyond Guide 1:

**Enforce data types from the schema.** When the schema says `"type": "array"`, you MUST pass an array — even for single values:
- `"to": "user@example.com"` → WRONG. Use `"to": ["user@example.com"]`
- `"pageSize": "100"` → WRONG if schema says number. Use `"pageSize": 100`
- `"cc": ""` → OK only if schema allows string; if array, use `"cc": []`

Always check `task-schemas.json` for the exact type of each incoming field before wiring.

**Inspect the actual response before wiring a query path.** Adapter responses are transformed — they do not match the native API's structure. After a successful test run:
1. `GET /operations-manager/jobs/{jobId}` — find the task in `data.tasks` by its task ID
2. Read the task's outgoing variables — that is the real response object
3. Use `jq` to explore: `jq '.data.tasks["a1b2"]' job.json`
4. Wire the `query` path from what you see — not from the upstream API docs

**End-to-end sequence:**
```
1. tasks.json search   → found "getDevice", app "networkAdapter"
2. apps.json lookup    → correct app name is "NetworkAdapter" (capital N)
3. adapters.json       → adapter_id is "network-prod-1"
4. multipleTaskDetails → incoming: {deviceId: string}, outgoing: {result: object}
5. Build + test        → job completes
6. Inspect job         → result is {"response": {"hostname": "...", "model": "..."}}
7. Wire query path     → "response.hostname" (NOT "result.hostname" or "data.hostname")
```

### Guide 3: Add a task to an existing workflow

**Step 1:** Extract the task structure from an asset project that uses the same task type:
```bash
# Adapter task (e.g., ServiceNow)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.location == "Adapter")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-servicenow.json

# Application task (WorkFlowEngine)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.app == "WorkFlowEngine" and .value.name != "childJob")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/itential-platform-configuration-management.json

# childJob
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "childJob")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json
```

**Step 2:** Fill in the fields using the mapping rules from Guide 1 Step 4.

**Step 3:** Generate a hex task ID (e.g., `d4e5`) — must be `[0-9a-f]{1,4}`.

**Step 4:** Add the task to `tasks` and add transitions. Remember error transitions on adapter tasks.

**Step 5:** Update via `PUT /automation-studio/automations/{id}` with `{"update": {...}}`.

### Guide 4: Build a childJob (parent calls child workflow)

childJob has two modes. Both are tested and verified on a live platform.

#### Mode A: Single child — pass variables with `{"task","value"}`

The parent passes specific variables to one child workflow run.

**Parent childJob task:**
```json
{
  "a1a1": {
    "name": "childJob",
    "canvasName": "childJob",
    "summary": "Run Single Child",
    "location": "Application",
    "locationType": null,
    "app": "WorkFlowEngine",
    "type": "operation",
    "displayName": "WorkFlowEngine",
    "variables": {
      "incoming": {
        "task": "",
        "workflow": "My Child Workflow",
        "variables": {
          "deviceName": {"task": "job", "value": "targetDevice"},
          "action": {"task": "static", "value": "validate"}
        },
        "data_array": "",
        "transformation": "",
        "loopType": ""
      },
      "outgoing": {"job_details": null}
    },
    "actor": "job"
  }
}
```

**Variable passing rules (uses `"value"`, NOT `"variable"`):**
- `{"task": "job", "value": "targetDevice"}` → passes the parent's `targetDevice` job variable to the child as `deviceName`
- `{"task": "static", "value": "validate"}` → passes the literal string `"validate"`
- `{"task": "b2c3", "value": "return_data"}` → passes a previous task's output (preferred for runtime data)

> **WARNING — `{task:"job"}` refs in childJob variables add fields to `inputSchema.required`** — same behavior as merge (see `### merge` section). Only use `{task:"job", value:"x"}` for genuine workflow inputs. For runtime data produced by earlier tasks, use `{task:"<taskId>", value:"<outVar>"}` to reference the producing task directly.

> **WRONG for task output refs in childJob:**
> `{"task": "b2c3", "variable": "return_data"}` — `"variable"` is for merge/evaluation only.
> In childJob, ALL refs (job, static, AND task output) use `"value"`. Using `"variable"` causes `undefined.indexOf()` at job start time (P6.4.0+) — the workflow fails before any task runs.

**Extracting single child output:**
```json
{
  "b2b2": {
    "name": "query",
    "variables": {
      "incoming": {
        "pass_on_null": false,
        "query": "taskStatus",
        "obj": "$var.a1a1.job_details"
      },
      "outgoing": {"return_data": "$var.job.childStatus"}
    }
  }
}
```
Query uses flat variable names — `"taskStatus"`, NOT `"variables.job.taskStatus"`.

**If the query returns null even though the childJob succeeded** — the `$var` form in `obj` may not resolve on your platform version. Use the merge+taskRef workaround:
```
a1a1 (childJob) → m1m1 (merge: captures job_details via taskRef) → b2b2 (query: reads merged_object)
```
```json
{
  "m1m1": {
    "name": "merge",
    "variables": {
      "incoming": {
        "data_to_merge": [
          {"task": "a1a1", "variable": "job_details"},
          {"task": "static", "value": {}}
        ]
      },
      "outgoing": {"merged_object": null}
    }
  },
  "b2b2": {
    "name": "query",
    "variables": {
      "incoming": {
        "pass_on_null": false,
        "query": "taskStatus",
        "obj": "$var.m1m1.merged_object"
      },
      "outgoing": {"return_data": "$var.job.childStatus"}
    }
  }
}
```
The static `{}` second item is required — merge needs at least 2 items in `data_to_merge`.

#### Mode B: Loop — one child per item in `data_array`

Each element in `data_array` becomes the child's input variables for that iteration. Set `variables: {}` (empty).

**Parent childJob task:**
```json
{
  "a1a1": {
    "name": "childJob",
    "canvasName": "childJob",
    "summary": "Run Child Per Device",
    "variables": {
      "incoming": {
        "task": "",
        "workflow": "My Child Workflow",
        "variables": {},
        "data_array": "$var.job.devices",
        "transformation": "",
        "loopType": "parallel"
      },
      "outgoing": {"job_details": null}
    },
    "actor": "job"
  }
}
```

**Input:** `devices` is an array of objects. Each object becomes one child's variables:
```json
{
  "devices": [
    {"deviceName": "IOS-CAT8KV-1", "action": "backup"},
    {"deviceName": "IOS-CAT8KV-2", "action": "check"},
    {"deviceName": "EOS-AWS-1", "action": "backup"}
  ]
}
```

**Extracting loop output:** Query `"loop"` to get the results array:
```json
{
  "b2b2": {
    "name": "query",
    "variables": {
      "incoming": {
        "pass_on_null": false,
        "query": "loop",
        "obj": "$var.a1a1.job_details"
      },
      "outgoing": {"return_data": "$var.job.childResults"}
    }
  }
}
```
If the query returns null (platform-version-specific `$var` resolution issue), use the same merge+taskRef workaround described above (Mode A) — capture `job_details` via `{"task": "a1a1", "variable": "job_details"}` in merge, then query `$var.m1m1.merged_object`.

**Loop element completeness — required fields must be in each element (not in `variables`).**

The platform validates the child workflow's `inputSchema.required` against **each element's keys only**. Static `variables` set on the childJob task are NOT counted toward satisfying required fields. If your loop elements only contain per-iteration fields (e.g., `subnet_name`, `subnet_cidr`) but the child also requires shared fields (e.g., `subscription_id`, `region`), the validation fails before any iteration runs.

**Fix — forEach enrichment pattern:** enrich each element with the shared fields before the childJob loop, then set `variables: {}` on the childJob:

```
forEach (loop over elements) → merge (add shared fields to current_item) → arrayPush (append enriched element to new array)
                                                                                    ↓ (after forEach success)
childJob (data_array: enrichedArray, variables: {})
```

```json
// forEach outgoing binds current_item to job var
{"outgoing": {"current_item": "$var.job.currentElement"}}

// merge combines current element + shared fields
{"data_to_merge": [
  {"task": "forEachId", "variable": "current_item"},
  {"key": "subscription_id", "value": {"task": "job", "variable": "subscription_id"}},
  {"key": "region", "value": {"task": "job", "variable": "region"}}
]}
// → $var.mergeId.merged_object is the enriched element

// arrayPush appends to accumulator
{"incoming": {"job_variable": "enrichedElements", "item_to_push": "$var.mergeId.merged_object"}}

// childJob uses the enriched array and no static variables
{"data_array": "$var.job.enrichedElements", "variables": {}, "loopType": "parallel"}
```

**Loop output shape** (each element is a flat spread of the child's job variables):
```json
[
  {"status": "complete", "childJobLoopIndex": 0, "deviceName": "IOS-CAT8KV-1", "action": "backup", "taskStatus": "success"},
  {"status": "complete", "childJobLoopIndex": 1, "deviceName": "IOS-CAT8KV-2", "action": "check", "taskStatus": "success"},
  {"status": "complete", "childJobLoopIndex": 2, "deviceName": "EOS-AWS-1", "action": "backup", "taskStatus": "success"}
]
```

Use `"[**].taskStatus"` in a query to extract one field from all iterations.

#### childJob checklist
- [ ] `actor` is `"job"` (NOT `"Pronghorn"`)
- [ ] `task` is `""` (empty string)
- [ ] `job_details` outgoing is `null`
- [ ] All incoming fields present — even unused ones: `"data_array": ""`, `"transformation": ""`, `"loopType": ""`
- [ ] Variables use `{"task","value"}` NOT `$var` (single mode)
- [ ] `variables` is `{}` when using `data_array` (loop mode)
- [ ] Child workflow's `inputSchema.required` matches what you're passing
- [ ] `loopType`: `""` (single), `"parallel"` (simultaneous), `"sequential"` (one at a time)
- [ ] If a downstream `query` of a childJob returns null: the `"obj": "$var.<childJobId>.job_details"` form may not resolve on this platform version — use merge+taskRef workaround (see "Extracting single child output" above)

#### Building the child workflow

The child workflow must:
1. Accept inputs via `inputSchema` that match what the parent passes
2. Set output variables via `newVariable` or task outgoing → `$var.job.x`
3. Handle errors internally (try-catch pattern) so it always completes:
```
task --success--> newVariable("taskStatus" = "success") -> workflow_end
task --error--> newVariable("taskStatus" = "error") -> workflow_end
```
The parent can then check `taskStatus` from `job_details` to decide what to do.

---

## Projects

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/automation-studio/projects/import` | **Import a project (preferred — atomic)** |
| POST | `/automation-studio/projects` | Create an empty project |
| GET | `/automation-studio/projects/{projectId}` | Get a project |
| PATCH | `/automation-studio/projects/{projectId}` | Update a project |
| DELETE | `/automation-studio/projects/{id}` | Delete a project |
| GET | `/automation-studio/projects/{id}/export` | Export project as JSON |
| POST | `/automation-studio/projects/{projectId}/components/add` | Add components (legacy) |
| DELETE | `/automation-studio/projects/{projectId}/components/{componentId}` | Remove component |

### Preferred: Import a project (atomic — all assets in one call)

**Always use import instead of create + add components.** Import creates the project with all workflows, templates, and MOP templates inside it in a single atomic call. No intermediate state, no broken childJob refs, no project-locking issues.

```
POST /automation-studio/projects/import
```

**Build all assets locally first, then import everything at once:**

```json
{
  "project": {
    "_id": "24-char-hex-mongodb-objectid",
    "iid": 1,
    "name": "My Project",
    "description": "...",
    "thumbnail": "",
    "backgroundColor": "#FFFFFF",
    "components": [
      {
        "iid": 1,
        "type": "workflow",
        "reference": "uuid-of-workflow",
        "folder": "/",
        "document": { "...full workflow object..." }
      },
      {
        "iid": 2,
        "type": "mopCommandTemplate",
        "reference": "@projectId: Template Name",
        "folder": "/",
        "document": { "...full MOP object..." }
      }
    ],
    "created": "2026-03-13T00:00:00.000Z",
    "createdBy": {"_id": "000000000000000000000000", "provenance": "CloudAAA", "username": "admin@itential"},
    "lastUpdated": "2026-03-13T00:00:00.000Z",
    "lastUpdatedBy": {"_id": "000000000000000000000000", "provenance": "CloudAAA", "username": "admin@itential"}
  }
}
```

**Import format rules (different from create/export):**

| Field | Import format | Notes |
|-------|--------------|-------|
| `encodingVersion` | **OMIT** from workflow documents | Causes silent component failure if included |
| `created_by` (workflow) | `{username, provenance, firstname, inactive, sso}` — NO `_id` | Different from project-level `createdBy` |
| `createdBy` (project) | `{_id, username, provenance}` — HAS `_id` | Different from workflow-level |
| `_id` (project) | Pre-compute 24-char hex string | So childJob refs can use `@{projectId}:` |
| Workflow `name` | Clean names — no prefix | Import adds `@projectId:` automatically |
| childJob `workflow` | Must include `@{projectId}:` prefix | Pre-wire using the same `_id` |
| `reference` (workflow) | UUID string | Becomes the workflow's `uuid` |
| `reference` (MOP) | `@{projectId}: Template Name` | String reference |
| `iid` (components) | Sequential integers starting at 1 | Incrementing ID |

Response:
```json
{
  "message": "Successfully imported project",
  "data": {"_id": "...", "name": "...", "components": [...]},
  "metadata": {"failedComponents": []}
}
```
**Check `metadata.failedComponents`** — empty array means success.

### Why import instead of create + move

| Problem | Create + move | Import |
|---------|--------------|--------|
| childJob refs | Break on move — manual fix needed | Pre-wired with `@projectId:` — just work |
| Project locking | Race conditions during move | Single atomic call |
| Intermediate state | Workflows exist outside project | Never |
| API calls | Create + create each asset + move + fix refs | One POST |
| Reproducibility | Hard to replay | `project-import.json` is the artifact |

### Legacy: Create + add components (avoid if possible)

Only use this for adding a single asset to an existing project after initial import.

```
POST /automation-studio/projects/{projectId}/components/add
```
```json
{
  "components": [
    {"type": "workflow", "reference": "uuid-...", "folder": "/"}
  ],
  "mode": "move"
}
```

**Warning:** Both `move` and `copy` rename assets with `@projectId:` prefix but do NOT update internal references (childJob `workflow` fields, template names). You must fix these manually.

**Component types:** `workflow`, `template`, `transformation`, `jsonForm`, `mopCommandTemplate`, `mopAnalyticTemplate`

### Update membership (full replacement)

**Before patching, always ask the engineer:** *"Who else should have access to this project? (usernames or group names)"*

Do not auto-discover or assume groups. Wait for the answer, resolve each name to a reference ID by scanning existing projects, then PATCH.

```
PATCH /automation-studio/projects/{projectId}
```

Use the helper: `${CLAUDE_PLUGIN_ROOT}/helpers/update/update-project-members.json`

Include ALL members in every PATCH — this is a full replacement. Omitting an existing member removes them.

**To resolve a username or group name to a reference ID**, scan existing projects:
```bash
for pid in $(curl -s "$BASE/automation-studio/projects?limit=100" \
  -H "Authorization: Bearer $TOKEN" | jq -r '.data[]._id'); do
  curl -s "$BASE/automation-studio/projects/$pid" \
    -H "Authorization: Bearer $TOKEN" \
    | jq -r '.data.members[]? | [.type, .reference, (.username // .name)] | @tsv'
done | sort -u
```
If a name cannot be resolved, ask the engineer for the reference ID — do not guess.

### Resolve membership references from spec

> **_MANDATORY:_** Import sets the OAuth service account as project owner — not the UI user from the spec. The engineer specified in the spec's Project Membership table will be locked out of the project unless you PATCH membership immediately after import. This runs in **Phase 3 (Import)**, not Phase 6 (Deliver).

There is no user/group lookup API on the Itential platform. The only way to resolve a username (e.g., `joksan.flores@itential.com`) or group name (e.g., `solutions-engineers`) to a platform reference ID is by scanning existing projects' members.

**Step 1: Build a membership lookup table.**

The list endpoint (`GET /automation-studio/projects?limit=50`) does NOT include `username`/`name` on member objects — only individual `GET /automation-studio/projects/{id}` calls do. Scan all projects to build the lookup:

```bash
# Get all project IDs
PROJECT_IDS=$(curl -s -H "Authorization: Bearer $TOKEN" \
  "$PLATFORM_URL/automation-studio/projects?limit=100" \
  | jq -r '.data[]._id')

# Build lookup table from individual GETs
> {use-case}/membership-lookup.txt
for pid in $PROJECT_IDS; do
  curl -s -H "Authorization: Bearer $TOKEN" \
    "$PLATFORM_URL/automation-studio/projects/$pid" \
    | jq -r '.data.members[]? | [.type, .reference, (.username // .name), .provenance] | @tsv'
done | sort -u >> {use-case}/membership-lookup.txt
```

Output format (TSV): `type  reference  username/name  provenance`

**Step 2: Match spec members to references.**

For each member in the spec's Project Membership table, find their `reference` ID in `membership-lookup.txt`:
```bash
grep "joksan.flores@itential.com" {use-case}/membership-lookup.txt
# → account  699a67bb...  joksan.flores@itential.com  CloudAAA
```

**Step 3: PATCH membership immediately after import.**

```
PATCH /automation-studio/projects/{projectId}
```
```json
{
  "members": [
    {"type": "account", "role": "owner", "reference": "699a67bb..."},
    {"type": "group", "role": "editor", "reference": "67c859..."}
  ]
}
```

> **If a username or group cannot be resolved from the lookup table, stop and ask the engineer.** Do not guess reference IDs or skip members.

**Baseline members (when no spec membership is defined):** If there is no Project Membership table in the spec, or when doing a freeform build/import outside the spec lifecycle, **ask the engineer:** *"Which user accounts or groups should have access to this project?"* — do not assume or skip. Once you have the names, resolve them via the lookup table above and PATCH immediately. Without this step the engineer will be locked out of the project in the IAP UI. See [#63](https://github.com/itential/builder-skills/issues/63)

### Project Thumbnail

| Operation | Endpoint |
|-----------|----------|
| Set | `PUT /automation-studio/projects/{id}/thumbnail` — body: `{"imageData": "<data-URI>", "backgroundColor": "<hex>"}` |
| Get | `GET /automation-studio/projects/{id}/thumbnail` — returns `{"data": {"image": "<data-URI>", "backgroundColor": "<hex>"}}` |

**`imageData` must be a full data URI — not raw base64.** Passing raw base64 without the `data:image/png;base64,` prefix returns HTTP 200 and stores the value, but the UI renders a black/blank image with no error.

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...
```

Build the data URI in Python:
```python
import base64, io
buf = io.BytesIO()
img.save(buf, format='PNG')
data_uri = f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"
```

- **Optimal dimensions: 330 × 100 px** — matches the project card aspect ratio in Automation Studio
- Accepted formats: `jpg`, `jpeg`, `png` — max 1000 KB
- `backgroundColor` (hex, e.g. `"#1B2A4A"`) sets the card background color visible before the image loads

---

## JSON Forms

JSON Forms have their own dedicated skill — `itential-json-forms`. See that skill for the form structure (`struct` / `schema` / `uiSchema` / `bindingSchema`), the static-enum vs. REST-bound vs. cascading dropdown (aka field dependency) patterns, the full API reference (including the bulk-only DELETE), and the manual-trigger wiring (`legacyWrapper: false`).

Helper templates for forms still live under `${CLAUDE_PLUGIN_ROOT}/helpers/`:
- `create-json-form.json` — static-enum dropdowns
- `create-json-form-rest-bound.json` — REST-bound or cascading dropdowns

---

## Operations Manager (Automations & Triggers)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/operations-manager/automations` | Create an automation |
| GET | `/operations-manager/automations` | List automations |
| POST | `/operations-manager/triggers` | Create a trigger |
| PATCH | `/operations-manager/triggers/{id}` | Update a trigger |
| GET | `/operations-manager/triggers` | List triggers |

### Create a Manual Trigger with JSON Form

This is a two-step process: create the automation, then create a manual trigger that binds to it.

Use the helper template: `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-ops-manager-automation.json`

**Critical: `legacyWrapper` must be `false`.** When creating a manual trigger with a JSON form, set `legacyWrapper: false`. The default is `true`, which wraps form field values under `formData`, breaking the mapping to workflow job variables. With `legacyWrapper: false`, form field values map directly to workflow input variables by name.

**Required trigger fields:** `name`, `type` (`"manual"`), `enabled`, `actionType` (`"automations"`), `actionId`, `formId`, `legacyWrapper`

---

## Task Discovery

### Pull Task Catalog

**`{use-case}/tasks.json` should already exist** — pulled by `/solution-arch-agent` or `/explore` during feasibility. Do not re-pull if the file exists. If missing, fetch it:

```
GET /workflow_builder/tasks/list → save to {use-case}/tasks.json
GET /automation-studio/apps/list → save to {use-case}/apps.json
```

Search locally:
```bash
grep -i "template" {use-case}/tasks.json
jq '.[] | select(.app == "ConfigurationManager") | .name' {use-case}/tasks.json
```

### Look up task wiring in asset projects first

Before fetching schemas from the API, check if an asset project already has the task wired up. If it does, you get the exact field structure for free — no API call needed.

```bash
# Does any asset project use this task? Find it by task name:
grep -rl '"name": "TASK_NAME"' ${CLAUDE_PLUGIN_ROOT}/helpers/assets/

# Extract the wired task from the matching project:
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "TASK_NAME")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/MATCHING_FILE.json

# See which tasks a specific workflow uses:
jq '[.components[] | select(.type=="workflow") | select(.document.name | test("WORKFLOW"; "i"))] | first | .document.tasks | to_entries[] | {id:.key, name:.value.name, app:.value.app}' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/MATCHING_FILE.json
```

Asset project → best match by task type:
| Task | Best asset to check |
|------|-------------------|
| ServiceNow adapter tasks | `vendor-servicenow.json` |
| Infoblox / DNS / IPAM tasks | `vendor-infoblox-nios-ddi.json` |
| NetBox tasks | `vendor-netbox.json` |
| itential_cli, RunCommandTemplate, MOP tasks | `itential-platform-configuration-management.json`, `vendor-cisco-ios.json` |
| transformation (JST) | `vendor-netbox.json`, `itential-platform-data-manipulation.json` |
| childJob, evaluation, query, newVariable | any vendor project |
| LCM action workflow tasks | `helpers/assets/lcm/lcm-vxlan-fabric-services-project.json` |

### Get Full Task Schemas (only if not found in assets)

**Single task:**
```
GET /automation-studio/locations/{location}/packages/{pckg}/tasks/{method}?dereferenceSchemas=true
```

**Multiple tasks:**
```
POST /automation-studio/multipleTaskDetails?dereferenceSchemas=true
```
```json
{
  "inputsArray": [
    {"location": "Application", "pckg": "WorkFlowEngine", "method": "query"},
    {"location": "Adapter", "pckg": "Servicenow", "method": "createChangeRequest"}
  ]
}
```

**Mapping from tasks.json → schema endpoint:**

| tasks.json field | Maps to |
|------------------|---------|
| `location` (`Application`/`Adapter`) | `{location}` |
| `app` (e.g., `TemplateBuilder`) | `{pckg}` |
| `name` (e.g., `renderJinjaTemplate`) | `{method}` |

**IMPORTANT:** The `pckg` value must come from `apps.json`, NOT `tasks.json`. The names can differ (e.g., tasks.json says `ServiceNow` but apps.json says `Servicenow`).

**Before fetching schemas:**
1. Search asset projects (above) — if found, use the wired example directly
2. Check if `{use-case}/task-schemas.json` exists — search it next
3. Only call `multipleTaskDetails` for tasks not found in either place
4. After fetching, append to `{use-case}/task-schemas.json`

### nodeLocation Spacing Convention

Workflows are laid out **top-to-bottom (vertical)** by default — this is the Itential best practice for readability and consistency, and matches the conventions used in the platform's working examples. Use horizontal only when the engineer explicitly asks for it.

#### Vertical Layout (default)

| Rule | Value |
|------|-------|
| Sequential tasks (y-delta) | +108px |
| Fork branch offset from spine (x-delta) | ±264px |
| Spine x | a constant column (e.g. `x=600`) |

**Clean canvas principles:**
- The **spine is a constant `x`** — non-forked sequences (start, single-thread tasks, end, convergence points) sit on it.
- **Forks split off the spine** — at a fork point, both outgoing branches leave the spine column. Place one at `spine - 264` and the other at `spine + 264`. The spine column stays empty between the fork and the convergence point so transition lines don't cross task nodes. Direction (which branch goes left vs. right) is the engineer's call — pick whatever keeps the picture clean.
- **Branches stay in their own column** until they converge.
- **Convergence tasks** (workflow_end, merges, error sinks) return to the spine `x`.
- **Tight y-spacing** — the canvas grid is dense; ~108px between sequential rows reads well. Don't pad to +250 or +360.
- **Preserve Studio-arranged positions** — if an engineer has arranged a workflow in Automation Studio, treat its `nodeLocation` values as authoritative. Always read from the live export before reimporting. Never recalculate positions from scratch on a workflow that has already been arranged.

Example — fork with a shared error handler (same pattern as ServiceNow "Create Change Request" in `helpers/assets/vendor-servicenow.json`):
```
workflow_start                        (x=600, y=200)
e1a1 merge                            (x=600, y=312)
a1b2 createCR  ── fork point ──       (x=600, y=420)
b2c3 query   [success branch]         (x=336, y=540)
c3d4 updateCR [success branch]        (x=336, y=636)   ef01 newVar [shared error handler]  (x=864, y=636)
workflow_end                          (x=600, y=804)
```

For a childJob phase with query + evaluation (single-thread, no fork → all on spine):
```
y=312  — childJob     (x=600)
y=420  — query        (x=600)   ← extracts taskStatus from job_details
y=528  — evaluation   (x=600)
```

#### Horizontal Layout (only when requested)

If the engineer explicitly asks for horizontal, swap x and y throughout: phases advance on x, fork branches offset on y, spine becomes a constant y row. Same magnitudes, opposite axes.

---

## Workflows

### Workflow Structure

```
POST /automation-studio/automations
```

Body wraps the workflow in `{"automation": {...}}`:

```json
{
  "automation": {
    "name": "My Workflow",
    "description": "Does something useful",
    "type": "automation",
    "canvasVersion": 3,
    "encodingVersion": 1,
    "font_size": 12,
    "tasks": {
      "workflow_start": {
        "name": "workflow_start",
        "groups": [],
        "nodeLocation": {"x": 600, "y": 200}
      },
      "a1b2": {
        "name": "query",
        "canvasName": "query",
        "summary": "Extract Data",
        "description": "Extracts field from response",
        "location": "Application",
        "locationType": null,
        "app": "WorkFlowEngine",
        "type": "operation",
        "displayName": "WorkFlowEngine",
        "variables": {
          "incoming": {
            "pass_on_null": false,
            "query": "hostname",
            "obj": "$var.job.deviceData"
          },
          "outgoing": {
            "return_data": "$var.job.deviceName"
          },
          "error": "",
          "decorators": []
        },
        "groups": [],
        "actor": "Pronghorn",
        "scheduled": false,
        "nodeLocation": {"x": 600, "y": 312}
      },
      "workflow_end": {
        "name": "workflow_end",
        "groups": [],
        "nodeLocation": {"x": 600, "y": 420}
      }
    },
    "transitions": {
      "workflow_start": {
        "a1b2": {"type": "standard", "state": "success"}
      },
      "a1b2": {
        "workflow_end": {"type": "standard", "state": "success"}
      },
      "workflow_end": {}
    },
    "groups": [],
    "inputSchema": {
      "type": "object",
      "properties": {
        "deviceData": {"title": "deviceData", "type": "object"}
      },
      "required": ["deviceData"]
    },
    "outputSchema": {
      "type": "object",
      "properties": {
        "deviceName": {"title": "deviceName", "type": "string"}
      }
    }
  }
}
```

**Update a workflow:**
```
PUT /automation-studio/automations/{id}
```
```json
{"update": { ...same structure as automation object... }}
```

**Project-scoped name required on PUT.** If the workflow belongs to a project, the `name` field in the `update` body must include the `@<projectId>: ` prefix — even if the workflow was created without it:
```json
{"update": {"name": "@69f10abc: My Workflow", "tasks": {...}, "transitions": {...}}}
```
Sending the bare name (`"name": "My Workflow"`) returns `{"error": {"message": "Name must begin with '@projectId: '"}}`.

Asymmetry: workflow **CREATE** (`POST /automation-studio/automations`) does NOT require the prefix — the platform applies it when the workflow is added to a project. But **PUT-update** always requires it for project-member workflows.

Always read the workflow before updating (`GET /automation-studio/workflows/detailed/{name}` or export the project) to get the current scoped name. See [Rule 24](#) and [issue #55](https://github.com/itential/builder-skills/issues/55).

### Task Fields

| Field | Application Tasks | Adapter Tasks |
|-------|-------------------|---------------|
| `name` | Method name from tasks.json | Method name from tasks.json |
| `canvasName` | From tasks.json `canvasName` field (may differ from `name`: `arrayPush`→`push`) | Same |
| `location` | `"Application"` | `"Adapter"` |
| `locationType` | `null` | Same as `app` |
| `app` | App name (e.g., `WorkFlowEngine`) | From `apps.json` (NOT tasks.json) |
| `type` | `"automatic"` or `"operation"` — read from tasks.json `.type`, do not guess |
| `actor` | `"Pronghorn"` | `"Pronghorn"` |
| `displayName` | App name | May differ from `app` |

**Adapter tasks also require `adapter_id`** in incoming variables — the adapter instance name from `health/adapters`.

### Task Access Control (`groups`)

The `groups` field on a task definition is **task-level GBAC** — group-based access control that restricts which IAP groups can see, claim, and complete a manual task in the Job Inbox.

| Field | Type | Meaning |
|---|---|---|
| `groups` *(plural)* | `string[]` | GBAC. Each entry is a group's MongoDB `_id` (24-char hex). Empty `[]` means no task-level restriction. |
| `group` *(singular, optional)* | `string` | Canvas display category (e.g., `"Tools"`, `"JsonForms"`). Set by the Studio canvas. **NOT access control** — easy to confuse with `groups`. |

```json
{
  "name": "ViewData",
  "type": "manual",
  "app": "WorkFlowEngine",
  "view": "/workflow_engine/task/ViewData",
  ...
  "groups": ["69e65b4189b39131a9b8cce1"]
}
```

**Look up group IDs:**
- `GET /authorization/groups` — list groups (each has `_id` and `name`)
- `GET /authorization/groups/<id>` — resolve a single group

**Two GBAC scopes** — both use the same `string[]` shape (group `_id`s) but apply at different levels:
- **Per-task `groups`** (on the task definition, sibling of `name`/`app`/`type`) — gates access to a single manual task.
- **Top-level workflow `groups`** (sibling of `tasks`/`transitions` at the workflow level) — gates access to the workflow as a whole.

**Tasks of any type can carry `groups`**, but only `type: "manual"` tasks surface in the Job Inbox where GBAC actually gates user access. Leave it as `[]` on automatic tasks unless platform-specific docs say otherwise.

> **Edge cases not yet documented** — verify on your platform before relying on:
> - Semantics with **multiple group IDs** in the array (likely OR — any-of — but unverified)
> - Interaction between **task-level and workflow-level** `groups` (additive vs. override)
> - Whether `groups` accepts a **`$var` job-variable** for dynamic group resolution (almost certainly no — design-time only — but worth confirming)

### Task IDs

Task IDs must be **hex-only**: `[0-9a-f]{1,4}`. Non-hex IDs (e.g., `apush`) cause `$var` references to silently fail.

### Transitions

```json
"transitions": {
  "workflow_start": {
    "a1b2": {"type": "standard", "state": "success"}
  },
  "a1b2": {
    "c3d4": {"type": "standard", "state": "success"},
    "err1": {"type": "standard", "state": "error"}
  },
  "c3d4": {
    "workflow_end": {"type": "standard", "state": "success"}
  },
  "err1": {
    "workflow_end": {"type": "standard", "state": "success"}
  },
  "workflow_end": {}
}
```

**Transition states:**
- `success` — task completed without error (all tasks)
- `error` — task encountered errors (all tasks)
- `failure` — evaluation didn't match or query returned undefined (evaluation/query only)
- `loop` — forEach loop iteration (forEach only)

**Transition types:**
- `standard` — moves forward
- `revert` — moves backward to a previous task (retry loops)

**MANDATORY: Every adapter/external task needs an error transition.** Without one, errors cause "Job has no available transitions" and the job gets stuck forever.

**JSON duplicate key problem:** If both success and error need to go to `workflow_end`, you can't use `workflow_end` as a key twice. Route error to an intermediate task (e.g., `newVariable` to set error status), then route that to `workflow_end`.

### Create Response Shape

Both workflow and template creation return `{created, edit}` — NOT `{message, data, metadata}`:
```json
{
  "created": {"_id": "...", "name": "..."},
  "edit": "/automation-studio/#/edit?..."
}
```

---

## $var Resolution Rules

`$var` only resolves as **direct top-level incoming variable values:**

| Wiring | Works? | Why |
|--------|--------|-----|
| `"deviceName": "$var.job.x"` | Yes | Direct top-level value |
| `"variables": {"key": "$var.job.x"}` | **NO** | Nested inside object |
| `"body": {"data": "$var.job.x"}` | **NO** | Nested — stored as literal string |

**Workaround:** Use `merge`, `makeData`, or `query` to build the nested object, then reference the task's output with `$var.taskId.merged_object`.

**Task ID validation:** `$var.taskId.x` only resolves when `taskId` matches `[0-9a-f]{1,4}`. Non-hex IDs silently fail.

**Prefer task-to-task wiring:** When a task's output feeds directly into the next task's input, wire it as `$var.<taskId>.<outVar>` instead of bouncing through `$var.job.x`. Only use job variables when: (a) values cross non-adjacent tasks, (b) values need to be visible in job output, or (c) multiple downstream tasks need the same value. Direct task-to-task wiring reduces clutter and makes data flow easier to trace.

**`incomingRefs` cache — what PUT does and doesn't fix:**

| Scenario | Result | Fix |
|----------|--------|-----|
| New tasks added via PUT | incomingRefs **generated** — task-to-task `$var` refs resolve immediately | None needed |
| Existing task field values changed via PUT | incomingRefs **NOT regenerated** — literals/changed taskRefs resolve to `null` | Open in Studio → Save |
| `POST /workflow_builder/workflows/save` | Does NOT regenerate incomingRefs either | Open in Studio → Save |
| Evaluation silently returns `false` after PUT | Stale operand cache | Constant-holder workaround below, or Studio save |
| Workflow hangs at `workflow_start` (status: running forever) after PUT | Any task's incomingRefs stale | Recreate via fresh POST — more PUTs won't fix it |

**Constant-holder workaround (API-only, no Studio save needed):** store `operand_2` literal values in a `newVariable` task and reference via `{"task": "k_const", "variable": "value"}` — taskRef resolution bypasses the cache.

**`makeData` static `input` strings do NOT resolve after API create/PUT.** The `input` and `outputType` fields are backed by `job_data` (type `static`). Workaround: use `newVariable` with `value: [...]` (array literal) — `newVariable.value` resolves correctly after API create without a Studio save.

**`task: "static"` values broadly** are backed by `job_data` written at Studio-save time. Any static value (template strings, query paths, model IDs, inline constants in childJob `variables` dicts) resolves as `null` at runtime on a freshly API-imported workflow until saved through Automation Studio.

**Outgoing must write to job var for cross-task `$var` to be readable by downstream tasks.** Pattern: `"outgoing": {"result": "$var.job.raw_result"}` then downstream: `"obj": "$var.job.raw_result"`. If outgoing is `null`, the value is accessible via task iteration (`GET /operations-manager/tasks/{iterationId}`) but NOT via `$var.taskId.result` in downstream tasks at runtime. Use job vars for any result you need to pass forward.

**`POST /automation-studio/workflows/validate`** — runs pre-flight schema validation before create or update. Returns `{errors: [], warnings: []}`. An empty `errors` array means the workflow is schema-valid. Run this on every workflow before POSTing or PUTting.

---

## Utility Tasks (WorkFlowEngine)

These are built-in tasks that require no adapter. They handle data manipulation and control flow.

### query

Extract nested values from objects using dot-path syntax.

**Incoming:** `pass_on_null` (boolean), `query` (string — dot-path), `obj` (object — usually `$var` ref)
**Outgoing:** `return_data` (any)
**Transitions:** `success` (found), `failure` (null/undefined when `pass_on_null: false`)

```json
{
  "incoming": {
    "pass_on_null": false,
    "query": "response.id",
    "obj": "$var.a1b2.result"
  },
  "outgoing": {
    "return_data": "$var.job.changeId"
  }
}
```

**IMPORTANT: Don't guess the query path for adapter responses.** Adapters transform upstream API responses — the field path in the adapter's output is NOT the same as the native API's response structure. The adapter's `result` outgoing is always a `{response, headers, metrics}` object, never a primitive. When the upstream API returns a simple string (like Infoblox's `_ref`), it's at `result.response`, not `result` directly. Always verify the actual response shape from a test job (`GET /operations-manager/jobs/{jobId}` → `data.tasks`) before wiring a path.

### merge

Build an object from multiple resolved values. Primary workaround for `$var` not resolving inside nested objects.

**Incoming:** `data_to_merge` (array, min 2 items)
**Outgoing:** `merged_object` (object)

**IMPORTANT: The field is `"variable"` NOT `"value"`** in the reference objects inside `data_to_merge`.

**Reference format in `data_to_merge`:**
- `{"task": "job", "variable": "varName"}` — pull from a **user-supplied** job variable (input to the workflow)
- `{"task": "static", "variable": "literalValue"}` — literal value
- `{"task": "taskId", "variable": "outVar"}` — pull from a previous task's output

> **WARNING — `{task:"job"}` references add fields to `inputSchema.required`.**
> The platform scans every `data_to_merge` entry in merge tasks (and every `variables` entry in childJob) for `{task:"job"}` references and automatically adds that variable name to `inputSchema.required`. This means using `{task:"job", variable:"changeId"}` for a variable that was produced internally by a query task will prompt operators to supply `changeId` as a workflow input — even though it should never come from the user.
>
> **Rule:** only use `{task:"job"}` for variables that are genuine workflow inputs. For anything produced by an earlier task, use the producing task's ref directly:
>
> | Value source | Correct ref form |
> |---|---|
> | User workflow input | `{"task": "job", "variable": "x"}` |
> | `query` output | `{"task": "queryTaskId", "variable": "return_data"}` |
> | `merge` output | `{"task": "mergeTaskId", "variable": "merged_object"}` |
> | `newVariable` output | `{"task": "newVarTaskId", "variable": "value"}` |
> | `makeData` output | `{"task": "makeDataTaskId", "variable": "output"}` |
> | `parse` output | `{"task": "parseTaskId", "variable": "return_data"}` |
> | adapter task output | `{"task": "adapterTaskId", "variable": "result"}` |

```json
{
  "incoming": {
    "data_to_merge": [
      {"key": "hostname", "value": {"task": "static", "variable": "IOS-CAT8KV-1"}},
      {"key": "details", "value": {"task": "job", "variable": "deviceInfo"}},
      {"key": "config", "value": {"task": "a1b2", "variable": "renderedTemplate"}}
    ]
  },
  "outgoing": {
    "merged_object": "$var.job.requestBody"
  }
}
```

**Gotchas:** Requires at least 2 items (1 item = silently null). Outgoing MUST declare `"merged_object": null` (empty `{}` makes it unreachable). **Duplicate keys produce arrays** — merging `{"ip": "1.2.3.4"}` and `{"ip": "1.2.3.4"}` yields `{"ip": ["1.2.3.4", "1.2.3.4"]}`, not an overwrite. To avoid this, pass a pre-built object as a single workflow input variable instead of merging multiple objects with the same keys.

### parse

Convert a JSON string into a JavaScript object. Essential after extracting `result.stdout` from `runService` (which is always a string, even when the script printed valid JSON).

**Incoming:** `stringToParse` (string — the JSON string to parse)
**Outgoing:** `result` (object — the parsed object)

```json
{
  "name": "parse",
  "canvasName": "parse",
  "summary": "Parse JSON String",
  "location": "Application",
  "locationType": null,
  "app": "WorkFlowEngine",
  "type": "operation",
  "displayName": "WorkFlowEngine",
  "variables": {
    "incoming": {
      "stringToParse": "$var.a1b2.return_data"
    },
    "outgoing": {
      "result": "$var.job.parsedOutput"
    }
  },
  "actor": "Pronghorn"
}
```

**Common pattern — runService → query → parse:**
```
runService → query(result.stdout) → parse(stringToParse) → use parsed fields
```

After `parse`, fields are accessible: `$var.parseTask.result.hostname`, `$var.parseTask.result.status`, etc.

### evaluation

Conditional branching. **MUST have BOTH success AND failure transitions.**

**Incoming:** `all_true_flag` (boolean), `evaluation_groups` (array)
**Outgoing:** `return_value` (boolean)
**Transitions:** `success` (true), `failure` (false)

**Operator enum — closed set. Only these 8 are valid:**
```
contains, !contains, <, <=, >, >=, ==, !=
```
`regex`, `match`, `matches`, `contains_key`, `in`, `startsWith` — **do not exist**. An invalid operator silently returns `false` with empty outgoing and `finish_state: failure`. No error message. Always validate against this list before wiring. Source of truth: `openapi.json` at `components/schemas/workflow_engine_wfEngineCommon_evaluationItem/properties/operator/enum`.

**`contains` is regex-based, not substring.** `operand_2` is interpreted as a regex pattern. A literal like `9.2(4)` is parsed as regex — `.` matches any char, `(4)` becomes a capture group — and may match unintended strings or fail to match the intended one. Escape regex metacharacters in literal patterns: `9\.2\(4\)` not `9.2(4)`.

**`contains` also works for object-key presence** — it is the universal "does X contain Y" operator. On a string operand it does regex matching; on an object operand it tests key presence. There is no separate `contains_key` operator.

**Direct evaluation test (no workflow needed):**
```
POST /workflow_engine/runEvaluationGroups
{"evaluation_groups":[{"operator":"AND","evaluations":[{"operand_1":"<test input>","operator":"contains","operand_2":"<pattern>"}]}]}
```
Returns `true`/`false`. Invalid operators silently return `false`. Use this to validate operators and escape patterns before wiring them into a workflow.

**`incomingRefs` cache — API PUT does not regenerate it for existing task changes.** See the incomingRefs table in [$var Resolution Rules](#var-resolution-rules). Diagnostic sign: `GET /operations-manager/tasks/{iterationUUID}` shows `incomingRefs[n].taskId: null` or `taskPointer: "/variables/outgoing/undefined"`.

**Operand reference format (uses `"variable"`, same as merge):**
- `{"task": "job", "variable": "varName"}`
- `{"task": "static", "variable": "literalValue"}`

```json
{
  "incoming": {
    "all_true_flag": true,
    "evaluation_groups": [{
      "all_true_flag": true,
      "evaluations": [{
        "operand_1": {"variable": "status", "task": "job"},
        "operator": "==",
        "operand_2": {"variable": "success", "task": "static"}
      }]
    }]
  },
  "outgoing": {"return_value": null}
}
```

### childJob

Run another workflow as a sub-job. **Read a live childJob example first:**
```bash
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "childJob")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json
```

**Critical differences from normal tasks:**
- **`actor` MUST be `"job"`** — not `"Pronghorn"`
- **`task` MUST be `""`** (empty string)
- **`outgoing.job_details` MUST be `null`** — do NOT override with `$var.job.X`
- **All incoming fields required** — even unused ones: `"data_array": ""`, `"transformation": ""`, `"loopType": ""`

**Variables use `{"task", "value"}` syntax — NOT `$var`:**
```json
{
  "incoming": {
    "task": "",
    "workflow": "My Child Workflow",
    "variables": {
      "deviceName": {"task": "job", "value": "deviceName"},
      "configData": {"task": "a1b2", "value": "return_data"}
    },
    "data_array": "",
    "transformation": "",
    "loopType": ""
  },
  "outgoing": {"job_details": null}
}
```

**childJob uses `"value"`. merge/evaluation use `"variable"`. Do NOT mix them.**

**Variable passing:**
- `{"task": "static", "value": [...]}` — literal value
- `{"task": "job", "value": "varName"}` — parent job variable (must exist at start)
- `{"task": "taskId", "value": "outVar"}` — previous task's output (preferred for runtime data)

**Loop modes:** `loopType: ""` (single), `"parallel"` (multiple simultaneous), `"sequential"` (one at a time). With loops, use `data_array` (each element becomes a child job's variables) and set `variables: {}`.

**Querying childJob output:**
```json
{
  "name": "query",
  "variables": {
    "incoming": {
      "query": "taskStatus",
      "obj": "$var.f48f.job_details",
      "pass_on_null": false
    }
  }
}
```
Use flat variable names, NOT nested paths. For loop output: `"[**].fieldName"`.

### forEach

Iterate over an array. **Deprecated** — prefer `childJob` with `loopType`. Still common in existing workflows.

**Incoming:** `data_array` (array) — **ONLY `data_array`**. Do NOT include `job_id` in incoming — it triggers errors.
**Outgoing:** `current_item` (any)

**Transition pattern (critical):**
```
forEach --state:loop--> firstBodyTask -> ... -> lastBodyTask --(empty {})
forEach --state:success--> nextTaskAfterLoop
```

#### forEach constraints (all four are required)

1. **`incoming` must only contain `data_array`** — do NOT include `job_id` or any other field. Adding `job_id` causes errors at runtime.

2. **`$var.<taskId>.<output>` does NOT resolve inside the loop body** — string references like `$var.n01.current_item` silently resolve to `null` inside a forEach body. Use `$var.job.<varName>` instead (bind the forEach's outgoing to a job variable and reference that). This applies to ALL reference styles — even taskRef objects `{"task": "outerTask", "variable": "current_item"}` are unreliable inside a nested body.

3. **Loop body tasks cannot transition to tasks outside the loop** — no error transitions from loop body tasks to external error handlers. The `forEach` task itself handles exit via `state: "error"` on the forEach transition. Handle errors within the loop body, then let the forEach's error transition route out.

4. **The last loop body task signals loop-back with an empty `{}` transition** — do NOT add an explicit loop-back target pointing to forEach.

```json
"transitions": {
  "forEachTaskId": {
    "firstBodyTask": {"type": "standard", "state": "loop"},
    "nextTaskAfterLoop": {"type": "standard", "state": "success"},
    "errorHandlerTask": {"type": "standard", "state": "error"}
  },
  "lastBodyTask": {}
}
```

### newVariable

Create or set a job variable at runtime.

**Incoming:** `name` (string), `value` (any)
**Outgoing:** `value` (any)

```json
{
  "incoming": {"name": "taskStatus", "value": "success"},
  "outgoing": {"value": "$var.job.taskStatus"}
}
```

**GOTCHA:** `$var` inside `value` does NOT resolve. The literal string is stored. Use merge + query to build dynamic values.

### makeData

Construct data with `<!var!>` variable substitution.

**Incoming:** `input` (string with `<!var!>` placeholders), `outputType` (`"string"`/`"json"`/`"number"`/`"boolean"`), `variables` (object)
**Outgoing:** `output` (any)

**The `variables` field must be a resolved object.** Use merge first to build it, then pass via `$var.taskId.merged_object`:

```
merge (build variables object) → makeData (use $var.taskId.merged_object as variables)
```

> **WARNING — `makeData.incoming.variables` cannot use `$var` references to a merge that sources childJob output.**
> When a `merge` task's `data_to_merge` contains a childJob reference (e.g., `{"task": "childJobId", "variable": "job_details"}`), the platform cannot compile `$var.<mergeId>.merged_object` as a `taskRef` for `makeData.incoming.variables` — it is stored as a literal static string. Template substitution then operates on the literal string and emits unresolved placeholders.
>
> `query.incoming.obj` does NOT have this limitation — it resolves `$var.<mergeId>.merged_object` correctly even when the merge references childJob output.
>
> **Fix:** extract individual values from the childJob-sourced merge using `query` tasks, then pass those resolved scalars to makeData via a second merge (that contains only non-childJob refs). Do NOT feed a childJob-sourced merge directly into makeData's `variables`.

### delay

Pause execution. **Incoming:** `time` (integer, seconds). **Outgoing:** `time_in_milliseconds`.

### push / pop / shift

Array manipulation on job variables **by name** (plain string, NOT `$var` reference).

```json
{
  "incoming": {
    "job_variable": "collectedResults",
    "item_to_push": "$var.c3d4.return_data"
  }
}
```

**GOTCHA:** Pass `"myArray"`, NOT `"$var.job.myArray"`.

### deepmerge

Same as `merge` but merges nested objects recursively instead of overwriting top-level keys. Use when combining objects that share nested keys.

**Incoming:** `data_to_merge` (array, min 2 items — same format as merge)
**Outgoing:** `merged_object` (object)

### transformation

Perform JSON transformation using JST (JSON Schema Transformation).

**Incoming:** `tr_id` (string — transformation ID), `variableMap` (object — maps transformation inputs to data locations), `options` (object, optional — e.g., `{"extractOutput": true}`)
**Outgoing:** `outgoing` (any)

Used in childJob mode 3 (loop with transformation) to reshape each `data_array` element before passing to the child.

### decision

Multi-way branching based on conditions. Unlike `evaluation` (binary true/false), `decision` branches to different tasks based on multiple conditions.

**Incoming:** `decisionArray` (array of decision objects with conditions and target task IDs)
**Outgoing:** `return_value` (string — the ID of the next task)

### restCall

Make external HTTP calls from within a workflow. Use when calling APIs not exposed through adapters.

**Response shape — no wrapper.** `restCall` returns the **already-parsed JSON body directly** as the outgoing value. There is no `response` or `result` wrapper. Query paths target body fields directly:

```
Correct:   "query": "access_token"
Wrong:     "query": "response.access_token"   ← no response wrapper
Wrong:     "query": "result.access_token"     ← no result wrapper
```

This is the opposite of adapter tasks (e.g., `genericAdapterRequest`), which always wrap the upstream response in `{response, headers, metrics}`. Don't cross-apply the adapter query paths to `restCall` output — you'll get null every time.

### modify

Modify data by querying into an object and replacing with a new value.

**Incoming:** `object_to_update` (any), `query` (string — json-query path), `new_value` (any)
**Outgoing:** `updated_object` (any)

### validateJsonSchema

Validate JSON data against a JSON schema.

**Incoming:** `jsonData` (object), `schema` (object)
**Outgoing:** `result` (object — `{"valid": true}` or `{"valid": false}`)

### Additional Utility Tasks (60+)

Search `tasks.json` for the full catalog:
```bash
jq '.[] | select(.app == "WorkFlowEngine") | {name, summary}' {use-case}/tasks.json
```

| Category | Examples |
|----------|---------|
| String | `stringConcat`, `replace`, `split`, `toLowerCase`, `toUpperCase`, `trim`, `substring` |
| Array | `arrayConcat`, `arrayPush`, `sort`, `join`, `arraySlice`, `map`, `reverse` |
| Object | `assign`, `keys`, `values`, `objectHasOwnProperty`, `setObjectKey` |
| Time | `getTime`, `addDuration`, `convertTimezone`, `calculateTimeDiff` |
| Parse/Transform | `parse`, `transformation`, `stringify` |
| Tools | `restCall`, `csvStringToJson`, `excelToJson`, `asciiToBase64` |

**Reach for purpose-built tasks before chaining primitives.** Two tasks that are commonly underused:

- **`setObjectKey`** (WorkFlowEngine) — writes a value directly into a nested key of an existing object. Use instead of `query` + `merge` when updating a single field on an object already in `$var.job.*`.
- **`renderJinja2ContextWithCast`** (ConfigurationManager) — renders a Jinja2 template with the full job context automatically injected, plus optional type casting on the output. Use instead of `merge` → `renderJinja2` → `query` chains when the template needs access to existing job variables. Outputs `renderedTemplate` accessible via `$var.<taskId>.renderedTemplate`.

Fetch full schemas with `POST /automation-studio/multipleTaskDetails?dereferenceSchemas=true`.

### Task Endpoint Patterns (Standalone Testing)

Some tasks have standalone REST endpoints — **faster than creating test workflows:**
- **WorkFlowEngine:** `POST /workflow_engine/{method}` (e.g., `/workflow_engine/query`) — requires `job_id` (use dummy ObjectId `"4321abcdef694aa79dae47ad"`)
- **MOP:** `POST /mop/RunCommandTemplate` — test command templates directly
- **TemplateBuilder:** `POST /template_builder/templates/{name}/renderJinja` with `{"context": {...}}` (note: `context`, not `variables`)

Most utility tasks (array ops, string ops, forEach, childJob, merge) do NOT have standalone endpoints. Test those by creating a minimal `start → task → end` workflow and running via `jobs/start`.

---

## Templates (Jinja2 / TextFSM)

```
POST /automation-studio/templates
```
```json
{
  "template": {
    "name": "VLAN_Interface_Config",
    "type": "jinja2",
    "group": "Cisco IOS",
    "command": "configure terminal",
    "description": "Generates VLAN interface config",
    "template": "interface Vlan{{ vlan_id }}\n description {{ description }}\n ip address {{ ip_address }} {{ subnet_mask }}\n no shutdown",
    "data": "{\"vlan_id\": 100, \"description\": \"Management\", \"ip_address\": \"10.0.1.1\", \"subnet_mask\": \"255.255.255.0\"}"
  }
}
```

**Required fields:** `name`, `group`, `command`, `description`, `template`, `data`, `type`

**Types:** `jinja2` (config generation) or `textfsm` (output parsing)

**Test rendering directly:**
```
POST /template_builder/templates/{name}/renderJinja
```
```json
{"context": {"vlan_id": 100, "description": "Management"}}
```

**Gotchas:**
- `group` cannot be empty or whitespace-only
- Use underscores in template names (e.g., `IOS_Switchport_Config`)
- `data` field is a JSON string, not an object
- Variable syntax is `{{ var }}` (Jinja2), NOT `$var` or `<!var!>`
- **No `from_json` filter** — Ansible's `from_json` Jinja2 filter does NOT exist in Itential's TemplateBuilder. If you need to parse a JSON string, use a `parse` task before the template render step, not a filter inside the template
- **`renderJinjaTemplate` as a workflow task** — use `TemplateBuilder.renderJinjaTemplate` with incoming `templateName` (string) and `variables` (object). Output is at `result.renderedTemplate` (string). Different from the standalone API endpoint which uses `context` instead of `variables`

---

## Command Templates (MOP)

MOP manages command templates for running CLI commands with validation rules. **MOP is read-only validation only — never use it to push config.**

**To push config to a device, use `itential_cli` via AGManager** — not MOP. The standard pattern for any config push delivery is:

```
Pre-Check (RunCommandTemplate child)
  → Push Configuration to Device (renderJinjaTemplate → dry run approval → itential_cli → commit approval → itential_cli)
  → Post-Check (RunCommandTemplate child)
  → runTemplatesDiff (compare pre vs post)
```

Read the Arista EOS "Push Configuration to Device - IAG" and "Command Template Runner" workflows before building any config push delivery:
```bash
jq '[.components[] | select(.type=="workflow") | select(.document.name | test("Push Config|Command Template"))] | .[].document | {name:.name, tasks:.tasks, transitions:.transitions}' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-arista-eos.json
```

### Create a Command Template

```
POST /mop/createTemplate
```
```json
{
  "mop": {
    "name": "Port_Turn_Up_Pre_Check",
    "description": "Validates interface and VLAN",
    "os": "",
    "passRule": true,
    "ignoreWarnings": false,
    "commands": [
      {
        "command": "show interface <!interface!>",
        "passRule": true,
        "rules": [
          {
            "rule": "line protocol is",
            "eval": "contains",
            "severity": "error"
          }
        ]
      },
      {
        "command": "show vlan brief",
        "passRule": true,
        "rules": [
          {
            "rule": "<!vlan_id!>",
            "eval": "contains",
            "severity": "error"
          }
        ]
      }
    ]
  }
}
```

**Variable syntax:** `<!variable_name!>` in both commands and rules (NOT `{{ }}` or `$var`)

### passRule Logic

- **Template-level `passRule: true`** = ALL commands must pass (AND)
- **Template-level `passRule: false`** = ONE command must pass (OR)
- **Command-level** = same logic for rules within a command

### Rule Evaluation

| Eval | Purpose | Example |
|------|---------|---------|
| `contains` | String exists in output | `"line protocol is"` |
| `!contains` | String does NOT exist | `"ERROR"` |
| `contains1` | String exists exactly once | `"Active"` |
| `RegEx` | Regex matches (capital R, E!) | `"/\\d+\\.\\d+/"` |
| `!RegEx` | Regex does NOT match | `"/ERROR/"` |
| `#comparison` | Extract + compare two values | See below |

**#comparison:** Extract values with regex, compare numerically:
```json
{
  "rule": "/Available: (\\d+)/",
  "ruleB": "/Total: (\\d+)/",
  "eval": "#comparison",
  "evaluator": ">=",
  "severity": "error"
}
```
Evaluators: `=`, `!=`, `<`, `>`, `<=`, `>=`, `%` (percentage)

**Flags:** `case: true` = case-INSENSITIVE (confusing name), `global: true`, `multiline: true` (RegEx only)

### Run a Command Template

**Standalone:**
```
POST /mop/RunCommandTemplate
```
```json
{
  "template": "Port_Turn_Up_Pre_Check",
  "variables": {"interface": "GigabitEthernet0/1", "vlan_id": "100"},
  "devices": ["IOS-CAT8KV-1"]
}
```

**In a workflow (MOP.RunCommandTemplate task):**
```json
{
  "incoming": {
    "template": "$var.job.templateName",
    "variables": "$var.job.templateVariables",
    "devices": "$var.job.devices"
  },
  "outgoing": {
    "mop_template_results": null
  }
}
```

### Response Shape

```json
{
  "all_pass_flag": true,
  "result": true,
  "name": "Port_Turn_Up_Pre_Check",
  "commands_results": [
    {
      "raw": "show interface <!interface!>",
      "evaluated": "show interface GigabitEthernet0/1",
      "all_pass_flag": true,
      "device": "IOS-CAT8KV-1",
      "response": "...command output...",
      "result": true,
      "rules": [{"rule": "line protocol is", "eval": "contains", "result": true}]
    }
  ]
}
```

### Update a Command Template

```
POST /mop/updateTemplate/{mopID}
```
`mopID` is the template name (URL-encoded). Body is `{"mop": {...}}` — **full replacement**, include ALL fields.

### Analytic Templates (Pre/Post Comparison)

```
POST /mop/createAnalyticTemplate
```
```json
{
  "name": "Interface_Change_Validation",
  "os": "cisco-ios",
  "passRule": true,
  "prepostCommands": [
    {
      "preRawCommand": "show interface GigabitEthernet0/1",
      "postRawCommand": "show interface GigabitEthernet0/1",
      "passRule": true,
      "rules": [
        {
          "type": "matches",
          "preRegex": "/line protocol is (\\w+)/",
          "postRegex": "/line protocol is (\\w+)/",
          "evaluator": "="
        }
      ]
    }
  ]
}
```

**In a workflow (MOP.runAnalyticsTemplate task):**
```json
{
  "incoming": {
    "pre": "$var.preCheckTaskId.mop_template_results",
    "post": "$var.postCheckTaskId.mop_template_results",
    "analytic_template_name": "Interface_Change_Validation",
    "variables": {}
  },
  "outgoing": {"analytic_result": null}
}
```

---

## Testing & Debugging

### Start a Job

```
POST /operations-manager/jobs/start
```
```json
{
  "workflow": "My Workflow Name",
  "options": {
    "description": "Test run",
    "type": "automation",
    "variables": {"deviceName": "IOS-CAT8KV-1"}
  }
}
```

Response: `{"message": "...", "data": {"_id": "jobId", "status": "running"}}`

### Check Job Status

```
GET /operations-manager/jobs/{jobId}
```

Response wrapped in `{message, data, metadata}`:
- `data.status` — `"running"`, `"complete"`, `"error"`, `"canceled"`
- `data.variables` — all job variables including outputs
- `data.error` — array of error objects on failure

### Debug Failed Jobs

1. `GET /operations-manager/jobs/{jobId}` — check `data.status`
2. If `"error"`, read `data.error[]` — each has `task` (ID) and `message.IAPerror.displayString`
3. Identify the failing task ID, check its `metrics.finish_state`

**Common failures:**
| Symptom | Cause | Fix |
|---------|-------|-----|
| "Method not found" validation error | Task name doesn't exist | Search `tasks.json` |
| "No available transitions" | Missing error transition | Add `"state": "error"` transition |
| `$var` resolves to literal string | Non-hex task ID or nested object | Check task IDs, use merge |
| "Cannot find workflow" | childJob ref broken after project move | Update `workflow` field with `@projectId:` prefix |
| Schema validation error | Wrong/missing fields | Check `task-schemas.json` |
| Adapter error | Wrong app name or adapter down | Check `apps.json` and `GET /health/adapters` |
| "No config found for Adapter: X" | `app` field uses adapter instance name instead of type name | `app`/`locationType` must be the **type** from `apps.json` (e.g., `EmailOpensource`), not instance name (e.g., `email`). Instance name goes in `adapter_id`. |
| Silent data mismatch | Field type doesn't match schema (string vs array) | Check `task-schemas.json` — pass arrays for array fields, numbers for number fields |

### Standalone Test Endpoints

Some tasks have REST endpoints for quick testing without creating workflows:
- **query:** `POST /workflow_engine/query` (needs dummy `job_id`)
- **Jinja2 render:** `POST /template_builder/templates/{name}/renderJinja` with `{"context": {...}}`
- **MOP:** `POST /mop/RunCommandTemplate` with `{"template": "name", "devices": [...], "variables": {...}}`

### Updating Assets (Edit Locally, PUT to Update)

| Asset | Create | Update | Delete |
|-------|--------|--------|--------|
| Workflow | `POST /automation-studio/automations` | `PUT /automation-studio/automations/{id}` with `{"update": {...}}` | `DELETE /workflow_builder/workflows/delete/{URL-encoded-name}` (by name, not ID) |
| Template | `POST /automation-studio/templates` | `PUT /automation-studio/templates/{id}` with `{"update": {...}}` | `DELETE /automation-studio/templates/{id}` |
| Command Template | `POST /mop/createTemplate` | `POST /mop/updateTemplate/{name}` with `{"mop": {...}}` (full replacement) | — |

**Pre-flight validate before every create or update:**
```
POST /automation-studio/workflows/validate
{"workflow": {...}}
→ {"errors": [], "warnings": []}
```
Empty `errors` = schema valid. Run this before every POST or PUT.

**Workflow rename:**
```
POST /workflow_builder/workflows/rename
{"workflow": {...full doc...}, "newName": "New Workflow Name"}
```
Renames in-place without recreating. Use instead of appending `[Fixed]` suffixes.

---

## Workflow Patterns

### Error Handling: Try-Catch

**In child workflows:** catch errors with `newVariable` to set a status flag:
```
task --success--> newVariable("taskStatus" = "success") -> workflow_end
task --error--> newVariable("taskStatus" = "error") -> workflow_end
```

**In parent workflows:** after childJob, extract and check:
```
childJob -> query (extract taskStatus from job_details) -> evaluation (== "success"?)
  |-- success -> continue
  |-- failure -> handle error
```

### Error Transitions on Adapter Tasks

Every adapter task needs both success and error transitions. Route errors to an intermediate `newVariable` task if both need to reach `workflow_end`:

```json
"transitions": {
  "a1b2": {
    "c3d4": {"type": "standard", "state": "success"},
    "err1": {"type": "standard", "state": "error"}
  },
  "err1": {
    "workflow_end": {"type": "standard", "state": "success"}
  }
}
```

### Manual Tasks (Human-in-the-Loop)

**ViewHTML** — renders an HTML string in a modal for operator review. Requires specific fields or it becomes a draft workflow:
```json
{
  "name": "ViewHTML", "canvasName": "ViewHTML",
  "location": "Application", "locationType": null, "app": "WorkFlowEngine",
  "type": "manual", "displayName": "Tools",
  "view": "/workflow_engine/task/ViewHTML",
  "taskVersion": 2, "hostApp": "@itential/app-operations_manager",
  "variables": {
    "incoming": {
      "header": "Report Title",
      "body": "$var.job.html_output",
      "variables": "",
      "btn_success": "Acknowledge",
      "btn_failure": ""
    },
    "outgoing": {}
  },
  "actor": "Pronghorn"
}
```
`view`, `taskVersion: 2`, and `hostApp` are all **required** — omitting any one causes "Manual Tasks require 'view' key" draft error.

**Read a live ViewData example** from the Cisco IOS upgrade workflow — it shows makeData → ViewData → success/failure branches in production:
```bash
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "ViewData")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json
```

Three rules that cause draft validation errors if missed:
1. `view` is a **top-level** field (sibling of `name`, `type`, `app`) — NOT inside `variables`. Missing it → `"Manual Tasks require 'view' key with path to task view"`.
2. `incoming.variables` **MUST be present** (value can be `{}` if unused). Missing it → `"Input: 'variables' is not defined in task model"`.
3. `displayName` must be `"Tools"` and `actor` must be `null` (no actor field) on manual tasks.

Note: production assets include `"error": ""` and `"decorators": []` in the variables block on ViewData tasks — these are added by Studio on export and are harmless. You do not need to add or remove them.

```json
{
  "name": "ViewData",
  "canvasName": "ViewData",
  "location": "Application",
  "app": "WorkFlowEngine",
  "displayName": "Tools",
  "type": "manual",
  "view": "/workflow_engine/task/ViewData",
  "variables": {
    "incoming": {
      "header": "Approval Required",
      "message": "Review and approve.",
      "body": "$var.job.dataToReview",
      "variables": "$var.job.dataToReview",
      "btn_success": "Approve",
      "btn_failure": "Reject"
    },
    "outgoing": {}
  },
  "groups": []
}
```

### ViewHTML (Manual Task — HTML Display)

Use `ViewHTML` when you need to display formatted HTML to an operator during a workflow — for reports, tables, or styled summaries. Same manual task rules as ViewData apply.

**Read a live ViewHTML example:**
```bash
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "ViewHTML")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json
```

Key differences from ViewData:
1. `view` is `/workflow_engine/task/ViewHTML`
2. `body` is a raw HTML string — use inline CSS (no `<style>` blocks), `<!var!>` syntax for variable substitution
3. `incoming.variables` is a **plain object** `{"varName": "value"}` that populates `<!var!>` placeholders in the HTML — NOT a `$var` reference
4. `displayName: "Tools"`, no `actor` field (same as ViewData)

```json
{
  "name": "ViewHTML",
  "canvasName": "ViewHTML",
  "location": "Application",
  "app": "WorkFlowEngine",
  "displayName": "Tools",
  "type": "manual",
  "view": "/workflow_engine/task/ViewHTML",
  "variables": {
    "incoming": {
      "header": "Report",
      "body": "<h2>Status: <!status!></h2><p>Device: <!device!></p>",
      "variables": {
        "status": "$var.job.deviceStatus",
        "device": "$var.job.deviceName"
      },
      "btn_success": "Continue",
      "btn_failure": "End"
    },
    "outgoing": {}
  },
  "groups": []
}
```

### autoApprove Pattern

Use an `evaluation` task to conditionally skip manual approval:

```
evaluation (autoApprove == true?)
  |-- success -> skip to next task (auto-approved)
  |-- failure -> ViewData (human reviews and approves/rejects)
```

The workflow accepts an `autoApprove` boolean input. When `true`, skips the manual step. Useful for CI/CD pipelines that run unattended vs interactive operator sessions.

### Revert Transitions (Retry Loops)

Use `"type": "revert"` transitions to go backward for retry scenarios:

```
renderTemplate -> viewConfig (approve/reject)
  |-- success -> pushConfig -> evalSuccess
  |                             |-- success -> end
  |                             |-- failure -> viewError (retry/abort)
  |                                             |-- success (retry) --revert--> renderTemplate
  |                                             |-- failure (abort) -> end
  |-- failure (reject) --revert--> renderTemplate
```

The `revert` transition moves execution back to a previous task, allowing the user to fix inputs and retry.

### Modular Workflow Design

- Build each child workflow independently testable via `jobs/start`
- Use `childJob` with `data_array` + `loopType: "parallel"` to fan out
- Check for existing workflows before building new ones
- Keep all asset JSON locally — edit locally, PUT to update

### Network Device Config Pattern

1. **MOP command templates** for validation checks only (show commands + rules)
2. **Jinja2 templates** to generate configuration
3. **Push config** via existing workflow or adapter task — ask the engineer
4. **Test CLI commands** on the actual device BEFORE building workflows

---

## Variable Syntax Reference

| Context | Syntax | Example |
|---------|--------|---------|
| Jinja2 templates | `{{ var }}` | `interface Vlan{{ vlan_id }}` |
| Command templates (MOP) | `<!var!>` | `show interface <!interface!>` |
| `makeData` input | `<!var!>` | `{"name": "<!name!>"}` |
| Workflow variable refs | `$var.job.x` or `$var.taskId.x` | `$var.job.deviceName` |
| childJob variable refs | `{"task":"job","value":"varName"}` | `{"task":"static","value":["a"]}` |
| merge/evaluation refs | `{"task":"job","variable":"varName"}` | `{"task":"static","variable":"success"}` |

**childJob uses `"value"`. merge/evaluation use `"variable"`. Do NOT mix them.**

---

## API Response Shapes

| Endpoint | Shape |
|----------|-------|
| `POST /operations-manager/jobs/start` | `{message, data: {_id, status}}` |
| `GET /operations-manager/jobs/{id}` | `{message, data: {status, variables, error}}` |
| `POST /automation-studio/projects` | `{message, data: {_id, name}}` |
| `POST /automation-studio/automations` | `{created: {_id, name}, edit: "..."}` |
| `POST /automation-studio/templates` | `{created: {_id, name}, edit: "..."}` |
| `GET /automation-studio/workflows` | `{items: [...], skip, limit, total}` |
| `GET /automation-studio/templates` | `{items: [...], skip, limit, total}` |

### Adapter Response Shapes

**Adapters transform upstream API responses.** Don't assume the native API's response structure. For example, ServiceNow's Table API returns `result.sys_id`, but the Itential adapter flattens it to `response.id`. Always verify by calling the adapter directly or checking `openapi.json`.

### Adapter URI Prefix

`genericAdapterRequest` auto-prepends the adapter's `base_path` to `uriPath`. Don't include `/api/v1` in `uriPath`. Use `genericAdapterRequestNoBasePath` to bypass.

---

## Gotchas

> **Pre-flight scan list — read this before every project import and job start.** This list is intentionally redundant with the body sections. The repetition is deliberate: scanning a flat list before submitting catches mistakes that are easy to miss when building task by task.
>
> **To add a new finding:** put the detail in the relevant body section first, then add a one-liner here pointing to it.

### Projects
1. **Use `POST /projects/import` to create projects with all assets atomically** — avoids broken childJob refs, project-locking issues, and intermediate state. Pre-compute `_id` so childJob `@projectId:` refs can be wired before push.
2. **Avoid create + move pattern** — moving assets renames them with `@projectId:` prefix but does NOT update internal references (childJob `workflow` fields, template names).
3. **Import format differs from create** — OMIT `encodingVersion` from workflow documents (causes silent component failure). Workflow `created_by` has NO `_id` but has `firstname`, `inactive`, `sso`. Project `createdBy` HAS `_id`.
4. **Component type is `mopCommandTemplate`** — not `mop`.
5. **Members PATCH is full replacement** — include ALL members or omitted ones are removed.
6. **Import sets the OAuth service account as project owner** — not the UI user. PATCH membership immediately after import (Phase 3, not Phase 6) or the spec engineer is locked out.
7. **`accessControl` in PATCH body is silently ignored** — API returns 200 but the field is a no-op. Always use the `members` array format (`[{type, reference, role}]`).

### Workflows
8. **`canvasName` must come from `tasks.json`** — some differ from method name: `arrayPush`→`push`, `stringConcat`→`concat`. Wrong `canvasName` causes silent `$var` failures.
9. **Task IDs must be hex `[0-9a-f]{1,4}`** — non-hex causes silent `$var` failure.
10. **Validation errors = draft workflow** that cannot be started. Run `POST /automation-studio/workflows/validate` before every create or update.
11. **`$var` inside nested objects doesn't resolve** — use merge/makeData/query to build the object first.
12. **`stringConcat` does not resolve `$var` inside `stringN` arrays** — values stored as literal strings. Use `merge` → `makeData` with `<!var!>` placeholders instead.
13. **Every adapter/external task needs an error transition** — without one, errors cause "Job has no available transitions" and the job gets stuck forever.
14. **JSON can't have duplicate keys** — if success and error both go to `workflow_end`, route error to an intermediate `newVariable` task first.

### Utility Tasks
15. **merge uses `"variable"`, childJob uses `"value"`** — don't mix them. Using `"variable"` in childJob causes `undefined.indexOf()` at job start (P6.4.0+).
16. **merge requires at least 2 items** — 1 item silently returns null.
17. **childJob `actor` MUST be `"job"`**, `task` MUST be `""`, `job_details` outgoing MUST be `null`.
18. **childJob `variables` use `{"task","value"}` NOT `$var`** — `$var` strings inside variables cause an indefinite hang at runtime.
19. **`evaluation` MUST have both success AND failure transitions** — missing one silently drops the job.
20. **`forEach` last body task transition must be empty `{}`** — do NOT connect it back to forEach.
21. **`push`/`pop`/`shift` take variable NAME as a plain string** — `"myArray"` not `"$var.job.myArray"`.
22. **`newVariable` value with `$var` stores the literal string** — use merge + query to build dynamic values.
23. **`makeData` `variables` must be a resolved object** — use merge first, then pass `$var.taskId.merged_object`.
24. **Adapter task `result` is always an object** — never a primitive. When the upstream API returns a simple string (e.g., Infoblox `_ref`), it's at `result.response`. Passing raw `result` in a string context produces `[object Object]`.

### Templates
25. **Template `group` cannot be empty or whitespace-only** — causes a silent rejection.
26. **TextFSM templates may contain control characters** that break jq — use Python with a control-char strip when parsing them.

### MOP
27. **Missing variable = skip = PASS (not fail)** — if a variable isn't passed, the rule is skipped and the command auto-passes. Always verify variables are passed correctly.
28. **`case: true` = case-INsensitive** — the name is backwards. Easy to wire the wrong behavior.
29. **Eval types are case-sensitive** — `"RegEx"` not `"regex"`. Wrong casing silently fails.
30. **Empty rules = auto-pass** — a command with no rules always passes. Add at least one rule to validate output.
31. **MOP update is full replacement** — include ALL fields or omitted ones are lost.
32. **MOP is read-only** — never use it to push config. Use `itential_cli` via AGManager for config push.

### General
33. **Adapter `app` must come from `apps.json`** — NOT `tasks.json`. Names can differ completely (e.g., `ServiceNow` vs `Servicenow`). Wrong `app` causes "No config found for Adapter" at runtime.
34. **`legacyWrapper: false` on Operations Manager manual triggers** — default `true` wraps all form values under `formData`, breaking variable mapping to workflow inputs.
35. **`status: complete` doesn't mean CLI commands succeeded** — always check `stdout` for actual command output and errors.
36. **Endpoint base paths differ** — task catalog at `/workflow_builder/tasks/list`, schemas at `/automation-studio/multipleTaskDetails` (NOT `/workflow_builder/multipleTaskDetails`).
37. **`evaluation` operator is a closed enum** — only `contains, !contains, <, <=, >, >=, ==, !=` exist. Any other string silently returns `false` with empty outgoing and no error message. Validate against this list before wiring.
38. **`contains` uses regex, not substring matching** — `operand_2` is interpreted as a regex pattern. Escape metacharacters (`(`, `)`, `.`, `[`, `]`, `?`, `+`, `*`, `|`) in literal values: `9\.2\(4\)` not `9.2(4)`. Test with `POST /workflow_engine/runEvaluationGroups` before wiring.
39. **API PUT does not regenerate `incomingRefs` for existing task changes** — evaluation operand literals resolve to `null` after PUT. Broader symptom: entire workflow hangs after `workflow_start` (status: running forever). Fix: open in Studio and save. If still failing, recreate via fresh POST — more PUTs won't fix it.
40. **`$var.<taskId>.<out>` does not resolve inside nested forEach bodies** — use `$var.job.<varName>` for any variable referenced inside a nested loop body.
41. **Workflow delete endpoint** — `DELETE /workflow_builder/workflows/delete/{URL-encoded-name}` deletes by name, returns 200 with deleted doc. `DELETE /automation-studio/automations/{id}` does NOT exist (404). Always export the project before deleting anything.
42. **Always use a local venv for Python** — `python3 -m venv .venv && source .venv/bin/activate` before any Python scripts during the build.
43. **Search `tasks.json` before designing any sub-workflow** — a purpose-built platform task may already exist for the intent (filter, inventory, tag, etc.). Server-side is always better than a forEach + evaluation chain.
44. **Prefer server-side filtering over client-side when available** — fetching the full collection and filtering in a forEach adds unnecessary iterations. Check for a filtered-fetch task first.
45. **Propose decomposition when a workflow exceeds ~20 tasks** — extract inner iteration bodies into reusable child workflows.
46. **DRY check on sibling workflows** — if building multiple similarly-named workflows, compare task graphs. Identical graphs → propose one generic workflow, not N clones.
47. **Project component refresh** — `mode: "copy"` creates a new project-scoped UUID that immediately diverges from the standalone. To refresh: DELETE each old component, POST fresh, then update any Operations Manager automation `componentId` via `PATCH /operations-manager/automations/{id}`.
48. **`renderJinja2` inline template with `\n` breaks `parse`** — static values store literal `\n` characters, causing `parse` to fail with "Expected property name or '}' in JSON at position 1". Fix: write single-line templates.
49. **Task outgoing writes directly to job var** — `"outgoing": {"result": "$var.job.myVar"}` works on any task and is more reliable than a separate `newVariable` copy step (written at execution time, bypassing incomingRefs cache).
50. **GatewayManager `"failed to parse start_time"` = device unreachable** — this IAG error (`"failed to parse start_time for command 0: failed to parse timestamp string ''"`) means the device is offline, unreachable, or auth failed. The timestamp complaint is misleading — the session never opened. It is NOT a workflow bug. Guard with an `evaluation` checking whether the response contains a `result` key; if not, route to a skip handler and continue.
51. **NEVER wire a Configuration Manager remediation task** — `runAutoRemediation`, `advancedAutoRemediation`, `convertChangesToConfig`, `patchDeviceConfiguration`, `advancedPatchDeviceConfiguration`, `patchCMDeviceConfiguration` (IAP), `ManualRemediation`, and `ManualRemediationResults` are **prohibited** in every workflow, even when a spec asks for fully automatic remediation. Golden Config detects and reports drift; it never applies fixes to a device. To correct a device, build a normal config-push delivery. (`updateNodeConfig` is allowed — it authors the GC node template, not a device.)

---

## Helper Templates

**Two separate concerns — don't mix them:**
- **API wrappers** (project, workflow, template, form creation) → use `helpers/create/` scaffolds below. These are POST body wrappers — correct structure, required fields.
- **Task JSON inside a workflow** → extract from `helpers/assets/` using jq (see Guide 1 STOP block). Do NOT use `helpers/create/` files for task bodies — they are scaffold stubs, not task examples.

### Scaffolds — start from these

Read these first. They have the correct wrapper, required fields, and structure.

| When you need to... | Read this helper | Then POST to |
|---------------------|------------------|--------------|
| Create a project | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-project.json` | `POST /automation-studio/projects` |
| Create a workflow | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-workflow.json` | `POST /automation-studio/automations` |
| Create a Jinja2 template | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-template-jinja2.json` | `POST /automation-studio/templates` |
| Create a TextFSM template | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-template-textfsm.json` | `POST /automation-studio/templates` |
| Create a MOP command template | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-command-template.json` | `POST /mop/createTemplate` |
| Update a MOP template | `${CLAUDE_PLUGIN_ROOT}/helpers/update/update-command-template.json` | `POST /mop/updateTemplate/{name}` |
| Create a JSON form (static dropdowns) | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-json-form.json` | `POST /json-forms/forms` — see `itential-json-forms` skill |
| Create a JSON form (REST-bound or cascading dropdowns) | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-json-form-rest-bound.json` | `POST /json-forms/forms` — see `itential-json-forms` skill |
| Create an Ops Manager automation | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-ops-manager-automation.json` | `POST /operations-manager/automations` |
| Create a manual trigger (with form) | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-ops-manager-trigger-manual.json` | `POST /operations-manager/triggers` — `legacyWrapper` MUST be false |
| Create a scheduled trigger | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-ops-manager-trigger-schedule.json` | `POST /operations-manager/triggers` |
| Import a project (atomic) | `${CLAUDE_PLUGIN_ROOT}/helpers/create/import-project.json` | `POST /automation-studio/projects/import` |
| Add assets to a project | `${CLAUDE_PLUGIN_ROOT}/helpers/operations/add-components-to-project.json` | `POST /projects/{id}/components/add` |
| Update project membership | `${CLAUDE_PLUGIN_ROOT}/helpers/update/update-project-members.json` | `PATCH /projects/{id}` |

### Task templates — extract from asset projects

Do not write task JSON from scratch. For every task type, extract a real example from an asset project and adapt it. Use the jq commands below — they work against the project files in `${CLAUDE_PLUGIN_ROOT}/helpers/assets/`.

```bash
# Adapter task (ServiceNow, Infoblox, etc.)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.location == "Adapter")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-servicenow.json

# Application task (WorkFlowEngine — getTime, newVariable, query, evaluation, transformation, merge, makeData)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.app == "WorkFlowEngine" and .value.name == "TASK_NAME")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/itential-platform-configuration-management.json

# childJob
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "childJob")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json

# evaluation / branching
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "evaluation")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json

# transformation (JST)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "transformation")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-netbox.json

# RunCommandTemplate / viewTemplateResults / reattempt / runTemplatesDiff (MOP tasks)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "TASK_NAME")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/itential-platform-configuration-management.json

# itential_cli (config push via IAG)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "itential_cli")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-arista-eos.json

# ViewData / ViewHTML (manual tasks)
jq '[.components[].document.tasks // {} | to_entries[] | select(.value.name == "ViewData")] | first | .value' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/vendor-cisco-ios.json
```

Key fields to verify after extracting (see body sections above for full rules per task type):

| Task type | Must-check fields |
|-----------|-------------------|
| Adapter | `app`/`locationType` from apps.json (not tasks.json), `adapter_id`, error transition |
| childJob | `actor: "job"`, `task: ""`, variables use `{"task","value"}` not `$var` |
| evaluation | `evaluation_groups[]`, `all_true_flag`, both success AND failure transitions |
| transformation | `tr_id`, `variableMap` keys match transformation's `incoming` schema |
| ViewData / ViewHTML | `view` is top-level (not inside `variables`), `displayName: "Tools"`, no `actor`, no `error`/`decorators` |
| Manual tasks (any) | `type: "manual"`, `taskVersion: 2`, `hostApp` required |

### Reference workflows — read from asset projects

Real, production-tested workflows. Use the jq commands to extract and study them before building.

| Pattern | Asset file | jq filter |
|---------|-----------|-----------|
| Adapter workflow: merge → create → query → update + error handling | `vendor-servicenow.json` | `select(.document.name \| test("Create Change"))` |
| childJob orchestrator + evaluation branching | `vendor-cisco-ios.json` | `select(.document.name \| test("IOS Upgrade"))` |
| childJob loop with data_array (parallel/sequential) | `vendor-cisco-ios.json` | `select(.document.name \| test("Upgrade\|Runner"))` |
| Config push: renderJinja → dry-run ViewData → itential_cli → commit | `vendor-arista-eos.json` | `select(.document.name \| test("Push Config"))` |
| Pre/post MOP check: RunCommandTemplate → viewTemplateResults → evaluation → reattempt | `itential-platform-configuration-management.json` | `select(.document.name \| test("Command Template Runner"))` |
| IPAM CRUD (adapter + transformation + error) | `vendor-infoblox-nios-ddi.json` | `select(.document.name \| test("Create Network\|Assign Next"))` |
| ITSM ticket + update (ServiceNow) | `vendor-servicenow.json` | `select(.document.name \| test("Create Incident"))` |
| LCM action workflow (must output `instance`) | `lcm/lcm-vxlan-fabric-services-project.json` | `select(.document.name \| test("Create\|Delete"))` — note: this file uses `.data.project.components[]` |
| Email/notification | `itential-platform-email.json` | `select(.document.name \| test("Email"))` |

```bash
# General pattern to read any workflow by name from an asset project:
jq '[.components[] | select(.type=="workflow") | select(.document.name | test("PATTERN"; "i"))] | first | .document | {name:.name, tasks:.tasks, transitions:.transitions}' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/ASSET_FILE.json

# For the LCM project (different wrapper):
jq '[.data.project.components[] | select(.type=="workflow") | select(.document.name | test("PATTERN"; "i"))] | first | .document | {name:.name, tasks:.tasks, transitions:.transitions}' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/lcm/lcm-vxlan-fabric-services-project.json
```

````

============================================================
FILE: .claude/skills/documentation/SKILL.md
DIRECTORY: .claude/skills/documentation/
FILENAME: SKILL.md
============================================================
SHA256: 373bac9e19991e9d53fdeda7c8b6c849c21d7dcea47f80b51e03a15f5540a082

````markdown
---
name: documentation
description: Use this skill to survey and catalog an Itential platform — when someone wants to know what's on their platform, document global assets (workflows, templates, LCM models, golden config, OM automations) that are NOT inside a named project, group them into logical use cases, and produce a master catalog or README. Trigger it for phrases like "document everything on the platform", "what use cases do we have?", "catalog all our global workflows", "I inherited this platform and have no idea what's there", "group our automations by use case", or "produce a platform README". The output is a structured catalog: customer-spec.md + solution-design.md per use case + master README. NOT for documenting a specific named project — use /project-to-spec for that. NOT for building new automation.
---

# Documentation

**Purpose:** Read Itential assets → discover relationships → group into use cases → produce documentation
**Output:** `customer-spec.md` (inferred HLD per use case) + `solution-design.md` (as-built LLD per use case) + `README.md` (master index, only when multiple use cases)
**Feeds into:** Can be handed to `/spec-agent` for refinement or `/solution-arch-agent` for redesign

## CRITICAL: Output Requirements

**The ONLY deliverables are markdown files.** Do NOT produce JSON index files, JSON catalogs, or any intermediate artifacts. All analysis happens in-memory.

```
{reports-directory}/
  README.md                          ← master index of all use cases ONLY when more than one use case
  {use-case-slug}/
    customer-spec.md                 ← inferred HLD (business purpose, scope, requirements)
    solution-design.md               ← as-built LLD (components, flows, adapters, data model)
  {use-case-slug}/
    customer-spec.md
    solution-design.md
  ...
```

**Never write JSON files as output.** No `workflow-index.json`, no `asset-index.json`, no `use-case-groups.json`. The user wants documentation, not data dumps.

---

## What This Does

Surveys **global** Itential assets — workflows, JSON forms, transformations, templates, command templates, analytic templates, Operations Manager automations, golden configuration trees and compliance plans, and LCM resource models that live outside named projects. Accepts `all`, `platform`, a directory path, or a list of specific global asset names. Discovers how they relate to each other, groups them into logical use cases, and produces documentation for each group plus a master index when there are multiple use cases.

> **For a named project:** Use `/project-to-spec` instead — it reads a single project's components and produces customer-spec.md + solution-design.md tailored to that project.

---

## Flow

```
User invokes /documentation ['all' | 'platform' | directory | specific global asset names]
      |
      ├── Step 0: Determine Scope
      |     ├── Project named? → redirect to /project-to-spec
      |     ├── Specific global assets named? → resolve + discover relationships → ask grouping preference
      |     └── 'all' / platform / directory? → full collection + grouping flow
      |
      ├── Step 1: Collect + classify global assets (in-memory)
      ├── Step 2: Discover relationships + group into use cases (in-memory)
      ├── Step 3: Present proposed groupings to engineer for approval
      ├── Step 4: Write per-use-case reports (customer-spec.md + solution-design.md)
      ├── Step 5: Write master README.md (ONLY when more than one use case)
      └── Step 6: Present summary to engineer for review
```

---

## Step 0: Determine Scope

Before collecting assets, determine what the user wants to document.

### Pattern 1 — Project named

If the user names a specific project, **redirect them to `/project-to-spec`** — that skill is purpose-built for single-project documentation and produces a more thorough analysis.

> "It looks like you want to document a specific project — use `/project-to-spec` for that. It reads the project's components directly and produces a more thorough customer-spec.md and solution-design.md for it."

### Pattern 2 — Specific global asset(s) named

If the user provides one or more asset names or IDs:

1. Resolve each asset via the platform API or local files
2. Traverse the relationship graph starting from each named asset (childJob links, OM→workflow, LCM→workflow, golden config→command template, etc.)
3. Present the discovered asset cluster to the engineer:
   - List all assets found (named + discovered via relationships)
   - Show how they connect

4. Ask the engineer:
   > "I found these assets and their relationships. How should I document them?"
   > - **(Default) Group into use cases** — analyze and cluster into logical groups, then produce HLD+LLD per group
   > - **Document as a single unit** — treat the entire cluster as one use case, produce one HLD+LLD
   > - **Document each asset independently** — produce separate minimal documentation per asset without cross-linking

Proceed based on the engineer's answer.

### Pattern 3 — All globals / platform / directory

If the user says `all`, `platform`, or provides a directory path, run the full collection and grouping flow (Steps 1–6) without asking about grouping preference.

---

## Step 1: Collect and Classify Assets

Ask the engineer for the asset source if not specified. Two modes:

### Mode A — Local Directory

Scan for asset JSON files organized by type:

```
directory/
  workflows/                          *.json
  json_forms/                         *.json
  transformations/                    *.json or *.jst.json
  templates/                          *.json
  command_templates/                  *.json
  operations_manager_automations/     *.json
  golden_config/                      *.json
  lcm/                                *.json
```

If the directory is flat (all JSON at root), classify by JSON structure signatures below.

If a `projects/` subfolder exists, scan it too. Project manifest files (containing `name` + `components[]`) identify which assets belong to a project — use that grouping when building the relationship graph. Strip `@projectId:` prefixes from any workflow names found inside.

### Mode B — Platform API

Authenticate using `.auth.json` (see AGENTS.md auth reuse pattern). Fetch global assets (ensure you fetch pagination if there are a lot of assets):

```
GET /automation-studio/workflows?exclude-project-members=true&limit=500
GET /automation-studio/templates?limit=500
GET /automation-studio/json-forms?limit=500
GET /operations-manager/automations
GET /mop/templates
GET /golden-config/trees
GET /golden-config/plans
GET /lifecycle-manager/model
GET /automation-studio/projects?limit=500
```

> **Visibility caveat:** Global Automation Studio assets (the focus of this skill) are **not** access-restricted by ACL — they are visible to any authenticated client, so list endpoints like `GET /automation-studio/workflows?exclude-project-members=true` return the complete global set regardless of the calling client. The catalog of *globals* is therefore not undercounted by RBAC. The one exception in the list above is `GET /automation-studio/projects?limit=500`, which **is** filtered by per-project ACLs (each project must explicitly grant access to a user or group; there is no platform-wide admin or "all-projects" role). Since this skill targets global assets, projects are out of scope by default — but if the engineer names a specific project they expect, route to `/project-to-spec`, which handles visibility-vs-existence properly.

### Classification Signatures

| Asset Type | Identifying Fields |
|---|---|
| **Workflow** | `tasks` (object), `transitions` |
| **JSON Form** | `schema`, `struct`, `uiSchema` |
| **Transformation** | `incoming`, `outgoing`, `steps` |
| **Template** | `type` (textfsm/jinja2), `template` field |
| **Command Template** | `commands[]` with `rules[]` |
| **Analytic Template** | `commands[]` with `analytics[]` or `baseline` fields |
| **OM Automation** | `triggers[]`, `componentName` |
| **Golden Config Tree** | `nodes[]`, `rootNode`, `treeType` |
| **Golden Config Compliance Plan** | `planType`, `configSpec`, `devices[]` |
| **LCM Resource Model** | `resourceType`, `actions[]`, `schema` |

**Build the asset index in-memory only.** For each asset, note: name, file path/ID, type, and key metadata.

---

## Step 2: Discover Relationships and Group

### Relationship Discovery

Build a relationship graph in-memory connecting all assets:

1. **Workflow → Workflow (childJob links):** For each workflow task where `name === "childJob"` AND `app === "WorkFlowEngine"`, extract child workflow name from `variables.incoming.workflow`. Strip `@projectId:` prefixes.

2. **Workflow → JSON Form:** Tasks where `app === "JsonForms"` or name contains `RenderJsonSchema`/`JsonForm`.

3. **Workflow → Template:** Tasks where `app === "TemplateBuilder"` (renderJinjaTemplate, applyTemplate, applyTextFSMTemplate).

4. **Workflow → Transformation:** Tasks where `name === "transformation"`.

5. **Workflow → Command Template:** Tasks referencing MOP operations (runCommandTemplate).

6. **OM Automation → Workflow:** `componentName` field names the target workflow. Trigger types reveal entry mode: schedule, endpoint (webhook/API), manual (with optional formId).

7. **LCM Resource Model → Workflow:** Each LCM action has an `actionWorkflow` field naming an IAP workflow → link.

8. **Golden Config Compliance Plan → Command Template:** Plans reference MOP command templates for configuration checks → link.

9. **Workflow → Golden Config:** Workflows calling golden-config API tasks via adapter → link.

10. **Adapter patterns:** Collect tasks where `location === "Adapter"` — extract `app` (type name) and operation name.

11. **Naming prefix clustering:** Split on ` - ` (space-dash-space). Assets sharing a prefix are candidates for the same use case.

### Grouping Rules (apply in order)

1. **OM Automations as Entry Points:** Each OM automation's `componentName` → root workflow → traverse childJob graph → collect all reachable workflows + referenced forms/templates/transformations/command templates = one cluster.

2. **LCM Resource Models as Entry Points:** Each LCM model → action workflows → traverse childJob graph → collect all reachable assets = one cluster. If a workflow cluster already contains these workflows, merge the LCM model into that cluster.

3. **Golden Config Clusters:** Golden config trees + their compliance plans + referenced command templates → one cluster. If workflows reference these golden config assets, merge into the same cluster.

4. **Expand by Naming Prefix:** Add ungrouped assets sharing the same naming prefix as assets already in a cluster.

5. **Ungrouped Workflow Trees:** Any root workflow (no parent) with children → new cluster.

6. **Shared Utilities:** Workflows appearing in 3+ clusters → "Shared Utilities" group. Also include: generic TextFSM templates, utility transformations (math, array ops), common utilities (MongoDB CRUD, credential retrieval, notifications).

7. **Test / Standalone:** Workflows with developer name prefixes, `[TEST]`/`test-`/`dummy` patterns, Jira ticket patterns, or <5 tasks with no children and no triggers → "Standalone / Test Workflows" (catalog only, no full HLD/LLD).

8. **Remaining Ungrouped:** Group by functional similarity or list as individual entries in master README.

### Analyze the Components

Work through the components to reconstruct intent and structure.

#### Identify the orchestrator

Find the parent workflow — usually the one that:
- Has no `childJob` references pointing to it from other workflows
- References other workflows via `childJob` tasks
- Has the most complex transition graph

For LCM clusters, the resource model itself is the anchor — its action workflows are the orchestrators.
For golden config clusters, the compliance plan anchors the cluster.

#### Map the data flow

For the orchestrator and each child:
1. What are the **inputs**? (inputSchema properties)
2. What adapters are called? (location: "Adapter" tasks)
3. What utility tasks are used? (merge, query, evaluation, childJob, makeData)
4. What are the **outputs**? (outputSchema properties, `$var.job.x` assignments)
5. What external systems are touched? (adapter names → infer ServiceNow, Route53, etc.)

#### Infer the phases

Each major section of the orchestrator maps to a phase:
- A `childJob` to a child workflow = one phase
- An `evaluation` branch = a decision point
- An adapter call cluster = an integration phase
- A `ViewData` = an approval gate
- Error handling branches = rollback/recovery phases
- An LCM action = a lifecycle phase
- A compliance plan check = a validation phase

#### Reconstruct acceptance criteria

From the workflow structure, infer what "done" looks like:
- What does the final outgoing variable represent?
- What adapters were called? → "ServiceNow ticket created and updated"
- What verifications exist? → `evaluation` tasks checking status
- What is the `outputSchema`? → these are the observable outcomes

---

## Step 3: Present Groupings to Engineer

**Stop and present the proposed groupings before writing any reports.** Ask:

1. "Here are the use case groups I identified — does this look right?"
2. "These assets are ungrouped — should any be added to an existing group?" — default no
3. "These appear to be test/dev workflows — should I catalog or skip them?" — default skip

Show each group with: name, category (Core/Specialized/Shared/Reference), approximate asset count, and 1-line description.

**Wait for engineer approval before proceeding to Step 4.**

---

## Step 4: Write Per-Use-Case Reports

For each approved use case group, create a directory (or write directly to reports root if only one use case) with two markdown files.

### Produce `customer-spec.md`

Write professional, narrative documentation — not mechanical spec sheets. The HLD should read like a business-facing document with rich prose, detailed tables, and domain-specific context.

→ See template in `helpers/documentation-output-templates.md` — **"customer-spec.md Template"**

**For test/standalone use cases**, use a simplified catalog format — asset table with Purpose and Adapters columns only. No full HLD needed.

### Produce `solution-design.md`

Write the as-built LLD — this is factual, not inferred. Each component should have at least a sentence description, so an engineer could understand the full system without reading the source JSON.

→ See template in `helpers/documentation-output-templates.md` — **"solution-design.md Template"**

#### Generating Section D: Execution Flow

The guidance and example are in the Section D placeholder in `helpers/documentation-output-templates.md`.

Do not add a sequence diagram to the HLD (`customer-spec.md`). Section 2 of the HLD is a narrative paragraph only.

---

## Step 5: Write Master README

**Only write this step when there are 2 or more use cases.**

Create `README.md` at the root of the reports directory.

→ See template in `helpers/documentation-output-templates.md` — **"README.md Template"**

---

## Step 6: Present to Engineer

Show a summary:

1. **Asset inventory** — total files analyzed per type
2. **Use case groups** — count and names
3. **Reports produced** — list of directories/files with customer-spec.md + solution-design.md
4. **Excluded assets** — what was skipped
5. **Gaps** — "I don't see rollback logic or notifications."

Ask the engineer to review the reports. Next steps:
- **Accept** — use the reports as-is
- **Refine** — hand specific use case specs to `/spec-agent`
- **Redesign** — hand to `/solution-arch-agent`
- **Organize into projects** — proceed to Step 7

---

## Step 7: Organize Global Assets into Projects (Optional)

After the engineer accepts the use case groupings and reviews the reports, ask:

> "Would you like me to create a project for each use case and move the assets in? Moving assets into a project renames them with an `@projectId:` prefix — anything currently referencing those assets by name will need updating. Shared utility assets will stay global. Should I proceed?"

If no, stop here. The documentation stands as-is.

If yes, for each approved use case group (skip "Shared Utilities"):

**1. Create the project:**
```
POST /automation-studio/projects
{"name": "{use-case-name}", "description": "{one-line from customer-spec.md}", "thumbnail": "", "backgroundColor": "#FFFFFF"}
```
Save `data._id` as `projectId`.

**2. Add components:**
```
POST /automation-studio/projects/{projectId}/components/add
{
  "components": [
    {"type": "workflow", "reference": "{workflow-id}", "folder": "/"},
    {"type": "template", "reference": "{template-id}", "folder": "/"},
    {"type": "mopCommandTemplate", "reference": "{mop-name}", "folder": "/"}
  ],
  "mode": "move"
}
```

Component type values: `workflow`, `template`, `transformation`, `jsonForm`, `mopCommandTemplate`, `mopAnalyticTemplate`

**3. Build a reference impact report before moving anything:**

Before executing any moves, scan all global workflows, OM automations, and LCM models to find references that will break. For each asset being moved, find:

- **Workflows** with a `childJob` task where `variables.incoming.workflow` matches the asset's current name
- **OM automations** where `componentName` matches the asset's current name
- **LCM models** where any `actions[].actionWorkflow` matches the asset's current name

Produce a table:

| Asset being moved | Referenced by | Field | New name after move |
|------------------|--------------|-------|-------------------|
| `VLAN_Provision_Parent` | `Monthly_Audit` (workflow) | childJob.workflow | `@abc123: VLAN_Provision_Parent` |
| `DNS_Create` | `DNS Automation` (OM automation) | componentName | `@abc123: DNS_Create` |

Show this to the engineer **before** proceeding:
> "Moving these assets will break the following references. I won't fix them automatically — you'll need to update these manually after the move. Here's what needs changing:"

**4. Execute the moves** (after engineer confirms they've noted the impact):

For each group, run the `POST .../components/add` calls as above.

**5. After all groups are processed, show a final summary:**

| Use Case | Project ID | Assets Moved | Broken References to Fix |
|----------|------------|-------------|--------------------------|
| {name} | {id} | {count} | {count} — see impact report above |

Flag anything that couldn't be moved (already in a project, API error) for manual follow-up.

**Warnings to keep in mind:**
- Shared Utilities stay global — do not move them
- Assets already in a project cannot be moved again — skip and report
- Cross-project references (workflow in one project referencing a workflow in another) must use the full `@{otherProjectId}: {name}` format

---

## What to Watch For

- **Orphaned workflows:** No childJob parent AND no OM trigger. May be standalone utilities, abandoned, or externally invoked. Check adapter usage to infer purpose.
- **`@projectId:` prefixed names:** Strip prefix (everything through colon+space) before matching.
- **Empty componentName:** Fall back to trigger names, `actionId`, or automation name.
- **Duplicate/backup workflows:** Names with "Backup", date suffixes, version numbers → note as backups, don't give own group.
- **Cross-use-case shared workflows:** Document fully in primary group, add cross-references in others.
- **Transformation `.jst.json` naming:** Match on internal `name` field, not filename.
- **Template `data` field:** Often a JSON string, not parsed object — parse before analyzing.
- **Large TextFSM libraries:** Group under Shared Utilities, not individual use cases.
- **Command template rules:** Each rule encodes a compliance check — valuable for HLD requirements.
- **LCM `actionWorkflow` may be missing:** If a LCM action has no linked workflow, note the gap — the action is defined but not implemented.
- **Golden config trees without compliance plans:** Document the structure but note there is no automated compliance enforcement.
- **Workflow descriptions and task summaries are the best source of business intent** — use them heavily.
- **Non-hex task IDs:** Task IDs like `apush` or `myTask` are a known bug pattern (`$var` references silently fail on these).
- **Static values as indicators:** Hard-coded strings in merge tasks or newVariable tasks often reveal business rules (e.g., `"value": "production"` → production-only path).
- **Missing error transitions:** Note any adapter tasks without error transitions — this is a quality gap in the existing implementation.

---

## Gotchas

- **Global assets are not access-restricted; projects are.** Global Automation Studio assets (the focus of this skill) are visible to any authenticated client — RBAC does not undercount the global catalog. The `/automation-studio/projects` list, however, **is** filtered by per-project ACL (every project must explicitly grant a user or group; there is no platform-wide admin or "all-projects" role). For documenting *globals*, this is mostly out of scope; if the engineer names a specific project they expect, route to `/project-to-spec` rather than declaring it absent.
- **NEVER produce JSON files as output.** Only markdown reports.
- **childJob `workflow` is the primary relationship link.** Don't trace `$var` references across workflows.
- **Naming prefix is a heuristic, not a rule.** Prioritize childJob graph over naming when they conflict.
- **OM automations can have multiple triggers.** Document all of them.
- **Not every asset connects.** Don't force them into groups — catalog in Shared Utilities or Reference.
- **When unsure about golden config or LCM relationships**, ask the engineer rather than guessing.
- **Master README is only for multiple use cases.** Single use case → write files directly in reports directory, no subdirectory, no README.
- **Task descriptions and summaries are the best source of intent** — use them heavily.

````

============================================================
FILE: .claude/skills/explore/SKILL.md
DIRECTORY: .claude/skills/explore/
FILENAME: SKILL.md
============================================================
SHA256: b28b89c08c831a9b4a29408d79809d81c3acfa262b34cdc350c2153dfd4acc61

````markdown
---
name: explore
description: Use this skill whenever someone wants to connect to an Itential platform and browse, inspect, or discover what's there — without starting a formal delivery. Trigger it for phrases like "connect to my platform", "show me what adapters are running", "authenticate and pull platform data", "I want to poke around before starting", "what workflows exist?", "give me an inventory of the platform", "browse capabilities freely", "check if adapter X is running", or "I just set up a new environment — show me what's there". Also use it for ad-hoc freestyle work where the user wants to build something directly without going through the full spec→design→build lifecycle.
---

# Explore

**Path:** Freeform — not part of the delivery lifecycle
**Owns:** Auth, environment discovery, freestyle skill use
**Use when:** You want to browse adapters, try tasks, build something experimental, or understand the platform before committing to a spec

---

## What This Does

Connects you to a platform, pulls everything needed to work freely, and routes you to the right skill for whatever you want to do.

```
/explore
    │
    ├── Auth (from env file or interactive)
    ├── Pull platform data
    ├── Summarize environment
    └── Use skills directly
```

---

## Step 1: Authenticate

Check for credentials in this order:
1. `{use-case}/.env` — use-case-specific
2. `${CLAUDE_PLUGIN_ROOT}/environments/*.env` — pre-configured environments at repo root

If found, authenticate automatically. If not, ask:
1. Platform URL
2. Credentials (username/password or client_id/secret)

**Local Development (username/password):**
```
POST /login
Content-Type: application/json

{"username": "admin", "password": "admin"}
```
Returns a token string. Use as query parameter: `?token=TOKEN`

**Cloud / OAuth:**
```
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=client_credentials
```
Returns `{"access_token": "..."}`. Use as Bearer header.

Save to `.auth.json`:
```json
{
  "platform_url": "https://...",
  "auth_method": "oauth",
  "token": "eyJhbG...",
  "timestamp": "2026-03-25T10:00:00Z"
}
```

---

## Step 2: Pull Platform Data

Run in two groups. Do not run all in one parallel batch — if one fails, parallel cancellation kills the others.

**Group 1 (core — run in parallel):**
```bash
curl -s "{BASE}/help/openapi?url={ENCODED_BASE}&token=TOKEN" > {use-case}/openapi.json
curl -s "{BASE}/workflow_builder/tasks/list?token=TOKEN"     > {use-case}/tasks.json
curl -s "{BASE}/automation-studio/apps/list?token=TOKEN"    > {use-case}/apps.json
curl -s "{BASE}/health/adapters?token=TOKEN"                > {use-case}/adapters.json
curl -s "{BASE}/health/applications?token=TOKEN"            > {use-case}/applications.json
```

**Group 2 (environment-specific — run in parallel after Group 1):**

Devices (note: POST, not GET):
```bash
curl -s -w "\n%{http_code}" -X POST "{BASE}/configuration_manager/devices?token=TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"options":{"start":0,"limit":1000,"sort":[{"name":1}],"order":"ascending"}}' \
  > {use-case}/devices.json
```

Existing workflows:
```bash
curl -s "{BASE}/automation-studio/workflows?limit=500&token=TOKEN" > {use-case}/workflows.json
```

Before parsing any saved file, validate JSON:
```bash
jq type {use-case}/devices.json 2>/dev/null || echo "empty"
```
If invalid, treat as no data — don't block.

---

## Step 3: Present Summary

Show:
- Adapters: name, state, connection
- Apps: count, key platform apps running
- Tasks: count
- Devices: count and OS types (if available)
- Existing workflows: count

> **Visibility note:** Itential Automation Studio access control has two layers. **Project-scoped assets** (anything inside a named project) are gated by **per-project ACLs** — the calling client only sees projects whose ACL includes the client or one of its groups, and there is no platform-wide "admin" or "all-projects" role. **Global Automation Studio assets** (workflows, templates, etc. that live outside any project) are not access-restricted that way and are visible to any authenticated client. If the engineer expects a specific *project* (or any asset inside one) and it does not appear, treat it as *possibly access-restricted*, not *missing* — see the gotcha below. For global assets, absence is real absence.

---

## Step 3b: Initialize Memory File

After pulling platform data, check for `{use-case}/use-case-memory.md`:
- **Exists** → read it. It has context from a previous session — platform URL, prior decisions, open items.
- **Missing** → create it from `${CLAUDE_PLUGIN_ROOT}/helpers/use-case-memory.md`. Populate Platform URL, `Stage: requirements` (explore is freeform — set the real stage once the engineer commits to a delivery path), `Status: active`, and any adapter/app names discovered in Step 2.

---

## Step 4: Route to Skills

Point to the right skill for what the engineer wants to do:

| I want to... | Use |
|-------------|-----|
| Build workflows, templates, or projects | `/builder-agent` |
| Manage devices, backups, diffs | `/itential-devices` |
| Build compliance and golden config | `/itential-golden-config` |
| Build IAG services (Python, Ansible, OpenTofu) | `/iag` |
| Create AI agents | `/flowagent` |
| Manage lifecycle resources | `/itential-lcm` |
| Manage device inventories (IAG5) | `/itential-inventory` |

---

## Gotchas

- OAuth MUST use `Content-Type: application/x-www-form-urlencoded`, not JSON
- Tokens expire mid-session — re-authenticate silently from `.env` on auth errors
- OpenAPI spec is ~1.5MB — search locally with `jq`, never load into context
- `tasks/list` `app` field has WRONG casing for adapters — use `apps/list` for correct names
- Devices endpoint is POST not GET — body required
- **Project list responses are RBAC-filtered — absence in the project list does NOT mean the project doesn't exist.** Itential projects use per-project ACLs only: every project explicitly grants access to specific users or groups, and there is no platform-wide "admin" or "all-projects" role. If the engineer names a specific *project* (or any asset inside one) you can't find, say *"not visible to this client (`{client_id}`) — possibly access-restricted; ask the project owner (or someone with manage rights on that project) to add `{client_id}` to its ACL"* rather than *"doesn't exist"*. Never grant access to yourself — ask the engineer how to proceed. **Global Automation Studio assets** (anything outside a named project) are not access-restricted in the same way; for those, absence in the API response is real absence.
- `PATCH /automation-studio/projects/{id}` silently ignores an `accessControl` body — use the `members` array instead: `[{"type": "account"|"group", "reference": "<id>", "role": "owner"|"editor"|"operator"|"viewer"}]`. See [#62](https://github.com/itential/builder-skills/issues/62)

````

============================================================
FILE: .claude/skills/flowagent-to-spec/SKILL.md
DIRECTORY: .claude/skills/flowagent-to-spec/
FILENAME: SKILL.md
============================================================
SHA256: 78739912a95b9aebef994ecbf20676f03432b0b1bbc5c8c5db09875a83964e64

````markdown
---
name: flowagent-to-spec
description: Convert a FlowAgent into a deterministic workflow spec. Reads the agent definition, tools, and session history (Agent Project Service / Agent Session Manager APIs) to understand what the agent does, then produces a customer-spec.md that describes the same use case as structured, deterministic automation. Turns agentic → deterministic.
argument-hint: "[agent-name or agent-id]"
---

# FlowAgent to Spec

**Purpose:** Read a FlowAgent → produce a deterministic workflow spec
**Output:** `customer-spec.md` describing the same use case as deterministic automation
**Feeds into:** `/spec-agent` for refinement → `/solution-arch-agent` → `/builder-agent`

---

## The Core Idea

A FlowAgent proves a use case works. The LLM figured out which tools to call in what order to accomplish an objective. Now you want to productionize it — remove the LLM from the execution path and replace it with a deterministic workflow that does the same thing reliably every time.

```
FlowAgent (agentic)          →    Deterministic Workflow
─────────────────────              ────────────────────────
LLM decides what to call           Explicit task sequence
LLM interprets results             query/evaluation tasks
LLM handles errors                 error transitions
LLM formats output                 merge/makeData tasks
Non-deterministic                  Same result every run
```

The spec produced by this skill describes the deterministic equivalent — same outcome, no LLM in the loop.

**Note on the typed `inputSchema`:** an agent's `inputSchema` already declares its input contract as typed fields. This makes Step 3's "identify inputs" analysis mostly a lookup, not an inference — read the agent's `inputSchema` directly rather than reverse-engineering input variance across session objectives.

---

## Step 1: Read the Agent

Pull the agent definition:

```
GET /agent-project-service/agents/{agentId}
```

Or find it by name (no direct name-search endpoint — filter client-side):
```
GET /agent-project-service/agent-names/accessible
```

Extract:
- **`instructions`** — the system prompt; tells you the agent's purpose and constraints
- **`inputSchema`** — the declared, typed input contract (properties + required) — this is your starting point for the deterministic workflow's `inputSchema`, not something you need to infer from session history
- **`tools`** — array of `{referenceId, decoratorId?}` the agent can use. Resolve each `referenceId` via `GET /tools/{referenceId}` to get its name/description; if a `decoratorId` is present, fetch `GET /tools/decorators/{decoratorId}` too — the decorator's `toolInputSchema` is what the agent actually sends, not the tool's native schema
- **`provider`** — `{profile, model}` UUIDs (not needed for the spec, but useful context on which LLM ran it)
- **`operators`** — who could invoke this agent (informational, not usually spec-relevant)

The agent definition doesn't declare what platform identity its tool calls run as — if you need to know what permissions the agent's tool calls actually exercised, infer it from which adapters/apps the tools in `tools[]` touch.

Save to `{use-case}/agent-config.json`.

---

## Step 2: Read Session History

Pull completed sessions to understand what the agent actually did:

```
GET /agent-session-manager/sessions?filters=[{"field":"agentDefinitionId","value":"<agentId>"}]&sortBy=startedAt&sortOrder=desc&limit=20
```

For the most recent successful sessions for this agent:
```
GET /agent-session-manager/sessions/{sessionId}
```

From each session extract:
- **`inputs`** — what the session was started with (the typed inputs, matching the agent's `inputSchema` — no need to reverse-engineer these from free text)
- **`status`** — `COMPLETE` vs `FAILED` vs `CANCELED`; `errorMessage`/`errorCategory` on failure
- **`totalToolCallCount`** / **`iterationCount`** — how much work it did
- **`startedAt`** / **`endTime`** / **`duration`** — how long it took

Then read the session's activity log to see the actual tool call sequence:
```
GET /agent-session-manager/sessions/{sessionId}/messages?sortBy=timestamp&sortOrder=asc
```

Messages contain the full execution trace, now with a formal type taxonomy:
- `category: AGENT_REASONING` (`type: inference-succeeded`/`inference-failed`) — the LLM's reasoning and decisions (`text` field)
- `category: TOOL_CALLED` (`type: tool-execution`) — which tool, with what inputs/outputs (`data` field — fetch `GET .../messages/{eventId}` for the untruncated payload)
- `category: AGENT_STATUS` — lifecycle transitions (paused/resumed/completed/failed/canceled)

Save representative sessions to `{use-case}/session-samples.json`.

---

## Step 3: Analyze the Pattern

From the agent config and session messages, reconstruct the deterministic pattern.

### Identify the fixed sequence

Look across multiple sessions for the tool call pattern that repeats. The LLM may phrase its reasoning differently each time, but the underlying tool sequence is usually consistent:

```
Example from session messages (category: TOOL_CALLED):
  1. ServiceNow//getChangeRequest   (input: changeId)
  2. Infoblox//getHostRecord        (input: hostname)
  3. Infoblox//updateHostRecord     (input: hostname, ipv4addr)
  4. ServiceNow//updateChangeRequest (input: changeId, work_notes)
```
(Tool names here are shown resolved from `referenceId` via `GET /tools/{referenceId}` — the raw session message will reference the structured `referenceId`/`toolId` string (`<type>:<source>:<method>`, e.g. `adapter:Servicenow:ServiceNow:createChangeRequest`), not a plain readable name. Resolve every distinct tool call in the sequence before presenting it.)

This becomes your deterministic workflow task sequence.

### Identify the decision points

Where did the LLM branch? Look for:
- Sessions where different tools were called based on a condition
- `AGENT_REASONING` messages that say "since X is Y, I will call Z instead of W"
- Tool results that caused the agent to take a different path

Each branch point becomes an `evaluation` task in the deterministic workflow.

### Identify the data flow

For each tool call in the sequence:
- What inputs did it take? → these are incoming variables
- What outputs did it return? → these are outgoing variables that feed the next step
- Did the LLM extract a specific field? → that's a `query` task

### Identify error handling

Where did sessions fail (`status: FAILED`), and what did the agent do?
- Did it retry? → add retry logic or `revert` transitions
- Did it stop and report (`errorMessage`/`errorCategory`)? → add error transitions to `workflow_end`
- Did it create a ticket? → add a ServiceNow error-handling task

### Identify inputs and outputs

**Inputs:** Read the agent's `inputSchema` directly (Step 1) — agents already declare a typed input contract, so this is a lookup, not an inference. Cross-check against the `inputs` actually supplied across several sessions (Step 2) to confirm which declared properties are used in practice vs. rarely populated.

**Outputs:** What did the final `AGENT_REASONING` message (the session's concluding text) consistently report? These become the workflow `outputSchema`.

---

## Step 4: Map Agentic → Deterministic

Convert each observed agent behavior to a workflow construct:

| Agent behavior | Deterministic equivalent |
|----------------|--------------------------|
| Tool call | Adapter task |
| LLM extracts a field from tool result | `query` task |
| LLM decides which path to take | `evaluation` task |
| LLM builds a request body | `merge` task |
| LLM formats output | `makeData` or `renderJinjaTemplate` |
| LLM asks for approval | `ViewData` manual task |
| LLM calls multiple tools for each item in a list | `childJob` with `loopType: parallel` |
| LLM retries a failed call | `revert` transition |
| Agent conclusion | workflow `outputSchema` variables |

---

## Step 5: Produce `customer-spec.md`

Write the spec for the deterministic equivalent.

```markdown
# Use Case: {Derived from agent instructions and inputSchema}

> **Note:** This spec was derived from FlowAgent `{agentName}` ({agentId}).
> It describes the same use case as deterministic automation — no LLM in the execution path.
> Review the inferred phases and acceptance criteria before using as a delivery baseline.

## 1. Problem Statement
{Derived from agent system prompt — what problem was the agent solving?}

## 2. High-Level Flow
{Derived from the dominant tool call sequence across sessions}

## 3. Phases
{One phase per logical cluster of tool calls}

### Phase N: {Name}
{What happens, what tools are called, what conditions are checked}
Decision points: {list evaluation conditions observed}
Stop conditions: {when does this phase fail/stop?}

## 4. Key Design Decisions
{What choices did the agent consistently make? These become explicit design decisions}

Example:
- Always verified the change ticket existed before updating it
- Skipped DNS update if the IP hadn't changed
- Created a follow-up ticket if the primary action failed

## 5. Scope

**In scope (observed in sessions):**
{tools used, systems touched}

**Not in scope:**
{things the agent could theoretically do with its tools but didn't}

## 6. Risks & Mitigations
{Derived from session failures (status: FAILED) and error patterns}

## 7. Requirements

### Capabilities
| Capability | Required | Source |
|-----------|----------|--------|
| {e.g., Update DNS records} | Yes | Observed in all sessions |

### Integrations
| System | Purpose | Adapter Used |
|--------|---------|-------------|
| {e.g., ServiceNow} | Change tickets | Servicenow |

### Inputs (from agent's inputSchema)
| Variable | Type | Description |
|----------|------|-------------|
| {e.g., changeId} | string | ServiceNow change request ID |

## 8. Batch Strategy
{Did the agent loop over multiple items? If so, describe the pattern}

## 9. Acceptance Criteria
{Derived from session concluding messages and final tool states}
1. {e.g., DNS record updated and verified}
2. {e.g., Change ticket updated with work notes}
3. {e.g., Workflow completes within N seconds}
```

---

## Step 6: Present to Engineer

Show the spec with clear attribution — what was observed vs what was inferred:

**Observed (high confidence):**
- Tool call sequence that appeared in >80% of sessions
- The agent's declared `inputSchema` (already typed — not inferred)
- Output values the agent always reported in its final message

**Inferred (needs verification):**
- Business purpose (from `instructions` interpretation)
- Phase boundaries (grouping of tool calls)
- Error handling intent (from failed sessions)
- Acceptance criteria (from concluding-message patterns)

Ask the engineer:
1. "Does this correctly capture what the agent was doing?"
2. "Are there edge cases the agent handled that I should capture as phases?"
3. "The agent made these decisions dynamically — should the deterministic version always follow the dominant path, or do we need all branches?"
4. "What inputs should the workflow accept?"

Then offer next steps:
- **Refine and deliver** → hand to `/spec-agent` for requirements refinement → `/solution-arch-agent` → `/builder-agent`
- **Accept as-is** → hand directly to `/solution-arch-agent` with the approved spec

---

## Gotchas

**LLM verbosity ≠ complexity:** The agent may write long reasoning messages but the actual tool sequence is short. Focus on `TOOL_CALLED` messages, not the LLM's narrative (`AGENT_REASONING`).

**One-off sessions aren't reliable:** Look for the pattern across 5+ sessions. A single session may show unusual branching.

**Tool identity is a colon-separated `<type>:<source>:<method>` string.** E.g. `adapter:Servicenow:ServiceNow:createChangeRequest` (adapter instance + app type + method) or `application:ConfigurationManager:runCompliancePlan` (app + method). Resolve each `referenceId` via `GET /tools/{referenceId}` to confirm its exact name/description, and map the `<source>` segment(s) back to `app` (apps.json) and `adapter_id` (adapters.json) for the deterministic workflow.

**Decorators change what the agent actually sent.** If a tool reference has a `decoratorId`, the decorator's `toolInputSchema` — not the tool's native schema — is what the LLM populated. Fetch `GET /tools/decorators/{decoratorId}` to see the real, narrowed input contract the agent was working with.

**LLM error recovery:** The agent may retry tools on failure — that's agentic behavior that doesn't directly translate. In the deterministic version, use explicit error transitions and define the recovery path.

**Stateful reasoning:** If an `AGENT_REASONING` message said "I checked earlier and the device was reachable" — that's stateful context the LLM maintained. In the deterministic version, that check must be an explicit task that stores its result in a job variable.

**Sub-agents / delegation is not a supported field.** There's no way for an agent to call another agent by name in the Agent Project Service schemas. If session messages show what looks like delegation (a `sessionType: child` session, or tool calls that look like they're invoking another agent), treat each as its own candidate deterministic workflow and confirm with the engineer how the two were actually being orchestrated — don't assume a direct agent-to-agent call pattern exists.

````

============================================================
FILE: .claude/skills/flowagent/SKILL.md
DIRECTORY: .claude/skills/flowagent/
FILENAME: SKILL.md
============================================================
SHA256: e35fb862a6cd2118a724f5e665c59bfe1360fad43f85e5fa31444f9736e866f6

````markdown
---
name: flowagent
description: Create and run AI agents on the Itential Platform (Agent Project Service, Model Registry Service, Tools Service, Agent Session Manager). Agents use LLMs to autonomously call platform tools (adapters, workflows, IAG services) to complete objectives. Use when setting up agents, configuring LLM provider profiles, managing tools and decorators, or running/tracking agent sessions.
argument-hint: "[action or agent-name]"
---

# FlowAI - Agent Skills Guide

FlowAI lets you create AI agents that use LLMs (Anthropic, OpenAI, Google, Ollama, AWS Bedrock, Databricks, or platform-managed models) to autonomously operate the Itential Platform. Agents can call adapters, run workflows, and invoke IAG services — all driven by natural language instructions and a typed input contract.

**This skill documents six services**: **Agent Project Service** (projects + agents), **Model Registry Service** (LLM provider profiles + models), **Tools Service** (tools + decorators), **Agent Session Manager** (running and tracking agents), **Agent Execution Engine** (internal execution kernel — not called directly), and **Tool RPC** (tool-call execution tracking). Human-in-the-loop approval is handled by a separate WorkCenter Service — see Work Items in the API Reference below.

**Response schema caveat:** several endpoints (notably most of Agent Project Service and the Tools Service) declare their success response as a bare `{"type": "object"}` in the OpenAPI spec — the exact response field names are not formally typed. Where this skill states a response shape, it's inferred from request-body schemas, the project-bundle export format (which IS fully typed), or cross-referenced fields — not guessed. Treat every shape and JSON example below as a known-good working structure, not a guarantee that matches your platform version exactly.

## Verifying This Skill Against Your Platform

This skill is a map, not a substitute for checking the live API. Don't hardcode a field name or endpoint from memory when you can look it up in seconds:

- **Pull the real spec and search it locally.** `GET /help/openapi?url={ENCODED_BASE}` (or reuse an already-pulled `openapi.json`), then `jq '.paths["/agent-project-service/agents/{agentId}"]' openapi.json`. The services in this skill live under `/agent-project-service`, `/model-registry-service`, `/tools`, `/agent-session-manager`, `/tool-rpc`, and `/work-center-service` — filter on those base paths.
- **Get a tool's live schema instead of assuming it.** `GET /tools/{referenceId}` always returns that tool's current `inputSchema` exactly as the LLM sees it — adapters and app methods change independently of this skill, so this call is the one source that's always current.
- **When the OpenAPI spec itself is untyped, call the endpoint and read the real response** rather than trusting a shape in this skill as final — every response shape documented below was built that way, and your platform version may have moved on.
- **Prefer real exported structures over hand-authored JSON.** `GET /agent-project-service/project-bundles/{projId}/export` on any existing project returns a complete, valid Agent + Project payload straight from the platform — exporting something that already works and reading it is faster and more reliable than composing a bundle from memory. Two ready-made local references follow the same idea:
  - `helpers/create/create-flowagent-project-bundle.json` — a structurally-correct starting template with `REPLACE_*` placeholders. Edit and import it rather than typing a bundle out from scratch.
  - `helpers/assets/flowagent-sample-agent-project.json` — a real project bundle, exported after building and running it against a live platform: one project with three agents, including a multi-tool agent that calls a device command, opens a ServiceNow incident through a decorated tool, and presents a WorkCenter approval step. It's exact platform data, not a hand-written example — but it's still one specific environment's snapshot: its `referenceId`s, `decoratorId`, and `provider` names won't exist on your platform verbatim. Read it to see the real shape (in particular, how `{{ deviceName }}` in `instructions` lines up with `inputSchema`, and how `tools[].decoratorId` attaches), then re-resolve every ID against your own `GET /tools` and `GET /model-registry-service/profiles` before reusing it.

## Concepts

- **Project** — the top-level container that owns agents. GBAC-controlled (`owner`/`editor`/`viewer` roles via `members`). Agents cannot exist outside a project. Supports portable bundle import/export.
- **Agent** — a named AI entity: `instructions` (system prompt), a typed `inputSchema` (what parameters it accepts), a `provider` reference (which LLM profile + model it uses), a `tools` list, and an `operators` access list.
- **Profile** — a configured, credentialed instance of an LLM provider (e.g., "Production Anthropic"). Owned by Model Registry Service. Holds masked credentials and a curated list of enabled models, each with its own UUID.
- **Model** — one specific model enabled on a profile (e.g., a Claude or GPT model), addressed by a UUID assigned when it's added to the profile. An agent's `provider` field is `{profile: <uuid>, model: <uuid>}` — both required together.
- **Tool** — a callable platform capability (adapter method, IAG service, app method), addressed by a structured `referenceId` (`<type>:<source>:<method>`, e.g. `application:ConfigurationManager:runCompliancePlan`). Discovered via `POST /tools/discover`, never created by hand.
- **Decorator** — a standalone, ID-addressed override of a tool's description and input schema for a specific use case. Cloneable and portable (bulk export/import). An agent attaches a decorator to a specific tool reference, not globally.
- **Session** — a single run of an agent. Has an 8-state lifecycle (`PENDING` → `RUNNING` → `COMPLETE`/`FAILED`/`CANCELED`, plus `PAUSING`/`PAUSED`/`CANCELING`) and a typed activity log (`messages`).
- **Operators** — an agent-level access-control list (account/group IDs) granting specific callers the right to run that agent, independent of their project role. Only project owners can edit it.
- **Builder Groups** — a profile-level access-control list controlling which groups can build agents against a given LLM profile.
- **Work Item** — a human-in-the-loop task, created when an agent calls a `view`-type tool (e.g. `view:WorkCenter:QuickForm`). Lives in a separate WorkCenter Service (`/work-center-service/*`), not the Tools Service. The agent's tool call sits at `status: "pending"` until a person completes the work item.

## Gotchas

- **`inputSchema` only allows `string`/`number` property types**, requires `additionalProperties: false`, and validates session `inputs` at start time — a session start with inputs that don't match returns a validation error, not a soft failure inside the agent run.
- **Every declared `inputSchema` property MUST be used in `instructions`.** `instructions` isn't just a static system prompt — it's a template, and `inputSchema` properties are substituted into it as `{{ propertyName }}` at session-start time. Declaring a property and never referencing it fails agent create/update with `"'<name>' is defined in schema but not used in template"`.
- **Agent create vs. update field asymmetry:** `instructions`/`inputSchema` are top-level on create, but nested under `prompt` on `PATCH`. Tool changes are a full array on create (`tools`) but deltas on update (`addTools`/`removeTools`/`decorateTools`/`authorizeTools`).
- **`provider.profile` and `provider.model` are two separate UUIDs, both required together** (`additionalProperties: false` — no inline API key, temperature, or other override at the agent level; all of that lives on the Profile).
- **Profile credentials are always masked on read** (`credential.masked: true`) — there's no way to retrieve a saved secret via the API, by design.
- **Provider type is immutable on a profile once created.** To switch providers, create a new profile and repoint agents at it — `GET /model-registry-service/profiles/{id}/agent-impact` first to see what breaks.
- **Deleting a profile is irreversible (hard delete)** — always check `agent-impact` first.
- **Deleting a project cascades to every agent inside it** — no soft-delete/recovery.
- **Updating an agent's `operators` requires the owner GBAC role**, even though other agent fields only need editor — a common source of unexpected 403s.
- **`operators` grants operate-access only — it does not configure what identity the agent's tool calls run as.** That's a separate concern, not set on the agent definition itself.
- **Decorators replace the ENTIRE tool input schema**, not just the fields you specify. Omitting a required field means the agent will never send it, and the underlying adapter call fails with a schema validation error. Always test the tool directly first to enumerate every required field.
- **`agentSnapshot` on a session is frozen at session-start time.** Editing the agent afterward does not change what an already-running or already-completed session executed.
- **Tool execution is asynchronous and externalized internally**, but a fast tool call still completes and shows up fully resolved in `messages` within seconds in practice — the async/receipt pattern is an internal implementation detail, not something that makes results harder to read via the session API. If a session does seem stuck mid-tool-call, check `GET /tool-rpc/executions?status=running`.
- **Generic WorkFlowEngine utility tasks (merge, query, getTime, etc.) are not discoverable as tools.** `POST /tools/discover` only registers adapter methods, app methods, workflows, and IAG gateway services — a task existing in `tasks.json` doesn't mean it's addressable as a tool `referenceId`. If you need simple platform-level info, look for it via an app method (e.g., `application:ConfigurationManager:*`) instead.
- **No bulk session delete.** You must delete sessions one at a time.
- **No documented ad-hoc/ephemeral agent capability.** Every session-start path requires a saved `agentDefinitionId` — there is no "run this agent definition once without saving it" endpoint.
- **`run-agent`'s HTTP response is not the final answer** — it returns `{sessionId, status}` immediately just like plain `sessions` start. The "wait for the result" behavior only happens through the `terminationCallbackSignature` mechanism at the workflow-engine layer, not by blocking the HTTP call.
- **Most Agent Project Service and Tools Service responses are untyped in the OpenAPI spec** (`{"type":"object"}`). Verify exact field names against a live call before hardcoding a `$var` path in a workflow task.
- **A session stuck in `RUNNING` may just be waiting on a human.** The session's own `status` never enters a distinct "awaiting input" state — check `GET /work-center-service/work-items?rootExecutionId=<sessionId>` before assuming it's stuck. See Work Items below.

### Quick fixes for common problems

| Problem | Cause | Fix |
|---------|-------|-----|
| Tool execution fails | Wrong parameters | Test the tool directly (see Tools below), check openapi for correct inputs, update `instructions` or add a decorator |
| Agent calls wrong tool | Unclear objective | Be more specific in `instructions` about what to do and when |
| Agent loops (`iterationCount` high) | Too many tools or vague instructions | Reduce the `tools` array, add step-by-step guidance in `instructions` |
| Session input validation error | Inputs don't match `inputSchema` | Check `required`/`properties`/`additionalProperties` — only `string`/`number` types allowed |
| Agent create/update rejected: "defined in schema but not used in template" | An `inputSchema` property isn't referenced in `instructions` | Add `{{ propertyName }}` somewhere in `instructions`, or remove the unused property |
| Agent doesn't use a tool | Tool not in `tools` array or instructions don't mention it | Add the tool's `referenceId`, mention it by purpose in `instructions` |
| Session stuck in `PENDING`/`RUNNING` | Long-running tool call, a stuck external tool executor, or a pending human-in-the-loop task | Check `GET /work-center-service/work-items?rootExecutionId=<sessionId>` before assuming it's stuck; if genuinely stuck, `POST /agent-session-manager/sessions/{sessionId}` with `{"action":"CANCEL"}` |
| High token usage | Agent is exploring too many options | Constrain with "use ONLY these tools, in this order" in `instructions` |

---

## API Reference

### Projects (Agent Project Service)

**Base path:** `/agent-project-service`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/agent-project-service/projects` | List projects (`limit`, `skip`, `sort`: name\|created\|lastUpdated, `order`: 1\|-1, `search`) |
| POST | `/agent-project-service/projects` | Create a project |
| GET | `/agent-project-service/projects/{projId}` | Get a project (`projId` = UUID `_id` or integer `iid`) |
| PATCH | `/agent-project-service/projects/{projId}` | Update name/description/members |
| DELETE | `/agent-project-service/projects/{projId}` | Delete a project **and all agents within it** — requires owner role |
| GET | `/agent-project-service/admin/projects` | Admin: list all projects, bypassing GBAC |
| PATCH / DELETE | `/agent-project-service/admin/projects/{projId}` | Admin: update/delete any project, bypassing GBAC |

**Create:**
```json
{ "name": "Network Operations", "description": "..." }
```
`name`: 1–100 chars, no leading/trailing whitespace. `description`: max 500 chars. Creator defaults to sole `owner`.

**Update membership:**
```json
{
  "members": [
    { "type": "account", "reference": "<24-char-hex-account-id>", "role": "owner" },
    { "type": "group", "reference": "<24-char-hex-group-id>", "role": "editor" }
  ]
}
```
Roles: `owner` | `editor` | `viewer`. **Only owners can update `members`.** This is a full field replacement per the PATCH body shape (only send what you're changing — `name`, `description`, `members` are each independently optional, but if you send `members` at all, send the complete list).

### Project Bundles (Import/Export) — the preferred way to create a project + agents together

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/agent-project-service/project-bundles/{projId}/export` | Export a project and all its agents as a portable bundle |
| POST | `/agent-project-service/project-bundles/import` | Import a bundle to create (or merge into) a project |

**Prefer this over individual `POST /projects` + `POST /projects/{projId}/agents` calls** when creating a project with one or more agents — same rationale as Automation Studio's project import: build the whole thing locally, import atomically, avoid multi-call intermediate state.

**Bundle shape** (`agentProjectBundleVersion: 1`):
```json
{
  "_id": "<project-uuid>",
  "name": "NERC Compliance",
  "description": "Runs NERC-CIP compliance plan, collects device violations, ...",
  "agentProjectBundleVersion": 1,
  "created": "2026-07-01T13:59:16.070Z",
  "createdBy": { "provenance": "CloudAAA", "username": "joksan.flores@itential.com" },
  "agents": [
    {
      "_id": "<agent-uuid>",
      "name": "NERC CIP Compliance",
      "description": "",
      "instructions": "You are a NERC-CIP compliance automation engineer...",
      "inputSchema": {
        "type": "object",
        "additionalProperties": false,
        "required": ["device"],
        "properties": { "device": { "type": "string" } }
      },
      "created": "2026-07-01T14:09:15.000Z",
      "createdBy": { "username": "joksan.flores@itential.com", "provenance": "CloudAAA" },
      "provider": { "profileName": "anthropic-selab-gw", "modelName": "claude-sonnet-4-6" },
      "tools": [
        { "referenceId": "application:ConfigurationManager:runCompliancePlan", "lastKnownName": "runCompliancePlan", "decoratorId": "6a453e7b025a4623ad3df433" },
        { "referenceId": "application:ConfigurationManager:searchCompliancePlanInstances", "lastKnownName": "searchCompliancePlanInstances" },
        { "referenceId": "adapter:Servicenow:ServiceNow:createChangeRequest", "lastKnownName": "createChangeRequest", "decoratorId": "6a4522569c7614ba882f176c" },
        { "referenceId": "gatewayService:selab-iag5-standalone:04a19e29-f2dc-41f7-b9c7-102e6b19df08", "lastKnownName": "sleep-and-echo" }
      ]
    }
  ]
}
```

`provider` is de-identified on export to `{profileName, modelName}` strings (not the live UUIDs) — portable across environments where those UUIDs would differ. `agents[]` supports multiple agents per project. `tools[].decoratorId` is present only on entries that have one attached.

**Import:**
```
POST /agent-project-service/project-bundles/import
```
```json
{
  "bundle": { "...same shape as export, agentProjectBundleVersion: 1..." },
  "conflictMode": "keep-both",
  "name": "Network Operations",
  "description": "optional override of the bundle's project name/description",
  "providerResolutions": {
    "<agent identifier from the bundle>": { "profileName": "Production Anthropic", "modelName": "claude-sonnet-4-6" }
  }
}
```
`conflictMode`: `keep-both` (duplicate) | `replace` (overwrite an existing project/agent with matching identity). `providerResolutions` remaps each agent's `profileName`/`modelName` to a profile/model that actually exists in the **target** environment — required because profiles are environment-specific (different credentials per environment) even though the bundle references them by portable name. **The named profile/model must already exist in the target environment before import** — bundle import does not create profiles.

### Agents (Agent Project Service)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/agent-project-service/projects/{projId}/agents` | Create an agent inside a project |
| DELETE | `/agent-project-service/projects/{projId}/agents/{agentId}` | Delete an agent |
| GET | `/agent-project-service/agents/{agentId}` | Get an agent (flat path — not project-nested) |
| PATCH | `/agent-project-service/agents/{agentId}` | Update an agent |
| GET | `/agent-project-service/operable-agents` | Paginated list of agents the caller can run (project role OR `operators` membership) |
| GET | `/agent-project-service/operable-agents/{agentId}` | Single operable agent |
| GET | `/agent-project-service/agent-names/accessible` | Minimal names of agents visible under read/write/manage GBAC; filterable by `modelId`, `toolReferenceId`, `projUUID`, `access` |
| GET | `/agent-project-service/agent-names/operable` | Minimal `{name, _id, project}` for every agent the caller can operate (unpaginated) |

**There is no endpoint to list all agents within one project** — use `agent-names/accessible?projUUID=<uuid>` instead.

**Create (full body):**
```json
{
  "name": "network-ops-agent",
  "description": "...",
  "instructions": "...",
  "inputSchema": {
    "type": "object", "additionalProperties": false,
    "required": ["deviceName"],
    "properties": { "deviceName": { "type": "string" } }
  },
  "provider": { "profile": "<uuid>", "model": "<uuid>" },
  "tools": [
    { "referenceId": "string", "decoratorId": "<24-hex, optional>", "lastKnownName": "string, optional" }
  ],
  "operators": ["<24-hex-account-or-group-id>"]
}
```
`tools[].referenceId` is the only required field per tool entry. `provider` requires both `profile` and `model` together if present — `additionalProperties: false` (no inline API keys or temperature here; those live on the Profile).

**Writing `instructions` and `inputSchema`:**

`instructions` is a single string (not a chat array) — tell the agent WHO it is and HOW to work: its role, what tools are available and when to use each, expected output format, and constraints (read-only, require approval, etc.).

`inputSchema` is a strict, flat contract for what a caller must supply when starting a session — only `string`/`number` property types are allowed, `additionalProperties` must be `false`, and `required` lists which of the declared properties are mandatory:
```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["deviceName"],
  "properties": {
    "deviceName": { "type": "string" },
    "priority": { "type": "string" }
  }
}
```
This is a real function-signature-style contract now, not a free-form context bag — the platform validates session inputs against it.

**CRITICAL — every declared `inputSchema` property MUST appear as a `{{ propertyName }}` template variable somewhere in `instructions`.** `instructions` isn't just a static system prompt — it's a template, and `inputSchema` properties are substituted into it at session-start time. Declaring a property that isn't referenced fails agent create/update with: *"'&lt;name&gt;' is defined in schema but not used in template"*. A session's `agentSnapshot.instructions` shows the **post-substitution** text — e.g. a schema property `count` referenced as `{{ count }}` in the instructions becomes the literal value (`3`) in the snapshot once a session starts with `inputs: {count: 3}`. Declare a property only if you actually reference it with `{{ }}` somewhere in `instructions`.

**Update — note the shape differs from create:**
```json
{
  "name": "string, optional",
  "description": "string, optional",
  "prompt": { "instructions": "string", "inputSchema": { "...same strict schema..." } },
  "provider": { "profile": "<uuid>", "model": "<uuid>" },
  "addTools": [{ "referenceId": "string", "decoratorId": "<24-hex, optional>" }],
  "decorateTools": [{ "referenceId": "string", "decoratorId": "<24-hex-or-null>" }],
  "authorizeTools": [{ "referenceId": "string" }],
  "removeTools": [{ "referenceId": "string" }],
  "operators": ["<24-hex-id>"]
}
```
- `instructions`/`inputSchema` are top-level on **create** but nested under `prompt` on **update** — an intentional API asymmetry, not a typo.
- Tool changes on update are **deltas**, not a full-array replace: `addTools`, `removeTools`, `decorateTools` (attach/detach/change a decorator on an existing reference — `decoratorId: null` clears it), and `authorizeTools` (marks a tool reference as explicitly authorized — exact semantics not documented beyond the field name; verify against your platform before relying on it for anything security-sensitive).
- **Updating `operators` requires the owner GBAC role** on the parent project, even though other agent edits only need editor.

**`operators` — what it actually is:** a direct, agent-level access grant (array of 24-hex account/group IDs) letting those specific callers *operate* (run) this one agent, independent of their project role. It's additive to project GBAC, not a replacement — a project editor/owner can already operate every agent in the project; `operators` extends operate-access to accounts that otherwise wouldn't have it. This does not control what identity the agent's own tool calls run as — that's a separate concern not configured on the agent definition itself.

### Providers and Profiles (Model Registry Service)

**Base path:** `/model-registry-service`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/model-registry-service/providers` | List supported provider types (read-only catalog — cannot create/edit/delete) |
| GET | `/model-registry-service/providers/{providerId}` | Get one provider type's credential field requirements |
| POST | `/model-registry-service/providers/{providerId}/fetch-models` | Validate a credential and preview its available models |
| GET | `/model-registry-service/profiles` | List profiles (`search`, `provider`, `sortBy`: name\|provider\|agentCount\|createdAt, `sortDir`, `page`, `pageSize`) |
| POST | `/model-registry-service/profiles` | Create a profile |
| GET | `/model-registry-service/profiles/{id}` | Get a profile (credentials always masked) |
| PATCH | `/model-registry-service/profiles/{id}` | Update a profile (provider type is immutable) |
| DELETE | `/model-registry-service/profiles/{id}` | Hard-delete a profile |
| GET | `/model-registry-service/profiles/{id}/agent-impact` | List agents that will break if this profile is deleted |
| GET | `/model-registry-service/gateways` | List GatewayManager clusters available for `category: "gateway"` profiles |

**Provider type IDs observed in the credential union:** `openai`, `anthropic`, `google`, `ollama`, `bedrock`, `bedrock-proxy`, `databricks`, `gateway-manager`, plus `managed` (platform-hosted, no credential). **There is no distinct `azure-openai` provider ID** — reach Azure OpenAI via `provider: "openai"` with `credential.baseURL` pointed at your Azure endpoint, or via gateway/proxy routing. Always confirm against `GET /providers` on your actual deployment before assuming an ID exists.

**Create a profile — three categories, discriminated by `category`:**

`"direct"` (you supply the credential straight to the provider):
```json
{
  "profile": {
    "category": "direct",
    "name": "Production Anthropic",
    "provider": "anthropic",
    "credential": { "type": "anthropic", "apiKey": "sk-ant-..." },
    "models": [{ "name": "claude-opus-4-6-20260201" }],
    "builderGroups": []
  }
}
```

`"gateway"` (routed through a GatewayManager cluster — adds a required `gatewayCluster`):
```json
{
  "profile": {
    "category": "gateway",
    "name": "Gateway-Routed Bedrock",
    "provider": "bedrock",
    "gatewayCluster": "<cluster-id-from-GET-gateways>",
    "credential": { "type": "bedrock", "config": { "region": "us-east-1", "accessKeyId": "...", "secretAccessKey": "..." } },
    "models": [{ "name": "anthropic.claude-3-5-sonnet-20241022-v2:0" }],
    "builderGroups": []
  }
}
```

`"managed"` (platform-hosted, no credential at all):
```json
{
  "profile": {
    "category": "managed",
    "name": "Platform-Managed Model",
    "provider": "<provider-id-with-managedModels>",
    "models": [{ "name": "<must-match-one-of-provider.managedModels[].name>" }],
    "builderGroups": []
  }
}
```

**Credential shapes by type:**

| `type` | Required | Optional |
|---|---|---|
| `openai` | `apiKey` | `baseURL` |
| `anthropic` | `apiKey` | `baseURL` |
| `google` | `apiKey` | — |
| `ollama` | *(none)* | `baseURL` |
| `bedrock` | `config.region`, `config.accessKeyId`, `config.secretAccessKey` | `config.iamRole` |
| `bedrock-proxy` | `config.serviceUrl`, `config.tokenUrl`, `config.clientId`, `config.clientSecret` | — |
| `databricks` | `config.type` (const `"oauth-m2m"`), `config.host`, `config.clientId`, `config.clientSecret` | — |
| `gateway-manager` | `config.clusterId`, `config.backendProvider`, `config.credential` | `config.properties` |

**Response (create/get):**
```json
{
  "id": "<profile-uuid>",
  "name": "Production Anthropic",
  "provider": "anthropic",
  "credential": { "type": "api-key", "masked": true, "baseUrl": "..." },
  "models": [
    { "id": "<model-uuid>", "name": "claude-opus-4-6-20260201", "enabled": true, "status": "active" }
  ],
  "builderGroups": [],
  "agentCount": 0,
  "createdAt": "...", "updatedAt": "...", "createdBy": "...", "updatedBy": "..."
}
```
`credential.masked` is always `true` on read — the actual secret is never echoed back. **`models[].id` is the UUID you use as an agent's `provider.model`; `id` (top level) is `provider.profile`.**

**Update:** wrapped in `{"update": {...}}`, all fields optional. Provider type cannot change. `models[]` items on update require both `name` and `enabled` (unlike create, which only requires `name`).

**Before deleting a profile**, always check impact first:
```
GET /model-registry-service/profiles/{id}/agent-impact
→ { "affectedAgents": [{ "id", "name", "modelId", "modelName" }] }
```

**Discover models for a credential before saving it:**
```
POST /model-registry-service/providers/{providerId}/fetch-models
```
```json
{ "credential": { "type": "anthropic", "apiKey": "sk-ant-..." } }
```
or, to refresh using an already-saved profile's credential:
```json
{ "profileId": "<existing-profile-uuid>" }
```
Response: `{ "success": true, "models": [{ "id", "name", "enabled", "status" }], "retrievedAt": "..." }`. **These `models[].id` values are provider-native, not registry UUIDs** — use `models[].name` to populate a profile's `models` array; the registry assigns a new UUID once the model is actually saved into a profile.

**Related read-through view for agent authoring** (`/agent-project-service/profiles`, `/agent-project-service/profiles/{profileId}`) — GBAC-scoped proxy onto the same profiles, used when wiring an agent so the UI only shows profiles the current user is allowed to use. Same profile `id`/UUID either way.

### Tools

**Base path:** `/tools`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tools` | Search tools (see query params below) |
| GET | `/tools/{referenceId}` | Get a single tool |
| POST | `/tools/bulk` | Batch lookup by `referenceIds` |
| POST | `/tools/discover` | Scan the platform and register/refresh tools |

**`GET /tools` query parameters:** `skip`, `limit`, `type`, `name`, `referenceIds` (comma-separated), `description` (keyword), `active` (boolean), `parentIds`/`parentTypes`/`parentTitles` (comma-separated — tools can be hierarchical, e.g. children of an adapter instance), `excludeToolChildren` (top-level only), `sort` (`name`\|`type`\|`description`\|`source`\|`referenceId`), `order` (`asc`\|`desc`).

**Test a tool directly before wiring it to an agent.** Don't give an agent a tool you haven't tested yourself — every tool wraps a real platform API call, and if the direct call fails, the agent's call will too:
```bash
# Look up the tool's registry entry (schema/description the LLM will see)
GET /tools/{referenceId}

# Test the underlying endpoint directly — same as testing any platform call, independent of FlowAI:
# Adapter:     POST /ServiceNow/createChangeRequest   {"body": {...}}
# App:         POST /configuration_manager/getDevice  {"name": "IOS-CAT8KV-1"}
# IAG service: POST /gateway_manager/v1/gateways/{clusterId}/services/{serviceName}/run  {"params": {...}}
# Workflow:    POST /operations-manager/jobs/start     {"workflow": "...", "options": {...}}
```
Look up the exact route and request body from `openapi.json` (`jq '.paths | keys[] | select(contains("<adapter-or-app-name>"))' openapi.json`) the same way you would for any platform call — this doesn't depend on FlowAI at all. **If the tool's native schema is too broad or the LLM keeps sending wrong/incomplete inputs**, create a decorator (see Decorators below) — but only after confirming the native tool actually works when called correctly.

**Discover:**
```
POST /tools/discover
```
No body. Scans adapters, IAG services, and app methods, persisting each as a registry entry addressed by `referenceId`. Safe to re-run — refreshes the registry rather than duplicating entries.

**Tool identity — `referenceId` format:** a colon-separated `<type>:<source>:<method>` string. Observed `type` values: `application`, `adapter`, `gatewayService`, `workflow`, `integration`, `template`, `jsonForm`, `method` (a method belonging to a parent `application`/`adapter` entry — see `parentType`/`parentId`/`parentTitle` on the tool object):

| Type | Example `referenceId` | Structure |
|---|---|---|
| `application` | `application:ConfigurationManager:runCompliancePlan` | `application:<app-name>:<method>` |
| `adapter` | `adapter:Servicenow:ServiceNow:createChangeRequest` | `adapter:<adapter-instance-id>:<app-type-name>:<method>` |
| `gatewayService` | `gatewayService:selab-iag5-standalone:04a19e29-f2dc-41f7-b9c7-102e6b19df08` | `gatewayService:<cluster-id>:<service-uuid>` |
| `workflow` | `workflow:7473bb49-f317-4280-9d7a-9e4bd4969365` | `workflow:<workflow-uuid>` |
| `integration` | `integration:BECentral%3A2.3:BECentral23:getDevicesByTagId` | `integration:<instance-id-may-be-url-encoded>:<app-name>:<method>` |

**Tool object shape** (`GET /tools/{referenceId}`):
```json
{
  "_id": "<mongo-id>",
  "type": "method",
  "referenceId": "application:ConfigurationManager:getDevicesFiltered",
  "active": true,
  "checksum": "...",
  "description": "Gets a specific subset of devices for based on given options",
  "inputSchema": { "...full JSON Schema draft 2020-12, with real property definitions, enums, and examples..." },
  "lastUpdated": "...",
  "name": "getDevicesFiltered",
  "parentId": "ConfigurationManager",
  "parentInstance": null,
  "parentTitle": "ConfigurationManager",
  "parentType": "application"
}
```
`inputSchema` on a tool is a full, real JSON Schema (types, enums, patterns, examples) — this is what an LLM actually sees for that tool's parameters, and it's what a decorator's `toolInputSchema` replaces if one is attached.

There is **no create/update/delete for individual tools** — the registry is populated only by discovery.

### Decorators

**Base path:** `/tools/decorators`

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tools/decorators` | Create a decorator for a tool |
| GET | `/tools/decorators/{decoratorId}` | Get a decorator |
| DELETE | `/tools/decorators/{decoratorId}` | Delete a decorator |
| POST | `/tools/decorators/{decoratorId}/clone` | Clone a decorator (start from an existing one, adapt for a new team/agent) |
| GET | `/tools/decorators/bulk/export` | Export all decorators (paginated) |
| POST | `/tools/decorators/bulk/import` | Bulk-import decorators |
| GET | `/tools/{referenceId}/decorators` | List all decorators for one tool — a tool can have many |

`helpers/create/create-flowagent-decorator.json` is a ready-to-edit starting template for the body below.

**Create — required shape:**
```json
{
  "toolDecorator": {
    "referenceId": "<tool's referenceId>",
    "name": "<decorator name>",
    "description": "<what this decorator customizes and why>",
    "toolDescription": "<replacement description the LLM sees>",
    "toolInputSchema": { "...replacement JSON Schema..." }
  }
}
```
`referenceId`, `name`, `description`, `toolDescription`, `toolInputSchema` are all required. Response contains the generated `decoratorId` (24-char hex Mongo ObjectId), plus the full decorator record (`toolDescription`, `toolInputSchema` with `$schema` auto-added, `created`/`createdBy`/`lastUpdated`/`lastUpdatedBy`) — this response shape isn't in the OpenAPI spec, so treat the fields above as the reference.

**Example — narrowing a vague native schema:** `adapter:Servicenow:ServiceNow:createIncident`'s native `inputSchema` only declares `{body: {type: object}}`, with no field-level detail. An LLM working from that schema alone has no way to know `summary` and `short_description` are required, and the adapter rejects a call missing them: `"Schema validation failed on must have required property 'summary'"`. A decorator fixes this by declaring the fields explicitly:

```
POST /tools/decorators
```
```json
{
  "toolDecorator": {
    "referenceId": "adapter:Servicenow:ServiceNow:createIncident",
    "name": "create-incident-required-fields",
    "description": "Ensures summary and short_description are always included -- the native schema doesn't declare them.",
    "toolDescription": "Creates a ServiceNow incident. The body MUST include both 'summary' and 'short_description' -- omitting summary causes a schema validation error from the adapter. Include 'description' for full diagnostic detail.",
    "toolInputSchema": {
      "type": "object",
      "properties": {
        "body": {
          "type": "object",
          "properties": {
            "summary": { "type": "string", "description": "Required. Short one-line summary of the incident." },
            "short_description": { "type": "string", "description": "Required. Brief description shown in incident lists -- usually the same text as summary." },
            "description": { "type": "string", "description": "Full diagnostic detail." }
          },
          "required": ["summary", "short_description"]
        }
      },
      "required": ["body"]
    }
  }
}
```
**Response shape:**
```json
{
  "_id": "6a465ed52d79d885c63eb250",
  "toolDescription": "...",
  "toolInputSchema": { "note": "same shape as sent, with $schema auto-added" },
  "referenceId": "adapter:Servicenow:ServiceNow:createIncident",
  "name": "create-incident-required-fields",
  "description": "...",
  "created": "...",
  "createdBy": { "_id": "...", "username": "...", "provenance": "..." },
  "lastUpdated": "...",
  "lastUpdatedBy": { "_id": "...", "username": "...", "provenance": "..." }
}
```
`_id` is the `decoratorId`. Note the decorator only narrows `body`'s known properties (`summary`, `short_description`, `description`) — it doesn't set `additionalProperties: false`, so other real adapter fields the LLM already knows about (from training or context) can still pass through; only omit `additionalProperties: false` if you deliberately want to lock the schema down to exactly those fields.

**Two ways to attach it to an agent:**

1. **At agent creation** — include `decoratorId` directly in the `tools[]` entry:
```json
{ "tools": [{ "referenceId": "adapter:Servicenow:ServiceNow:createIncident", "decoratorId": "6a465ed52d79d885c63eb250" }] }
```

2. **On an existing agent** — `PATCH` with `decorateTools`:
```
PATCH /agent-project-service/agents/{agentId}
```
```json
{ "decorateTools": [{ "referenceId": "adapter:Servicenow:ServiceNow:createIncident", "decoratorId": "6a465ed52d79d885c63eb250" }] }
```
Decorators are looked up by ID when an agent runs, not embedded inline — the same decorator can be referenced by multiple agents, and `clone` lets you start from an existing decorator rather than hand-authoring overrides from scratch for a new team/use case.

**Effect:** with the decorator attached, `createIncident` produces a single `tool-execution` message with `status: "succeeded"` — the LLM has the exact required fields up front and doesn't need a failed first attempt to discover them.

**CRITICAL:** a decorator's `toolInputSchema` **replaces the entire schema the LLM sees** — any field you omit will never be sent by the agent, even if the underlying adapter requires it. Test the tool directly (see Tools above) to find every required field before writing the decorator.

**When to create a decorator (and when NOT to):** create one only when the tool's native schema is too broad and the LLM sends wrong/incomplete inputs despite good `instructions`, or when different teams need different required fields on the same tool. Skip it for read-only tools and skip it if fixing the `instructions` text alone solves the problem.

### Sessions (Agent Session Manager)

**Base path:** `/agent-session-manager`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/agent-session-manager/sessions` | List/search sessions |
| POST | `/agent-session-manager/sessions` | Start a session (async — fire and forget) |
| GET | `/agent-session-manager/sessions/{sessionId}` | Get one session's metadata |
| POST | `/agent-session-manager/sessions/{sessionId}` | Cancel / Pause / Resume a session |
| DELETE | `/agent-session-manager/sessions/{sessionId}` | Delete a session (per-session only — no bulk clear) |
| POST | `/agent-session-manager/sessions/run-agent` | Run an agent from inside an Itential workflow |
| GET | `/agent-session-manager/sessions/sources` | Distinct `trigger.source` values (UI filter helper) |
| GET | `/agent-session-manager/sessions/{sessionId}/messages` | Session activity log (paginated) |
| GET | `/agent-session-manager/sessions/{sessionId}/messages/{eventId}` | One event, untruncated |

**List — query parameters:** `filters` (array of field/operator/value), `offset`, `limit` (max 100), `sortBy` (`createdAt`\|`updatedAt`\|`startedAt`\|`status`\|`createdBy`\|`agentDefinitionId`), `sortOrder`.

**Session object** (`agentSnapshot.instructions` shows `{{ }}` template variables already substituted with the actual session `inputs`):
```json
{
  "sessionId": "string",
  "agentDefinitionId": "string",
  "agentSnapshot": { "_id": "...", "name": "...", "instructions": "... (template vars substituted) ...", "namespace": { "_id": "...", "name": "..." } },
  "status": "PENDING | RUNNING | PAUSING | PAUSED | COMPLETE | FAILED | CANCELING | CANCELED",
  "startedAt": "...", "endTime": "...", "durationMs": 0,
  "createdAt": "...", "createdBy": "<account-id>",
  "provider": "anthropic",
  "modelVersion": "claude-sonnet-4-6",
  "sessionType": "root | child",
  "trigger": { "type": "eventSystem|endpoint|schedule|manual|job|session", "name": "...", "source": "..." },
  "errorMessage": "...", "errorCategory": "...",
  "iterationCount": 0, "toolGroupCount": 0, "totalToolCallCount": 0,
  "totalInputTokens": 0, "totalOutputTokens": 0,
  "inputs": {}
}
```
`provider`/`modelVersion` are plain strings (provider id and model name) at the session level — not the `{profile, model}` UUID pair used on the agent itself. `agentSnapshot` is a copy of the agent's config **at session-start time** — updating the agent afterward does not retroactively change what a past session ran. `sessionType: child` implies sessions can spawn child sessions; the mechanism for that isn't exposed in this API slice — treat as informational unless you see it triggered from elsewhere.

**Start a session (async):**
```
POST /agent-session-manager/sessions
```
```json
{ "agentDefinitionId": "<agent-uuid>", "inputs": { "deviceName": "IOS-CAT8KV-1" } }
```
`inputs` must satisfy the agent's `inputSchema`. Response: `{ "sessionId": "...", "status": "..." }` — returns immediately, does not wait for completion. **`status` in the response was observed going straight to `RUNNING` in testing** — don't assume you'll always see `PENDING` first; poll and branch on the terminal states (`COMPLETE`/`FAILED`/`CANCELED`), not on catching a specific intermediate value.

**Cancel / Pause / Resume:**
```
POST /agent-session-manager/sessions/{sessionId}
```
```json
{ "action": "CANCEL", "canceledBy": "<username>", "correlationId": "<for tracing>" }
```
`action` is one of `CANCEL` | `PAUSE` | `RESUME`. Response: the full updated Session object.

**Delete:**
```
DELETE /agent-session-manager/sessions/{sessionId}
```
Per-session only — **there is no bulk "clear all sessions" endpoint**. To purge history, page through `GET /sessions` and delete individually.

**Run from a workflow:**
```
POST /agent-session-manager/sessions/run-agent
```
```json
{
  "agent": "<agent-uuid>",
  "inputs": { "deviceName": "IOS-CAT8KV-1" },
  "terminationCallbackSignature": {
    "location": "string", "serviceName": "string", "methodName": "string", "identifier": "string"
  }
}
```
Note the field is `agent`, not `agentDefinitionId`. `terminationCallbackSignature` is an IAP cog hook invoked when the session reaches a terminal state — **the calling workflow task stays "running" until then**, which is what makes this feel synchronous from the workflow's perspective, even though the HTTP response itself returns immediately with `{sessionId, status}`. The "wait" happens at the workflow-engine layer, not the HTTP layer — see "Using Agents in Workflows" below.

**Activity log:**
```
GET /agent-session-manager/sessions/{sessionId}/messages?sortBy=timestamp&sortOrder=asc
```
Each message: `{ sessionId, eventId, timestamp, type, category, sequenceNumber?, text?, data }`.
- `type`: `inference-pending` | `inference-succeeded` | `inference-failed` | `tool-execution` | `agent-session-paused` | `agent-session-resumed` | `agent-session-completed` | `agent-session-failed` | `agent-session-canceled`
- `category`: `AGENT_REASONING` | `TOOL_CALLED` | `AGENT_STATUS`
- `sequenceNumber` is `null` on `tool-execution` and `AGENT_STATUS` messages — only `AGENT_REASONING` messages are sequenced.

**Real `data` shapes:** session messages return the actual resolved tool input/output inline, not just a store/receipt pointer — the receipt pattern described under Agent Execution Engine below is internal plumbing between the execution engine and its tool executor; it doesn't change what this endpoint returns.

`inference-succeeded`:
```json
{
  "durationMs": 2125,
  "stopReason": "tool_use | end_turn",
  "tokenUsage": { "inputTokens": 1055, "outputTokens": 73, "cacheReadTokens": 0, "cacheCreationTokens": 0 }
}
```
Sibling `text` field on the same message has the LLM's actual reasoning/response text.

`tool-execution`:
```json
{
  "toolGroupId": "<uuid>",
  "toolCallId": "toolu_...",
  "toolName": "getDevicesFiltered",
  "toolType": "method",
  "input": { "options": { "limit": 3 } },
  "isInputTruncated": false,
  "output": { "...the tool's actual return value..." },
  "isOutputTruncated": false,
  "durationMs": 764,
  "errorMessage": null, "errorCategory": null, "canceledBy": null,
  "outcomeEventId": "<eventId of the AGENT_REASONING message that follows>",
  "status": "succeeded"
}
```
`output` is the real, resolved tool result — inspect it directly rather than assuming you need `GET .../messages/{eventId}` to see it. `isInputTruncated`/`isOutputTruncated` flag when a large payload WAS truncated in this listing; fetch the single-event endpoint only in that case. A `view`-type tool call (see Work Items below) instead sits at `"status": "pending"` with `"output": null` until a person completes the corresponding work item.

### Work Items (WorkCenter Service)

**Base path:** `/work-center-service`

An agent can pause and wait for a real person to act, using a `view`-type tool. This is a different mechanism from a normal tool call:

**The tool:** `view:WorkCenter:QuickForm` (discovered and wired into an agent's `tools[]` exactly like any other tool). Its `inputSchema` fields:

| Field | Type | Required | Purpose |
|---|---|---|---|
| `quickFormData` | array | ✅ | The rows to render in the table |
| `columnDisplay` | `all` \| `allowlist` \| `denylist` | ✅ | Which columns appear |
| `columns` | array | | Column names to include/exclude (used with `allowlist`/`denylist`) |
| `actionColumnHeader` | string | ✅ | Display header for the action column |
| `actionColumnKey` | string | ✅ | Key used to annotate each row with the operator's input in the outgoing rows |
| `actionColumnType` | `dropdown` \| `text` \| `selection` | ✅ | Input control rendered per row |
| `actionColumnRequired` | boolean | ✅ | When `true`, Complete is disabled until every row is actioned |
| `actionColumnLabels` | array | | Dropdown options (required when `actionColumnType` is `dropdown`) |
| `actionColumnAllowMultiple` | boolean | | Allow multiple dropdown selections per row |

Example agent tool-call input (one summary row, dropdown acknowledgement):
```json
{
  "quickFormData": [
    { "device": "dc1-leaf1", "summary": "show version failed — unsupported device_type", "incidentNumber": "INC0012773" }
  ],
  "columnDisplay": "all",
  "actionColumnHeader": "Acknowledge",
  "actionColumnKey": "acknowledged",
  "actionColumnType": "dropdown",
  "actionColumnRequired": true,
  "actionColumnLabels": ["Acknowledged", "Needs Follow-up"]
}
```

**What actually happens when an agent calls it:**
1. The tool call's session message shows up with `"status": "pending"` and `"output": null` — it does not resolve on its own.
2. The session's own `status` stays `RUNNING` the whole time — there is no distinct "awaiting input" session state. Don't rely on session `status` alone to detect a HITL wait; check whether the latest `tool-execution` message has `status: "pending"`.
3. A real work item is created in a separate service — **WorkCenter Service** (`/work-center-service/*`), not the Tools Service or Agent Session Manager. This is a distinct application with its own API surface.

**Finding and completing the pending work item:**
```
GET /work-center-service/work-items?rootExecutionId=<sessionId>
```
Returns the pending item(s) for that session, including `id`, `status`, `view`, and the `execution`/`rootExecution` metadata linking it back to the session.

```
GET /work-center-service/work-items/{id}
GET /work-center-service/work-items/{id}/variables/incoming
```
Get the full item detail or just its incoming variables (what was passed to the `view` tool call — e.g., the `quickFormData` rows and column config).

**Complete it (this is what a human does by clicking "Complete" in the WorkCenter UI):**
```
PATCH /work-center-service/work-items/{id}/complete
```
```json
{
  "finishState": "completed",
  "variables": { "acknowledged": "Acknowledged" }
}
```
`variables` is a flat key-value object — the key matches `actionColumnKey` from the original QuickForm input, the value is one of `actionColumnLabels` (for a dropdown). **Method is `PATCH`, not `POST`** — a `POST` to this path returns a plain 404. Response is the completed work item (`status: "completed"`); the agent's session then resumes on its own and reaches `COMPLETE` shortly after.

**Other work-item lifecycle endpoints:**
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/work-center-service/work-items` | List (requires `rootExecutionId` query param) |
| POST | `/work-center-service/work-items/search` | Richer search (requires `sort.field`/`sort.order`) |
| GET | `/work-center-service/work-items/count` | Count matching items |
| POST | `/work-center-service/work-items/{id}/claim` | Claim ownership before acting |
| POST | `/work-center-service/work-items/{id}/release` | Release a claimed item back to the pool |
| POST | `/work-center-service/work-items/{id}/assign` | Assign to a specific operator |
| PATCH | `/work-center-service/work-items/{id}/complete` | Submit the operator's response and resolve the item |
| POST | `/work-center-service/work-items/cancel` / `/cancel-work-items` | Cancel one or more pending items |

**Design implication:** if an agent's `instructions` call for presenting something to a human before finishing, expect the session to sit `RUNNING` indefinitely (minutes to hours, however long the human takes) until someone completes the corresponding work item. Poll or watch WorkCenter, not just the session — a session "stuck" in `RUNNING` with a `pending` `tool-execution` message is working as intended, not failing. Not just `QuickForm` — any `view`-type tool (e.g. `view:WorkFlowEngine:ViewHTML`) follows the same pause/work-item/complete pattern, and an agent can call more than one in sequence, each producing its own work item.

### Tool Executions (Tool RPC — observability only)

**Base path:** `/tool-rpc`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tool-rpc/executions` | Search tool executions (`status`: `running`\|`complete`, paginated) |
| GET | `/tool-rpc/executions/{toolExecutionId}` | Get one tool execution's full detail |

Read-only. This is where to look up the outcome of one specific tool call an agent made, without paging through the session's full message log. Response: `{ skip, limit, total, results: [...] }` for the list; a single untyped object for the detail call.

### Agent Execution Engine (internal — do not call directly)

**Base path:** `/agent_execution_engine`. Scoped `AgentExecutionEngine.admin` only — no operator/builder role exists for it. Normal users and workflows should always go through Agent Session Manager; the Execution Engine is the internal kernel Session Manager calls on your behalf. Documented here only so session behavior makes sense when debugging — **never wire a workflow task directly to `/agent_execution_engine/*`.**

**How a session actually runs, internally:**
1. Session Manager resolves `agentDefinitionId` → fetches instructions, provider/model, resolved+decorated tools from Agent Project Service and Model Registry Service.
2. Session Manager hands a fully-materialized definition to the Agent Execution Engine, which starts the inference loop.
3. The LLM decides which tool(s) to call based on the objective and `inputs`.
4. Tool execution happens **asynchronously and externally under the hood** — the engine dispatches a tool call, an external executor runs it and persists the result, then calls back into the engine with a receipt (the `handle-tool-response` callback pattern, tracked via Tool RPC). This is internal plumbing — the session's `messages` still show the actual resolved tool input/output directly, not the receipt, and a fast tool call is fully visible there within seconds.
5. The engine fetches the actual result and feeds it back to the LLM; repeats until the objective is met or an error occurs.
6. Every step is recorded as a typed session message; the session's `status` reaches a terminal state (`COMPLETE`/`FAILED`/`CANCELED`) — unless a `view`-type tool call is pending, in which case the session stays `RUNNING` until the corresponding work item is completed (see Work Items above).

---

## Using Agents in Workflows

Run an agent from inside an Itential workflow using the `run-agent` cog task, which uses the termination-callback pattern to make the workflow task wait for the session to finish:

```json
{
  "name": "runAgent",
  "app": "FlowAI",
  "type": "operation",
  "location": "Application",
  "variables": {
    "incoming": {
      "agent": "$var.job.agentId",
      "inputs": "$var.job.agentInputs"
    },
    "outgoing": {
      "sessionId": "$var.job.sessionId",
      "status": "$var.job.sessionStatus"
    }
  }
}
```

The exact task name and available FlowAI workflow tasks depend on what's registered as a `tools`-app on your platform — look it up with `jq '.[] | select(.app == "FlowAI")' tasks.json` before wiring, since task names may not map 1:1 to the raw REST operation names shown in this skill (`runAgent` above mirrors the `POST /agent-session-manager/sessions/run-agent` operation, but the literal task name is platform-specific — check your platform's `tasks.json`).

The task holds the workflow at that point until the session reaches a terminal state (`COMPLETE`/`FAILED`/`CANCELED`), then continues with the session's outcome available to downstream tasks — check `status` and branch accordingly (e.g., `evaluation` on `status == "FAILED"` to route to an error-handling path).

## Patterns

### Minimal agent (no tools, just LLM)
```json
{
  "name": "poet",
  "description": "writes poems",
  "instructions": "You are a poet. Write a haiku about the topic you're given.",
  "inputSchema": {
    "type": "object", "additionalProperties": false,
    "required": ["topic"],
    "properties": { "topic": { "type": "string" } }
  },
  "provider": { "profile": "<profile-uuid>", "model": "<model-uuid>" },
  "tools": [],
  "operators": []
}
```

### Agent with platform tools
```json
{
  "name": "device-checker",
  "description": "Checks device health using platform adapters",
  "instructions": "You check device health using the available tools. Use the exact device name given — do not guess or reformat it.",
  "inputSchema": {
    "type": "object", "additionalProperties": false,
    "required": ["deviceName"],
    "properties": { "deviceName": { "type": "string" } }
  },
  "provider": { "profile": "<profile-uuid>", "model": "<model-uuid>" },
  "tools": [{ "referenceId": "<referenceId-for-AutomationGateway-sendCommand>" }],
  "operators": []
}
```

**Agent-to-agent delegation is not supported.** There is no field in the Agent Project Service schemas for one agent to call another by name. If you need one agent's output to feed another, orchestrate it at the workflow level instead — run one agent's session, wait for its result via `run-agent`'s termination callback, then start the next session with that result as part of its `inputs`.

## Developer Scenarios

### 1. Set up from scratch

Before building, decide: what should the agent accomplish, what external systems does it need to touch, what inputs will vary between runs (→ `inputSchema`), does it need to make changes or just gather information, which project should own it, and who needs to be able to run it (`operators`) vs. edit it (project `members`).

```bash
# Discover platform tools into the Tools Service registry (idempotent — safe to re-run)
POST /tools/discover

# Pull the tool list locally (paginated — use skip/limit) and search by keyword
GET /tools?limit=200 > tools.json
GET /tools?skip=200&limit=200 >> tools.json   # repeat until fewer than `limit` returned
jq '.[] | select(.name | test("ServiceNow"; "i"))' tools.json

# Check what LLM provider profiles and provider types already exist
GET /model-registry-service/profiles
GET /model-registry-service/providers
```

```
1. POST /agent-project-service/projects                        → create (or reuse) a project — see Projects
2. GET  /model-registry-service/providers/{providerId}         → confirm credential fields — see Providers and Profiles
3. POST /model-registry-service/providers/{providerId}/fetch-models → validate credential, preview models
4. POST /model-registry-service/profiles                       → create the LLM profile, save profile+model UUIDs
5. POST /tools/discover                                        → scan platform for available tools (above)
6. GET  /tools                                                 → review what's available, note referenceIds
7. POST /agent-project-service/projects/{projId}/agents        → create agent with tools + instructions + inputSchema — see Agents
8. POST /agent-session-manager/sessions                        → run it — see Sessions
9. GET  /agent-session-manager/sessions/{id}                   → check status and results
```

**Prefer building the project + agent(s) locally and importing as one bundle** (`POST /agent-project-service/project-bundles/import`) once a project has more than one agent, or when replicating a known-good setup into a new environment — see Project Bundles above. The inline call sequence above is fine for a single quick agent in an existing project.

### 2. Debug a failed session
```
1. GET /agent-session-manager/sessions/{id}                → check status, errorMessage, errorCategory
2. Check iterationCount / totalToolCallCount / totalInputTokens+totalOutputTokens → looping or context exhaustion?
3. GET /agent-session-manager/sessions/{id}/messages       → find the failing tool-execution event
4. GET /agent-session-manager/sessions/{id}/messages/{eventId} → untruncated detail on that event
5. GET /tool-rpc/executions/{toolExecutionId}              → if the event references a stuck/failed tool execution
6. Test the tool directly (same endpoint the tool wraps) with the same parameters the agent used
7. PATCH the agent's instructions or add a decorator, then re-run the session with the same inputs
```
See **Gotchas → Quick fixes for common problems** above for a symptom → cause → fix lookup table.

### 3. Rotate or replace an LLM credential
```
1. GET  /model-registry-service/profiles/{id}/agent-impact  → see which agents use this profile
2. PATCH /model-registry-service/profiles/{id}              → update the credential (provider type stays fixed)
   { "update": { "credential": { "type": "anthropic", "apiKey": "<new-key>" } } }
3. No agent changes needed — agents reference the profile by UUID, not the credential directly
```

### 4. Add human-in-the-loop approval to an agent
```
1. Add a view-type tool reference (e.g. view:WorkCenter:QuickForm) to the agent's tools[] — same as any other tool
2. Reference it explicitly in instructions with the exact QuickForm inputSchema fields (quickFormData, actionColumnKey, actionColumnLabels, etc.)
3. Run the session — the QuickForm tool call sits at status: "pending"; session status stays RUNNING throughout
4. GET  /work-center-service/work-items?rootExecutionId=<sessionId>   → find the pending item
5. GET  /work-center-service/work-items/{id}/variables/incoming       → see exactly what was presented to the human
6. PATCH /work-center-service/work-items/{id}/complete                → resolve it; the session resumes and reaches a terminal state on its own
```
See **Work Items (WorkCenter Service)** above for the full field reference and lifecycle endpoints.

### 5. Fix a tool's schema with a decorator
```
1. Test the tool directly (see Tools → "Test a tool directly...") to find every field the underlying adapter actually requires
2. POST /tools/decorators with a toolInputSchema that covers every required field the native schema omits
3. Attach it: decoratorId in tools[] at agent creation, or PATCH .../agents/{agentId} with decorateTools on an existing agent
4. Re-run the same session inputs — the tool call should now succeed on the first attempt instead of failing and retrying
```
See **Decorators** above for the full worked example.

````

============================================================
FILE: .claude/skills/iag/SKILL.md
DIRECTORY: .claude/skills/iag/
FILENAME: SKILL.md
============================================================
SHA256: 65d3e8b6dc3d11c2699824e3a12b71e2cb34e58e2338dd9d0a1eefb1957a02a1

````markdown
---
name: iag
description: Build and run IAG (Itential Automation Gateway) services — Python scripts, Ansible playbooks, OpenTofu plans. YAML-driven service definitions, imported with iagctl. Call services from Itential workflows via GatewayManager.
argument-hint: "[action or service-name]"
---

# IAG — Itential Automation Gateway

IAG exposes Python scripts, Ansible playbooks, and OpenTofu plans as REST APIs. Everything is defined in YAML, imported with `iagctl db import`.

```
Write YAML → iagctl db import → Services available → Workflows call them
```

---

## Gotchas

- **`clusterId` must match** the IAG cluster config — discover with `GET /gateway_manager/v1/gateways/`
- **`params` maps to decorator schema** — check with `iagctl run service <type> <name> --use`
- **`inventory` is `""` (empty string)** when not targeting nodes, not `[]` or `null`
- **OpenTofu services require `action: apply|plan|destroy`** in the service YAML — field names are `vars` and `var-files` (NOT `plan-vars` / `plan-var-files`)
- **`runService` result is JSON-RPC wrapped** — extract with `query` path `result.stdout`, not `stdout`
- **`stdout` is always a string** — even when a Python script prints valid JSON, `result.stdout` is a string (e.g., `"{\"hostname\":\"Router1\"}"`). You must parse it before referencing fields inside it. Use a `parse` task (WorkFlowEngine) or `transformation` to convert the JSON string to an object.
- **`req-file` path is relative to `working-directory`** — if `working-directory: scripts`, then `req-file: requirements.txt` looks for `scripts/requirements.txt` inside the cloned repo, not the repo root
- **`$var` doesn't resolve inside `newVariable` objects** — use separate `query` tasks instead
- **Secrets in YAML files contain raw values** — prefer `iagctl create secret --prompt-value`. Keep `secrets:` out of `services.yaml` so `--force` never overwrites them.
- **Import is additive** — use `--force` to overwrite existing services
- **`--force` overwrites secrets too** — placeholder secrets replace real ones
- **Decorators reject unknown params** — every `--set` key must exist in the decorator schema
- **Validate first** — always run `iagctl db import file.yaml --validate` before importing
- **Ansible `network_cli` needs `paramiko` + `look_for_keys = False`** — add `paramiko` to `runtime.req-file` (requirements.txt), and in `ansible.cfg` add `[paramiko_connection]\nlook_for_keys = False`. Without `look_for_keys = False`, password auth fails with "No existing session". Use `cisco.iosxr.iosxr_command` (or `ansible.netcommon.cli_command`) for show commands — NOT `ansible.builtin.raw`
- **OpenTofu CLI syntax differs** — `iagctl run service opentofu-plan apply <name> --set key=value` (the `apply`/`destroy` subcommand goes between the type and service name)
- **OpenTofu results include `state_file`** — outputs are in `state_file.outputs`, not `result.stdout` like Python/Ansible

## How It Works

1. **Write a YAML service file** — defines repos, decorators, secrets, services
2. **`iagctl db import`** — loads into IAG
3. **`iagctl run service`** — test from CLI
4. **`GatewayManager.runService`** — call from Itential workflows

**Always start from a helper template.** Read the matching example from `${CLAUDE_PLUGIN_ROOT}/helpers/iag/` first, then modify:
- Python service → `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-python-service.yaml`
- Ansible service → `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-ansible-service.yaml`
- OpenTofu service → `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-opentofu-service.yaml`
- Multi-service chain → `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-multi-service-chain.yaml`
- Full schema reference → `${CLAUDE_PLUGIN_ROOT}/helpers/iag/service-file-schema.md`

**Do NOT build YAML from scratch. Read the helper first.**

---

## Authentication

| Mode | Auth | How |
|------|------|-----|
| **Local** | None needed | `iagctl` talks to local IAG directly |
| **Server/Client** | Login required | `iagctl login <username>` → interactive password prompt |
| **Itential workflows** | Pre-configured | Platform admin sets up gateway. `clusterId` references it. |

**The agent cannot run `iagctl login`** — it requires an interactive terminal. If the engineer hasn't logged in yet, tell them:
> "Run `iagctl login admin` in your terminal and enter your password. Once done, I can continue."

Quick check — if this works, you're authenticated:
```bash
iagctl get services
```

---

## Writing Service Files

### YAML Structure

A service file has these top-level sections (all optional — include only what you need):

```yaml
decorators: []      # Input schemas for services
repositories: []    # Git repos with code
services: []        # Python/Ansible/OpenTofu services
registries: []      # Package registries (PyPI, Galaxy)
secrets: []         # Credentials and keys
```

### Service Types

| Type | Key fields | Runs |
|------|-----------|------|
| `python-script` | `filename`, `runtime.env`, `runtime.req-file` | Python file from repo |
| `ansible-playbook` | `playbooks`, `runtime.inventory`, `runtime.env` | Ansible playbook(s) from repo |
| `opentofu-plan` | `action`, `vars`, `var-files`, `state-file` | OpenTofu apply/plan/destroy |
| `executable` | `filename`, `arg-format` | Custom executable |

### Python Script Services

**Complete service YAML with all common fields:**

```yaml
decorators:
  - name: my-service                       # should match service name
    schema:
      $id: my-service                      # should match service name
      $schema: https://json-schema.org/draft/202012/schema
      properties:
        device_ip:
          type: string
          description: "Target device IP"
          examples: ["10.0.0.1", "172.20.100.63"]
        device_type:
          type: string
          description: "Netmiko device type"
          enum: ["cisco_ios", "cisco_xr", "cisco_nxos"]
          default: "cisco_ios"
        interfaces:
          type: string
          description: "Comma-separated interface names"
      required:
        - device_ip
        - interfaces
      type: object

repositories:
  - name: my-repo
    url: https://github.com/org/repo.git
    reference: main

services:
  - name: my-service
    type: python-script
    description: Connects to device and returns interface health report
    filename: main.py
    working-directory: scripts              # directory containing main.py in repo
    repository: my-repo
    decorator: my-service                   # links to decorator above
    secrets:                                # injected as env vars at runtime
      - name: device-username
        type: env
        target: DEVICE_USERNAME             # script reads os.environ['DEVICE_USERNAME']
      - name: device-password
        type: env
        target: DEVICE_PASSWORD
    runtime:
      req-file: requirements.txt            # or pyproject.toml — installs dependencies
      env:                                  # extra environment variables
        NETMIKO_TIMEOUT: "30"
```

**Python script contract — how IAG runs your script:**

1. **Inputs arrive as `--property_name` CLI args.** Decorator schema property names become argparse flags. A property named `device_ip` becomes `--device_ip`.
2. **Credentials arrive as env vars** from the `secrets` block. Use `os.environ.get('DEVICE_USERNAME')`.
3. **Behavior selection via `runtime.env`** — use this to make one script serve multiple services (see pattern below).
4. **Output: JSON to stdout.** Always `print(json.dumps(result))`. Even on errors, return JSON with `"success": false`.
5. **Exit code:** 0 for any parseable result (success or handled error). 1 only for fatal setup failures (missing credentials).

**Script template:**

```python
#!/usr/bin/env python3
import argparse
import json
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device_ip", required=True)
    parser.add_argument("--device_type", default="cisco_ios")
    parser.add_argument("--interfaces", required=True)
    args = parser.parse_args()

    username = os.environ.get("DEVICE_USERNAME")
    password = os.environ.get("DEVICE_PASSWORD")
    if not username or not password:
        print(json.dumps({"success": False, "error": "DEVICE_USERNAME and DEVICE_PASSWORD env vars required"}))
        sys.exit(1)

    try:
        result = {"success": True, "data": do_work(args, username, password)}
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}))

if __name__ == "__main__":
    main()
```

**One-file-multi-service pattern:** Same Python file, different services with different `runtime.env`:

```yaml
services:
  - name: aws-ec2-add
    type: python-script
    filename: aws-ec2.py                   # same file
    working-directory: aws-operations
    repository: my-repo
    decorator: aws-ec2-add
    runtime:
      env:
        OPERATION: add                     # script checks os.environ.get('OPERATION')
        OUTPUT_FORMAT: json
    secrets:
      - name: aws_access_key_id
        type: env
        target: AWS_ACCESS_KEY_ID

  - name: aws-ec2-delete
    type: python-script
    filename: aws-ec2.py                   # same file
    working-directory: aws-operations
    repository: my-repo
    decorator: aws-ec2-delete
    runtime:
      env:
        OPERATION: delete                  # different operation
        OUTPUT_FORMAT: json
    secrets:
      - name: aws_access_key_id
        type: env
        target: AWS_ACCESS_KEY_ID
```

The script checks env vars first, then falls back to argparse:
```python
operation = os.environ.get('OPERATION') or args.op
```

### Ansible Playbook Services

**Complete service YAML — `runtime` block is critical for Ansible:**

```yaml
decorators:
  - name: sros-config
    schema:
      $id: sros-config
      $schema: https://json-schema.org/draft/202012/schema
      properties:
        sros_cli_commands:
          type: array
          items:
            type: string
          minItems: 1
          description: "CLI commands to execute"
        target_hosts:
          type: string
          description: "Target hosts or inventory groups"
          default: "all"
      required:
        - sros_cli_commands
      type: object

repositories:
  - name: my-ansible-repo
    url: git@github.com:org/ansible-playbooks.git
    private-key-name: git-ssh-key

services:
  - name: sros-config
    type: ansible-playbook
    description: Execute CLI commands on Nokia SROS devices
    playbooks:
      - sros_config.yml                    # one playbook per service (array but always single)
    working-directory: sros_config         # directory containing the playbook
    repository: my-ansible-repo
    decorator: sros-config
    runtime:
      inventory:                           # REQUIRED for Ansible — inventory file(s)
        - inventory.yaml
      config-file: ansible.cfg             # optional — custom ansible config
      env:                                 # IMPORTANT — controls Ansible behavior
        ANSIBLE_HOST_KEY_CHECKING: "false"  # disable SSH host key checking
        ANSIBLE_STDOUT_CALLBACK: json       # JSON output — critical for structured results
```

**Ansible service with secrets (SSH key injection):**

```yaml
services:
  - name: linux-patch-check
    type: ansible-playbook
    playbooks:
      - patch_check.yml
    working-directory: linux_patch_check
    repository: my-ansible-repo
    decorator: linux-patch-check
    secrets:
      - name: SELAB-PEM                    # secret name in IAG
        type: env
        target: SELAB-PEM                  # playbook reads with lookup('env', 'SELAB-PEM')
    runtime:
      inventory:
        - inventory.yaml
      env:
        ANSIBLE_HOST_KEY_CHECKING: "false"
        ANSIBLE_STDOUT_CALLBACK: json
```

The playbook writes the injected key to a temp file:
```yaml
- name: Write PEM to temp file
  ansible.builtin.copy:
    content: "{{ lookup('env', 'SELAB-PEM') }}"
    dest: "/tmp/ssh_key.pem"
    mode: '0600'
```

**Multiple services sharing a working-directory** — different playbooks in the same directory:

```yaml
services:
  - name: linux-patch-check
    playbooks: [patch_check.yml]
    working-directory: linux_patch_check   # same directory
    # ...
  - name: linux-execute-patch
    playbooks: [execute_patch.yml]
    working-directory: linux_patch_check   # same directory
    # ...
  - name: linux-mock-patch
    playbooks: [mock_patch.yml]
    working-directory: linux_patch_check   # same directory
    # ...
```

**Ansible runtime options** (all optional, in the `runtime:` block):

| Field | Purpose | Example |
|-------|---------|---------|
| `inventory` | Inventory file(s) | `["inventory.yaml"]` |
| `config-file` | ansible.cfg path | `"ansible.cfg"` |
| `env` | Environment variables | `{ANSIBLE_HOST_KEY_CHECKING: "false"}` |
| `req-file` | pip requirements or ansible-galaxy requirements.yml | `"requirements.txt"` or `"requirements.yml"` |
| `extra-vars` | Extra variables | `["env=prod"]` |
| `extra-vars-file` | Variable files | `["vars.yml"]` |
| `check` | Dry-run mode | `false` |
| `diff` | Show diffs | `true` |
| `forks` | Parallel processes | `10` |
| `tags` | Run only these tags | `"webservers"` |
| `limit` | Limit to hosts | `["host1"]` |

**Ansible `network_cli` for network devices (Cisco XR, IOS, NXOS, Nokia SROS):**

Use `network_cli` connection with vendor modules (e.g., `cisco.iosxr.iosxr_command`, `ansible.netcommon.cli_command`). This is the recommended approach for network devices.

Required files in the working directory:

`requirements.txt` — pip dependencies for `network_cli`:
```
paramiko
```

`ansible.cfg` — must include `look_for_keys = False` for password auth:
```ini
[defaults]
host_key_checking = False
stdout_callback = json
timeout = 30

[persistent_connection]
connect_timeout = 30
command_timeout = 30

[paramiko_connection]
look_for_keys = False
```

`inventory.yaml` — use Jinja2 refs to decorator schema properties:
```yaml
all:
  children:
    xr_device:
      hosts:
        xr-router:
          ansible_host: "{{ device_ip }}"
          ansible_user: "{{ device_username }}"
          ansible_password: "{{ device_password }}"
          ansible_connection: network_cli
          ansible_network_os: cisco.iosxr.iosxr
          ansible_ssh_common_args: '-o StrictHostKeyChecking=no'
          ansible_host_key_checking: false
          ansible_paramiko_host_key_checking: false
```

`health_check.yml` — playbook using vendor module:
```yaml
---
- name: Cisco XR Health Check
  hosts: xr_device
  gather_facts: false

  tasks:
    - name: Run show commands
      cisco.iosxr.iosxr_command:
        commands:
          - show version
          - show platform
          - show ip interface brief
      register: command_output

    - name: Display results
      ansible.builtin.debug:
        msg:
          device_ip: "{{ ansible_host }}"
          show_version: "{{ command_output.stdout[0] }}"
          show_platform: "{{ command_output.stdout[1] }}"
          show_ip_interface_brief: "{{ command_output.stdout[2] }}"
```

`services.yaml` — wire it all together with `runtime.req-file`:
```yaml
services:
  - name: xr-health-check
    type: ansible-playbook
    playbooks:
      - health_check.yml
    working-directory: playbooks
    repository: xr-health-check-repo
    decorator: xr-health-check
    runtime:
      inventory:
        - inventory.yaml
      config-file: ansible.cfg
      req-file: requirements.txt
      env:
        ANSIBLE_HOST_KEY_CHECKING: "false"
        ANSIBLE_STDOUT_CALLBACK: json
```

**Key points:**
- `paramiko` in `requirements.txt` — IAG installs it in the service venv
- `look_for_keys = False` in `ansible.cfg` — fixes "No existing session" error with password auth
- `ansible_network_os` must match the vendor collection (e.g., `cisco.iosxr.iosxr`, `sros`)
- Inventory uses `{{ var }}` Jinja2 refs matching decorator schema property names
- `runtime.req-file` can be a pip `requirements.txt` or ansible-galaxy `requirements.yml`

### OpenTofu Plan Services

**Complete service YAML — note the correct field names:**

```yaml
decorators:
  - name: azure-landing-zone
    schema:
      $id: azure-landing-zone
      $schema: https://json-schema.org/draft/202012/schema
      properties:
        resource_group_name:
          type: string
          description: "Resource group name"
          default: "lz-demo-rg"
        vnet_address_space:
          type: array
          items:
            type: string
            pattern: "^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$"
          default: ["10.0.0.0/16"]
      required:
        - resource_group_name
      type: object

repositories:
  - name: my-tofu-repo
    url: git@github.com:org/opentofu.git
    private-key-name: git-ssh-key

services:
  - name: azure-landing-zone
    type: opentofu-plan
    description: Deploy Azure landing zone infrastructure
    working-directory: infra/modules/landing-zone   # directory with .tf files
    repository: my-tofu-repo
    decorator: azure-landing-zone
    action: apply                          # REQUIRED: apply, plan, or destroy
    vars: []                               # optional: ["-var flags"] e.g. ["region=us-east-1"]
    var-files: []                          # optional: ["-var-file flags"] e.g. ["prod.tfvars"]
    state-file: null                       # optional: custom state file path
```

**IMPORTANT — field names:** The fields are `vars` and `var-files`, NOT `plan-vars` / `plan-var-files`. The `action` field is required.

**Secrets for cloud credentials use the `TF_VAR_` convention:**

```yaml
services:
  - name: deploy-infra
    type: opentofu-plan
    working-directory: infra
    repository: my-tofu-repo
    decorator: deploy-infra
    action: apply
    vars: []
    var-files: []
    state-file: null
    secrets:
      - name: aws-access-key
        type: env
        target: TF_VAR_aws_access_key     # OpenTofu reads TF_VAR_* as variables
      - name: aws-secret-key
        type: env
        target: TF_VAR_aws_secret_key
```

**Decorator params pass directly as OpenTofu variables** — each property in the decorator schema becomes a variable available to your `.tf` files. Backend/provider config lives in the `.tf` files, not the service YAML.

### Decorators — Input Validation

Every service should have a decorator. The `$id` should match the service name:

```yaml
decorators:
  - name: my-service
    schema:
      $id: my-service                      # match service name, not "root"
      $schema: https://json-schema.org/draft/202012/schema
      properties:
        device_ip:
          type: string
          description: "Target device IP"
        format:
          type: string
          enum: ["json", "table"]          # restricted values
          default: "json"
        commands:
          type: array                      # array with item validation
          items:
            type: string
          minItems: 1
        verbose:
          type: string
          enum: ["true", "false"]          # booleans as strings (common pattern)
          default: "false"
      required:
        - device_ip
      type: object
      additionalProperties: false          # reject unknown params (recommended)
```

### Adding Secrets

**Best practice:** Never put real secret values in YAML. Define secret references in the service, create actual secrets separately.

```yaml
# In services.yaml — only references, no values
services:
  - name: my-service
    type: python-script
    filename: main.py
    working-directory: scripts
    repository: my-repo
    secrets:                               # injected as env vars at runtime
      - name: api-token                    # secret name in IAG
        type: env
        target: API_TOKEN                  # script reads os.environ['API_TOKEN']
```

```bash
# Create secrets separately — never in the YAML file
iagctl create secret api-token --prompt-value
```

**WARNING:** `--force` import overwrites secrets too. If your YAML has a top-level `secrets:` section with placeholder values, `--force` will replace real secrets with placeholders. **Keep the top-level `secrets:` section out of `services.yaml` entirely.** Only define secret references inside each service's `secrets:` array.

### Private Git Repos

```yaml
repositories:
  # SSH auth (most common):
  - name: private-repo
    url: git@github.com:org/private.git
    private-key-name: git-ssh-key          # name of secret holding SSH key
    reference: main

  # HTTPS auth:
  - name: https-repo
    url: https://github.com/org/repo.git
    username: myuser
    password-name: git-password            # name of secret holding password
```

Create the SSH key secret separately: `iagctl create secret git-ssh-key --prompt-value`

---

## Import / Export

```bash
# Validate only (no changes)
iagctl db import services.yaml --validate

# Dry run with checks
iagctl db import services.yaml --check

# Import (additive — new added, existing skipped)
iagctl db import services.yaml

# Import with overwrite (existing replaced by name)
iagctl db import services.yaml --force

# Export current state
iagctl db export state.yaml

# Import directly from Git repo
iagctl db import --repository https://github.com/org/repo.git --reference main
```

**Import behavior:**
- New resources → **added**
- Existing (same name) → **skipped** without `--force`, **replaced** with `--force`
- Resources not in the YAML → **untouched** (never deleted)

---

## Development Loop

When iterating on service code, every change requires pushing to Git and re-importing — IAG pulls code from the repo, not from local files.

```
Edit code → git commit + push → iagctl db import services.yaml --force → iagctl run service → repeat
```

**Tip:** Keep secrets out of `services.yaml` so `--force` imports don't clobber them (see Secrets warning above).

---

## Testing Services (CLI)

```bash
# List services
iagctl get services
iagctl get services --type python-script

# See what inputs a service expects
iagctl run service python-script my-service --use

# Run with inputs
iagctl run service python-script my-service \
  --set device_ip=10.0.0.1 \
  --set device_type=ios

# Ansible
iagctl run service ansible-playbook my-playbook --set target_host=router1

# OpenTofu apply
iagctl run service opentofu-plan apply my-plan --set region=us-east-1

# OpenTofu destroy
iagctl run service opentofu-plan destroy my-plan

# Raw JSON output
iagctl run service python-script my-service --raw
```

---

## Calling IAG from Itential Workflows

### Finding the clusterId

The `clusterId` is required for all GatewayManager tasks. Discover it via the platform API:

```
GET /gateway_manager/v1/gateways/
```

This returns the list of configured gateway clusters. Use the cluster name as the `clusterId` value in workflow tasks.

### GatewayManager Tasks

| Task | What it does |
|------|-------------|
| `runService` | Run an IAG service by name |
| `sendCommand` | Send CLI commands to inventory nodes |
| `sendConfig` | Send config text to inventory nodes |
| `getServices` | List available services |
| `getGateways` | List connected gateways |

### runService Task Wiring

```json
{
  "name": "runService",
  "app": "GatewayManager",
  "type": "automatic",
  "location": "Application",
  "displayName": "GatewayManager",
  "actor": "Pronghorn",
  "variables": {
    "incoming": {
      "serviceName": "device-info",
      "clusterId": "ankitcluster",
      "params": {"device_ip": "10.0.0.1", "device_type": "ios"},
      "inventory": ""
    },
    "outgoing": {
      "result": "$var.job.iagResult"
    }
  }
}
```

**Incoming:**
| Field | Type | Description |
|-------|------|-------------|
| `serviceName` | string | IAG service name (same name as in YAML/iagctl) |
| `clusterId` | string | Gateway cluster ID — ask the engineer |
| `params` | object | Key/value inputs matching the decorator schema |
| `inventory` | array or `""` | Target nodes: `[{"inventory": "inv-name", "nodeNames": ["node1"]}]` or `""` if not needed |

**Outgoing:**
| Field | Type | Description |
|-------|------|-------------|
| `result` | object | JSON-RPC envelope with service execution result |

### Result Shape — JSON-RPC Wrapper

`runService` returns a JSON-RPC envelope, NOT raw stdout:

```json
{
  "id": "dc7c4a5d-...",
  "jsonrpc": "2.0",
  "result": {
    "return_code": 0,
    "stdout": "{ ... script output ... }",
    "stderr": "",
    "start_time": "2026-03-03T19:26:37Z",
    "end_time": "2026-03-03T19:26:37Z",
    "elapsed_time": 0.659
  },
  "status": "completed"
}
```

**To extract stdout in a workflow:** use a `query` task with path `result.stdout`:

```json
{
  "name": "query",
  "app": "WorkFlowEngine",
  "type": "operation",
  "variables": {
    "incoming": {
      "pass_on_null": false,
      "query": "result.stdout",
      "obj": "$var.job.iagResult"
    },
    "outgoing": {
      "return_data": "$var.job.serviceOutput"
    }
  }
}
```

### Chaining Services in a Workflow

Pass output from one service as input to the next:

```
runService(device-info)
    → query: extract result.stdout → parse JSON
        → runService(config-generator) with params from previous output
            → query: extract result.stdout
                → runService(config-validator)
```

Each `query` extracts `result.stdout` from the JSON-RPC envelope. If the stdout is JSON, parse it before passing as params to the next service.

### sendCommand Task Wiring

```json
{
  "name": "sendCommand",
  "app": "GatewayManager",
  "type": "automatic",
  "actor": "Pronghorn",
  "variables": {
    "incoming": {
      "clusterId": "ankitcluster",
      "commands": ["show version", "show ip interface brief"],
      "inventory": [{"inventory": "my-inventory", "nodeNames": ["router1"]}]
    },
    "outgoing": {
      "result": "$var.job.commandResult"
    }
  }
}
```

### sendConfig Task Wiring

```json
{
  "name": "sendConfig",
  "app": "GatewayManager",
  "type": "automatic",
  "actor": "Pronghorn",
  "variables": {
    "incoming": {
      "clusterId": "ankitcluster",
      "config": "$var.job.renderedConfig",
      "inventory": [{"inventory": "my-inventory", "nodeNames": ["switch1"]}]
    },
    "outgoing": {
      "result": "$var.job.configResult"
    }
  }
}
```

### Testing IAG Services via Workflow

After CLI testing passes (`iagctl run service`), test the full workflow integration:

**1. Create the workflow** (runService → query to extract stdout):
```
POST /automation-studio/automations
```

**2. Start a job:**
```
POST /operations-manager/jobs/start
```
```json
{
  "workflow": "My IAG Workflow",
  "options": {
    "type": "automation",
    "variables": {
      "device_ip": "172.20.100.63",
      "device_type": "cisco_xr",
      "interfaces": "GigabitEthernet0/0/0/0",
      "clusterId": "ankitcluster"
    }
  }
}
```

**3. Check the job:**
```
GET /operations-manager/jobs/{jobId}
```
Verify:
- `data.status` is `"complete"` (not `"error"`)
- `data.error` is `null` (no task errors)
- `data.variables.serviceOutput` contains the extracted stdout from the IAG service

**If the job errors with "Service not found on cluster":** the `clusterId` is wrong. Check `GET /gateway_manager/v1/gateways/` for the correct cluster name.

---

## When to Use Which

| Need | Use |
|------|-----|
| Run a Python/Ansible/OpenTofu service | `GatewayManager.runService` |
| Send ad-hoc CLI commands | `GatewayManager.sendCommand` or `AGManager.itential_cli` |
| Push config text to device | `GatewayManager.sendConfig` or `AGManager.itential_set_config` |
| Run MOP validation checks | `MOP.RunCommandTemplate` (separate from IAG) |

### AGManager vs GatewayManager

| | AGManager | GatewayManager |
|---|-----------|---------------|
| **Tasks** | One per script/playbook (e.g., `itential_cli`) | Generic (`runService`, `sendCommand`) |
| **Input style** | Task-specific variables | `serviceName` + `params` object |
| **When to use** | Built-in IAG capabilities | Custom services built with iagctl |

---

## Operational Commands (Inspect, Verify, Clean Up)

After importing, use these to verify and manage resources:

```bash
# === LIST RESOURCES ===
iagctl get services
iagctl get services --type python-script
iagctl get services --type ansible-playbook
iagctl get services --type opentofu-plan
iagctl get repositories
iagctl get secrets
iagctl get decorators
iagctl get registries
iagctl get clusters                          # find clusterId for workflows

# === INSPECT A SPECIFIC RESOURCE ===
iagctl describe service <name>               # full details: repo, decorator, secrets, runtime
iagctl describe repository <name>            # URL, reference, auth method
iagctl describe decorator <name>             # JSON schema
iagctl describe secret <name>                # secret metadata (value redacted)

# === DELETE ===
iagctl delete service <name>
iagctl delete repository <name>
iagctl delete decorator <name>
iagctl delete secret <name>

# === EXPORT CURRENT STATE ===
iagctl db export current-state.yaml          # full dump of everything in IAG
```

**After every import, verify with:**
```bash
iagctl describe service <name>
```
This confirms the service was created with the correct repo, decorator, secrets, and working directory.

---

## Organizing Services for Teams

### Naming Conventions

```
Services:     {team}-{domain}-{action}        e.g. netops-device-health-check
Decorators:   {service-name}                  e.g. netops-device-health-check
Repositories: {team}-{purpose}                e.g. netops-automation
Secrets:      {team}-{system}-{purpose}        e.g. netops-git-ssh-key
```

Tag services: `tags: [team:netops, domain:network]` — filter with `iagctl get services --tag team:netops`

### Repository Layouts

| Layout | When | Structure |
|--------|------|-----------|
| **Standalone repo** | One service per repo | `services.yaml` at repo root, code in subdirectory |
| **Mono-repo** | < 20 services, one team | `.gateway/services/{name}.yml` per service, shared repo |
| **Multi-repo** | 20+ services, domain ownership | Each team owns a repo with its own `services.yaml` |

**Standalone repo** (cleanest for individual services):
```
cisco-interface-check/
├── services.yaml           ← decorators + repos + services in one file
└── scripts/
    ├── main.py
    └── requirements.txt
```

**Mono-repo** (shared codebase, per-file service definitions):
```
automation-services/
├── .gateway/services/      ← one YAML per service
│   ├── device-info.yml
│   └── config-push.yml
├── device-info/main.py
└── config-push/main.py
```

### Environment Promotion

| Setting | Dev | Staging | Production |
|---------|-----|---------|------------|
| Git `reference` | branch | release branch | tagged version (e.g., `v1.2.3`) |
| Secrets | `--prompt-value` | vault or `--prompt-value` | vault only |
| Import mode | `--force` | `--check` then import | `--validate` → `--check` → import |
| Who imports | developer | CI/CD pipeline | CI/CD with approval |

### CI/CD Integration

**GitLab CI:**
```yaml
stages: [validate, deploy]
validate:
  stage: validate
  script: iagctl db import services.yaml --validate
  only: [merge_requests]
deploy-dev:
  stage: deploy
  script:
    - iagctl login $IAG_USER
    - iagctl db import services.yaml --force
  only: [develop]
deploy-prod:
  stage: deploy
  script:
    - iagctl db import services.yaml --check
    - iagctl db import services.yaml
  only: [main]
  when: manual
```

**GitHub Actions:**
```yaml
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: iagctl db import services.yaml --validate
      - run: iagctl db import services.yaml --force
```

---

## Before Handing Off

**Service quality:**
- [ ] Service has a decorator with `additionalProperties: false`
- [ ] Service tested: `iagctl run service <type> <name> --set ...`
- [ ] Output is valid JSON (for Python: `print(json.dumps(result))`)
- [ ] Error cases return JSON with `"success": false`, not stderr
- [ ] Service YAML validates: `iagctl db import file.yaml --validate`

**Workflow integration:**
- [ ] Itential workflow tested end-to-end with `runService` task
- [ ] Workflow extracts `result.stdout` from JSON-RPC envelope via `query` task
- [ ] Error transitions on `runService` task (handles service failures)

**Security and ops:**
- [ ] Secrets created via `iagctl create secret --prompt-value` (never in YAML)
- [ ] No top-level `secrets:` section in committed service files
- [ ] Git references pinned to tags (not branches) for production
- [ ] Naming conventions followed

## Helper Templates

**Always start from a helper template.** Read the matching example from `${CLAUDE_PLUGIN_ROOT}/helpers/iag/` first, then modify:

| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-python-service.yaml` | Python script service |
| `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-ansible-service.yaml` | Ansible playbook service |
| `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-opentofu-service.yaml` | OpenTofu plan service |
| `${CLAUDE_PLUGIN_ROOT}/helpers/iag/example-multi-service-chain.yaml` | Multi-service orchestration |
| `${CLAUDE_PLUGIN_ROOT}/helpers/iag/service-file-schema.md` | Full YAML schema reference |

````

============================================================
FILE: .claude/skills/itential-devices/SKILL.md
DIRECTORY: .claude/skills/itential-devices/
FILENAME: SKILL.md
============================================================
SHA256: fa8d23a1b022835871f887a485837b59e53c717c3793ca1141adc45da6a4e156

````markdown
---
name: itential-devices
description: Manage network devices, backups, diffs, device groups, and device templates in Itential Configuration Manager. Use when the user needs to work with device inventory, configs, or backups.
argument-hint: "[device-name or action]"
---

# Configuration Manager - Developer Skills Guide

Configuration Manager is the Itential Platform application for managing devices, their configurations, and compliance. It provides the tools to retrieve, back up, apply, and diff device configurations.

For Golden Configurations, compliance, and grading, use `/itential-golden-config`.

## Gotchas

- `POST /configuration_manager/devices` is a **POST**, not GET — requires `{"options": {...}}` body
- Device list is in the **`list`** field, not `devices` or `results`
- Backup response returns `{status, message, id}` — the `id` is the backup's MongoDB insertedId
- Apply config body has nested structure: `{"config": {"device": "...", "config": "..."}}` — config inside config
- Diff endpoint is **PUT** `/configuration_manager/lookup_diff`, not POST. Supports `options.type`: `'line'`, `'word'` (default), `'char'`
- Create group: `/devicegroup` (singular), list groups: `/deviceGroups` (plural)
- `deviceNames` in create group is a **comma-separated string**, NOT an array: `"dev1, dev2"`
- `provider` in backup can be a string OR an array depending on the adapter
- Empty device config → backup silently not created (returns error, no backup stored)
- Large configs auto-stored in GridFS — `rawConfig` field is empty in the document, config is in GridFS
- Cannot delete device groups referenced by a Compliance Plan or Golden Config — deletion is blocked
- Device group update only accepts: `name`, `devices`, `description`, `gbac` — other fields silently dropped
- Duplicate group names blocked on create and rename
- `searchDeviceGroups` caps page size at 100 regardless of requested limit
- `getDeviceGroupById` accepts both ID and name — auto-detects which one you passed
- Device template apply checks OS type compatibility — fails if device `ostype` doesn't match template's `deviceOSTypes`
- Backup search uses regex by default — set `options.regex: false` for exact matching

## What is Configuration Manager?

Configuration Manager handles the full lifecycle of device configuration:

- **Devices** - Inventory of network devices discovered through adapters, with the ability to retrieve, back up, and apply configurations
- **Device Groups** - Logical groupings of devices for bulk operations
- **Template Designer** - Reusable Jinja2 config templates that can be applied to devices
- **Backups & Diff** - Backup device configs and compare versions to see what changed
- **Golden Configurations** - Use `/itential-golden-config` for trees, config specs, compliance, grading, and remediation

### How They Connect

```
Devices ──────────────────────────────────────────────────┐
   │                                                       │
   ├── belong to Device Groups                             │
   │                                                       │
   ├── configs can be backed up and diffed                 │
   │                                                       │
   ├── Device Templates can be applied to devices          │
   │                                                       │
   ├── are assigned to Golden Config tree nodes             │
   │        │                                              │
   │        └── See /itential-golden-config for full details  │
   │                                                       │
   └── Compliance runs compare device config ◄─────────────┘
        against Config Specs → produce Compliance Reports
```

## API Reference

**Base Path:** `/configuration_manager`
**Authentication:** Bearer token (OAuth), Query token, Basic Auth, or Cookie

### Devices

Devices are discovered through adapters (e.g., IAG, Cisco DNA). Configuration Manager can retrieve, back up, and apply configurations to them.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/devices` | Find devices with filtering and pagination |
| GET | `/configuration_manager/devices/{name}` | Get device details by name |
| GET | `/configuration_manager/devices/{name}/configuration` | Get current device configuration |
| POST | `/configuration_manager/devices/{deviceName}/configuration` | Apply a config to a device |
| POST | `/configuration_manager/devices/backups` | Backup device configuration |
| POST | `/configuration_manager/backups` | Search/list backups with filtering and pagination |
| GET | `/configuration_manager/backups/{id}` | Get a backup by ID |
| PUT | `/configuration_manager/backups/{id}` | Update backup metadata (description, notes) |
| DELETE | `/configuration_manager/backups` | Delete backups by array of IDs |
| GET | `/configuration_manager/devices/{name}/isAlive` | Check if device is connected |

**Get device details:**
```
GET /configuration_manager/devices/IOS-CAT8KV-1
```
```json
{
  "name": "IOS-CAT8KV-1",
  "device-type": "network_cli",
  "ipaddress": "10.1.8.80",
  "port": 22,
  "ostype": "cisco-ios",
  "chosenAdapter": "AutomationGateway",
  "origin": "AutomationGateway"
}
```

**Find devices with filtering:**
```
POST /configuration_manager/devices
```
```json
{
  "options": {
    "filter": { "name": "" },
    "start": 0,
    "limit": 25,
    "sort": [{ "name": 1 }],
    "order": "ascending"
  }
}
```

**Options fields:**
- **`limit`** (integer, required) - max results to return (min: 1)
- **`start`** (integer) - pagination offset (min: 0)
- **`filter`** (object) - filter by `name`, `address` (IP), `port`
- **`sort`** (array) - sort objects, e.g. `[{"name": 1}]` (1 = ascending, -1 = descending)
- **`order`** (string) - `"ascending"` or `"descending"`
- **`adapterType`** (array) - filter by adapter type, e.g. `["AnsibleManager", "NSO"]`
- **`adapterId`** (array) - filter by adapter instance ID
- **`exactMatch`** (boolean) - `true` for exact match, `false` for partial/contains match

**Response:**
```json
{
  "entity": "device",
  "total": 24,
  "unique_device_count": 24,
  "return_count": 24,
  "start_index": 0,
  "list": [
    {
      "name": "IOS-CAT8KV-1",
      "device-type": "network_cli",
      "ipaddress": "10.1.8.80",
      "port": 22,
      "ostype": "cisco-ios",
      "host": "AutomationGateway",
      "chosenAdapter": "AutomationGateway"
    }
  ]
}
```
Note: devices are in the **`list`** field, not `devices`.

**Get device config response:**
```json
{
  "device": "IOS-CAT8KV-1",
  "config": "! Last configuration change at ...\nversion 17.15\nservice timestamps debug datetime msec\n..."
}
```
The `config` field contains the full running configuration as a string.

**Backup device config:**
```
POST /configuration_manager/devices/backups
```
```json
{
  "name": "IOS-CAT8KV-1",
  "options": {
    "description": "Pre-change backup",
    "notes": "Backup before port turn-up"
  }
}
```
Response:
```json
{
  "status": "success",
  "message": "Device IOS-CAT8KV-1 backed up successfully",
  "id": "699b69e25ae7d527cda5ffe4"
}
```
The `id` field is the backup's MongoDB ID — use it to retrieve the backup later.

**Note:** If the device returns an empty configuration, the backup is NOT created and returns an error.

**Backup structure** (GET `/configuration_manager/backups/{id}`):
```json
{
  "_id": "699b69e25ae7d527cda5ffe4",
  "name": "IOS-CAT8KV-1",
  "provider": "AutomationGateway",
  "type": "native",
  "date": "2026-02-22T20:41:06.160Z",
  "rawConfig": "...(full config text)...",
  "description": "Pre-change backup",
  "notes": "Backup before port turn-up"
}
```

Note: `provider` can be a string or array depending on the adapter. For very large configs, `rawConfig` may be empty — the config is stored in GridFS (check `storage.type === 'gridfs'`).

**Search/list backups:**
```
POST /configuration_manager/backups
```
```json
{
  "options": {
    "filter": { "name": "IOS-CAT8KV-1" },
    "start": "0",
    "limit": 25,
    "sort": { "date": -1 },
    "regex": true
  }
}
```
Response:
```json
{
  "total": 3,
  "list": [
    { "_id": "699b69e25ae7d527cda5ffe4", "name": "IOS-CAT8KV-1", "date": "...", "description": "..." }
  ]
}
```
- `options.start` must be a string (not integer)
- `options.regex` defaults to `true` (filter values use regex). Set `false` for exact matching.
- Backups are in the `list` field.

**Update backup metadata:**
```
PUT /configuration_manager/backups/{id}
```
```json
{
  "description": "Updated description",
  "notes": "Updated notes"
}
```

**Delete backups:**
```
DELETE /configuration_manager/backups
```
```json
{
  "backupIds": ["699b69e25ae7d527cda5ffe4", "699b6c745ae7d527cda5ffe8"]
}
```

**Apply config to a device** (`POST /configuration_manager/devices/{deviceName}/configuration`):

The `deviceName` is a **path parameter**, not in the body. The `config` field is an object:
```json
{
  "config": {
    "device": "IOS-CAT8KV-1",
    "config": "interface GigabitEthernet0/1\n switchport access vlan 100\n no shutdown"
  },
  "options": {}
}
```

**Compare two backups (diff):**
```
PUT /configuration_manager/lookup_diff
```
```json
{
  "id": "699b69e25ae7d527cda5ffe4",
  "nextId": "699b6c745ae7d527cda5ffe8",
  "collection": "backups",
  "nextCollection": "backups"
}
```
- `collection` - must be one of: `backups`, `nodes`, `deviceGroups`
- `nextCollection` - must be one of: `devices`, `backups`, `nodes`, `deviceGroups`
- `options` (optional) - `{"type": "word"}` where type is `"line"`, `"word"` (default), or `"char"`
- Response is an array of `[operation, text]` tuples:
  - `0` = unchanged text
  - `1` = added text
  - `-1` = removed text

**Run compliance on backups** (compare backup against golden config without touching the device):
```
POST /configuration_manager/compliance_reports/backups
```
```json
{
  "treeInfo": { "treeId": "...", "version": "initial", "nodePath": "base" },
  "backupIds": ["699b69e25ae7d527cda5ffe4"]
}
```

**DiffViewer** (workflow task for visual diff):
- Task: `ConfigurationManager.DiffViewer`
- Incoming: `compareFirstString`, `firstTitle`, `compareSecondString`, `secondTitle`, `darkMode`
- Displays a side-by-side diff for manual review in a workflow

### Device Groups

Logical groupings of devices for running bulk compliance checks, golden config assignments, and operational tasks.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/configuration_manager/deviceGroups` | List all device groups |
| POST | `/configuration_manager/devicegroup` | Create a device group |
| GET | `/configuration_manager/deviceGroups/{id}` | Get a device group by ID |
| GET | `/configuration_manager/name/devicegroups` | Get a device group by name |
| PUT | `/configuration_manager/deviceGroups/{id}` | Update a device group |
| DELETE | `/configuration_manager/deviceGroups` | Delete device groups |
| POST | `/configuration_manager/deviceGroups/{id}/devices` | Add devices to a group |
| DELETE | `/configuration_manager/deviceGroups/{id}/devices` | Remove devices from a group |
| POST | `/configuration_manager/deviceGroups/search` | Search groups with pagination |
| GET | `/configuration_manager/groups/device/{deviceName}` | Find all groups containing a device |

**Create a device group:**
```
POST /configuration_manager/devicegroup
```
```json
{
  "groupName": "Cisco Devices",
  "groupDescription": "All Cisco IOS devices in the lab",
  "deviceNames": "IOS-CAT8KV-1, IOS-CSR-AWS-1"
}
```

**Device group structure:**
```json
{
  "_id": "683a07a602c95837ccbfd39f",
  "name": "Cisco Devices",
  "devices": ["IOS-CAT8KV-1", "IOS-CSR-AWS-1"],
  "description": "",
  "created": "2025-05-30T19:31:50.069Z",
  "createdBy": "ankit.bhansali@itential.com"
}
```

### Template Designer (Device Templates)

Device templates are reusable Jinja2 configuration snippets that can be applied to devices. They store both the template text and default variable values.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/templates` | Create a device template |
| POST | `/configuration_manager/templates/search` | Search/get device templates |
| PUT | `/configuration_manager/templates` | Update a device template |
| DELETE | `/configuration_manager/templates` | Delete device templates by ID |
| POST | `/configuration_manager/templates/apply` | Apply a template to a device |
| POST | `/configuration_manager/import/templates` | Import device templates |

**Create a device template:**
```
POST /configuration_manager/templates
```
```json
{
  "name": "IOS_Subinterface_Config",
  "template": "interface GigabitEthernet1.{{ vlan_id }}\n description {{ description }}\n encapsulation dot1Q {{ vlan_id }}\n ip address {{ ip_address }} {{ subnet_mask }}",
  "variables": {
    "vlan_id": "800",
    "description": "Test Subinterface",
    "ip_address": "10.80.0.1",
    "subnet_mask": "255.255.255.0"
  }
}
```
- `template` - Jinja2 template text with `{{ variable }}` placeholders
- `variables` - default values for the template variables (used when applying without overrides)

**Response:**
```json
{
  "result": "success",
  "data": {
    "_id": "699b6b8a5ae7d527cda5ffe7",
    "name": "IOS_Subinterface_Config",
    "template": "interface GigabitEthernet1.{{ vlan_id }}\n ...",
    "variables": { "vlan_id": "800", "description": "Test Subinterface", ... },
    "deviceOSTypes": []
  }
}
```

**Apply a template to a device:**
```
POST /configuration_manager/templates/apply
```
```json
{
  "deviceName": "IOS-CAT8KV-1",
  "templateId": "699b6b8a5ae7d527cda5ffe7",
  "options": {}
}
```

**Response:**
```json
{
  "status": "success",
  "result": [{ "value": "4 Command(s) Sent." }],
  "chosenAdapter": "AutomationGateway"
}
```
The template is rendered with the stored variables and pushed to the device as CLI commands.

**Search templates:**
```
POST /configuration_manager/templates/search
```
```json
{
  "name": "IOS_Subinterface",
  "options": {}
}
```

### Import/Export

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/import/backups` | Import backup documents |
| POST | `/configuration_manager/import/groups` | Import device group documents |
| POST | `/configuration_manager/import/templates` | Import device config templates |

For golden config import/export, use `/itential-golden-config`.

## Developer Scenarios

### 1. Device configuration management
```
GET /configuration_manager/devices/{name} → get device details
GET /configuration_manager/devices/{name}/configuration → get current config
POST /configuration_manager/devices/backups → backup before changes
POST /configuration_manager/templates/apply → apply a template
GET /configuration_manager/devices/{name}/configuration → verify change
POST /configuration_manager/devices/backups → backup after changes
PUT /configuration_manager/lookup_diff → diff pre vs post backups
```

### 2. Create and apply a device template
```
POST /configuration_manager/templates → create template with Jinja2 text + variables
POST /configuration_manager/templates/apply → apply to device {deviceName, templateId}
Verify: GET /configuration_manager/devices/{name}/configuration
```

### 3. Golden config and compliance
Use `/itential-golden-config` for the full flow.

````

============================================================
FILE: .claude/skills/itential-golden-config/SKILL.md
DIRECTORY: .claude/skills/itential-golden-config/
FILENAME: SKILL.md
============================================================
SHA256: 5bf45257b05df267eb09f4da00731bdf7282c32cb25dbabf28f549e64ae41c52

````markdown
---
name: itential-golden-config
description: Build golden config trees, config specs, compliance plans, run compliance checks, grade reports, and remediate violations. Use when the user needs to define configuration standards or check device compliance.
argument-hint: "[action or tree-name]"
---

# Golden Configurations - Developer Skills Guide

Golden Configurations define the "desired state" for device configurations. They enable compliance checking, grading, and remediation of configuration drift across your network.

## Gotchas

- **NEVER wire any task that applies golden-config/compliance-derived changes onto a device.** This skill detects, reports, and grades compliance — it does **not** remediate. The prohibited tasks are `runAutoRemediation`, `advancedAutoRemediation`, `convertChangesToConfig`, `patchDeviceConfiguration`, `advancedPatchDeviceConfiguration`, `patchCMDeviceConfiguration`, `ManualRemediation`, and `ManualRemediationResults`. No exceptions — not even when a spec asks for fully automatic remediation. To actually correct a device, hand the violations to a separate config-push delivery (see Remediation section).
- `deviceType` must match exactly: `"cisco-ios"` not `"Cisco IOS"` or `"ios"`
- `variables` in `PUT /configuration_manager/node/config` must be a **JSON object**, not a string
- `updateVariables` boolean is **REQUIRED** in node config update — omitting it silently skips variable merge
- Compliance run is **async** — returns `batchId`, not the report. Poll with `GET /compliance_reports/batch/{batchId}`
- Plan instance results are inside `groups[].plans[]`, not top-level
- `nodeId` in compliance plan is the **`configId`**, NOT the node name — get it from the tree version response
- Node path uses node **name** separated by `/` — root varies by tree (e.g., `base`, `Global`)
- Parser name must match the device's `ostype` or compliance parsing produces wrong results
- Parser `template` must reference an existing parser — list with `GET /configurations/parser`
- Parser lexRules are validated with `safe-regex` — unsafe patterns (catastrophic backtracking) are rejected
- Config spec regex patterns need escaped backslashes in JSON (`"\\d+"` not `"\d+"`)
- Duplicate tree names blocked — `"A tree with the name already exists"`
- Node path leading `/` is auto-stripped — `/base/DataCenter` and `base/DataCenter` are equivalent
- Creating a new tree version requires a `base` parameter specifying which version to clone from

## What is Golden Config?

Golden Config provides a hierarchical, version-controlled system for defining what device configurations should look like:

- **Trees** - Top-level containers associated with a device type (e.g., `cisco-ios`, `arista-eos`)
- **Versions** - Each tree can have multiple versions (e.g., `initial`) to evolve standards over time
- **Nodes** - Hierarchical structure within a version (e.g., `Global` → `EMEA` → `London`). Child nodes inherit from parents.
- **Config Specs** - Rules attached to each node that define required, disallowed, or informational configuration lines
- **Variables** - Tree-level variables accessible by all node templates via Jinja2 `{{ var }}` syntax
- **Configuration Parsers** - Define how raw CLI config is tokenized for comparison against config specs
- **Compliance Reports** - Results of checking device configs against golden config specs
- **Grading** - Scoring formula that produces a grade (Pass/Review/Fail) from compliance results
- **Remediation** - Correcting a device is **out of scope for this skill** — it reports violations; a separate config-push delivery applies fixes. The Configuration Manager remediation tasks are never used (see Remediation section).

### How Inheritance Works

```
Global (base node)
  ├── config spec: service password-encryption, aaa new-model, ntp server
  │
  ├── DataCenter
  │     ├── config spec: ip http secure-server, ip ssh version 2
  │     │
  │     └── Atlanta
  │           ├── devices: [IOS-CAT8KV-1]
  │           └── config spec: (empty or site-specific rules)
  │
  └── Branch
        └── ...
```

A device assigned to `Atlanta` is checked against **all inherited specs**: `Global` + `DataCenter` + `Atlanta`. This allows global standards at the top with site-specific overrides at the leaves.

## API Reference

**Base Path:** `/configuration_manager`

### Trees

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/configuration_manager/configs` | List all golden config trees |
| POST | `/configuration_manager/configs` | Create a new golden config tree |
| GET | `/configuration_manager/configs/{treeId}` | Get tree summary |
| GET | `/configuration_manager/configs/{treeId}/{version}` | Get tree version details (full node hierarchy) |
| PUT | `/configuration_manager/configs/{treeId}` | Update tree properties |
| PUT | `/configuration_manager/configs/{treeId}/{version}` | Update tree version properties |
| DELETE | `/configuration_manager/configs/{treeId}` | Delete a tree |
| DELETE | `/configuration_manager/configs` | Bulk delete trees by IDs |
| DELETE | `/configuration_manager/configs/{treeId}/{version}` | Delete a tree version |
| POST | `/configuration_manager/configs/{treeId}` | Create a new tree version (clone from existing) |
| POST | `/configuration_manager/search/configs` | Search trees by name/deviceType |
| DELETE | `/configuration_manager/configs/variables/{treeId}/{version}` | Delete tree-level variables |
| POST | `/configuration_manager/devices/device/trees` | Find which trees contain a specific device |
| POST | `/configuration_manager/devices/tree` | List all devices assigned to a tree |
| POST | `/configuration_manager/export/goldenconfigs` | Export a tree |
| POST | `/configuration_manager/import/goldenconfigs` | Import tree documents |

**Create a golden config tree:**
```
POST /configuration_manager/configs
```
```json
{
  "name": "Cisco IOS Baseline",
  "deviceType": "cisco-ios"
}
```
Response creates the tree with version `initial`, a root node, and an empty config spec:
```json
{
  "id": "699b70325ae7d527cda5fff0",
  "name": "Cisco IOS Baseline",
  "version": "initial",
  "deviceType": "cisco-ios",
  "root": {
    "name": "base",
    "attributes": {
      "devices": [],
      "deviceGroups": [],
      "remediationWorkflow": null,
      "configId": "699b70325ae7d527cda5ffef"
    },
    "children": []
  },
  "variables": {}
}
```

**Device types:** `cisco-ios`, `cisco-ios-xr`, `cisco-nx`, `arista-eos`, `json` (for non-CLI structured data like AWS Security Groups)

**`variables` are NOT set on create** — the create body only accepts `name`, `deviceType`, and `description`. Variables are set after creation via `PUT /configuration_manager/node/config` on the `base` node with `updateVariables: true`:
```json
{
  "treeId": "{treeId}",
  "treeVersion": "initial",
  "nodePath": "base",
  "data": { "template": "", "variables": { "hostname": "router.example.com" } },
  "updateVariables": true
}
```

**Bulk delete trees** — `DELETE /configuration_manager/configs` requires body `{"treeIds": ["id1", "id2"]}`. A tree cannot be deleted while it is referenced by a compliance plan — delete the plan first.

### Nodes

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/configs/{treeId}/{version}/{parentNodePath}` | Create a child node |
| PUT | `/configuration_manager/configs/{treeId}/{version}/{nodePath}` | Update a node |
| DELETE | `/configuration_manager/configs/{treeId}/{version}/{nodePath}` | Delete a node |
| POST | `/configuration_manager/configs/{treeId}/{version}/{nodePath}/devices` | Add devices to a node |
| DELETE | `/configuration_manager/configs/{treeId}/{version}/{nodePath}/devices` | Remove devices from a node |
| POST | `/configuration_manager/configs/devices/groups` | Add device groups to a node |
| DELETE | `/configuration_manager/configs/devices/groups` | Remove device groups from a node |

**Create a child node:**
```
POST /configuration_manager/configs/{treeId}/initial/base
```
```json
{
  "name": "DataCenter"
}
```
Response includes the auto-created config spec:
```json
{
  "name": "DataCenter",
  "attributes": {
    "devices": [],
    "deviceGroups": [],
    "remediationWorkflow": null,
    "configId": "699b705b5ae7d527cda5fff2"
  },
  "children": []
}
```

**Add devices to a node:**
```
POST /configuration_manager/configs/{treeId}/initial/base/DataCenter/Atlanta/devices
```
```json
{
  "devices": ["IOS-CAT8KV-1"]
}
```

**Node path format:** Node paths use the node `name` separated by `/`. Root varies by tree (e.g., `Global`, `base`). Example: `Global/EMEA/London`, `base/DataCenter/Atlanta`.

### Node Configuration (Template)

This is where you define the golden config rules for a node. You write config as a template string, and the platform parses it into structured config spec lines.

```
PUT /configuration_manager/node/config
```
```json
{
  "treeId": "699b70325ae7d527cda5fff0",
  "treeVersion": "initial",
  "nodePath": "base",
  "data": {
    "template": "service password-encryption\naaa new-model\n<e/>ntp server {{ ntp_server }}\n<i/>version {/ {{ version_regex }} /}\n{d/}ip domain-lookup",
    "variables": {
      "ntp_server": "ntp1.east.itential.com",
      "version_regex": "\\d+\\.\\d+"
    }
  },
  "updateVariables": true
}
```

- `template` - config text using golden config template syntax (see below)
- `variables` - **JSON object** (NOT a string) with variable values for `{{ var }}` substitutions
- `updateVariables` - **required boolean** - whether to merge variables into the tree-level variables

Response: `{"status": "success", "message": "Node Config updated"}`

The platform automatically parses the template text into structured `lines` in the config spec.

## Golden Config Template Syntax

The template uses special prefixes to control how each line is evaluated during compliance checks.

### Line Prefixes

Control `evalMode` and `severity` for each line:

| Prefix | evalMode | severity | Meaning |
|--------|----------|----------|---------|
| _(none)_ | `required` | `warning` | Line must exist on device |
| `<i/>` | `required` | `info` | Required, informational only |
| `<e/>` | `required` | `error` | Required, critical - fails compliance |
| `{i/}` | `ignored` | `warning` | Informational, not evaluated |
| `{i/}<i/>` | `ignored` | `info` | Ignored, info severity |
| `{i/}<e/>` | `ignored` | `error` | Ignored but flagged as error if found |
| `{d/}` | `disallowed` | `warning` | Line must NOT exist on device |
| `{d/}<e/>` | `disallowed` | `error` | Disallowed, critical |

### Variable and Pattern Syntax

| Syntax | Purpose | Example |
|--------|---------|---------|
| `{{ variable }}` | Jinja2 variable from tree variables | `ntp server {{ ntp_server }}` |
| `{/regex/}` | Inline regex pattern match | `hostname {/\S+/}` |
| `{/ {{ var }} /}` | Regex pattern from a variable | `version {/ {{ version_regex }} /}` where `version_regex` = `\d+\.\d+` |
| `{% for ... %}` / `{% endfor %}` | Jinja2 loop (generates lines from array variables) | See example below |
| Indentation | Nested config lines (interface children) | `interface Gi1.1\n description ...` |

### Regex as Variable

You can store regex patterns in tree variables and reference them in the template. This is useful when the same pattern is reused or needs to be configurable:

```
version {/ {{ version_regex }} /}
ip access-list extended ACL-VLAN100-IN
 10 permit tcp 10.100.1.0 0.0.0.255 any eq www
 {/ {{ acl_line_regex }} /} permit tcp 10.100.1.0 0.0.0.255 any eq 443
 30 deny ip any any log
```
With variables:
```json
{
  "version_regex": "\\d+\\.\\d+",
  "acl_line_regex": "^(10000|[1-9][0-9]{0,3})"
}
```

### Template Examples

**Global baseline (mixed evalModes):**
```
<i/>version {/\d+\.\d+/}
service password-encryption
{i/}hostname {/\S+/}
aaa new-model
aaa authentication login default local
<e/>ntp server {{ ntp_server }}
{d/}service internal
{d/}<e/>ip domain-lookup
```

**Interface blocks with nested children:**
```
<e/>interface GigabitEthernet1.1
 description reserved for dev1
<e/>interface GigabitEthernet1.2
 description reserved for dev2
```
Child lines (indented) inherit the parent's evalMode. The interface line is `required`+`error`, its child `description` line is also checked.

**Jinja2 loops for dynamic interface generation:**
```
{% for interface in interfaces %}
{i/}interface {{ interface['name'] }}
  {i/}description {{ interface['description']|upper }}
  {i/}ip address {{ interface['ip'] }} {{ interface['mask'] }}
  {i/}no shutdown
{% endfor %}
```
This generates lines for each entry in the `interfaces` array variable. Jinja2 filters like `|upper` are supported.

**Disallowed with regex:**
```
{d/}<e/>access-list 4 permit 14.126.166.15
{i/}<e/>access-list 5 permit {/192\.168\.1/}
```

## Config Specs

Config specs are the parsed representation of the template. When you update a node's template, the platform auto-parses it into a config spec with structured `lines`. You can also create/update config specs directly.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/config_specs` | Create a config spec |
| GET | `/configuration_manager/config_specs/{id}` | Get a config spec |
| PUT | `/configuration_manager/config_specs/{id}` | Update a config spec |
| POST | `/configuration_manager/config_template` | Get a rendered config spec template |
| POST | `/configuration_manager/generate/config_spec` | Build a config spec from raw device config |
| POST | `/configuration_manager/translate/config_spec` | Convert a config spec to readable string |

**Config spec structure:**
```json
{
  "id": "699b70325ae7d527cda5ffef",
  "deviceType": "cisco-ios",
  "template": "service password-encryption\naaa new-model\n<e/>ntp server {{ ntp_server }}",
  "lines": [
    {
      "id": "699b6f14c9ed5903",
      "words": [
        { "type": "literal", "value": "service" },
        { "type": "literal", "value": "password-encryption" }
      ],
      "lines": [],
      "evalMode": "required",
      "fixMode": "manual",
      "severity": "warning",
      "ordering": "none",
      "membership": "default"
    },
    {
      "id": "699b6f14dec62d74",
      "words": [
        { "type": "literal", "value": "ntp" },
        { "type": "literal", "value": "server" },
        { "type": "literal", "value": "ntp1.east.itential.com" }
      ],
      "lines": [],
      "evalMode": "required",
      "fixMode": "manual",
      "severity": "error",
      "ordering": "none",
      "membership": "default"
    }
  ]
}
```

**Word types:**
- `literal` - exact match (e.g., `service`, `password-encryption`)
- `variable` - matches any value, captures it
- `regex` - matches a regex pattern (from `{/pattern/}` or `{/ {{ var }} /}`)

**Config spec fields:**
- `evalMode` - `required`, `disallowed`, `ignored`
- `fixMode` - `manual` or `automatic`
- `severity` - `error`, `warning`, `info`
- `ordering` - `none` or `strict`
- `membership` - `default`
- `lines` - nested child lines (for hierarchical configs like interface blocks)

**JSON Specs** (for `json` device type):

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/json_specs/create` | Create a JSON spec |
| GET | `/configuration_manager/json_specs/{id}` | Get a JSON spec |
| PUT | `/configuration_manager/json_specs/{id}` | Update a JSON spec |

## Configuration Parsers

Parsers define how raw CLI configuration text is tokenized into words and lines for comparison against config specs. Different OS types need different parsing rules.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/configurations/parser` | Create a config parser |
| GET | `/configuration_manager/configurations/parser` | List all config parsers |
| POST | `/configuration_manager/configurations/parser/search` | Search for a parser |
| PUT | `/configuration_manager/configurations/parser` | Update a parser |
| DELETE | `/configuration_manager/configurations/parser` | Delete a parser |
| DELETE | `/configuration_manager/configurations/parsers` | Bulk delete parsers by ID array |
| POST | `/configuration_manager/import/parsers` | Import parser documents |

**Config parser structure:**
```json
{
  "id": "67c5c272cd98641b4bae74ad",
  "name": "a10-acos",
  "template": "cisco-ios",
  "lexRules": [
    ["(\\r\\n|\\r|\\n)", "end_line"],
    ["$", "end_line"],
    ["\"(?:[^\\\\\"\\r\\n]|\\\\.)*\"", "word"],
    ["\\S+", "word"]
  ]
}
```

- `name` - Parser name (typically matches the OS type)
- `template` - Base parser template to inherit rules from (e.g., `'cisco-ios'`). List available parsers with `GET /configuration_manager/configurations/parser`.
- `lexRules` - Array of `[regex_pattern, token_type]` pairs. Token types: `end_line`, `word`, `comment`. Patterns are validated with `safe-regex` — unsafe patterns are rejected.

## Compliance Plans

Compliance plans group golden config nodes with their target devices into a runnable plan. Running a plan triggers compliance checks for all nodes and produces a batch of reports.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/compliance_plans` | Create a compliance plan |
| GET | `/configuration_manager/compliance_plans/{planId}` | Get a compliance plan |
| PUT | `/configuration_manager/compliance_plans` | Update a compliance plan |
| DELETE | `/configuration_manager/compliance_plans` | Delete compliance plans — body: `{"planIds": ["id1"]}` |
| POST | `/configuration_manager/compliance_plans/run` | Run a compliance plan |
| POST | `/configuration_manager/compliance_plans/nodes` | Add nodes to a compliance plan |
| DELETE | `/configuration_manager/compliance_plans/nodes` | Remove nodes from a compliance plan |
| POST | `/configuration_manager/search/compliance_plans` | Search compliance plans |
| POST | `/configuration_manager/search/compliance_plan_instances` | Search plan run instances |
| POST | `/configuration_manager/import/plans` | Import compliance plan documents |

**Create a compliance plan:**
```
POST /configuration_manager/compliance_plans
```
```json
{
  "name": "IOS Baseline Compliance",
  "options": {
    "description": "Checks all Cisco IOS devices against the baseline golden config",
    "nodes": [
      {
        "treeId": "699b70325ae7d527cda5fff0",
        "version": "initial",
        "nodeId": "699b705b5ae7d527cda5fff3",
        "devices": ["IOS-CAT8KV-1"],
        "deviceGroups": [],
        "variables": {}
      }
    ]
  }
}
```

**Node fields (all required):**
- `treeId` - the golden config tree ID
- `version` - tree version (e.g., `"initial"`)
- `nodeId` - the **`configId`** of the node (NOT the node name)
- `devices` - array of device names to check
- `deviceGroups` - array of device group IDs (use `[]` if none)
- `variables` - variable overrides for this node (use `{}` if none)

**Response:**
```json
{
  "_id": "699b8c3b5ae7d527cda5fff6",
  "name": "IOS Baseline Compliance",
  "description": "Checks all Cisco IOS devices against the baseline golden config",
  "throttle": 5,
  "nodes": [
    {
      "treeId": "699b70325ae7d527cda5fff0",
      "version": "initial",
      "nodeId": "699b705b5ae7d527cda5fff3",
      "variables": {},
      "devices": ["IOS-CAT8KV-1"],
      "deviceGroups": []
    }
  ]
}
```

**Run a compliance plan:**
```
POST /configuration_manager/compliance_plans/run
```
```json
{
  "planId": "699b8c3b5ae7d527cda5fff6",
  "options": {}
}
```
Response:
```json
{
  "message": "Successfully started compliance plan.",
  "planId": "699b8c3b5ae7d527cda5fff6",
  "instanceId": "699b8c4a5ae7d527cda5fff7"
}
```

**Get plan run instance** (shows status, processed devices, batch ID):
```
POST /configuration_manager/search/compliance_plan_instances
```
```json
{
  "searchParams": {
    "instanceId": "699b8c4a5ae7d527cda5fff7"
  }
}
```
Response (plans are inside `groups[]`, not top-level):
```json
{
  "totalCount": 1,
  "groups": [
    {
      "totalCount": 1,
      "plans": [
        {
          "id": "699b8c4a5ae7d527cda5fff7",
          "name": "IOS Baseline Compliance",
          "jobStatus": "complete",
          "planId": "699b8c3b5ae7d527cda5fff6",
          "batchId": "699b8c4a5ae7d527cda5fff8",
          "started": "2026-02-22T23:07:54.697Z",
          "finished": "2026-02-22T23:07:59.735Z",
          "nodes": [
            {
              "treeId": "699b70325ae7d527cda5fff0",
              "nodeId": "699b705b5ae7d527cda5fff3",
              "status": "completed",
              "devices": ["IOS-CAT8KV-1"],
              "processedDevices": ["IOS-CAT8KV-1"]
            }
          ]
        }
      ]
    }
  ]
}
```
Use the `batchId` to retrieve compliance reports via `GET /configuration_manager/compliance_reports/batch/{batchId}`.

**Add nodes to an existing plan:**
```
POST /configuration_manager/compliance_plans/nodes
```
```json
{
  "planId": "699b8c3b5ae7d527cda5fff6",
  "nodes": [
    {
      "treeId": "699b70325ae7d527cda5fff0",
      "version": "initial",
      "nodeId": "699b705b5ae7d527cda5fff2",
      "devices": ["IOS-CAT8KV-2"],
      "deviceGroups": [],
      "variables": {}
    }
  ]
}
```

## Compliance Reports

Results of compliance checks showing what passed, what failed, and what needs remediation.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/configuration_manager/compliance_reports` | Run compliance reports |
| GET | `/configuration_manager/compliance_reports/details/{reportId}` | Get a compliance report |
| GET | `/configuration_manager/compliance_reports/batch/{batchId}` | Get reports for a batch |
| POST | `/configuration_manager/compliance_reports/grade` | Get graded compliance reports for a node |
| POST | `/configuration_manager/compliance_reports/grade/history` | Get historical graded reports |
| POST | `/configuration_manager/compliance_reports/grade/single` | Grade a single report |
| POST | `/configuration_manager/compliance_reports/history` | Compliance report totals for a device |
| POST | `/configuration_manager/compliance_reports/topissues` | Get top issues from reports |
| GET | `/configuration_manager/compliance_reports/tree/{treeId}` | Summarize reports for a tree |
| GET | `/configuration_manager/compliance_reports/node/{treeId}/{nodePath}` | Summarize reports for a node |
| POST | `/configuration_manager/compliance_reports/backups` | Run compliance on backup configs |
| POST | `/configuration_manager/compliance_reports/config` | Run compliance against a raw config string |
| POST | `/configuration_manager/compliance_reports/details` | Get details of multiple reports at once |
| POST | `/configuration_manager/compliance_reports/history/backups` | Compliance report history for backups |
| POST | `/configuration_manager/compliance_reports/query/history` | Paginated grading history |

**Run compliance:**
```
POST /configuration_manager/compliance_reports
```
```json
{
  "options": {
    "treeId": "699b70325ae7d527cda5fff0",
    "version": "initial",
    "nodePath": "base/DataCenter/Atlanta",
    "devices": ["IOS-CAT8KV-1"]
  }
}
```
Response (async - compliance runs in background):
```json
{
  "status": 202,
  "message": "compliance batch 699b70d55ae7d527cda5fff4 started",
  "batchId": "699b70d55ae7d527cda5fff4"
}
```

**Run compliance against a raw config string** (without fetching from device):
```
POST /configuration_manager/compliance_reports/config
```
```json
{
  "options": {
    "treeId": "699b70325ae7d527cda5fff0",
    "version": "initial",
    "nodePath": "base/DataCenter/Atlanta",
    "deviceName": "IOS-CAT8KV-1",
    "configuration": "service password-encryption\naaa new-model\n..."
  }
}
```
Useful for testing compliance against a config you already have (e.g., from a backup or generated config) without connecting to the device.

**Get batch results** (returns array of report summaries):
```
GET /configuration_manager/compliance_reports/batch/{batchId}
```
Each entry has `id` (report ID), `batchId`, `treeId`, `nodePath`, `deviceName`, `specId`, `inheritedSpecIds`.

**Get detailed report:**
```
GET /configuration_manager/compliance_reports/details/{reportId}
```
```json
{
  "id": "699b70d95ae7d527cda5fff5",
  "deviceName": "IOS-CAT8KV-1",
  "nodePath": "base/DataCenter/Atlanta",
  "timestamp": "2026-02-22T21:03:16.136Z",
  "inheritedSpecIds": ["699b70325ae7d527cda5ffef", "699b705b5ae7d527cda5fff2"],
  "totals": {
    "errors": 1,
    "warnings": 2,
    "infos": 0,
    "passes": 7
  },
  "issues": [
    {
      "severity": "error",
      "type": "required",
      "message": "Required config not found",
      "spec": {
        "words": [
          {"type": "literal", "value": "ntp"},
          {"type": "literal", "value": "server"},
          {"type": "literal", "value": "ntp1.east.itential.com"}
        ],
        "evalMode": "required",
        "severity": "error"
      }
    }
  ]
}
```

**Report fields:**
- `totals` - counts of `errors`, `warnings`, `infos`, `passes`
- `issues` - array of violations, each with `severity`, `type` (required/disallowed), `message`, and the `spec` line that failed
- `inheritedSpecIds` - parent node specs that were also evaluated (shows inheritance in action)

## Compliance Grading

Compliance reports can be graded to produce a score and letter grade.

**Scoring formula:**
```
Score = (totalNumPassLines / ((numOfErrorLines * errorWeight) + (numOfWarnLines * warnWeight) + (numOfInfoLines * infoWeight) + totalNumPassLines)) * 100
```

**Default severity weights:**
| Severity | Weight |
|----------|--------|
| Error | 2 |
| Warning | 1 |
| Info | 0.5 |

**Default grade benchmarks:**
| Grade | Minimum Score |
|-------|--------------|
| Pass | 90 |
| Review | 80 |
| Fail | 0 |

Errors count double because they represent critical compliance violations.

**Grade a report:**
```
POST /configuration_manager/compliance_reports/grade/single
```
```json
{
  "reportId": "699b70d95ae7d527cda5fff5"
}
```

## Remediation

> **This skill does not remediate. NEVER wire a Configuration Manager remediation task that pushes golden-config/compliance-derived changes onto a device — auto *or* human-reviewed.** The job of Golden Config is to define the standard, check devices against it, and grade the result. Applying a fix to a device is a separate, deliberately-designed config-push delivery with its own change control — not something Golden Config does automatically.

**Prohibited tasks (never wire any of these into a workflow, never suggest them):**

| Task | App | What it (wrongly) does here |
|------|-----|------------------------------|
| `runAutoRemediation` | ConfigurationManager | Auto-fixes the device from the compliance report |
| `advancedAutoRemediation` | ConfigurationManager | Auto-fix with extra options |
| `convertChangesToConfig` | ConfigurationManager | Converts compliance patch data into device config (auto-remediation plumbing) |
| `patchDeviceConfiguration` | ConfigurationManager | Alters the device configuration |
| `advancedPatchDeviceConfiguration` | ConfigurationManager | Alters the device configuration with options |
| `patchCMDeviceConfiguration` | IAP (legacy) | Alters a device configuration to achieve compliance |
| `ManualRemediation` | ConfigurationManager | Generates GC-derived device changes for review/apply |
| `ManualRemediationResults` | ConfigurationManager | Applies the manual-remediation results to the device |

There is **no exception** — not even when a spec asks for fully automatic remediation with no human in the loop. (Itential is also deprecating the auto-remediation feature: `updateNodeConfig` and `convertChangesToConfig` are deprecated in Platform 6.5 and removed in Platform 7 — see the [deprecation notice](https://docs.itential.com/itential-platform/release-notes/deprecations/autoremediation-tasks). Building on it is a dead end regardless.)

**If a spec calls for remediation, do this instead:**
1. This skill produces the compliance report — the list of violations (`issues`) per device.
2. Hand those violations to a **config-push delivery** built with `/builder-agent`: render the corrective configuration, then push it through the **config-push mechanism available in the environment**, with the normal dry-run → approval → commit pattern that any config change gets. **Which push task to use depends on what the platform has configured** — check the task catalog / adapters first, don't assume. Common options:
   - **`sendConfig`** (GatewayManager) — "Send configuration to inventory nodes" via an Automation Gateway
   - **`runService`** (GatewayManager) — run a gateway service such as the `itential_cli` Ansible role
   - **`netmikoSendConfig` / `netmikoSendConfigSet`** (AG) — netmiko-based config push
   - whatever vendor/SSH adapter the environment uses for config push

   See `/builder-agent`'s config-push pattern and the Arista EOS "Push Configuration to Device - IAG" workflow in `helpers/assets/vendor-arista-eos.json`.
3. Re-run compliance (this skill) afterward to confirm the device is back in standard.

This keeps detection (Golden Config) and correction (a reviewed config-push) cleanly separated, and survives the Platform 7 removal of auto-remediation.

> Note: `updateNodeConfig` is **not** prohibited — it authors the Golden Config **node template** (the standard), it does not touch a device. Likewise `applyDeviceConfig`/`applyDeviceTemplate` are generic config-apply tasks; they're fine for a deliberate push delivery but must never be wired to auto-apply changes derived from a compliance report.

## Helper JSON Templates

| File | API Call | Description |
|------|----------|-------------|
| `create-golden-config-tree.json` | `POST /configuration_manager/configs` | Create a golden config tree |
| `reference-golden-config-tree.json` | `POST /configuration_manager/import/goldenconfigs` | Full multi-region tree reference (Global → EMEA/NA/APAC with node templates and variables) |
| `update-node-config.json` | `PUT /configuration_manager/node/config` | Update node template with all syntax features |
| `create-golden-config-node.json` | `POST /configuration_manager/configs/{treeId}/{version}/{parentPath}` | Create a child node |
| `add-devices-to-node.json` | `POST /configuration_manager/configs/{treeId}/{version}/{nodePath}/devices` | Assign devices |
| `run-compliance.json` | `POST /configuration_manager/compliance_reports` | Run compliance directly (async) |
| `create-compliance-plan.json` | `POST /configuration_manager/compliance_plans` | Create a compliance plan with nodes, devices, variables |
| `run-compliance-plan.json` | `POST /configuration_manager/compliance_plans/run` | Run a compliance plan |

## Developer Scenarios

### 1. Set up golden config compliance from scratch
```
1. POST /configuration_manager/configs → create tree with {name, deviceType}
2. PUT /configuration_manager/node/config → write template with prefixes, variables, regex
3. POST /configuration_manager/configs/{treeId}/initial/base → create child nodes
4. PUT /configuration_manager/node/config → set child node templates (inherited + overrides)
5. POST /configuration_manager/configs/{treeId}/initial/{nodePath}/devices → assign devices
6. POST /configuration_manager/compliance_reports → run compliance (returns batchId)
7. GET /configuration_manager/compliance_reports/batch/{batchId} → get report IDs
8. GET /configuration_manager/compliance_reports/details/{reportId} → see totals + issues
9. POST /configuration_manager/compliance_reports/grade/single → grade the report
```

### 2. Build config spec from existing device config
```
1. GET /configuration_manager/devices/{name}/configuration → get live config
2. POST /configuration_manager/generate/config_spec → auto-generate spec from raw config
3. Use the generated spec as a starting template for your golden config node
```

### 3. Import/Export for CI/CD
```
POST /configuration_manager/export/goldenconfigs → export tree as JSON
POST /configuration_manager/import/goldenconfigs → import to another environment
```

````

============================================================
FILE: .claude/skills/itential-inventory/SKILL.md
DIRECTORY: .claude/skills/itential-inventory/
FILENAME: SKILL.md
============================================================
SHA256: 611adf352f7cd4406a1ece4d1ccdf8844319e98add7856731ee1c97a49deee25

````markdown
---
name: itential-inventory
description: Manage device inventories, nodes, actions, and tags in Itential Inventory Manager. Use when working with IAG5 inventory, bulk node population, or running actions against inventory devices.
argument-hint: "[action or inventory-name]"
---

# Inventory Manager - Developer Skills Guide

Inventory Manager provides centralized device and endpoint inventory for the Itential Platform. It maintains inventories of nodes (devices/targets), with actions that can be executed against them via IAG5 services. Required for IAG5 and Configuration Manager Enterprise.

## Concepts

- **Inventory** — a named collection of nodes with associated actions. Has groups for access control.
- **Node** — a device or target within an inventory. Has a name, attributes (key-value pairs like host, platform, credentials), and tags.
- **Action** — an operation that can be run against nodes. Currently only `iag5-service` type. Links to IAG services via `service_name` and `cluster_id`.
- **Tag** — a label for organizing inventories and nodes. Auto-created on first use, auto-cleaned when unused. Stored lowercase.

## Gotchas

- Response shape is `{status: "Success", result: {...}}` — extract data from `result`, not top-level
- Paginated responses inside `result` use `{data: [...], totalRecords, currentPage, pageSize, totalPages}`
- Inventories require at least one `group` — without it, creation fails
- Node names must be unique within an inventory (database constraint on `inventory_id + name`)
- `populateInventory` (bulk) **clears ALL existing nodes first** before inserting — it's a full replace, not append
- Action names must be unique within an inventory
- Only `iag5-service` action type is currently supported
- `cluster_id` resolves from `action_config.cluster_id` first, then falls back to `node.attributes.cluster_id`
- Tag names are stored lowercase — `"Core"` becomes `"core"`
- Identifiers accept both MongoDB ObjectId and name strings — auto-detected
- `createBrokerActions: true` auto-creates 4 standard actions (get-config, set-config, run-command, is-alive) — requires `defaultClusterId`

## API Reference

**Base Path:** `/inventory_manager/v1`

### Inventories

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/inventory_manager/v1/inventories` | Create a new inventory |
| GET | `/inventory_manager/v1/inventories` | List inventories with filtering and pagination |
| GET | `/inventory_manager/v1/inventories/{identifier}` | Get inventory by ID or name |
| DELETE | `/inventory_manager/v1/inventories/{identifier}` | Delete an inventory |
| GET | `/inventory_manager/v1/stats` | Get overview stats (total inventories, nodes, actions) |

**Create an inventory:**
```
POST /inventory_manager/v1/inventories
```
```json
{
  "name": "Lab Routers",
  "description": "Routers in the Atlanta Lab",
  "groups": ["Solutions Engineering"],
  "tags": ["routers", "lab"],
  "actions": [
    {
      "name": "get-config",
      "action_type": "iag5-service",
      "action_config": {
        "service_name": "get-config",
        "cluster_id": "labCluster"
      },
      "action_parameters": {}
    }
  ]
}
```
- `name` — required, must be unique
- `groups` — required, at least one group name for access control
- `tags` — optional, auto-created if they don't exist
- `actions` — optional, define operations runnable against nodes

**Or use `createBrokerActions` for standard actions:**
```json
{
  "name": "DC Switches",
  "description": "Data center switches",
  "groups": ["Solutions Engineering"],
  "createBrokerActions": true,
  "defaultClusterId": "dcCluster"
}
```
This auto-creates 4 actions: `get-config`, `set-config`, `run-command`, `is-alive` — all as `iag5-service` type pointing to the specified cluster.

**Response:**
```json
{
  "status": "Success",
  "result": {
    "_id": "697eb0fc4aef5efec3d7bbcf",
    "name": "Lab Routers",
    "groups": ["67c85954abe686cf9cb78b2e"],
    "description": "Routers in the Atlanta Lab",
    "actions": [
      {
        "name": "get-config",
        "action_type": "iag5-service",
        "action_config": {"service_name": "get-config", "cluster_id": "labCluster"},
        "action_parameters": {},
        "created_at": "2026-02-01T01:48:44.786Z",
        "created_by": "Pronghorn"
      }
    ],
    "tags": ["routers", "lab"]
  }
}
```

**List inventories with filtering:**
```
GET /inventory_manager/v1/inventories?page=1&pageSize=25&search=router&tags=core&sortField=name&sortOrder=1
```

**Query parameters:**
- `page` — page number (default 1)
- `pageSize` — results per page (default 25)
- `sortField` — field to sort by
- `sortOrder` — `1` ascending, `-1` descending
- `search` — text search across name/description
- `names` — filter by inventory names (array)
- `groups` — filter by group IDs or names
- `tags` — filter by tag names
- `minNodes` / `maxNodes` — filter by node count

**Stats:**
```
GET /inventory_manager/v1/stats
```
```json
{
  "status": "Success",
  "result": {
    "totalInventories": 1,
    "totalNodes": 2,
    "totalActions": 4
  }
}
```

### Nodes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/inventory_manager/v1/nodes` | List all nodes with filtering and pagination |
| GET | `/inventory_manager/v1/inventories/{identifier}/nodes` | List nodes for a specific inventory |
| GET | `/inventory_manager/v1/inventories/{inventoryId}/nodes/{nodeId}` | Get a single node |
| POST | `/inventory_manager/v1/nodes/bulk` | Bulk populate inventory with nodes (replaces all existing) |
| DELETE | `/inventory_manager/v1/nodes/clear/{identifier}` | Clear all nodes from an inventory |
| POST | `/inventory_manager/v1/nodes/expand` | Expand node identifiers to full documents |
| POST | `/inventory_manager/v1/nodes/filter/build` | Build filter structure for service execution |

**Bulk populate an inventory with nodes:**
```
POST /inventory_manager/v1/nodes/bulk
```
```json
{
  "inventory_identifier": "Lab Routers",
  "nodes": [
    {
      "name": "core-router-1",
      "attributes": {
        "itential_host": "10.1.1.1",
        "itential_platform": "iosxr",
        "cluster_id": "cluster_east",
        "itential_user": "$SECRET.network_devices.username",
        "itential_password": "$SECRET.network_devices.password"
      },
      "tags": ["core", "datacenter-1"]
    },
    {
      "name": "core-router-2",
      "attributes": {
        "itential_host": "10.1.1.2",
        "itential_platform": "iosxr",
        "cluster_id": "cluster_east"
      },
      "tags": ["core", "datacenter-1"]
    }
  ]
}
```
- `inventory_identifier` — inventory name or ID
- **WARNING:** This clears ALL existing nodes first, then inserts. It's a full replace, not append.
- Tags are auto-created if they don't exist
- Node names must be unique within the inventory

**Response:**
```json
{
  "status": "Success",
  "result": {
    "data": [
      {
        "_id": "697eb1be4aef5efec3d7bbd2",
        "inventory_id": "697eb0fc4aef5efec3d7bbcf",
        "name": "core-router-1",
        "attributes": {"itential_host": "10.1.1.1", "itential_platform": "iosxr", ...},
        "tags": ["core", "datacenter-1"]
      }
    ],
    "totalRecords": 2,
    "currentPage": 1,
    "pageSize": 25,
    "totalPages": 1
  }
}
```

**Node attributes:** Arbitrary key-value pairs. Common patterns:
- `itential_host` — device IP or hostname
- `itential_platform` — OS type (iosxr, ios, eos, etc.)
- `itential_user` / `itential_password` — credentials (use `$SECRET.` prefix for vault references)
- `cluster_id` — IAG cluster for this node (used as fallback if action doesn't specify one)

### Actions

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/inventory_manager/v1/actions` | List all actions across all inventories |
| GET | `/inventory_manager/v1/inventories/{identifier}/actions` | List actions for a specific inventory |
| GET | `/inventory_manager/v1/inventories/{identifier}/actions/{actionId}` | Get a single action |
| POST | `/inventory_manager/v1/inventories/{identifier}/actions` | Create a new action |
| DELETE | `/inventory_manager/v1/inventories/{identifier}/actions/{actionId}` | Delete an action |

**Create an action:**
```
POST /inventory_manager/v1/inventories/Lab%20Routers/actions
```
```json
{
  "name": "backup-config",
  "action_type": "iag5-service",
  "action_config": {
    "service_name": "backup-config",
    "cluster_id": "labCluster"
  },
  "action_parameters": {}
}
```
- `action_type` — currently only `"iag5-service"` is supported
- `action_config.service_name` — the IAG service to call (required)
- `action_config.cluster_id` — IAG cluster (optional, falls back to node's `cluster_id` attribute)

**Action execution** (via workflow task `InventoryManager.runInventoryAction`):
- Calls `GatewayManager.runService` with the action's `service_name` and `cluster_id`
- Response is JSON-RPC wrapped (same as IAG service responses)
- Non-zero `return_code` or error status throws an error

### Tags

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/inventory_manager/v1/tags` | List all tags with pagination |
| GET | `/inventory_manager/v1/tags/accessible` | Get tags from accessible inventories only |
| GET | `/inventory_manager/v1/tags/{identifier}` | Get a single tag by ID or name |
| GET | `/inventory_manager/v1/tags/{identifier}/usage` | Get usage statistics for a tag |
| POST | `/inventory_manager/v1/tags/search` | Find inventories and nodes by tags |

**Search by tags:**
```
POST /inventory_manager/v1/tags/search
```
```json
{
  "tagIdentifiers": ["core", "datacenter-1"]
}
```
- Field is `tagIdentifiers`, NOT `tags`
- Returns `{inventories: [...], nodes: [...]}` matching the specified tags

## How It Connects to IAG

Inventory Manager is the bridge between device inventory and IAG5 services:

```
Inventory (Lab Routers)
  ├── Nodes: core-router-1, core-router-2
  │     └── attributes: host, platform, cluster_id, credentials
  │
  ├── Actions: get-config, set-config, run-command, is-alive
  │     └── each action → IAG5 service via GatewayManager.runService
  │
  └── In a workflow:
        InventoryManager.runInventoryAction
          → resolves node attributes + action config
          → calls GatewayManager.runService(serviceName, clusterId, params, inventory)
          → returns JSON-RPC response
```

To use inventory nodes in IAG workflow tasks, the `inventory` parameter in `GatewayManager.runService` takes:
```json
[{"inventory": "Lab Routers", "nodeNames": ["core-router-1"]}]
```

## RBAC

Access is controlled through groups:
- `inventory:read` — list, get, search
- `inventory:create` — create inventories, nodes, tags
- `inventory:update` — update inventories, nodes, actions
- `inventory:delete` — delete inventories, nodes, actions
- `inventory:run` — execute actions

Users must be in a group with the required role. The Pronghorn internal account bypasses authorization.

## Developer Scenarios

### 1. Create an inventory with devices and test an action
```
1. POST /inventory_manager/v1/inventories        → create with groups + createBrokerActions
2. POST /inventory_manager/v1/nodes/bulk          → populate with device nodes
3. GET  /inventory_manager/v1/inventories/{name}  → verify inventory + actions
4. In a workflow: InventoryManager.runInventoryAction on a node
5. Or via GatewayManager.runService with inventory parameter
```

### 2. Organize with tags
```
1. Create inventory with tags: ["production", "datacenter-1"]
2. Add nodes with tags: ["core", "border"]
3. POST /inventory_manager/v1/tags/search → find all "core" nodes across inventories
4. GET  /inventory_manager/v1/tags/{name}/usage → see how many inventories/nodes use a tag
```

### 3. Bulk refresh inventory from external source
```
1. Pull device list from external system (CMDB, IPAM, etc.)
2. Transform to node format: [{name, attributes, tags}, ...]
3. POST /inventory_manager/v1/nodes/bulk → replaces all nodes (WARNING: clears first)
4. Verify: GET /inventory_manager/v1/inventories/{name}/nodes
```

````

============================================================
FILE: .claude/skills/itential-json-forms/SKILL.md
DIRECTORY: .claude/skills/itential-json-forms/
FILENAME: SKILL.md
============================================================
SHA256: 76fe49f256d4e82c93e7d32e8d7c3a9e79971c46b08b4825a0eb9777efa3221b

````markdown
---
name: itential-json-forms
description: Build IAP JSON Forms — static-enum dropdowns, REST-bound dropdowns (live data pulled from IAP endpoints), and cascading dropdowns (aka field dependency — one field's value drives another's URL path param). Use when creating, updating, or wiring forms consumed by manual triggers, manual tasks (ShowJsonForm), or any UI surface that needs a structured input panel.
argument-hint: "[form name or operation]"
---

# JSON Forms (itential-json-forms)

JSON Forms are reusable form definitions stored in the `json-forms` application. They drive structured input panels across IAP — manual triggers in Operations Manager, the `JsonForms/ShowJsonForm` manual task, and any workflow surface that prompts a user for typed input.

A form is a single document with four cooperating schemas — `struct` (UI rendering), `schema` (data contract / validation), `uiSchema` (per-field widget hints), and `bindingSchema` (live-data binding for REST dropdowns). Get the relationships wrong and the form will render but break silently at runtime.

## Concepts

- **`struct`** — the UI definition. `struct.type` is always `"array"`; `struct.items[]` is the list of fields. `customKey` on each field becomes the property key in `schema` and the variable key when the form's data is consumed.
- **`schema`** — the data contract. `schema.properties.<customKey>` must exist for every field in `struct.items[]` (and stay in sync with the field's type, enum values, etc.). `schema.required` lists mandatory `customKey`s.
- **`uiSchema`** — per-`customKey` widget hints: placeholder text, `ui:widget` overrides, disabled flags. Required for cascading dropdowns (see below).
- **`bindingSchema`** — empty `{}` for static-enum forms. Required (and non-trivial) for REST-bound dropdowns: every REST-bound field needs a mirroring `bindingSchema.properties.<customKey>` entry. Studio fills this in invisibly through the GUI; the server does not.
- **Static vs. REST-bound dropdowns** — static dropdowns hardcode the list via `enum`/`enumNames`. REST-bound dropdowns pull options live from an IAP endpoint at form-render time.
- **Cascading dropdowns** (aka **field dependency** in the Studio UI) — a REST-bound dropdown whose URL path parameter is filled from another field's current value. The dependent field re-fetches when the source field changes.

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/json-forms/forms` | List all JSON forms |
| GET | `/json-forms/forms/{id}` | Fetch a single form |
| POST | `/json-forms/forms` | Create a JSON form |
| PUT | `/json-forms/forms/{id}` | Update a JSON form (full replacement — see Update below) |
| DELETE | `/json-forms/forms` | Bulk delete — body `{"ids":["...","..."]}`. There is no per-id DELETE endpoint; per-id calls 404. |
| GET | `/automation-studio/json-forms/method-options` | Canonical list of bindable endpoints (same list Studio shows in its dropdown picker) |

## Create a JSON Form

```
POST /json-forms/forms
```

Choose the helper that matches your form's dropdown needs:

| Use case | Annotated scaffold (fill in the blanks) | Real export (read to see the actual shape) |
|---|---|---|
| Static-enum dropdowns only (hardcoded option lists) | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-json-form.json` | `${CLAUDE_PLUGIN_ROOT}/helpers/assets/json-form-example-static-enum.json` — real Cisco IOS "Port Turn Up" form, 8 fields incl. static dropdown, number `updown` widgets, `ipv4` format validation |
| REST-bound dropdowns (live data from IAP endpoints) | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-json-form-rest-bound.json` | `${CLAUDE_PLUGIN_ROOT}/helpers/assets/json-form-example-rest-bound.json` — real Cisco IOS "Compliance" form, one REST-bound dropdown pulling tree names live from `GET /configuration_manager/configs` |
| Cascading dropdowns (field dependency) | `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-json-form-rest-bound.json` (Inventory Manager Site/Device cascade worked example) | *(no real cascading export on hand yet — the scaffold is hand-built but follows the same field shapes as the two real exports above)* |

The scaffolds are annotated with `_comment_*` fields to fill in; the real exports are genuine `POST /json-forms/forms` payloads pulled from a live platform (IDs/timestamps/`createdBy` stripped since the server assigns those on create) — read one when you want to see exactly what a working form looks like end-to-end, not just the shape.

### Static-enum dropdowns

`enum`/`enumNames` arrays appear in both `struct.items[i]` and `schema.properties.<customKey>` — they must stay in sync.

- `struct.items[i].enum` / `enumNames` are arrays of `{id, label, value}` objects.
- `schema.properties.<customKey>.enum` / `enumNames` are **flat string arrays** of the same values (not objects).

Leave `bindingSchema: {}` for static-enum forms.

### REST-bound dropdowns

When options should reflect live platform state (devices, inventories, projects, templates) instead of a hardcoded list, the dropdown pulls from a GET against an IAP endpoint at render time. Three things must line up:

1. **`struct.type` MUST be `"array"`** (not `"object"`). The static-enum scaffold uses `"array"` too — keep it.
2. **`bindingSchema.properties.<customKey>` must mirror every REST-bound field.** Studio reverse-engineers `bindingSchema` from `struct` in the GUI, but the server does not — leaving `bindingSchema: {}` produces dropdowns that render but never fetch.
3. **Endpoint discovery:** `GET /automation-studio/json-forms/method-options` returns the canonical list of bindable endpoints — the same list Studio shows in its dropdown picker.

Per-field shape in `struct.items[i]`:

```jsonc
{
  "type": "string",
  "title": "Site",
  "binding": true,
  "rel": "collection",
  "targetPointer": "/enum",
  "method": "GET",
  "base": "/inventory_manager",
  "href": "/v1/inventories",
  "sourcePointer": "/result/data",
  "sourceKeyPointer": "/name",
  "customKey": "site"
}
```

- `base + href` is the endpoint.
- `sourcePointer` is a JSON pointer into the response, walked to the array of items.
- `sourceKeyPointer` is the per-item field that becomes BOTH the value and the label. **`labelKeyPointer` is unused** — both columns come from `sourceKeyPointer`.

### Cascading dropdowns (aka field dependency)

The Studio UI labels this pattern **field dependency**; the form JSON calls it cascading. Same feature, two names. A REST-bound dropdown whose URL path parameter is filled from another field's value (e.g., dropdown 2 lists devices from the inventory selected in dropdown 1):

- The dependent dropdown's `href` stays as a **TEMPLATE** with placeholders: `/v1/inventories/:inventoryIdentifier/nodes`. **Path params use `:name` colon syntax, NOT `{name}` curly braces.**
- A `variables` array maps each placeholder to a JSON pointer into form data: `[{"name": "inventoryIdentifier", "reference": "/site"}]` substitutes `:inventoryIdentifier` with whatever value the field whose `customKey` is `site` currently holds.
- The same `variables` array must appear in **both** places:
  - `struct.items[i].variables`
  - `bindingSchema.properties.<dependentKey>.binding:hyperSchema.links[0].variables`
- **Both the source and the dependent field need `ui:widget: "DependencyWidget"`** in `uiSchema` — without it, the runtime will not re-fetch when the source changes.

## Update a JSON Form

```
PUT /json-forms/forms/{id}
```

- Body MUST be wrapped in `{"options": {...}}`.
- Include ALL fields the form already has: `created`, `createdBy`, `lastUpdated`, `lastUpdatedBy`, `name`, `description`, `struct`, `schema`, `uiSchema`, `validationSchema`, `bindingSchema`, `version`.
- This is a **full replacement** — omitting any field clears it.

## Delete JSON Forms

Bulk-only:

```
DELETE /json-forms/forms
Body: {"ids": ["<id1>", "<id2>", ...]}
```

Per-id calls (`DELETE /json-forms/forms/<id>`) return 404 — the endpoint does not exist.

## Wiring to a Manual Trigger

A JSON Form is consumed by an Operations Manager **manual trigger** that hands the user's form input to a workflow as job variables. See `builder-agent` for the trigger creation details.

**Critical flag — `legacyWrapper: false`:** The default is `true`, which wraps form field values under a `formData` object and breaks the mapping to workflow job variables. Set `legacyWrapper: false` so each form field maps directly to a workflow input variable by name (i.e., field `customKey: "device_name"` → job variable `device_name`).

Required trigger fields: `name`, `type` (`"manual"`), `enabled`, `actionType` (`"automations"`), `actionId`, `formId`, `legacyWrapper`.

Helper for the wired-up trigger: `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-ops-manager-trigger-manual.json`.

## Common Gotchas

- **`struct.type` is `"array"`, not `"object"`.** Forms with `"object"` render empty.
- **`bindingSchema` mirroring is mandatory for REST-bound fields.** Studio hides this in the GUI; an API-created form needs both `struct.items[i]` AND `bindingSchema.properties.<customKey>` populated, or the dropdown renders and never fetches.
- **`:name` colon syntax in `href`, not `{name}`.** Curly-brace placeholders are silently ignored.
- **`enum`/`enumNames` flat-vs-object asymmetry.** In `struct.items[i]` they're `{id, label, value}` objects; in `schema.properties.<customKey>` they're flat string arrays.
- **`DependencyWidget` required on BOTH ends of a cascade.** Easy to remember to set it on the dependent field and forget the source — without the source-side widget the dependent won't re-fetch.
- **`labelKeyPointer` is a red herring.** Don't bother setting it; both label and value come from `sourceKeyPointer`.
- **Bulk DELETE has no per-id alternative.** Always send `{"ids":[...]}` to `/json-forms/forms`.

## See Also

- `builder-agent` for workflows that consume form output, manual-trigger wiring, and project-level component management.
- Helper files in `${CLAUDE_PLUGIN_ROOT}/helpers/`:
  - `create/create-json-form.json` — static-enum scaffold
  - `create/create-json-form-rest-bound.json` — REST-bound + cascading scaffold (Inventory Manager Site/Device cascade worked example)
  - `create/create-ops-manager-trigger-manual.json` — manual trigger that consumes a form
  - `assets/json-form-example-static-enum.json` — real export, static-enum (Cisco IOS Port Turn Up)
  - `assets/json-form-example-rest-bound.json` — real export, REST-bound (Cisco IOS Compliance)

````

============================================================
FILE: .claude/skills/itential-lcm/SKILL.md
DIRECTORY: .claude/skills/itential-lcm/
FILENAME: SKILL.md
============================================================
SHA256: c00d7cc5b0db0bfce1aa2ba7e5344aab6e1ca9730319086e0cf6e10cf48324ef

````markdown
---
name: itential-lcm
description: Manage resource models, instances, actions, and lifecycle execution in Itential Lifecycle Manager. Use when defining reusable service models, running actions against resource instances, or tracking action execution history.
argument-hint: "[action or resource-name]"
---

# Lifecycle Manager - Developer Skills Guide

Lifecycle Manager (LCM) provides a declarative framework for managing the lifecycle of reusable resources. Define a resource model (schema + actions), create instances of it, and run workflow-driven actions to create, update, or delete those instances — with full execution history and optional pre/post transformations.

## Concepts

- **Resource Model** — a template defining what a resource looks like (JSON Schema) and what actions can be performed on it. Actions link to workflows.
- **Resource Instance** — a concrete instantiation of a model. Stores `instanceData` conforming to the model's schema. Tracks state and last action.
- **Action** — an operation on an instance (create, update, delete, import). Each action can have a workflow, pre-transformation, and post-transformation.
- **Action Execution** — an audit record of running an action. Tracks 3 phases: preTransformation → workflow → postTransformation.
- **Instance Group** — a collection of instances (manual list or dynamic filter) for bulk operations. Requires `LCM_GROUPS_ENABLED=true`.

## Gotchas

- Base path is `/lifecycle-manager` (hyphens), NOT `/lifecycle_manager` (underscores)
- Response shape is `{message, data, metadata}` — same as projects, NOT `{status, result}` like inventory manager
- Pagination metadata uses `{skip, limit, total, currentPageSize, nextPageSkip, previousPageSkip}`
- Sort requires BOTH `sort` and `order` parameters: `?sort=startTime&order=-1`. The `-` prefix syntax (`sort=-startTime`) does NOT work — returns error.
- `PUT /resources/{modelId}/instances/{instanceId}` only updates `name` and `description` — NOT `instanceData`. You must run an action to modify instance data.
- Create actions: `instance` parameter is forbidden, use `instanceName` instead
- Update/delete actions: `instance` (ID or object) is required
- Action `_id` is a 4-char hex string (same as workflow task IDs)
- Instance states: `"0001"` = Ready, `"0000"` = Error, `"0002"` = Deleted
- `DELETE /resources/{id}` does NOT delete instances by default — pass `?delete-associated-instances=true` to cascade
- Bulk actions and instance groups require `LCM_GROUPS_ENABLED=true` environment variable
- **Action workflows MUST output a job variable named `instance`** containing the instance data. Without it, the action fails validation with "workflow does not output a value for 'instance'". Use a `merge` task to build the instance object and wire outgoing to `$var.job.instance`.
- **Create action — instance merge must cover every `schema.required` field.** If the merge task's `data_to_merge` omits even one field listed in the model's `schema.required` array, the platform writes all provisioned cloud/network resources first and THEN fails the instance write — leaving those resources orphaned from LCM with no tracked state. Before building the merge task, read the model's required fields: `jq '.schema.required' helpers/assets/lcm/<model>.json`. Every required field must have a corresponding key in `data_to_merge`.
- Action job type is `'resource:action'`, not `'automation'`
- Transformations are Jinja2 templates referenced by template ID (`preWorkflowJst` / `postWorkflowJst`)

## API Reference

**Base Path:** `/lifecycle-manager`

### Resource Models

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/lifecycle-manager/resources` | Create a new resource model |
| GET | `/lifecycle-manager/resources` | List resource models (searchable) |
| GET | `/lifecycle-manager/resources/{id}` | Get a single resource model |
| PUT | `/lifecycle-manager/resources/{id}` | Update a resource model |
| DELETE | `/lifecycle-manager/resources/{id}` | Delete a resource model |
| POST | `/lifecycle-manager/resources/import` | Import a resource model |
| GET | `/lifecycle-manager/resources/{modelId}/export` | Export a resource model |
| POST | `/lifecycle-manager/resources/{modelId}/edit` | Auto-generate action workflows and transformations |
| POST | `/lifecycle-manager/resources/{modelId}/actions/validate` | Validate action definitions |

**Create a resource model:**
```
POST /lifecycle-manager/resources
```
```json
{
  "name": "Network Service",
  "description": "Manages network service lifecycle",
  "schema": {
    "$id": "network-service",
    "type": "object",
    "required": ["service_name", "vlan_id"],
    "properties": {
      "service_name": {"type": "string"},
      "vlan_id": {"type": "integer"},
      "status": {"type": "string", "enum": ["provisioned", "active", "decommissioned"]}
    }
  },
  "actions": [
    {
      "_id": "a1b2",
      "name": "Provision",
      "type": "create",
      "workflow": null,
      "preWorkflowJst": null,
      "postWorkflowJst": null
    },
    {
      "_id": "c3d4",
      "name": "Update Config",
      "type": "update",
      "workflow": null,
      "preWorkflowJst": null,
      "postWorkflowJst": null
    },
    {
      "_id": "e5f6",
      "name": "Decommission",
      "type": "delete",
      "workflow": null,
      "preWorkflowJst": null,
      "postWorkflowJst": null
    }
  ]
}
```

- `schema` — JSON Schema (draft-07) defining valid instance data
- `actions[]._id` — 4-char hex ID (same convention as workflow task IDs)
- `actions[].type` — `"create"`, `"update"`, `"delete"`, or `"import"`
- `actions[].workflow` — workflow ID to execute (set after creating the workflow, or use the edit endpoint to auto-generate)
- `actions[].preWorkflowJst` / `postWorkflowJst` — template IDs for Jinja2 transformations before/after the workflow

**Response:**
```json
{
  "message": "Successfully created resource model",
  "data": {
    "_id": "687fe493ef863896dcba8d78",
    "name": "Network Service",
    "schema": {...},
    "actions": [...],
    "created": "2026-03-04T...",
    "createdBy": "user@example.com"
  },
  "metadata": {}
}
```

**Auto-generate action workflows:**
```
POST /lifecycle-manager/resources/{modelId}/edit
```
```json
{
  "editType": "generate-action-workflow",
  "actionId": "a1b2"
}
```
Edit types: `generate-action-workflow`, `generate-action-pre-transformation`, `generate-action-post-transformation`

**Delete with cascade:**
```
DELETE /lifecycle-manager/resources/{id}?delete-associated-instances=true
```

### Resource Instances

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/lifecycle-manager/resources/{modelId}/instances` | List instances (searchable) |
| GET | `/lifecycle-manager/resources/{modelId}/instances/{instanceId}` | Get a single instance |
| PUT | `/lifecycle-manager/resources/{modelId}/instances/{instanceId}` | Update instance name/description only |
| POST | `/lifecycle-manager/resources/{modelId}/instances/import` | Import an instance |
| GET | `/lifecycle-manager/resources/{modelId}/instances/{instanceId}/export` | Export an instance |

**Instance structure:**
```json
{
  "_id": "687fea14ef863896dcba8d79",
  "name": "customer-portal",
  "description": "Customer portal service",
  "modelId": "687fe493ef863896dcba8d78",
  "instanceData": {
    "service_name": "customer-portal",
    "vlan_id": 100,
    "status": "active"
  },
  "stateId": "0001",
  "lastAction": {
    "_id": "a1b2",
    "executionId": "67d07212df84d4150b6498f7",
    "name": "Provision",
    "type": "create",
    "status": "complete"
  },
  "created": "2026-03-04T...",
  "lastUpdated": "2026-03-04T..."
}
```

**Note:** `instanceData` can only be modified by running an action — NOT by PUT. The PUT endpoint only updates `name` and `description`.

### Running Actions

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/lifecycle-manager/resources/{modelId}/run-action` | Run an action on a single instance |
| POST | `/lifecycle-manager/resources/{modelId}/run-bulk-action` | Run an action on multiple instances |

**Run a create action (new instance):**
```
POST /lifecycle-manager/resources/{modelId}/run-action
```
```json
{
  "actionId": "a1b2",
  "instanceName": "customer-portal",
  "instanceDescription": "Customer portal service",
  "inputs": {
    "service_name": "customer-portal",
    "vlan_id": 100
  }
}
```

**Run an update/delete action (existing instance):**
```json
{
  "actionId": "c3d4",
  "instance": "687fea14ef863896dcba8d79",
  "inputs": {
    "new_vlan_id": 200
  }
}
```
- `instance` — instance ID or full instance object (required for update/delete, forbidden for create)
- `inputs` — workflow input variables (optional, passed to the action workflow)

**Response:**
```json
{
  "success": true,
  "data": {
    "executionId": "67d07212df84d4150b6498f7"
  }
}
```

**Run bulk action (requires LCM_GROUPS_ENABLED):**
```json
{
  "actionId": "c3d4",
  "instances": ["id1", "id2", "id3"],
  "inputs": {"base_config": "standard"},
  "inputOverrides": [
    {"instanceId": "id1", "inputs": {"vlan_id": 100}},
    {"instanceId": "id2", "inputs": {"vlan_id": 200}}
  ]
}
```

### Action Execution History

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/lifecycle-manager/action-executions` | List all action executions (searchable) |
| GET | `/lifecycle-manager/action-executions/{id}` | Get a single execution record |
| POST | `/lifecycle-manager/action-executions/{executionId}/cancel` | Cancel a running execution |

**Execution record:**
```json
{
  "_id": "67d07212df84d4150b6498f7",
  "modelId": "687fe493ef863896dcba8d78",
  "modelName": "Network Service",
  "instanceId": "687fea14ef863896dcba8d79",
  "instanceName": "customer-portal",
  "actionId": "a1b2",
  "actionName": "Provision",
  "actionType": "create",
  "status": "complete",
  "startTime": "2026-03-04T12:00:00Z",
  "endTime": "2026-03-04T12:00:05Z",
  "jobId": "24-char-workflow-engine-job-id",
  "progress": [
    {"_id": "preTransformation", "status": "complete"},
    {"_id": "workflow", "status": "complete"},
    {"_id": "postTransformation", "status": "complete"}
  ],
  "errors": []
}
```

Execution statuses: `running`, `complete`, `error`, `canceled`, `paused`

**Query parameters for filtering:**
- `equals[status]=complete` — exact match
- `contains[modelName]=Network` — substring match
- `in[status]=running,complete` — match any in list
- `gt[startTime]=2026-03-01` — greater than
- `sort=startTime&order=-1` — sort descending (requires BOTH `sort` and `order`)
- `skip=0&limit=25` — pagination

### Instance Groups (conditional)

Requires `LCM_GROUPS_ENABLED=true` environment variable.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/lifecycle-manager/resources/{modelId}/groups` | Create a group |
| GET | `/lifecycle-manager/resources/{modelId}/groups` | List groups |
| GET | `/lifecycle-manager/resources/{modelId}/groups/{groupId}` | Get a group |
| PATCH | `/lifecycle-manager/resources/{modelId}/groups/{groupId}` | Update a group |
| DELETE | `/lifecycle-manager/resources/{modelId}/groups/{groupId}` | Delete a group |

**Group types:**
- `manual` — explicit list of instance IDs: `{"type": "manual", "instances": ["id1", "id2"]}`
- `dynamic` — filter-based: `{"type": "dynamic", "filter": {"status": "active"}}`

## Action Execution Flow

When an action runs, it goes through 3 phases:

```
1. Pre-Transformation (optional)
   └── Jinja2 template transforms inputs before workflow

2. Workflow Execution
   └── Runs the action's linked workflow with (transformed) inputs

3. Post-Transformation (optional)
   └── Jinja2 template transforms workflow outputs
   └── Can produce/update instance data
```

Errors at any phase stop execution. Each phase has its own status tracked in the `progress` array.

## Helper Templates

**Read a real LCM action workflow before building.** The VXLAN Fabric Services project contains production LCM action workflows — they show exactly how to declare and output the required `instance` variable:

```bash
# List available LCM action workflows
jq '[.data.project.components[] | select(.type=="workflow")] | .[].document.name' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/lcm/lcm-vxlan-fabric-services-project.json

# Read a specific action workflow (e.g., Create)
jq '[.data.project.components[] | select(.type=="workflow") | select(.document.name | test("Create"; "i"))] | first | .document | {name:.name, tasks:.tasks, transitions:.transitions}' \
  ${CLAUDE_PLUGIN_ROOT}/helpers/assets/lcm/lcm-vxlan-fabric-services-project.json
```

The resource model exports (in `${CLAUDE_PLUGIN_ROOT}/helpers/assets/lcm/`) show how actions are wired to workflows — import via `POST /lifecycle-manager/resources/import`:

| File | Actions |
|------|---------|
| `lcm-vxlan-fabric-management.json` | Create Network, Re-Provision, Delete, Decommission (4/5 wired) |
| `lcm-fan-device-lifecycle-management.json` | Device Onboarding, SW Compliance, Upgrade, Decommission, and more (9/10 wired) |
| `lcm-ip-blocking-service.json` | Create, Update, Delete, Retry (fully wired) |
| `lcm-interface-service-provisioning.json` | Create, Modify, Delete (fully wired) |
| `lcm-port-turn-up.json` | Create, Delete, Service Verification, Update Service Policy (4/6 wired) |

## Developer Scenarios

### 1. Create a resource model with actions
```
1. POST /lifecycle-manager/resources                    → create model with schema + actions
2. Read model's schema.required BEFORE building Create workflow
   jq '.schema.required' helpers/assets/lcm/<model>.json  -- every field here must be in the instance merge task
3. Create workflows for each action in /itential-studio
   Create action: instance-write merge task must cover ALL schema.required fields (missing one = orphaned resources)
4. PUT /lifecycle-manager/resources/{id}                → update actions with workflow IDs
5. POST /lifecycle-manager/resources/{id}/actions/validate → verify actions are valid
```

### 2. Run the full lifecycle
```
1. POST /lifecycle-manager/resources/{id}/run-action    → create action (new instance)
2. GET  /lifecycle-manager/action-executions/{execId}   → check execution status
3. GET  /lifecycle-manager/resources/{id}/instances      → see created instance
4. POST /lifecycle-manager/resources/{id}/run-action    → update action (modify instance)
5. POST /lifecycle-manager/resources/{id}/run-action    → delete action (decommission)
```

### 3. Track and debug execution history
```
1. GET /lifecycle-manager/action-executions?equals[status]=error → find failed executions
2. GET /lifecycle-manager/action-executions/{id}        → check progress phases + errors
3. Check errors[].origin to identify which phase failed
4. Fix the workflow/transformation and re-run the action
```

````

============================================================
FILE: .claude/skills/itential-mop/SKILL.md
DIRECTORY: .claude/skills/itential-mop/
FILENAME: SKILL.md
============================================================
SHA256: 0292bba2393cc71373eecf28294dee07297b5503fb46bbbb27fe00add59d5b10

````markdown
---
name: itential-mop
description: Build command templates with validation rules, run CLI checks against devices, and use analytic templates for pre/post comparison. Use when building pre-checks, post-checks, or compliance validations that run show commands and evaluate output.
argument-hint: "[action or template-name]"
---

# MOP (Method of Procedure) - Developer Skills Guide

MOP manages command templates and analytic templates for running CLI commands against network devices with validation rules. Command templates execute show commands and evaluate the output against rules. Analytic templates compare command output before and after a change.

**MOP is for read-only validation only -- never use it to push configuration to devices.** Use Jinja2 templates and workflow tasks for config changes.

## Concepts

- **Command template** = a set of CLI commands + validation rules, run against one or more devices
- **Analytic template** = pre/post comparison of command output to detect drift
- **Variable syntax** = `<!variable_name!>` in both commands and rules (NOT `{{ var }}` or `$var`)
- **Pass/fail logic** = hierarchical: template-level -> command-level -> rule-level, each with AND/OR control

## API Reference

All `/mop/*` endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/mop/createTemplate` | Create a command template |
| GET | `/mop/listTemplates` | List all command templates |
| GET | `/mop/listATemplate/{name}` | Get a command template by name |
| POST | `/mop/updateTemplate/{mopID}` | Update a command template (full replacement) |
| POST | `/mop/deleteTemplate/{id}` | Delete a command template |
| POST | `/mop/exportTemplate` | Export template (body: `{"_id": "..."}` or `{"name": "..."}`) |
| POST | `/mop/importTemplate` | Import a template |
| POST | `/mop/RunCommandTemplate` | Run a command template against devices |
| POST | `/mop/RunCommand` | Run a single ad-hoc command on one device (workflow task) |
| POST | `/mop/RunCommandDevices` | Run a single ad-hoc command on multiple devices |
| POST | `/mop/RunCommandTemplateSingleCommand` | Run one command from a template by index |
| POST | `/mop/GetBootFlash` | Get boot flash image name from a device |
| POST | `/mop/reattempt` | Retry/delay mechanism for workflows |
| POST | `/mop/createAnalyticTemplate` | Create an analytic template |
| GET | `/mop/listAnalyticTemplates` | List all analytic templates |
| GET | `/mop/listAnAnalyticTemplate/{name}` | Get an analytic template by name (path param) |
| POST | `/mop/updateAnalyticTemplate/{id}` | Update an analytic template |
| POST | `/mop/deleteAnalyticTemplate/{id}` | Delete an analytic template |
| POST | `/mop/runAnalyticsTemplate` | Run an analytic template (workflow task) |

## Template Structure

Create with `POST /mop/createTemplate`. The body uses a `{"mop": {...}}` wrapper.

```json
{
  "mop": {
    "name": "Port_Turn_Up_Pre_Check",
    "description": "Validates interface and VLAN before port turn-up",
    "os": "",
    "passRule": true,
    "ignoreWarnings": false,
    "commands": [
      {
        "command": "show interface <!interface!>",
        "passRule": true,
        "rules": [
          {
            "rule": "line protocol is",
            "eval": "contains",
            "severity": "error"
          }
        ]
      },
      {
        "command": "show vlan brief",
        "passRule": true,
        "rules": [
          {
            "rule": "<!vlan_id!>",
            "eval": "contains",
            "severity": "error",
          }
        ]
      }
    ]
  }
}
```

**Field reference:**
- **`name`** -- template name (required, must be unique)
- **`description`** -- human-readable description
- **`os`** -- target OS filter (empty string = any OS)
- **`passRule`** (template-level) -- `true` = ALL commands must pass (AND), `false` = ONE command must pass (OR)
- **`ignoreWarnings`** -- see ignoreWarnings section below
- **`commands[]`** -- array of commands to execute
  - **`command`** -- the CLI command string. Variables use `<!variable_name!>` syntax
  - **`passRule`** (command-level) -- `true` = ALL rules must pass (AND), `false` = ONE rule must pass (OR)
  - **`rules[]`** -- validation rules applied to the command output
    - **`rule`** -- the string or pattern to match against. Can contain `<!variables!>`
    - **`eval`** -- evaluation operator (case-sensitive, see Rule Evaluation below)
    - **`severity`** -- `"error"`, `"warning"`, or `"info"`
    - **`flags`** -- optional evaluation flags (see Flags below)

**Only "name" is required** -- template validation uses AJV with strict=false, so minimal templates are accepted.

### passRule Logic

- **Template-level `passRule: true`** = ALL commands must pass (AND logic)
- **Template-level `passRule: false`** = at least ONE command must pass (OR logic)
- **Command-level `passRule: true`** = ALL rules in this command must pass (AND logic)
- **Command-level `passRule: false`** = at least ONE rule must pass (OR logic)

### ignoreWarnings

Template-level field, default `false`. When `true`: only rules with `severity: "error"` count as real failures. Rules with `severity: "warning"` or `"info"` that fail are treated as passing. When `false` (default): all severity levels count.

```json
{
  "mop": {
    "name": "...",
    "passRule": true,
    "ignoreWarnings": true,
    "commands": [...]
  }
}
```

## Rule Evaluation

The `eval` field determines how rule matching works. **Eval types are case-sensitive.**

| Eval | Purpose | Example Rule |
|------|---------|-------------|
| `contains` | String exists in output | `"line protocol is"` |
| `!contains` | String does NOT exist in output | `"ERROR"` |
| `contains1` | String exists exactly once | `"Active"` |
| `RegEx` | Regex matches output (capital R and E!) | `"/\\d+\\.\\d+/"` |
| `!RegEx` | Regex does NOT match | `"/ERROR/"` |
| `#comparison` | Extract + compare two values | See details below |

### Flags

Optional `flags` object on each rule:
- **`case: true`** = case-INSENSITIVE matching (confusing name -- `case: true` does NOT mean case-sensitive)
- **`global: true`** = global search (RegEx only)
- **`multiline: true`** = `^`/`$` match start/end of lines, not just start/end of string (RegEx only)

`case` is available for all eval types. `global` and `multiline` are only meaningful for `RegEx` and `!RegEx`.

### #comparison Details

Extract two values from command output using regex, then compare numerically.

```json
{
  "rule": "/Available: (\\d+)/",
  "ruleB": "/Total: (\\d+)/",
  "eval": "#comparison",
  "evaluator": ">=",
  "severity": "error"
}
```

- **`rule`** / **`ruleB`** -- regex patterns (in `/pattern/` format) to extract values from the command output
- **`evaluator`** -- comparison operator: `=`, `!=`, `<`, `>`, `<=`, `>=`, `%`
- **`%` operator** -- passes if `ruleB/rule * 100 <= percentage`. Set `"percentage": 80` to pass if ruleB is at most 80% of rule.

Example with percentage:
```json
{
  "rule": "/Total: (\\d+)/",
  "ruleB": "/Used: (\\d+)/",
  "eval": "#comparison",
  "evaluator": "%",
  "percentage": 80,
  "severity": "error"
}
```

## Variable Substitution

- **Syntax:** `<!variable_name!>` in both commands and rules
- Variables are substituted BEFORE execution
- If a variable is missing, the command is **SKIPPED** (not failed!) and counts as **PASSED**
- This syntax is different from Jinja2 templates (`{{ var }}`) and workflow variable references (`$var.job.x`)

Example command with variables:
```json
{
  "command": "show running-config interface <!interface!>",
  "passRule": true,
  "rules": [
    {
      "rule": "switchport access vlan <!vlan_id!>",
      "eval": "contains",
      "severity": "error",
      "evaluation": "pass"
    }
  ]
}
```

## Execution

### Standalone (without a workflow)

```
POST /mop/RunCommandTemplate
```
```json
{
  "template": "Port_Turn_Up_Pre_Check",
  "variables": {
    "interface": "GigabitEthernet0/1",
    "vlan_id": "100"
  },
  "devices": ["IOS-CAT8KV-1"]
}
```

- **`template`** -- template name (string)
- **`variables`** -- object with values for `<!variable!>` substitutions
- **`devices`** -- array of device names (or single device name string)

### In a Workflow

Use the `MOP.RunCommandTemplate` task. See `/itential-studio` for full workflow task wiring patterns.

```json
{
  "incoming": {
    "template": "$var.job.templateName",
    "variables": "$var.job.templateVariables",
    "devices": "$var.job.devices"
  },
  "outgoing": {
    "mop_template_results": null
  }
}
```

- **`template`** -- name of the command template (string or `$var` reference)
- **`variables`** -- object with values for `<!variable!>` substitutions
- **`devices`** -- array of device names to run against

See `/itential-builder` for running the workflow via `POST /operations-manager/jobs/start`.

### Ad-Hoc Commands (without a template)

Run a single command directly without creating a template first:

```
POST /mop/RunCommand
```
```json
{
  "command": "show version",
  "variables": {},
  "device": "IOS-CAT8KV-1"
}
```
Returns: `{raw, evaluated, device, response, result}` — same shape as one entry in `commands_results`.

For multiple devices: `POST /mop/RunCommandDevices` with `"devices": ["dev1", "dev2"]` (array instead of singular `device`).

To run a single command from an existing template by index: `POST /mop/RunCommandTemplateSingleCommand` with `{"templateId": "name", "commandIndex": 0, "variables": {}, "devices": ["dev1"]}`.

### Response Shape

```json
{
  "all_pass_flag": true,
  "result": true,
  "name": "Port_Turn_Up_Pre_Check",
  "commands_results": [
    {
      "raw": "show interface <!interface!>",
      "evaluated": "show interface GigabitEthernet0/1",
      "all_pass_flag": true,
      "device": "IOS-CAT8KV-1",
      "response": "...command output...",
      "result": true,
      "parameters": {"interface": "GigabitEthernet0/1"},
      "rules": [
        {"rule": "line protocol is", "eval": "contains", "result": true, "severity": "error"}
      ]
    }
  ]
}
```

- **`result`** (top-level) -- overall template pass/fail (boolean)
- **`all_pass_flag`** (top-level) -- the template's passRule setting
- **`commands_results[]`** -- one entry per command per device
  - **`raw`** -- original command string (before variable substitution)
  - **`evaluated`** -- command with variables substituted
  - **`response`** -- raw device output
  - **`result`** -- whether this command passed (boolean)
  - **`all_pass_flag`** -- this command's passRule setting
  - **`device`** -- the device this command ran against
  - **`parameters`** -- the variables that were substituted
  - **`rules[].result`** -- `true`/`false` for each individual rule

### Update

```
POST /mop/updateTemplate/{mopID}
```

The `mopID` is the template name (URL-encoded). Uses the same `{"mop": {...}}` body wrapper as create. The body is a **full replacement** -- include ALL fields, not just changed ones.

Response on success:
```json
{
  "n": 1,
  "ok": 1,
  "nModified": 1
}
```

## Analytic Templates

Analytic templates compare command output before and after a change to detect drift or validate results. Endpoints are listed in the API Reference table above.

### Create an Analytic Template

```
POST /mop/createAnalyticTemplate
```
```json
{
  "name": "Interface_Change_Validation",
  "os": "cisco-ios",
  "passRule": true,
  "prepostCommands": [
    {
      "preRawCommand": "show interface GigabitEthernet0/1",
      "postRawCommand": "show interface GigabitEthernet0/1",
      "passRule": true,
      "rules": [
        {
          "type": "matches",
          "preRegex": "/line protocol is (\\w+)/",
          "postRegex": "/line protocol is (\\w+)/",
          "evaluator": "="
        }
      ]
    }
  ]
}
```

### Structure

- **`name`** -- template name
- **`os`** -- target OS
- **`passRule`** -- `true` = ALL prepostCommands must pass (AND), `false` = ONE must pass (OR)
- **`prepostCommands[]`** -- array of pre/post command pairs
  - **`preRawCommand`** -- CLI command to run before the change
  - **`postRawCommand`** -- CLI command to run after the change
  - **`passRule`** -- `true` = ALL rules must pass, `false` = ONE must pass
  - **`rules[]`** -- comparison rules
    - **`type`** -- `matches`, `!matches`, `regex`, or `table`
    - **`preRegex`** -- regex to extract value from pre-change output
    - **`postRegex`** -- regex to extract value from post-change output
    - **`evaluator`** -- comparison operator: `=`, `!=`, `<`, `>`, `<=`, `>=`, `%`

### Rule Types

| Type | Purpose |
|------|---------|
| `matches` | Pre and post extracted values must match per evaluation operator |
| `!matches` | Pre and post extracted values must NOT match |
| `regex` | Regex-based extraction and comparison |
| `table` | Table-based comparison of structured output |

### Running an Analytic Template

In a workflow, use the `MOP.runAnalyticsTemplate` task:

```json
{
  "incoming": {
    "pre": "$var.preCheckTaskId.mop_template_results",
    "post": "$var.postCheckTaskId.mop_template_results",
    "analytic_template_name": "Interface_Change_Validation",
    "variables": {}
  },
  "outgoing": {
    "analytic_result": null
  }
}
```

**Critical:** The `pre` and `post` inputs must be the full `RunCommandTemplate` output object (which contains a `commands_results` property). Do NOT pass just the `commands_results` array — pass the entire result object.

**Gotcha:** Pre and post commands must have **exactly 1 match each** in the collected results. If 0 or >1 match, it produces an error. The matching compares against both the `raw` and `evaluated` command strings — if variables were used, the `evaluated` string (with variables replaced) is what will match.

## Gotchas

1. **Missing variable = skip = PASS (not fail)** -- if a `<!var!>` token has no value, the command is silently skipped and counts as PASSED. Verify variables are passed correctly.

2. **`case: true` = case-INsensitive** -- confusing naming. `"flags": {"case": true}` enables case-insensitive matching. It does NOT mean case-sensitive.

3. **Empty rules = auto-pass** -- a command with no rules (`"rules": []`) always passes. Add at least one rule if you want validation.

4. **RegEx 5-second timeout** -- complex regex patterns run in a sandboxed VM with a 5-second limit. Patterns prone to catastrophic backtracking will timeout.

5. **`contains` does substring matching** -- `"100"` matches `"1002"`. For exact matching, use `RegEx` with multiline flag:
   ```json
   {"rule": "^<!vlanId!>\\s+", "eval": "RegEx", "severity": "error", "flags": {"multiline": true}}
   ```

6. **Eval types are case-sensitive** -- `"RegEx"` not `"regex"` or `"REGEX"`. `"#comparison"` not `"Comparison"`.

7. **Only "name" is required** -- template validation uses AJV with strict=false. Minimal templates are accepted.

8. **Update is full replacement** -- `POST /mop/updateTemplate/{mopID}` replaces the entire template. Include ALL fields when updating, not just changed ones.

9. **MOP is read-only** -- command templates run show commands and evaluate output. Never use MOP to push configuration changes. Use Jinja2 templates and workflow adapter tasks for config changes.

10. **`_id` equals `name`** -- the engine sets `_id = name` on create. They are always identical. Use either for lookups.

11. **Rule-level missing variable ≠ command-level skip** -- if a *command* has `<!var!>` missing, the whole command is skipped (passes). But if a *rule* has `<!var!>` missing, it gets `eval: "missing_parameters"` and returns `"Invalid Rule: Missing Parameters"` with `result: false`. The rule fails, not skips.

12. **Template name change on update = delete + create** -- if you update with a different name, the engine deletes the old template and creates a new one. This is destructive — the old `_id` is gone.

13. **Import renames on collision** -- `importTemplate` does not fail on duplicate names. It appends ` (N)` to the name (e.g., `My_Template` becomes `My_Template (1)`).

14. **Cannot set `namespace` directly** -- providing `namespace` in the create body throws an error. Namespaces are managed through project membership.


## Helper Templates

Always start from a helper template when creating assets. Read the helper file first, then modify it.

| File | API Call | Purpose |
|------|----------|---------|
| `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-command-template.json` | `POST /mop/createTemplate` | Command template with rules |
| `${CLAUDE_PLUGIN_ROOT}/helpers/update/update-command-template.json` | `POST /mop/updateTemplate/{mopID}` | Update template (full replacement) |

## Developer Scenarios

### 1. Build a pre-check command template

1. Identify the show commands needed (e.g., `show interface`, `show vlan brief`)
2. Read `${CLAUDE_PLUGIN_ROOT}/helpers/create/create-command-template.json` as a starting template
3. Fill in `name`, `description`, add commands with `<!variable!>` placeholders
4. Add rules for each command -- use `contains` for simple checks, `RegEx` for pattern matching
5. Set `passRule` at template and command level (AND vs OR logic)
6. Create with `POST /mop/createTemplate`
7. Test standalone with `POST /mop/RunCommandTemplate` providing variables and devices
8. Check `result` (top-level) and `commands_results[].rules[].result` for pass/fail details

### 2. Wire RunCommandTemplate into a workflow

After standalone testing passes:

1. Use `/itential-studio` to build a workflow
2. Add a `MOP.RunCommandTemplate` task to the workflow
3. Wire incoming variables: `template`, `variables`, `devices` using `$var.job.*` references
4. Wire outgoing: capture results in a variable like `mop_template_results`
5. Add downstream logic to branch on `$var.taskName.result` (true/false)
6. Use `/itential-builder` to run via `POST /operations-manager/jobs/start`

### 3. Build an analytic template for pre/post comparison

1. Identify the commands to run before and after the change
2. Create an analytic template with `POST /mop/createAnalyticTemplate`
3. Define `prepostCommands` with pre/post command pairs
4. Add rules with `preRegex`/`postRegex` to extract values for comparison
5. Set `evaluation` operator (`=` to verify values match, `!=` to verify they changed)
6. In a workflow: run pre-change commands, execute the change, run post-change commands, compare
7. Remember: pre and post commands must have exactly 1 match each in results

````

============================================================
FILE: .claude/skills/project-to-spec/SKILL.md
DIRECTORY: .claude/skills/project-to-spec/
FILENAME: SKILL.md
============================================================
SHA256: e8a03d66c232a5ef53cc4fbf36f1ae368ea752f8e37a46b6b5f62d4a8843fd36

````markdown
---
name: project-to-spec
description: Use this skill when a user names a specific existing Itential project and wants it documented — reverse-engineered into a requirements spec and solution design. Trigger it for phrases like "document the DNS_Management project", "create a spec from the Firewall_Rule_Lifecycle project", "reverse-engineer project X into a spec", "I have a project with no docs — produce a customer-spec and solution design for it", or "use this project as a baseline for a rebuild". Reads the project's workflows, templates, and MOP components, infers business purpose and design decisions, and produces customer-spec.md + solution-design.md. For documenting global/unprojectized assets across the whole platform, use /documentation instead.
argument-hint: "[project-name or project-id]"
---

# Project to Spec

**Purpose:** Read an existing project → produce documentation
**Output:** `customer-spec.md` (inferred HLD) + `solution-design.md` (as-built LLD)
**Feeds into:** Can be handed directly to `/solution-arch-agent` (design-only mode) or `/spec-agent` for refinement

---

## What This Does

Takes an undocumented or partially-documented project and produces the spec and design documents that *should* have existed before it was built. The engineer reviews and corrects the inferred documents — then they can feed into the standard delivery lifecycle for updates, rebuilds, or knowledge transfer.

```
Existing Project
      │
      ├── Pull all components (workflows, templates, MOP)
      ├── Read each workflow: tasks, adapters, transitions, data flows
      ├── Infer: business purpose, phases, inputs, outputs, integrations
      │
      ├── customer-spec.md   ← inferred HLD (engineer reviews + corrects)
      └── solution-design.md ← as-built LLD (actual component inventory)
```

---

## Step 1: Identify the Project

Ask the engineer for a project name or ID. Then pull the project:

```
GET /automation-studio/projects/{projectId}
```

Or search by name:
```
GET /automation-studio/projects?contains=name:{projectName}
```

Response: `{message, data: {_id, name, components: [...], members: [...]}}`

Save the project ID and component list.

### If the project is not returned

Project list/get responses are RBAC-filtered. A 404 or empty `data` array does NOT prove the project doesn't exist — it may be invisible to the calling client.

**Important:** Itential projects use per-project ACLs only. There is **no platform-wide admin or "all-projects" role** — every project explicitly grants access to specific users or groups via its own ACL. The calling client sees a project iff that project's ACL includes the client or one of its groups. (This applies to **projects** specifically; global Automation Studio assets that live outside any project are not access-restricted the same way.)

Before declaring the project missing, do all of:

1. **Identify the calling client** — `GET /iam/clients/{client_id}` (the `client_id` from `.auth.json` or the env file). Note its group memberships — these (together with the client itself) determine which project ACLs it might be on.
2. **Try a broader query** — `GET /automation-studio/projects?limit=500` and inspect the result for partial-name matches; the `contains` filter is case-sensitive in some Platform versions.
3. **Surface visibility, not absence** — report: *"No project named `{name}` is visible to this client (`{client_id}`). It may not exist, or it may be access-restricted. To confirm, ask the project's owner (or someone with manage rights on that project) to add `{client_id}` to its ACL via the Automation Studio UI."*
4. **Do not auto-grant access.** Adding the calling client to a project ACL is a privileged write to a shared resource — always ask the engineer to handle it via the UI, or via a different client that is already on that project's ACL with manage rights. If the engineer authorizes a DB-level read-only confirmation (e.g. local dev Mongo), that is acceptable, but the granting itself stays a human action.

Stop and wait for engineer direction before proceeding to Step 2.

---

## Step 2: Pull All Components

For each component in the project, fetch the full document.

**Workflows:**
```
GET /automation-studio/workflows/detailed/{urlEncodedName}
```

**Templates:**
```
GET /automation-studio/templates/{id}
```

**MOP Command Templates:**
```
GET /mop/listATemplate/{name}
```

For each workflow, extract and save locally:
- `tasks` — every task with name, app, adapter, incoming/outgoing variables
- `transitions` — the flow between tasks
- `inputSchema` / `outputSchema` — what the workflow accepts and returns
- Task summaries and descriptions (these often contain intent)

Save to `{use-case}/project-components.json`.

---

## Step 3: Analyze the Components

Work through the components to reconstruct intent and structure.

### Identify the orchestrator

Find the parent workflow — usually the one that:
- Has no `childJob` references pointing to it from other workflows
- References other workflows via `childJob` tasks
- Has the most complex transition graph

### Map the data flow

For the orchestrator and each child:
1. What are the **inputs**? (inputSchema properties)
2. What adapters are called? (location: "Adapter" tasks)
3. What utility tasks are used? (merge, query, evaluation, childJob, makeData)
4. What are the **outputs**? (outputSchema properties, $var.job.x assignments)
5. What external systems are touched? (adapter names → infer ServiceNow, Route53, etc.)

### Infer the phases

Each major section of the orchestrator maps to a phase:
- A `childJob` to a child workflow = one phase
- An `evaluation` branch = a decision point
- An adapter call cluster = an integration phase
- A `ViewData` = an approval gate
- Error handling branches = rollback/recovery phases

### Reconstruct acceptance criteria

From the workflow structure, infer what "done" looks like:
- What does the final outgoing variable represent?
- What adapters were called? → "ServiceNow ticket created and updated"
- What verifications exist? → `evaluation` tasks checking status
- What is the `outputSchema`? → these are the observable outcomes

---

## Step 4: Produce `customer-spec.md`

Write the inferred HLD. Use the standard spec structure but mark inferred sections clearly.

```markdown
# Use Case: {Inferred Name}

> **Note:** This spec was produced by reading project `{projectName}` ({projectId}).
> Review and correct any inferences before using as a delivery baseline.

## 1. Problem Statement
{Inferred from workflow descriptions, adapter usage, and task summaries}

## 2. High-Level Flow
{Inferred from orchestrator transition graph}

## 3. Phases
{One section per major workflow / childJob cluster}

## 4. Key Design Decisions
{Inferred from adapter choices, error handling patterns, approval gates}

## 5. Scope
**In scope (as built):** {list components that exist}
**Not observed:** {common patterns not present — rollback, notifications, etc.}

## 6. Risks & Mitigations
{Inferred from error transitions, evaluation branches}

## 7. Requirements

### Capabilities
{Derived from apps and tasks used}

### Integrations
{Derived from adapter names and instance IDs}

## 8. Batch Strategy
{Inferred from childJob loopType usage}

## 9. Acceptance Criteria
{Inferred from outputSchema and evaluation checks}
```

---

## Step 5: Produce `solution-design.md`

Write the as-built LLD — this is factual, not inferred.

```markdown
# Solution Design: {Project Name}

> **As-Built** — produced by reading project `{projectId}`.

## A. Environment Summary
{Platform, adapters found, apps used}

## B. Component Inventory
| # | Component | Type | Workflow/Template Name | ID |
|---|-----------|------|----------------------|-----|
| 1 | {name} | {workflow/template/mop} | {actual name} | {id} |
...

## C. Adapter Mappings
| Adapter | app name | adapter_id | Tasks Used |
|---------|----------|-----------|------------|
| ServiceNow | Servicenow | ServiceNow | createChangeRequest, updateChangeRequest |
...

## D. Workflow Structure
For each workflow: inputs, task sequence, outputs, error handling pattern.

## E. Data Flow
Key variables and how they move between tasks and workflows.

## F. Known Gaps
Patterns not present that are typically expected:
- No rollback logic observed
- No notifications (email/Teams)
- No audit trail
etc.
```

---

## Step 6: Write Memory File

Before presenting to the engineer, create `{use-case}/use-case-memory.md` from `${CLAUDE_PLUGIN_ROOT}/helpers/use-case-memory.md` and populate it with what you just read — don't leave this for later:

- **Platform References** — platform URL, project name, project `_id`, adapter instance names and type names, group memberships observed
- **What Was Built** — every component from the inventory table: name, type, ID, status=`existing`
- **Architecture Decisions** — any patterns you inferred (why childJob loop, why this adapter, why approval gate)
- **Stage / Status** — `Stage: delivered`, `Status: active` if the project is fully in production and this is pure documentation; `Stage: requirements` (or wherever the engineer decides to re-enter) if this is a baseline for a rebuild or refinement

This means any skill that picks up from here (spec-agent, solution-arch-agent, builder-agent, qa-agent) starts with the real IDs already recorded — no re-discovery.

---

## Step 7: Present to Engineer

Show both documents and walk through:

1. **Inferences to verify** — "I inferred the purpose is X based on the adapter usage and task names. Is that correct?"
2. **Gaps** — "I don't see rollback logic or notifications. Were these intentional omissions or should they be added?"
3. **Next steps** — offer three options:
   - **Use as-is** — accept the documents as the baseline for this project
   - **Refine the spec** — hand to `/spec-agent` to refine the requirements with the engineer
   - **Redesign** — hand to `/solution-arch-agent` in design-only mode to produce an updated implementation plan

---

## What to Watch For

**Orphaned tasks:** Tasks with no useful summary — check their adapter/app and incoming variables to infer purpose.

**Non-hex task IDs:** If you encounter task IDs like `apush` or `myTask`, note them — these are a known bug pattern ($var references silently fail on these).

**Deep nesting:** childJob → childJob → childJob patterns indicate a modular design — document each layer separately.

**Static values as indicators:** Hard-coded strings in merge tasks or newVariable tasks often reveal business rules (e.g., `"value": "production"` → production-only path).

**Missing error transitions:** Note any adapter tasks without error transitions — this is a quality gap in the existing implementation.

---

## Gotchas

- Workflow names include `@projectId:` prefix — strip it when displaying to the engineer
- `GET /automation-studio/workflows?exclude-project-members=false` is needed to list project-owned workflows
- Template `data` field is a JSON string, not an object — parse it before analyzing
- childJob `workflow` field shows the child workflow name (with prefix) — this is the dependency graph
- Task descriptions and summaries are the best source of intent — use them heavily
- **Project not returned ≠ project doesn't exist.** Itential projects use per-project ACLs only — there is no platform-wide admin role that sees every project. List/get responses are filtered by the calling client's ACL membership per project. A named project the engineer expects but the API doesn't return is more likely access-restricted than missing. Follow the "If the project is not returned" path in Step 1 — never silently switch to a different project, never declare absence without surfacing the visibility caveat, and never grant the calling client access on its own initiative.

````

============================================================
FILE: .claude/skills/qa-agent/SKILL.md
DIRECTORY: .claude/skills/qa-agent/
FILENAME: SKILL.md
============================================================
SHA256: 091ab13ccf6f45c7fc2ed5280f37e3bfe79dac025f577406227c8b9e0cf13553

````markdown
---
name: qa-agent
description: Use this skill when a build is complete and needs to be verified before customer sign-off. Trigger it for phrases like "the build is done, let's test it", "run acceptance tests", "verify this against the acceptance criteria", "test the delivery", "is this ready to ship", "produce the as-built record", "write the as-built documentation", "sign off on this delivery", or "certify this is working". This skill drafts a test plan from the approved acceptance criteria, gets engineer approval, generates and runs both static (structural) and acceptance (live job) test cases, produces test-report.md, and — once tests pass — writes as-built.md. On any test failure, it reports the failure with evidence and hands back to /builder-agent for a fix; it never edits workflows itself. Invoke after /builder-agent completes a build. This is the last technical stage before customer delivery.
---

# QA Agent

**Stages:** Test → As-Built
**Owns:** Verifying the delivered build against acceptance criteria and structural correctness; recording delivered state at closeout.
**Receives from:** `/builder-agent` (deployed assets + complete workspace)
**Produces:** `test-plan.md` (approved) → `test-cases.json` → `test-report.md` → `as-built.md`

---

## Stage Expectations

### Test

| | |
|--|--|
| **Engineer provides** | Deployed assets from Build, confirmed test data/targets |
| **Agent does** | Drafts a test plan from the approved acceptance criteria, generates static + acceptance test cases, executes them, reports results |
| **Engineer action** | Approves `test-plan.md` before anything runs live; reviews `test-report.md` |
| **Deliverable** | `test-plan.md` (approved) → `test-cases.json` → `test-report.md` |
| **Customer receives** | Proof the delivered solution meets every stated acceptance criterion, with evidence — not just a claim that it works |

### As-Built

| | |
|--|--|
| **Engineer provides** | An approved `test-report.md` (all cases passing, or explicitly accepted residual issues) |
| **Agent does** | Records delivered state, deviations from design, and learnings; updates design and spec where needed |
| **Engineer action** | Signs off on the as-built record |
| **Deliverable** | `as-built.md` + design/spec updates |
| **Customer receives** | As-built record — delivered state, deviations from design with reasons, test evidence, and learnings. The baseline for future work on this use case. |

As-Built is closeout documentation, backed by real test evidence instead of build-time narration. Design deviations update `solution-design.md` as an `## As-Built` section. Scope changes amend `customer-spec.md` with a dated `## Amendments` section.

---

## What This Skill Does NOT Do

- **Does not build or edit workflows, templates, or projects.** That's `/builder-agent`. On any test failure, qa-agent reports it with evidence and hands back to `/builder-agent` for a fix — it never patches an asset itself, even for an obvious one-field fix. Keeping build and test separate means nobody is grading their own homework.
- **Does not re-pull discovery data.** Uses whatever Build left in the workspace — `openapi.json`, `tasks.json`, `apps.json`, `adapters.json` are already there.
- **Does not skip the test-plan approval gate.** Acceptance-level tests have real side effects — they can push config to a device, open a ServiceNow ticket, or allocate an IP. The engineer confirms concrete test data and targets before any live execution, the same way they approve the spec, feasibility, and design before those stages proceed.

---

## Workspace Contract

**Required files (must exist before Test starts):**
```
{use-case}/
  .auth.json              ← auth token
  .env                    ← credentials (for re-auth if token expires)
  use-case-memory.md      ← living context: IDs, decisions, gotchas — READ THIS FIRST
  customer-spec.md        ← approved HLD — Section 9: Acceptance Criteria
  solution-design.md      ← approved LLD — Section D: Component Inventory (real IDs), Section F: Acceptance Criteria → Tests
  openapi.json, tasks.json, apps.json, adapters.json, applications.json
```

**If `solution-design.md` Section D doesn't have real IDs yet** (workflow IDs, project ID — placeholders or missing), Build isn't actually done. Stop and tell the engineer to confirm Build completed before starting Test. `use-case-memory.md`'s `Stage` field should already say `test` at this point (builder-agent sets it at handoff) — if it still says `build`, that's the same signal: verify before proceeding, per AGENTS.md's "Resuming a Use-Case" table.

**The only API calls the QA agent makes are:**
- **Static checks** — `POST /automation-studio/workflows/validate`, `GET` the built workflow/template JSON to run local `jq` checks
- **Acceptance checks** — `POST /operations-manager/jobs/start`, `GET /operations-manager/jobs/{jobId}` for status and output
- **Re-auth** — if the token expires, refresh from `.env` exactly as builder-agent does

---

## Test Lifecycle

```
1. Draft test-plan.md       → from customer-spec.md §9 + solution-design.md §F
2. Confirm test data        → ask the engineer for concrete targets (device, record, sandbox vs prod)
3. Present for approval     → GATE — nothing executes live until approved
4. Generate test-cases.json → static (structural) + acceptance (live job) cases
5. Run static cases first   → cheap, catches structural bugs before spending a live job run
6. Run acceptance cases     → jobs/start against confirmed test data, check real outcomes
7. Write test-report.md     → pass/fail + evidence per case, rollup
8. On failure                → hand back to /builder-agent with the exact failing case + evidence
9. Re-run                   → after builder-agent reports a fix, re-run ONLY the previously-failed cases
10. Write as-built.md        → once every case passes, or the engineer explicitly accepts a residual issue
```

### Step 1: Draft `test-plan.md`

Read `customer-spec.md` Section 9 (Acceptance Criteria) and `solution-design.md` Section F (Acceptance Criteria → Tests — this is already a first-pass mapping from the Solution Architecture Agent; refine it into something concrete now that real IDs exist). Every acceptance criterion gets exactly one test-plan entry:

```markdown
## Test Plan: {Use Case Name}

### AC-1: Port is in the correct VLAN and mode after turn-up
**Type:** acceptance
**Method:** Run the Port Turn Up workflow against a confirmed test port. Post-check reads the interface config and compares VLAN/mode to the requested values.
**Needs from engineer:** a real device + port safe to test against, and the VLAN/mode values to request

### AC-8: ITSM ticket is updated with results (when ITSM is available)
**Type:** acceptance
**Method:** After the workflow completes, GET the ServiceNow change request and confirm its state/notes reflect the run outcome.
**Needs from engineer:** confirmation that the ServiceNow instance is a sandbox, not production

### AC-11: Evidence report documents request, changes, verification, and external system updates
**Type:** artifact-inspection
**Method:** After a run, read the generated evidence report and confirm it contains all four sections. No live job needed beyond the AC-1 run already covers this.
```

**Not every criterion needs a live job.** Some are checked by inspecting an artifact already produced by another test case (`artifact-inspection`), and some genuinely can't be automated (e.g., "port link status is reported — automation can't fix physical layer" is a statement of scope, not a testable claim) — note those as `not-testable` with a one-line reason rather than forcing a fake test around them.

**Static checks are one shared checklist, not itemized per criterion.** They validate structural correctness of what was built, independent of any specific acceptance criterion. Pull the machine-checkable subset of `builder-agent`'s Step 9 pre-submit checklist — skip the visual/canvas-layout items (spacing, crossing lines), since those are aesthetic, not correctness bugs:

```markdown
### Static Checks (run once per built workflow)
- Every task ID is hex-only ([0-9a-f]{1,4})
- Every adapter task has adapter_id in incoming
- Every adapter task has an error transition
- evaluation tasks have both success AND failure transitions
- merge uses "variable", childJob uses "value"
- No {task:"job"} refs in merge/childJob for internally-produced variables
- workflow_end transition is empty {}
- POST /automation-studio/workflows/validate returns empty errors[]
```

### Step 2: Confirm test data

Acceptance-level tests run real jobs with real side effects. Ask directly: *"To test [criterion], I need [a device / a sample record / a target]. What should I use, and is it safe to run against?"* Never invent test data — a device name, a ticket number, an IP block — pulled from imagination instead of the engineer. That's how a test accidentally pushes config to a production device or opens a real ticket nobody asked for.

### Step 3: Present for approval (GATE)

Show the complete `test-plan.md`: every acceptance criterion, its method, and what test data it needs. **Do not generate `test-cases.json` or run anything live until the engineer approves.** This is the same gate discipline as spec/feasibility/design — the difference here is the tests themselves have real-world side effects, which the earlier stages don't.

### Step 4: Generate `test-cases.json`

Once approved, turn each test-plan entry into an executable case. See schema below. Static cases can be generated immediately (they don't need test data). Acceptance cases need the confirmed test data from Step 2 substituted into the actual `jobs/start` payload.

### Step 5: Run static cases first

Cheaper and faster than a live job — catch a broken workflow before spending a live run on it. Run `POST /automation-studio/workflows/validate` on every built workflow, then the `jq`-checkable structural rules directly against the fetched workflow JSON (`GET /automation-studio/workflows/detailed/{name}`). If a static case fails, stop — hand back to `/builder-agent` immediately (Step 8) rather than continuing to acceptance cases against a structurally broken workflow.

### Step 6: Run acceptance cases

For each `acceptance`-type case: `POST /operations-manager/jobs/start` with the confirmed test data, poll `GET /operations-manager/jobs/{jobId}` until `data.status` is `complete` or `error`, then check the case's `verify` condition against `data.variables` / task outputs. For `artifact-inspection` cases, read whatever artifact the prior run produced (evidence report, ticket, etc.) and check it directly — no new job needed.

### Step 7: Write `test-report.md`

One row per case — static and acceptance — with a pass/fail verdict and cited evidence (job ID, exact field values, or the specific static-check output). See format below.

### Step 8: On failure — hand back, don't fix

For every failed case, write a precise failure record: the case ID, what was expected, what actually happened, and the evidence (job ID, task ID, exact values). Hand this to `/builder-agent` — do not attempt to patch the workflow, template, or task yourself, even if the fix looks trivial (e.g., a wrong `adapter_id`). Keeping the boundary firm means the delivered asset and its test evidence never come from the same hand.

### Step 9: Re-run after a fix

When `/builder-agent` reports a fix, re-run **only the cases that previously failed** — not the whole suite — unless the fix plausibly touched something else (e.g., a shared merge task used by multiple workflows). Append the re-run results to `test-report.md` under a `## Re-runs` section; don't overwrite the original run.

### Step 10: Write `as-built.md`

Once every case passes, or the engineer explicitly accepts a residual known issue (documented as such, not silently dropped), update `use-case-memory.md` to `Stage: as-built` and write the as-built record. See format below.

---

## `test-cases.json` Schema

```json
{
  "use_case": "Port Turn Up - Acme Corp",
  "test_plan_approved": "2026-07-02",
  "test_cases": [
    {
      "id": "static-01",
      "type": "static",
      "criterion": null,
      "description": "All task IDs are hex-only",
      "target": "workflow:Port Turn Up",
      "check": "jq '[.tasks | keys[] | select(test(\"^(workflow_start|workflow_end|[0-9a-f]{1,4})$\") | not)] | length'",
      "expected": 0
    },
    {
      "id": "static-02",
      "type": "static",
      "criterion": null,
      "description": "Workflow passes platform validation",
      "target": "workflow:Port Turn Up",
      "check": "POST /automation-studio/workflows/validate",
      "expected": "errors: []"
    },
    {
      "id": "acceptance-01",
      "type": "acceptance",
      "criterion": "AC-1: Port is in the correct VLAN and mode after turn-up",
      "description": "Run Port Turn Up against confirmed test port, verify VLAN/mode",
      "job_start": {
        "workflow": "Port Turn Up",
        "options": {
          "variables": {"deviceName": "IOS-CAT8KV-1", "port": "Gi1/0/24", "vlan": 100, "mode": "access"}
        }
      },
      "verify": "job status == complete AND post-check task output shows vlan==100 AND mode==access"
    },
    {
      "id": "artifact-01",
      "type": "artifact-inspection",
      "criterion": "AC-11: Evidence report documents request, changes, verification, and external system updates",
      "description": "Check the evidence report generated by acceptance-01 contains all four sections",
      "target": "output of acceptance-01",
      "verify": "evidence report contains: request, changes, verification, external_system_updates"
    }
  ]
}
```

**Fields:**
- `type` — `static` (structural, no live call), `acceptance` (live job + outcome check), `artifact-inspection` (checks an artifact from a prior case), or `not-testable` (documented scope limitation, no execution)
- `criterion` — the acceptance-criteria ID this case verifies, or `null` for static checks that apply to the whole build
- `check` / `verify` — human-readable enough that a different engineer could execute it manually if needed; this file is evidence, not just automation input

---

## `test-report.md` Format

```markdown
# Test Report: {Use Case Name}

**Date:** {date}
**Test plan:** test-plan.md (approved {date})
**Result:** {N}/{M} passed

## Static Checks

| Case | Result | Evidence |
|---|---|---|
| static-01 | PASS | 0 non-hex task IDs found across all 3 built workflows |
| static-02 | PASS | POST /workflows/validate returned errors: [] |

## Acceptance Criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| AC-1 | Port is in the correct VLAN and mode after turn-up | PASS | Job `67d0...`, post-check shows vlan=100 mode=access |
| AC-8 | ITSM ticket is updated with results | FAIL | Job `67d1...` completed, but GET on the change request shows state unchanged — handed back to builder-agent 2026-07-02 |

## Re-runs

| Date | Cases re-run | Result | Notes |
|---|---|---|---|
| 2026-07-03 | AC-8 | PASS | builder-agent fixed the update task's changeId wiring; re-ran only AC-8, all other cases unaffected |
```

Every FAIL row states what was handed back and when. Every re-run states what changed and why only those cases were re-run.

---

## `as-built.md` Format

```markdown
# As-Built: {Use Case Name}

**Delivered:** {date}
**Test report:** test-report.md — {N}/{M} passed{, "N known residual issues accepted by engineer" if applicable}

## Delivered Components
{Component inventory from solution-design.md Section D, with final real IDs}

## Deviations from Design
{Anything that changed between the approved solution-design.md and what was actually built/tested — with the reason. If nothing deviated, say so explicitly.}

## Test Evidence Summary
{One line per acceptance criterion: met / met with a documented residual issue, pointing to test-report.md for detail}

## Known Residual Issues
{Anything the engineer explicitly accepted rather than blocking delivery on — with the reason it was accepted and who accepted it}

## Learnings
{Anything worth carrying into the next similar use case — a platform gotcha, a design decision that worked well or didn't}
```

Design deviations get appended to `solution-design.md` as a dated `## As-Built` section — don't rewrite the locked plan. Scope changes get appended to `customer-spec.md` as a dated `## Amendments` section — same principle.

---

## Handoff

### Receiving from Builder

```
{use-case}/
  .auth.json, .env
  use-case-memory.md      ← read first
  customer-spec.md, feasibility.md, solution-design.md   ← approved, with real IDs in solution-design.md §D
  openapi.json, tasks.json, apps.json, adapters.json, applications.json
  task-schemas.json       ← whatever builder-agent accumulated during build
```

Before drafting `test-plan.md`, update `use-case-memory.md` — read it for what was actually built and any gotchas hit during Build; don't re-derive that from scratch.

### Handing back to Builder on failure

Give `/builder-agent` exactly what it needs to fix the issue without re-discovery:
- The failing case ID and its `criterion`/`description`
- Expected vs. actual, verbatim
- The job ID (for acceptance failures) or the static check output (for structural failures)
- Which task/workflow is implicated, if known

### Closeout

Once `as-built.md` is signed off, update `use-case-memory.md` to `Stage: delivered`. The delivery lifecycle for this use case is complete. Future work on this use case (an enhancement, a bug months later) re-enters at whichever stage fits — a small fix might go straight to `/builder-agent`, a new requirement re-enters at `/spec-agent`. Whichever skill picks it back up should set `Stage` forward again from `delivered`, not leave it stale.

---

## Gotchas

- **Acceptance tests are not unit tests.** They exercise the real, delivered workflow through a real job — if the workflow has a bug that component-level testing during Build didn't catch (e.g., a wiring issue that only surfaces with a specific device response shape), that's exactly what this stage exists to find.
- **A test-plan entry with no engineer-supplied test data is not ready to execute.** Don't guess a device name or record ID to keep moving — stop and ask.
- **Static checks catching a failure doesn't mean the whole build is bad** — it usually means one specific rule was missed on one specific task. Report precisely which one; don't send builder-agent back to re-examine the entire workflow.
- **`test-report.md` is written incrementally, not all at once.** Static results land before acceptance results are even generated (Step 5 runs before Step 6). Don't wait until everything is done to start writing it.
- **Residual issues are a documented decision, not a loophole.** If the engineer accepts a known failing case rather than blocking delivery on it, that acceptance — who, why, and what the residual risk is — belongs in both `test-report.md` and `as-built.md`. Silently dropping a FAIL row because "the engineer said it's fine" loses the audit trail.

````

============================================================
FILE: .claude/skills/solution-arch-agent/SKILL.md
DIRECTORY: .claude/skills/solution-arch-agent/
FILENAME: SKILL.md
============================================================
SHA256: ccd5b823ac7f81ff7f0d16d7cf7007ed202b6c50f7e20807ecfd72b6d1b3914c

````markdown
---
name: solution-arch-agent
description: Use this skill when someone has approved requirements (a customer-spec.md) and needs to assess platform feasibility or produce a solution design. Trigger it for phrases like "requirements are approved", "my spec is done", "check if the platform supports this", "run feasibility", "connect to the platform and design the solution", "I have a customer-spec — now what?", or "produce a solution-design.md". This skill connects to the live platform, checks what adapters and capabilities are available, and produces feasibility.md and solution-design.md. Also trigger it in design-only mode when the implementation plan needs to change but requirements are stable. Invoke after /spec-agent produces an approved customer-spec.md. Hands off to /builder-agent after design approval.
---

# Solution Architecture Agent

**Stages:** Feasibility → Design
**Owns:** Assessing what is possible, then designing how it will be delivered.
**Receives from:** `/spec-agent` (approved `customer-spec.md`)
**Hands off to:** `/builder-agent`

---

## Stage Expectations

### Feasibility

| | |
|--|--|
| **Engineer provides** | Approved `customer-spec.md`, platform credentials |
| **Agent does** | Connects to platform, assesses capabilities, checks adapters, finds reuse candidates, identifies constraints |
| **Engineer action** | Reviews assessment and approves decision to proceed |
| **Deliverable** | `feasibility.md` (assessment + decision) |
| **Customer receives** | Feasibility assessment with a clear decision (feasible / feasible with constraints / not feasible), flagged constraints, and identified reuse opportunities. |

Feasibility confirms what is possible. Decision options: **feasible**, **feasible with constraints**, **feasible with changes**, or **not feasible**. Design does not start until feasibility is approved.

### Design

| | |
|--|--|
| **Engineer provides** | Approved `feasibility.md` |
| **Agent does** | Produces implementation design — component inventory, adapter mappings, reuse decisions, build order, test plan |
| **Engineer action** | Reviews and approves the solution design |
| **Deliverable** | `solution-design.md` (Solution Design / LLD, approved) |
| **Customer receives** | Solution Design / LLD — component inventory, adapter mappings, build order, and acceptance criteria mapped to tests. Nothing is built until this is signed off. |

Design defines how it will be delivered. Nothing is built until this is approved.

### Design-Only Mode

If requirements are unchanged but the implementation plan needs to change, invoke `/solution-architecture design-only`. Skips Feasibility. Reads existing `feasibility.md` as context and produces an updated `solution-design.md`.

---

## Artifact Lifecycle

```
${CLAUDE_PLUGIN_ROOT}/spec-files/spec-*.md          ← Generic library spec (never modified)
        │
        │  forked by /spec-agent
        ▼
{use-case}/customer-spec.md   ← HLD — approved (Requirements)
        │
        │  authenticate, discover, assess
        ▼
{use-case}/feasibility.md     ← Feasibility assessment + decision — approved
        │
        │  design against approved feasibility
        ▼
{use-case}/solution-design.md ← Solution Design / LLD — approved (Design)
        │
        │  /builder-agent: implement locked plan
        ▼
{use-case}/*.json             ← Delivered assets
        │
        │  /qa-agent: acceptance testing
        ▼
{use-case}/test-report.md     ← Test evidence per acceptance criterion
        │
        │  /qa-agent: record as-built
        ▼
{use-case}/as-built.md        ← Delivered state, deviations, learnings
```

---

## Spec File Structure

| Spec Section | What to Extract |
|-------------|----------------|
| **1. Problem Statement** | Context — what are we solving and why |
| **2. High-Level Flow** | The major phases to implement |
| **3. Phases** | What each phase does, decision points, stop/rollback conditions |
| **4. Key Design Decisions** | Constraints to honor during implementation |
| **5. Scope** | What to build, what NOT to build |
| **6. Risks & Mitigations** | Error handling and fallback behavior to build in |
| **7. Requirements** | **Capabilities, Integrations, Discovery Questions — drives design** |
| **8. Batch/Bulk Strategy** | Orchestration pattern if multi-device/multi-record |
| **9. Acceptance Criteria** | How to verify the build is correct |

Section 7 has three parts:
- **Capabilities** — what the platform must do → assessed during Feasibility
- **Integrations** — external systems → checked during Feasibility
- **Discovery Questions** — ask when platform data can't answer

---

## Feasibility

**Entered after `/spec-agent` produces an approved `customer-spec.md`.** Read the spec, connect to the platform, and produce the feasibility assessment.

### Step 1: Read the Approved Spec

Read `{use-case}/customer-spec.md` and extract:
- **Phases** from Section 3 (workflow stages)
- **Design decisions** from Section 4 (constraints)
- **Capabilities** table from Section 7 (platform checks)
- **Integrations** table from Section 7 (adapter checks)
- **Discovery questions** from Section 7
- **Acceptance criteria** from Section 9 (test cases)

### Step 2: Ask Only What the Spec Can't Answer

Go through the spec's Discovery Questions. Skip anything already answered by the spec. Ask only what platform data won't resolve.

### Step 3: Authenticate

**Now — and only now — connect to the platform.** The approved spec tells you exactly what data you need.

### Authenticate

Check for credentials in this order:
1. `{use-case}/.auth.json` — already authenticated (reuse token)
2. `{use-case}/.env` — credentials saved during setup
3. `${CLAUDE_PLUGIN_ROOT}/environments/*.env` — pre-configured environments at repo root

If none found, ask the engineer for:
1. Platform URL
2. Credentials (username/password or client_id/secret)

**Local Development (username/password):**
```
POST /login
Content-Type: application/json

{"username": "admin", "password": "admin"}
```
Returns a token string. Use as query parameter: `GET /endpoint?token=TOKEN`

**Cloud / OAuth (client_credentials):**
```
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
grant_type=client_credentials
```
Returns `{"access_token": "eyJhbG..."}`. Use as Bearer header.

**Save auth for all downstream skills:**
```bash
cat > {use-case}/.auth.json << EOF
{
  "platform_url": "https://platform.example.com",
  "auth_method": "oauth",
  "token": "eyJhbG...",
  "timestamp": "2026-03-13T10:00:00Z"
}
EOF
```

### Pull Platform Data

Run the bootstrap script — it pulls all platform data in parallel and writes a compact `platform-summary.json` with only what's needed for feasibility:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/.claude/skills/solution-arch-agent/pull-platform-data.py {use-case}
```

**What gets written:**

| File | Use for | Load into context? |
|------|---------|-------------------|
| `platform-summary.json` | Feasibility — running adapters, apps, type names, projects | ✅ Yes — compact |
| `openapi.json` | API reference — search locally with `jq` | ❌ No — too large |
| `tasks.json` | Task catalog — search locally with `jq` | ❌ No — too large |
| `apps.json` | Adapter type names — search locally with `jq` | ❌ No |
| `adapters.json` | Adapter instances — search locally with `jq` | ❌ No |
| `applications.json` | App health — search locally with `jq` | ❌ No |
| `workflows.json` | Existing workflows — search locally with `jq` | ❌ No |
| `projects.json` | Existing projects — search locally with `jq` | ❌ No |
| `devices.json` | Device inventory — search locally with `jq` | ❌ No |
| `device-groups.json` | Device groups — search locally with `jq` | ❌ No |

**After running, read `platform-summary.json` for feasibility. Search raw files locally when you need specifics — never load them into context.**

### File Shapes and jq Queries

Every file has a specific shape. Use these queries — don't guess.

| File | Shape | Example query |
|------|-------|---------------|
| `platform-summary.json` | `{adapters, applications, adapter_type_names, projects, workflow_count, device_count}` | `jq '.adapters[] | select(.connection == "ONLINE")' platform-summary.json` |
| `tasks.json` | plain array `[...]` | `jq '.[] | select(.name | test("X";"i")) | {name,app,type,location}' tasks.json` |
| `apps.json` | plain array `[...]` | `jq '.[] | select(.name | test("X";"i")) | {name,type}' apps.json` |
| `adapters.json` | `{"results":[...], "total":N}` | `jq '.results[] | select(.id | test("X";"i")) | {id,state,package_id}' adapters.json` |
| `applications.json` | `{"results":[...], "total":N}` | `jq '.results[] | select(.state=="RUNNING") | {id,package_id}' applications.json` |
| `workflows.json` | `{"items":[...], "count":N}` | `jq '.items[] | select(.name | test("X";"i")) | {name,_id}' workflows.json` |
| `projects.json` | `{"data":[...]}` | `jq '.data[] | select(.name | test("X";"i")) | {name,_id}' projects.json` |
| `devices.json` | `{"list":[...]}` | `jq '.list[] | select(.name | test("X";"i")) | {name,os}' devices.json` |
| `device-groups.json` | varies by platform | `jq 'type' device-groups.json` first to check shape |
| `openapi.json` | `{"paths":{...}}` | `jq '.paths["/the/endpoint"]' openapi.json` |

**Handling failures:** Before parsing any saved file, check if it contains valid JSON:
```bash
python3 -c "import json,sys; json.load(open(sys.argv[1])); print('ok')" {use-case}/devices.json 2>/dev/null || echo "empty"
```
If invalid, treat as "no data available" — don't block the flow.

### Resolve Capabilities

For each row in the spec's Capabilities table:
- Can the platform do this? → **✓ Resolved**
- Can't + Required? → **⚠ Blocked** (stop and discuss)
- Can't + Not Required? → **✗ Skipped** (use fallback from spec)

### Resolve Integrations

For each row in the spec's Integrations table:
- Found + Running? → **✓ Resolved** (record adapter name, app name)
- Found + Stopped? → **⚠ Warning** (needs to be started)
- Not found + Required? → **⚠ Blocked** (stop and discuss)
- Not found + Not Required? → **✗ Skipped**

### Find Reuse Opportunities

Search `workflows.json` for existing workflows that match spec phases. Flag as **↻ Reuse** candidates.

---

## Design

Produce the solution design from the approved spec + feasibility results.

### Produce `{use-case}/solution-design.md`

**Write the file to disk** using the Write tool. Contents:

**A. Environment Summary** — one paragraph

**B. Requirements Resolution**
```
┌─────────────────────────────────────────┬────────┬──────────────────────────────┐
│ Spec Requirement                        │ Status │ Resolution                   │
├─────────────────────────────────────────┼────────┼──────────────────────────────┤
│ Execute CLI commands on devices         │ ✓      │ MOP app + AutomationGateway  │
│ ITSM / ticketing                        │ ✓      │ ServiceNow adapter           │
│ Monitoring                              │ ✗      │ SKIP — engineer handles      │
└─────────────────────────────────────────┴────────┴──────────────────────────────┘
```

**C. Design Decisions**
```
┌─────────────────────────────────────┬────────────────────────────────────────┐
│ Decision                            │ In This Environment                    │
├─────────────────────────────────────┼────────────────────────────────────────┤
│ ITSM integration                    │ ServiceNow — create incidents          │
│ Naming convention                   │ VLAN_{id}_{site} (customer standard)   │
└─────────────────────────────────────┴────────────────────────────────────────┘
```

**D. Modular Design — Decompose First**

Before listing components, decide the parent/child split. Ask for each phase in the spec:

- Can it be run and tested independently? → **Child workflow**
- Does it make sense to reuse it in other use cases? → **Child workflow**
- Does it loop over multiple items? → **Child workflow with `loopType`**
- Is it a one-off step that only makes sense in this flow? → **Task in orchestrator**

**Rule:** Each logical phase becomes a child workflow. The orchestrator sequences them via childJob. This makes every phase independently testable before the orchestrator is built.

**Example decomposition:**
```
Spec phases → Component split
─────────────────────────────────────────────────────────
Pre-flight validation        → Child: Pre-Flight Check
Execute change               → Child: Execute Change
Verify propagation           → Child: Verify Propagation
Rollback on failure          → Child: Rollback
Notifications + ticket close → Tasks in orchestrator
```

The orchestrator is always the last thing built, after all children are tested.

**D. Component Inventory**
```
┌────┬──────────────────────────────┬─────────────────────┬──────────┐
│ #  │ Component                    │ Type                │ Action   │
├────┼──────────────────────────────┼─────────────────────┼──────────┤
│ 1  │ Pre-Check                    │ Command Template    │ Build    │
│ 2  │ Backup workflow              │ Child Workflow      │ Reuse    │
│ 3  │ Orchestrator                 │ Parent Workflow     │ Build    │
└────┴──────────────────────────────┴─────────────────────┴──────────┘
```

**E. Implementation Plan** — ordered build steps with test method for each

**F. Acceptance Criteria → Tests** — map each criterion to how to verify it. This is a first-pass mapping — `/qa-agent` refines it into an executable `test-plan.md` once real IDs exist after Build, but the verification *method* per criterion should be decided now, while the design is fresh.

### Present for Review

**Present the full solution design. Do NOT proceed to build until approved.**

Walk through each section:
- Requirements: "I'll use [adapter/app]. Correct?"
- Decisions: "The spec says [X], I'll do [Y]. Sound right?"
- Components: "Reuse this? Build that? Skip this?"
- Plan: "Here's the build order. Agree?"

The engineer may:
- Change reuse → build ("that workflow is outdated")
- Add components ("we also need a cleanup workflow")
- Change the plan order
- Modify how acceptance criteria get tested

Update `{use-case}/solution-design.md` with every change.

---

## Design Approval

**When the engineer approves the solution design: it is locked.**

Both artifacts are now complete before any building begins:
1. `{use-case}/customer-spec.md` — HLD, approved (Requirements)
2. `{use-case}/feasibility.md` — assessment + decision, approved (Feasibility)
3. `{use-case}/solution-design.md` — Solution Design / LLD, approved (Design)

Hand off to `/builder-agent`. The workspace is complete.

---

## Handoff to Builder

**The workspace the `/builder-agent` agent receives:**

```
{use-case}/
  .auth.json              ← auth token
  .env                    ← credentials (for re-auth)
  use-case-memory.md      ← living context: platform refs, built assets, decisions, open items
  customer-spec.md        ← approved HLD
  feasibility.md          ← approved feasibility assessment
  solution-design.md      ← approved Solution Design / LLD
  customer-context.md     ← business rules, naming (if provided)
  openapi.json            ← platform API reference (pulled during feasibility)
  tasks.json              ← task catalog (pulled during feasibility)
  apps.json               ← app/adapter type names (pulled during feasibility)
  adapters.json           ← adapter instances (pulled during feasibility)
  applications.json       ← app health (pulled during feasibility)
  devices.json            ← device inventory (if spec involves devices)
  workflows.json          ← existing workflows (if reuse planned)
  device-groups.json      ← device groups (if spec involves groups)
  task-schemas.json       ← fetched on demand by builder during build (not pre-populated)
```

The builder builds from the locked plan and tests each component individually. Once the build is complete, `/builder-agent` hands off to `/qa-agent`, which runs acceptance testing against Section F's criteria-to-tests mapping and produces the `as-built.md` record.

**Before handing off — update `use-case-memory.md`** (create from `helpers/use-case-memory.md` if `/spec-agent` didn't already):
- Platform URL and project name (if a project already exists)
- `Stage: build`, `Status: active`
- Any adapter instance names and type names resolved during feasibility
- Key decisions made during design (why this adapter, why this split, any constraints)

**Update `Stage` at each internal transition too, not just at final handoff** — set `Stage: feasibility` when starting the feasibility assessment (if `/spec-agent` left it at `requirements`) and `Stage: design` once feasibility is approved and design work begins. Someone resuming mid-Feasibility shouldn't see `Stage: build`.

The builder will read this file first and update it after every build session.

---

## How This Gets Invoked

Entered from `/spec-agent` after the engineer approves `customer-spec.md`. At that point the workspace contains:

```
{use-case}/
  customer-spec.md    ← approved HLD (Requirements complete)
  .env                ← credentials
```

```
/solution-architecture flow:
    Feasibility: authenticate → pull platform data → assess capabilities → write feasibility.md → engineer approves
    Design:      produce solution-design.md from approved feasibility → engineer approves
    Handoff:     pass complete workspace to /builder
```

To revise requirements: update `customer-spec.md` via `/spec-agent` → re-run `/solution-architecture` from Feasibility.
To revise design only: invoke `/solution-architecture design-only` → reads existing `feasibility.md` → produces updated `solution-design.md`.

---

## Gotchas

- OAuth MUST use `Content-Type: application/x-www-form-urlencoded`, not JSON
- Tokens expire mid-session — on auth errors, re-authenticate silently from `.env`
- `tasks/list` `app` field has WRONG casing for adapters — use `apps/list`
- OpenAPI spec is ~1.5MB — search it locally with `jq`, never load into context

````

============================================================
FILE: .claude/skills/solution-arch-agent/pull-platform-data.py
DIRECTORY: .claude/skills/solution-arch-agent/
FILENAME: pull-platform-data.py
============================================================
SHA256: 78f9d7669efac803aee341120edafa06d52217f185253d151649208e7dbf0919

````python
#!/usr/bin/env python3
"""
Pull platform data for feasibility assessment.
Writes raw files + platform-summary.json with only what the AI needs.

Usage:
    python3 pull-platform-data.py <use-case-dir>

Reads: {use-case}/.auth.json
Writes:
    {use-case}/openapi.json       — full OpenAPI spec (search locally, never load into context)
    {use-case}/tasks.json         — full task catalog
    {use-case}/apps.json          — adapter/app type names
    {use-case}/adapters.json      — adapter instances and status
    {use-case}/applications.json  — running applications
    {use-case}/platform-summary.json — compact summary for AI context
"""

import json, sys, os, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen, Request
from urllib.error import URLError

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pull-platform-data.py <use-case-dir>")
        sys.exit(1)

    use_case = sys.argv[1]
    auth_file = os.path.join(use_case, ".auth.json")

    if not os.path.exists(auth_file):
        print(f"ERROR: {auth_file} not found. Run authentication first.")
        sys.exit(1)

    with open(auth_file) as f:
        auth = json.load(f)

    base = auth["platform_url"].rstrip("/")
    token = auth["token"]
    headers = {"Authorization": f"Bearer {token}"}

    def get(path, out_file):
        url = f"{base}{path}"
        req = Request(url, headers=headers)
        try:
            with urlopen(req, timeout=120) as r:
                data = r.read().decode("utf-8")
            with open(os.path.join(use_case, out_file), "w") as f:
                f.write(data)
            return json.loads(data)
        except Exception as e:
            print(f"  WARN: {out_file} failed — {e}")
            return None

    encoded_base = urllib.parse.quote(base, safe="")

    print("Pulling platform data...")
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {
            "openapi":       pool.submit(get, f"/help/openapi?url={encoded_base}", "openapi.json"),
            "tasks":         pool.submit(get, "/workflow_builder/tasks/list", "tasks.json"),
            "apps":          pool.submit(get, "/automation-studio/apps/list", "apps.json"),
            "adapters":      pool.submit(get, "/health/adapters", "adapters.json"),
            "applications":  pool.submit(get, "/health/applications", "applications.json"),
            "workflows":     pool.submit(get, "/automation-studio/workflows?limit=500", "workflows.json"),
            "projects":      pool.submit(get, "/automation-studio/projects?limit=100", "projects.json"),
            "device_groups": pool.submit(get, "/configuration_manager/deviceGroups", "device-groups.json"),
        }
        # devices needs POST
        def get_devices():
            import json as _json
            url = f"{base}/configuration_manager/devices"
            body = _json.dumps({"options": {"start": 0, "limit": 1000, "sort": [{"name": 1}], "order": "ascending"}}).encode()
            req = Request(url, data=body, headers={**headers, "Content-Type": "application/json"})
            try:
                with urlopen(req, timeout=120) as r:
                    data = r.read().decode("utf-8")
                with open(os.path.join(use_case, "devices.json"), "w") as f:
                    f.write(data)
                return _json.loads(data)
            except Exception as e:
                print(f"  WARN: devices.json failed — {e}")
                return None
        futures["devices"] = pool.submit(get_devices)
        results = {k: v.result() for k, v in futures.items()}

    # Build compact summary — only what's needed for feasibility
    summary = {
        "platform_url": base,
        "adapters": [],
        "applications": [],
        "adapter_type_names": [],
        "workflow_count": 0,
        "device_count": 0,
        "device_group_count": 0,
        "projects": []
    }

    # Running adapters (name, package, state, connection)
    if results["adapters"] and isinstance(results["adapters"], dict):
        for a in results["adapters"].get("results", []):
            if a.get("state") == "RUNNING":
                summary["adapters"].append({
                    "name": a.get("id"),
                    "package_id": a.get("package_id"),
                    "connection": a.get("connection", {}).get("state")
                })

    # Running applications
    if results["applications"] and isinstance(results["applications"], dict):
        for a in results["applications"].get("results", []):
            if a.get("state") == "RUNNING":
                summary["applications"].append({
                    "name": a.get("id"),
                    "package_id": a.get("package_id")
                })

    # Adapter type names from apps (needed for workflow task app/locationType fields)
    if results["apps"] and isinstance(results["apps"], list):
        for a in results["apps"]:
            if a.get("type") == "Adapter":
                summary["adapter_type_names"].append(a.get("name"))

    # Counts only — AI searches raw files for details
    if results["workflows"] and isinstance(results["workflows"], dict):
        summary["workflow_count"] = results["workflows"].get("count", 0)

    if results["devices"] and isinstance(results["devices"], dict):
        summary["device_count"] = len(results["devices"].get("list", []))

    # Projects — name, id, component count in summary
    if results["projects"] and isinstance(results["projects"], dict):
        for p in results["projects"].get("data", []):
            summary["projects"].append({
                "name": p.get("name"),
                "id": p.get("_id"),
                "components": len(p.get("components") or [])
            })

    if results["device_groups"] and isinstance(results["device_groups"], (list, dict)):
        dg = results["device_groups"]
        summary["device_group_count"] = len(dg) if isinstance(dg, list) else len(dg.get("results", dg.get("list", [])))

    out = os.path.join(use_case, "platform-summary.json")
    with open(out, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nDone.")
    print(f"  Running adapters:     {len(summary['adapters'])}")
    print(f"  Running applications: {len(summary['applications'])}")
    print(f"  Adapter type names:   {len(summary['adapter_type_names'])}")
    print(f"  Workflows:            {summary['workflow_count']}")
    print(f"  Projects:             {len(summary['projects'])}")
    print(f"  Devices:              {summary['device_count']}")
    print(f"  Device groups:        {summary['device_group_count']}")
    print(f"  Summary:              {out}")
    print(f"\nFiles written to {use_case}/:")
    print(f"  platform-summary.json — read this for feasibility")
    print(f"  openapi.json, tasks.json, apps.json, adapters.json, applications.json")
    print(f"  workflows.json, projects.json, devices.json, device-groups.json")
    print(f"\nSearch raw files locally with jq — never load them into context.")

if __name__ == "__main__":
    main()

````

============================================================
FILE: .claude/skills/spec-agent/SKILL.md
DIRECTORY: .claude/skills/spec-agent/
FILENAME: SKILL.md
============================================================
SHA256: 2d820a3afe5b6464f54502a67308c47760e93886c93f04b950e650f217607aa4

````markdown
---
name: spec-agent
description: Use this skill to start any new automation delivery — when someone wants to automate something, build a new use case, figure out requirements, write up an HLD, or kick off a project on the Itential Platform. Trigger it for phrases like "I want to automate X", "help me build a workflow for Y", "we're starting a new automation project", "I need to define requirements for Z", "kick off a delivery", or "let's start with requirements". This is the entry point for the spec-driven delivery lifecycle. It picks from 22 built-in use case specs or starts from scratch, refines requirements with the engineer, and produces an approved customer-spec.md. Use it whenever someone is at the beginning of building something new and hasn't yet defined what they're building. For ad-hoc platform exploration, use /explore instead. Hands off to /solution-arch-agent after approval.
---

# Spec Agent

**Stage:** Requirements
**Owns:** Defining what needs to be built. Producing the approved HLD.
**Hands off to:** `/solution-arch-agent`

---

## Stage Expectations

| | |
|--|--|
| **Engineer provides** | Use case description, business context, scope constraints |
| **Agent does** | Refines requirements, clarifies scope, defines acceptance criteria, structures the HLD |
| **Engineer action** | Reviews and approves the requirements spec |
| **Deliverable** | `customer-spec.md` (HLD, approved) |
| **Customer receives** | Approved statement of what will be built — scope, constraints, acceptance criteria. Nothing is assessed or built until this is signed off. |

Requirements defines what is needed. Nothing is built or assessed until this is approved.

**No auth. No API calls. Pure conversation.**

---

## How to Begin

```
/spec-agent
    │
    ├── Deliver from Spec → Pick spec → Fork → Refine → Approve → /solution-arch-agent
    │
    └── Already set up? → Reuse existing working directory
```

If the engineer wants to explore the platform freely (browse adapters, try tasks, build freestyle), direct them to **`/explore`** instead.

---

## Step 1: Pick a Spec

Present available specs from `${CLAUDE_PLUGIN_ROOT}/spec-files/`, grouped by category:

| Category | Specs |
|----------|-------|
| **Networking** | Port Turn-Up, VLAN Provisioning, Circuit Provisioning, BGP Peer, VPN Tunnel, WAN Bandwidth |
| **Operations** | Software Upgrade, Config Backup, Health Check, Device Onboarding, Device Decommissioning, Change Management, Incident Remediation |
| **Security** | Firewall Rules, Cloud Security Groups, SSL Certificates |
| **Infrastructure** | DNS Records, IPAM Lifecycle, Load Balancer VIP, Config Drift Remediation, Compliance Audit |

Or the engineer describes what they need and you recommend a spec.

---

## Step 2: Fork the Spec

```bash
mkdir -p {use-case-name}
# Only fork if it doesn't already exist — engineer may have customized from a previous session
[ ! -f {use-case}/customer-spec.md ] && cp ${CLAUDE_PLUGIN_ROOT}/spec-files/spec-port-turn-up.md {use-case}/customer-spec.md
```

If `{use-case}/customer-spec.md` already exists, **reuse it** — do not overwrite.

If the engineer provided credentials or a `.env` file exists, save it to `{use-case}/.env` for later use during Feasibility. Do NOT authenticate yet.

---

## Step 3: Understand and Refine

Read `{use-case}/customer-spec.md` and extract:
- **Phases** from Section 3 (workflow stages)
- **Design decisions** from Section 4 (constraints)
- **Capabilities** and **Integrations** tables from Section 7
- **Discovery questions** from Section 7
- **Acceptance criteria** from Section 9

Ask: *"Do you have existing documentation I should follow? Naming conventions, change policies, runbooks, config standards?"*

Write to `{use-case}/customer-context.md` if provided.

Then go through the spec's discovery questions — skip anything the spec already answers, ask only what the engineer must decide.

Incorporate all input into `{use-case}/customer-spec.md`:
- Added requirements → Section 7
- Changed scope → Section 5
- Business rules → relevant sections
- Changed decisions → Section 4

---

## Step 4: Present for Approval

Show the engineer the updated spec:
- Summary of changes from the generic spec
- What's in scope vs out of scope
- Discovery question answers captured

Ask: *"Here's your spec. Review it — add, remove, or change anything. When you approve it, I'll hand off to the Solution Architecture Agent."*

**When the engineer approves: the spec is locked.** Save the file.

---

## Step 5: Set Expectations and Hand Off

Tell the engineer what happens next:

> "Requirements are locked. Here's the rest of the delivery:
>
> 1. **Feasibility** — The Solution Architecture Agent connects to your platform and assesses what's possible against your approved spec.
> 2. **Design** — A solution design is produced with exactly what to build, reuse, and skip. You approve it before anything is built.
> 3. **Build** — The Builder Agent implements the approved design and tests each component individually.
> 4. **Test** — The QA Agent drafts a test plan from your acceptance criteria, which you approve before anything runs live, then verifies the delivered solution against it with real evidence.
> 5. **As-Built** — What was actually delivered is recorded, backed by that test evidence, including any deviations and learnings.
>
> You own approval at Feasibility, Design, and the Test Plan. Nothing gets built or tested live without your sign-off."

**Artifact-based handoff.** The workspace the Solution Architecture Agent receives:

```
{use-case}/
  customer-spec.md     ← approved HLD (Requirements complete)
  .env                 ← credentials (if provided)
  customer-context.md  ← business rules, naming (if provided)
  use-case-memory.md   ← create from helpers/use-case-memory.md, set Stage: feasibility, Status: active
```

Create `use-case-memory.md` at handoff — populate the use-case name, one-sentence description, and `Stage: feasibility` / `Status: active`. The solution-arch-agent will add platform refs and adapter details during feasibility, and update `Stage` again at its own handoff; the builder will add asset IDs and decisions during build.

No auth. No platform data. `/solution-arch-agent` owns everything from Feasibility onward.

---

## Files Created

| File | Purpose |
|------|---------|
| `customer-spec.md` | Approved HLD — the source of truth for this delivery |
| `.env` | Credentials saved for later auth during Feasibility |
| `customer-context.md` | Business rules and naming conventions (if provided) |
| `use-case-memory.md` | Living context file — initialized here, updated throughout all stages |

````

============================================================
FILE: .github/ISSUE_TEMPLATE/bug_report.md
DIRECTORY: .github/ISSUE_TEMPLATE/
FILENAME: bug_report.md
============================================================
SHA256: 81cc3cbf243bb2eb26111994422f03adf9dc614d5cdbbb201d778ba4aee31a40

````markdown
---
name: Bug Report
about: Create a report to help us improve
title: 'bug: '
labels: bug
assignees: ''
---

## Description

## Reproduction Steps

## Expected Behavior

## Environment

- **OS:**
- **Version:**
- **Python/Node/Go Version (if applicable):**

## Checklist

- [ ] I have checked existing issues to avoid duplicates
- [ ] I have provided a clear description of the issue
- [ ] I have included steps to reproduce (if applicable)
- [ ] I have included relevant environment details

````

============================================================
FILE: .github/ISSUE_TEMPLATE/feature_request.md
DIRECTORY: .github/ISSUE_TEMPLATE/
FILENAME: feature_request.md
============================================================
SHA256: 260c4717583d1fe536fb0e7c23a621258e4b39bc9535ff39f6fb35e3063bd4dc

````markdown
---
name: New Feature
about: Suggest an idea for this project
title: 'feat: '
labels: enhancement
assignees: ''
---

## Problem Statement

## Proposed Solution

## Alternatives Considered

## Checklist

- [ ] I have checked existing issues to avoid duplicates
- [ ] I have described the problem and solution clearly
- [ ] I have considered the scope and complexity

````

============================================================
FILE: .github/pull_request_template.md
DIRECTORY: .github/
FILENAME: pull_request_template.md
============================================================
SHA256: d31d77e7636059b3bb3a444e0d042b35a2f3f04120d4b3cba5b2322f258c7277

````markdown
## Description

<!-- What does this PR do? Why is it needed? -->

## Type of Change

<!-- Mark the appropriate option with an "x" -->

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Refactor
- [ ] Chore

## Changes Made

<!-- Summarize the key changes in this PR -->

## Testing

<!-- Describe how you tested your changes -->

## Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code has been performed
- [ ] Code has been commented where necessary
- [ ] Tested with `make setup` or relevant profile
- [ ] Commits follow conventional format (`type: subject`)
- [ ] No secrets or credentials committed
- [ ] Documentation has been updated accordingly
- [ ] PR has been labeled appropriately (`enhancement`, `bug`, `documentation`, `refactor`, `chore`)

````

============================================================
FILE: .github/workflows/pr-compliance.yml
DIRECTORY: .github/workflows/
FILENAME: pr-compliance.yml
============================================================
SHA256: a83bd51e8568c10281139638d3f00c0fd835acb7df4e6fe5e6c3c7ad2e05e194

````yaml
name: PR Compliance

on:
  pull_request:
    types: [opened, edited, reopened, synchronize]
    branches: [main]

jobs:
  branch-naming:
    name: Branch Naming
    runs-on: ubuntu-latest
    steps:
      - name: Validate branch name
        run: |
          branch="${{ github.head_ref }}"
          pattern="^(feature|fix|refactor|docs|chore)/[a-z][a-z0-9-]*$"
          if [[ ! "$branch" =~ $pattern ]]; then
            echo "::error::Branch '$branch' does not follow naming conventions."
            echo ""
            echo "Required format: <type>/<description>"
            echo "Valid types:     feature, fix, refactor, docs, chore"
            echo "Description:     lowercase letters, numbers, and hyphens only"
            echo "Example:         feature/add-auth-middleware"
            exit 1
          fi
          echo "Branch name '$branch' is valid."

  commit-messages:
    name: Commit Messages
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Validate conventional commits
        run: |
          pattern="^(feat|fix|docs|style|refactor|test|chore|perf)(\(.+\))?: .{1,72}"
          failed=0
          count=0

          while IFS= read -r msg; do
            [[ -z "$msg" ]] && continue
            count=$((count + 1))
            if [[ "$msg" =~ ^Merge ]]; then
              echo "::error::Merge commit found: '$msg'"
              echo "  Merge commits are not allowed — use squash or rebase instead."
              failed=1
            elif [[ ! "$msg" =~ $pattern ]]; then
              echo "::error::Non-conforming commit: '$msg'"
              echo "  Expected: <type>[(scope)]: <description>"
              echo "  Valid types: feat, fix, docs, style, refactor, test, chore, perf"
              echo "  Example: feat(auth): add JWT token validation"
              failed=1
            else
              echo "  OK: $msg"
            fi
          done < <(git log --format="%s" "origin/${{ github.base_ref }}..${{ github.event.pull_request.head.sha }}")

          if [[ $count -eq 0 ]]; then
            echo "No new commits found."
            exit 0
          fi

          echo ""
          if [[ $failed -eq 1 ]]; then
            echo "One or more commits do not follow conventional commit format."
            echo "See CONTRIBUTING.md for commit message guidelines."
            exit 1
          fi

          echo "All $count commit(s) conform to conventional commits."

````

============================================================
FILE: .gitignore
DIRECTORY: ./
FILENAME: .gitignore
============================================================
SHA256: b6b6103aa788739b122b84cc1bf7a5c7f00a6b774c26b5598a3dc9ddb4fb3665

````text
# =============================================================================
# OS Generated Files
# =============================================================================
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
desktop.ini

# =============================================================================
# Editor and IDE
# =============================================================================
# JetBrains (IntelliJ, PyCharm, GoLand, etc.)
.idea/

# VS Code (uncomment to ignore all settings, or keep to share workspace config)
# .vscode/

# Vim
*.swp
*.swo
*~

# Emacs
\#*\#
.#*

# =============================================================================
# Security - NEVER commit these
# =============================================================================
.env
.env.*
!.env.example
.auth.json
*.pem
*.key
*.p12
*.pfx
credentials.json
secrets.yaml
secrets.yml

# =============================================================================
# Logs and Databases
# =============================================================================
*.log
logs/
*.sqlite
*.sqlite3
*.db

# =============================================================================
# Build Artifacts and Caches
# =============================================================================
dist/
build/
out/
.cache/
*.tmp
*.temp

# =============================================================================
# Test Coverage
# =============================================================================
coverage/
htmlcov/
.coverage
*.cover

# =============================================================================
# Platform and Use-Case Runtime Data
# =============================================================================
# Pulled from live platform — not committed, regenerated via scripts/
platform/
use-cases/

# =============================================================================
# Eval Run Artifacts
# =============================================================================
# Generated by running evals/ (transcripts, outputs, grading.json, benchmark
# files, rendered viewer HTML) — regenerate via the skill-creator eval pipeline.
# Keep evals/evals.json and evals/COVERAGE-REPORT.md tracked (those are source).
evals/workspace/

# =============================================================================
# MAINTAINER: Add language-specific patterns below
# =============================================================================
# Examples:
#
# Python:
#   __pycache__/
#   *.py[cod]
#   .venv/
#   venv/
#   .pytest_cache/
#
# Node.js:
#   node_modules/
#   npm-debug.log
#   .npm/
#
# Go:
#   vendor/
#   *.exe
#
# Rust:
#   target/
#   Cargo.lock (for libraries only)

````

============================================================
FILE: AGENTS.md
DIRECTORY: ./
FILENAME: AGENTS.md
============================================================
SHA256: 70374eab431cc0f59fc61eb9d0393d7f0cb758c96e364564ae28412a3248a28b

````markdown
# Itential Platform - AI Agent Guide

This project contains skills for assisting developers on the Itential Platform. Read this first, then use the skills for detailed API references.

## Skill Router

Each skill owns a domain. **Invoke the skill using the Skill tool before working in that domain.** Skills contain the correct API methods, request bodies, response shapes, and patterns. Don't guess — load the skill.

| Skill | Agent | When to Use |
|-------|-------|-------------|
| `/explore` | — | Explore a platform freely — auth, discover, browse, build freestyle. |
| `/spec-agent` | **Spec Agent** | Start a delivery from a spec. Owns Requirements stage. |
| `/project-to-spec` | — | Read an existing project → produce customer-spec.md + solution-design.md. |
| `/documentation` | — | Survey global platform assets → discover relationships → group by use case → produce HLD+LLD per use case → optionally create projects and move assets in. For a specific named project, redirect to `/project-to-spec`. |
| `/flowagent-to-spec` | — | Read a FlowAgent → produce customer-spec.md as a deterministic workflow spec. |
| `/solution-arch-agent` | **Solution Architecture Agent** | Feasibility assessment + solution design. Runs after Requirements. |
| `/builder-agent` | **Builder Agent** | Build all assets, test each component individually. Runs after Design. |
| `/qa-agent` | **QA Agent** | Acceptance testing against the approved acceptance criteria + as-built record. Runs after Build — last technical stage before customer sign-off. |
| `/iag` | — | Automation Gateway: IAG services (Python, Ansible, OpenTofu). |
| `/flowagent` | — | AI Agents: configure LLM providers, tools, and agent sessions. |
| `/itential-mop` | — | Command templates with validation rules. |
| `/itential-devices` | — | Devices, backups, diffs, device groups. |
| `/itential-golden-config` | — | Golden config, compliance, grading, remediation. |
| `/itential-inventory` | — | Device inventories, nodes, actions, tags. |
| `/itential-lcm` | — | Resource models, instances, lifecycle actions. |
| `/itential-json-forms` | — | JSON Forms: static-enum, REST-bound, and cascading dropdowns for manual triggers and manual tasks. |

### Delivery Lifecycle

Spec-based delivery follows six stages. Each stage has a named agent, a clear input, and a deliverable.

```
Requirements → Feasibility →   Design    →  Build   →    Test    →  As-Built
      │              │             │            │             │            │
  Spec Agent   Solution Arch  Solution Arch  Builder      QA Agent    QA Agent
                   Agent          Agent       Agent
      │              │             │            │             │            │
  customer-      feasibility.md solution-    assets/    test-report.md as-built.md
  spec.md        (assessment    design.md    configs    (evidence per  (delivered
  (approved)     + decision)   (approved)   (delivered) criterion, from   state,
                                                          test-plan.md    deviations,
                                                          approved by     learnings)
                                                          engineer)      ↳ design updates
                                                                         ↳ spec amendments
```

**Deliverables:**

| Deliverable | Artifact | Produced by | Audience |
|-------------|----------|-------------|----------|
| HLD | `customer-spec.md` | Spec Agent | Customer / stakeholder |
| Feasibility Assessment | `feasibility.md` | Solution Architecture Agent | Customer / architect |
| Solution Design / LLD | `solution-design.md` | Solution Architecture Agent | Engineer / delivery team |
| Test Plan | `test-plan.md` | QA Agent | Engineer (approves before any live test execution) |
| Test Report | `test-report.md` | QA Agent | Customer / delivery — evidence per acceptance criterion |
| As-Built | `as-built.md` | QA Agent | Customer / delivery / support / system of record |

**Explore path** (no spec, no delivery lifecycle):
```
/explore → auth → pull platform data → summarize → use skills directly
```

**IMPORTANT: Invoke skills using the Skill tool** — don't just reference them in text. When you need to build workflows/templates, invoke `/builder-agent`. When a build needs acceptance testing or a closeout record, invoke `/qa-agent`. The skills contain the API details you need. Without loading them, you're guessing.

### Directory Layout

Platform data (shared, pulled once) and use-case data (per engagement) live in separate directories. **Never mix them.**

```
builder-skills/
├── platform/               ← shared pre-pull via scripts/platform_pull.py (fallback only)
│   ├── openapi.json        — full API reference
│   ├── tasks.json          — task catalog
│   ├── apps.json           — app and adapter type names
│   ├── adapters.json       — adapter instances and state
│   ├── applications.json   — application details
│   ├── environment.md      — human-readable summary
│   └── .pulled-at          — timestamp of last pull
│
└── use-cases/
    └── <use-case-name>/    ← scaffolded via scripts/use_case_init.py
        ├── .env              — credentials (gitignored)
        ├── .auth.json        — live bearer token (gitignored, auto-refreshed)
        ├── openapi.json      — pulled fresh by /explore or /solution-arch-agent (prefer over platform/)
        ├── tasks.json        — pulled fresh per engagement (prefer over platform/)
        ├── apps.json         — pulled fresh per engagement (prefer over platform/)
        ├── adapters.json     — pulled fresh per engagement (prefer over platform/)
        ├── applications.json — pulled fresh per engagement (prefer over platform/)
        ├── task-schemas.json — fetched on demand during build, never pre-populated
        ├── use-case-memory.md — living context: IDs, decisions, gotchas, test log, open items
        └── (deliverables: customer-spec.md, feasibility.md, solution-design.md, test-plan.md, test-cases.json, test-report.md, as-built.md)
```

**Setup sequence (one-time per platform):**
```bash
./scripts/platform_pull.py <platform-url> <client-id> <client-secret>
```

**Per use-case:**
```bash
./scripts/use_case_init.py <use-case-name> <platform-url> <client-id> <client-secret>
```

**Refresh platform data** (after platform upgrade or new adapters installed):
```bash
./scripts/platform_pull.py --refresh <platform-url> <client-id> <client-secret>
```

**At the start of every session — read the memory file first:**
```bash
cat use-cases/<name>/use-case-memory.md
```
It contains the platform URL, project ID, what's already built, decisions made, and open items. Don't re-discover what's already documented. If the file doesn't exist, create it from `helpers/use-case-memory.md`.

### Resuming a Use-Case

`use-case-memory.md`'s `Stage` field tells you where to pick up — but a field can go stale (an agent forgets to update it, a session gets interrupted mid-write). **Verify `Stage` against which files actually exist before trusting it.** If they disagree, the files are ground truth — investigate the mismatch before proceeding, don't just pick one.

| `Stage` says | Files that should exist | Files that should NOT exist yet |
|---|---|---|
| `requirements` | (nothing yet, or a draft `customer-spec.md`) | `feasibility.md` |
| `feasibility` | `customer-spec.md` (approved) | `feasibility.md` (approved) |
| `design` | `feasibility.md` (approved) | `solution-design.md` (approved) |
| `build` | `solution-design.md` (approved) | Component Inventory (§D) has real IDs |
| `test` | `solution-design.md` §D has real IDs | `test-report.md` (complete) |
| `as-built` | `test-report.md` (all cases passing, or residuals explicitly accepted) | `as-built.md` |
| `delivered` | `as-built.md` (signed off) | — |

`Status: on-hold` can apply at any `Stage` — it means work is paused, not that the stage is wrong. Every skill that hands off to another stage MUST update `Stage` (and `Last updated`) before ending its session — see each skill's handoff section for the exact point to do it.

**Data lookup order:**
- `{use-case}/tasks.json`, `apps.json`, `adapters.json`, `openapi.json` — pulled by `/solution-arch-agent` or `/explore` during feasibility. **Always prefer these — they are per-engagement and fresh.**
- `platform/tasks.json`, `platform/apps.json` etc. — pulled once by `scripts/platform_pull.py`, shared across engagements. Use as fallback only if `{use-case}/` files are missing.
- `{use-case}/task-schemas.json` — fetched on demand during build (never pre-populated). Append after every fetch; never re-fetch what's already cached.
- If neither `{use-case}/tasks.json` nor `platform/tasks.json` exist → tell the user to run `/explore` or `scripts/platform_pull.py` first.

### Auth Reuse — Authenticate Once, Reuse Everywhere

**Auth happens when first needed** — in `/explore` (explore path) or in `/solution-arch-agent` during Feasibility. The token is saved to `use-cases/{use-case}/.auth.json`. Every subsequent skill should:
1. Read `use-cases/{use-case}/.auth.json` for the token
2. Read `use-cases/{use-case}/.env` for `PLATFORM_URL` and credentials
3. Use the token for all API calls (Bearer header for OAuth)
4. On auth error (401/403): re-authenticate silently — see procedure below
5. **Never ask the user for credentials if `.env` exists**

This means the user authenticates once and every subsequent skill just works.

**Token expiry — silent re-auth procedure:**

When any API call returns 401 or 403, do not stop and do not ask the user. Re-authenticate silently:

1. Read credentials from `use-cases/{use-case}/.env`
2. Call: `POST {PLATFORM_URL}/oauth/token` with `Content-Type: application/x-www-form-urlencoded` and body `grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}`
3. Write the new token back to `use-cases/{use-case}/.auth.json`
4. Retry the failed request with the new token

If `.env` does not exist and re-auth is needed, then and only then ask the user for credentials.

### Key Rule: Look Up Before You Act — Don't Guess

**Skills** teach patterns, workflows, and know-how (how to build a childJob, how to wire variables, how to test).

**`platform/openapi.json`** has every endpoint, method, request body, and response schema. Search it locally — never load the full file into context.

**Before making any API call:**
1. Check the relevant skill for the pattern
2. Search `platform/openapi.json` to confirm the endpoint, method, request body, and response schema — `jq '.paths["/the/endpoint"]' platform/openapi.json`
3. **Check the body wrapper** — most Itential APIs wrap the body in a top-level key. Find it: `jq '.paths["/the/endpoint"].post.requestBody.content["application/json"].schema.properties | keys' platform/openapi.json` → returns the wrapper name (e.g., `["role"]` means `{role: {...}}`)
4. Never hardcode API assumptions — the spec is the source of truth

**Before fetching task schemas:**
1. Check if `use-cases/{use-case}/task-schemas.json` exists — search it first with `jq` or `grep`
2. Only call `multipleTaskDetails` for tasks NOT already in the local file
3. After fetching, always append to the local file so future lookups are instant

**Before parsing any local JSON file:**
1. Check the response shape first — `jq type` and `jq keys` on the file
2. The `/solution-arch-agent` skill has a file-to-shape table — use it
3. Key shapes to remember:
   - `adapters.json` → `{"results": [...]}`
   - `applications.json` → `{"results": [...]}`
   - `devices.json` → `{"list": [...]}`
   - `workflows.json` → `{"items": [...]}`
   - `apps.json` → plain array `[...]`
   - `tasks.json` → plain array `[...]`
4. Use `jq` for parsing, not inline Python scripts with isinstance fallbacks

**When something fails or returns unexpected data — check local files FIRST:**
1. **`openapi.json`** — verify the endpoint exists, check the method (GET vs POST), read the request body schema and response schema. This file has EVERY endpoint, field, and type. Don't guess what a payload looks like — look it up.
2. **`tasks.json`** — verify the task name, app, location. If a task is "not found," search here first.
3. **`task-schemas.json`** — if you already fetched schemas, the full input/output definition is here. Check field names, types, required vs optional.
4. **`adapters.json` / `apps.json`** — verify adapter instance names, app names, casing. Adapter names from `apps.json` (type name) differ from `adapters.json` (instance name).
5. **`job.error` array** — for runtime errors (not just task status)
6. **Actual task output** — `status: complete` doesn't mean the CLI commands worked

**The filesystem is your debugger.** Every API endpoint, every task schema, every adapter name is already saved locally after setup. Never guess a payload structure, field name, or endpoint path — the answer is in these files. Reading a local file costs zero API calls and zero time.

## Understanding User Intent

Figure out which **category of work** the user needs:

- **Building** — create something new (workflow, template, compliance standard). Start with requirements, then build.
- **Operating** — do something now (configure a device, run compliance, backup configs). Identify targets and execute.
- **Exploring** — understand what's available (devices, adapters, workflows). Discover and navigate.
- **Debugging** — something broke (workflow failing, adapter errors). Get job details, check `job.error`.
- **Designing** — planning architecture (modular workflows, compliance hierarchy). Think before building.

## Developer Flow

Six stages. Four agents. Each stage has a named agent, a clear input, and a deliverable. Nothing moves forward without the engineer's sign-off at each stage.

```
Requirements → Feasibility →   Design    →  Build   →    Test    →  As-Built
      │              │             │            │             │            │
 /spec-agent   /solution-     /solution-   /builder-     /qa-agent   /qa-agent
                arch-agent     arch-agent    agent
      │              │             │            │             │            │
  customer-      feasibility.md solution-    assets/    test-plan.md  as-built.md
  spec.md        (approved)     design.md   (delivered) (approved),   (approved)
  (approved)                    (approved)              test-report.md
```

**Stage summaries:**

| Stage | Agent | What happens | Engineer does |
|-------|-------|-------------|---------------|
| Requirements | `/spec-agent` | Refines use case, defines scope, structures HLD | Approves `customer-spec.md` |
| Feasibility | `/solution-arch-agent` | Connects to platform, assesses capabilities, flags constraints | Approves `feasibility.md` |
| Design | `/solution-arch-agent` | Produces component inventory, adapter mappings, build plan, acceptance-criteria-to-test mapping | Approves `solution-design.md` |
| Build | `/builder-agent` | Builds all assets, tests each component individually, delivers | Reviews and accepts delivery |
| Test | `/qa-agent` | Drafts `test-plan.md`, runs static + acceptance test cases against confirmed test data, reports evidence | Approves `test-plan.md` before live execution; reviews `test-report.md` |
| As-Built | `/qa-agent` | Records delivered state, deviations, learnings, backed by test evidence | Signs off on `as-built.md` |

**For explore / freestyle work:**
```
/spec-agent → auth → pull platform data → use skills directly
```

## Key Rules

1. **Never invent task names** — always look them up from `tasks/list`
2. **Always get the schema before building** — `multipleTaskDetails?dereferenceSchemas=true`
3. **Adapter `app` AND `locationType` fields come from `apps/list`**, not `tasks/list` (names can be completely different, not just casing). The `app` field is the adapter **type name** (e.g., `EmailOpensource`), NOT the adapter **instance name** (e.g., `email`). Using the instance name causes `"No config found for Adapter"` errors. Resolve from local `apps.json` and `adapters.json`. When multiple adapter apps exist for the same product, ask the user.
4. **Test each piece individually** before composing into a larger workflow
5. **Check `job.error` for failures**, not just task status
6. **Variable syntax differs by context:**
   - Jinja2 templates: `{{ var }}`
   - Command templates / makeData: `<!var!>`
   - Workflow wiring: `$var.job.x`
   - childJob variable refs: `{"task": "job", "value": "varName"}`
   - merge/evaluation refs: `{"task": "job", "variable": "varName"}` (NOT `"value"` — different field than childJob)
7. **Validation errors = draft workflow** that cannot be started
8. **`$var` references don't resolve inside object values** (e.g., inside `newVariable` value or adapter `body`) — use `merge`, `makeData`, `query`, or other utility tasks to build the object, then pass it as a top-level `$var` reference
9. **Task IDs are hex-only** — `[0-9a-f]{1,4}`. Non-hex IDs (e.g., `qt`, `ok`, `success`, `err1`) cause two problems: (a) `$var` references silently fail at runtime (classified as static), and (b) **project import fails** with `"must NOT have additional properties"` — the import schema rejects any task key that is not `workflow_start`, `workflow_end`, or a valid hex ID. Always generate task IDs in hex format from the start. To fix existing workflows with bad IDs: rename tasks in-place via PUT, updating transitions and all `$var.<taskId>.*` references simultaneously.
10. **`genericAdapterRequest` prepends the adapter's `base_path`** to `uriPath` — don't include `/api/v1` in `uriPath`. Use `genericAdapterRequestNoBasePath` if you need the full path
11. **Use `POST /projects/import` to create projects atomically** — build all assets locally, pre-compute the project `_id`, pre-wire childJob `@projectId:` refs, then import everything in one call. Avoid the create-then-move pattern (breaks childJob refs, causes project-locking issues).
11a. **Patch project membership immediately after every create or import** — the platform sets the OAuth service account as the sole owner on creation, locking out human users. Immediately after `POST /automation-studio/projects` or `POST /automation-studio/projects/import`, call `PATCH /automation-studio/projects/{id}` to add the engineer's user account or group as owner. This is mandatory — skip it and the engineer cannot open the project. Resolve reference IDs by scanning existing projects (see "Resolve membership references" below). PATCH is a **full replacement** — always include all members, including the service account, or they will be removed.
11b. **Project thumbnails use a data URI, not raw base64** — `PUT /automation-studio/projects/{id}/thumbnail` expects `{"imageData": "data:image/png;base64,...", "backgroundColor": "#RRGGBB"}`. Passing raw base64 without the `data:image/png;base64,` prefix results in a black/blank thumbnail in the UI. Use `GET /automation-studio/projects/{id}/thumbnail` to retrieve; the response is `{"data": {"image": "data:image/png;base64,...", "backgroundColor": "..."}}`. Accepted formats: jpg, jpeg, png up to 1000 KB. **Optimal dimensions: 330×100 px.**
12. **API response shapes vary** — projects use `{message, data, metadata}`, but workflow and template lists use `{items, skip, limit, total}`, and create endpoints return `{created, edit}`. Always check the response shape before parsing
13. **Project component types** — valid values: `workflow`, `template`, `transformation`, `jsonForm`, `mopCommandTemplate`, `mopAnalyticTemplate`
14. **Use skills, don't reimplement** — `/builder-agent` covers projects, workflows, templates, MOP, and component-level testing. Acceptance testing and as-built records are `/qa-agent`'s job, not builder-agent's. Only load other skills for their specific domains (IAG, FlowAgent, MOP, etc.)
15. **When unsure about ANY endpoint, method, or payload — check `openapi.json` FIRST.** Run `jq '.paths["/the/endpoint"]' platform/openapi.json` to see the method, request body schema, and response schema. Don't guess, don't try variations, don't make up field names — look it up. The spec is always right.
16. **If `openapi.json` is not local, fetch it** — `GET /help/openapi?url={ENCODED_BASE}` and save it. Then search locally.
17. **If the openapi schema is empty for an endpoint** — check the corresponding POST/PUT endpoint's schema for the wrapper pattern. As a last resort, send `{}` and read the `"Missing Params"` error — it lists every required field with name, type, and examples.
18. **Endpoint base paths differ** — task catalog is at `/workflow_builder/tasks/list`, but task schemas are at `/automation-studio/multipleTaskDetails` (NOT `/workflow_builder/multipleTaskDetails`). Don't mix them up.
19. **Error transitions are mandatory on adapter/external tasks** — without an error transition, task errors produce "Job has no available transitions" and the job gets stuck forever. Always add `"state": "error"` transitions on tasks that call adapters or external systems.
20. **Adapter responses are transformed** — adapters reshape the upstream API response. Don't assume the native API's response structure (e.g., ServiceNow `result.sys_id`). Call the adapter endpoint directly or check `openapi.json` to verify the actual response shape before wiring query paths.
21. **Duplicate transition keys to same target** — JSON doesn't allow two keys with the same name. If a task needs both `success` and `error` to reach `workflow_end`, create an error handler task (e.g., `newVariable` to set error status) and route error there, then route that task to `workflow_end`.
22. **Respect task schema data types** — When wiring task inputs, match the type from `task-schemas.json` exactly. If a field is typed as `array`, pass an array (e.g., `["joksan@example.com"]`), not a bare string. If typed as `number`, pass a number, not a string. Common offenders: `to`/`cc`/`bcc` in email tasks (arrays, not strings), `pageSize`/`page` in queries (numbers, not strings). Mismatched types cause silent failures or validation errors.
23. **Adapter `app` ≠ adapter instance name** — The `app` and `locationType` fields on adapter tasks must be the adapter **type name** from `apps.json` (e.g., `EmailOpensource`, `Servicenow`), NOT the adapter **instance name** from `adapters.json` (e.g., `email`, `servicenow-prod`). Using the instance name causes `"No config found for Adapter: <name>"` at runtime. The `adapter_id` field is where the instance name goes. Triple-check: `app` = type, `adapter_id` = instance.
24. **Project-scoped asset names** — once an asset is added to a project, its `name` is prefixed with `@{projectId}: `. When reading or updating a project-owned asset via PUT, you MUST use the scoped name or the API returns 400. Read the asset first to get its current name, or construct it as `@{projectId}: {displayName}`. Strip this prefix when displaying names to the user.
25. **NEVER wire a Configuration Manager remediation task** — `runAutoRemediation`, `advancedAutoRemediation`, `convertChangesToConfig`, `patchDeviceConfiguration`, `advancedPatchDeviceConfiguration`, `patchCMDeviceConfiguration`, `ManualRemediation`, and `ManualRemediationResults` are prohibited in every workflow, even when a spec asks for fully automatic remediation. Golden Config detects and reports drift; it never applies fixes to a device. To correct a device, build a normal config-push delivery using the environment's config-push task (`sendConfig`/`runService` via GatewayManager, `itential_cli`, or netmiko send-config). See the `/itential-golden-config` Remediation section. (`updateNodeConfig` is allowed — it authors the GC node template, not a device.)

## Helper JSON Templates

**For workflow design and task wiring — read from `helpers/assets/` first.** The asset projects are real, tested, production imports. Extract task structures, variable wiring, transition patterns, and transformation usage directly from those files. Do not invent task schemas from memory.

**For API call bodies (create, update, operations) — use the helpers below.** These cover request wrappers and field names for endpoints that the asset projects don't demonstrate.

Helper templates are organized in subdirectories under `helpers/`:

**`helpers/create/`** — POST bodies for creating assets

| File | Purpose |
|------|---------|
| `create-workflow.json` | Workflow scaffold with start/end tasks |
| `create-project.json` | Project creation |
| `import-project.json` | Import a project (atomic — preferred over create + add) |
| `create-command-template.json` | Command template with `<!var!>` syntax |
| `create-template-jinja2.json` | Jinja2 template |
| `create-template-textfsm.json` | TextFSM template |
| `create-json-form.json` | JSON form for user input |
| `create-json-form-rest-bound.json` | JSON form with REST-bound dropdowns |
| `create-ops-manager-automation.json` | Operations Manager automation |
| `create-ops-manager-trigger.json` | API endpoint trigger |
| `create-ops-manager-trigger-manual.json` | Manual/form trigger (legacyWrapper: false) |
| `create-ops-manager-trigger-schedule.json` | Scheduled trigger (repeat object, not cron) |
| `create-lcm-resource-model.json` | LCM resource model with lifecycle actions |
| `create-integration.json` | Virtual integration (adapter instance) |
| `create-golden-config-tree.json` | Golden config tree |
| `create-golden-config-node.json` | Child node |
| `create-compliance-plan.json` | Compliance plan |
| `create-flowagent-project-bundle.json` | FlowAI agent project bundle (project + agent + tools + decorator) — import via `/agent-project-service/project-bundles/import` |
| `create-flowagent-decorator.json` | FlowAI tool decorator body — narrows a tool's `inputSchema` for the LLM |

**`helpers/update/`** — PUT/PATCH bodies for updating assets

| File | Purpose |
|------|---------|
| `update-command-template.json` | Update command template (full replacement) |
| `update-json-form.json` | Update a JSON form — wrapped in `options` key (full replacement) |
| `update-node-config.json` | Node template with full syntax |
| `update-project-members.json` | Update project membership — include all members (PATCH = full replacement) |

**`helpers/operations/`** — Add, run, and other operation bodies

| File | Purpose |
|------|---------|
| `add-components-to-project.json` | Add assets to an existing project |
| `add-devices-to-node.json` | Assign devices to a golden config node |
| `run-compliance-plan.json` | Run a compliance plan |
| `run-compliance.json` | Run compliance directly against a tree/node |

**`helpers/assets/`** — Importable sample projects. Use these as design references and borrow components directly rather than building from scratch.

Import via `POST /automation-studio/projects/import` with body `{"project": <file contents>}`.
After import, PATCH membership immediately (see Rule 11a).

**FlowAI agent samples** — different domain, different import path (not Automation Studio):

| File | What's Inside |
|------|--------------|
| `flowagent-sample-agent-project.json` | Real FlowAI project bundle exported from a live platform: 3 agents, including a multi-tool agent (device command → decorated ServiceNow tool → WorkCenter approval step). Import via `POST /agent-project-service/project-bundles/import` with `{"bundle": <file contents>, "providerResolutions": {...}}` — see the `flowagent` skill. |

**JSON Form samples** — different domain, different import path (`POST /json-forms/forms` directly, not Automation Studio project import):

| File | What's Inside |
|------|--------------|
| `json-form-example-static-enum.json` | Real Cisco IOS "Port Turn Up" form export: 8 fields incl. a static-enum dropdown, number `updown` widgets, `ipv4` format validation. No REST binding. |
| `json-form-example-rest-bound.json` | Real Cisco IOS "Compliance" form export: one REST-bound dropdown pulling tree names live from `GET /configuration_manager/configs`, plus one plain text field. |

Both extracted from real, working `jsonForm`-type components inside `vendor-cisco-ios.json` — see the `itential-json-forms` skill for the full form-structure reference.

**Itential Platform — core utilities**

| File | What's Inside |
|------|--------------|
| `itential-platform-configuration-management.json` | 6 workflows (Command Template Runner, Golden Config, Backup Config, Push Config, Diff), 2 templates, 6 transformations — *requires IAG* |
| `itential-platform-data-manipulation.json` | 21 transformations — Parse Number, Chunk Array, Get Value From JSON Pointer, Group Records, Filter Array, Split String, Remove Duplicates, Allocate Numbers, Convert CSV to JSON, and more |
| `itential-platform-email.json` | 1 workflow (Send Email SMTP), 2 transformations — *requires Email Adapter* |
| `itential-platform-regex-operations.json` | 4 transformations — Test Match, Find Match, Replace, Extract |

**Vendor integrations — design and wiring examples**

*Software upgrade patterns:*

| File | What's Inside |
|------|--------------|
| `vendor-cisco-ios.json` | IOS Upgrade, Port Turn Up, Run Compliance, NetBox Inventory sync — 5 workflows, 6 MOP command templates, 3 JSON forms |
| `vendor-juniper-junos.json` | JUNOS Upgrade, Port Turn Up, Run Compliance, NetBox Inventory sync — 5 workflows, 6 MOP command templates, 1 template, 2 JSON forms |
| `vendor-arista-eos.json` | Software Upgrade, Port Turn Up, Create VLAN, Push Config, File Transfer — 7 workflows, 9 MOP command templates, 6 transformations |

*DNS and IPAM:*

| File | What's Inside |
|------|--------------|
| `vendor-infoblox-nios-ddi.json` | 20 workflows — full CRUD for Networks, Network Containers, DNS A/CNAME/PTR/NS/Fixed Address records, Assign Next IP |
| `vendor-netbox.json` | 6 workflows (Create/Delete Prefix, Reserve/Delete IP, Assign Next IP, Onboard Device), 9 transformations, 1 JSON form |

*ITSM integration:*

| File | What's Inside |
|------|--------------|
| `vendor-servicenow.json` | 9 workflows (Create/Update/Close Incidents, Change Requests, RITMs, Get Catalog Inputs), 6 transformations |

**`helpers/assets/lcm/`** — LCM resource model exports + their backing project (exported from live platform)

The `lcm-*.json` files are resource model exports (import via `POST /lifecycle-manager/resources/import`).
The project file contains the actual LCM action workflows — read it to understand how LCM workflows are structured.

| File | What's Inside |
|------|--------------|
| `lcm-vxlan-fabric-management.json` | Resource model: 5 actions (Create Network, Re-Provision, Delete, Force Delete, Decommission) — 4 wired |
| `lcm-vxlan-fabric-services-project.json` | **Backing project**: 6 LCM action workflows, 13 transformations, 3 JSON forms, 2 templates, 1 MOP template — the real workflow structure to learn from |
| `lcm-fan-device-lifecycle-management.json` | Resource model: 10 actions (Device Onboarding, SW Compliance, CVE Scan, Upgrade, Decommission, etc.) — 9/10 wired |
| `lcm-port-turn-up.json` | Resource model: 6 actions (Create, Delete, Service Verification, Update Service Policy) — 4/6 wired |
| `lcm-ip-blocking-service.json` | Resource model: 4 actions (Create, Update, Delete, Retry) — fully wired |
| `lcm-interface-service-provisioning.json` | Resource model: 3 actions (Create, Modify, Delete) — fully wired |

**Key LCM rule:** every action workflow **must** declare and output an `instance` variable — this is what LCM uses to track resource state between actions. Read the VXLAN project workflows to see the exact pattern.

**`helpers/assets/openapi-specs/`** — OpenAPI spec examples for use with the OpenAPI adapter

| File | Purpose |
|------|---------|
| `whoami-basic-auth.json` | WhoAmI endpoint spec with Basic Auth |
| `whoami-client-creds.json` | WhoAmI endpoint spec with Client Credentials |

### Assets Library — when a vendor or pattern isn't here

The full asset library lives at **https://github.com/itential/assets** (branch: `devel`). Structure: `<Vendor>/<Product>/Projects/<name>.project.json`.

**When to check the repo:**
- The use case involves a vendor not covered by the files above (AWS, Arista, Juniper, F5, Palo Alto, Alkira, Kentik, etc.)
- You need a workflow pattern that isn't in the local helpers
- The customer asks about supported integrations

**How to pull a project from the repo:**
```bash
# List available projects for a vendor
gh api repos/itential/assets/contents/<Vendor>/<Product>/Projects --jq '.[].name'

# Download it into helpers/assets/
curl -sL "https://raw.githubusercontent.com/itential/assets/devel/<Vendor>/<Product>/Projects/<encoded-name>.project.json" \
  -o "helpers/assets/<local-name>.json"
```

**Full vendor index (has Projects/):** Alkira, Apache/Kafka, Arista/EOS, Atlassian/Jira, AWS/EC2, Cisco/ASA, Cisco/IOS, Cisco/Meraki, Cisco/NSO, Cisco/NX-OS, F5/BIG-IP, F5/BIG-IQ, GitHub, GitLab, IP Fabric, Infoblox/NIOS DDI, Juniper/JUNOS, Kentik, Microsoft/Teams, NetBox, Palo Alto/Panorama, ServiceNow, Versa/Director

**`helpers/iag/`** — Automation Gateway service files

| File | Purpose |
|------|---------|
| `example-python-service.yaml` | Python script service |
| `example-ansible-service.yaml` | Ansible playbook service |
| `example-opentofu-service.yaml` | OpenTofu plan service |
| `example-multi-service-chain.yaml` | Multi-service orchestration |
| `service-file-schema.md` | Full YAML schema reference |

````

============================================================
FILE: CLA.md
DIRECTORY: ./
FILENAME: CLA.md
============================================================
SHA256: 705be49ba63921ed0b73061977d1f362a675e223087475be857eede5cacf7681

````markdown
# Contributor License Agreement

Thank you for your interest in contributing to the builder-skills project (the "Project").

## Individual Contributor License Agreement

By signing this Contributor License Agreement ("CLA"), you accept and agree to the following terms and conditions for your present and future contributions submitted to Itential, Inc. ("Itential"). Except for the license granted herein to Itential and recipients of software distributed by Itential, you reserve all right, title, and interest in and to your contributions.

### 1. Definitions

**"You"** (or **"Your"**) shall mean the copyright owner or legal entity authorized by the copyright owner that is making this Agreement with Itential.

**"Contribution"** shall mean any original work of authorship, including any modifications or additions to an existing work, that is intentionally submitted by You to Itential for inclusion in, or documentation of, any of the products owned or managed by Itential (the "Work"). For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to Itential or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, Itential for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by You as "Not a Contribution."

### 2. Grant of Copyright License

Subject to the terms and conditions of this Agreement, You hereby grant to Itential and to recipients of software distributed by Itential a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Work, and to permit persons to whom the Work is furnished to do so.

### 3. Grant of Patent License

Subject to the terms and conditions of this Agreement, You hereby grant to Itential and to recipients of software distributed by Itential a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by You that are necessarily infringed by Your Contribution(s) alone or by combination of Your Contribution(s) with the Work to which such Contribution(s) was submitted. If any entity institutes patent litigation against You or any other entity (including a cross-claim or counterclaim in a lawsuit) alleging that your Contribution, or the Work to which you have contributed, constitutes direct or contributory patent infringement, then any patent licenses granted to that entity under this Agreement for that Contribution or Work shall terminate as of the date such litigation is filed.

### 4. Representations

You represent that:

a) You are legally entitled to grant the above license. If your employer(s) has rights to intellectual property that you create that includes your Contributions, you represent that you have received permission to make Contributions on behalf of that employer, that your employer has waived such rights for your Contributions to Itential, or that your employer has executed a separate Corporate CLA with Itential.

b) Each of Your Contributions is Your original creation (see section 7 for submissions on behalf of others).

c) Your Contribution submissions include complete details of any third-party license or other restriction (including, but not limited to, related patents and trademarks) of which you are personally aware and which are associated with any part of Your Contributions.

### 5. Support

You are not expected to provide support for Your Contributions, except to the extent You desire to provide support. You may provide support for free, for a fee, or not at all. Unless required by applicable law or agreed to in writing, You provide Your Contributions on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.

### 6. Third Party Contributions

Should You wish to submit work that is not Your original creation, You may submit it to Itential separately from any Contribution, identifying the complete details of its source and of any license or other restriction (including, but not limited to, related patents, trademarks, and license agreements) of which you are personally aware, and conspicuously marking the work as "Submitted on behalf of a third-party: [named here]".

### 7. Notification of Changes

You agree to notify Itential of any facts or circumstances of which you become aware that would make these representations inaccurate in any respect.

## How to Sign

To sign this CLA, please comment on your pull request with the following statement:

```
I have read the CLA Document and I hereby sign the CLA
```

## Contact Information

If you have questions about this CLA, please contact us at:
- Email: opensource@itential.com
- Website: https://itential.com

---

**Project:** builder-skills  
**Organization:** Itential, Inc.  
**Date:** 2026-03-25
**License:** GPL-3.0-or-later

````

============================================================
FILE: CLAUDE.md
DIRECTORY: ./
FILENAME: CLAUDE.md
============================================================
SHA256: 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49

````markdown
@AGENTS.md

````

============================================================
FILE: CODEOWNERS
DIRECTORY: ./
FILENAME: CODEOWNERS
============================================================
SHA256: 6ad7f4b749277f474d0d2b41e3fffc5e3afdc5b748be042e3ccbcd041917da38

````text
# Global owners for the whole repository
* @itential/builder-skills-maintainers
* @itential/community-managers

````

============================================================
FILE: CODE_OF_CONDUCT.md
DIRECTORY: ./
FILENAME: CODE_OF_CONDUCT.md
============================================================
SHA256: b1bd98126e5b447689e0eed8188c36de1f1572a580f2ab224237b24cc2a2b3d2

````markdown
# Open Source Code of Conduct

## Purpose

This Code of Conduct sets expectations for behavior in our open source community. It ensures a respectful, safe, and inclusive environment for contributors, maintainers, users, and newcomers—regardless of background, skill level, or personal identity.

Open source thrives when everyone can contribute without harassment, discrimination, or toxicity. If you're here to collaborate, you're expected to follow this.

## Expected Behavior

We expect all contributors to:

- **Be respectful**: Value different perspectives. Disagree without personal attacks.
- **Be constructive**: Critique code and ideas, not people. If something’s broken, propose a fix.
- **Be inclusive**: Welcome beginners, mentor others, and use inclusive language.
- **Take responsibility**: Own your mistakes, learn from feedback, and help improve the project.
- **Communicate clearly**: Write good issues, PRs, and commit messages. Default to transparency.

## Unacceptable Behavior

These are **not tolerated**:

- Hate speech, slurs, or discriminatory jokes.
- Harassment, intimidation, or sustained disruption.
- Doxxing or sharing private information without consent.
- Trolling, flame wars, or intentionally derailing conversations.
- “Gatekeeping” or belittling others based on experience, tools, or tech stack.

## Enforcement

Violations will be handled promptly and decisively:

- Minor incidents may result in a warning.
- Repeated or severe behavior can lead to bans from the project (GitHub issues, PRs, Slack/Discord, etc.).
- Reports will be reviewed by the maintainers or a designated moderation team.

## Reporting

If you experience or witness a violation, **speak up**:

- Email: opensource@itential.com
- Or DM a maintainer in private on our official chat

All reports are confidential. Retaliation against reporters **will not be tolerated**.

## Scope

This Code of Conduct applies in all project spaces, including:

- GitHub issues and PRs
- Community forums, chats, and meetings
- Social media when representing the project

## Attribution

This code is based on the [Contributor Covenant](https://www.contributor-covenant.org), with pragmatic additions tailored for modern open source development.

````

============================================================
FILE: CONTRIBUTING.md
DIRECTORY: ./
FILENAME: CONTRIBUTING.md
============================================================
SHA256: 0059e48dc2a04539e74d18068a8a56e6199097dc22a5372d5958b1a975e0d29f

````markdown
# Contributing to builder-skills

Thank you for your interest in contributing to the builder-skills project! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Contributor License Agreement](#contributor-license-agreement)
- [Development Setup](#development-setup)
- [Contributing Process](#contributing-process)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Pull Request Labels](#pull-request-labels)
- [Testing](#testing)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Getting Help](#getting-help)

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please report unacceptable behavior to [opensource@itential.com](mailto:opensource@itential.com).

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Set up the development environment**
4. **Create a feature branch** for your changes
5. **Make your changes** and test them
6. **Submit a pull request**

## Contributor License Agreement

**All contributors must sign a Contributor License Agreement (CLA) before their contributions can be merged.** 

The CLA ensures that:
- You have the right to contribute the code
- Itential has the necessary rights to use and distribute your contributions
- The project remains legally compliant

When you submit your first pull request, you will be prompted to sign the CLA. Please complete this process before your contribution can be reviewed.

## Development Setup

<!--
MAINTAINER: Replace the Prerequisites and Setup Instructions sections below
with project-specific requirements and commands for your tech stack.
-->

### Prerequisites

<!-- List your project's prerequisites here. Examples:
- Python 3.10+ with uv package manager
- Node.js 18+ with npm/yarn
- Go 1.21+
- Rust 1.70+ with cargo
-->

- Git

### Setup Instructions

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/builder-skills.git
   cd builder-skills
   ```

2. **Add the upstream remote:**
   ```bash
   git remote add upstream https://github.com/itential/builder-skills.git
   ```

3. **Set up the development environment:**
   ```bash
   # Add your setup commands here
   # Examples:
   # - Python: uv sync --all-extras --dev
   # - Node.js: npm install
   # - Go: go mod download
   # - Rust: cargo build
   ```

4. **Verify the setup:**
   ```bash
   # Add your verification commands here
   # Examples:
   # - Python: make test && make lint
   # - Node.js: npm test && npm run lint
   # - Go: go test ./... && golangci-lint run
   # - Rust: cargo test && cargo clippy
   ```

## Contributing Process

### Fork and Pull Model

This project uses a fork and pull request model for contributions:

1. **Fork the repository** to your GitHub account
2. **Create a topic branch** from `main`:
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** in logical, atomic commits — every commit message must follow the [Commit Message Format](#commit-message-format) below; CI will reject the PR otherwise
4. **Test your changes** thoroughly
5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a pull request** against the `main` branch

### Branch Naming Conventions

Branch names are validated by CI against this regex:

```
^(feature|fix|refactor|docs|chore)/[a-z][a-z0-9-]*$
```

Format: `<type>/<description>` where:

| Field | Rule |
|---|---|
| Type | One of `feature`, `fix`, `refactor`, `docs`, `chore` |
| Description | Lowercase letters, numbers, and hyphens only; must start with a letter |

Type meanings:
- `feature/` — new features
- `fix/` — bug fixes
- `refactor/` — code restructuring without changing behavior
- `chore/` — maintenance tasks (dependencies, tooling, build)
- `docs/` — documentation updates

Examples:
- `feature/add-authentication-support`
- `fix/handle-connection-timeout`
- `refactor/extract-token-helper`
- `chore/update-dependencies`
- `docs/improve-api-examples`

### Commit Message Format

Every commit on a PR is validated by CI against the [Conventional Commits](https://www.conventionalcommits.org/) regex:

```
^(feat|fix|docs|style|refactor|test|chore|perf)(\(.+\))?: .{1,72}
```

Format: `<type>[(scope)]: <description>` where:

| Field | Rule |
|---|---|
| Type | One of `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf` |
| Scope | *(Optional)* parenthesized, e.g. `(builder-agent)` |
| Description | 1–72 characters |

> **Note** — the commit type list is **different from the branch type list**. Branches use `feature/` (full word); commits use `feat:` (Conventional Commits short form). Branches don't have `style`, `test`, or `perf`.

Type meanings (commit-side):
- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation only
- `style` — formatting, whitespace, missing semicolons (no code logic change)
- `refactor` — code restructuring without behavior change
- `test` — adding or fixing tests
- `chore` — build process, tooling, dependencies
- `perf` — performance improvements

**Merge commits are not allowed** on PR branches — the CI rejects them. Use squash or rebase to integrate updates from `main`.

**`git revert`'s default message never conforms** — it produces `Revert "<original message>"`, and `Revert` isn't a valid type. Reword it before pushing:

```bash
git revert --no-edit <sha>
git commit --amend -m "fix: revert <what and why>"
```

If reverting multiple commits, squash them into a single properly-typed commit instead of leaving several auto-generated `Revert "..."` messages:

```bash
git reset --soft <sha-before-the-commits-being-reverted>
git commit -m "fix: revert <what and why>"
```

Examples:
- `feat(auth): add JWT token validation`
- `fix: handle empty response from upstream`
- `docs(contributing): document commit and branch CI rules`
- `chore: bump dependency versions`

## Pull Request Guidelines

### Before Submitting

- [ ] Ensure your branch is up to date with `main`
- [ ] Run the full test suite: `make test`
- [ ] Run code quality checks: `make lint`
- [ ] Add tests for new functionality
- [ ] Update documentation if needed
- [ ] Sign the Contributor License Agreement (CLA)

### Pull Request Description

Your pull request should include:

1. **Clear title** describing the change
2. **Detailed description** explaining:
   - What the change does
   - Why the change is needed
   - How it was tested
3. **References to related issues** (if applicable)
4. **Breaking changes** (if any)

### Example Pull Request Template

```markdown
## Summary
Brief description of what this PR does.

## Changes
- List of specific changes made
- Another change

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Related Issues
Closes #123
```

## Pull Request Labels

This project uses Release Drafter to automatically generate release notes. Please apply appropriate labels to your pull requests:

### Change Type Labels
- `feature`, `enhancement` - New features and enhancements
- `fix`, `bug`, `bugfix` - Bug fixes and corrections
- `chore`, `dependencies`, `refactor` - Maintenance, dependency updates, and refactoring
- `documentation`, `docs` - Documentation changes
- `security` - Security fixes and improvements
- `breaking`, `breaking-change` - Breaking changes that require major version bump

### Version Impact Labels
- `major` - Breaking changes (increments major version)
- `minor` - New features (increments minor version)
- `patch` - Bug fixes and maintenance (increments patch version)

### Auto-Labeling
The Release Drafter will automatically apply labels based on:
- **Branch names**: `feature/`, `fix/`, `chore/` prefixes
- **File changes**: Documentation files, dependency files
- **PR titles**: Keywords like "feat", "fix", "chore"

### Special Labels
- `skip-changelog` - Exclude from release notes
- `duplicate`, `question`, `invalid`, `wontfix` - Issues that don't represent changes

## Testing

<!--
MAINTAINER: Replace this section with project-specific testing instructions.
Examples for common tech stacks are provided as comments.
-->

### Running Tests

```bash
# Add your test commands here
# Examples:
# - Python: make test, pytest, uv run pytest
# - JavaScript: npm test, yarn test
# - Go: go test ./..., make test
# - Rust: cargo test
```

### Test Coverage

```bash
# Add your coverage commands here
# Examples:
# - Python: make coverage, pytest --cov
# - JavaScript: npm run coverage, nyc npm test
# - Go: go test -cover ./...
# - Rust: cargo tarpaulin
```

### Writing Tests

- Place tests in the appropriate directory for your language/framework
- Use descriptive test names that explain the expected behavior
- Include both positive and negative test cases
- Mock external dependencies appropriately
- Aim for meaningful coverage of critical paths

<!--
MAINTAINER: Add project-specific test structure and conventions here.
Example: "Place tests in `tests/` directory mirroring `src/` structure"
-->

## Code Style

<!--
MAINTAINER: Replace this section with project-specific code style guidelines.
Examples for common tech stacks are provided as comments.
-->

### Code Quality Commands

```bash
# Add your linting/formatting commands here
# Examples:
# - Python: make lint, ruff check ., black --check .
# - JavaScript: npm run lint, eslint ., prettier --check .
# - Go: golangci-lint run, go fmt ./...
# - Rust: cargo clippy, cargo fmt --check
```

### Style Guidelines

<!--
MAINTAINER: Add your project's style guidelines here. Examples:

Python:
- Follow PEP 8 conventions
- Use type hints for all function parameters and return values
- Keep line length to 88 characters (Black default)

JavaScript/TypeScript:
- Follow ESLint recommended rules
- Use TypeScript strict mode
- Prefer const over let, avoid var

Go:
- Follow Effective Go guidelines
- Use gofmt for formatting
- Keep functions focused and small

Rust:
- Follow Rust API Guidelines
- Use clippy lints
- Prefer Result over panics
-->

- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Write self-documenting code where possible

### Documentation Standards

- Document public APIs and exported functions
- Include usage examples for complex functionality
- Keep documentation up-to-date with code changes

<!--
MAINTAINER: Add project-specific documentation conventions here.
Example: "Use Google-style docstrings with Args, Returns, and Raises sections"
-->

## Documentation

### Types of Documentation

1. **Code documentation** - Docstrings and inline comments
2. **API documentation** - Tool descriptions and examples
3. **User documentation** - README and usage guides
4. **Developer documentation** - This CONTRIBUTING.md and AGENTS.md

### Documentation Updates

- Update docstrings when changing function signatures
- Add examples for new tools and features
- Update README.md for user-facing changes
- Maintain the AGENTS.md file for development guidelines

## Getting Help

### Resources

- **Documentation**: Check the README.md and AGENTS.md files
- **Issues**: Search existing issues for similar problems
- **Discussions**: Use GitHub Discussions for questions
- **Maintainer**: [@wcollins](https://github.com/wcollins)

### Reporting Issues

When reporting issues, please include:

1. **Clear description** of the problem
2. **Steps to reproduce** the issue
3. **Expected vs actual behavior**
4. **Environment information** (runtime version, OS, etc.)
5. **Error messages** and stack traces (if applicable)

### Asking Questions

- Use GitHub Discussions for general questions
- Search existing discussions and issues first
- Provide context and specific details
- Be patient and respectful

## Recognition

Contributors who have their pull requests merged will be:
- Listed in the project's contributors
- Mentioned in release notes (when appropriate)
- Recognized in the project documentation

Thank you for contributing to builder-skills!

---

For questions about contributing, please contact [opensource@itential.com](mailto:opensource@itential.com).

````
