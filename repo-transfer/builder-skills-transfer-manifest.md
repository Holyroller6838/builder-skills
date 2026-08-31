# Builder Skills Repository Transfer — Manifest

## Repository Manifest

- **Total Git-tracked files:** 223
- **Generated:** 2026-08-31 21:28:30 UTC
- **Git branch:** main
- **Git commit SHA:** 982d97c1573ca7ea892b39acced9b0d15955c4a9
- **Repository root:** /Users/ericbaker/Downloads/projects/builder-skills
- **Transfer documents:** 11 part file(s) (builder-skills-transfer-001.md .. -011.md)
- **Binary files (require separate transfer):** 0
- **Files with redacted secret values:** 3

### Intentionally Excluded Files

No tracked files were excluded from this transfer — all 223 Git-tracked files are represented across the part documents. The following file *classes* are excluded by design because they are untracked/generated and therefore have no Git-tracked path to begin with: `.git/`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, `.ruff_cache/`, `.venv/`, `node_modules/`, `.DS_Store`, IDE temp files, build artifacts, and untracked local `.env`/`.auth.json` credential files (e.g. `eos-ab-upgrade/.env`, `eos-readiness-engine/.venv/`, `docs-review/`, `software-upgrade/` — none of these are Git-tracked as of this commit).

### Files With Redacted Secret Values

These 3 files are template/example credential files (`environments/*.env`). Their current committed values are placeholders or well-known local-dev defaults (e.g. `your-client-secret`, `admin`/`admin`), not real secrets — but per the redaction instruction, the value portion of every `CLIENT_ID=`/`CLIENT_SECRET=`/`USERNAME=`/`PASSWORD=`/`TOKEN=` line was replaced with `[REDACTED — SECRET MUST BE RECREATED IN DESTINATION ENVIRONMENT]` in the transferred content below. File structure and comments are preserved exactly.

- `environments/cloud-lab.env`
- `environments/local-dev.env`
- `environments/staging.env`

### Binary Files Requiring Separate Transfer

None. All 223 Git-tracked files are text.

## Directory Tree

```
.
├── .claude/
│   └── skills/
│       ├── builder-agent/
│       │   └── SKILL.md
│       ├── documentation/
│       │   └── SKILL.md
│       ├── explore/
│       │   └── SKILL.md
│       ├── flowagent/
│       │   └── SKILL.md
│       ├── flowagent-to-spec/
│       │   └── SKILL.md
│       ├── iag/
│       │   └── SKILL.md
│       ├── itential-devices/
│       │   └── SKILL.md
│       ├── itential-golden-config/
│       │   └── SKILL.md
│       ├── itential-inventory/
│       │   └── SKILL.md
│       ├── itential-json-forms/
│       │   └── SKILL.md
│       ├── itential-lcm/
│       │   └── SKILL.md
│       ├── itential-mop/
│       │   └── SKILL.md
│       ├── project-to-spec/
│       │   └── SKILL.md
│       ├── qa-agent/
│       │   └── SKILL.md
│       ├── solution-arch-agent/
│       │   ├── SKILL.md
│       │   └── pull-platform-data.py
│       └── spec-agent/
│           └── SKILL.md
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── workflows/
│   │   └── pr-compliance.yml
│   └── pull_request_template.md
├── docs/
│   ├── builder-flow.md
│   ├── developer-flow.md
│   ├── quickstart.md
│   └── troubleshooting.md
├── environments/
│   ├── cloud-lab.env
│   ├── local-dev.env
│   └── staging.env
├── eos-ab-upgrade/
│   ├── .github/
│   │   └── workflows/
│   │       └── validate-eos-project.yml
│   ├── docs/
│   │   ├── acceptance-test-plan.md
│   │   ├── architecture.md
│   │   ├── device-broker-map.md
│   │   ├── itential-task-map.md
│   │   ├── python-action-map.md
│   │   └── rollback-plan.md
│   ├── iag/
│   │   ├── eos-precheck-service.yaml
│   │   └── eos-readiness-service.yaml
│   ├── services/
│   │   └── eos_upgrade/
│   │       ├── __init__.py
│   │       ├── cli.py
│   │       ├── device_broker.py
│   │       ├── iag_entrypoint.py
│   │       ├── maintenance.py
│   │       ├── models.py
│   │       ├── precheck.py
│   │       ├── readiness.py
│   │       ├── readiness_entrypoint.py
│   │       ├── reporting.py
│   │       ├── upgrade.py
│   │       └── validation.py
│   ├── specs/
│   │   ├── spec-arista-eos-ab-upgrade.md
│   │   └── workflow-task-map.md
│   ├── tests/
│   │   ├── fixtures/
│   │   │   ├── fake_broker.py
│   │   │   └── readiness_payloads.py
│   │   ├── test_device_broker.py
│   │   ├── test_maintenance.py
│   │   ├── test_precheck.py
│   │   ├── test_readiness.py
│   │   ├── test_reporting.py
│   │   └── test_validation.py
│   ├── workflows/
│   │   ├── eos-postcheck.json
│   │   ├── eos-precheck.json
│   │   ├── eos-upgrade-orchestrator.json
│   │   ├── eos-upgrade-readiness.json
│   │   └── eos-upgrade-single-device.json
│   ├── .gitignore
│   ├── MVP1-DEPLOYMENT-CHECKLIST.md
│   ├── MVP1-INTEGRATION.md
│   ├── README.md
│   ├── integration-contracts.md
│   └── pyproject.toml
├── eos-readiness-engine/
│   ├── eos_readiness/
│   │   ├── checks/
│   │   │   ├── __init__.py
│   │   │   ├── bgp.py
│   │   │   ├── collection.py
│   │   │   ├── interfaces.py
│   │   │   ├── mlag.py
│   │   │   └── version.py
│   │   ├── profiles/
│   │   │   ├── __init__.py
│   │   │   └── registry.py
│   │   ├── raw/
│   │   │   ├── __init__.py
│   │   │   ├── collectors.py
│   │   │   ├── normalize.py
│   │   │   └── parsers.py
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── errors.py
│   │   ├── iag_entrypoint.py
│   │   ├── models.py
│   │   └── status.py
│   ├── iag/
│   │   └── eos-readiness-service.yaml
│   ├── tests/
│   │   ├── fixtures/
│   │   │   └── raw/
│   │   │       ├── USILD001LAB01A__show_version.json
│   │   │       └── command_results_pair_sample.json
│   │   ├── factories.py
│   │   ├── test_checks_bgp.py
│   │   ├── test_checks_collection.py
│   │   ├── test_checks_interfaces.py
│   │   ├── test_checks_mlag.py
│   │   ├── test_checks_version.py
│   │   ├── test_collectors.py
│   │   ├── test_engine_decision_contract.py
│   │   ├── test_evaluate_pair.py
│   │   ├── test_normalize.py
│   │   ├── test_parse_show_version.py
│   │   ├── test_profiles.py
│   │   └── test_status.py
│   ├── workflows/
│   │   └── eos-ab-readiness.json
│   ├── .gitignore
│   ├── README.md
│   └── pyproject.toml
├── evals/
│   ├── e2e/
│   │   ├── e2e-results.json
│   │   ├── run-e2e-tests.sh
│   │   ├── test1-utility-chain.json
│   │   ├── test2-child-workflow.json
│   │   ├── test2-parent-loop.json
│   │   └── test3-adapter-servicenow.json
│   ├── trigger-evals/
│   │   ├── README.md
│   │   ├── builder-agent-results.json
│   │   ├── builder-agent.json
│   │   ├── documentation-results.json
│   │   ├── documentation.json
│   │   ├── explore-results.json
│   │   ├── explore.json
│   │   ├── solution-arch-agent-results.json
│   │   ├── solution-arch-agent.json
│   │   ├── spec-agent-results.json
│   │   └── spec-agent.json
│   ├── COVERAGE-REPORT.md
│   └── evals.json
├── helpers/
│   ├── assets/
│   │   ├── lcm/
│   │   │   ├── lcm-fan-device-lifecycle-management.json
│   │   │   ├── lcm-interface-service-provisioning.json
│   │   │   ├── lcm-ip-blocking-service.json
│   │   │   ├── lcm-port-turn-up.json
│   │   │   ├── lcm-vxlan-fabric-management.json
│   │   │   └── lcm-vxlan-fabric-services-project.json
│   │   ├── openapi-specs/
│   │   │   ├── whoami-basic-auth.json
│   │   │   └── whoami-client-creds.json
│   │   ├── flowagent-sample-agent-project.json
│   │   ├── itential-platform-configuration-management.json
│   │   ├── itential-platform-data-manipulation.json
│   │   ├── itential-platform-email.json
│   │   ├── itential-platform-regex-operations.json
│   │   ├── json-form-example-rest-bound.json
│   │   ├── json-form-example-static-enum.json
│   │   ├── vendor-arista-eos.json
│   │   ├── vendor-cisco-ios.json
│   │   ├── vendor-infoblox-nios-ddi.json
│   │   ├── vendor-juniper-junos.json
│   │   ├── vendor-netbox.json
│   │   └── vendor-servicenow.json
│   ├── create/
│   │   ├── create-command-template.json
│   │   ├── create-compliance-plan.json
│   │   ├── create-flowagent-decorator.json
│   │   ├── create-flowagent-project-bundle.json
│   │   ├── create-golden-config-node.json
│   │   ├── create-golden-config-tree.json
│   │   ├── create-integration.json
│   │   ├── create-json-form-rest-bound.json
│   │   ├── create-json-form.json
│   │   ├── create-lcm-resource-model.json
│   │   ├── create-ops-manager-automation.json
│   │   ├── create-ops-manager-trigger-manual.json
│   │   ├── create-ops-manager-trigger-schedule.json
│   │   ├── create-ops-manager-trigger.json
│   │   ├── create-project.json
│   │   ├── create-template-jinja2.json
│   │   ├── create-template-textfsm.json
│   │   ├── create-workflow.json
│   │   └── import-project.json
│   ├── iag/
│   │   ├── example-ansible-service.yaml
│   │   ├── example-multi-service-chain.yaml
│   │   ├── example-opentofu-service.yaml
│   │   ├── example-python-service.yaml
│   │   └── service-file-schema.md
│   ├── operations/
│   │   ├── add-components-to-project.json
│   │   ├── add-devices-to-node.json
│   │   ├── run-compliance-plan.json
│   │   └── run-compliance.json
│   ├── update/
│   │   ├── update-command-template.json
│   │   ├── update-json-form.json
│   │   ├── update-node-config.json
│   │   └── update-project-members.json
│   ├── documentation-output-templates.md
│   └── use-case-memory.md
├── scripts/
│   ├── platform_pull.py
│   └── use_case_init.py
├── spec-files/
│   ├── demo/
│   │   ├── device-health-agent.md
│   │   ├── linux-diagnostics-agent.md
│   │   ├── spec-dns-a-record-infoblox-simple.md
│   │   └── spec-dns-a-record-provisioning.md
│   ├── spec-arista-eos-ab-upgrade.md
│   ├── spec-aws-webserver-deploy.md
│   ├── spec-bgp-peer-provisioning.md
│   ├── spec-change-management.md
│   ├── spec-circuit-provisioning.md
│   ├── spec-cloud-security-groups.md
│   ├── spec-config-backup-compliance.md
│   ├── spec-config-drift-remediation.md
│   ├── spec-device-decommissioning.md
│   ├── spec-device-onboarding.md
│   ├── spec-dns-record-management.md
│   ├── spec-firewall-rule-lifecycle.md
│   ├── spec-incident-auto-remediation.md
│   ├── spec-ipam-lifecycle.md
│   ├── spec-load-balancer-vip.md
│   ├── spec-network-compliance-audit.md
│   ├── spec-network-health-check.md
│   ├── spec-port-turn-up.md
│   ├── spec-software-upgrade.md
│   ├── spec-ssl-certificate-lifecycle.md
│   ├── spec-vlan-provisioning.md
│   ├── spec-vpn-tunnel-provisioning.md
│   └── spec-wan-bandwidth-modification.md
├── .gitignore
├── AGENTS.md
├── CLA.md
├── CLAUDE.md
├── CODEOWNERS
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

## File Index — Part Assignment and Checksums

| # | File | Part | SHA-256 | Size (bytes) | Redacted |
|---|------|------|---------|---------------|----------|
| 1 | `.claude-plugin/marketplace.json` | 001 | `1bba898b36cc04b2d58112a1b7d839f67435993f591064a57b5ca84e69d8df22` | 1121 |  |
| 2 | `.claude-plugin/plugin.json` | 001 | `d0bab506a58971d7ce9b645aed610a238e0e67e85fa69d73a4577a345992e97e` | 636 |  |
| 3 | `.claude/skills/builder-agent/SKILL.md` | 001 | `8c76a60f6cff60386035916f3f806b82e43e3d72c7cef56a7e41713d2ce04eb9` | 119777 |  |
| 4 | `.claude/skills/documentation/SKILL.md` | 001 | `373bac9e19991e9d53fdeda7c8b6c849c21d7dcea47f80b51e03a15f5540a082` | 22271 |  |
| 5 | `.claude/skills/explore/SKILL.md` | 001 | `b28b89c08c831a9b4a29408d79809d81c3acfa262b34cdc350c2153dfd4acc61` | 7029 |  |
| 6 | `.claude/skills/flowagent-to-spec/SKILL.md` | 001 | `78739912a95b9aebef994ecbf20676f03432b0b1bbc5c8c5db09875a83964e64` | 13546 |  |
| 7 | `.claude/skills/flowagent/SKILL.md` | 001 | `e35fb862a6cd2118a724f5e665c59bfe1360fad43f85e5fa31444f9736e866f6` | 60973 |  |
| 8 | `.claude/skills/iag/SKILL.md` | 001 | `65d3e8b6dc3d11c2699824e3a12b71e2cb34e58e2338dd9d0a1eefb1957a02a1` | 33588 |  |
| 9 | `.claude/skills/itential-devices/SKILL.md` | 001 | `fa8d23a1b022835871f887a485837b59e53c717c3793ca1141adc45da6a4e156` | 15620 |  |
| 10 | `.claude/skills/itential-golden-config/SKILL.md` | 001 | `5bf45257b05df267eb09f4da00731bdf7282c32cb25dbabf28f549e64ae41c52` | 32297 |  |
| 11 | `.claude/skills/itential-inventory/SKILL.md` | 001 | `611adf352f7cd4406a1ece4d1ccdf8844319e98add7856731ee1c97a49deee25` | 12228 |  |
| 12 | `.claude/skills/itential-json-forms/SKILL.md` | 001 | `76fe49f256d4e82c93e7d32e8d7c3a9e79971c46b08b4825a0eb9777efa3221b` | 10562 |  |
| 13 | `.claude/skills/itential-lcm/SKILL.md` | 001 | `c00d7cc5b0db0bfce1aa2ba7e5344aab6e1ca9730319086e0cf6e10cf48324ef` | 15013 |  |
| 14 | `.claude/skills/itential-mop/SKILL.md` | 001 | `0292bba2393cc71373eecf28294dee07297b5503fb46bbbb27fe00add59d5b10` | 18460 |  |
| 15 | `.claude/skills/project-to-spec/SKILL.md` | 001 | `e8a03d66c232a5ef53cc4fbf36f1ae368ea752f8e37a46b6b5f62d4a8843fd36` | 11955 |  |
| 16 | `.claude/skills/qa-agent/SKILL.md` | 001 | `091ab13ccf6f45c7fc2ed5280f37e3bfe79dac025f577406227c8b9e0cf13553` | 19274 |  |
| 17 | `.claude/skills/solution-arch-agent/SKILL.md` | 001 | `ccd5b823ac7f81ff7f0d16d7cf7007ed202b6c50f7e20807ecfd72b6d1b3914c` | 19987 |  |
| 18 | `.claude/skills/solution-arch-agent/pull-platform-data.py` | 001 | `78f9d7669efac803aee341120edafa06d52217f185253d151649208e7dbf0919` | 7130 |  |
| 19 | `.claude/skills/spec-agent/SKILL.md` | 001 | `2d820a3afe5b6464f54502a67308c47760e93886c93f04b950e650f217607aa4` | 6739 |  |
| 20 | `.github/ISSUE_TEMPLATE/bug_report.md` | 001 | `81cc3cbf243bb2eb26111994422f03adf9dc614d5cdbbb201d778ba4aee31a40` | 491 |  |
| 21 | `.github/ISSUE_TEMPLATE/feature_request.md` | 001 | `260c4717583d1fe536fb0e7c23a621258e4b39bc9535ff39f6fb35e3063bd4dc` | 364 |  |
| 22 | `.github/pull_request_template.md` | 001 | `d31d77e7636059b3bb3a444e0d042b35a2f3f04120d4b3cba5b2322f258c7277` | 794 |  |
| 23 | `.github/workflows/pr-compliance.yml` | 001 | `a83bd51e8568c10281139638d3f00c0fd835acb7df4e6fe5e6c3c7ad2e05e194` | 2489 |  |
| 24 | `.gitignore` | 001 | `b6b6103aa788739b122b84cc1bf7a5c7f00a6b774c26b5598a3dc9ddb4fb3665` | 2771 |  |
| 25 | `AGENTS.md` | 001 | `70374eab431cc0f59fc61eb9d0393d7f0cb758c96e364564ae28412a3248a28b` | 33952 |  |
| 26 | `CLA.md` | 001 | `705be49ba63921ed0b73061977d1f362a675e223087475be857eede5cacf7681` | 5401 |  |
| 27 | `CLAUDE.md` | 001 | `336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49` | 11 |  |
| 28 | `CODEOWNERS` | 001 | `6ad7f4b749277f474d0d2b41e3fffc5e3afdc5b748be042e3ccbcd041917da38` | 111 |  |
| 29 | `CODE_OF_CONDUCT.md` | 001 | `b1bd98126e5b447689e0eed8188c36de1f1572a580f2ab224237b24cc2a2b3d2` | 2244 |  |
| 30 | `CONTRIBUTING.md` | 001 | `0059e48dc2a04539e74d18068a8a56e6199097dc22a5372d5958b1a975e0d29f` | 12310 |  |
| 31 | `LICENSE` | 002 | `d89bfd34f67eb6ec72bd6e3f1aaaeccaff520a97bdc6fcf6a99315336c91b532` | 35146 |  |
| 32 | `README.md` | 002 | `ca905da00f2e2ff0adc210020b6bbfd9aff2cdb0cd13885656e5ce97bfc88b15` | 11590 |  |
| 33 | `SECURITY.md` | 002 | `f9ca508818d631e68bfedb296d3f3e89452739baa81e611813004987ac2493e5` | 2010 |  |
| 34 | `docs/builder-flow.md` | 002 | `6e882bab5a3975aae233870c2d2a0607e171e7c666c01637c13a50380a2c9567` | 19006 |  |
| 35 | `docs/developer-flow.md` | 002 | `b19b44c379d8a984479c0ffbc73efc2448709c30da1f9b4e2b4630c0052a96ba` | 13612 |  |
| 36 | `docs/quickstart.md` | 002 | `289defe37c23cc0224f19f3badb3654d963507e4b5602e4350df290d21c37e78` | 5578 |  |
| 37 | `docs/troubleshooting.md` | 002 | `d943c4b5d3bdb5ee9a234b81c2d90503cec311547fbb49873cce5cdd69a4eebb` | 1051 |  |
| 38 | `environments/cloud-lab.env` | 002 | `62d148d9413da01ced2d44a226a76530153829cd37f30ffb6759b1052269b0c0` | 437 | YES |
| 39 | `environments/local-dev.env` | 002 | `fd987879e8cce7ab66762dce7cce2fd0f5647599f62a2c47fa6c1f66368d7e52` | 430 | YES |
| 40 | `environments/staging.env` | 002 | `7ad5189207f41a9f4dabfa30bbd8bada19271f659ae9fc904ca73eae9935c91d` | 391 | YES |
| 41 | `eos-ab-upgrade/.github/workflows/validate-eos-project.yml` | 002 | `6dc0126b55851f8bb9980f11e6156e12ab57300110606dc280f34528c71deef8` | 843 |  |
| 42 | `eos-ab-upgrade/.gitignore` | 002 | `c6d1f6ba18525a490e5d8f93b342613720474606aa6dff7f90e5913250e79e07` | 260 |  |
| 43 | `eos-ab-upgrade/MVP1-DEPLOYMENT-CHECKLIST.md` | 002 | `8e6b6af5afd5504ff42318942c6cf2db1fa0d937053b55a71eec6517c67d7f5f` | 6096 |  |
| 44 | `eos-ab-upgrade/MVP1-INTEGRATION.md` | 002 | `637f18076895775297c6eb8881b6f40315173e0fff74d238445120a5fe1ba105` | 17131 |  |
| 45 | `eos-ab-upgrade/README.md` | 002 | `77d255853dc99c8a464e13b7b4f620d763f8dc8d0f3a89fd8a405d1688d2ac08` | 3269 |  |
| 46 | `eos-ab-upgrade/docs/acceptance-test-plan.md` | 002 | `aae07461dbe604048dd5fcc93feba576708813c0aac493e60d56b14a02cea0b3` | 3648 |  |
| 47 | `eos-ab-upgrade/docs/architecture.md` | 002 | `dab8b4456ba3902cce12c899e87cf67a46ca7ab5be34210a8ea65edf583cafaf` | 4259 |  |
| 48 | `eos-ab-upgrade/docs/device-broker-map.md` | 002 | `920619d40a194038662683a9c3f66aba614da988496d74d63f7b2b05f9d9adb0` | 3614 |  |
| 49 | `eos-ab-upgrade/docs/itential-task-map.md` | 002 | `e692d48e9498e44c9c2891a510b2b78ddb267300800c7889709bc9867488923b` | 3737 |  |
| 50 | `eos-ab-upgrade/docs/python-action-map.md` | 002 | `5400d9fd6b414aff540da6b91ee9f105630f353c850942afc05f8b2217270d7c` | 3254 |  |
| 51 | `eos-ab-upgrade/docs/rollback-plan.md` | 002 | `55ecdad0e22f4b7f8b725c31afd0958940c81f908dc1585c2e60b954506474e7` | 2162 |  |
| 52 | `eos-ab-upgrade/iag/eos-precheck-service.yaml` | 002 | `a919757c3cfb67f1ef25a1411e00fb7273cfe921f529d52ff2a4ccf70b228123` | 2466 |  |
| 53 | `eos-ab-upgrade/iag/eos-readiness-service.yaml` | 002 | `479f66ae13445576b64c916bfa32094ae4e4dc5adaaf09addd0b7af3dbb7c296` | 2826 |  |
| 54 | `eos-ab-upgrade/integration-contracts.md` | 002 | `d90036f945a28ccb800c393830ef85c1e9f372e5a87d421a9b41ddb9583fac9f` | 12684 |  |
| 55 | `eos-ab-upgrade/pyproject.toml` | 002 | `abac7a4acd4095d0d82dbf812d60bfb43d3c5f1fd29f8b3c978d18fdeee7bd07` | 598 |  |
| 56 | `eos-ab-upgrade/services/eos_upgrade/__init__.py` | 002 | `d20ac91f39a421d5724e8196df1b900f17dca06098216939b68099ede38c11bf` | 482 |  |
| 57 | `eos-ab-upgrade/services/eos_upgrade/cli.py` | 002 | `7af4f1bc8e4c93ac3e714e999de3021593bd14eeab6948812d846b080387f7f4` | 2071 |  |
| 58 | `eos-ab-upgrade/services/eos_upgrade/device_broker.py` | 002 | `fc3cbe328e32e3ebdf15093982dc657a992f6e2643362ac1c8256dc673a68fff` | 2537 |  |
| 59 | `eos-ab-upgrade/services/eos_upgrade/iag_entrypoint.py` | 002 | `57bb512d7a22d881b4dfaf2b9f74823fb15a64a83d8af4e02295706e831b97bb` | 591 |  |
| 60 | `eos-ab-upgrade/services/eos_upgrade/maintenance.py` | 002 | `49405497ad12324af8fb6e136fcddcd90dfb512f11cffc030677434a15af64f0` | 1957 |  |
| 61 | `eos-ab-upgrade/services/eos_upgrade/models.py` | 002 | `13794b557695f0eb917f36dcf486afc87febbb8ed10b625433432524b2389a1d` | 3070 |  |
| 62 | `eos-ab-upgrade/services/eos_upgrade/precheck.py` | 002 | `78a693ae6aa62d371dffde6604ed8a2e9e3b9fd54cf4b8350df02c62cda9ef35` | 3947 |  |
| 63 | `eos-ab-upgrade/services/eos_upgrade/readiness.py` | 002 | `34ad9f4db81f9730a73d792586e8c50d860486658217e1bb0eed50d96cafb3f4` | 2364 |  |
| 64 | `eos-ab-upgrade/services/eos_upgrade/readiness_entrypoint.py` | 002 | `126aa551f9e11718420f6fad890808f66c063e8d96ec4f1df33703a9fed09798` | 600 |  |
| 65 | `eos-ab-upgrade/services/eos_upgrade/reporting.py` | 002 | `722d18aa1c2719e0ff6041dd999f4fc87029f257e826f424ad8769d7c40df4df` | 3129 |  |
| 66 | `eos-ab-upgrade/services/eos_upgrade/upgrade.py` | 002 | `545d3eb88653fa4cf4f618e5889884f5657351b396815a90a85fc41722379203` | 5295 |  |
| 67 | `eos-ab-upgrade/services/eos_upgrade/validation.py` | 002 | `353f4db4389fbc42be4f15acf136852857fae77e721bf299ab5a4384504bf36f` | 1451 |  |
| 68 | `eos-ab-upgrade/specs/spec-arista-eos-ab-upgrade.md` | 002 | `9ea36939ceabcb76909ed46a1ec7df7504d7c50e72b65bac442532eaaedb0e6d` | 15867 |  |
| 69 | `eos-ab-upgrade/specs/workflow-task-map.md` | 002 | `75fd9d3b104142be0ead00ed6e4ac69f5bcf0772f7f078eead98492f6f4c16e4` | 2350 |  |
| 70 | `eos-ab-upgrade/tests/fixtures/fake_broker.py` | 002 | `86aebabc0879b0ec7c194f7d76d630f35c20dca0a1d978809f4026857aa7074c` | 1724 |  |
| 71 | `eos-ab-upgrade/tests/fixtures/readiness_payloads.py` | 002 | `0cd3d13127709e8bae076a0122a44962c57a723446ba1e745631059a25e04df5` | 981 |  |
| 72 | `eos-ab-upgrade/tests/test_device_broker.py` | 002 | `e0d328929a034f7f8ffaff210401a5c682c083b5b42493ec539e49755598926a` | 3195 |  |
| 73 | `eos-ab-upgrade/tests/test_maintenance.py` | 002 | `1a7cb7b3c5e09ba16d95c099878c4c169da73d085caa72e59b78885c90ca771c` | 1846 |  |
| 74 | `eos-ab-upgrade/tests/test_precheck.py` | 002 | `c698fedee3691a78b624df41104161421a9564f8688b0aa08e33ac6ffec0ad88` | 4474 |  |
| 75 | `eos-ab-upgrade/tests/test_readiness.py` | 002 | `296e58c954c1bacf5074600cab472edd02d90c615044118d11e91630d4bd047b` | 3557 |  |
| 76 | `eos-ab-upgrade/tests/test_reporting.py` | 002 | `21b641d92e38f7f6c85ff68a7b39f7861ebda3fad5ba664d9c6f3e0c188bc53b` | 2256 |  |
| 77 | `eos-ab-upgrade/tests/test_validation.py` | 002 | `b787446c11fe04fe4d10ec2012cd246c5b109444c9f6101b701b7b1955748b5d` | 1810 |  |
| 78 | `eos-ab-upgrade/workflows/eos-postcheck.json` | 002 | `73dd1c75d1614a8e1a96c41889e6cffd366371a2f680ba9a52bf51f48588ca47` | 1714 |  |
| 79 | `eos-ab-upgrade/workflows/eos-precheck.json` | 002 | `f64139d34557a500f1da9e7fbd1cb78bcef3d0032177535485c01612777527f8` | 16001 |  |
| 80 | `eos-ab-upgrade/workflows/eos-upgrade-orchestrator.json` | 002 | `e1b47f233945c88a19f9d52cdd0f6568cbe9d4badfb526d0d272e5fcd64b0044` | 2199 |  |
| 81 | `eos-ab-upgrade/workflows/eos-upgrade-readiness.json` | 002 | `d89fc53c344e7a4aefb005cb3d6f54148786a8b0029790525ccd8abfe879b584` | 14081 |  |
| 82 | `eos-ab-upgrade/workflows/eos-upgrade-single-device.json` | 002 | `35326eac79dfc9c6889eedbbcc99847e93f4d8f63be0572dabbb7c28ced2cfc5` | 1872 |  |
| 83 | `eos-readiness-engine/.gitignore` | 002 | `8962e682183305bf1e68766d862524ce1bfec6b635491747a812c3df92a35c8b` | 66 |  |
| 84 | `eos-readiness-engine/README.md` | 002 | `54f8631a63d601aa2f2fe5df5c961e097bea92177153007d083bc371d5106da6` | 5783 |  |
| 85 | `eos-readiness-engine/eos_readiness/__init__.py` | 002 | `e1fa9afb22cc9c8546909b95ee30af917b994d8032be416efd2d874841f3f5f4` | 303 |  |
| 86 | `eos-readiness-engine/eos_readiness/checks/__init__.py` | 002 | `03bc8337f3553e23bdd19479ac81119d132aac92f54b27790ac4434f47c0f69c` | 269 |  |
| 87 | `eos-readiness-engine/eos_readiness/checks/bgp.py` | 002 | `2e6131f68bfba2932dce8fb4b8cc15ec867e5fa358f6b993bfdd4fb61c368d66` | 2176 |  |
| 88 | `eos-readiness-engine/eos_readiness/checks/collection.py` | 002 | `9fd034b0d377ef356770bf2fc2baa9ab53c6b9c5b45cee07db56ec82a0cf7b58` | 1303 |  |
| 89 | `eos-readiness-engine/eos_readiness/checks/interfaces.py` | 002 | `ed33977a6fff2967f3e4447ce71315f7a581c6eea02aa96e3324a1a50a5b57ab` | 2208 |  |
| 90 | `eos-readiness-engine/eos_readiness/checks/mlag.py` | 002 | `a537e42152e53a7126d2e0a55c0c4bd39b3cef6a7aac45656488e35cba7fa18c` | 1897 |  |
| 91 | `eos-readiness-engine/eos_readiness/checks/version.py` | 002 | `805342868af82bfcfebd747dfbee69051cd6d223529e90f322a41e088f40710d` | 1281 |  |
| 92 | `eos-readiness-engine/eos_readiness/engine.py` | 002 | `68bd5979117146388aa3b1e14ffc27704a73071ede6f572f3dd4cdc2fb55b7c7` | 3187 |  |
| 93 | `eos-readiness-engine/eos_readiness/errors.py` | 002 | `e11674f05bdb4a502fce8f5db1ce20d4f3b4c2144cf4979b3a14eb75a3fdd060` | 247 |  |
| 94 | `eos-readiness-engine/eos_readiness/iag_entrypoint.py` | 002 | `f89bff287ded7825d24eec9b50b13661e7642dfec917b49e0dbd8cf98b81fad4` | 673 |  |
| 95 | `eos-readiness-engine/eos_readiness/models.py` | 002 | `23ae4855627e4d3ae4a64877f117c2921b7ec7450774dd16226f07ba037b8b66` | 1657 |  |
| 96 | `eos-readiness-engine/eos_readiness/profiles/__init__.py` | 002 | `aa1b3fee884850dc058923b96d290fc76bebe85e6cc615c9373224f18874035e` | 151 |  |
| 97 | `eos-readiness-engine/eos_readiness/profiles/registry.py` | 002 | `1df3d4ad11d9418cb86edc72ff163bdb396f943a7509843cb98438de2af0cc9e` | 771 |  |
| 98 | `eos-readiness-engine/eos_readiness/raw/__init__.py` | 002 | `a3fccc857532a6438c2b1a07de735413d7009262f9427da45c48832011dbd681` | 543 |  |
| 99 | `eos-readiness-engine/eos_readiness/raw/collectors.py` | 002 | `1837c81836800cfc08eb00fed743470f5694fc02a1bbc143a628e8df0fd3dabd` | 1248 |  |
| 100 | `eos-readiness-engine/eos_readiness/raw/normalize.py` | 002 | `954c427cd9b7242154732809df23a0bb218e165958acd5119f0bb4e32468ca22` | 2598 |  |
| 101 | `eos-readiness-engine/eos_readiness/raw/parsers.py` | 002 | `7ed63f84570869a95c6ca8d548e394fd38e9def8cdb3b9a59c19dca9a2243d35` | 1721 |  |
| 102 | `eos-readiness-engine/eos_readiness/status.py` | 002 | `d211ad74252b2ac97c3b6182c68e20a4166a1cd7b4ca0e4a6123c528792f3e14` | 514 |  |
| 103 | `eos-readiness-engine/iag/eos-readiness-service.yaml` | 002 | `2ab7d9df291a6f1041be115fbd8030bbb95040c1e26cf8b5c650033d4e116650` | 2831 |  |
| 104 | `eos-readiness-engine/pyproject.toml` | 002 | `5e40996a5628b05664dc98661e07dbd12a5bfd96d7914a55cc1caf9035d44271` | 548 |  |
| 105 | `eos-readiness-engine/tests/factories.py` | 002 | `cbf9f52276934f382204148bac1039816fd866de38f7d4cf39cac1e524457247` | 1973 |  |
| 106 | `eos-readiness-engine/tests/fixtures/raw/USILD001LAB01A__show_version.json` | 002 | `d8da9d18869dec32d1b77d69b4bf00163bf68e210d4ecd0bb259b98d0a484244` | 563 |  |
| 107 | `eos-readiness-engine/tests/fixtures/raw/command_results_pair_sample.json` | 002 | `cc49221658fdf6e8cb2292a1d1f46341e67cb9ad6206ca887835c15ce28b7f74` | 4359 |  |
| 108 | `eos-readiness-engine/tests/test_checks_bgp.py` | 002 | `bf22a8369a9266b16ad5acf8dba9c306b05e3aa87bc6b8fb49fbff0dfcf7d578` | 2539 |  |
| 109 | `eos-readiness-engine/tests/test_checks_collection.py` | 002 | `9351fbe70d7b2ad73f8838d34ada07447e4693fc06b0d0947faab3ba680d35f6` | 1996 |  |
| 110 | `eos-readiness-engine/tests/test_checks_interfaces.py` | 002 | `ee78a26239b96fd58faa81057bdbc63dedbe6f9086dbb754fe01532ea4e93980` | 2230 |  |
| 111 | `eos-readiness-engine/tests/test_checks_mlag.py` | 002 | `0cfa54ae8e4a00bc01c9bc2c308de07eaa0260bc5c9609065a21f2578242f23a` | 1771 |  |
| 112 | `eos-readiness-engine/tests/test_checks_version.py` | 002 | `add6ef41ba2b1175e5144fb70b438a3b312d3da29aed6a58f595c772945fc529` | 1425 |  |
| 113 | `eos-readiness-engine/tests/test_collectors.py` | 002 | `9755e0c02cc9a2730cc2e337baee39ce08716a0311f89c563c4c2e15f098edc1` | 2503 |  |
| 114 | `eos-readiness-engine/tests/test_engine_decision_contract.py` | 002 | `673439dfd5294379d4bb3d5a3fcbdd6aa39ad9bda80bd5ed668c4819c5ecfd34` | 4374 |  |
| 115 | `eos-readiness-engine/tests/test_evaluate_pair.py` | 002 | `c88a152dc6841ec7cb4baa1e62f2d4ca53d0e7b9f9e9fa626be8f06ba7cc5eb9` | 3976 |  |
| 116 | `eos-readiness-engine/tests/test_normalize.py` | 002 | `623d6e5671a29c07d583b27b8d1bdb2a25e92fe1419f6f18a1ff4176de9e595e` | 4359 |  |
| 117 | `eos-readiness-engine/tests/test_parse_show_version.py` | 002 | `1ad7294e0d21c13ba9bc10ef4e8ae3f81e301eadc5cdf354d0ebad52ff0a97d8` | 1540 |  |
| 118 | `eos-readiness-engine/tests/test_profiles.py` | 002 | `998cc08e9b77afa2859e15ed15a683d9dd21eba64a0de1f43c10ea761ab2c81b` | 1200 |  |
| 119 | `eos-readiness-engine/tests/test_status.py` | 002 | `4bcef47f6f328d136fb4a7a320dc964df2dfe4a9a4651a8d6b295acabb37fb13` | 829 |  |
| 120 | `eos-readiness-engine/workflows/eos-ab-readiness.json` | 002 | `6da4685c05dfd7730266da57422ef8dff0f1b2a2dcdb707a74a32d55e8a0fae5` | 20844 |  |
| 121 | `evals/COVERAGE-REPORT.md` | 002 | `53bf9c1138fe6eefff1cb4c659dcbe498cd7947bc78fd4763b1fcd69293c7983` | 7536 |  |
| 122 | `evals/e2e/e2e-results.json` | 002 | `2fa10acf0f22dc59234a5ee1db26e804ab0c143123d01dde6c08efd607009c5d` | 1460 |  |
| 123 | `evals/e2e/run-e2e-tests.sh` | 002 | `75b4ce84f58eac9883364aca267fc8a22ad3caf9ee6b1b2d7137e1b9bd2acae4` | 14768 |  |
| 124 | `evals/e2e/test1-utility-chain.json` | 002 | `a97a57a0d2b3f612d67dacc159b21cd318993e8c573c69fc850827e17a375bee` | 6627 |  |
| 125 | `evals/e2e/test2-child-workflow.json` | 002 | `43d95b3f14d5c1c11f99de1e39dde7ec6560bdf5846cbab4158887d116a4e980` | 3534 |  |
| 126 | `evals/e2e/test2-parent-loop.json` | 002 | `f5bd665346e1d75df961b83189df9730a269fa5385b2b434c06bfc54aba125be` | 3765 |  |
| 127 | `evals/e2e/test3-adapter-servicenow.json` | 002 | `c741df540afae816a69f611ce3f0770083e3b26826d369a938e44178dd1b0fd8` | 5617 |  |
| 128 | `evals/evals.json` | 002 | `e3ef313e4291703c22ac0f3ed2eb60257d221876ba4b041f9eb1d3f85989c2fa` | 53224 |  |
| 129 | `evals/trigger-evals/README.md` | 002 | `7c997cb476024b3eafbcf944297491ed139a890d399e0df99539c75751059e97` | 1657 |  |
| 130 | `evals/trigger-evals/builder-agent-results.json` | 002 | `5179439e62048a3d34da89426b4b9813ebc01b96db7d34abe4aaad16d932edce` | 5851 |  |
| 131 | `evals/trigger-evals/builder-agent.json` | 002 | `fc62edc8e978d251fb0448244bb0522370714bef15aaefdee7e662e71e5ecea8` | 3085 |  |
| 132 | `evals/trigger-evals/documentation-results.json` | 002 | `00e90a132735e4445917251a7c47246abd34685caa0a613ac08e147a19087e3a` | 7249 |  |
| 133 | `evals/trigger-evals/documentation.json` | 002 | `db169c6e9d59c76853d636168431965de156b88428827991fceed7b342672bc4` | 4399 |  |
| 134 | `evals/trigger-evals/explore-results.json` | 002 | `501ad8a33f4118515190029120532a38cd4bea7910991bbbc8458fc6abf23744` | 5736 |  |
| 135 | `evals/trigger-evals/explore.json` | 002 | `63d5974f8d4b1bb81863b5d43ddfb092daf6e2472c5ccbb65ba54c5f6bba2302` | 3011 |  |
| 136 | `evals/trigger-evals/solution-arch-agent-results.json` | 002 | `af806a37062d569f8a6d73dd36b9b36e0854d118b4732d49e69c0d19e180cd33` | 5909 |  |
| 137 | `evals/trigger-evals/solution-arch-agent.json` | 002 | `50481d289a811529cd61744112dab62b42eaa922c54a7f34eeab77da285b77cf` | 3191 |  |
| 138 | `evals/trigger-evals/spec-agent-results.json` | 002 | `4374fcb113562cf2b4d994c3542380318ace5297cf2b00878936187ea68d5e7a` | 6383 |  |
| 139 | `evals/trigger-evals/spec-agent.json` | 002 | `c8a11b54e527a965d1a17c4b3405d62e47ea236e3bfae5174335be721da4e2e7` | 3572 |  |
| 140 | `helpers/assets/flowagent-sample-agent-project.json` | 002 | `7992aad2265b03c1933fb10c8bcbfdce4f48cfefcdc3885ae67eecc46627c08a` | 6785 |  |
| 141 | `helpers/assets/itential-platform-configuration-management.json` | 003 | `6ace31e639f9f131b0a8eb5c5cc55a97f58677facd582725a776395bee4ed8a7` | 284546 |  |
| 142 | `helpers/assets/itential-platform-data-manipulation.json` | 004 | `e28a737a190e61297f7319c02aed21f9657b49c1a9aed06f99eef9d4a4aa213d` | 572699 |  |
| 143 | `helpers/assets/itential-platform-email.json` | 005 | `f52927d0d921d04793fc8c330ba591ecb4b8ed085698e89b1ca4cc987b2b348c` | 52681 |  |
| 144 | `helpers/assets/itential-platform-regex-operations.json` | 005 | `e899f02efeef218ca6dfb5b3d388d08fb106e48f801209b8399632e8f3a975f3` | 74608 |  |
| 145 | `helpers/assets/json-form-example-rest-bound.json` | 005 | `cdcb0caf6c5aa4a97822d7415f441cd7814dbc3373f1a5259d60231852eec2a4` | 3061 |  |
| 146 | `helpers/assets/json-form-example-static-enum.json` | 005 | `be725dd18ac66c9c72e0db9a0fb0f557af3487ae9abff0a1cf365c345b0c0b16` | 6548 |  |
| 147 | `helpers/assets/lcm/lcm-fan-device-lifecycle-management.json` | 005 | `c98da25a0797174e04d2671c96b2db823cd18b28dcd3e2aca56328931d08848f` | 8692 |  |
| 148 | `helpers/assets/lcm/lcm-interface-service-provisioning.json` | 005 | `f1cd841fa9296eedc4153c890e3741f12d34c4df6cf5bcac6bf8f8313a26f471` | 4895 |  |
| 149 | `helpers/assets/lcm/lcm-ip-blocking-service.json` | 005 | `751e7853f79ca534dd3cb4056456adebcf1b145384c827e3f552e0ea3dfb91b2` | 2767 |  |
| 150 | `helpers/assets/lcm/lcm-port-turn-up.json` | 005 | `eda3417a2225dc198efaf01b42dc0c7751d77d5ea77982115bf010a61695f578` | 17578 |  |
| 151 | `helpers/assets/lcm/lcm-vxlan-fabric-management.json` | 005 | `5c63c15af648ab00788d23e82a13f59f906c04eaa65dc6275f52bf31805b1202` | 19507 |  |
| 152 | `helpers/assets/lcm/lcm-vxlan-fabric-services-project.json` | 006 | `5b5b61f685c995839db233fc2432a5fc209ce681ec29baf60f214535cb66683b` | 331741 |  |
| 153 | `helpers/assets/openapi-specs/whoami-basic-auth.json` | 006 | `7c08c286b959ba937e7de387f5a06e3b78de9f9c4c82876e2250d4df73cc8e95` | 1352 |  |
| 154 | `helpers/assets/openapi-specs/whoami-client-creds.json` | 006 | `b911142410e8117dffac5d03822f633e6a46aa7874b342edda62a914cb801c9d` | 1227 |  |
| 155 | `helpers/assets/vendor-arista-eos.json` | 007 | `50cb879c813ee36dae8a68512bc4095e547f1d243928aea23d0170452e1d60cb` | 257023 |  |
| 156 | `helpers/assets/vendor-cisco-ios.json` | 008 | `1c072dfb95ca55d70687757b91e545509bc9d61880282d97ba34ffec473ef343` | 341275 |  |
| 157 | `helpers/assets/vendor-infoblox-nios-ddi.json` | 009 | `71e8dfb5a4c5cee7de5e32c905f31753769dff286f13394ee4b39e92567450aa` | 302461 |  |
| 158 | `helpers/assets/vendor-juniper-junos.json` | 009 | `8b364175a33ea0d16c25092d3f7f2fa88dd09b7c3ca588badf1f2208ef7e3a10` | 152400 |  |
| 159 | `helpers/assets/vendor-netbox.json` | 010 | `62972f30dc2f74fe25035674c362deeeab0844249c5228a41d4d25101ae6e68b` | 183963 |  |
| 160 | `helpers/assets/vendor-servicenow.json` | 010 | `febfc6152102f9e07f95acdd87aca46c3c5b3d19369715d08ae1805b5129f579` | 141501 |  |
| 161 | `helpers/create/create-command-template.json` | 010 | `02f04e1a20595f058b8acf6de9d3e3a368a67240ebc27cb51d4cbdec1f4f76de` | 475 |  |
| 162 | `helpers/create/create-compliance-plan.json` | 010 | `1e0cbea0a26a2feeb245fe670827b1f577fb503262e2b34ffd9e1d65923d6d43` | 780 |  |
| 163 | `helpers/create/create-flowagent-decorator.json` | 010 | `0041d02fdfdf1017ac3e6472eccd566ba7d35b9bee0978ed6bf5905c59f8d7f2` | 1168 |  |
| 164 | `helpers/create/create-flowagent-project-bundle.json` | 010 | `f0421d325d4aabd9faaf6d7323bc6d93f55dfff2e158d9275ee4dc66454969a0` | 2780 |  |
| 165 | `helpers/create/create-golden-config-node.json` | 010 | `b8c7c7b2e1fe987b94ebbdedde5b7a913295bc572755e7453a2c80af74c2b86a` | 34 |  |
| 166 | `helpers/create/create-golden-config-tree.json` | 010 | `3e105398a7fa8e02a28198cdd571aeca70c46108729f02bf9bbf652c8276e5cf` | 63 |  |
| 167 | `helpers/create/create-integration.json` | 010 | `2009e71e95bb6b370cf3a4ef0a96688c7f36251e6b9be56e339beb04e38571cb` | 1488 |  |
| 168 | `helpers/create/create-json-form-rest-bound.json` | 010 | `0fe1eaf6d8e715730f7480890696a349ea50184203cfe51cb8761aa7ac5f73a3` | 7591 |  |
| 169 | `helpers/create/create-json-form.json` | 010 | `3a375912a174aa6611473d5b02b1f5b22bd2c9d0e9303d9ad533ea47eb31f2a5` | 3338 |  |
| 170 | `helpers/create/create-lcm-resource-model.json` | 010 | `389336ed82e3fa3cdd76e1a26bed86763149597b4eb1356b982f074f7addeba8` | 1381 |  |
| 171 | `helpers/create/create-ops-manager-automation.json` | 010 | `8125764195f15d2f0f57a460d9608a4aeeb309437fa9a53f408661c07d979458` | 268 |  |
| 172 | `helpers/create/create-ops-manager-trigger-manual.json` | 010 | `65d4a5093bf0688d7a0ca046446c486f9b4af29724633828553bb0bd830456a5` | 170 |  |
| 173 | `helpers/create/create-ops-manager-trigger-schedule.json` | 010 | `f03724cd6488688b7bcaca9875e1a910227b077db06ce01f24592b3adbe17e4f` | 605 |  |
| 174 | `helpers/create/create-ops-manager-trigger.json` | 010 | `f33401b088fa31a05a8c0eec929993447c5c48c3d7bd7dc263c34f62ef7c520e` | 431 |  |
| 175 | `helpers/create/create-project.json` | 010 | `19a6021a729561d7b6219615ab230ef3de96729e5a84d8592e5e0751d29e1203` | 76 |  |
| 176 | `helpers/create/create-template-jinja2.json` | 010 | `9ce272f10f38b98aa2fc67692c00c328691bc79af08a86fc7a9101a64a9cb8b8` | 2302 |  |
| 177 | `helpers/create/create-template-textfsm.json` | 010 | `a85505c05d2abe44e775f2165bb7adfc282a06abec483b80a041d876a008802b` | 876 |  |
| 178 | `helpers/create/create-workflow.json` | 010 | `268d864cef886a0c1c0723aba3057cd66faf9b912ee139e6220b8f9b78774130` | 726 |  |
| 179 | `helpers/create/import-project.json` | 010 | `48d1bf58e53f3bb61befab7b2a8872448faf9ca847671b1e69a4ad5027d2bfa2` | 4020 |  |
| 180 | `helpers/documentation-output-templates.md` | 010 | `7175ffbf8dc001d93246ae0ffe2f3912dce47bf8bbbd800d9434a09ce0ad2dbf` | 16025 |  |
| 181 | `helpers/iag/example-ansible-service.yaml` | 010 | `101a5f6c4cb8bab48086c49841df5285b144e606665bd80a13ddfcb20953668e` | 1422 |  |
| 182 | `helpers/iag/example-multi-service-chain.yaml` | 010 | `0db8481080fadae6e709007c91921ed8e8fc8d94f42b9b53382dde00a7ca0f05` | 2800 |  |
| 183 | `helpers/iag/example-opentofu-service.yaml` | 010 | `bfec162ca22dec30771e1dfb47d2bb081dffae72f01db247fe29000cef91bcbf` | 1673 |  |
| 184 | `helpers/iag/example-python-service.yaml` | 010 | `e44154a5a483ee50484d1717a737d8ec508fc6534eb75f6d6efda79eebf964a4` | 1387 |  |
| 185 | `helpers/iag/service-file-schema.md` | 010 | `6f883045f0a44e2453c887d323570013a7b37627ec2e61f250441e375b9a8927` | 10014 |  |
| 186 | `helpers/operations/add-components-to-project.json` | 010 | `3c7cb7446e585cdde36be568bb66cce0d0727da51d408139cb9df289323b38f8` | 734 |  |
| 187 | `helpers/operations/add-devices-to-node.json` | 010 | `bd23188b4dbeb9d166064f4341d37ac32a03ea8a3db76bbe6fe24e7797b28b65` | 68 |  |
| 188 | `helpers/operations/run-compliance-plan.json` | 010 | `86b7160c8f23334fcbbe068c674eaa7fb55f201a027a0c1b9f6390717e158f6a` | 51 |  |
| 189 | `helpers/operations/run-compliance.json` | 010 | `cb77054838de6ca4615dc0c931ec563c26edd3c3ca2a577e54cf97904e2a275d` | 124 |  |
| 190 | `helpers/update/update-command-template.json` | 010 | `8505666d1f13d637b149b91e2fc24c7e722f5ec3a6c3e65eedd250723ed3f6ad` | 441 |  |
| 191 | `helpers/update/update-json-form.json` | 010 | `0185b8516f52ec225bf0bcd49e5377d3a14f73a20d1a8e0958a8419dea8be99c` | 899 |  |
| 192 | `helpers/update/update-node-config.json` | 010 | `c25a883ad7ae307eb6ff51a50479f21c2968987d512e10b730cac744d1cf18f1` | 898 |  |
| 193 | `helpers/update/update-project-members.json` | 010 | `c76bfbb520abc1d84cae26c71ed75da3f12ebcc78d03905ea79ee23ab11b6631` | 334 |  |
| 194 | `helpers/use-case-memory.md` | 010 | `14ee19f60cf439ec738779c1f30625ef0aabd750c9d053d06ea68276c55136c9` | 2233 |  |
| 195 | `scripts/platform_pull.py` | 010 | `36bcebc03cc4efb1dcbd72670acbedac416fafbed5b7d866baff1047979a77b2` | 6549 |  |
| 196 | `scripts/use_case_init.py` | 010 | `94bfa0efde8a751a7dd07680e2bb8ec62fc948fd3cc3596eefd640d5a2466435` | 3389 |  |
| 197 | `spec-files/demo/device-health-agent.md` | 010 | `2c434698dff07052facfafb80fc89df48f54b4c94d54f3377620753f2df883b8` | 10777 |  |
| 198 | `spec-files/demo/linux-diagnostics-agent.md` | 010 | `2123ba71c9c83ff017437a3f370ab7cb4ef0537b0c04758b4af4a9d048a9d9fb` | 36767 |  |
| 199 | `spec-files/demo/spec-dns-a-record-infoblox-simple.md` | 010 | `b7bbb890806a000a3c00b392634ff2074556b9288f5ec170145372389a694474` | 13457 |  |
| 200 | `spec-files/demo/spec-dns-a-record-provisioning.md` | 010 | `a9152d863c5cc13a7626f58d7ca15648893c1a501cc1cd1461dca7ff09994b84` | 10062 |  |
| 201 | `spec-files/spec-arista-eos-ab-upgrade.md` | 010 | `9ea36939ceabcb76909ed46a1ec7df7504d7c50e72b65bac442532eaaedb0e6d` | 15867 |  |
| 202 | `spec-files/spec-aws-webserver-deploy.md` | 010 | `11f72c2d40c8260d562ff1bb9b37462f0a097234b44956b0363f8a369304e906` | 7958 |  |
| 203 | `spec-files/spec-bgp-peer-provisioning.md` | 011 | `0f75286627a07359afe86635d446f8eaa5169937fb0a2f91f8b4bf97c75ef151` | 10174 |  |
| 204 | `spec-files/spec-change-management.md` | 011 | `57dfee2c929fd1daa0c3fcbc72c412e4bb4427394142756559c284d20f13231f` | 8846 |  |
| 205 | `spec-files/spec-circuit-provisioning.md` | 011 | `91acdba64031fa30cb79e867f280734b4be0c52d2e312c2dde5e73304a9636b1` | 8740 |  |
| 206 | `spec-files/spec-cloud-security-groups.md` | 011 | `4e4474b384b85014a4bce1d15f15b74bd7e8c8cb25ae4a92dbceed5db6d61537` | 9272 |  |
| 207 | `spec-files/spec-config-backup-compliance.md` | 011 | `b914ea07952b29a203d20963e8daa3d8d843c4e0d964cb9c66290b942c86ce77` | 8226 |  |
| 208 | `spec-files/spec-config-drift-remediation.md` | 011 | `2685952de631fb7e039283c117e769f2723fef14b3d75dbd5996fa749c70cc4b` | 9397 |  |
| 209 | `spec-files/spec-device-decommissioning.md` | 011 | `581ce951d165ebaee15c5eeb27c32384f165098ba169a6494f15126bee71ab1b` | 9335 |  |
| 210 | `spec-files/spec-device-onboarding.md` | 011 | `33715efbb82531b9c8efaf3f7bd45d303c578f24dbcf078c82d7a85787c0f10f` | 8402 |  |
| 211 | `spec-files/spec-dns-record-management.md` | 011 | `0c199f7a44c580804c60b92dec9e1942ce684b47ce6cd7fdf123d69bbb1d30f5` | 11171 |  |
| 212 | `spec-files/spec-firewall-rule-lifecycle.md` | 011 | `dd4a7d3fd6674ba12f24096a734cf4a6678de41a859ad37fc6d74425a7e420d7` | 9159 |  |
| 213 | `spec-files/spec-incident-auto-remediation.md` | 011 | `859078bca74e99a43ec64c25520e05550766ab26c142d8e5a5413e6fc3cf372a` | 8996 |  |
| 214 | `spec-files/spec-ipam-lifecycle.md` | 011 | `8cf66014d0468b2e8f1c91f3b2a24dcf2298ee8a6632f57ea641b9af3168f4a8` | 9299 |  |
| 215 | `spec-files/spec-load-balancer-vip.md` | 011 | `043db32838c7bcdec7c8334ac22a89c2a61d2e813b61ed20a00bf2ce06dce7d2` | 8875 |  |
| 216 | `spec-files/spec-network-compliance-audit.md` | 011 | `0bcd0f3ea9e878c4a1bc3760c0081f6f3ff46c8b6384779592a340e04c7a368b` | 9322 |  |
| 217 | `spec-files/spec-network-health-check.md` | 011 | `8703004d9ab631187a1ac83d35ae702696008002df71a7de78d94ca79c44d4ed` | 8342 |  |
| 218 | `spec-files/spec-port-turn-up.md` | 011 | `551a28d4d8b2e7cbc40cbd7a3e93be9c08fb656f2c4a37d4decefd21ccc0daed` | 10225 |  |
| 219 | `spec-files/spec-software-upgrade.md` | 011 | `00370ddcb15a2dedabe9f6d4e6e4c6f30f20fdc17a9ddb5d90c105a4bd1758c9` | 6807 |  |
| 220 | `spec-files/spec-ssl-certificate-lifecycle.md` | 011 | `a668e2f92d68a45848f708c134e66b9f9a968afcb2058e0ab70e93c7f55d9eec` | 8441 |  |
| 221 | `spec-files/spec-vlan-provisioning.md` | 011 | `b0f2b76b6963e0331d5c7a2a1bf659145d7e2a4660181660c67b770f7f08182f` | 8490 |  |
| 222 | `spec-files/spec-vpn-tunnel-provisioning.md` | 011 | `33295cbfb51e9336087c1bb0c91377a58e2d06e2f96a7a8ab5cb7be3304a36ec` | 8872 |  |
| 223 | `spec-files/spec-wan-bandwidth-modification.md` | 011 | `4dcc7cab6cb81fe5a02a0989a3469f669bdd3b1f435eeefa710db20bd08041dc` | 8670 |  |
