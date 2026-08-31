# Builder Skills Repository Transfer — Part 010 of 011

**Git commit:** `982d97c1573ca7ea892b39acced9b0d15955c4a9` on branch `main`  
**Generated:** 2026-08-31 21:28:30 UTC  
**See also:** `builder-skills-transfer-manifest.md` for the full repository manifest, directory tree, and complete checksum index across all parts.

This part contains **44** file(s):

- `helpers/assets/vendor-netbox.json`
- `helpers/assets/vendor-servicenow.json`
- `helpers/create/create-command-template.json`
- `helpers/create/create-compliance-plan.json`
- `helpers/create/create-flowagent-decorator.json`
- `helpers/create/create-flowagent-project-bundle.json`
- `helpers/create/create-golden-config-node.json`
- `helpers/create/create-golden-config-tree.json`
- `helpers/create/create-integration.json`
- `helpers/create/create-json-form-rest-bound.json`
- `helpers/create/create-json-form.json`
- `helpers/create/create-lcm-resource-model.json`
- `helpers/create/create-ops-manager-automation.json`
- `helpers/create/create-ops-manager-trigger-manual.json`
- `helpers/create/create-ops-manager-trigger-schedule.json`
- `helpers/create/create-ops-manager-trigger.json`
- `helpers/create/create-project.json`
- `helpers/create/create-template-jinja2.json`
- `helpers/create/create-template-textfsm.json`
- `helpers/create/create-workflow.json`
- `helpers/create/import-project.json`
- `helpers/documentation-output-templates.md`
- `helpers/iag/example-ansible-service.yaml`
- `helpers/iag/example-multi-service-chain.yaml`
- `helpers/iag/example-opentofu-service.yaml`
- `helpers/iag/example-python-service.yaml`
- `helpers/iag/service-file-schema.md`
- `helpers/operations/add-components-to-project.json`
- `helpers/operations/add-devices-to-node.json`
- `helpers/operations/run-compliance-plan.json`
- `helpers/operations/run-compliance.json`
- `helpers/update/update-command-template.json`
- `helpers/update/update-json-form.json`
- `helpers/update/update-node-config.json`
- `helpers/update/update-project-members.json`
- `helpers/use-case-memory.md`
- `scripts/platform_pull.py`
- `scripts/use_case_init.py`
- `spec-files/demo/device-health-agent.md`
- `spec-files/demo/linux-diagnostics-agent.md`
- `spec-files/demo/spec-dns-a-record-infoblox-simple.md`
- `spec-files/demo/spec-dns-a-record-provisioning.md`
- `spec-files/spec-arista-eos-ab-upgrade.md`
- `spec-files/spec-aws-webserver-deploy.md`

---

============================================================
FILE: helpers/assets/vendor-netbox.json
DIRECTORY: helpers/assets/
FILENAME: vendor-netbox.json
============================================================
SHA256: 62972f30dc2f74fe25035674c362deeeab0844249c5228a41d4d25101ae6e68b

````json
{
  "_id": "67341ceda1c9aed687bfdcdc",
  "name": "NetBox",
  "description": "Netbox Project has assets form Creating Prefix, Delete Prefix, Reserve IP Address, Delete IP Address, Assign Next IP (in Previx), Onboard Device",
  "components": [
    {
      "iid": 0,
      "reference": "643bc63e-2607-4e06-9765-24f2f196c707",
      "type": "workflow",
      "folder": "/Create Prefix",
      "document": {
        "name": "Create Prefix",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 444,
              "y": 804
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 444,
              "y": 1128
            }
          },
          "c504": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "Error encountered creating prefix in NetBox. See error response below. Select 'Retry' to retry creating prefix or 'End Job' to end the job.\n\n\n",
                "body": "$var.2cd3.error",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 132,
              "y": 1020
            }
          },
          "6f52": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Build NetBox Prefix Creation Payload",
            "description": "Build NetBox prefix creation payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "61b0c093df69ba016dffc47f",
                "variableMap": {
                  "prefix": "$var.job.prefix",
                  "prefixStatus": "$var.job.prefixStatus",
                  "prefixDescription": "$var.job.prefixDescription"
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "prefixCreationPayload": null
              }
            },
            "groups": [],
            "task_name": "Build Netbox Prefix Creation Payload",
            "retrySettings": null,
            "nodeLocation": {
              "x": 444,
              "y": 912
            }
          },
          "2cd3": {
            "name": "postIpamPrefixes",
            "canvasName": "postIpamPrefixes",
            "summary": "Create Prefix",
            "description": "Create Prefix",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "data": "$var.6f52.prefixCreationPayload",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdPrefix"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 444,
              "y": 1020
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "6f52": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "c504": {
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            },
            "2cd3": {
              "state": "success",
              "type": "revert"
            }
          },
          "6f52": {
            "2cd3": {
              "state": "success",
              "type": "standard"
            }
          },
          "2cd3": {
            "c504": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "565e": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "prefix": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixStatus": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixDescription": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "prefix",
            "prefixStatus",
            "prefixDescription",
            "adapterId"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "prefix": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixStatus": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixDescription": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "createdPrefix": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "netboxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.46.0-2023.1.19.0",
        "font_size": 12,
        "lastUpdatedVersion": "4.69.3-2023.2.146",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated": "2025-01-24T11:03:15.603Z",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "created_by": {
          "provenance": "Local AAA",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": true
        },
        "canvasVersion": 3,
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 1,
      "reference": "2ad66a69-c0a5-44b2-ba0a-1df9ec708680",
      "type": "workflow",
      "folder": "/Delete Prefix",
      "document": {
        "name": "Delete Prefix",
        "tasks": {
          "6036": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "NetBox error encountered getting IP addresses of prefix, see error response below. Select 'Retry' to retry getting IP addresses of prefix or 'End Job' to end the job.\n\n\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -1128,
              "y": 1476
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1452,
              "y": 936
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -996,
              "y": 2220
            }
          },
          "c504": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "NetBox error encountered deleting prefix, see the error response below. Select 'Retry' to retry deleting prefix or select 'End Job' to end the job.\n\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -1416,
              "y": 2220
            }
          },
          "aa1b": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Prefix found?",
            "description": "Prefix found?",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "query": "response.count",
                        "operand_1": {
                          "variable": "result",
                          "task": "084d"
                        },
                        "operator": "==",
                        "operand_2": {
                          "variable": 1,
                          "task": "static"
                        }
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": -1452,
              "y": 1260
            }
          },
          "722f": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Prefix Not Found",
            "description": "Prefix Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Prefix Not Found",
                "message": "Prefix not found in NetBox. See response below.\n\n\n",
                "body": "$var.084d.result",
                "variables": {},
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -924,
              "y": 1296
            }
          },
          "1bd8": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Delete Prefix NetBox",
            "description": "Perform a JSON Transformation using the JST library.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "61b22fdadf69ba016dffc481",
                "variableMap": {
                  "prefixResponse": "$var.084d.result",
                  "ipAddressResponse": "$var.1db2.result",
                  "adapterId": "$var.job.adapterId"
                },
                "options": {
                  "extractOutput": false,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "prefixId": null,
                "prefixHasIps": null,
                "ipsInPrefix": null,
                "ipMessage": null
              },
              "decorators": []
            },
            "groups": [],
            "task_name": "Delete Prefix Netbox",
            "retrySettings": null,
            "nodeLocation": {
              "x": -1452,
              "y": 1608
            }
          },
          "de2b": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Confirm IP Deletion",
            "description": "Confirm IP Deletion",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Confirm IP Deletion",
                "message": "Select YES to delete the IP, select NO to not delete",
                "body": "$var.1bd8.ipMessage",
                "variables": {},
                "btn_success": "Yes",
                "btn_failure": "No"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -1620,
              "y": 1824
            }
          },
          "3ace": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Prefix has IPs?",
            "description": "Prefix has IPs?",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "query": "",
                        "operand_1": {
                          "variable": "prefixHasIps",
                          "task": "1bd8"
                        },
                        "operator": "==",
                        "operand_2": {
                          "variable": true,
                          "task": "static"
                        }
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": -1452,
              "y": 1716
            }
          },
          "4b5c": {
            "name": "childJob",
            "canvasName": "childJob",
            "summary": "Delete IP Address",
            "description": "Runs a child job inside a workflow.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "task": "",
                "workflow": "Delete IP Address - NetBox",
                "variables": {},
                "data_array": "$var.1bd8.ipsInPrefix",
                "transformation": "",
                "loopType": "sequential"
              },
              "outgoing": {
                "job_details": null
              }
            },
            "groups": [],
            "actor": "job",
            "nodeLocation": {
              "x": -1620,
              "y": 1932
            }
          },
          "084d": {
            "name": "getIpamPrefixes",
            "canvasName": "getIpamPrefixes",
            "summary": "Find Prefix",
            "description": "Find Prefix",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "id": "$var.fb34.numToString",
                "isPool": "",
                "markUtilized": "",
                "description": "",
                "created": "",
                "lastUpdated": "",
                "q": "",
                "tag": "",
                "tenantGroupId": "",
                "tenantGroup": "",
                "tenantId": "",
                "tenant": "",
                "family": "",
                "prefix": "",
                "within": "",
                "withinInclude": "",
                "contains": "",
                "depth": "",
                "children": "",
                "maskLength": "",
                "maskLengthGte": "",
                "maskLengthLte": "",
                "vrfId": "",
                "vrf": "",
                "presentInVrfId": "",
                "presentInVrf": "",
                "regionId": "",
                "region": "",
                "siteGroupId": "",
                "siteGroup": "",
                "siteId": "",
                "site": "",
                "vlanId": "",
                "vlanVid": "",
                "roleId": "",
                "role": "",
                "status": "",
                "idN": "",
                "idLte": "",
                "idLt": "",
                "idGte": "",
                "idGt": "",
                "descriptionN": "",
                "descriptionIc": "",
                "descriptionNic": "",
                "descriptionIew": "",
                "descriptionNiew": "",
                "descriptionIsw": "",
                "descriptionNisw": "",
                "descriptionIe": "",
                "descriptionNie": "",
                "createdN": "",
                "createdLte": "",
                "createdLt": "",
                "createdGte": "",
                "createdGt": "",
                "lastUpdatedN": "",
                "lastUpdatedLte": "",
                "lastUpdatedLt": "",
                "lastUpdatedGte": "",
                "lastUpdatedGt": "",
                "tagN": "",
                "tenantGroupIdN": "",
                "tenantGroupN": "",
                "tenantIdN": "",
                "tenantN": "",
                "depthN": "",
                "depthLte": "",
                "depthLt": "",
                "depthGte": "",
                "depthGt": "",
                "childrenN": "",
                "childrenLte": "",
                "childrenLt": "",
                "childrenGte": "",
                "childrenGt": "",
                "vrfIdN": "",
                "vrfN": "",
                "regionIdN": "",
                "regionN": "",
                "siteGroupIdN": "",
                "siteGroupN": "",
                "siteIdN": "",
                "siteN": "",
                "vlanIdN": "",
                "vlanVidN": "",
                "vlanVidLte": "",
                "vlanVidLt": "",
                "vlanVidGte": "",
                "vlanVidGt": "",
                "roleIdN": "",
                "roleN": "",
                "statusN": "",
                "ordering": "",
                "limit": "",
                "offset": "",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.prefixSearchResult"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -1452,
              "y": 1152
            }
          },
          "1db2": {
            "name": "getIpamIpAddresses",
            "canvasName": "getIpamIpAddresses",
            "summary": "Find IP Addresses in Prefix",
            "description": "Find IP Addresses in Prefix",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "id": "",
                "dnsName": "",
                "description": "",
                "created": "",
                "lastUpdated": "",
                "q": "",
                "tag": "",
                "tenantGroupId": "",
                "tenantGroup": "",
                "tenantId": "",
                "tenant": "",
                "family": "",
                "parent": "$var.4e27.return_data",
                "address": "",
                "maskLength": "",
                "vrfId": "",
                "vrf": "",
                "presentInVrfId": "",
                "presentInVrf": "",
                "device": "",
                "deviceId": "",
                "virtualMachine": "",
                "virtualMachineId": "",
                "interfaceParam": "",
                "interfaceId": "",
                "vminterface": "",
                "vminterfaceId": "",
                "fhrpgroupId": "",
                "assignedToInterface": "",
                "status": "",
                "role": "",
                "idN": "",
                "idLte": "",
                "idLt": "",
                "idGte": "",
                "idGt": "",
                "dnsNameN": "",
                "dnsNameIc": "",
                "dnsNameNic": "",
                "dnsNameIew": "",
                "dnsNameNiew": "",
                "dnsNameIsw": "",
                "dnsNameNisw": "",
                "dnsNameIe": "",
                "dnsNameNie": "",
                "descriptionN": "",
                "descriptionIc": "",
                "descriptionNic": "",
                "descriptionIew": "",
                "descriptionNiew": "",
                "descriptionIsw": "",
                "descriptionNisw": "",
                "descriptionIe": "",
                "descriptionNie": "",
                "createdN": "",
                "createdLte": "",
                "createdLt": "",
                "createdGte": "",
                "createdGt": "",
                "lastUpdatedN": "",
                "lastUpdatedLte": "",
                "lastUpdatedLt": "",
                "lastUpdatedGte": "",
                "lastUpdatedGt": "",
                "tagN": "",
                "tenantGroupIdN": "",
                "tenantGroupN": "",
                "tenantIdN": "",
                "tenantN": "",
                "vrfIdN": "",
                "vrfN": "",
                "interfaceN": "",
                "interfaceIdN": "",
                "vminterfaceN": "",
                "vminterfaceIdN": "",
                "fhrpgroupIdN": "",
                "statusN": "",
                "roleN": "",
                "ordering": "",
                "limit": "",
                "offset": "",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.prefixIPAddresses"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -1452,
              "y": 1476
            }
          },
          "e13a": {
            "name": "deleteIpamPrefixesId",
            "canvasName": "deleteIpamPrefixesId",
            "summary": "Delete Prefix",
            "description": "Delete Prefix",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "id": "$var.1bd8.prefixId",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletePrefixResult"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -1272,
              "y": 1956
            }
          },
          "3dd6": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "NetBox error encountered getting prefix, see error response below. Select 'Retry' to retry getting prefix or 'End Job' to end the job.\n\n\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -684,
              "y": 1152
            }
          },
          "4e27": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query prefix",
            "description": "Query prefix from search results by prefix Id",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.results[0].prefix",
                "obj": "$var.084d.result"
              },
              "outgoing": {
                "return_data": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -1452,
              "y": 1368
            }
          },
          "fb34": {
            "name": "numberToString",
            "canvasName": "toString",
            "summary": "Convert prefix ID to string",
            "description": "Convert prefix ID to string",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "automatic",
            "displayName": "Number",
            "variables": {
              "incoming": {
                "num": "$var.job.prefixId",
                "radix": 10
              },
              "outgoing": {
                "numToString": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -1452,
              "y": 1044
            }
          },
          "82ca": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query Delete IP Addresses Result",
            "description": "Query result of deleting IP addresses",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "loop",
                "obj": "$var.4b5c.job_details"
              },
              "outgoing": {
                "return_data": "$var.job.deleteIPAddressResult"
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -1620,
              "y": 2076
            }
          }
        },
        "transitions": {
          "2577": {},
          "6036": {
            "1db2": {
              "state": "success",
              "type": "revert"
            },
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            }
          },
          "workflow_start": {
            "fb34": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "c504": {
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            },
            "e13a": {
              "state": "success",
              "type": "revert"
            }
          },
          "aa1b": {
            "722f": {
              "type": "standard",
              "state": "failure"
            },
            "4e27": {
              "state": "success",
              "type": "standard"
            }
          },
          "722f": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "1bd8": {
            "3ace": {
              "type": "standard",
              "state": "success"
            }
          },
          "de2b": {
            "4b5c": {
              "type": "standard",
              "state": "success"
            },
            "e13a": {
              "type": "standard",
              "state": "failure"
            }
          },
          "3ace": {
            "de2b": {
              "type": "standard",
              "state": "success"
            },
            "e13a": {
              "type": "standard",
              "state": "failure"
            }
          },
          "4b5c": {
            "82ca": {
              "state": "success",
              "type": "standard"
            }
          },
          "084d": {
            "aa1b": {
              "state": "success",
              "type": "standard"
            },
            "3dd6": {
              "type": "standard",
              "state": "error"
            }
          },
          "1db2": {
            "6036": {
              "type": "standard",
              "state": "error"
            },
            "1bd8": {
              "state": "success",
              "type": "standard"
            }
          },
          "e13a": {
            "c504": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "3dd6": {
            "084d": {
              "state": "success",
              "type": "revert"
            },
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            }
          },
          "4e27": {
            "1db2": {
              "state": "success",
              "type": "standard"
            }
          },
          "fb34": {
            "084d": {
              "state": "success",
              "type": "standard"
            }
          },
          "82ca": {
            "e13a": {
              "state": "success",
              "type": "standard"
            }
          },
          "565e": {},
          "97f6": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixId": {
              "title": "num",
              "type": "number",
              "examples": [124]
            }
          },
          "required": ["adapterId", "prefixId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixId": {
              "title": "num",
              "type": "number",
              "examples": [124]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "netboxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixSearchResult": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixIPAddresses": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "deletePrefixResult": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "deleteIPAddressResult": {
              "title": "return_data",
              "oneOf": [
                {
                  "type": "string"
                },
                {
                  "type": "number"
                },
                {
                  "type": "object"
                },
                {
                  "type": "array"
                },
                {
                  "type": "boolean"
                },
                {
                  "type": "null"
                }
              ],
              "examples": ["value"]
            }
          }
        },
        "createdVersion": "5.46.0-2023.1.19.0",
        "font_size": 12,
        "lastUpdatedVersion": "4.69.3-2023.2.146",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated": "2025-01-24T11:03:15.604Z",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "created_by": {
          "provenance": "Local AAA",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": true
        },
        "canvasVersion": 3,
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 2,
      "reference": "4afe6804-8703-42b0-ac9a-554ff3bc6493",
      "type": "workflow",
      "folder": "/",
      "document": {
        "name": "Reserve IP Address",
        "tasks": {
          "9262": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build IP Reservation Payload",
            "description": "",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "address",
                    "value": {
                      "task": "job",
                      "variable": "ipAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "nat_outside",
                    "value": {
                      "task": "job",
                      "variable": "natOutside",
                      "editable": true
                    }
                  },
                  {
                    "key": "description",
                    "value": {
                      "task": "job",
                      "variable": "description",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 1188,
              "y": 996
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 1188,
              "y": 900
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 1188,
              "y": 1200
            }
          },
          "4ce5": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "Error encountered reserving IP address, see error response below. Select 'Retry' to retry reserving IP address or select 'End Job' to end the job.\n\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 876,
              "y": 1092
            }
          },
          "5bed": {
            "name": "postIpamIpAddresses",
            "canvasName": "postIpamIpAddresses",
            "summary": "Reserve IP Address",
            "description": "Reserve IP Address",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "data": "$var.9262.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.reserveIPAddressResult"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 1188,
              "y": 1092
            }
          }
        },
        "transitions": {
          "9262": {
            "5bed": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_start": {
            "9262": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "4ce5": {
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            },
            "5bed": {
              "state": "success",
              "type": "revert"
            }
          },
          "5bed": {
            "4ce5": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "natOutside": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "description": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["ipAddress", "natOutside", "description", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "natOutside": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "description": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "netboxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "reserveIPAddressResult": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.46.0-2023.1.19.0",
        "font_size": 12,
        "lastUpdatedVersion": "4.69.3-2023.2.146",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated": "2025-01-24T11:03:15.606Z",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "created_by": {
          "provenance": "Local AAA",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": true
        },
        "canvasVersion": 3,
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 3,
      "reference": "60f4909e-fbc2-43b4-8da0-210a2e06ea4f",
      "type": "workflow",
      "folder": "/",
      "document": {
        "name": "Delete IP Address",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -624,
              "y": 900
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -624,
              "y": 1656
            }
          },
          "c504": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "Error encountered deleting the IP address. See error response below. Select 'Retry' to retry deleting the IP address or select 'End Job' to end the job.\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -108,
              "y": 1344
            }
          },
          "aa1b": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "IP address found?",
            "description": "IP address found?",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "query": "response.count",
                        "operand_1": {
                          "variable": "result",
                          "task": "f624"
                        },
                        "operator": "==",
                        "operand_2": {
                          "variable": 1,
                          "task": "static"
                        }
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": -624,
              "y": 1104
            }
          },
          "722f": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "IP Address Not Found",
            "description": "IP Address Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "IP Address Not Found",
                "message": "The IP address was not found in NetBox. See response below.\n\n",
                "body": "$var.f624.result",
                "variables": {},
                "btn_success": "End Job",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -804,
              "y": 1224
            }
          },
          "7b0a": {
            "name": "query",
            "canvasName": "query",
            "summary": "Get IP Address ID",
            "description": "",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.results[0].id",
                "obj": "$var.f624.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -432,
              "y": 1224
            }
          },
          "f624": {
            "name": "getIpamIpAddresses",
            "canvasName": "getIpamIpAddresses",
            "summary": "Find IP Address",
            "description": "Find IP Address",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "id": "",
                "dnsName": "",
                "description": "",
                "created": "",
                "lastUpdated": "",
                "q": "",
                "tag": "",
                "tenantGroupId": "",
                "tenantGroup": "",
                "tenantId": "",
                "tenant": "",
                "family": "",
                "parent": "",
                "address": "$var.job.ipAddress",
                "maskLength": "",
                "vrfId": "",
                "vrf": "",
                "presentInVrfId": "",
                "presentInVrf": "",
                "device": "",
                "deviceId": "",
                "virtualMachine": "",
                "virtualMachineId": "",
                "interfaceParam": "",
                "interfaceId": "",
                "vminterface": "",
                "vminterfaceId": "",
                "fhrpgroupId": "",
                "assignedToInterface": "",
                "status": "",
                "role": "",
                "idN": "",
                "idLte": "",
                "idLt": "",
                "idGte": "",
                "idGt": "",
                "dnsNameN": "",
                "dnsNameIc": "",
                "dnsNameNic": "",
                "dnsNameIew": "",
                "dnsNameNiew": "",
                "dnsNameIsw": "",
                "dnsNameNisw": "",
                "dnsNameIe": "",
                "dnsNameNie": "",
                "descriptionN": "",
                "descriptionIc": "",
                "descriptionNic": "",
                "descriptionIew": "",
                "descriptionNiew": "",
                "descriptionIsw": "",
                "descriptionNisw": "",
                "descriptionIe": "",
                "descriptionNie": "",
                "createdN": "",
                "createdLte": "",
                "createdLt": "",
                "createdGte": "",
                "createdGt": "",
                "lastUpdatedN": "",
                "lastUpdatedLte": "",
                "lastUpdatedLt": "",
                "lastUpdatedGte": "",
                "lastUpdatedGt": "",
                "tagN": "",
                "tenantGroupIdN": "",
                "tenantGroupN": "",
                "tenantIdN": "",
                "tenantN": "",
                "vrfIdN": "",
                "vrfN": "",
                "interfaceN": "",
                "interfaceIdN": "",
                "vminterfaceN": "",
                "vminterfaceIdN": "",
                "fhrpgroupIdN": "",
                "statusN": "",
                "roleN": "",
                "ordering": "",
                "limit": "",
                "offset": "",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.ipAddressSearchResult"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -624,
              "y": 996
            }
          },
          "0910": {
            "name": "deleteIpamIpAddressesId",
            "canvasName": "deleteIpamIpAddressesId",
            "summary": "Delete IP Address",
            "description": "Delete IP Address",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "id": "$var.7b0a.return_data",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deleteIPAddressResult"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -432,
              "y": 1344
            }
          },
          "ddcb": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "Error encountered getting IP address. See error response below. Select 'Retry' to retry getting IP address or select 'End Job' to end the job.\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -1080,
              "y": 1128
            }
          }
        },
        "transitions": {
          "2577": {},
          "workflow_start": {
            "f624": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "c504": {
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            },
            "0910": {
              "state": "success",
              "type": "revert"
            }
          },
          "aa1b": {
            "722f": {
              "type": "standard",
              "state": "failure"
            },
            "7b0a": {
              "type": "standard",
              "state": "success"
            }
          },
          "722f": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "7b0a": {
            "0910": {
              "state": "success",
              "type": "standard"
            }
          },
          "f624": {
            "aa1b": {
              "state": "success",
              "type": "standard"
            },
            "ddcb": {
              "type": "standard",
              "state": "error"
            }
          },
          "0910": {
            "c504": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "ddcb": {
            "f624": {
              "state": "success",
              "type": "revert"
            },
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            }
          },
          "565e": {},
          "97f6": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["ipAddress", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "netboxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddressSearchResult": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "deleteIPAddressResult": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.46.0-2023.1.19.0",
        "font_size": 12,
        "lastUpdatedVersion": "4.69.3-2023.2.146",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated": "2025-01-24T11:03:15.605Z",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "created_by": {
          "provenance": "Local AAA",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": true
        },
        "canvasVersion": 3,
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 4,
      "reference": "329c0adc-4136-403e-ae33-af7ee6fd141d",
      "type": "workflow",
      "folder": "/Assign Next IP (in Prefix)",
      "document": {
        "name": "Assign Next IP Address In Prefix",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 132,
              "y": 984
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 132,
              "y": 1548
            }
          },
          "c504": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "Error encountered getting available IPs for provided Prefix ID. Select Retry to retry call to get available IPs or End Job to end the job.\n\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 876,
              "y": 1188
            }
          },
          "48bc": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Build NetBox IP Assignment Payload",
            "description": "Build NetBox IP assignment payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "61b0ed26df69ba016dffc480",
                "variableMap": {
                  "ipStatus": "$var.job.ipStatus",
                  "dnsName": "$var.job.dnsName",
                  "netboxIpResponse": "$var.4b9c.result"
                },
                "options": {
                  "extractOutput": false,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "nextIpFound": null,
                "ipAssignmentPayload": null
              }
            },
            "groups": [],
            "task_name": "Netbox Extract Next Available IP",
            "retrySettings": null,
            "nodeLocation": {
              "x": 132,
              "y": 1176
            }
          },
          "b8ac": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Next IP Found?",
            "description": "Next IP Found?",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "query": "",
                        "operand_1": {
                          "variable": "nextIpFound",
                          "task": "48bc"
                        },
                        "operator": "==",
                        "operand_2": {
                          "variable": true,
                          "task": "static"
                        }
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 132,
              "y": 1272
            }
          },
          "aeef": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "NetBox Prefix Exhausted",
            "description": "NetBox Prefix Exhausted",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Prefix Exhausted",
                "message": "Requested prefix has been exhausted in NetBox. See prefix data below.\n\n",
                "body": "$var.4b9c.result",
                "variables": {},
                "btn_success": "End Job",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 444,
              "y": 1272
            }
          },
          "4b9c": {
            "name": "getIpamPrefixesIdAvailableIps",
            "canvasName": "getIpamPrefixesIdAvailableIps",
            "summary": " Get Available IPs for Prefix",
            "description": "",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "id": "$var.job.prefixId",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": ""
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 132,
              "y": 1080
            }
          },
          "7fab": {
            "name": "postIpamIpAddresses",
            "canvasName": "postIpamIpAddresses",
            "summary": "Create IP Address",
            "description": "ipam_ip-addresses_create",
            "location": "Adapter",
            "locationType": "NetboxV33",
            "app": "NetboxV33",
            "type": "automatic",
            "displayName": "NetBoxV33",
            "variables": {
              "incoming": {
                "data": "$var.48bc.ipAssignmentPayload",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.assignedIPAddress"
              },
              "error": "$var.job.netboxError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 132,
              "y": 1380
            }
          },
          "d107": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "View NetBox Error",
            "description": "View NetBox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NetBox Error",
                "message": "Error encountered creating IP Address. Select Retry to retry creating IP Address or End Job to end the job.\n\n",
                "body": "$var.job.netboxError",
                "variables": {},
                "btn_success": "Retry",
                "btn_failure": "End Job"
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -192,
              "y": 1392
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "4b9c": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "c504": {
            "4b9c": {
              "state": "success",
              "type": "revert"
            },
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            }
          },
          "48bc": {
            "b8ac": {
              "type": "standard",
              "state": "success"
            }
          },
          "b8ac": {
            "aeef": {
              "type": "standard",
              "state": "failure"
            },
            "7fab": {
              "state": "success",
              "type": "standard"
            }
          },
          "aeef": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "4b9c": {
            "c504": {
              "type": "standard",
              "state": "error"
            },
            "48bc": {
              "state": "success",
              "type": "standard"
            }
          },
          "7fab": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            },
            "d107": {
              "type": "standard",
              "state": "error"
            }
          },
          "d107": {
            "7fab": {
              "state": "success",
              "type": "revert"
            },
            "workflow_end": {
              "type": "standard",
              "state": "failure"
            }
          },
          "565e": {},
          "97f6": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "ipStatus": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["ipStatus", "dnsName", "prefixId", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "ipStatus": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "prefixId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "netboxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "assignedIPAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.46.0-2023.1.19.0",
        "font_size": 12,
        "lastUpdatedVersion": "4.69.3-2023.2.146",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated": "2025-01-24T11:03:15.605Z",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "created_by": {
          "provenance": "Local AAA",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": true
        },
        "canvasVersion": 3,
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 8,
      "reference": "453f35ad-1392-4f88-9685-3e8da5b297c5",
      "type": "workflow",
      "folder": "/Sample Use Cases/Onboard Device in Branch",
      "document": {
        "name": "Onboard Device",
        "tasks": {
          "5630": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query Mgmt Interface ID",
            "description": "Query data using a dot/bracket notation string and a matching key/value pair.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "$var.bbc3.deviceInterfaceQuery",
                "obj": "$var.30af.response"
              },
              "outgoing": {
                "return_data": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 324
            }
          },
          "9147": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query Device ID",
            "description": "Query data using a dot/bracket notation string and a matching key/value pair.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "body.id",
                "obj": "$var.8c57.response"
              },
              "outgoing": {
                "return_data": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -60
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -708
            },
            "x": 0,
            "y": 0.5
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 984
            },
            "x": 1,
            "y": 0.5
          },
          "84e8": {
            "name": "plugins_branching_branches_create",
            "canvasName": "plugins_branching_branches_create",
            "summary": "Create Branch",
            "description": "Post a list of branch objects.",
            "location": "Adapter",
            "locationType": "NetBox:4.1",
            "app": "NetBox:4.1",
            "type": "automatic",
            "displayName": "NetBox",
            "variables": {
              "incoming": {
                "bodyContentType": "application/json",
                "requestBodyPayload": "$var.51ac.payload",
                "X-NetBox-Branch": "",
                "adapter_id": "NetBox"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -480
            }
          },
          "1de4": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query Branch Schema ID",
            "description": "Query data using a dot/bracket notation string and a matching key/value pair.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "body.schema_id",
                "obj": "$var.84e8.response"
              },
              "outgoing": {
                "return_data": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -372
            }
          },
          "8c57": {
            "name": "dcim_devices_create",
            "canvasName": "dcim_devices_create",
            "summary": "Create Device",
            "description": "Post a list of device objects.",
            "location": "Adapter",
            "locationType": "NetBox:4.1",
            "app": "NetBox:4.1",
            "type": "automatic",
            "displayName": "NetBox",
            "variables": {
              "incoming": {
                "bodyContentType": "application/json",
                "requestBodyPayload": "$var.f7d6.payload",
                "X-NetBox-Branch": "$var.1de4.return_data",
                "adapter_id": "NetBox"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -156
            }
          },
          "400b": {
            "name": "delay",
            "canvasName": "delay",
            "summary": "Branch Pending",
            "description": "Delay a Job for a duration by Job ID and number of seconds.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "time": 5
              },
              "outgoing": {
                "time_in_milliseconds": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -312,
              "y": -276
            }
          },
          "30af": {
            "name": "dcim_interfaces_create",
            "canvasName": "dcim_interfaces_create",
            "summary": "Create Device Interfaces",
            "description": "Post a list of interface objects.",
            "location": "Adapter",
            "locationType": "NetBox:4.1",
            "app": "NetBox:4.1",
            "type": "automatic",
            "displayName": "NetBox",
            "variables": {
              "incoming": {
                "bodyContentType": "application/json",
                "requestBodyPayload": "$var.a6ca.interfaceList",
                "X-NetBox-Branch": "$var.1de4.return_data",
                "adapter_id": "NetBox"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 132
            }
          },
          "bd41": {
            "name": "ipam_prefixes_available_ips_create",
            "canvasName": "ipam_prefixes_available_ips_create",
            "summary": "Assign Mgmt IP",
            "description": "Post a IP address object.",
            "location": "Adapter",
            "locationType": "NetBox:4.1",
            "app": "NetBox:4.1",
            "type": "automatic",
            "displayName": "NetBox",
            "variables": {
              "incoming": {
                "id": 1,
                "bodyContentType": "application/json",
                "requestBodyPayload": "$var.4e80.payload",
                "X-NetBox-Branch": "$var.1de4.return_data",
                "adapter_id": "NetBox"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 540
            }
          },
          "a6ca": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Device Interface List",
            "description": "Perform a JSON Transformation using the JST library.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "67341cedfaaef76ad59b308a",
                "variableMap": {
                  "deviceId": "$var.9147.return_data",
                  "interfacePrefix": "$var.job.interfacePrefix",
                  "interfaceConcatenator": "",
                  "interfaceType": "$var.job.interfaceType",
                  "enabled": true,
                  "interfaceCount": "$var.job.interfaceCount"
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "interfaceList": null
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 36
            }
          },
          "4e80": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "IP Assignment",
            "description": "Perform a JSON Transformation using the JST library.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "67341cedfaaef76ad59b308c",
                "variableMap": {
                  "status": "active",
                  "description": "management",
                  "comments": "$var.job._id",
                  "interfaceID": "$var.5630.return_data"
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "payload": null
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 420
            }
          },
          "2f14": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Merge Branch",
            "description": "Displays a message and runtime data to an operator. This can be used to request a decision, or used for acknowledgement only.",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Merge Branch?",
                "message": "",
                "body": "<p>Please click <a href=\"https://demo.netbox.dev/plugins/branching/branches/<!id!>\"target=\"_blank\">here</a> to review the branch and decide if to merge or delete it.</p>",
                "variables": "$var.7fc6.return_data",
                "btn_success": "Merge",
                "btn_failure": "Delete"
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 744
            }
          },
          "cb9c": {
            "name": "plugins_branching_branches_merge_create",
            "canvasName": "plugins_branching_branches_merge_create",
            "summary": "Merge Branch",
            "description": "Enqueue a background job to merge a branch.",
            "location": "Adapter",
            "locationType": "NetBox:4.1",
            "app": "NetBox:4.1",
            "type": "automatic",
            "displayName": "NetBox",
            "variables": {
              "incoming": {
                "id": "$var.e561.return_data",
                "bodyContentType": "application/json",
                "requestBodyPayload": {
                  "commit": true
                },
                "X-NetBox-Branch": "",
                "adapter_id": "NetBox"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -180,
              "y": 864
            }
          },
          "0a68": {
            "name": "plugins_branching_branches_destroy",
            "canvasName": "plugins_branching_branches_destroy",
            "summary": "Delete Branch",
            "description": "Delete a branch object.",
            "location": "Adapter",
            "locationType": "NetBox:4.1",
            "app": "NetBox:4.1",
            "type": "automatic",
            "displayName": "NetBox",
            "variables": {
              "incoming": {
                "id": "$var.e561.return_data",
                "X-NetBox-Branch": "",
                "adapter_id": "NetBox"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 156,
              "y": 864
            }
          },
          "51ac": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Branch Payload",
            "description": "Perform a JSON Transformation using the JST library.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "67341cedfaaef76ad59b308d",
                "variableMap": {
                  "name": "$var.job._id",
                  "branchDescription": "$var.job.branchDescription",
                  "comments": "$var.job._id"
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "payload": null
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -576
            }
          },
          "f7d6": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Device Payload",
            "description": "Perform a JSON Transformation using the JST library.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "67341cedfaaef76ad59b308f",
                "variableMap": {
                  "name": "$var.job.deviceName",
                  "deviceTypeId": "$var.job.deviceTypeId",
                  "deviceRoleId": "$var.job.deviceRoleId",
                  "siteId": "$var.job.siteId",
                  "deviceStatus": "active",
                  "deviceDescription": "$var.job.deviceDescription",
                  "comments": "$var.job._id"
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": false,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "payload": null
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -276
            }
          },
          "bbc3": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Device Interface Query",
            "description": "Perform a JSON Transformation using the JST library.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "67341cedfaaef76ad59b3090",
                "variableMap": {
                  "interfacePrefix": "$var.job.interfacePrefix",
                  "interfaceConcatenator": ""
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "deviceInterfaceQuery": null
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 228
            }
          },
          "7fc6": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query Branch Body",
            "description": "Query data using a dot/bracket notation string and a matching key/value pair.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "body",
                "obj": "$var.84e8.response"
              },
              "outgoing": {
                "return_data": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -156,
              "y": 636
            }
          },
          "e561": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query Branch ID",
            "description": "Query data using a dot/bracket notation string and a matching key/value pair.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "body.id",
                "obj": "$var.84e8.response"
              },
              "outgoing": {
                "return_data": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 156,
              "y": 636
            }
          }
        },
        "transitions": {
          "5630": {
            "4e80": {
              "state": "success",
              "type": "standard"
            }
          },
          "9147": {
            "a6ca": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_start": {
            "51ac": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "84e8": {
            "1de4": {
              "state": "success",
              "type": "standard"
            }
          },
          "1de4": {
            "f7d6": {
              "state": "success",
              "type": "standard"
            }
          },
          "8c57": {
            "9147": {
              "state": "success",
              "type": "standard"
            },
            "400b": {
              "type": "standard",
              "state": "error"
            }
          },
          "400b": {
            "1de4": {
              "state": "success",
              "type": "revert"
            }
          },
          "30af": {
            "bbc3": {
              "state": "success",
              "type": "standard"
            }
          },
          "bd41": {
            "7fc6": {
              "state": "success",
              "type": "standard"
            },
            "e561": {
              "state": "success",
              "type": "standard"
            }
          },
          "a6ca": {
            "30af": {
              "state": "success",
              "type": "standard"
            }
          },
          "4e80": {
            "bd41": {
              "state": "success",
              "type": "standard"
            }
          },
          "2f14": {
            "cb9c": {
              "state": "success",
              "type": "standard"
            },
            "0a68": {
              "type": "standard",
              "state": "failure"
            }
          },
          "cb9c": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "0a68": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "51ac": {
            "84e8": {
              "state": "success",
              "type": "standard"
            }
          },
          "f7d6": {
            "8c57": {
              "state": "success",
              "type": "standard"
            }
          },
          "bbc3": {
            "5630": {
              "state": "success",
              "type": "standard"
            }
          },
          "7fc6": {
            "2f14": {
              "state": "success",
              "type": "standard"
            }
          },
          "e561": {
            "2f14": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "interfacePrefix": {
              "type": "string",
              "examples": ["eth0/0/"]
            },
            "interfaceType": {
              "type": "string",
              "examples": ["1000base-t"]
            },
            "interfaceCount": {
              "type": "number",
              "examples": [10]
            },
            "_id": {
              "type": "string",
              "examples": ["comments test"]
            },
            "branchDescription": {
              "type": "string",
              "examples": ["description"]
            },
            "deviceName": {
              "type": "string",
              "examples": ["device-name"]
            },
            "deviceTypeId": {
              "type": "number",
              "examples": [1]
            },
            "deviceRoleId": {
              "type": "number",
              "examples": [1]
            },
            "siteId": {
              "type": "number",
              "examples": [1]
            },
            "deviceDescription": {
              "type": "string",
              "examples": ["my descr"]
            }
          },
          "required": [
            "interfacePrefix",
            "interfaceType",
            "interfaceCount",
            "_id",
            "branchDescription",
            "deviceName",
            "deviceTypeId",
            "deviceRoleId",
            "siteId",
            "deviceDescription"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "interfacePrefix": {
              "type": "string",
              "examples": ["eth0/0/"]
            },
            "interfaceType": {
              "type": "string",
              "examples": ["1000base-t"]
            },
            "interfaceCount": {
              "type": "number",
              "examples": [10]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "branchDescription": {
              "type": "string",
              "examples": ["description"]
            },
            "deviceName": {
              "type": "string",
              "examples": ["device-name"]
            },
            "deviceTypeId": {
              "type": "number",
              "examples": [1]
            },
            "deviceRoleId": {
              "type": "number",
              "examples": [1]
            },
            "siteId": {
              "type": "number",
              "examples": [1]
            },
            "deviceDescription": {
              "type": "string",
              "examples": ["my descr"]
            },
            "initiator": {
              "type": "string"
            }
          }
        },
        "type": "automation",
        "font_size": 12,
        "last_updated": "2025-01-24T11:03:15.607Z",
        "lastUpdatedVersion": "4.69.3-2023.2.146",
        "createdVersion": "5.55.2-2023.2.5",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "2024-11-13T03:12:29.075Z",
        "created_by": {
          "provenance": "Local AAA",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": true
        },
        "canvasVersion": 3,
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 5,
      "reference": "67341cedfaaef76ad59b308e",
      "type": "transformation",
      "folder": "/Assign Next IP (in Prefix)",
      "document": {
        "_id": "67341cedfaaef76ad59b308e",
        "name": "Build IP Assignment Payload",
        "description": "",
        "incoming": [
          {
            "$id": "netboxIpResponse",
            "type": "object",
            "properties": {
              "response": {
                "type": "array"
              }
            },
            "required": []
          },
          {
            "$id": "ipStatus",
            "type": "string"
          },
          {
            "$id": "dnsName",
            "type": "string"
          }
        ],
        "outgoing": [
          {
            "$id": "nextIpFound",
            "type": "boolean"
          },
          {
            "$id": "ipAssignmentPayload",
            "type": "object",
            "properties": {
              "address": {
                "type": "string",
                "examples": ["50%2E1%2E0%2E3/20"]
              },
              "status": {
                "type": "string",
                "examples": ["active"]
              },
              "dns_name": {
                "type": "string",
                "examples": ["host%2Eone%2Elocal"]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 1,
            "type": "method",
            "library": "Array",
            "method": "getIndex",
            "args": [null, 0],
            "view": {
              "row": 2,
              "col": 1
            }
          },
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "netboxIpResponse",
              "ptr": "/response"
            },
            "to": {
              "location": "method",
              "name": 1,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 4,
            "type": "method",
            "library": "Array",
            "method": "length",
            "args": [null],
            "view": {
              "row": 1,
              "col": 1
            }
          },
          {
            "id": 5,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "netboxIpResponse",
              "ptr": "/response"
            },
            "to": {
              "location": "method",
              "name": 4,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 6,
            "type": "declaration",
            "library": "Boolean",
            "method": "new Boolean",
            "args": [null],
            "view": {
              "row": 1,
              "col": 2
            }
          },
          {
            "id": 7,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 4,
              "ptr": "/return"
            },
            "to": {
              "location": "declaration",
              "name": 6,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 12,
            "type": "method",
            "library": "Object",
            "method": "optional chaining",
            "args": [null, "address"],
            "view": {
              "row": 2,
              "col": 2
            }
          },
          {
            "id": 13,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 1,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 12,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 16,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "dnsName",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "ipAssignmentPayload",
              "ptr": "/dns_name"
            }
          },
          {
            "id": 17,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "ipStatus",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "ipAssignmentPayload",
              "ptr": "/status"
            }
          },
          {
            "id": 18,
            "type": "assign",
            "from": {
              "location": "declaration",
              "name": 6,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "nextIpFound",
              "ptr": ""
            }
          },
          {
            "id": 19,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 12,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "ipAssignmentPayload",
              "ptr": "/address"
            }
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 3,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.270Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.606Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 6,
      "reference": "67341cedfaaef76ad59b3088",
      "type": "transformation",
      "folder": "/Create Prefix",
      "document": {
        "_id": "67341cedfaaef76ad59b3088",
        "name": "Build Prefix Creation Payload",
        "description": "",
        "incoming": [
          {
            "$id": "prefix",
            "type": "string"
          },
          {
            "$id": "prefixStatus",
            "type": "string"
          },
          {
            "$id": "prefixDescription",
            "type": "string"
          }
        ],
        "outgoing": [
          {
            "$id": "prefixCreationPayload",
            "type": "object",
            "properties": {
              "prefix": {
                "type": "string"
              },
              "status": {
                "type": "string"
              },
              "description": {
                "type": "string"
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 1,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "prefix",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "prefixCreationPayload",
              "ptr": "/prefix"
            }
          },
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "prefixStatus",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "prefixCreationPayload",
              "ptr": "/status"
            }
          },
          {
            "id": 3,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "prefixDescription",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "prefixCreationPayload",
              "ptr": "/description"
            }
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 3,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.269Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.607Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 7,
      "reference": "67341cedfaaef76ad59b3089",
      "type": "transformation",
      "folder": "/Delete Prefix",
      "document": {
        "_id": "67341cedfaaef76ad59b3089",
        "name": "Delete Prefix",
        "description": "",
        "incoming": [
          {
            "$id": "prefixResponse",
            "type": "object",
            "properties": {
              "response": {
                "type": "object",
                "properties": {
                  "results": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer"
                        }
                      },
                      "required": []
                    }
                  }
                },
                "required": []
              }
            },
            "required": []
          },
          {
            "$id": "ipAddressResponse",
            "type": "object",
            "properties": {
              "response": {
                "type": "object",
                "properties": {
                  "count": {
                    "type": "integer"
                  },
                  "results": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "address": {
                          "type": "string"
                        }
                      },
                      "required": []
                    }
                  }
                },
                "required": []
              }
            },
            "required": []
          },
          {
            "$id": "adapterId",
            "type": "string",
            "examples": ["NetBox"]
          }
        ],
        "outgoing": [
          {
            "$id": "prefixId",
            "type": "string"
          },
          {
            "$id": "prefixHasIps",
            "type": "boolean"
          },
          {
            "$id": "ipsInPrefix",
            "type": "array"
          },
          {
            "$id": "ipMessage",
            "type": "string"
          }
        ],
        "steps": [
          {
            "id": 1,
            "type": "declaration",
            "library": "Boolean",
            "method": "new Boolean",
            "args": [null],
            "view": {
              "row": 2,
              "col": 1
            }
          },
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "ipAddressResponse",
              "ptr": "/response/count"
            },
            "to": {
              "location": "declaration",
              "name": 1,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 3,
            "type": "assign",
            "from": {
              "location": "declaration",
              "name": 1,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "prefixHasIps",
              "ptr": ""
            }
          },
          {
            "id": 4,
            "type": "method",
            "library": "Array",
            "method": "map",
            "args": [null, "getIpStrings"],
            "view": {
              "row": 4,
              "col": 1
            }
          },
          {
            "id": 5,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "ipAddressResponse",
              "ptr": "/response/results"
            },
            "to": {
              "location": "method",
              "name": 4,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 7,
            "type": "method",
            "library": "Array",
            "method": "join",
            "args": [null, "\n"],
            "view": {
              "row": 4,
              "col": 2
            }
          },
          {
            "id": 8,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 4,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 7,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 10,
            "type": "method",
            "library": "String",
            "method": "concat",
            "args": [
              "The following IP addresses exist in this prefix.  Delete them as well?",
              "\n",
              null
            ],
            "view": {
              "row": 4,
              "col": 3
            }
          },
          {
            "id": 12,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 10,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "ipMessage",
              "ptr": ""
            }
          },
          {
            "id": 13,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 7,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 10,
              "ptr": "/args/2/value"
            }
          },
          {
            "id": 15,
            "type": "method",
            "library": "Array",
            "method": "map",
            "args": [null, "getIpObjects", null],
            "view": {
              "row": 3,
              "col": 1
            }
          },
          {
            "id": 16,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "ipAddressResponse",
              "ptr": "/response/results"
            },
            "to": {
              "location": "method",
              "name": 15,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 17,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 15,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "ipsInPrefix",
              "ptr": ""
            }
          },
          {
            "id": 18,
            "type": "method",
            "library": "Array",
            "method": "getIndex",
            "args": [null, 0],
            "view": {
              "row": 1,
              "col": 1
            }
          },
          {
            "id": 19,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "prefixResponse",
              "ptr": "/response/results"
            },
            "to": {
              "location": "method",
              "name": 18,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 20,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "id"],
            "view": {
              "row": 1,
              "col": 2
            }
          },
          {
            "id": 21,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 18,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 20,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 22,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 20,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "prefixId",
              "ptr": ""
            }
          },
          {
            "id": 23,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "adapterId",
              "ptr": ""
            },
            "to": {
              "location": "method",
              "name": 15,
              "ptr": "/args/2/value"
            },
            "context": "#"
          }
        ],
        "functions": [
          {
            "incoming": [
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "address": {
                    "type": "string"
                  }
                },
                "required": [],
                "$id": "currentValue"
              },
              {
                "title": "index",
                "type": "number",
                "optional": true,
                "$id": "index"
              },
              {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "address": {
                      "type": "string"
                    }
                  },
                  "required": []
                },
                "$id": "array",
                "optional": true
              }
            ],
            "outgoing": [
              {
                "title": "newValue",
                "type": [
                  "array",
                  "boolean",
                  "number",
                  "integer",
                  "string",
                  "object",
                  "null"
                ],
                "editable": true,
                "$id": "newValue"
              }
            ],
            "steps": [
              {
                "id": 1,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": "/address"
                },
                "to": {
                  "location": "outgoing",
                  "name": "newValue",
                  "ptr": ""
                }
              }
            ],
            "functions": [],
            "name": "getIpStrings",
            "view": {
              "col": 1,
              "row": 5
            },
            "id": "getIpStrings",
            "comments": []
          },
          {
            "incoming": [
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "address": {
                    "type": "string"
                  }
                },
                "required": [],
                "$id": "currentValue"
              },
              {
                "title": "index",
                "type": "number",
                "optional": true,
                "$id": "index"
              },
              {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "address": {
                      "type": "string"
                    }
                  },
                  "required": []
                },
                "$id": "array",
                "optional": true
              },
              {
                "$id": "constantValue1",
                "type": "string",
                "isConstValue": true
              }
            ],
            "outgoing": [
              {
                "$id": "newValue",
                "type": "object",
                "properties": {
                  "ipAddress": {
                    "type": "string",
                    "examples": ["0.0.0.0"]
                  },
                  "adapterId": {
                    "type": "string",
                    "examples": ["NetBox"]
                  }
                },
                "required": []
              }
            ],
            "steps": [
              {
                "id": 1,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": "/address"
                },
                "to": {
                  "location": "outgoing",
                  "name": "newValue",
                  "ptr": "/ipAddress"
                },
                "context": "#"
              },
              {
                "id": 2,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "constantValue1",
                  "ptr": ""
                },
                "to": {
                  "location": "outgoing",
                  "name": "newValue",
                  "ptr": "/adapterId"
                },
                "context": "#"
              }
            ],
            "functions": [],
            "name": "getIpObjects",
            "view": {
              "col": 2,
              "row": 5
            },
            "id": "getIpObjects",
            "comments": []
          }
        ],
        "comments": [],
        "view": {
          "col": 3,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.273Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.625Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 11,
      "reference": "67341cedfaaef76ad59b308b",
      "type": "transformation",
      "folder": "/Sample Use Cases/Onboard Device in Branch/Templates",
      "document": {
        "_id": "67341cedfaaef76ad59b308b",
        "name": "Device Interface",
        "description": "",
        "incoming": [
          {
            "$id": "deviceId",
            "type": "number"
          },
          {
            "$id": "interfaceName",
            "type": "string"
          },
          {
            "$id": "interfaceType",
            "type": "string"
          },
          {
            "$id": "enabled",
            "type": "boolean"
          }
        ],
        "outgoing": [
          {
            "$id": "payload",
            "type": "object",
            "properties": {
              "device": {
                "type": "number",
                "examples": [2]
              },
              "name": {
                "type": "string",
                "examples": ["eth0/0/[0-23]"]
              },
              "type": {
                "type": "string",
                "examples": ["1000base-t"]
              },
              "enabled": {
                "type": "boolean",
                "examples": [true, false]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 1,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "enabled",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/enabled"
            },
            "context": "#"
          },
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceType",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/type"
            },
            "context": "#"
          },
          {
            "id": 3,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceName",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/name"
            },
            "context": "#"
          },
          {
            "id": 4,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "deviceId",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/device"
            },
            "context": "#"
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 2,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.274Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.608Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 12,
      "reference": "67341cedfaaef76ad59b308a",
      "type": "transformation",
      "folder": "/Sample Use Cases/Onboard Device in Branch/Templates",
      "document": {
        "_id": "67341cedfaaef76ad59b308a",
        "name": "Device Interface List",
        "description": "",
        "incoming": [
          {
            "$id": "deviceId",
            "type": "number",
            "examples": [2]
          },
          {
            "$id": "interfacePrefix",
            "type": "string",
            "examples": ["eth0/0/"]
          },
          {
            "$id": "interfaceConcatenator",
            "type": "string",
            "examples": [""]
          },
          {
            "$id": "interfaceType",
            "type": "string",
            "examples": ["1000base-t"]
          },
          {
            "$id": "enabled",
            "type": "boolean",
            "examples": [true, false]
          },
          {
            "$id": "interfaceCount",
            "type": "number",
            "examples": [10]
          }
        ],
        "outgoing": [
          {
            "$id": "interfaceList",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "device": {
                  "type": "integer",
                  "examples": [2]
                },
                "name": {
                  "type": "string",
                  "examples": ["eth0/0/[0-23]"]
                },
                "type": {
                  "type": "string",
                  "examples": ["1000base-t"]
                },
                "enabled": {
                  "type": "boolean",
                  "examples": [true, false]
                }
              },
              "required": []
            }
          }
        ],
        "steps": [
          {
            "id": 17,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "deviceId",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 16,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 18,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfacePrefix",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 16,
              "ptr": "/args/1/value"
            },
            "context": "#"
          },
          {
            "id": 19,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceConcatenator",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 16,
              "ptr": "/args/2/value"
            },
            "context": "#"
          },
          {
            "id": 20,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceType",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 16,
              "ptr": "/args/3/value"
            },
            "context": "#"
          },
          {
            "id": 21,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "enabled",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 16,
              "ptr": "/args/4/value"
            },
            "context": "#"
          },
          {
            "id": 27,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceCount",
              "ptr": ""
            },
            "to": {
              "location": "method",
              "name": 25,
              "ptr": "/args/3/value"
            },
            "context": "#"
          },
          {
            "id": 30,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceCount",
              "ptr": ""
            },
            "to": {
              "location": "declaration",
              "name": 29,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 29,
            "type": "declaration",
            "library": "Array",
            "method": "new Array",
            "args": [null],
            "view": {
              "row": 1,
              "col": 2
            },
            "context": "#",
            "polymorphIndex": 1
          },
          {
            "id": 31,
            "type": "assign",
            "from": {
              "location": "declaration",
              "name": 29,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 25,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 16,
            "type": "template",
            "library": "String",
            "method": "templateLiteral",
            "template": "{\n    \"device\": ${deviceId},\n    \"name\": \"${interfacePrefix}${interfaceConcatenator}\",\n    \"type\": \"${interfaceType}\",\n    \"enabled\": ${enabled}\n}",
            "args": [null, null, null, null, null],
            "view": {
              "row": 1,
              "col": 1
            },
            "context": "#"
          },
          {
            "id": 24,
            "type": "assign",
            "from": {
              "location": "template",
              "name": 16,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 23,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 23,
            "type": "method",
            "library": "JSON",
            "method": "parse",
            "args": [null, null],
            "view": {
              "row": 2,
              "col": 1
            },
            "context": "#"
          },
          {
            "id": 26,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 23,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 25,
              "ptr": "/args/1/value"
            },
            "context": "#"
          },
          {
            "id": 25,
            "type": "method",
            "library": "Array",
            "method": "fill",
            "args": [null, null, 0, null],
            "view": {
              "row": 2,
              "col": 2
            },
            "context": "#"
          },
          {
            "id": 33,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 25,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 32,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 32,
            "type": "method",
            "library": "Array",
            "method": "map",
            "args": [null, "ƒ_map_1"],
            "view": {
              "row": 3,
              "col": 2
            },
            "context": "#"
          },
          {
            "id": 34,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 32,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "interfaceList",
              "ptr": ""
            },
            "context": "#"
          }
        ],
        "functions": [
          {
            "incoming": [
              {
                "type": [
                  "array",
                  "boolean",
                  "number",
                  "integer",
                  "string",
                  "object",
                  "null"
                ],
                "$id": "currentValue"
              },
              {
                "title": "index",
                "type": "number",
                "optional": true,
                "$id": "index"
              },
              {
                "type": "array",
                "$id": "array",
                "optional": true
              }
            ],
            "outgoing": [
              {
                "$id": "interface",
                "type": "object",
                "properties": {
                  "device": {
                    "type": "number",
                    "examples": [2]
                  },
                  "name": {
                    "type": "string",
                    "examples": ["eth0/0/0"]
                  },
                  "type": {
                    "type": "string",
                    "examples": ["1000base-t"]
                  },
                  "enabled": {
                    "type": "boolean",
                    "examples": [true, false]
                  }
                },
                "required": []
              }
            ],
            "steps": [
              {
                "id": 5,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": ""
                },
                "to": {
                  "location": "method",
                  "name": 4,
                  "ptr": "/args/0/value"
                },
                "context": "#"
              },
              {
                "id": 8,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "index",
                  "ptr": ""
                },
                "to": {
                  "location": "method",
                  "name": 7,
                  "ptr": "/args/0/value"
                },
                "context": "#"
              },
              {
                "id": 11,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": ""
                },
                "to": {
                  "location": "method",
                  "name": 10,
                  "ptr": "/args/0/value"
                },
                "context": "#"
              },
              {
                "id": 4,
                "type": "method",
                "library": "Object",
                "method": "getProperty",
                "args": [null, "name"],
                "view": {
                  "row": 1,
                  "col": 1
                },
                "context": "#"
              },
              {
                "id": 7,
                "type": "method",
                "library": "Number",
                "method": "toString",
                "args": [null, null],
                "view": {
                  "row": 2,
                  "col": 1
                },
                "context": "#"
              },
              {
                "id": 6,
                "type": "assign",
                "from": {
                  "location": "method",
                  "name": 4,
                  "ptr": "/return"
                },
                "to": {
                  "location": "method",
                  "name": 3,
                  "ptr": "/args/0/value"
                },
                "context": "#"
              },
              {
                "id": 9,
                "type": "assign",
                "from": {
                  "location": "method",
                  "name": 7,
                  "ptr": "/return"
                },
                "to": {
                  "location": "method",
                  "name": 3,
                  "ptr": "/args/1/value"
                },
                "context": "#"
              },
              {
                "id": 3,
                "type": "method",
                "library": "String",
                "method": "concat",
                "args": [null, null],
                "view": {
                  "row": 3,
                  "col": 1
                },
                "context": "#"
              },
              {
                "id": 12,
                "type": "assign",
                "from": {
                  "location": "method",
                  "name": 3,
                  "ptr": "/return"
                },
                "to": {
                  "location": "method",
                  "name": 10,
                  "ptr": "/args/2/value"
                },
                "context": "#"
              },
              {
                "id": 10,
                "type": "method",
                "library": "Object",
                "method": "setProperty",
                "args": [null, "name", null],
                "view": {
                  "row": 2,
                  "col": 2
                },
                "context": "#"
              },
              {
                "id": 13,
                "type": "assign",
                "from": {
                  "location": "method",
                  "name": 10,
                  "ptr": "/return"
                },
                "to": {
                  "location": "outgoing",
                  "name": "interface",
                  "ptr": ""
                },
                "context": "#"
              }
            ],
            "functions": [],
            "name": "ƒ_map_1",
            "view": {
              "col": 2,
              "row": 4
            },
            "id": "ƒ_map_1",
            "comments": []
          }
        ],
        "comments": [],
        "view": {
          "col": 2,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.276Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.611Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 13,
      "reference": "67341cedfaaef76ad59b308c",
      "type": "transformation",
      "folder": "/Sample Use Cases/Onboard Device in Branch/Templates",
      "document": {
        "_id": "67341cedfaaef76ad59b308c",
        "name": "IP Assignment",
        "description": "",
        "incoming": [
          {
            "$id": "status",
            "type": "string",
            "examples": ["active"]
          },
          {
            "$id": "description",
            "type": "string",
            "examples": ["description test"]
          },
          {
            "$id": "comments",
            "type": "string",
            "examples": ["comments test"]
          },
          {
            "$id": "interfaceID",
            "type": "number",
            "examples": [9223372036854776000]
          }
        ],
        "outgoing": [
          {
            "$id": "payload",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "status": {
                  "type": "string",
                  "examples": ["active"]
                },
                "description": {
                  "type": "string",
                  "examples": ["management"]
                },
                "comments": {
                  "type": "string",
                  "examples": ["set from IAP"]
                },
                "interface": {
                  "type": "number",
                  "examples": [9223372036854776000]
                }
              },
              "required": []
            }
          }
        ],
        "steps": [
          {
            "id": 7,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "status",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 6,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 8,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "description",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 6,
              "ptr": "/args/1/value"
            },
            "context": "#"
          },
          {
            "id": 9,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "comments",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 6,
              "ptr": "/args/2/value"
            },
            "context": "#"
          },
          {
            "id": 10,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceID",
              "ptr": ""
            },
            "to": {
              "location": "template",
              "name": 6,
              "ptr": "/args/3/value"
            },
            "context": "#"
          },
          {
            "id": 6,
            "type": "template",
            "library": "String",
            "method": "templateLiteral",
            "template": "  {\n    \"status\": \"${status}\",\n    \"description\": \"${description}\",\n    \"comments\": \"${comments}\",\n    \"interface\": ${objectid}\n  }\n",
            "args": [null, null, null, null],
            "view": {
              "row": 1,
              "col": 1
            },
            "context": "#"
          },
          {
            "id": 15,
            "type": "assign",
            "from": {
              "location": "template",
              "name": 6,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 14,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 14,
            "type": "method",
            "library": "JSON",
            "method": "parse",
            "args": [null, null],
            "view": {
              "row": 2,
              "col": 1
            },
            "context": "#"
          },
          {
            "id": 16,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 14,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 11,
              "ptr": "/args/1/value"
            },
            "context": "#"
          },
          {
            "id": 11,
            "type": "method",
            "library": "Array",
            "method": "push",
            "args": [[], null],
            "view": {
              "row": 1,
              "col": 2
            },
            "context": "#"
          },
          {
            "id": 13,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 11,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": ""
            },
            "context": "#"
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 2,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.277Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.608Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 14,
      "reference": "67341cedfaaef76ad59b308d",
      "type": "transformation",
      "folder": "/Sample Use Cases/Onboard Device in Branch/Templates",
      "document": {
        "_id": "67341cedfaaef76ad59b308d",
        "name": "Branch Creation",
        "description": "",
        "incoming": [
          {
            "$id": "name",
            "type": "string",
            "examples": ["branch1-new"]
          },
          {
            "$id": "branchDescription",
            "type": "string",
            "examples": ["description"]
          },
          {
            "$id": "comments",
            "type": "string",
            "examples": ["comments"]
          }
        ],
        "outgoing": [
          {
            "$id": "payload",
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "examples": ["branch1-new"]
              },
              "description": {
                "type": "string",
                "examples": ["string"]
              },
              "comments": {
                "type": "string",
                "examples": ["string"]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 1,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "name",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/name"
            },
            "context": "#"
          },
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "branchDescription",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/description"
            },
            "context": "#"
          },
          {
            "id": 3,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "comments",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/comments"
            },
            "context": "#"
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 1,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.275Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.610Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 15,
      "reference": "67341cedfaaef76ad59b308f",
      "type": "transformation",
      "folder": "/Sample Use Cases/Onboard Device in Branch/Templates",
      "document": {
        "_id": "67341cedfaaef76ad59b308f",
        "name": "Device Create",
        "description": "",
        "incoming": [
          {
            "$id": "name",
            "type": "string",
            "examples": ["device-name"]
          },
          {
            "$id": "deviceTypeId",
            "type": "number",
            "examples": [1]
          },
          {
            "$id": "deviceRoleId",
            "type": "number",
            "examples": [1]
          },
          {
            "$id": "siteId",
            "type": "number",
            "examples": [1]
          },
          {
            "$id": "deviceStatus",
            "type": "string",
            "examples": ["offline"]
          },
          {
            "$id": "deviceDescription",
            "type": "string",
            "examples": ["my descr"]
          },
          {
            "$id": "comments",
            "type": "string",
            "examples": ["my comments"]
          }
        ],
        "outgoing": [
          {
            "$id": "payload",
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "examples": ["new3"]
              },
              "device_type": {
                "type": "number",
                "examples": [1]
              },
              "role": {
                "type": "number",
                "examples": [1]
              },
              "site": {
                "type": "number",
                "examples": [1]
              },
              "status": {
                "type": "string",
                "examples": ["offline"]
              },
              "description": {
                "type": "string",
                "examples": ["my descr"]
              },
              "comments": {
                "type": "string",
                "examples": ["my comments"]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 1,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "name",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/name"
            },
            "context": "#"
          },
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "deviceTypeId",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/device_type"
            },
            "context": "#"
          },
          {
            "id": 3,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "deviceRoleId",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/role"
            },
            "context": "#"
          },
          {
            "id": 4,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "siteId",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/site"
            },
            "context": "#"
          },
          {
            "id": 5,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "deviceStatus",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/status"
            },
            "context": "#"
          },
          {
            "id": 6,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "deviceDescription",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/description"
            },
            "context": "#"
          },
          {
            "id": 7,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "comments",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "payload",
              "ptr": "/comments"
            },
            "context": "#"
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 2,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.279Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.612Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 16,
      "reference": "67341cedfaaef76ad59b3090",
      "type": "transformation",
      "folder": "/Sample Use Cases/Onboard Device in Branch",
      "document": {
        "_id": "67341cedfaaef76ad59b3090",
        "name": "Device Interface Query",
        "description": "",
        "incoming": [
          {
            "$id": "interfacePrefix",
            "type": "string",
            "examples": ["eth0/1/"]
          },
          {
            "$id": "interfaceConcatenator",
            "type": "string",
            "examples": [""]
          }
        ],
        "outgoing": [
          {
            "$id": "deviceInterfaceQuery",
            "type": "string",
            "examples": ["body[display="]
          }
        ],
        "steps": [
          {
            "id": 1,
            "type": "method",
            "library": "String",
            "method": "concat",
            "args": ["body[display=", null, null, "0].id"],
            "view": {
              "row": 1,
              "col": 1
            },
            "context": "#"
          },
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfacePrefix",
              "ptr": ""
            },
            "to": {
              "location": "method",
              "name": 1,
              "ptr": "/args/1/value"
            },
            "context": "#"
          },
          {
            "id": 3,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "interfaceConcatenator",
              "ptr": ""
            },
            "to": {
              "location": "method",
              "name": 1,
              "ptr": "/args/2/value"
            },
            "context": "#"
          },
          {
            "id": 4,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 1,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "deviceInterfaceQuery",
              "ptr": ""
            },
            "context": "#"
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 1,
          "row": 5
        },
        "created": "2025-01-23T14:21:33.278Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:03:15.612Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 9,
      "reference": "67341ced1ef8108b32e9cb0c",
      "type": "jsonForm",
      "folder": "/Sample Use Cases/Onboard Device in Branch",
      "document": {
        "id": "67341ced1ef8108b32e9cb0c",
        "created": "2024-11-13T03:12:29.071Z",
        "createdBy": "admin@itential",
        "lastUpdated": "2025-01-24T11:03:15.611Z",
        "lastUpdatedBy": "admin@itential",
        "description": "",
        "struct": {
          "type": "array",
          "items": [
            {
              "nodeId": "810cd84a-03ce-42cf-94e4-a2aacef24a3c",
              "type": "string",
              "title": "Branch Description",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default"
            },
            {
              "nodeId": "bc7b1f83-9384-4e41-aa85-e2376950875a",
              "type": "string",
              "title": "Site",
              "description": "",
              "placeholder": "Select an item",
              "required": true,
              "enum": [
                {
                  "id": "47985962-7987-4feb-b0dd-78ec07e19bfc",
                  "label": "1",
                  "value": "1"
                },
                {
                  "id": "b83a3261-755f-41dd-8448-972c24a5d5a1",
                  "label": "2",
                  "value": "2"
                }
              ],
              "enumNames": [
                {
                  "id": "2ea614fe-722c-4aef-8d02-7bac71b7ad84",
                  "label": "Nice",
                  "value": "Nice"
                },
                {
                  "id": "93fbf586-5f46-452d-9d54-2671d766912c",
                  "label": "Manchester",
                  "value": "Manchester"
                }
              ],
              "binding": false,
              "rel": "collection",
              "targetPointer": "/enum",
              "customKey": "siteId"
            },
            {
              "nodeId": "349c6bf8-78c9-4846-a6ac-e1d64d4d163f",
              "type": "string",
              "title": "Device Name",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "customKey": "deviceName"
            },
            {
              "nodeId": "c16f25e8-63a1-47e4-bd61-d6b5a452f078",
              "type": "string",
              "title": "Device Role",
              "description": "",
              "placeholder": "Select an item",
              "required": true,
              "enum": [
                {
                  "id": "eae77f38-0503-4238-b0ba-9725fc04c39a",
                  "label": "1",
                  "value": "1"
                }
              ],
              "enumNames": [
                {
                  "id": "abac6483-dc13-4154-837f-5a5cacbddbd3",
                  "label": "Switch",
                  "value": "Switch"
                }
              ],
              "binding": false,
              "rel": "collection",
              "targetPointer": "/enum",
              "customKey": "deviceRoleId",
              "default": "1"
            },
            {
              "nodeId": "f54509d7-1869-4453-935f-16262877146f",
              "type": "string",
              "title": "Device Type",
              "description": "",
              "placeholder": "Select an item",
              "required": true,
              "enum": [
                {
                  "id": "83922597-761e-4d91-b34b-92a427ac7ff4",
                  "label": "1",
                  "value": "1"
                }
              ],
              "enumNames": [
                {
                  "id": "81006f91-ba77-4af0-9c88-c1fc7fc0a5dc",
                  "label": "Cisco 8000",
                  "value": "Cisco 8000"
                }
              ],
              "binding": false,
              "rel": "collection",
              "targetPointer": "/enum",
              "customKey": "deviceTypeId",
              "default": "1"
            },
            {
              "nodeId": "cf02d743-7c24-423b-97cc-586d3d367b16",
              "type": "string",
              "title": "Device Description",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "customKey": false
            },
            {
              "nodeId": "29650859-082f-40c8-85c6-1af83c301b95",
              "type": "string",
              "title": "Interface Prefix",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "customKey": "interfacePrefix",
              "default": "eth0/0/"
            },
            {
              "nodeId": "8c1cbea8-4b4c-4ecd-96bb-f11b051535c3",
              "type": "string",
              "title": "Interface Type",
              "description": "",
              "placeholder": "Select an item",
              "required": true,
              "enum": [
                {
                  "id": "3be1fe96-0868-4922-a5d6-d9e5ecaf14d5",
                  "label": "1000base-t",
                  "value": "1000base-t"
                }
              ],
              "enumNames": [
                {
                  "id": "a4375a57-4ad7-4417-88c7-689a6cc19957",
                  "label": "",
                  "value": ""
                }
              ],
              "binding": false,
              "rel": "collection",
              "targetPointer": "/enum",
              "customKey": false,
              "default": "1000base-t"
            },
            {
              "nodeId": "02f1ac9d-5905-4e00-8dca-870d6aec2737",
              "type": "number",
              "widget": "updown",
              "title": "Interface Count",
              "description": "",
              "placeholder": "Enter a number",
              "required": true,
              "minimum": 1,
              "maximum": 48,
              "default": 24
            }
          ]
        },
        "schema": {
          "title": "Onboard Device",
          "description": "",
          "type": "object",
          "required": [
            "branchDescription",
            "siteId",
            "deviceName",
            "deviceRoleId",
            "deviceTypeId",
            "deviceDescription",
            "interfacePrefix",
            "interfaceType",
            "interfaceCount"
          ],
          "properties": {
            "branchDescription": {
              "type": "string",
              "title": "Branch Description",
              "_id": "/properties/branchDescription",
              "description": ""
            },
            "siteId": {
              "type": "string",
              "title": "Site",
              "_id": "/properties/siteId",
              "description": "",
              "enum": ["1", "2"],
              "enumNames": ["Nice", "Manchester"]
            },
            "deviceName": {
              "type": "string",
              "title": "Device Name",
              "_id": "/properties/deviceName",
              "description": ""
            },
            "deviceRoleId": {
              "type": "string",
              "title": "Device Role",
              "_id": "/properties/deviceRoleId",
              "description": "",
              "default": "1",
              "enum": ["1"],
              "enumNames": ["Switch"]
            },
            "deviceTypeId": {
              "type": "string",
              "title": "Device Type",
              "_id": "/properties/deviceTypeId",
              "description": "",
              "default": "1",
              "enum": ["1"],
              "enumNames": ["Cisco 8000"]
            },
            "deviceDescription": {
              "type": "string",
              "title": "Device Description",
              "_id": "/properties/deviceDescription",
              "description": ""
            },
            "interfacePrefix": {
              "type": "string",
              "title": "Interface Prefix",
              "_id": "/properties/interfacePrefix",
              "description": "",
              "default": "eth0/0/"
            },
            "interfaceType": {
              "type": "string",
              "title": "Interface Type",
              "_id": "/properties/interfaceType",
              "description": "",
              "default": "1000base-t",
              "enum": ["1000base-t"],
              "enumNames": [""]
            },
            "interfaceCount": {
              "type": "number",
              "title": "Interface Count",
              "_id": "/properties/interfaceCount",
              "description": "",
              "default": 24,
              "minimum": 1,
              "maximum": 48
            }
          }
        },
        "uiSchema": {
          "branchDescription": {
            "ui:placeholder": "Enter text"
          },
          "siteId": {
            "ui:placeholder": "Select an item"
          },
          "deviceName": {
            "ui:placeholder": "Enter text"
          },
          "deviceRoleId": {
            "ui:placeholder": "Select an item"
          },
          "deviceTypeId": {
            "ui:placeholder": "Select an item"
          },
          "deviceDescription": {
            "ui:placeholder": "Enter text"
          },
          "interfacePrefix": {
            "ui:placeholder": "Enter text"
          },
          "interfaceType": {
            "ui:placeholder": "Select an item"
          },
          "interfaceCount": {
            "ui:placeholder": "Enter a number",
            "ui:widget": "updown"
          }
        },
        "bindingSchema": {},
        "validationSchema": {},
        "version": "2020.1",
        "name": "Onboard Device"
      }
    },
    {
      "iid": 10,
      "reference": "67341ceda1c9aed687bfdcdd",
      "type": "template",
      "folder": "/Sample Use Cases/Onboard Device in Branch/Templates",
      "document": {
        "_id": "67341ceda1c9aed687bfdcdd",
        "type": "jinja2",
        "command": "",
        "template": "[\n {% for i in range(0,interfaceCount) %}\n  {\n    \"device\": {{deviceId}},\n    \"name\": \"{{interfacePrefix}}{{i}}\",\n    \"type\": \"{{interfaceType}}\",\n    \"enabled\": {{enabled | lower}}\n  }{{ \",\" if not loop.last }}\n {% endfor %}\n]",
        "name": "Device Interface List",
        "version": 1,
        "data": "{\n    \"deviceId\": 2,\n    \"interfaceType\": \"1000base-t\",\n    \"interfacePrefix\": \"eth0/0/\",\n    \"interfaceCount\": 24,\n    \"enabled\": true\n}",
        "group": "J2",
        "description": "",
        "created": "2024-11-13T03:12:29.077Z",
        "lastUpdated": "2025-01-24T11:03:15.625Z",
        "createdBy": {
          "_id": "6786b32af921f091fd105007",
          "provenance": "Local AAA",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": true
        },
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false
        }
      }
    }
  ],
  "folders": [
    {
      "nodeType": "folder",
      "name": "Create Prefix",
      "children": [
        {
          "iid": 0,
          "nodeType": "component"
        },
        {
          "iid": 6,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Delete Prefix",
      "children": [
        {
          "iid": 1,
          "nodeType": "component"
        },
        {
          "iid": 7,
          "nodeType": "component"
        }
      ]
    },
    {
      "iid": 2,
      "nodeType": "component"
    },
    {
      "iid": 3,
      "nodeType": "component"
    },
    {
      "nodeType": "folder",
      "name": "Assign Next IP (in Prefix)",
      "children": [
        {
          "iid": 5,
          "nodeType": "component"
        },
        {
          "iid": 4,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Sample Use Cases",
      "children": [
        {
          "nodeType": "folder",
          "name": "Onboard Device in Branch",
          "children": [
            {
              "iid": 9,
              "nodeType": "component"
            },
            {
              "iid": 8,
              "nodeType": "component"
            },
            {
              "nodeType": "folder",
              "name": "Templates",
              "children": [
                {
                  "iid": 10,
                  "nodeType": "component"
                },
                {
                  "iid": 11,
                  "nodeType": "component"
                },
                {
                  "iid": 12,
                  "nodeType": "component"
                },
                {
                  "iid": 13,
                  "nodeType": "component"
                },
                {
                  "iid": 14,
                  "nodeType": "component"
                },
                {
                  "iid": 15,
                  "nodeType": "component"
                }
              ]
            },
            {
              "iid": 16,
              "nodeType": "component"
            }
          ]
        }
      ]
    }
  ],
  "created": "2024-08-29T17:59:45.726Z",
  "createdBy": {
    "_id": "6786b32af921f091fd105007",
    "provenance": "Local AAA",
    "username": "admin@itential"
  },
  "lastUpdated": "2025-01-24T11:03:15.574Z",
  "lastUpdatedBy": {
    "_id": "66d1e2b552e6dc384b5d6626",
    "provenance": "Okta",
    "username": "admin@itential"
  },
  "iid": 52,
  "thumbnail": "data:image/png;base64,UklGRv4sAABXRUJQVlA4WAoAAAAQAAAA/wEA0gEAQUxQSHEVAAABHAVt2zAJf9j7QxARE8BP9e6WKNPZtQPBa0ZNvM62x5Es6b8EXgIv4b+BA9DuVWbvnbasdMMrtBWmvC4rkE56ackKq2eLWXLWNNIIoM+SEFBAL4UI9cYUi4z6Zqmuov6o88ev2SoiJsCPbGtzKzvbdjXhasLdBHSAEWgAJD0+nsqqtqUCtortwjkmzds5Hi3xqSxacJ6KDh0VNO5QyQg8CDLyfgDkDZ7QZezMjXVdIPjUT0bEBJCqXdPtniYA4+fbdSDF8/V2/ysAeHp82XiyUtfuUfC+Od03Ogv9lPC+GcPKW4i/Sxkfnse1U1d7yKi59dbhOtTOU6urcDihcu6daYQxVwPyo9eT+4uCGacfGsY6Y96p0RKPmPfUm0V/wtyl1dFVwtxlcDbRF8xfWg21kDg4i+gLJJZWPw1kDs4eNgUyS6MdTkLwF+bQFEidvG7cK0g9rY3BTZD7qJtbCGZb6CE4t5oJWdLeFEKWhMkpZg/JubWEB4jOa72EkyiMhuCzLIx62UN2buxgA+G50YqH9Hs7+L00/EIrPxMHZwWcxE1aGeRdWcEa4nPQiYP8rRXcy8NKJyHJG61gPIOtTtY4QyvAGe51cncGz8EG3Dn8SicPZ5CNIBzPADrZnwEWpqfF73Oz8fkMRp08mA3hDD/XyfYM/mAF0xnsdNKdAZwR7M+g00mT5U1khJ28FHTiIf/eCpokDk4ndJC3sgKS96+k1Ftx2ZtBL620WuEibSAzDCdhyWmFRmG5tQMahHWkVS7CJmcIIYtKTiucIDuvyRIfJeWOlMoJwkdnCizp4JTCCcJLQ7a4PskJpFNOkN6TNe6knFakU06QPjhzcIOM0pNOOUF68mSPbpBQetIpJ0hPTBbphvlOPemUE6RPTDbpdqeZSkc65QThZfBklqt5pkA65QTh5daRYfrHU73ekU45QfbpEMg4w/5UZ+tJqZwgOo8tGWiIFX7pSaucUD1+tnqVP6DgviEbfapwQ1rlhOqRichfb38FPB+PGdP+tnFkpYrihOqR6T05BE+2qidOqB6ZTFdNnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9Mi1hnFA9MtkihxDCJeBCCMG9BydUj0x2GLrHCfl4PD4D+9vGqc1fbX8FHI/HI/Cr3coTESdUj0xW6DdTxvsX3AeNuXbAh+ZXq88SqkcmIwwPGTXz6yttuS5liI5MNui2GbXznlXVThAemWywmTBrpyf3kCE8MtngpmDe8uiUxBOkRyYb7AtmH7yKWoiPTDbYFwiMXkEtxEcmG+wLRA5OPQHiI5MNrk8Q+qgdn8RFJhsMGVJLp5wB0iOTDboRglk1XZEWmYywy5L2mvGQHpmM0CdIzleK2UqLTFa4gezXevEQPjFZoUvCclBLL+3fyAzbLAzxSeQdEMPDfysNzgz+FZf6ygocLvZ7KwjpYoMVdLjYn9kIdpcbGiP4/IJbG8F4wd0YAf7Xv18tfvsL7oURbC+3HIzg+nKDNwJOF9tIVjhdbFsz6C+10phBk6X98kbkvwPO/uEnaRPZ4SjNk8gA8PTwV9I2htBmWTtSi0vCvCHQKCqzXqjLou7IEn94ktSTYtwoaXKmQA+CJqcZaoqcvCJbdJOY0pBq6LaI2ZE1BimlI+W4QcorZw7UFhGlJ+2Qey0jMRlkWwSUnvRDHCUkJpNs53vbk4bIDfNNTEYZprlWpCNyu9M85dGRWbqH0wz5wKQlotWbWToyzR+OpVbqSPq6kd/lWqcHT9bZHnKFkjpHuiIKuyplH8hCm35K75Vwf+XoDFeP6HvPFb5HZsrXd49PAH71+XYd6EyfgHCsEOzko/jFf1/898V/X/z3xX9f/PfFf1/898V/n6gRmhcvb27W18FbynAxcDcg4d05T/dXzkZ8/7bCm87py7WHgg99g22wD7/NqJs6p6z1lFH1tA/G0WHG6YeaCoeC6vnWGYYfyhw49U5NXcasI5tFSJh78DpyDwVzt0bRQuDEGnID5i+tSbQQmVg/boDE0hoEJxkYnHq+gszSmoObIPVBO7dFCN6wNTxAbFnrpikQe3C20GY5gNeMmyA3d6bgJkh+0EwH0d4SOog+Bb14yN4agptk4VEvG2HwdtBmYfhe+Nh/NwK+m4t8I21jBwOkp+PHPv4BEK8S/wTpkxl4XOo5WMHVxYaNFWwvt70VfH65wQpwuWe/9D0HGwjPlxus4Pg//v6w9BEu9+fFL3sjeHW5gYxwe7l9bgVXl9utFfiLLTdWQIO4dPzYxz8A4lXin8RNZIZtEVa+Fz72342A7+YSv5Wl9XbwGYTv6aOfXwE5ibwTlr0ZcBJ2CnrxwnZkhZwg/JH0QhtZ3go4QTprxk2SNmSEnCC8dKQZ+mGRMzoj4ATpX5FuqC9imGyQE6RPTjtuEFJaskFOkJ6YtENuEPH252SDnCA9MemH3CCg3JENcoL0gUlD5L4qc5WWbJAThOedIx0R3ZZ5pkA2yAnCpxV9fS6PwpjrlZ0jG+QE4XeONEWuS5XyPpARckL16W+RPyhPG09fq4+AyK3HXOE+kBVyQvXI5K7up5z/TMbYN/R1+xiIiG9fIf25Z9yvPJkhJ1SPTO/04cXLm5ub7jo4+hp+GETkwnV3c3Nz86JhskROqB6ZVPhIjJITqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkemJYwTqkem5ck16+3D09PT46678u/ghOqRaWnym1fIeM889oE4oXpk0uq3/lThWyYS9hkfnn9XUD0yKdVvMmr23jzCPkN2ZNKp26B670zD3WYIj0w6bSbMOLWGwa8gPTLp9LZg1tNfOKtoEqRHJpW6rwrmHpxNtBAfmVTqBgh8zRbRQHxkUqkbIHJw9sBJXGTS6QOEDs4a3AHSI5NOuyKl9NbwF5AemXQaMsSWxhZCkRaZlHqA4MmZwgHCI5NSV0USOktoT8Iik1LdBNHJGcJrCP8GabXNstDZQThJ69QyQPhkBz2kH7TCRVpuzGASV1gpHcT3VsBFHFZK2csbreAa8ndKwRk6I7g7g1En/CwvByPYnwF0EnCG10bwdA5OJS/O4aUR4AyPQSXrc7hZlm4Wv5d2M57BM6vkhd08nQFIpVfnsDaC3aUQns/gygi6M/hcJw7yUzCCJsu71QmN8kBG6CC+NErZyttbAQ3i4JRyVcStzGAl7p6U6iDem4GTlhut0FbanuxwK2wktXKWlRtD8LJOrV7oQdZAlrgRdSDFsqgSTMFNgkrQDG0k7cgWmyKm3JJq3UHO5IyBbouUwemG+I2UEsgcH4RMnrTbFhmlJXt0g4jEpN+2SHh7RxbphjLfxKThtsxXfk426fo81+BJx22arSWzXM1Tekda5qHMcmAyTP+Yq+WxIU13c2wc2WbzOlcp09qRrv221taTfYZ7lA8aWkf69t2YPyRPG0826q62v8LzM4D8B4z3K09a524PHP/LH4D9JpCtcngnqd+Fd3r65P9P/v/k///bnXPkspYL8HnxO37y3xf//W9tnCOXtVyAz4vf8ZP/Pvnvf6Rw6U8hXt/eQvCVexB55U+hvX6yCydfuqcjq3wI3fVtDGFf54/Elb4JIV7fxhAaX2arlgP5PVy3Ueb23SFfWr4LUeb3fVOxHuczvwvJoQsomzjJ7Bhq9whcfbr1Mj/dznVmxuXgTIlzrHszyvz8c+4wCjZ9qBZUNDfBj02hlcsyR2vucBN031a8LFe3veCnbu9sZAKOTuci0G+yN1eFOorih2IZXHdJdFMoHtHVVvazUVR7z8spz6No96GyQHXCyFllJ9CpIh0+JlG9/yPbYx/FYArZqvFhFPX+dSHVhyQmu8oAHUEfXxWKEfOPpOM6Ue821rZRjKYdr1fZi8lLtoDiksRsLPW4w0h0MO4F2rFOFsXg8GKq+CCG22ytDpMYHbbW+HAXy9PZadFmwMgZdhLosCGVLIrJ4cXQLonpVK4S/1YM/4xNFb1YHystqhPm4yuoTpBUkwp3YnTYWOGLWB9+uELcienOGdomsT8dtOiIkegg2SDQI+kcxWzPNja92P/mh6vDnRiPmRU+yjJ/y0p8w8gZwa1AO9apkx05mygGWWJ6WZufifmY2eDfylI71qEiYT6+AvYCTQWp/HkUw6ky8DLIMofNutxlgR1b4E6We2Ed2mIkulnlHbMlnX8T05HVNlGW2vGqLPNigC+y5Avr0Bkj5zluFOiZlEZbstXKRlnu8emRvd5Rln1hHe4xH19nnAXas5b1qMSdoGMb/NtT6CfYVD4991Lra1n6QYeKBJHo3rUVaCrosciLzlGwsSmZ3pnVbY+Rnp8d6VmnvC8uverQFiPn92wSZkuP5qRSTZDomWa7ZoSIf3rkoMK9LH9wOnTGfHz9HHcCvZCpvj34PM/zyrcjLmrwKMizI2jRQSI/hnEJMey3+Vu/vwwqY6Hxj6I5XPY+f+v3IWpIUOIeItF95h8FOjpLo3f0TteMKPkjhUaA6aeE5p8hxM/hfOZ3Edccai4dS3o3V2HESVAo7rjxXDG9uzyOuI+VDhUJIudPVRPkXpKdccc0s0gojytGQKpJsUFEnjE7h5BJpbFxND/72R2WCtwHQd+Pjua7ZkRJzzq0xXx8feMGge7IzljQ/E0CBVwQ4IE0+QKQ1/W5ZIQtOpQEWCXotiDs5oISr0RniERHRBeBXshOzAhZJMwNViTAhXRdBLRrc98RnJsEmjJUB0oHJvjuDoqsxD1EzkQ7gQ7OzrAhrMdERp1lfsqUaAuYsnUZKtLc3jHSgCrBflOTZjVgZKtERYJ8fC1GyFSRmakiMEeI5CA3Av6B1Lt5sl+V4YV0fzhhImMumPsPSfdlwHRatIVI7AV6IDtngm8xJWgv80entwW0azL9kLS/xkgFyXrMlrR/OEGk1KIzBNyyndHh3ADxoAhoSN/183q3IjvSP2NOkL1AT6R/wDRq3FsZMrJzIsWLnTzNS7kBaudJtR4f2ACPkB7SQUY2wC3kpkZFsjFVZKjU8Hb2Mr8niw2gWY17QRZfIZIDsglSkcViQkipRlsbRzIUWSO30wIaEx7QrkYgmxHiAbUgI9kMkL0enS10bCmQ6tUKR0BtIgdc1yIVRipIAJwglZEiIYIB7vWGDVnyOjcruQDzhaRsJT6QUb4hboAOcSOrERENUJG0Uk2mKp1gZQsYg8kLQMqVqK1Qg4g8i6+IxswWkTIDtNU6kq38IewBy/XrMGVmSoTks3JBlmayBJDSAp11eraVMp2TlfBs9WSWI6KcVSIim6EbwpvgXiMVZOtKun59wjoEO9Qi/CyPaMluWAoVSWFLaxSfLW8oLORkyCNONmiLO9MqXf/j4hfilxWMVBPs8J8i+WNplpUvJhsEPlVPXvsEnWaFVeJWFIfsubs+Qc1TcBDVlv/zo1yWn7VfVrWQatKRw39+eEN7C35ZfhnZIMpTtT79s7U3FBYSDO0RjR63oj5kqxOerWDotpDOUEB4vYMYbPl5i+sQ7bgekc/KEb2zExG1WjVZkMPaeMC48wvdroP8kZlXsZAlgFRmSkHmWtkgJqdqZSqA5PRwH8vBzAlxpflXxMlMg+idErdidMjWJUuA+rm5WXEJEQEtIjkjfEPcSPkgZlteFRoBzXMjlREvyAA4IMQbqQR5UqomO3JYlzPg9uR0NjhCPKCCRLbRQWqdbBDokDBTtSo1QMrnRrYmDgLNATwgZGdiK8iUqXAr2O0RI0O2Jq4HHJ+cwRkoRshIyBYyFgayAdKR6kGwZ+IeIy2vCLWA0Zl4qVdLLqzGvUBPkFeIdKzGrUD3KtWE6ZmoSBg5rMkrQM4WNjEd2UyWAJIvSRotvgi2gnCCyG9ZqxFo7zSyQaBjQUS0BU3VinAETJXeJolIt7FCV0S1KGl0+FeCHRhCDUZ+xTqNYAMpcivYHX3ygpHo1oMOABkyrU2St0O9oOOypGEFvgj4SNhsxMhvWYGPgk2lxkGwF/q0GzFyWRF3B0jMdMpBPp2OvJjIy5I2gxW9gFMBogCSWwHLWgHfSLGaMKP7DJUTRnbrQf+AkLjR2CZ5Z7cxERHiFyaDZwgfRkF/IHQxgmTcMYT9IOBUKmSDQKeS3nkA3cv14IiQoYK5s7x/qC0ESMzmOVki8SuexT4KvoJRgxKJnmfxV73AA+G5FeyB3sstRka3GrSFyHR2mG2UuanhZUiXzXkZrYnEpuR3uOo0iOKN8C7CRIZT5d7BL00UfMoUDoJt+V2UDRi5rAddICL3JpvFr50g20zNYyQ12edcue8k2hORGMPJex/CrRfVqVCgWkFE+lsI3vtT6KOo7ghfTZgho5l1wshuPbKEEelbn/Pn8vo0CHiotGqQSIrhk3EUEbkuwuyRVIOK1ZZx2SDQVNPsI+hergbVCfQ23sLb21U0718p5bC5j2xkHTcuLm4Izq1gjzSfe4yMbjXooGAzshLFlZtKUi7SwqaK8DvBdgygImHksh7820WlDWmHh3FfyD+Q+g/Tsr4mfHnHpA1BPUh2q0HcLWjYkHr9MK63RfyKDH6dltQQ3o2C3RL4ArqXq0HcLWZ4IX03PIzivoCOLdBP03IaUrwI9kxoN2JkdKtBfFlILMli8zBoZ69jsrm9LyQdSHEn2J5h9BcTRi7rQXxMS+g3ZNKND4N+Zq1lsloNi0g1KZZ3zL0gxQNIdutBtE32WkdGd4+Df2XryGR30y1gLEjRjYLdkSa3oHu5IlS0xu4HJqvcPgziXxlKWzLN/zgZm85MmhfBXkh3M2BkdCtC7AdLfUmGs/FhEB0mK21B1svOVF+R6k6wo1OiOmHksiZE7jhaSTsm05v+cVA1mkieyT77aGb0TKrlHTNVpH4CyW5ViPLjaCE1jqy7y+Mgbka1sXG0TPa9ibhzpOtGwR5In3vQvVwXIreLSqnzjpa4HXWiJSLXDCqpcbRcrtpeKX14ZdK+CLZlA1QkjIzuZ2H+z5SqAKwMEVHZ9AmVuqakpfK2S7D+Us3LwvyfvYPI1W0PGtuaaeFu246w/sM+I/2XAM7IZB3AX9EaZ/Wpu86J3anOaNmZD7Gfk65t8+poia4+3eKMa9dUjh6iq/aXmGaka9tUjv7DnZfe+1MIwXtf5kyP0eW19z6EELz3VZ7Rol1ee38KIXjvy5webJbX3jchhMZ7n2e07gBWUDggZhcAAJCBAJ0BKgAC0wE+kUKcSyWjoqGokKk4sBIJTdwtBcCfwD8APXoQToF4A/YD+ofGpQCzAfwD8AP3H/n3mA/gH4Afo7/AOoA/gH8A/AD8Rdv/2f/NAfgH8A/AD9+bzjMr8H/S/7n/xP3/8zLYXcf6t/cf9J/kf3m9CLIT2j+v/3z/Ac/nbHnv+UfpH/J/v3+P/dD5lf1j+5/2T+R/Aj+Mf6b/z+4B+nf7I+tz6j/7D6AP63/kf2B96D/J/rL7qP3B9gD+r/73///8/3nv93///cG9AD+b/5H1bv+T+9PwSf1P/ofup/4Peu////t9wD/y+oB/3/////+3X6Af038APnp6RCeYYgJHjhfGZedncHKFQX9pQOWg/idKrEbodFnAj9Ow6IubiValpZq5vzgfcZoQjkfnDoi5vtb3waJYOGHPg4KOBUvJWZnDoi5vzh0EHAHW9Gxa4mGIBsUy+mkmuN1c35w2+3tlyWyuJzpech2ftw5+qgWs8nxurm/OHRBTZl3y5oFYOhxOKhpCWnpUxyc3sFqRASPsR2UZFeiAM/mlJbz2x4hoyhaHKo+AEj7G6uTsNtSPr0BaxTLEnZfYkUn8FqSoddWQHrx1MMOiLm/OHRCtsxwnVA1fUhgWGkO9gtSICR9jdXN93ias+XNxJz+h2HRFzfnDoi5vzQtybRE1GVlNlYBww6Iub84dEXLS2ooZ2wAfl6t7BakQEj7G6ub7WHiRu3opgHCV1EotRh7XwpOdecOiLm/OHP1CfLahsqodaoWCWIw7va714bB/+xurm/OHRBnkh4R03HQwDJkjvzyHjeBXLm/OHRFzb8/sHUP/Y9ykvlEdFawKR88Db2/UiAkfY3SLJqdWwNA6+Lm+1i95/nX+XIUoZ4ASPsbqxO5T6gz5w5+oTZWX684dEXN+cOgeGNrQx/DDn+N62hyqPgBI+xurkxi6P9QL1nsub8wszMpu/dYh3sFqRASPsUirm5K0UtFcMOf++d61WInDoi5vzh0Rc35w6IuUBYKLKakQEj7G6ub84dEXN+cOf4Daww6Iub84dEXN+cOiLE+HdRF3kRc35w6IubiqbhFuAohJtyi9VBJDh626SAVbbGf0DxbOpFQMbaPjHEmNTXvHWrJdw4ciotxwZmolO73PZ3KW0/bWMsu4xpaJ68KrZYaTw86rqxsGymxCdI3jJbAv+PIeOtoEJJCLPle/L18NhmRB6IpwAzGb3JSPyiazmo9N9g++qg69JMZIJLexFRXKKQI/guY4PJxRSEi3AHov0ab/lSRs9BWD19OcdMZgbSoI7jei4TEYbPcyOn5/HDlLBOdVswOII9rVHbZkiSkVTif4EJdH/8rfcyLRVI3SmgaQk+4vTECZrmkLeYETcsTMkfgia0AA/NiAaFlMNc2ZWigrl6vt03U0XQzVaB5ZC8f4qNl/hynzZP03aAFk+eRSgqavOCxvAuVM9C8AuK3jsakXjxH7nD1Y81i0XKeVQGJTJI8vbHVyvUaz5G2NSVGRYvPYCoAwU41PX6ps3zZBeJJ/DLox++L1oqBIX2m8wFlfOcj5Oqstr57XyR1kgPMDDT1PPrG8baaoNP1Z3xncPVjyYE5UhxpJLyMRNiB1cSHVsEXxFrvOow3MF3cB1H8+9F4AAIOLQQ2BEcOfT2aW1e3mPMHsy13l/xElnkwLRcZ1IV6Un9HPQs1KEiZGAAAKBO7d1SgFWTX02O7pbhxEgmlgGU6RNc4U20SC6MPJmIrPBACevvFda3ZxTEJT8EAA4G7qfrA3dT8+WD0/I+J73R5R73R4sHP4tBfOkpJAP4BiEZLDT/Pd7zB6CNV7zamn7ddbdavuaMFq60LfdpugndfKgRwVPsAAEnEropMPFpAnwJa1JdT4Fr/U/fT1MOs0nAX0OnIdZfZ39fruJ5kPT8EAA4G7qfrA3dT8+WD0/I+J73R5R73R4sHP4tBodMqM0JkIU31tUcTiutf3E8b7NBVM5iRPYUo7Ex9djbnSdBjo4uNBj5r4GueextkMOz7uL7gbomNa7iMVoD/2wyTCVhUiiP0zrnxyZmIxcFpXCEqjbZl09pyfC8X0ABnXheew5bhk7ql3ZBeOBJnD6LhGdAbcetxVBGOJV/909Z9IhRHeH591K844yQfT3qfFoPyDvPRKSyaTVyCJSLCm4o5rZ2MUDMTWMUw2a8UAxgcmzH84atd5hH3VV/Mq1Up/NxaRw4GS7ptzVx/NURDbpYhtbmjcy9msLiNQUeWAqkxBPYHbtiW44saGHJox/eNEX28w+xWbU/L8vXbG7sw8eMq1bl5Fiv/JHPLE0QBf3mEOXmLSraX1FqAXxR5kH9WxwAdj1E0tQaEJ4m3o5I68Oc44aEVKTJYkHvmsexqu/qFMgnck3/kPsvtiwg1VAQ1kYqNyVBmyAU5aCIRcCM/rSGOBQrbvXhnKUroQzEoedtxCD+P1q4M+sCVFREy0yilpRr8esz2D5iKewok2XHtKy4yIDJA0Rxjw8nJTT7n7eVeaIhccuRGUaab0oMCfoc27PjMtWu+cl/u86LbwMp/LWuY21/S4m6aabQAABaJcvR83noFblFH/h0l1Du2qD8p2w5+ALEnTjRjsOIZVuy2nE3P3bU7W/w3E2BOoJeXbu1VQ10re/mlPUcxfGHOEcDNpCrcK3AQJSKN8W6v0qHNd5sXE/LVbz0vp2PPw4Aa5GELb6w6hB+ymTs2OLMYV88rFYN311m2m5n/popLhABidviIReI6a0ngHhAUR9LX/ZpnGtnTjScpe7mQkIKuPs8zqnL0iaf3EqIeRYn3SyhhpOf3Zu4DTRSSpPJlHuxV4wBofJ/SuQli28ATzG6mv6VLvZjNq9wMSrCH+ckEu4MFh0MWKwMhA8IWLue20jUazEDlf2Y9HX1dJ35cBSAZ1E6/mdmg/DMdlo5IsWWqebLwwQ4GVlEORlV/I2tysBiSZQ3d9zAAAAAA0e7II+9bHAAABMFPE4Db3UAAAYwdcAbCNRq95gAAz5nXAqfI84AAANNse5mft6unxPG5ezpMYbXJo9N3v6jJFy/KnWVUekOXTBGySMx4pgmnUbjXEY1HtM/Vge0xBSOE3t9xo3YK3ovfcd4eVnhXSXJlEAD0n5mIdxsyvJtIa2Nng3tS9As/mRyhZ0tycaNz2oixYGbXgLUwFgeQEFsgZ0AbGwdBgP7dSjhn+pmC1s4MZdn9A7XAlr3PKF4/P+pfdYHa+Gl0Me67MzAfB9DBpqJ9jqmvTPYb44SFOMLn3axkn3bAdTKng4JKQqfQRFsUt5R0akYOoDL0fm255c11KfMU7pGgIABsPdn7T0T44DYagIRZX2O5lkas6f/wUfoCXhsHT72Tagyw1oboxehYlreBUbJ62h8l8odiCdlFe24jPg7QeTiLcpYjSa1Mib2TDtBKyiRyQ41cJCZ0tTJPFyvG/TCGNexjOyaJipfOI6qq69GIcNHrDxohfysbKWR+5BsnnsQ2TQAEQ/+1uDgQrAb7bqd/gpoV8O2ZKPkal2Qhrz9oM+XnPk2Sy6ELAa1NnvZW5xAUldCZ1NLWDOPRoOKl469nJcmfx6JO/zAxn58w2MW68EFy4PCO9kncVw3kfOsxok6pRkaZYr1AMVcW+TFofPUfJYpx6Wqg2W47vAeIsttGXJ6AZwvyCCmj8Wzmhj+AnreXwANhtajNMpBpTt2yrZpEJ8InwQodirPtgL3vJHwj80oGlxgqQhLK0T4kZHyQZfo46IP6CirQsBC1XAGU8vBO/Q17z1uSUqaXEEMpC/tEBaHe6oMBr7Y6l0be1eqJbDMuhggLGxUX/FJGLAAeSzZBeCW+0THFdBD0ta3q+XXS1C1rfkK7zLm7luAswbmICg6oZ44qzYBNWbPBuK05x7vdEdRpgAhqIIIclAY56/3uTxEV3tgYeSAC6yb+6RwrxgdiHoDWA3qrdZV6GUUCi1tAMTXJXkhakwXcgTkIfkayiDY1TofTvKE2KxT7LuegHw6p2AABTAUcTkNNlRjRYoWA9UwABtAVbflimWOL/tTe5VWZoo+KF/bTXMe1cZhIVFFNYqO95iNvxMsd14TK3JgAD8V4OXuSS/pKanHLyuDyKI+nYAQOOQF6x3bzybmoyxguar9l1/Y3pqjrvIfa9L4kAZMAUG38As4TsDBaBVlMKOjO3xY+uhk0aOMhbauWfI5x8FiTvC8fu7T8pm9uVr9TlVAjhB/gpCWM2K9HVupOhSGv48AABNpRdwxbEwCaoEbJ87FgPNACHIQb8G/7IACu5u9i/N4A7s0rwbjEFzMUi+vnA+qHAAAAIgjLhWSgehYj5r0aD7OQWmw3VWlaCwBavctuurSoDPiuvAAAABi4jPlzLC4NP3RWugAAALcC4pmc+R6MyKhRkfEv14EmmUUU0Q4bfWMACCg555lkxYwK5Q5evrM24E02l4E1ErYB0trLQjMb29bUDCrJ8rbqvNVSkyAgmrfJtIMa1JiRJcdSEuGspV8INixWasl62t6zSFLzgJwZxG5RjybEJrMcT6dKroBB3xQxgo4Ceyme9tdtK2r4Eqw8+MWUo7wWN/CZPqF4cYhBlL8GfICVsHCsxYT7kFmARI1Ke8afB8Fq+T1LRamjCl+oWtsXvbq/4thLL0dOIPCvxc1NhhubkurluHifZ5ZmslWbTT2AlpqlwG0nw3Em0FaXIHQShbIeT+YEoqKH/cDLdFlyJUl5qP2C+lzfLNEubg2JH89VcXJMTpFWc41PBUgILn38+cnsZJlZ7+WY6Hv/RHzrtL413hZLTkxu0KJrLfijzt/Do34jPfoN6SVgxDezDAvjA1QoqOS3FDvxStWjy0nnfVJ0lQi8f6Cs5DO7HDrkPzzAcr+D+JJAeKv8JVVS8y4anLZNBeh45D4lLUOTS7Tea365CbaFOHNDHQGjh04p3xsZsyGz5Ao9f2xvgK1yJ4AKPNH8PY0Y7ktaqt/zoI+zsWc/ijA8UyoE05C9GAPlBxPJcjozNiXwd2fwC9AcaWy8+PJ771yBYNgNOBdagjuMQXNbAEvMjzPJUZqdi+eqt1Ns24qA5H2uYV4vo+NJvQ4GTOGfMHsG1bcMJzImBYtmzp2z7q2m/c8cVVD5sMymsR2SWGWTOBN973oOFOkU5BEVSQK/vTKioSNhaA03BYvqIzD00taCVPLuEPg7CN93i0W/f7m9OZTb1aR09VOptHzQ3JqeTrvF4WTIl9YnlArmyEeLgO8KsUJLkr0AcjuF/Uud4TKh65c/2LALkfFhhnYzAuKZlTA8IG7fJq2tpfhH2eiqCLu3BAl3U0f82v7bUiwji/rIhMghCw7l/nQco7pMOH9P/saF7RjtFig5a7hQDFIVAKtGIBJ4zP7aW8ZjgwR4/azKzi6hrxMiqbM12yxPCFzfXTwMhT6xhSeKqwhBh/fKjA/ePpLUEuCAs/EF0d4q0cLBi+awfSEUQlyzOXdR3Yw6NffFQPX7K/8XQURvHEPfHCABlGKgJugvmu+U/7tyPs9k4arBuwTGHJFFFvpTYRQlMKlaX29UvlnPboRyGUIuc3ENqan9ySncO59OUPOfyUemO/09IVUdMNblG1Bj2U6zIof1Ba5jUC+ZvBD6ry5jeOkKU6ecxfRZWKSxksYLnVK+jKRP8oB6Kp24JjXw/7ppDrJhXiuasvnVCrpQB4hs1wYD20awcg+qO38Sf/cSys0AK0RlX5ttVwipEdNtQwxIdsko4XurVR0w1uUbUGPZTpbZ/kAYJebacQnGxx0HWSpbkyGODPA83Ea9JADm/tbcPYs+yBDJmgsRh03ouyfAr+kblA9WMDTotPEHkDzCSCyD5kYPuFGpnN8e7eQqD7iDXk/eYRdhi34CAXV9U57YKFnCs/dUt/m1A7hpMDzaE5CvGuIKyLpQteyT9z2OdaFYFXjIs+AAXBTrU9ckFgIAdhB0m/oaupXv4ooLGs7hPLRXBHyPeZWFPiV9/YpmWLZpFmDZCqS2T5wi523/7sbO0Zh9HwjjKbe03tBPvZhH+F4/dujqM+/M8cT6tYyCGvf2pXj9MGija8zpwjuKlgWUH97f4i57YFXrkvZP04pY9zo/7U6AG3nFWdkDGCJFYOAkcqRYLJmj6l9v3hapoz78zxWNUJw6yCmSi+pzzMc8bTGt6q0cYpRSwl28VCvelTgoZtGahHHTOouBn2qg9XFfV3vHMwfDbsEtUZNVWOKQ79W0osWGmuVxMDfZ+NG7gVxYeu7FvVCPxeEWhA7NPKUUR+ABSQwvkUIpqxZeh76T3WWy7kCupBUYVFQ1AGqMZPj+a6ptom/lWvg+I4414rgh2Cl0lNi+LZEC3y4NRqBdLB84XeF4/dpRbSlmWpIDW888+bxmaOXe36xh7kWRU6sYXik2YnBbPdolTGRXFBt+jw4qIm5g77HMy+r2/5uo2vxNCzvQ02FBZAWeq8LWVoVP1mjn8DQyIbdEYToT65oYIbpeRGYjzGj2kbk6YVDWWTaoGNcTURt6eudH/fUbzdd2z+caDVU9Q1lqF87mVL6JMInVn5OGJCA7ETMgriN8wxsmvztqYvEi+myV0mAIETT37IYidyPirsOwBQDoODMSnJraR5khH0SUPpWPModxgIH5/OfwBThKSkGJqgE1ub/ZT3hF+fdfAf3E5dH14w/sKj3j6796hrLKjKsTYO6CNS0wHNEXQJGakfIiPsmgaaaYWcB2HBybMfdoODpHL05dlTuR8VdkLHi/CPrPGNGeOyjydn8ebuOL506DD8DRp1FoWfxCmyum/8TKkKPOKOi4oKWaUmSm7lmx4t3xQJqMH7DZXoIgsWt/+Xt56ZRHkOfhIbzO638HnYKajCF9Z8h/DX8EwQiJxrzfFQ6cZ6jMVIWEcOEjcdLQzMwxSeVG37ajp8zmEGHzBHROahi8JufojTm7bvMlDhE3LtJi79pIJzwxv6auWLLmOfdQd5jnSZAotX4GAxhmzpQXl6K/dYBBZca0aWE8xO4zIVWBfH6TtpTgzJqBrXoYcDcVRrZZyq5guH8jhIIOPgmRpqNGRSgfq4BcKfUbTJxXhUwb8Cy8zlhtkwDwHp3hOx946a2d+YUJjzl5ctQe1kIQfrYYQBH2lQTP+uoueh67Yo5dTlCDaunlG1WeNB0x5KQAWOuPWOcHjdWCIvHM76qCncm2wpt7oug91YG7PsVxSRVrMrRNVp+VR/tHFKnydcTWjWtjYvo39hrJkuBfYJU06mfcFQtl7A0sz6KFEkjkxyb9o4tdQRx2vY/3gbLfUrHjV70hvabZpN19Lhelw6dKmygVOVvxJqtW7bmO+XqTRZ2l0gcrFSxwmFDftZqmB1Y6vAkFLZth4RuwXJohnAuJK0dQeOV1aIXTghaD68CNVHZ8Yftq2a+t7rRTuezMZgFnCgxpweMRfPlRdVdB5sL8YhUSuZFO9799NvSODyFNs2JAP4TIXdkJYKMjHJKpNC6e2DBcNWL6pJCV2FANSU41bZtOKDjM8VPCvNtre/Tm+lHRUq2imbjFF4Bb+gHKZZ1FkBezjLa88J3xkixIj5T0Ph5Tg4OjPCkyEtMHF43GBPzEZS2RbrnWcqYiUFKDhAl+ZMD8uSV0Q63B+vHxlm+QIldkLxpV+hAaKYX4Ocy3BRnhKJK30EoViszKerQHl1OhmVqUFhLGL2i87Cl3WNMzxU8K822tZIp6dFrfi8ecQZQ5uRLOGVyNbRL2LndSqgVFYoKleXA74EI32bJS18M1tAlqTk52W8PW89CE5vulho267Gt9h4H3N2pcsraRIpZU06Vc7Req/dmstSKic52lVP+5F9voF/j7FBgNm/6KWvjSMg/VqngU8Sp4V2DjBczXK3mdtZuJsqcufuLGti9IoqSMyZCJjY0tKM9sf3DbZAzoXuq2wvQKCtYd4JenlcvuwuFTB+DWVJB9n5me1mbZwyU4KPUbPAEW/2KCpS3JGzEE49kb1ZxrISw+ox85upm4xS1cIvRcGEwAA",
  "backgroundColor": "#FFFFFF"
}

````

============================================================
FILE: helpers/assets/vendor-servicenow.json
DIRECTORY: helpers/assets/
FILENAME: vendor-servicenow.json
============================================================
SHA256: febfc6152102f9e07f95acdd87aca46c3c5b3d19369715d08ae1805b5129f579

````json
{
  "_id": "66d0b88221161b4df271749d",
  "name": "ServiceNow",
  "description": "ServiceNow Project has assets for Create Change Request, Update Change Request, Close Change Request, Update Incident, Create Request Item, Create Incident, Approve Change Request,  Update Request Item",
  "components": [
    {
      "iid": 0,
      "reference": "36a32c57-042c-49af-8d6c-6e614a632d71",
      "type": "workflow",
      "folder": "/Close Change Request",
      "document": {
        "name": "Close Change Request",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -444,
              "y": 720
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -444,
              "y": 1284
            }
          },
          "c345": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Show ServiceNow Error",
            "description": "Show close change request error and decision options",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "ServiceNow Error",
                "message": "",
                "body": "$var.job.serviceNowError",
                "variables": {},
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": -144,
              "y": 1056
            }
          },
          "2ad1": {
            "name": "updateChangeRequest",
            "canvasName": "updateChangeRequest",
            "summary": "Update Change Request",
            "description": "Update change request to close it",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "changeId": "$var.e4c7.crSysId",
                "body": "$var.e4c7.crClosePayload",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedCR"
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -444,
              "y": 1164
            }
          },
          "fd22": {
            "name": "getChangeRequests",
            "canvasName": "getChangeRequests",
            "summary": "Get Change Request",
            "description": "Get change request with query parameters provided",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "sysparmQuery": "$var.ade8.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": null
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -444,
              "y": 936
            }
          },
          "ade8": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build sysparmQuery",
            "description": "Build sysparmQuery",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "number",
                    "value": {
                      "task": "job",
                      "variable": "crNumber",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": -444,
              "y": 816
            }
          },
          "e4c7": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Build CR Close Payload - ServiceNow",
            "description": "Build change request close payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "63d1a03fa15c2401e9a6143c",
                "variableMap": {
                  "changeRequestResponse": "$var.fd22.result",
                  "closeCode": "$var.job.closeCode",
                  "closeNotes": "$var.job.closeNotes"
                },
                "options": {
                  "extractOutput": false,
                  "validateIncoming": false,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "crSysId": null,
                "crClosePayload": null
              }
            },
            "groups": [],
            "task_name": "Build CR Close Payload - ServiceNow",
            "retrySettings": null,
            "nodeLocation": {
              "x": -444,
              "y": 1056
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "ade8": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "c345": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "2ad1": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "c345": {
              "type": "standard",
              "state": "error"
            }
          },
          "fd22": {
            "c345": {
              "type": "standard",
              "state": "error"
            },
            "e4c7": {
              "type": "standard",
              "state": "success"
            }
          },
          "ade8": {
            "fd22": {
              "type": "standard",
              "state": "success"
            }
          },
          "e4c7": {
            "2ad1": {
              "type": "standard",
              "state": "success"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "crNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "closeCode": {
              "type": "string"
            },
            "closeNotes": {
              "type": "string"
            }
          },
          "required": ["adapterId", "crNumber", "closeCode", "closeNotes"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "crNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "closeCode": {
              "type": "string"
            },
            "closeNotes": {
              "type": "string"
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedCR": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.72.0",
        "font_size": 12,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:06:05.886Z",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 1,
      "reference": "60abc503-6007-4e68-8470-2c103ad9b417",
      "type": "workflow",
      "folder": "/Update Request Item",
      "document": {
        "name": "Update Request Item (RITM)",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -96,
              "y": 612
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -96,
              "y": 1176
            }
          },
          "c345": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Show ServiceNow Error",
            "description": "Show ServiceNow request item update error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "ServiceNow Error",
                "message": "",
                "body": "$var.job.serviceNowError",
                "variables": {},
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 300,
              "y": 948
            }
          },
          "ade8": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build Request Item Search Query",
            "description": "Build request item search query",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "number",
                    "value": {
                      "task": "job",
                      "variable": "ritmNumber",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": -96,
              "y": 732
            }
          },
          "e4c7": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Build Request Item Update Payload",
            "description": "Build request item update payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "62279f8c7858d601db6606f9",
                "variableMap": {
                  "requestItemResponse": "$var.cb96.result",
                  "comments": "$var.job.comments",
                  "state": "$var.job.state"
                },
                "options": {
                  "extractOutput": false,
                  "validateIncoming": false,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "ritmSysId": null,
                "ritmUpdatePayload": null
              },
              "decorators": []
            },
            "groups": [],
            "task_name": "Build RITM Update Payload - ServiceNow",
            "retrySettings": null,
            "nodeLocation": {
              "x": -96,
              "y": 948
            }
          },
          "cb96": {
            "name": "getRequestItems",
            "canvasName": "getRequestItems",
            "summary": "Get Request Item",
            "description": "Get request item from ServiceNow",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "sysparmQuery": "$var.ade8.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": null
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -96,
              "y": 840
            }
          },
          "ba05": {
            "name": "updateRequestItems",
            "canvasName": "updateRequestItems",
            "summary": "Update Request Item",
            "description": "Update request item in ServiceNow",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "itemId": "$var.e4c7.ritmSysId",
                "body": "$var.e4c7.ritmUpdatePayload",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedRequestItem"
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -96,
              "y": 1056
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "ade8": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "c345": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "ade8": {
            "cb96": {
              "type": "standard",
              "state": "success"
            }
          },
          "e4c7": {
            "ba05": {
              "type": "standard",
              "state": "success"
            }
          },
          "cb96": {
            "c345": {
              "type": "standard",
              "state": "error"
            },
            "e4c7": {
              "type": "standard",
              "state": "success"
            }
          },
          "ba05": {
            "c345": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "ritmNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["ritmNumber", "comments", "state", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "ritmNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedRequestItem": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 12,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:06:05.888Z",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 2,
      "reference": "235a66e6-b944-4f0c-9cff-d960fd341584",
      "type": "workflow",
      "folder": "/Create Request Item (RITM)",
      "document": {
        "name": "Create Request Item",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 732,
              "y": 600
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 732,
              "y": 1020
            }
          },
          "12f6": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Verify Request Item Creation Successful",
            "description": "Verify if incident creation is successful",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "query": "response.number",
                        "operand_1": {
                          "variable": "result",
                          "task": "a683"
                        },
                        "operator": "contains",
                        "operand_2": {
                          "variable": "RITM",
                          "task": "static"
                        }
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 732,
              "y": 900
            }
          },
          "c345": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "ServiceNow Error",
            "description": "Show ServiceNow request item creation error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Create Request Item Error",
                "message": "Unable to create request item",
                "body": "$var.job.serviceNowError",
                "variables": {},
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 1080,
              "y": 888
            }
          },
          "aab9": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build Request Item Creation Payload",
            "description": "Build incident creation payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "summary",
                    "value": {
                      "task": "job",
                      "variable": "summary",
                      "editable": true
                    }
                  },
                  {
                    "key": "comments",
                    "value": {
                      "task": "job",
                      "variable": "comments",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 732,
              "y": 696
            }
          },
          "a683": {
            "name": "createRequestItems",
            "canvasName": "createRequestItems",
            "summary": "Create Request Item",
            "description": "Create request item in ServiceNow",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "ServiceNow",
            "variables": {
              "incoming": {
                "body": "$var.aab9.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdRequestItem"
              },
              "error": "$var.job.serviceNowError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 732,
              "y": 792
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "aab9": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "12f6": {
            "c345": {
              "type": "standard",
              "state": "failure"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "c345": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "aab9": {
            "a683": {
              "state": "success",
              "type": "standard"
            }
          },
          "a683": {
            "c345": {
              "type": "standard",
              "state": "error"
            },
            "12f6": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "summary": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["summary", "comments", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "summary": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "createdRequestItem": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.46.0-2023.1.15.0",
        "font_size": 12,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated": "2025-01-24T11:06:05.889Z",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 3,
      "reference": "ab5419b3-4bc8-4955-9539-20adcf71c4b7",
      "type": "workflow",
      "folder": "/Create Change Request",
      "document": {
        "name": "Create Change Request",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 780,
              "y": 780
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 780,
              "y": 1236
            }
          },
          "cc49": {
            "name": "createChangeRequest",
            "canvasName": "createChangeRequest",
            "summary": "Create Change Request",
            "description": "Create the change with the information provided and return the change number for future reference.",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "body": "$var.aab9.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdCR"
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 780,
              "y": 996
            }
          },
          "12f6": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Verify CR Creation Successful",
            "description": "CR Creation Successful?",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "query": "response.number",
                        "operand_1": {
                          "variable": "result",
                          "task": "cc49"
                        },
                        "operator": "contains",
                        "operand_2": {
                          "variable": "CHG",
                          "task": "static"
                        }
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 780,
              "y": 1104
            }
          },
          "c345": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Show ServiceNow Error",
            "description": "Show create change request error and decision options",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Create Change Request Error",
                "message": "Unable to create change request",
                "body": "$var.job.serviceNowError",
                "variables": {},
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 456,
              "y": 1104
            }
          },
          "aab9": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build CR Creation Payload",
            "description": "Build CR Creation Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "title",
                    "value": {
                      "task": "job",
                      "variable": "title",
                      "editable": true
                    }
                  },
                  {
                    "key": "summary",
                    "value": {
                      "task": "job",
                      "variable": "summary",
                      "editable": true
                    }
                  },
                  {
                    "key": "description",
                    "value": {
                      "task": "job",
                      "variable": "description",
                      "editable": true
                    }
                  },
                  {
                    "key": "comments",
                    "value": {
                      "task": "job",
                      "variable": "comments",
                      "editable": true
                    }
                  },
                  {
                    "key": "assignment_group",
                    "value": {
                      "task": "job",
                      "variable": "assignmentGroup",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 780,
              "y": 888
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "aab9": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "cc49": {
            "12f6": {
              "type": "standard",
              "state": "success"
            },
            "c345": {
              "type": "standard",
              "state": "error"
            }
          },
          "12f6": {
            "c345": {
              "type": "standard",
              "state": "failure"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "c345": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "aab9": {
            "cc49": {
              "type": "standard",
              "state": "success"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "title": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "summary": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "description": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "assignmentGroup": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "adapterId",
            "title",
            "summary",
            "description",
            "comments",
            "assignmentGroup"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "title": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "summary": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "description": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "assignmentGroup": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "createdCR": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 12,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:06:05.889Z",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 5,
      "reference": "33977fa9-428d-4476-a9a3-fd006780bb92",
      "type": "workflow",
      "folder": "/Approve Change Request",
      "document": {
        "name": "Approve Change Request",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -708,
              "y": -384
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -708,
              "y": 84
            }
          },
          "ca34": {
            "name": "autoApproveChangeRequest",
            "canvasName": "autoApproveChangeRequest",
            "summary": "Approve Change Request",
            "description": "Approve change request",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "ServiceNow",
            "variables": {
              "incoming": {
                "changeId": "$var.job.changeId",
                "approval": "$var.job.approval",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.result"
              },
              "error": "$var.job.error"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -708,
              "y": -48
            }
          },
          "a8f4": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Show ServiceNow Error",
            "description": "Show approve change request error and decision options",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "ServiceNow Error",
                "message": "",
                "body": "$var.ca34.error",
                "variables": "",
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -384,
              "y": -48
            }
          },
          "350a": {
            "name": "getChangeRequests",
            "canvasName": "getChangeRequests",
            "summary": "Get Change Request",
            "description": "Get change request with query parameters provided",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "ServiceNow",
            "variables": {
              "incoming": {
                "sysparmQuery": "$var.16cd.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": ""
              },
              "error": "$var.job.error"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -708,
              "y": -168
            }
          },
          "16cd": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build Query for Search",
            "description": "Build Query for Search",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "number",
                    "value": {
                      "task": "job",
                      "variable": "crNumber"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -708,
              "y": -276
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "16cd": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "ca34": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            },
            "a8f4": {
              "type": "standard",
              "state": "error"
            }
          },
          "a8f4": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "350a": {
            "ca34": {
              "state": "success",
              "type": "standard"
            }
          },
          "16cd": {
            "350a": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "changeId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "approval": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "crNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["changeId", "approval", "adapterId", "crNumber"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "changeId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "approval": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "crNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "result": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "error": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "type": "automation",
        "font_size": 12,
        "errorHandler": null,
        "preAutomationTime": 0,
        "sla": 0,
        "last_updated": "2025-01-24T11:06:05.890Z",
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "createdVersion": "5.46.0-2023.1.15.0",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 6,
      "reference": "79639555-5bb6-4ea8-8f25-7d11b269ca54",
      "type": "workflow",
      "folder": "/Update Change Request",
      "document": {
        "name": "Update Change Request",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -156,
              "y": 684
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -156,
              "y": 1308
            }
          },
          "c345": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Show ServiceNow Error",
            "description": "Show update change request error and decision options",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "ServiceNow Error",
                "message": "",
                "body": "$var.job.serviceNowError",
                "variables": {},
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 180,
              "y": 1044
            }
          },
          "2ad1": {
            "name": "updateChangeRequest",
            "canvasName": "updateChangeRequest",
            "summary": "Update Change Request",
            "description": "Update change request state",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "changeId": "$var.e4c7.crSysId",
                "body": "$var.e4c7.crUpdatePayload",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedCR"
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -156,
              "y": 1164
            }
          },
          "fd22": {
            "name": "getChangeRequests",
            "canvasName": "getChangeRequests",
            "summary": "Get Change Request",
            "description": "Get change request with query parameters provided",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "sysparmQuery": "$var.ade8.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": null
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -156,
              "y": 924
            }
          },
          "ade8": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build sysparmQuery",
            "description": "Build sysparmQuery",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "number",
                    "value": {
                      "task": "job",
                      "variable": "crNumber",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": -156,
              "y": 804
            }
          },
          "e4c7": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Build CR Update Payload - ServiceNow",
            "description": "Build change request update payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "621a5d367393d9019373d137",
                "variableMap": {
                  "changeRequestResponse": "$var.fd22.result",
                  "comments": "$var.job.comments",
                  "state": "$var.job.state"
                },
                "options": {
                  "extractOutput": false,
                  "validateIncoming": false,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "crSysId": null,
                "crUpdatePayload": null
              }
            },
            "groups": [],
            "task_name": "Build CR Update Payload - ServiceNow",
            "retrySettings": null,
            "nodeLocation": {
              "x": -156,
              "y": 1044
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "ade8": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "c345": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "2ad1": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "c345": {
              "type": "standard",
              "state": "error"
            }
          },
          "fd22": {
            "c345": {
              "type": "standard",
              "state": "error"
            },
            "e4c7": {
              "type": "standard",
              "state": "success"
            }
          },
          "ade8": {
            "fd22": {
              "type": "standard",
              "state": "success"
            }
          },
          "e4c7": {
            "2ad1": {
              "type": "standard",
              "state": "success"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "crNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "state": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["adapterId", "crNumber", "comments", "state"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "crNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "state": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedCR": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 12,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:06:05.891Z",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 7,
      "reference": "0c6ebd87-0e53-43f8-8810-9decfa5e3077",
      "type": "workflow",
      "folder": "/Update Incident",
      "document": {
        "name": "Update Incident",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 120,
              "y": 624
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 120,
              "y": 1212
            }
          },
          "c345": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "ServiceNow Error",
            "description": "Show ServiceNow incident update error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "ServiceNow Error",
                "message": "",
                "body": "$var.job.serviceNowError",
                "variables": {},
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 432,
              "y": 960
            }
          },
          "ade8": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build Incident Search Query",
            "description": "Build search query for incident in Service Now",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "number",
                    "value": {
                      "task": "job",
                      "variable": "incNumber",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 120,
              "y": 744
            }
          },
          "e4c7": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Build INC Update Payload - ServiceNow",
            "description": "Build INC Update Payload - ServiceNow",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "622785287858d601db6606f8",
                "variableMap": {
                  "incidentResponse": "$var.b6d3.result",
                  "comments": "$var.job.comments",
                  "state": "$var.job.state"
                },
                "options": {
                  "extractOutput": false,
                  "validateIncoming": false,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "incSysId": null,
                "incUpdatePayload": null
              },
              "decorators": []
            },
            "groups": [],
            "task_name": "Build INC Update Payload - ServiceNow",
            "retrySettings": null,
            "nodeLocation": {
              "x": 120,
              "y": 972
            }
          },
          "b6d3": {
            "name": "getIncidents",
            "canvasName": "getIncidents",
            "summary": "Get Incident",
            "description": "Get incident from ServiceNow",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "sysparmQuery": "$var.ade8.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": null
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 120,
              "y": 864
            }
          },
          "a002": {
            "name": "updateIncident",
            "canvasName": "updateIncident",
            "summary": "Update Incident",
            "description": "Update incident in ServiceNow",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "incidentId": "$var.e4c7.incSysId",
                "body": "$var.e4c7.incUpdatePayload",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedIncident"
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 120,
              "y": 1080
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "ade8": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "c345": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "ade8": {
            "b6d3": {
              "type": "standard",
              "state": "success"
            }
          },
          "e4c7": {
            "a002": {
              "type": "standard",
              "state": "success"
            }
          },
          "b6d3": {
            "c345": {
              "type": "standard",
              "state": "error"
            },
            "e4c7": {
              "type": "standard",
              "state": "success"
            }
          },
          "a002": {
            "c345": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "incNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["incNumber", "comments", "state", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "incNumber": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedIncident": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 12,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:06:05.890Z",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 8,
      "reference": "aab43a79-fafb-4bb6-9ed7-bc4a21a70666",
      "type": "workflow",
      "folder": "/Create Incident",
      "document": {
        "name": "Create Incident",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 636,
              "y": 636
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 636,
              "y": 1056
            }
          },
          "12f6": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Verify Incident Creation Successful",
            "description": "Verify if incident creation is successful",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "query": "response.number",
                        "operand_1": {
                          "variable": "result",
                          "task": "bb2d"
                        },
                        "operator": "contains",
                        "operand_2": {
                          "variable": "INC",
                          "task": "static"
                        }
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 636,
              "y": 948
            }
          },
          "c345": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "ServiceNow Error",
            "description": "Show ServiceNow incident creation error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Create Incident Error",
                "message": "Unable to create incident",
                "body": "$var.job.serviceNowError",
                "variables": {},
                "btn_success": "OK",
                "btn_failure": ""
              },
              "outgoing": {},
              "error": "",
              "decorators": []
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "scheduled": false,
            "nodeLocation": {
              "x": 288,
              "y": 948
            }
          },
          "aab9": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build Incident Creation Payload",
            "description": "Build incident creation payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "summary",
                    "value": {
                      "task": "job",
                      "variable": "summary",
                      "editable": true
                    }
                  },
                  {
                    "key": "comments",
                    "value": {
                      "task": "job",
                      "variable": "comments",
                      "editable": true
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 636,
              "y": 732
            }
          },
          "bb2d": {
            "name": "createIncident",
            "canvasName": "createIncident",
            "summary": "Create Incident",
            "description": "Create incident in ServiceNow",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "body": "$var.aab9.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdIncident"
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 636,
              "y": 840
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "aab9": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "12f6": {
            "c345": {
              "type": "standard",
              "state": "failure"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "c345": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "aab9": {
            "bb2d": {
              "type": "standard",
              "state": "success"
            }
          },
          "bb2d": {
            "12f6": {
              "type": "standard",
              "state": "success"
            },
            "c345": {
              "type": "standard",
              "state": "error"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "summary": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["summary", "comments", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "summary": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comments": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "createdIncident": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 12,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:06:05.891Z",
        "preAutomationTime": 0,
        "sla": 0,
        "type": "automation",
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 9,
      "reference": "ea1c7752-7206-4f52-8eea-629f9bec5386",
      "type": "workflow",
      "folder": "/Get Service Catalog Inputs",
      "document": {
        "name": "Get Service Catalog Inputs",
        "description": "Gets variables of Service Catalog in ServiceNow as provided by its name.",
        "tasks": {
          "3866": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Filter Service Catalog by Name and State",
            "description": "Filter for name",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "nameOfServiceCatalogItem",
                      "editable": true
                    }
                  },
                  {
                    "key": "state",
                    "value": {
                      "task": "job",
                      "variable": "stateOfServiceCatalogItem"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "nodeLocation": {
              "x": 948,
              "y": 624
            }
          },
          "4228": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Get ID of Service Catalog Found",
            "description": "Gets ID of Service Catalog matching search",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "64ff61c85449f701414638da",
                "variableMap": {
                  "serviceCatalogResults": "$var.eee7.result"
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "serviceCatalogId": "$var.job.serviceCatalogId"
              },
              "decorators": [],
              "error": "$var.job.serviceNowError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 948,
              "y": 840
            }
          },
          "5900": {
            "name": "transformation",
            "canvasName": "transformation",
            "summary": "Get Variables of Service Catalog",
            "description": "Get Variables of Service Catalog",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "tr_id": "64ff6ad65449f701414638db",
                "variableMap": {
                  "serviceCatalogDetails": "$var.474d.result"
                },
                "options": {
                  "extractOutput": true,
                  "validateIncoming": true,
                  "revertToDefaultValue": true
                }
              },
              "outgoing": {
                "serviceCatalogInputVariables": "$var.job.serviceCatalogInputVariables"
              },
              "decorators": [],
              "error": "$var.job.serviceNowError"
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 948,
              "y": 1152
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 948,
              "y": 504
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 948,
              "y": 1284
            }
          },
          "eee7": {
            "name": "queryTableByName",
            "canvasName": "queryTableByName",
            "summary": "Search the Service Catalog Table",
            "description": "Search the Service Catalog table by name and state",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "tableName": "sc_cat_item",
                "sysparmQuery": "$var.3866.merged_object",
                "adapter_id": "$var.job.adapterId"
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
            "nodeLocation": {
              "x": 948,
              "y": 732
            }
          },
          "474d": {
            "name": "getServiceCatalogItemById",
            "canvasName": "getServiceCatalogItemById",
            "summary": "Retrieves a specified catalog item.",
            "description": "Retrieves a specified catalog item.",
            "location": "Adapter",
            "locationType": "Servicenow",
            "app": "Servicenow",
            "type": "automatic",
            "displayName": "Servicenow",
            "variables": {
              "incoming": {
                "sysparmLimit": 1,
                "catalogId": "$var.4228.serviceCatalogId",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": null
              },
              "error": "$var.job.serviceNowError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 948,
              "y": 1056
            }
          },
          "5cb1": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Verify Service Catalog Item Found",
            "description": "Verify Service Catalog Item Found",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "all_true_flag": false,
                "evaluation_groups": [
                  {
                    "all_true_flag": false,
                    "evaluations": [
                      {
                        "operand_1": {
                          "task": "4228",
                          "variable": "serviceCatalogId"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": "No match found"
                        },
                        "operator": "!=",
                        "query": "",
                        "rightQuery": ""
                      }
                    ]
                  }
                ]
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 948,
              "y": 948
            }
          },
          "7f08": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Show Form for No Service Catalog Found",
            "description": "Display option when no matching Service Catalog item found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "No Service Catalog Found",
                "message": "No Service Catalog item matching search parameters found.",
                "body": "$var.3866.merged_object",
                "variables": "",
                "btn_success": "End Job",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": 600,
              "y": 936
            }
          }
        },
        "transitions": {
          "3866": {
            "eee7": {
              "type": "standard",
              "state": "success"
            }
          },
          "4228": {
            "5cb1": {
              "state": "success",
              "type": "standard"
            }
          },
          "5900": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_start": {
            "3866": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "eee7": {
            "4228": {
              "state": "success",
              "type": "standard"
            }
          },
          "474d": {
            "5900": {
              "state": "success",
              "type": "standard"
            }
          },
          "5cb1": {
            "474d": {
              "state": "success",
              "type": "standard"
            },
            "7f08": {
              "type": "standard",
              "state": "failure"
            }
          },
          "7f08": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "f38e": {},
          "22ce": {},
          "7b17": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "nameOfServiceCatalogItem": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "stateOfServiceCatalogItem": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "nameOfServiceCatalogItem",
            "stateOfServiceCatalogItem",
            "adapterId"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "nameOfServiceCatalogItem": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "stateOfServiceCatalogItem": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "serviceCatalogId": {
              "$id": "serviceCatalogId",
              "type": "string",
              "examples": ["id"]
            },
            "serviceNowError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "serviceCatalogInputVariables": {
              "$id": "serviceCatalogInputVariables",
              "type": "array"
            }
          }
        },
        "font_size": 12,
        "createdVersion": "5.46.0-2023.1.15.0",
        "last_updated": "2025-01-24T11:06:05.892Z",
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "type": "automation",
        "preAutomationTime": 0,
        "sla": 0,
        "last_updated_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "Okta",
          "username": "admin@itential",
          "firstname": "admin@itential",
          "inactive": false,
          "sso": true,
          "nameID": "admin@itential"
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 3
      }
    },
    {
      "iid": 10,
      "reference": "64ff6ad65449f701414638db",
      "type": "transformation",
      "folder": "/Get Service Catalog Inputs",
      "document": {
        "_id": "64ff6ad65449f701414638db",
        "name": "Get Variables of Service Catalog",
        "description": "Gets variables required for Service Catalog in ServiceNow",
        "incoming": [
          {
            "$id": "serviceCatalogDetails",
            "type": "object",
            "properties": {
              "response": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "examples": ["186d917a6fab7980575967ddbb3ee4f2"]
                  },
                  "summary": {
                    "type": "string",
                    "examples": ["New Email Creation"]
                  },
                  "variables": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "active": {
                          "type": "boolean",
                          "examples": [true, false]
                        },
                        "label": {
                          "type": "string",
                          "examples": ["Preferred Email address"]
                        },
                        "type": {
                          "type": "integer",
                          "examples": [26]
                        },
                        "mandatory": {
                          "type": "boolean",
                          "examples": [true, false]
                        },
                        "render_label": {
                          "type": "boolean",
                          "examples": [true, false]
                        },
                        "read_only": {
                          "type": "boolean",
                          "examples": [true, false]
                        },
                        "name": {
                          "type": "string",
                          "examples": ["new_email"]
                        },
                        "value": {
                          "type": "string"
                        },
                        "help_text": {
                          "type": "string"
                        }
                      },
                      "required": []
                    }
                  }
                },
                "required": []
              }
            },
            "required": []
          }
        ],
        "outgoing": [
          {
            "$id": "serviceCatalogInputVariables",
            "type": "array"
          }
        ],
        "steps": [
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "serviceCatalogDetails",
              "ptr": "/response/variables"
            },
            "to": {
              "location": "method",
              "name": 1,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 1,
            "type": "method",
            "library": "Array",
            "method": "map",
            "args": [null, "mapInputVariables"],
            "view": {
              "row": 1,
              "col": 1
            },
            "context": "#"
          },
          {
            "id": 3,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 1,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "serviceCatalogInputVariables",
              "ptr": ""
            },
            "context": "#"
          }
        ],
        "functions": [
          {
            "incoming": [
              {
                "type": "object",
                "properties": {
                  "active": {
                    "type": "boolean",
                    "examples": [true, false]
                  },
                  "label": {
                    "type": "string",
                    "examples": ["Preferred Email address"]
                  },
                  "type": {
                    "type": "integer",
                    "examples": [26]
                  },
                  "mandatory": {
                    "type": "boolean",
                    "examples": [true, false]
                  },
                  "displayvalue": {
                    "type": "string"
                  },
                  "friendly_type": {
                    "type": "string",
                    "examples": ["email"]
                  },
                  "display_type": {
                    "type": "string",
                    "examples": ["Email"]
                  },
                  "render_label": {
                    "type": "boolean",
                    "examples": [true, false]
                  },
                  "read_only": {
                    "type": "boolean",
                    "examples": [true, false]
                  },
                  "name": {
                    "type": "string",
                    "examples": ["new_email"]
                  },
                  "id": {
                    "type": "string",
                    "examples": ["65865e474fbb4200086eeed18110c7dd"]
                  },
                  "value": {
                    "type": "string"
                  },
                  "help_text": {
                    "type": "string"
                  },
                  "max_length": {
                    "type": "integer",
                    "examples": [0]
                  },
                  "order": {
                    "type": "integer",
                    "examples": [-1]
                  }
                },
                "required": [],
                "$id": "currentValue"
              },
              {
                "title": "index",
                "type": "number",
                "optional": true,
                "$id": "index"
              },
              {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "active": {
                      "type": "boolean",
                      "examples": [true, false]
                    },
                    "label": {
                      "type": "string",
                      "examples": ["Preferred Email address"]
                    },
                    "type": {
                      "type": "integer",
                      "examples": [26]
                    },
                    "mandatory": {
                      "type": "boolean",
                      "examples": [true, false]
                    },
                    "displayvalue": {
                      "type": "string"
                    },
                    "friendly_type": {
                      "type": "string",
                      "examples": ["email"]
                    },
                    "display_type": {
                      "type": "string",
                      "examples": ["Email"]
                    },
                    "render_label": {
                      "type": "boolean",
                      "examples": [true, false]
                    },
                    "read_only": {
                      "type": "boolean",
                      "examples": [true, false]
                    },
                    "name": {
                      "type": "string",
                      "examples": ["new_email"]
                    },
                    "id": {
                      "type": "string",
                      "examples": ["65865e474fbb4200086eeed18110c7dd"]
                    },
                    "value": {
                      "type": "string"
                    },
                    "help_text": {
                      "type": "string"
                    },
                    "max_length": {
                      "type": "integer",
                      "examples": [0]
                    },
                    "order": {
                      "type": "integer",
                      "examples": [-1]
                    }
                  },
                  "required": []
                },
                "$id": "array",
                "optional": true
              }
            ],
            "outgoing": [
              {
                "$id": "mappedInput",
                "type": "object",
                "properties": {
                  "input_name": {
                    "type": "string"
                  },
                  "input_is_active": {
                    "type": "boolean",
                    "examples": [true, false]
                  },
                  "input_is_read_only": {
                    "type": "boolean",
                    "examples": [true, false]
                  },
                  "input_is_mandatory": {
                    "type": "boolean",
                    "examples": [true, false]
                  },
                  "input_label": {
                    "type": "string",
                    "examples": ["Label"]
                  }
                },
                "required": []
              }
            ],
            "steps": [
              {
                "id": 1,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": "/name"
                },
                "to": {
                  "location": "outgoing",
                  "name": "mappedInput",
                  "ptr": "/input_name"
                },
                "context": "#"
              },
              {
                "id": 2,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": "/active"
                },
                "to": {
                  "location": "outgoing",
                  "name": "mappedInput",
                  "ptr": "/input_is_active"
                },
                "context": "#"
              },
              {
                "id": 3,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": "/read_only"
                },
                "to": {
                  "location": "outgoing",
                  "name": "mappedInput",
                  "ptr": "/input_is_read_only"
                },
                "context": "#"
              },
              {
                "id": 4,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": "/mandatory"
                },
                "to": {
                  "location": "outgoing",
                  "name": "mappedInput",
                  "ptr": "/input_is_mandatory"
                },
                "context": "#"
              },
              {
                "id": 5,
                "type": "assign",
                "from": {
                  "location": "incoming",
                  "name": "currentValue",
                  "ptr": "/label"
                },
                "to": {
                  "location": "outgoing",
                  "name": "mappedInput",
                  "ptr": "/input_label"
                },
                "context": "#"
              }
            ],
            "functions": [],
            "name": "mapInputVariables",
            "view": {
              "col": 1,
              "row": 4
            },
            "id": "mapInputVariables",
            "comments": []
          }
        ],
        "comments": [],
        "view": {
          "col": 1,
          "row": 5
        },
        "created": "2025-01-23T14:23:31.488Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:06:05.892Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 11,
      "reference": "64ff61c85449f701414638da",
      "type": "transformation",
      "folder": "/Get Service Catalog Inputs",
      "document": {
        "_id": "64ff61c85449f701414638da",
        "name": "Get ID of Service Catalog Found",
        "description": "Gets ID of Service Catalog matching search",
        "incoming": [
          {
            "$id": "serviceCatalogResults",
            "type": "object",
            "properties": {
              "response": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "examples": ["186d917a6fab7980575967ddbb3ee4f2"]
                    }
                  },
                  "required": []
                }
              }
            },
            "required": []
          }
        ],
        "outgoing": [
          {
            "$id": "serviceCatalogId",
            "type": "string",
            "examples": ["id"]
          }
        ],
        "steps": [
          {
            "id": 2,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "serviceCatalogResults",
              "ptr": "/response"
            },
            "to": {
              "location": "method",
              "name": 1,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 1,
            "type": "method",
            "library": "Array",
            "method": "shift",
            "args": [null],
            "view": {
              "row": 1,
              "col": 1
            },
            "context": "#"
          },
          {
            "id": 7,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 1,
              "ptr": "/return/value"
            },
            "to": {
              "location": "method",
              "name": 6,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 6,
            "type": "method",
            "library": "Logical",
            "method": "nullish",
            "args": [
              null,
              {
                "id": "No match found"
              }
            ],
            "view": {
              "row": 1,
              "col": 2
            },
            "context": "#"
          },
          {
            "id": 8,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 6,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 3,
              "ptr": "/args/0/value"
            },
            "context": "#"
          },
          {
            "id": 3,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "id"],
            "view": {
              "row": 1,
              "col": 3
            },
            "context": "#"
          },
          {
            "id": 5,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 3,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "serviceCatalogId",
              "ptr": ""
            },
            "context": "#"
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 3,
          "row": 5
        },
        "created": "2025-01-23T14:23:31.502Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:06:05.903Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 12,
      "reference": "62279f8c7858d601db6606f9",
      "type": "transformation",
      "folder": "/Create Request Item (RITM)",
      "document": {
        "_id": "62279f8c7858d601db6606f9",
        "name": "Build RITM Update Payload",
        "description": "",
        "incoming": [
          {
            "$id": "requestItemResponse",
            "type": "object",
            "properties": {
              "response": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "examples": ["a68d46e49712011015c5b4b3f153af9e"]
                    },
                    "current_state": {
                      "type": "string",
                      "examples": ["-5"]
                    }
                  },
                  "required": []
                }
              }
            },
            "required": []
          },
          {
            "$id": "comments",
            "type": "string"
          },
          {
            "$id": "state",
            "type": "string"
          }
        ],
        "outgoing": [
          {
            "$id": "ritmSysId",
            "type": "string"
          },
          {
            "$id": "ritmUpdatePayload",
            "type": "object",
            "properties": {
              "comments": {
                "type": "string"
              },
              "state": {
                "type": "integer",
                "examples": [0]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 4,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "comments",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "ritmUpdatePayload",
              "ptr": "/comments"
            }
          },
          {
            "id": 5,
            "type": "method",
            "library": "String",
            "method": "toLowerCase",
            "args": [null],
            "view": {
              "row": 3,
              "col": 1
            }
          },
          {
            "id": 6,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "state",
              "ptr": ""
            },
            "to": {
              "location": "method",
              "name": 5,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 7,
            "type": "method",
            "library": "JSON",
            "method": "parse",
            "args": [
              "{   \"pending\": 0,   \"open\": 1,   \"work in progress\": 2,   \"closed Complete\": 3,   \"closed incomplete\": 4,   \"closed skipped\": 5 }",
              null
            ],
            "view": {
              "row": 4,
              "col": 1
            }
          },
          {
            "id": 8,
            "type": "method",
            "library": "Object",
            "method": "optional chaining",
            "args": [null, null],
            "view": {
              "row": 3,
              "col": 2
            }
          },
          {
            "id": 9,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 7,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 8,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 10,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 5,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 8,
              "ptr": "/args/1/value"
            }
          },
          {
            "id": 17,
            "type": "method",
            "library": "Logical",
            "method": "nullish",
            "args": [null, null],
            "view": {
              "row": 3,
              "col": 3
            }
          },
          {
            "id": 18,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 8,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 17,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 20,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 17,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "ritmUpdatePayload",
              "ptr": "/state"
            }
          },
          {
            "id": 21,
            "type": "method",
            "library": "Number",
            "method": "parseInt",
            "args": [null, null],
            "view": {
              "row": 2,
              "col": 2
            }
          },
          {
            "id": 23,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 21,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 17,
              "ptr": "/args/1/value"
            }
          },
          {
            "id": 24,
            "type": "method",
            "library": "Array",
            "method": "getIndex",
            "args": [null, 0],
            "view": {
              "row": 1,
              "col": 1
            }
          },
          {
            "id": 25,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "id"],
            "view": {
              "row": 1,
              "col": 2
            }
          },
          {
            "id": 26,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "current_state"],
            "view": {
              "row": 2,
              "col": 1
            }
          },
          {
            "id": 27,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 24,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 25,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 28,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "requestItemResponse",
              "ptr": "/response"
            },
            "to": {
              "location": "method",
              "name": 24,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 29,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 25,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "ritmSysId",
              "ptr": ""
            }
          },
          {
            "id": 30,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 24,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 26,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 31,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 26,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 21,
              "ptr": "/args/0/value"
            }
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 3,
          "row": 5
        },
        "created": "2025-01-23T14:23:31.505Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:06:05.904Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 13,
      "reference": "622785287858d601db6606f8",
      "type": "transformation",
      "folder": "/Update Incident",
      "document": {
        "_id": "622785287858d601db6606f8",
        "name": "Build Incident Update Payload",
        "description": "",
        "incoming": [
          {
            "$id": "incidentResponse",
            "type": "object",
            "properties": {
              "response": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "examples": ["a68d46e49712011015c5b4b3f153af9e"]
                    },
                    "current_state": {
                      "type": "string",
                      "examples": ["-5"]
                    }
                  },
                  "required": []
                }
              }
            },
            "required": []
          },
          {
            "$id": "comments",
            "type": "string"
          },
          {
            "$id": "state",
            "type": "string"
          }
        ],
        "outgoing": [
          {
            "$id": "incSysId",
            "type": "string"
          },
          {
            "$id": "incUpdatePayload",
            "type": "object",
            "properties": {
              "comments": {
                "type": "string"
              },
              "state": {
                "type": "integer",
                "examples": [0]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 4,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "comments",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "incUpdatePayload",
              "ptr": "/comments"
            }
          },
          {
            "id": 5,
            "type": "method",
            "library": "String",
            "method": "toLowerCase",
            "args": [null],
            "view": {
              "row": 3,
              "col": 1
            }
          },
          {
            "id": 6,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "state",
              "ptr": ""
            },
            "to": {
              "location": "method",
              "name": 5,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 7,
            "type": "method",
            "library": "JSON",
            "method": "parse",
            "args": [
              "{   \"new\": 1,   \"in progress\": 2,   \"on hold\": 3,   \"resolved\": 6,   \"closed\": 7,   \"canceled\": 8 }",
              null
            ],
            "view": {
              "row": 4,
              "col": 1
            }
          },
          {
            "id": 8,
            "type": "method",
            "library": "Object",
            "method": "optional chaining",
            "args": [null, null],
            "view": {
              "row": 3,
              "col": 2
            }
          },
          {
            "id": 9,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 7,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 8,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 10,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 5,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 8,
              "ptr": "/args/1/value"
            }
          },
          {
            "id": 17,
            "type": "method",
            "library": "Logical",
            "method": "nullish",
            "args": [null, null],
            "view": {
              "row": 3,
              "col": 3
            }
          },
          {
            "id": 18,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 8,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 17,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 20,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 17,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "incUpdatePayload",
              "ptr": "/state"
            }
          },
          {
            "id": 21,
            "type": "method",
            "library": "Number",
            "method": "parseInt",
            "args": [null, null],
            "view": {
              "row": 2,
              "col": 2
            }
          },
          {
            "id": 23,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 21,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 17,
              "ptr": "/args/1/value"
            }
          },
          {
            "id": 24,
            "type": "method",
            "library": "Array",
            "method": "getIndex",
            "args": [null, 0],
            "view": {
              "row": 1,
              "col": 1
            }
          },
          {
            "id": 25,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "incidentResponse",
              "ptr": "/response"
            },
            "to": {
              "location": "method",
              "name": 24,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 26,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "id"],
            "view": {
              "row": 1,
              "col": 2
            }
          },
          {
            "id": 27,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 24,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 26,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 28,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 26,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "incSysId",
              "ptr": ""
            }
          },
          {
            "id": 29,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "current_state"],
            "view": {
              "row": 2,
              "col": 1
            }
          },
          {
            "id": 30,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 24,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 29,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 31,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 29,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 21,
              "ptr": "/args/0/value"
            }
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 3,
          "row": 5
        },
        "created": "2025-01-23T14:23:31.506Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:06:05.904Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 14,
      "reference": "66d0b852cddf0c8da2752c6d",
      "type": "transformation",
      "folder": "/Update Change Request",
      "document": {
        "_id": "66d0b852cddf0c8da2752c6d",
        "name": "Build CR Update Payload",
        "description": "",
        "incoming": [
          {
            "$id": "changeRequestResponse",
            "type": "object",
            "properties": {
              "response": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "examples": ["a68d46e49712011015c5b4b3f153af9e"]
                    },
                    "current_state": {
                      "type": "string",
                      "examples": ["-5"]
                    }
                  },
                  "required": []
                }
              }
            },
            "required": []
          },
          {
            "$id": "comments",
            "type": "string"
          },
          {
            "$id": "state",
            "type": "string"
          }
        ],
        "outgoing": [
          {
            "$id": "crSysId",
            "type": "string"
          },
          {
            "$id": "crUpdatePayload",
            "type": "object",
            "properties": {
              "comments": {
                "type": "string"
              },
              "state": {
                "type": "integer",
                "examples": [0]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 4,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "comments",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "crUpdatePayload",
              "ptr": "/comments"
            }
          },
          {
            "id": 5,
            "type": "method",
            "library": "String",
            "method": "toLowerCase",
            "args": [null],
            "view": {
              "row": 3,
              "col": 1
            }
          },
          {
            "id": 6,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "state",
              "ptr": ""
            },
            "to": {
              "location": "method",
              "name": 5,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 7,
            "type": "method",
            "library": "JSON",
            "method": "parse",
            "args": [
              "{    \"new\": -5,   \"assess\": -4,   \"authorize\": -3,   \"scheduled\": -2,   \"implement\": -1,   \"review\": 0,   \"closed\": -6,   \"canceled\": -7 }",
              null
            ],
            "view": {
              "row": 4,
              "col": 1
            }
          },
          {
            "id": 8,
            "type": "method",
            "library": "Object",
            "method": "optional chaining",
            "args": [null, null],
            "view": {
              "row": 3,
              "col": 2
            }
          },
          {
            "id": 9,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 7,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 8,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 10,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 5,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 8,
              "ptr": "/args/1/value"
            }
          },
          {
            "id": 17,
            "type": "method",
            "library": "Logical",
            "method": "nullish",
            "args": [null, null],
            "view": {
              "row": 3,
              "col": 3
            }
          },
          {
            "id": 18,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 8,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 17,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 20,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 17,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "crUpdatePayload",
              "ptr": "/state"
            }
          },
          {
            "id": 21,
            "type": "method",
            "library": "Number",
            "method": "parseInt",
            "args": [null, null],
            "view": {
              "row": 2,
              "col": 2
            }
          },
          {
            "id": 23,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 21,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 17,
              "ptr": "/args/1/value"
            }
          },
          {
            "id": 24,
            "type": "method",
            "library": "Array",
            "method": "getIndex",
            "args": [null, 0],
            "view": {
              "row": 1,
              "col": 1
            }
          },
          {
            "id": 25,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "changeRequestResponse",
              "ptr": "/response"
            },
            "to": {
              "location": "method",
              "name": 24,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 26,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "current_state"],
            "view": {
              "row": 2,
              "col": 1
            }
          },
          {
            "id": 27,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 24,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 26,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 28,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 26,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 21,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 29,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "id"],
            "view": {
              "row": 1,
              "col": 2
            }
          },
          {
            "id": 30,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 24,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 29,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 31,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 29,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "crSysId",
              "ptr": ""
            }
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 3,
          "row": 5
        },
        "created": "2025-01-23T14:23:31.504Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:06:05.903Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    },
    {
      "iid": 15,
      "reference": "63d1a03fa15c2401e9a6143c",
      "type": "transformation",
      "folder": "/Close Change Request",
      "document": {
        "_id": "63d1a03fa15c2401e9a6143c",
        "name": "Build CR Close Payload",
        "description": "",
        "incoming": [
          {
            "$id": "changeRequestResponse",
            "type": "object",
            "properties": {
              "response": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "examples": ["a68d46e49712011015c5b4b3f153af9e"]
                    },
                    "current_state": {
                      "type": "string",
                      "examples": ["-5"]
                    }
                  },
                  "required": []
                }
              }
            },
            "required": []
          },
          {
            "$id": "closeCode",
            "type": "string"
          },
          {
            "$id": "closeNotes",
            "type": "string"
          }
        ],
        "outgoing": [
          {
            "$id": "crSysId",
            "type": "string"
          },
          {
            "$id": "crClosePayload",
            "type": "object",
            "properties": {
              "close_code": {
                "type": "string"
              },
              "close_notes": {
                "type": "string"
              },
              "state": {
                "type": "number",
                "examples": [0]
              }
            },
            "required": []
          }
        ],
        "steps": [
          {
            "id": 24,
            "type": "method",
            "library": "Array",
            "method": "getIndex",
            "args": [null, 0],
            "view": {
              "row": 1,
              "col": 1
            }
          },
          {
            "id": 25,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "changeRequestResponse",
              "ptr": "/response"
            },
            "to": {
              "location": "method",
              "name": 24,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 29,
            "type": "method",
            "library": "Object",
            "method": "getProperty",
            "args": [null, "id"],
            "view": {
              "row": 1,
              "col": 2
            }
          },
          {
            "id": 30,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 24,
              "ptr": "/return"
            },
            "to": {
              "location": "method",
              "name": 29,
              "ptr": "/args/0/value"
            }
          },
          {
            "id": 31,
            "type": "assign",
            "from": {
              "location": "method",
              "name": 29,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "crSysId",
              "ptr": ""
            }
          },
          {
            "id": 32,
            "type": "declaration",
            "library": "Number",
            "method": "new Number",
            "args": [3],
            "view": {
              "row": 3,
              "col": 1
            }
          },
          {
            "id": 33,
            "type": "assign",
            "from": {
              "location": "declaration",
              "name": 32,
              "ptr": "/return"
            },
            "to": {
              "location": "outgoing",
              "name": "crClosePayload",
              "ptr": "/state"
            }
          },
          {
            "id": 34,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "closeCode",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "crClosePayload",
              "ptr": "/close_code"
            }
          },
          {
            "id": 35,
            "type": "assign",
            "from": {
              "location": "incoming",
              "name": "closeNotes",
              "ptr": ""
            },
            "to": {
              "location": "outgoing",
              "name": "crClosePayload",
              "ptr": "/close_notes"
            }
          }
        ],
        "functions": [],
        "comments": [],
        "view": {
          "col": 2,
          "row": 5
        },
        "created": "2025-01-23T14:23:31.509Z",
        "createdBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "lastUpdated": "2025-01-24T11:06:05.905Z",
        "lastUpdatedBy": {
          "_id": "66d1e2b552e6dc384b5d6626",
          "provenance": "Okta",
          "username": "admin@itential"
        },
        "version": "4.3.6-2023.2.5",
        "tags": []
      }
    }
  ],
  "folders": [
    {
      "nodeType": "folder",
      "name": "Update Change Request",
      "children": [
        {
          "iid": 14,
          "nodeType": "component"
        },
        {
          "iid": 6,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Close Change Request",
      "children": [
        {
          "iid": 0,
          "nodeType": "component"
        },
        {
          "iid": 15,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Update Incident",
      "children": [
        {
          "iid": 7,
          "nodeType": "component"
        },
        {
          "iid": 13,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Create Request Item (RITM)",
      "children": [
        {
          "iid": 2,
          "nodeType": "component"
        },
        {
          "iid": 12,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Get Service Catalog Inputs",
      "children": [
        {
          "iid": 9,
          "nodeType": "component"
        },
        {
          "iid": 11,
          "nodeType": "component"
        },
        {
          "iid": 10,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Create Change Request",
      "children": [
        {
          "iid": 3,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Create Incident",
      "children": [
        {
          "iid": 8,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Approve Change Request",
      "children": [
        {
          "iid": 5,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Update Request Item",
      "children": [
        {
          "iid": 1,
          "nodeType": "component"
        }
      ]
    }
  ],
  "created": "2024-08-29T18:05:54.354Z",
  "createdBy": {
    "_id": "6786b32af921f091fd105007",
    "provenance": "Local AAA",
    "username": "admin@itential"
  },
  "lastUpdated": "2025-01-24T11:06:05.874Z",
  "lastUpdatedBy": {
    "_id": "66d1e2b552e6dc384b5d6626",
    "provenance": "Okta",
    "username": "admin@itential"
  },
  "iid": 53,
  "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAdYAAAEsCAMAAABJzWIXAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAaVBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABi2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E5i2E4AAABi2E7///9rzh2VAAAAIHRSTlMAAECAUN/vYJ9wEL8gj8+vMCBgn7/fgFAQcM/vQDCPrwH8eukAAAABYktHRACIBR1IAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH6AcSEgkLJ0FllAAADHxJREFUeNrtnOmWmkwQhiPIIqAya2ZL4tz/TX7qCFRVF5tOjt8xz/MrE9pe6q3eqht+/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIC/xeL/TRTH8fLalbgutyfrMtkdSLNrV+Sa3Jys2a4hv3ZVrsitybrcdayuXZnrcWuyJkLWtLh2ba7GjckqO+tu9+9Orzcma6xk/Xdn15uWtbx2da7GTctKb70RWTMl67+7FL4xWYtUylpduzpX48ZkVaPw+tqVuR63JuuibFXd/Lvb1tuTdbE+qbr9h1W9QVkX1bosy3V97WpclRuUFZD1RkHWmwRZb5KLZV2uT1uKpIyjnkKKLD8lKvMsWKAWUcspflBncb5f9cT7P6vuYU/uIkGt/yyGarLb5KuBcEUdl6dbFmVcD5RZayOU6/HbNnf3D4+fR54en3+aYgdqX/UborYmvEzWKldRnV2aO62KtirNLjfWjLpH8SHPdXtmGumTNvecLTIJxJ9B85emJruNf3RXxIlKlthk6jTBpE7zoeDWy+vbp+L94UM8zgcC2nlvw2RsLbpY1mK9C7EmqMowTa48UclaiYYdqyhMtvHsJJQ6Hpv3yxolYU3cK0+rNEiWaHeVsjqp131b5pfn98+Qx05YYYvUatevuIiEJ4tLZa09Mx2sL83pNPpQZZlEyqqTR7rKO2cYrsTjWFtcJy+2O5+NGWM9P7SuKH7tpk78XfOrJ+pR2LsmibCpcThhCKu4qMPqUllrV7BjU7sC8740os7SQ3Wioy7i/7ahpWQBxYCs/bU19utNKGORu1GcQeDl8bOX9/umG/S2tuzNXbp2caGsVb+dOnP2qiprFg1nJIP3wawlZ5XcWlzImg2oqga1AfmFruOyhrr+ev8c4uHUoL7WSu2M4sJCTUvOlnXT26Du4GRAVdHuEVlD5fwWnazgyprthmnzHerUQtcJstoZY0TVva4v1marvpYaxZOw0HNl7TdU0jZ+tRsibeafEVllQ4O7hKJF28DirWEHxTpycsUiGUzVqj9FVl3XUVWb/iqskfS01Ci+dH5xrqz97W+NWY0Ys5mCx2QNVkUdznrKqUkxqmpTl/VIsmY9PEVWNbTcjava6Or0vdBIclPg9e8zZa11Ies4zk+jcjfsqzVistrXMVopb1hNk1XWWzmwmgma62iOrNvdGKdDPF2TfFktqqWaSJoeOEnWXbccfnmboOrn570ZbYVj5L15u7PxmbLK8XVzyqw6bMu7oUfaqNsdyh+mnjFPeZZl2epiIw6uCzcPQllt/sl6FS3jrTNlS0fcNiaq5Coi7pE1yeMoWpngTKfK70mqfr7f6cGpM2Yw4HQLGHftfKaswqUSMYfEu27bLmyUim2cHDdXvqxNqKquwqxUd906/x/KqueLsh2as+ZBM7LLioiOUghdU1fWLk9/YfNrmqr7/atpVevEwVKm27qK2nXGv1xWNd11K7Ra1EFtzoV3JZ6seRiikSnEfCMn3dYAQVJlERVUKnL9U2FPtYMoghiBtrCMQEWyWzVTXbBhffp9//Hx8fwn0PUQIhZLoNKpmpFQ2Fm4/Df01oWLWH2YdY4wUh3ImrqhcvETcaXbXSIHssqRNTXRn0wWWHjZWc/YBrKaK1NyljnV9cNo99bG94Ng4pNpbTO/Baq2w4lv58tl7bk01NXN7kqEkdZW1tSPuske1w4Icr7pWmRlVRYJfCYWBWZedoFb2VBWcBFOutHX/5jO+ipT35nF1CE8HA6F3lbxVK4wgtjMnimreoUpXYdnFsKaef+j0sradwMpcbKLwzY6skqPcG75i5rn/dXITaa2EMnSPrzTy6IPk/4h2OQIAyVB81sy64ty4jhT1sKUsbFnl2NxHeHOkfnbw5PQkzq0+Nb55ajrDDB4nmBrcDT9azB7anRnftF1PmZfexX5GuFFUjkUnSmrExfcrKTV4t0k6omyOgOuOzCHFvfF95hW4+2orGIUjgPZfoflvrxb2Zemzn4Q9tDosGNfJqsbQsojr21DRBNllSuD09peLOzl8GMtLv4evrjQHxVRlKOyig50lFUtiV6cku8D3YVxC/3nTmcuJl31DsO5spoXhNtGO1vNIZZTZQ02Mz2bHmtx+bvhV3ImyrqZK6taBz+7RT/Zratw4kyb2mzVw0XzhbL2zZ6rWbLGU2UNIoiifeo1VmPxaZnPkHU3KqsZhFVfvHOLlkGod+PEG91U6aa1rLN+l/d8WftuR+R/R9Zam1I2Tw2u/ztZn+WO1S9adWibRyWXp5mce3Lp6/p89wJZD7u+Xl2/exBWOZYD4f+/Lev4IDwg64Nf9EvQoeXeXsyfaaHuvoiFpLkHc5Gsi2Ll9djVdFlnWF4mMx48IGvvbYNzZR1fMhlZZYTwuadsG5CQq6RE9U/VIFGSeenzMlkP1siDLnsIK4kSowGKGR1KblXE/sn4qbW4+HvySjgfqHE9V9aHs2T1T34PhfXvdr5T1oVz/XYVxmUmdpOhdHKN5sYNXVm1rw9gg19DzJH1eaasd7Y2Hcfpxt2C2Bp/h6zBYLzp31BdIKsfBrIRZ2tx6dzDo7DZLP4NWR/97NTB3en/vLtica8Z7IW475HVnjT2X8m5RFY3cmW7oLW47OPehdSus3vnnN8gq4wdvvvZvTqyevvHL7d0xufgjtd3yapPGSLl+yMfXJksq3snyfZAa3EVvQ7k2huvbEwiD4JHuuscWdXu5aeb3ZvToZ3Gni4wDZzSfYOsmV2B6LbKw9DwXCYXFZm+B1lPaFBgcbXE8G7KN68YVEPZ7nfp9UAhA7KqidMdhZXwbdA4XBo1lQ/H58DAZ8tapfZVE93WWrqZdf5cGm66rI6fBlYNnumNi1xgte9vnIYTufKz/bpOpXfOkvVtrLs+ugnqnaWxYjA+hy8nnS3rofJppu4xae+RO1f9Tkq9UR1iuqyhB4dr1tDiegudNHWuRDDl6yaAcgC90Ds2rtN1lqxq5jzeQtPINdXXwdwXtlO2BrOnosIH6zjOqgtkPU1E7ZuP6k234Bh138DWAercVHOGrIEHh1vR0OLBj8p1HG/Nq4514ADdS3LtOr/VdZasd0q2N3uGo2LGn3+6B7ZTdm01G8p2wVSUyTrOD6WeKas8l0vKstSeVXpdaxtHhzuX4fnnDFlt8MpZZDsWH7vUfeSgmDltTNZZFC1j5wrlLFnNOfnTr4G+Kgdps2gSbTVb17Ybb47/qjbxubIOxwa/BoVi9LpBPlvWyCtoTNaB94U6pzsmXI0lO+k6T1Z7Re1312E/zFWmJ5mR7hdyVtCCN2PIqlxkZbneL0Gq82Qdbn7jV+OvvkRzZdUKpU4Cz+Ljb2s0i7p8LGF5hqzhhdI/rx+/Xj5+/n6yD+5lRrUqWe7k1PjTLpjK5SIuqyRa5KuzZB15u6adBMYuNGWze6vOMnYSuBYfc7Buqb6ZlHCmrLa79mL2P3K4U6tdJXgbFthbL07WabWI47NkXQ42XYwWw6+VnobQWbLKprrf4vctXg9OCGIDVpRTEs6UderLGp962lWDop5vpPd1LrkXNCn308mZsi7qgcarnfxAN2k/NDBP1lVPScOyDsql3yNYT0g4V9bg1arHh+fn50c7Br+anOROpveSeWeFPD4MwvvpP4nOXDItsh73t5/Y6P1kQ+6+gzUuq5gn3ch9r8XjHg8L3iNY9iQUnwWZK6t6vVV82+XuXk674SF7N9UbFy68CuwVrepFXcWbS4KH3jTkfLwm8vpJKawxT9Yu7OGfs/VbvPLWQ2kcjuSF5wEq4WxZu0Oa92e9cf1ohXVuxHSmsb7X9ha5x8sOlay3SXVRqL9ea2W92/3Hyhl7JvrzoTNlrfoNOmbxynxvabfJ/Jh+cOtjm00uxJd18fOrv3bfdAmeeHdNm2oEa/52eaPOUeptuksO/neJrAdDLeNtWaZpWearoU+97jf1ZXr4JNlIur9Ola3LY9yzLL/CbP0J82OQZbNPuPyOTxPfPTy9P977T956npzNWbICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAFP4DiSXcAIXfUFEAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjQtMDctMThUMTc6MjQ6MzIrMDA6MDBGXcLqAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDI0LTA3LTE4VDE3OjI0OjMyKzAwOjAwNwB6VgAAAABJRU5ErkJggg==",
  "backgroundColor": "#FFFFFF"
}

````

============================================================
FILE: helpers/create/create-command-template.json
DIRECTORY: helpers/create/
FILENAME: create-command-template.json
============================================================
SHA256: 02f04e1a20595f058b8acf6de9d3e3a368a67240ebc27cb51d4cbdec1f4f76de

````json
{
  "mop": {
    "name": "REPLACE_TEMPLATE_NAME",
    "description": "REPLACE_DESCRIPTION",
    "os": "",
    "passRule": true,
    "commands": [
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
    ]
  }
}

````

============================================================
FILE: helpers/create/create-compliance-plan.json
DIRECTORY: helpers/create/
FILENAME: create-compliance-plan.json
============================================================
SHA256: 1e0cbea0a26a2feeb245fe670827b1f577fb503262e2b34ffd9e1d65923d6d43

````json
{
  "name": "REPLACE_PLAN_NAME",
  "options": {
    "description": "REPLACE_DESCRIPTION",
    "nodes": [
      {
        "treeId": "REPLACE_TREE_ID_1",
        "version": "initial",
        "nodeId": "REPLACE_NODE_CONFIG_ID_1",
        "devices": ["IOS-CAT8KV-1"],
        "deviceGroups": [],
        "variables": {}
      },
      {
        "treeId": "REPLACE_TREE_ID_2",
        "version": "initial",
        "nodeId": "REPLACE_NODE_CONFIG_ID_2",
        "devices": ["XRV9K-ATL-1"],
        "deviceGroups": [],
        "variables": {}
      },
      {
        "treeId": "REPLACE_TREE_ID_3",
        "version": "initial",
        "nodeId": "REPLACE_NODE_CONFIG_ID_3",
        "devices": ["NX-ATL-LEAF-01"],
        "deviceGroups": [],
        "variables": {}
      }
    ]
  }
}

````

============================================================
FILE: helpers/create/create-flowagent-decorator.json
DIRECTORY: helpers/create/
FILENAME: create-flowagent-decorator.json
============================================================
SHA256: 0041d02fdfdf1017ac3e6472eccd566ba7d35b9bee0978ed6bf5905c59f8d7f2

````json
{
  "_comment": "A tool decorator -- replaces the ENTIRE inputSchema an LLM sees for one tool. Use when a tool's native schema is too vague and the LLM sends wrong or incomplete inputs.",
  "_usage": "POST /tools/decorators",
  "_schema_freshness_warning": "referenceId and every field inside toolInputSchema must match a REAL tool on your platform. Call GET /tools/{referenceId} first to see the tool's actual native schema, and test it directly to confirm every field the underlying adapter truly requires -- see SKILL.md 'Verifying This Skill Against Your Platform'.",
  "toolDecorator": {
    "referenceId": "REPLACE_TOOL_REFERENCE_ID",
    "name": "REPLACE_DECORATOR_NAME",
    "description": "REPLACE_DESCRIPTION -- what this decorator customizes and why",
    "toolDescription": "REPLACE_DESCRIPTION_THE_LLM_SEES -- be explicit about which fields are required and why",
    "toolInputSchema": {
      "type": "object",
      "properties": {
        "REPLACE_FIELD_NAME": {
          "type": "string",
          "description": "REPLACE -- what this field is for, and whether it's required"
        }
      },
      "required": ["REPLACE_FIELD_NAME"]
    }
  }
}

````

============================================================
FILE: helpers/create/create-flowagent-project-bundle.json
DIRECTORY: helpers/create/
FILENAME: create-flowagent-project-bundle.json
============================================================
SHA256: f0421d325d4aabd9faaf6d7323bc6d93f55dfff2e158d9275ee4dc66454969a0

````json
{
  "_comment": "A real, importable FlowAI Agent Project Bundle. Shows the exact structure the platform expects for a project + one agent + tools + a decorator. Edit this file locally, then import it atomically instead of creating a project and adding agents one call at a time.",
  "_usage": "POST /agent-project-service/project-bundles/import with body: { \"bundle\": <the 'bundle' object below>, \"conflictMode\": \"keep-both\", \"providerResolutions\": {...} }",
  "_provider_resolution_note": "provider is referenced by {profileName, modelName} here, not by UUID. Both must already exist in the target environment (GET /model-registry-service/profiles) or be remapped on import via providerResolutions.",
  "_schema_freshness_warning": "The REPLACE_* placeholders below (tool referenceIds, decoratorId) are structural examples, not real values. Resolve real ones from your own platform before importing: GET /tools to find referenceIds, GET /tools/{referenceId} to confirm the tool's current inputSchema, and GET /tools/decorators/{id} to inspect an existing decorator. See SKILL.md 'Verifying This Skill Against Your Platform'.",
  "_template_variable_rule": "Every inputSchema property must appear as {{ propertyName }} somewhere in instructions, or agent create/import fails validation. This template already follows that rule (deviceName is used below) -- keep it true if you add or rename properties.",
  "bundle": {
    "name": "REPLACE_PROJECT_NAME",
    "description": "REPLACE_PROJECT_DESCRIPTION",
    "agentProjectBundleVersion": 1,
    "agents": [
      {
        "name": "REPLACE_AGENT_NAME",
        "description": "REPLACE_AGENT_DESCRIPTION",
        "instructions": "You are a network diagnostics agent. Run a diagnostic check against {{ deviceName }} using the available tools. Summarize the result in 2-3 sentences. If the device is unreachable or reports an error, create a ServiceNow incident with short_description set to 'Diagnostic failure - {{ deviceName }}' and description set to the full diagnostic summary. If everything looks healthy, do not create a ticket -- just report the summary.",
        "inputSchema": {
          "type": "object",
          "additionalProperties": false,
          "required": ["deviceName"],
          "properties": {
            "deviceName": { "type": "string" }
          }
        },
        "provider": { "profileName": "REPLACE_PROFILE_NAME", "modelName": "REPLACE_MODEL_NAME" },
        "tools": [
          { "referenceId": "REPLACE_REFERENCE_ID_FOR_DIAGNOSTIC_TOOL", "lastKnownName": "REPLACE_TOOL_NAME" },
          { "referenceId": "REPLACE_REFERENCE_ID_FOR_CREATE_INCIDENT_TOOL", "lastKnownName": "createIncident", "decoratorId": "REPLACE_DECORATOR_ID_OR_REMOVE_THIS_FIELD" }
        ]
      }
    ]
  }
}

````

============================================================
FILE: helpers/create/create-golden-config-node.json
DIRECTORY: helpers/create/
FILENAME: create-golden-config-node.json
============================================================
SHA256: b8c7c7b2e1fe987b94ebbdedde5b7a913295bc572755e7453a2c80af74c2b86a

````json
{
  "name": "REPLACE_NODE_NAME"
}

````

============================================================
FILE: helpers/create/create-golden-config-tree.json
DIRECTORY: helpers/create/
FILENAME: create-golden-config-tree.json
============================================================
SHA256: 3e105398a7fa8e02a28198cdd571aeca70c46108729f02bf9bbf652c8276e5cf

````json
{
  "name": "REPLACE_TREE_NAME",
  "deviceType": "cisco-ios"
}

````

============================================================
FILE: helpers/create/create-integration.json
DIRECTORY: helpers/create/
FILENAME: create-integration.json
============================================================
SHA256: 2009e71e95bb6b370cf3a4ef0a96688c7f36251e6b9be56e339beb04e38571cb

````json
{
  "_comment": "Virtual integration (adapter instance) — connects the platform to an external system via REST. POST /integrations. Body must be wrapped in 'properties' key. The model field must match an adapter model from the catalog (pattern: @itential/adapter_<Name>:<version>). properties.id must equal name. properties.type is the adapter version type string. Authentication shape is model-specific — replace the authentication block with the one from GET /integration-models.",
  "properties": {
    "name": "REPLACE_integration_name",
    "model": "REPLACE_@itential/adapter_ModelName:version",
    "type": "Adapter",
    "virtual": true,
    "isEncrypted": false,
    "loggerProps": {
      "log_max_files": 100,
      "log_max_file_size": 1048576,
      "log_level": "info",
      "log_directory": "/var/log/itential/platform",
      "log_filename": "platform.log",
      "console_level": "warn"
    },
    "properties": {
      "id": "REPLACE_integration_name",
      "type": "REPLACE_AdapterModelVersionType",
      "brokers": [],
      "groups": [],
      "properties": {
        "authentication": {
          "bearerAuth": "REPLACE_bearer_token"
        },
        "server": {
          "protocol": "https",
          "host": "REPLACE_host",
          "base_path": "REPLACE_base_path"
        },
        "tls": {
          "enabled": false,
          "rejectUnauthorized": true
        },
        "variables": {},
        "version": "REPLACE_version"
      }
    }
  }
}

````

============================================================
FILE: helpers/create/create-json-form-rest-bound.json
DIRECTORY: helpers/create/
FILENAME: create-json-form-rest-bound.json
============================================================
SHA256: 0fe1eaf6d8e715730f7480890696a349ea50184203cfe51cb8761aa7ac5f73a3

````json
{
  "_comment_overview": "JSON Form scaffold for POST /json-forms/forms with REST-BOUND dropdowns whose options are pulled live from an IAP endpoint, including a cascading dependency (aka field dependency, as the Studio UI labels it) where one dropdown's URL path parameter is fed by another field's selection. For static enum dropdowns use create-json-form.json instead.",

  "_comment_when_to_use": "Use this template when a dropdown's options should reflect live platform state (devices, inventories, projects, templates, etc.) rather than a hardcoded list. The example below builds a Site/Device cascade against Inventory Manager: dropdown 1 lists inventories, dropdown 2 lists nodes from the selected inventory.",

  "name": "",
  "description": "",

  "_comment_struct_top": "struct.type MUST be 'array'. Every REST-bound dropdown lives in struct.items[] AND must have a mirror entry in bindingSchema.properties.<customKey> below — Studio reverse-engineers bindingSchema from struct in the GUI but the server does not, so an API-created form needs both populated.",

  "struct": {
    "type": "array",
    "items": [
      {
        "_comment": "REST-bound dropdown (no cascade). Options come from GET base+href; the response is walked via sourcePointer to an array, and each item's sourceKeyPointer field becomes BOTH the value and the label (labelKeyPointer is unused). Keep enum/enumNames as empty arrays.",
        "nodeId": "unique-uuid-per-field-1",
        "type": "string",
        "title": "Site",
        "description": "Inventory from Inventory Manager",
        "placeholder": "Select a site",
        "required": false,
        "enum": [],
        "enumNames": [],
        "uniqueItems": false,
        "binding": true,
        "rel": "collection",
        "targetPointer": "/enum",
        "method": "GET",
        "base": "/inventory_manager",
        "href": "/v1/inventories",
        "sourcePointer": "/result/data",
        "sourceKeyPointer": "/name",
        "customKey": "site"
      },
      {
        "_comment_cascade": "CASCADING dropdown (the Studio UI labels this pattern 'field dependency'). Depends on the 'site' field above. The href stays as a TEMPLATE with :paramName placeholders (colon syntax, NOT curly braces). The variables array maps each placeholder to a JSON pointer into form data: reference '/site' fills :inventoryIdentifier with whatever value the 'site' field currently holds. originalHref preserves the unresolved template; href is a copy used at runtime. The same variables array MUST also appear inside bindingSchema.properties.device.binding:hyperSchema.links[0].variables below.",
        "nodeId": "unique-uuid-per-field-2",
        "type": "string",
        "title": "Device",
        "description": "Device (node) from the selected site's inventory",
        "placeholder": "Select a device",
        "required": false,
        "enum": [],
        "enumNames": [],
        "uniqueItems": false,
        "binding": true,
        "rel": "collection",
        "targetPointer": "/enum",
        "method": "GET",
        "base": "/inventory_manager",
        "originalHref": "/v1/inventories/:inventoryIdentifier/nodes",
        "href": "/v1/inventories/:inventoryIdentifier/nodes",
        "sourcePointer": "/result/data",
        "sourceKeyPointer": "/name",
        "variables": [
          { "name": "inventoryIdentifier", "reference": "/site" }
        ],
        "customKey": "device"
      }
    ]
  },

  "_comment_schema": "schema is the data contract — property keys must match customKey values from struct. For REST-bound fields the enum/enumNames stay empty here too.",
  "schema": {
    "title": "Site and Device Selector",
    "description": "Pick a site, then a device from that site",
    "type": "object",
    "required": [],
    "properties": {
      "site": {
        "type": "string",
        "title": "Site",
        "_id": "/properties/site",
        "description": "Inventory from Inventory Manager",
        "enum": [],
        "enumNames": []
      },
      "device": {
        "type": "string",
        "title": "Device",
        "_id": "/properties/device",
        "description": "Device (node) from the selected site's inventory",
        "enum": [],
        "enumNames": []
      }
    }
  },

  "_comment_uiSchema": "Cascading dropdowns require ui:widget 'DependencyWidget' on BOTH the source field and the dependent field. Without it the runtime will not re-fetch the dependent dropdown when the source changes.",
  "uiSchema": {
    "site": {
      "ui:placeholder": "Select a site",
      "ui:widget": "DependencyWidget"
    },
    "device": {
      "ui:placeholder": "Select a device",
      "ui:widget": "DependencyWidget"
    },
    "ui:order": ["site", "device", "*"]
  },

  "_comment_bindingSchema": "bindingSchema.properties.<customKey> must mirror every REST-bound field in struct. Keys use 'binding:'-prefixed names. binding:hyperSchema.links[0] holds the actual href + variables; binding:source holds the response-walking pointers. body:variables (note the 'body:' prefix) appears on dependent fields and is normally an empty array.",
  "bindingSchema": {
    "properties": {
      "site": {
        "binding:method": "GET",
        "binding:link": { "$ref": "/links", "rel": "collection" },
        "binding:target": { "propertyPointer": "/enum" },
        "binding:hyperSchema": {
          "type": "object",
          "base": "/inventory_manager",
          "links": [
            {
              "rel": "collection",
              "href": "/v1/inventories",
              "targetMediaType": "application/json",
              "targetSchema": { "$ref": "#" },
              "variables": []
            }
          ]
        },
        "binding:source": { "propertyPointer": "/result/data", "keyPointer": "/name" }
      },
      "device": {
        "binding:method": "GET",
        "binding:link": { "$ref": "/links", "rel": "collection" },
        "body:variables": [],
        "binding:target": { "propertyPointer": "/enum" },
        "binding:hyperSchema": {
          "type": "object",
          "base": "/inventory_manager",
          "links": [
            {
              "rel": "collection",
              "href": "/v1/inventories/:inventoryIdentifier/nodes",
              "targetMediaType": "application/json",
              "targetSchema": { "$ref": "#" },
              "variables": [
                { "name": "inventoryIdentifier", "reference": "/site" }
              ]
            }
          ]
        },
        "binding:source": { "propertyPointer": "/result/data", "keyPointer": "/name" }
      }
    }
  },

  "validationSchema": {},
  "tags": [],
  "version": "2020.1",

  "_comment_gotchas": [
    "struct.type MUST be 'array' — 'object' silently produces a form whose dropdowns never render correctly.",
    "Path parameters in href use :name colon syntax, NOT {name} curly braces.",
    "labelKeyPointer is ignored; both label and value come from sourceKeyPointer.",
    "Cascading needs three things together: (1) variables[] in struct.items, (2) the same variables[] inside bindingSchema...links[0], (3) ui:widget 'DependencyWidget' on both fields.",
    "To discover what endpoints are bindable, GET /automation-studio/json-forms/method-options — the same list Studio shows in its dropdown picker.",
    "Bulk delete: DELETE /json-forms/forms with body {\"ids\":[\"...\"]}. There is no DELETE /json-forms/forms/{id}.",
    "To UPDATE: PUT /json-forms/forms/{id} with body wrapped in {\"options\": {...}} including ALL fields — full replacement."
  ]
}

````

============================================================
FILE: helpers/create/create-json-form.json
DIRECTORY: helpers/create/
FILENAME: create-json-form.json
============================================================
SHA256: 3a375912a174aa6611473d5b02b1f5b22bd2c9d0e9303d9ad533ea47eb31f2a5

````json
{
  "name": "",
  "description": "",

  "struct": {
    "type": "array",
    "items": [
      {
        "nodeId": "unique-uuid-per-field-1",
        "type": "string",
        "title": "Device Name",
        "description": "Short hostname of the target device",
        "placeholder": "Enter device name",
        "required": true,
        "binding": false,
        "rel": "item",
        "targetPointer": "/default",
        "customKey": "device_name"
      },
      {
        "nodeId": "unique-uuid-per-field-2",
        "type": "string",
        "title": "Environment",
        "description": "Target environment",
        "placeholder": "Select an environment",
        "required": true,
        "binding": false,
        "rel": "collection",
        "targetPointer": "/enum",
        "enum": [
          {"id": "e1", "label": "Production", "value": "production"},
          {"id": "e2", "label": "Staging", "value": "staging"},
          {"id": "e3", "label": "Development", "value": "development"}
        ],
        "enumNames": [
          {"id": "e1", "label": "Production", "value": "Production"},
          {"id": "e2", "label": "Staging", "value": "Staging"},
          {"id": "e3", "label": "Development", "value": "Development"}
        ],
        "customKey": "environment"
      },
      {
        "nodeId": "unique-uuid-per-field-3",
        "type": "number",
        "title": "Timeout (seconds)",
        "description": "Operation timeout",
        "placeholder": "Enter timeout",
        "required": false,
        "default": 300,
        "customKey": "timeout"
      },
      {
        "nodeId": "unique-uuid-per-field-4",
        "type": "string",
        "title": "Comment",
        "description": "Free-text note",
        "placeholder": "Enter comment",
        "required": false,
        "binding": false,
        "rel": "item",
        "targetPointer": "/default",
        "default": "",
        "customKey": "comment"
      }
    ]
  },

  "schema": {
    "title": "Form Title Here",
    "description": "Form description here",
    "type": "object",
    "required": ["device_name", "environment"],
    "properties": {
      "device_name": {
        "type": "string",
        "title": "Device Name",
        "_id": "/properties/device_name",
        "description": "Short hostname of the target device"
      },
      "environment": {
        "type": "string",
        "title": "Environment",
        "_id": "/properties/environment",
        "description": "Target environment",
        "enum": ["production", "staging", "development"],
        "enumNames": ["Production", "Staging", "Development"]
      },
      "timeout": {
        "type": "number",
        "title": "Timeout (seconds)",
        "_id": "/properties/timeout",
        "description": "Operation timeout",
        "default": 300
      },
      "comment": {
        "type": "string",
        "title": "Comment",
        "_id": "/properties/comment",
        "description": "Free-text note"
      }
    }
  },

  "uiSchema": {
    "device_name": {"ui:placeholder": "Enter device name"},
    "environment": {"ui:placeholder": "Select an environment"},
    "timeout": {"ui:placeholder": "Enter timeout"},
    "comment": {"ui:placeholder": "Enter comment"}
  },

  "bindingSchema": {},
  "validationSchema": {},
  "tags": [],
  "version": "2020.1"
}

````

============================================================
FILE: helpers/create/create-lcm-resource-model.json
DIRECTORY: helpers/create/
FILENAME: create-lcm-resource-model.json
============================================================
SHA256: 389336ed82e3fa3cdd76e1a26bed86763149597b4eb1356b982f074f7addeba8

````json
{
  "_comment": "LCM Resource Model — defines the schema and lifecycle actions for a service type. POST /lifecycle-manager/resources. Actions link to workflows via 'workflow' (UUID or null). Pre/post JSTs are MongoDB ObjectIds (24-char hex) or null — transform data before/after the action workflow runs.",
  "name": "",
  "description": "",
  "schema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "title": "Name",
        "description": "Unique name for this resource instance"
      },
      "status": {
        "type": "string",
        "title": "Status",
        "enum": ["provisioned", "deprovisioned", "error"],
        "description": "Current lifecycle state"
      }
    },
    "required": ["name"]
  },
  "actions": [
    {
      "name": "Create",
      "description": "Provision a new instance",
      "type": "create",
      "workflow": null,
      "preWorkflowJst": null,
      "postWorkflowJst": null
    },
    {
      "name": "Delete",
      "description": "Deprovision and remove an instance",
      "type": "delete",
      "workflow": null,
      "preWorkflowJst": null,
      "postWorkflowJst": null
    },
    {
      "name": "Update",
      "description": "Modify an existing instance",
      "type": "update",
      "workflow": null,
      "preWorkflowJst": null,
      "postWorkflowJst": null
    }
  ]
}

````

============================================================
FILE: helpers/create/create-ops-manager-automation.json
DIRECTORY: helpers/create/
FILENAME: create-ops-manager-automation.json
============================================================
SHA256: 8125764195f15d2f0f57a460d9608a4aeeb309437fa9a53f408661c07d979458

````json
{
  "name": "REPLACE_AUTOMATION_NAME",
  "description": "REPLACE_DESCRIPTION",
  "componentName": "@REPLACE_PROJECT_ID: REPLACE_WORKFLOW_NAME",
  "componentType": "workflows",
  "componentId": "REPLACE_WORKFLOW_UUID",
  "gbac": {
    "write": [],
    "read": []
  }
}

````

============================================================
FILE: helpers/create/create-ops-manager-trigger-manual.json
DIRECTORY: helpers/create/
FILENAME: create-ops-manager-trigger-manual.json
============================================================
SHA256: 65d4a5093bf0688d7a0ca046446c486f9b4af29724633828553bb0bd830456a5

````json
{
  "name": "",
  "type": "manual",
  "enabled": true,
  "actionType": "automations",
  "actionId": "",
  "description": "",
  "formId": null,
  "legacyWrapper": false
}

````

============================================================
FILE: helpers/create/create-ops-manager-trigger-schedule.json
DIRECTORY: helpers/create/
FILENAME: create-ops-manager-trigger-schedule.json
============================================================
SHA256: f03724cd6488688b7bcaca9875e1a910227b077db06ce01f24592b3adbe17e4f

````json
{
  "_comment": "Scheduled trigger — runs the automation on a repeating interval. POST /operations-manager/triggers. Uses 'repeat' object (not cron syntax). 'processMissedRuns' is required. Fields 'schedule', 'schema', and 'jst' are NOT valid for schedule triggers — those belong to endpoint triggers only.",
  "name": "",
  "type": "schedule",
  "enabled": true,
  "actionType": "automations",
  "actionId": "",
  "description": "",
  "processMissedRuns": "none",
  "repeat": {
    "type": "repeating",
    "duration": {
      "unit": "hour",
      "quantity": 1
    },
    "action": "execute"
  }
}

````

============================================================
FILE: helpers/create/create-ops-manager-trigger.json
DIRECTORY: helpers/create/
FILENAME: create-ops-manager-trigger.json
============================================================
SHA256: f33401b088fa31a05a8c0eec929993447c5c48c3d7bd7dc263c34f62ef7c520e

````json
{
  "_comment": "API endpoint trigger — creates a REST endpoint that starts the automation. POST /operations-manager/triggers. routeName becomes the URL path segment.",
  "name": "",
  "type": "endpoint",
  "enabled": true,
  "actionType": "automations",
  "actionId": "",
  "description": "",
  "verb": "POST",
  "routeName": "",
  "schema": {
    "type": "object",
    "properties": {},
    "required": []
  },
  "jst": null
}

````

============================================================
FILE: helpers/create/create-project.json
DIRECTORY: helpers/create/
FILENAME: create-project.json
============================================================
SHA256: 19a6021a729561d7b6219615ab230ef3de96729e5a84d8592e5e0751d29e1203

````json
{
  "name": "REPLACE_PROJECT_NAME",
  "description": "REPLACE_DESCRIPTION"
}

````

============================================================
FILE: helpers/create/create-template-jinja2.json
DIRECTORY: helpers/create/
FILENAME: create-template-jinja2.json
============================================================
SHA256: 9ce272f10f38b98aa2fc67692c00c328691bc79af08a86fc7a9101a64a9cb8b8

````json
{
  "template": {
    "name": "REPLACE_NAME",
    "type": "jinja2",
    "group": "REPLACE_GROUP",
    "command": "",
    "description": "REPLACE_DESCRIPTION",
    "tags": [],
    "template": "<!DOCTYPE html>\n<html>\n<head>\n  <meta charset=\"UTF-8\">\n  <title>{{ report_title }}</title>\n</head>\n<body style=\"font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 40px;\">\n\n  <div style=\"background-color: #ffffff; padding: 24px; border-radius: 8px; max-width: 600px; margin: 0 auto; box-shadow: 0 2px 6px rgba(0,0,0,0.1);\">\n\n    <h2 style=\"color: #2c3e50; margin-top: 0;\">{{ report_title }}</h2>\n    <p style=\"color: #555555; font-size: 14px; line-height: 1.5;\">\n      {{ report_description }}\n    </p>\n\n    <table style=\"width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 14px;\">\n      <thead>\n        <tr style=\"background-color: #2c3e50; color: #ffffff; text-align: left;\">\n          <th style=\"padding: 10px; border: 1px solid #ddd;\">Device Name</th>\n          <th style=\"padding: 10px; border: 1px solid #ddd;\">Status</th>\n          <th style=\"padding: 10px; border: 1px solid #ddd;\">Last Checked</th>\n        </tr>\n      </thead>\n      <tbody>\n        {% for device in devices %}\n        <tr style=\"background-color: {{ '#f9f9f9' if loop.index % 2 == 1 else '#ffffff' }};\">\n          <td style=\"padding: 10px; border: 1px solid #ddd;\">{{ device.deviceName }}</td>\n          <td style=\"padding: 10px; border: 1px solid #ddd; color: {{ '#27ae60' if device.status == 'Online' else '#c0392b' }};\">\n            {{ device.status }}\n          </td>\n          <td style=\"padding: 10px; border: 1px solid #ddd;\">{{ device.lastChecked }}</td>\n        </tr>\n        {% endfor %}\n      </tbody>\n    </table>\n\n  </div>\n\n</body>\n</html>",
    "data": "{\n  \"report_title\": \"Device Status Report\",\n  \"report_description\": \"The following devices were checked as part of the automation job.\",\n  \"devices\": [\n    {\n      \"deviceName\": \"CSR1000V-EDGE-01\",\n      \"status\": \"Unreachable\",\n      \"lastChecked\": \"2026-06-30 09:15\"\n    },\n    {\n      \"deviceName\": \"ARISTA-CORE-03\",\n      \"status\": \"Online\",\n      \"lastChecked\": \"2026-06-30 09:15\"\n    }\n  ]\n}"
  }
}

````

============================================================
FILE: helpers/create/create-template-textfsm.json
DIRECTORY: helpers/create/
FILENAME: create-template-textfsm.json
============================================================
SHA256: a85505c05d2abe44e775f2165bb7adfc282a06abec483b80a041d876a008802b

````json
{
  "template": {
    "name": "REPLACE_NAME",
    "type": "textfsm",
    "group": "REPLACE_GROUP",
    "command": "show ip interface brief",
    "description": "REPLACE_DESCRIPTION",
    "tags": [],
    "template": "Value INTERFACE (\\S+)\nValue IP_ADDRESS (\\S+)\nValue STATUS (up|down|administratively down)\nValue PROTOCOL (up|down)\n\nStart\n  ^Interface\\s+IP-Address\\s+OK\\?\\s+Method\\s+Status\\s+Protocol\\s*$$\n  ^${INTERFACE}\\s+${IP_ADDRESS}\\s+\\S+\\s+\\S+\\s+${STATUS}\\s+${PROTOCOL}\\s*$$ -> Record\n  ^\\s*$$\n  ^. -> Error",
    "data": "Interface              IP-Address      OK? Method Status                Protocol\nGigabitEthernet0/0      10.0.0.1        YES NVRAM  up                    up\nGigabitEthernet0/1      unassigned      YES NVRAM  administratively down down\nLoopback0               192.168.1.1     YES NVRAM  up                    up"
  }
}

````

============================================================
FILE: helpers/create/create-workflow.json
DIRECTORY: helpers/create/
FILENAME: create-workflow.json
============================================================
SHA256: 268d864cef886a0c1c0723aba3057cd66faf9b912ee139e6220b8f9b78774130

````json
{
  "automation": {
    "name": "",
    "description": "",
    "type": "automation",
    "canvasVersion": 3,
    "encodingVersion": 1,
    "font_size": 12,
    "tasks": {
      "workflow_start": {
        "name": "workflow_start",
        "groups": [],
        "nodeLocation": { "x": 600, "y": 200 }
      },
      "workflow_end": {
        "name": "workflow_end",
        "groups": [],
        "nodeLocation": { "x": 600, "y": 312 }
      }
    },
    "transitions": {
      "workflow_start": {},
      "workflow_end": {}
    },
    "groups": [],
    "inputSchema": {
      "type": "object",
      "properties": {},
      "required": []
    },
    "outputSchema": {
      "type": "object",
      "properties": {}
    }
  }
}

````

============================================================
FILE: helpers/create/import-project.json
DIRECTORY: helpers/create/
FILENAME: import-project.json
============================================================
SHA256: 48d1bf58e53f3bb61befab7b2a8872448faf9ca847671b1e69a4ad5027d2bfa2

````json
{
  "_comment": "Import a project with all assets atomically. Pre-compute _id so childJob @projectId: refs can be wired before push.",
  "_membership_warning": "MANDATORY: After import, PATCH membership immediately. Import sets the OAuth service account as owner \u2014 not the UI user from the spec. See SKILL.md 'Resolve membership references from spec' for the lookup pattern.",
  "_usage": "POST /automation-studio/projects/import",
  "_id_generation": "python3 -c \"import secrets; print(secrets.token_hex(12))\"",
  "_uuid_generation": "python3 -c \"import uuid; print(uuid.uuid4())\"",
  "project": {
    "_id": "REPLACE_24_CHAR_HEX",
    "iid": 1,
    "name": "REPLACE_PROJECT_NAME",
    "description": "REPLACE_DESCRIPTION",
    "thumbnail": "",
    "backgroundColor": "#FFFFFF",
    "components": [
      {
        "_comment": "Workflow component \u2014 reference is a UUID, document is the full workflow object",
        "iid": 1,
        "type": "workflow",
        "reference": "REPLACE_UUID",
        "folder": "/",
        "document": {
          "name": "REPLACE_WORKFLOW_NAME",
          "description": "REPLACE_DESCRIPTION",
          "type": "automation",
          "canvasVersion": 3,
          "font_size": 12,
          "created": "2026-01-01T00:00:00.000Z",
          "last_updated": "2026-01-01T00:00:00.000Z",
          "last_updated_by": {
            "provenance": "CloudAAA",
            "username": "admin@itential",
            "firstname": "Admin",
            "inactive": false,
            "sso": false
          },
          "createdVersion": "2024.1",
          "lastUpdatedVersion": "2024.1",
          "migrationVersion": 1,
          "tags": [],
          "groups": [],
          "uuid": "REPLACE_SAME_UUID_AS_REFERENCE",
          "scenarios": [],
          "tasks": {
            "workflow_start": {
              "name": "workflow_start",
              "groups": [],
              "nodeLocation": {
                "x": 180,
                "y": 300
              }
            },
            "a1b2": {
              "name": "REPLACE_TASK_NAME",
              "canvasName": "REPLACE_CANVAS_NAME",
              "summary": "REPLACE_SUMMARY",
              "location": "Application",
              "locationType": null,
              "app": "WorkFlowEngine",
              "type": "operation",
              "displayName": "WorkFlowEngine",
              "variables": {
                "incoming": {},
                "outgoing": {},
                "error": "",
                "decorators": []
              },
              "groups": [],
              "nodeLocation": {
                "x": 540,
                "y": 300
              }
            },
            "workflow_end": {
              "name": "workflow_end",
              "groups": [],
              "nodeLocation": {
                "x": 900,
                "y": 300
              }
            }
          },
          "transitions": {
            "workflow_start": {
              "a1b2": {
                "type": "standard",
                "state": "success"
              }
            },
            "a1b2": {
              "workflow_end": {
                "type": "standard",
                "state": "success"
              }
            },
            "workflow_end": {}
          },
          "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
          },
          "outputSchema": {
            "type": "object",
            "properties": {}
          }
        }
      }
    ],
    "created": "2026-01-01T00:00:00.000Z",
    "createdBy": {
      "_comment": "Project-level createdBy HAS _id \u2014 different from workflow-level created_by",
      "_id": "000000000000000000000000",
      "provenance": "CloudAAA",
      "username": "admin@itential"
    },
    "lastUpdated": "2026-01-01T00:00:00.000Z",
    "lastUpdatedBy": {
      "_id": "000000000000000000000000",
      "provenance": "CloudAAA",
      "username": "admin@itential"
    }
  }
}

````

============================================================
FILE: helpers/documentation-output-templates.md
DIRECTORY: helpers/
FILENAME: documentation-output-templates.md
============================================================
SHA256: 7175ffbf8dc001d93246ae0ffe2f3912dce47bf8bbbd800d9434a09ce0ad2dbf

````markdown
# Documentation Output Templates

Templates for the three markdown files produced by the `/documentation` skill.

---

## customer-spec.md Template

```markdown
# {Use Case Name} - High-Level Design (HLD)

**Use Case:** {One-Line Description}
**Version:** {Version or build identifier, if discoverable from naming or descriptions}

> **Note:** This spec was produced by reading {numberOfAssets} {typeOfAssets}.
> Review and correct any inferences before using as a delivery baseline.

---

## 1. Problem Statement
{Write 1-2 RICH PARAGRAPHS of narrative prose. This is NOT a bullet list.

Paragraph 1: Describe the overall purpose and business context — what this automation does,
why it exists, what business problem it solves.

Paragraph 2: Describe the major functional areas or modes of operation — what systems are
integrated, what types of automation are covered, how they connect. Also describe the operator
experience — how users interact with the system, what entry points exist, what the operational
model looks like.

Infer from workflow descriptions, adapter usage, task summaries, OM trigger configurations,
LCM action names, golden config structure, and naming patterns.}

## 2. High-Level Flow

{Write 1-3 sentences describing the end-to-end execution from trigger to completion, using
business language. Cover: the entry point (who or what starts this), the major phases in
order, which external systems are touched and why, and what the final outcome is.
Do not use workflow names or technical task names — describe what happens, not what it's called.}

## 3. Phases
{One section per major workflow / childJob cluster / LCM action / golden config check stage}

## 4. Key Design Decisions
{Inferred from adapter choices, error handling patterns, approval gates, LCM action structure}

## 5. Scope
**In scope (as built):** {list components that exist}
**Not observed:** {common patterns not present — rollback, notifications, audit trail, etc.}

## 6. Risks & Mitigations
{Inferred from error transitions, evaluation branches}

## 7. Requirements

### Capabilities
{Derived from apps and tasks used}

### Integrations
{Derived from adapter names and instance IDs}

## 8. Batch Strategy
{Inferred from childJob loopType usage}

## 9. User Interaction Model

### 9.1 Entry Points

| Entry Point | Trigger | Description |
|---|---|---|
| {Entry point name} | {Manual launch / Scheduled / Endpoint trigger / LCM action / etc.} | {How this entry point works and what it initiates} |

### 9.2 Operator Workflow (Manual Path)

1. **{Action name}** — {Detailed description of what happens at this step, what the operator sees, what choices are available.}
2. **{Action name}** — {description}

### 9.3 Automated Path

1. {Step description — what triggers, what runs, what the system checks}
2. {Step description}

## 10. Integration Points

| System | Direction | Purpose |
|---|---|---|
| **{System name}** | {Bi-directional / Inbound / Outbound} | {What data flows and why, including specific operations} |

## 11. Acceptance Criteria
{Inferred from outputSchema and evaluation checks}
```

**For test/standalone use cases**, use a simplified catalog format — asset table with Purpose and Adapters columns only. No full HLD needed.

---

## solution-design.md Template

```markdown
# {Use Case Name} - Solution Design (LLD)

**Use Case:** {One-Line Description}
**Version:** {Version if discoverable}

> **As-Built** — produced by reading {numberOfAssets} {typeOfAssets}.
> Review and correct any inferences before using as a delivery baseline.

---

## A. Environment Summary
{Platform, adapters found, apps used}

## B. Component Inventory
| # | Component | Type | Name | Purpose | ID |
|---|-----------|------|------|---------|-----|
| 1 | {name} | {workflow/template/mop/golden-config/lcm} | {actual name} | {A sentence to describe what this item does, what systems it touches, and its role in the overall flow.} | {id} |

## C. Adapter Mappings
| Adapter | app name | adapter_id | Tasks Used |
|---------|----------|-----------|------------|
| ServiceNow | Servicenow | ServiceNow | createChangeRequest, updateChangeRequest |

## D. Execution Flow

**Draw.io Architecture Diagram**

Generate one file in the same directory as `solution-design.md`:
- `solution-design.drawio` — editable mxGraph XML diagram

**What to show:**
- Entry points (operators, OM triggers, LCM actions) at the top
- The orchestrator workflow below entry points
- Each child workflow in execution order, top to bottom
- External systems (adapters/integrations) called by each workflow, to the RIGHT of the calling workflow on the same horizontal band
- Arrow labels describing the operation (e.g., "childJob", "Create ticket", "Get device")

**What to exclude:**
- Workflows or connections marked as "not wired", inactive, or not yet implemented
- Alternative / optional execution paths — describe those in prose in Section E instead
- Return arrows from child workflows back to the parent

**Grouping rule — eliminates horizontal sprawl:**
When 3 or more parallel child workflows follow the same pattern (e.g., multiple tool-removal workflows), represent them as ONE box with bullet lines listing the members. Use `&#xa;` for line breaks in the `value=` attribute. Label the arrow `childJob (×N)`. List the external systems those child workflows collectively reach once each, to the right of the group box.

**Layout rules — follow exactly:**
1. Workflow chain runs in a single vertical column on the LEFT (x=40 to x=380)
2. External systems sit in a column on the RIGHT (x=470 to x=680), at the same y-band as the workflow that calls them
3. Workflow → next workflow: vertical arrow going straight down
4. Workflow → external system: horizontal arrow going straight right
5. No diagonal arrows. No long arrows crossing the canvas.
6. Canvas width: ≤ 700px. Canvas height: grow as needed (100px per row).

**Shape guide:**
- Entry points: `style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=12;"` — Size: 180×50
- Workflows (orchestrator, child, grouped): `style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;"` — Size: 280×55 (taller for grouped bullet lists)
- forEach / loop: `style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=12;"` — Size: 280×55
- External systems: `style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3cd;strokeColor=#d0893c;fontStyle=1;fontSize=11;"` — Size: 180×45
- JSON Forms (user input): `style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;"` — Size: 160×60
- All arrows: `style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;"`

**`solution-design.drawio` scaffold** — generic pattern to follow; replace all `{...}` placeholders with real names from the use case:

\`\`\`xml
<mxfile>
  <diagram name="{Use Case Name} - Solution Design">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="700" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Entry points (y=30) — one ellipse per entry point, spaced at x=40, x=240, x=440... -->
        <mxCell id="ep1" value="{Entry Point, e.g. Operator}" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="40" y="30" width="180" height="50" as="geometry"/>
        </mxCell>
        <!-- Repeat for each additional entry point -->

        <!-- Orchestrator workflow (y=130) -->
        <mxCell id="mw" value="{Orchestrator Workflow Name}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="40" y="130" width="280" height="55" as="geometry"/>
        </mxCell>
        <mxCell id="e_ep1_mw" value="{trigger, e.g. launch}" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" source="ep1" target="mw" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Child workflow (y=240) — with external systems to the right -->
        <mxCell id="cw1" value="{Child Workflow Name}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="40" y="240" width="280" height="55" as="geometry"/>
        </mxCell>
        <mxCell id="e_mw_cw1" value="childJob" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" source="mw" target="cw1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <!-- External system at the same y-band, to the right -->
        <mxCell id="ext1" value="{External System Name}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3cd;strokeColor=#d0893c;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="380" y="248" width="180" height="45" as="geometry"/>
        </mxCell>
        <mxCell id="e_cw1_ext1" value="{operation}" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" source="cw1" target="ext1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <!-- Add more external systems at y+55 each for additional systems called by the same workflow -->

        <!-- Grouped child workflows — use when 3+ parallel children follow the same pattern (y=350) -->
        <mxCell id="grp1" value="{Group Label, e.g. Tool Removal Workflows (×N)}&#xa;• {Child Workflow 1}&#xa;• {Child Workflow 2}&#xa;• {Child Workflow 3}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="40" y="350" width="280" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="e_cw1_grp1" value="childJob (×N)" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" source="cw1" target="grp1" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <!-- External systems the group collectively reaches — one box per distinct system, stacked at y=350, y=405, y=460... -->
        <mxCell id="ext2" value="{External System A}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3cd;strokeColor=#d0893c;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="380" y="350" width="180" height="45" as="geometry"/>
        </mxCell>
        <mxCell id="e_grp1_ext2" value="{operation}" style="edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;" edge="1" source="grp1" target="ext2" parent="1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <!-- Continue for each additional external system at y+55 -->

        <!-- Continue adding child workflows/loops below (y += 100+ per row) -->

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
\`\`\`

## E. Workflow Structure

For each workflow, write a subsection using the following structure. Only include a task-type sub-table if that type actually exists in the workflow — suppress empty tables entirely.

### {Workflow Name}

**Description:** {One sentence describing the workflow's role.}

**Adapters and Integrations**

| Name | Operation |
|------|-----------|
| {Adapter instance name} | {Operation(s) called} |

_(Omit this table if the workflow uses no adapters.)_

**Inputs**

| Input | Type | Description |
|-------|------|-------------|
| {varName} | {string/object/array/number/boolean} | {What this input represents} |

**Outputs**

| Output | Type | Description |
|--------|------|-------------|
| {varName} | {string/object/array/number/boolean} | {What this output represents} |

**Child Jobs**

| Workflow Name | Task Summary | Task Description |
|---------------|--------------|-----------------|
| {child workflow name} | {task summary} | {what this task does} |

_(Omit if no child job tasks.)_

**Transformations**

| Transformation Name | Task Summary | Task Description |
|--------------------|--------------|-----------------|
| {transformation name} | {task summary} | {what this task does} |

_(Omit if no transformation tasks.)_

**Template Tasks**

| Template Name | Template Type | Task Summary | Task Description |
|---------------|--------------|--------------|-----------------|
| {template name} | {jinja2/textfsm} | {task summary} | {what this task does} |

_(Omit if no template tasks.)_

**Command Template Tasks**

| Template Name | Task Summary | Task Description |
|---------------|--------------|-----------------|
| {command template name} | {task summary} | {what this task does} |

_(Omit if no command template tasks.)_

**Analytic Template Tasks**

| Template Name | Task Summary | Task Description |
|---------------|--------------|-----------------|
| {analytic template name} | {task summary} | {what this task does} |

_(Omit if no analytic template tasks.)_

**JSON Form Tasks**

| Form Name | Task Summary | Task Description |
|-----------|--------------|-----------------|
| {form name} | {task summary} | {what this task does} |

_(Omit if no JSON form tasks.)_

## F. Command Templates

For each command template referenced in this use case, document its commands and validation rules. Omit this section entirely if no command templates exist.

### {Command Template Name}

| Command | Rules |
|---------|-------|
| `{cli command}` | {Rule: `{pattern}` — Eval: `{contains/regex/etc}`, Flags: `{flags if any}`, Severity: `{error/warn/info}`} |

_(Multiple rules for one command go in the same cell as a list. Multiple commands each get their own row.)_

## H. Known Gaps
Patterns not present that are typically expected:
- No rollback logic observed
- No notifications (email/Teams)
- No audit trail
```

---

## README.md Template

```markdown
# Assets Documentation

> Generated {YYYY-MM-DD} by analyzing {N} workflows, {N} templates,
> {N} transformations, {N} JSON forms, {N} command templates,
> {N} OM automations, {N} golden config assets, and {N} LCM resource models.

## How to Read These Reports

Each use case folder contains two documents:
- **`customer-spec.md`** — Inferred High-Level Design (HLD): business purpose,
  scope, user interaction model, integrations, acceptance criteria
- **`solution-design.md`** — As-Built Low-Level Design (LLD): component inventory,
  workflow hierarchy, adapter mappings, task flows, data model, error handling

## Use Case Index

### Core Network Automation Use Cases

| # | Use Case | Folder | Assets | Description |
|---|----------|--------|--------|-------------|
| 1 | [{Name}]({slug}/) | `{slug}` | ~{N} | {1-line description} |

### Specialized Use Cases

| # | Use Case | Folder | Assets | Description |
|---|----------|--------|--------|-------------|

### Shared Libraries & Infrastructure

| # | Use Case | Folder | Assets | Description |
|---|----------|--------|--------|-------------|

### Reference

| # | Use Case | Folder | Assets | Description |
|---|----------|--------|--------|-------------|
| | [Standalone/Test Workflows]({slug}/) | `{slug}` | ~{N} | {catalog description} |

## Cross-Use-Case Relationships

\`\`\`
{ASCII diagram showing how use cases connect.
OM triggers and LCM entry points at top, core use cases in middle,
shared utilities at bottom.}

                    Operations Manager / LCM Triggers
                              |
                              v
                    {Central Orchestrator Use Case}
                              |
          +--------+--------+---------+--------+
          |        |        |         |        |
      {UC1}    {UC2}    {UC3}     {UC4}    {UC5}
          |        |        |         |        |
          +--------+--------+---------+--------+
                              |
                    Shared Utilities
\`\`\`

## Excluded from Documentation

{List any assets excluded and why.}
```

````

============================================================
FILE: helpers/iag/example-ansible-service.yaml
DIRECTORY: helpers/iag/
FILENAME: example-ansible-service.yaml
============================================================
SHA256: 101a5f6c4cb8bab48086c49841df5285b144e606665bd80a13ddfcb20953668e

````yaml
decorators:
  - name: config-deploy
    schema:
      $id: config-deploy
      $schema: https://json-schema.org/draft/202012/schema
      type: object
      required:
        - target_host
        - config_template
      properties:
        target_host:
          type: string
          description: "Target device hostname or inventory group"
          examples: ["all", "cisco_devices", "router1"]
        config_template:
          type: string
          description: "Config template name to apply"
        dry_run:
          type: boolean
          default: false
          description: "Check mode — report changes without applying"

repositories:
  - name: ansible-playbooks
    url: git@github.com:org/ansible-network.git
    reference: main
    private-key-name: git-ssh-key

services:
  - name: deploy-config
    type: ansible-playbook
    description: Deploy network config using Ansible
    playbooks:
      - deploy.yml
    working-directory: playbooks
    repository: ansible-playbooks
    decorator: config-deploy
    tags:
      - network
      - config
    secrets:
      - name: vault-password
        type: env
        target: ANSIBLE_VAULT_PASSWORD
    runtime:
      inventory:
        - inventory.yaml
      config-file: ansible.cfg
      req-file: requirements.txt              # paramiko for network_cli
      env:
        ANSIBLE_HOST_KEY_CHECKING: "false"
        ANSIBLE_STDOUT_CALLBACK: json

````

============================================================
FILE: helpers/iag/example-multi-service-chain.yaml
DIRECTORY: helpers/iag/
FILENAME: example-multi-service-chain.yaml
============================================================
SHA256: 0db8481080fadae6e709007c91921ed8e8fc8d94f42b9b53382dde00a7ca0f05

````yaml
# Three services from one repo, designed to chain in an Itential workflow:
#   device-info → config-generator → config-validator
#
# Data flow:
#   runService(device-info) → stdout JSON → runService(config-generator) → stdout JSON → runService(config-validator)

decorators:
  - name: device-info-decorator
    schema:
      $id: root
      $schema: https://json-schema.org/draft/2020-12/schema
      type: object
      required:
        - device_ip
        - device_type
      properties:
        device_ip:
          type: string
          description: Target device IP address
        device_type:
          type: string
          description: Device OS type
          enum:
            - ios
            - nxos
            - eos

  - name: config-generator-decorator
    schema:
      $id: root
      $schema: https://json-schema.org/draft/2020-12/schema
      type: object
      required:
        - device_info
        - vlan_id
        - vlan_name
        - interface
      properties:
        device_info:
          type: string
          description: JSON string from device-info service stdout
        vlan_id:
          type: string
          description: VLAN ID to configure
        vlan_name:
          type: string
          description: VLAN name
        interface:
          type: string
          description: Interface name

  - name: config-validator-decorator
    schema:
      $id: root
      $schema: https://json-schema.org/draft/2020-12/schema
      type: object
      required:
        - config_result
      properties:
        config_result:
          type: string
          description: JSON string from config-generator service stdout
        require_description:
          type: string
          default: "true"
          description: Require interface description (true/false)

repositories:
  - name: iag-demo-services
    url: https://github.com/keepithuman/iag-demo-services.git
    reference: main
    description: Three chained services for IAG workflow demo

services:
  - name: device-info
    type: python-script
    description: Gathers device facts (hostname, OS, interfaces, uptime)
    filename: main.py
    working-directory: device-info
    repository: iag-demo-services
    decorator: device-info-decorator

  - name: config-generator
    type: python-script
    description: Generates vendor-specific config from device info and VLAN params
    filename: main.py
    working-directory: config-generator
    repository: iag-demo-services
    decorator: config-generator-decorator

  - name: config-validator
    type: python-script
    description: Validates generated config against best-practice checks
    filename: main.py
    working-directory: config-validator
    repository: iag-demo-services
    decorator: config-validator-decorator

````

============================================================
FILE: helpers/iag/example-opentofu-service.yaml
DIRECTORY: helpers/iag/
FILENAME: example-opentofu-service.yaml
============================================================
SHA256: bfec162ca22dec30771e1dfb47d2bb081dffae72f01db247fe29000cef91bcbf

````yaml
decorators:
  - name: deploy-infrastructure
    schema:
      $id: deploy-infrastructure
      $schema: https://json-schema.org/draft/202012/schema
      type: object
      required:
        - environment
        - region
      properties:
        environment:
          type: string
          description: Target environment
          enum:
            - dev
            - staging
            - production
        region:
          type: string
          description: Cloud region
          examples: ["us-east-1", "us-west-2", "eu-west-1"]
        instance_count:
          type: integer
          default: 1
          description: Number of instances to deploy
          minimum: 1
          maximum: 100

repositories:
  - name: terraform-infra
    url: git@github.com:org/terraform-modules.git
    reference: main
    private-key-name: git-ssh-key

services:
  - name: deploy-infrastructure
    type: opentofu-plan
    description: Deploy cloud infrastructure with OpenTofu
    working-directory: environments/aws
    repository: terraform-infra
    decorator: deploy-infrastructure
    action: apply                          # required: apply, plan, or destroy
    vars: []                               # optional: ["-var flags"] e.g. ["instance_type=t2.micro"]
    var-files: []                          # optional: ["-var-file flags"] e.g. ["prod.tfvars"]
    state-file: null                       # optional: custom state file path
    tags:
      - cloud
      - infrastructure
    secrets:
      - name: aws-access-key
        type: env
        target: TF_VAR_aws_access_key
      - name: aws-secret-key
        type: env
        target: TF_VAR_aws_secret_key

````

============================================================
FILE: helpers/iag/example-python-service.yaml
DIRECTORY: helpers/iag/
FILENAME: example-python-service.yaml
============================================================
SHA256: e44154a5a483ee50484d1717a737d8ec508fc6534eb75f6d6efda79eebf964a4

````yaml
decorators:
  - name: device-info
    schema:
      $id: device-info
      $schema: https://json-schema.org/draft/202012/schema
      type: object
      required:
        - device_ip
      properties:
        device_ip:
          type: string
          description: "Target device IP address"
          examples: ["10.0.0.1", "172.20.100.63"]
        device_type:
          type: string
          description: "Netmiko device type"
          enum:
            - cisco_ios
            - cisco_nxos
            - cisco_xr
          default: "cisco_ios"
        format:
          type: string
          description: "Output format"
          enum: ["json", "table"]
          default: "json"
      additionalProperties: false

repositories:
  - name: my-automation-repo
    url: https://github.com/org/automation-scripts.git
    reference: main

services:
  - name: device-info
    type: python-script
    description: Gathers device facts (hostname, OS, interfaces)
    filename: main.py
    working-directory: device-info
    repository: my-automation-repo
    decorator: device-info
    tags:
      - network
      - discovery
    secrets:
      - name: device-username
        type: env
        target: DEVICE_USERNAME
      - name: device-password
        type: env
        target: DEVICE_PASSWORD
    runtime:
      req-file: requirements.txt
      env:
        NETMIKO_TIMEOUT: "30"

````

============================================================
FILE: helpers/iag/service-file-schema.md
DIRECTORY: helpers/iag/
FILENAME: service-file-schema.md
============================================================
SHA256: 6f883045f0a44e2453c887d323570013a7b37627ec2e61f250441e375b9a8927

````markdown
# IAG Service File Schema Reference

The IAG service file is a YAML document that defines all resources managed by the Automation Gateway. Import with `iagctl db import <file>` and export with `iagctl db export`.

## Root Structure

```yaml
decorators: []          # Input schemas for services
repositories: []        # Git repos holding scripts/playbooks/plans
services: []            # Executable services (python, ansible, opentofu)
registries: []          # Package registries (PyPI, Ansible Galaxy)
secrets: []             # Credentials and keys
users: []               # Gateway user accounts
executable-objects: []  # Custom executable definitions
mcp_servers: []         # MCP server connections
```

---

## Decorators

JSON Schema definitions that validate service inputs and generate API docs.

```yaml
decorators:
  - name: "my-decorator"            # required — unique name
    schema:                          # option 1: inline JSON Schema
      $id: "root"
      $schema: "https://json-schema.org/draft/2020-12/schema"
      type: "object"
      required: ["device_ip"]
      properties:
        device_ip:
          type: "string"
          description: "Target device IP"
        device_type:
          type: "string"
          enum: ["ios", "nxos", "eos"]
    # file: "./path/to/schema.json"  # option 2: external file (instead of inline schema)
    # argument_order: ["device_ip", "device_type"]  # optional: ordered arg list
```

**Rules:** Provide either `schema` (inline) or `file` (path), not both.

---

## Repositories

Git repos containing scripts, playbooks, or plans.

```yaml
repositories:
  - name: "my-repo"                  # required — unique name
    url: "git@github.com:org/repo.git"  # required — git URL (ssh or https)
    reference: "main"                # optional — branch or commit SHA
    description: "My automation repo"  # optional
    tags: ["demo", "network"]        # optional

    # Auth for private repos (choose ONE method):
    # SSH key auth:
    private-key-name: "git-ssh-key"  # name of secret holding SSH private key

    # HTTPS auth:
    # username: "myuser"             # requires password-name
    # password-name: "git-password"  # name of secret holding password
```

**Rules:**
- Use `private-key-name` for SSH URLs (`git@...`)
- Use `username` + `password-name` for HTTPS URLs
- Cannot mix both auth methods

---

## Services

### Python Script

```yaml
services:
  - name: "my-python-service"        # required — unique name
    type: "python-script"            # required
    description: "Does something"    # optional
    repository: "my-repo"            # required — which repo has the code
    working-directory: "scripts/"    # required — path within repo
    filename: "main.py"             # required (unless pyproj-script)
    decorator: "my-decorator"        # optional — input validation schema
    tags: ["network", "automation"]  # optional
    secrets:                         # optional — injected as env vars at runtime
      - name: "api-token"
        type: "env"
        target: "API_TOKEN"          # env var name your script reads
    runtime:                         # optional
      env:                           # extra environment variables
        PYTHONPATH: "/usr/local/lib"
      req-file: "requirements.txt"   # or "pyproject.toml"
      # pyproj-script: "speak"       # alternative to filename (from pyproject.toml)
      # pyproj-optional-deps: ["fancy"]  # optional deps from pyproject.toml
```

**Rules:**
- Exactly one of `filename` OR `runtime.pyproj-script` must be set
- `runtime.req-file` must point to `requirements.txt` or `pyproject.toml`

### Ansible Playbook

```yaml
services:
  - name: "my-ansible-service"
    type: "ansible-playbook"         # required
    description: "Runs a playbook"
    repository: "my-repo"            # required
    working-directory: "ansible/"    # required
    playbooks:                       # required — at least one
      - "site.yml"
      - "deploy.yml"
    decorator: "my-decorator"        # optional
    tags: ["cisco", "network"]
    secrets:
      - name: "vault-key"
        type: "env"
        target: "ANSIBLE_VAULT_PASSWORD"
    runtime:                         # optional — ansible-specific settings
      inventory: ["./inventory.ini"] # inventory file(s)
      extra-vars: ["env=prod"]       # extra variables
      extra-vars-file: ["vars.yml"]  # variable files
      check: false                   # dry-run mode
      diff: false                    # show diffs
      verbose: false                 # verbose output
      verbose-level: 2               # 1-4 (like -v, -vv, -vvv, -vvvv)
      forks: 50                      # parallel processes
      tags: "webservers"             # only run tasks with these tags
      skip-tags: "debug"             # skip tasks with these tags
      limit: ["host1", "host2"]      # limit to these hosts
      config-file: "./ansible.cfg"   # custom ansible config
```

### OpenTofu Plan

```yaml
services:
  - name: "my-tofu-service"
    type: "opentofu-plan"            # required
    description: "Deploys infra"
    repository: "my-repo"            # required
    working-directory: "terraform/"  # required — directory containing .tf files
    decorator: "my-decorator"        # optional
    action: "apply"                  # required — "apply", "plan", or "destroy"
    vars: []                         # optional — passed as -var flags, e.g. ["region=us-east-1"]
    var-files: []                    # optional — passed as -var-file flags, e.g. ["prod.tfvars"]
    state-file: null                 # optional — custom state file path
    tags: ["infrastructure"]
    secrets:
      - name: "aws-key"
        type: "env"
        target: "TF_VAR_aws_access_key"  # OpenTofu reads TF_VAR_* as variables
```

**Rules:**
- `action` is required — must be `apply`, `plan`, or `destroy`
- `vars` and `var-files` are arrays (NOT `plan-vars` / `plan-var-files`)
- Decorator params pass directly as OpenTofu variables
- Backend/provider config lives in `.tf` files, not the service YAML

### Executable (Custom)

```yaml
services:
  - name: "custom-exec"
    type: "executable"               # required
    description: "Runs a shell script"
    repository: "my-repo"            # required
    working-directory: "./"          # required
    filename: "scripts/deploy.sh"    # required
    arg-format: "-{{.Key}}={{.Value}}"  # required — Go template for args
```

**Rules:** `arg-format` must be a valid Go template with `{{.Key}}` and `{{.Value}}`.

---

## Registries

Package registries for Python (PyPI) or Ansible (Galaxy).

```yaml
registries:
  # PyPI registry
  - name: "private-pypi"
    type: "pypi"                     # required: "pypi" or "ansible-galaxy"
    url: "http://private:8080/simple"  # required
    default: false                   # optional — mark as default for this type
    description: "Private PyPI"
    username: "admin"                # auth option 1: username + password
    password-name: "pypi-password"   # name of secret

  # Ansible Galaxy with token
  - name: "private-galaxy"
    type: "ansible-galaxy"
    url: "https://galaxy.example.com"
    token-name: "galaxy-token"       # auth option 2: token
    auth-url: "https://galaxy.example.com/api/v1/auth/"  # galaxy-only
    client-id: "my-client"           # galaxy-only, requires auth-url
    insecure: false                  # skip SSL verification
```

**Rules:**
- Cannot mix `username` with `token-name`
- `auth-url` and `client-id` only valid for `ansible-galaxy` type
- If `auth-url` is provided, `token-name` is required

---

## Secrets

Credentials stored encrypted at rest.

```yaml
secrets:
  - name: "git-ssh-key"             # required — unique name
    value: "-----BEGIN OPENSSH PRIVATE KEY-----\n..."  # required

  - name: "api-token"
    value: "token-abc123"
```

**Note:** Secrets in YAML files contain raw values. For interactive creation (never in shell history), use `iagctl create secret <name> --prompt-value` instead.

---

## Users

Gateway user accounts (server mode only).

```yaml
users:
  - name: "admin"                    # required
    password: "admin-password"       # required
```

---

## Executable Objects

Custom executable definitions that services can reference.

```yaml
executable-objects:
  - name: "python-interpreter"       # required
    exec-command: "/usr/bin/python3"  # required — command to execute
    description: "System Python"     # optional
    tags: ["python"]                 # optional
```

---

## MCP Servers

Model Context Protocol server connections.

```yaml
mcp_servers:
  # Local stdio transport
  - name: "local-mcp"
    transport: "stdio"               # required: "stdio", "sse", or "streamable-http"
    command: "/usr/local/bin/mcp-server"  # required — command (stdio) or URL (sse/http)
    description: "Local MCP server"
    tags: ["local"]
    env:                             # stdio only — environment variables
      PATH: "/usr/local/bin"

  # Remote SSE transport
  - name: "remote-mcp"
    transport: "sse"
    command: "https://mcp.example.com/sse"
    headers:                         # sse/http only — HTTP headers
      Authorization: "Bearer token123"
```

---

## Import/Export Commands

```bash
# Export current state to YAML
iagctl db export <file.yaml>

# Validate a service file (dry run, no changes)
iagctl db import <file.yaml> --validate

# Dry run with checks
iagctl db import <file.yaml> --check

# Import (additive — new resources added, existing skipped)
iagctl db import <file.yaml>

# Import with overwrite (existing resources replaced)
iagctl db import <file.yaml> --force

# Import directly from a Git repo
iagctl db import --repository <git-url> --reference <branch>
```

**Import behavior:**
- **New resources** → added
- **Existing resources (same name)** → skipped (use `--force` to overwrite)
- **Resources not in the YAML** → untouched (never deleted)

````

============================================================
FILE: helpers/operations/add-components-to-project.json
DIRECTORY: helpers/operations/
FILENAME: add-components-to-project.json
============================================================
SHA256: 3c7cb7446e585cdde36be568bb66cce0d0727da51d408139cb9df289323b38f8

````json
{
  "components": [
    {
      "type": "workflow",
      "reference": "REPLACE_WORKFLOW_UUID",
      "folder": "/"
    },
    {
      "type": "template",
      "reference": "REPLACE_TEMPLATE_ID",
      "folder": "/"
    },
    {
      "type": "transformation",
      "reference": "REPLACE_TRANSFORMATION_ID",
      "folder": "/"
    },
    {
      "type": "jsonForm",
      "reference": "REPLACE_FORM_ID",
      "folder": "/"
    },
    {
      "type": "mopCommandTemplate",
      "reference": "@REPLACE_PROJECT_ID: REPLACE_TEMPLATE_NAME",
      "folder": "/"
    },
    {
      "type": "mopAnalyticTemplate",
      "reference": "@REPLACE_PROJECT_ID: REPLACE_ANALYTIC_TEMPLATE_NAME",
      "folder": "/"
    }
  ],
  "mode": "copy"
}

````

============================================================
FILE: helpers/operations/add-devices-to-node.json
DIRECTORY: helpers/operations/
FILENAME: add-devices-to-node.json
============================================================
SHA256: bd23188b4dbeb9d166064f4341d37ac32a03ea8a3db76bbe6fe24e7797b28b65

````json
{
  "devices": ["REPLACE_DEVICE_NAME_1", "REPLACE_DEVICE_NAME_2"]
}

````

============================================================
FILE: helpers/operations/run-compliance-plan.json
DIRECTORY: helpers/operations/
FILENAME: run-compliance-plan.json
============================================================
SHA256: 86b7160c8f23334fcbbe068c674eaa7fb55f201a027a0c1b9f6390717e158f6a

````json
{
  "planId": "REPLACE_PLAN_ID",
  "options": {}
}

````

============================================================
FILE: helpers/operations/run-compliance.json
DIRECTORY: helpers/operations/
FILENAME: run-compliance.json
============================================================
SHA256: cb77054838de6ca4615dc0c931ec563c26edd3c3ca2a577e54cf97904e2a275d

````json
{
  "options": {
    "treeId": "REPLACE_TREE_ID",
    "version": "initial",
    "nodePath": "base",
    "devices": []
  }
}

````

============================================================
FILE: helpers/update/update-command-template.json
DIRECTORY: helpers/update/
FILENAME: update-command-template.json
============================================================
SHA256: 8505666d1f13d637b149b91e2fc24c7e722f5ec3a6c3e65eedd250723ed3f6ad

````json
{
  "mop": {
    "name": "REPLACE_TEMPLATE_NAME",
    "description": "REPLACE_DESCRIPTION",
    "os": "",
    "passRule": true,
    "tags": [],
    "commands": [
      {
        "command": "REPLACE_COMMAND",
        "passRule": true,
        "rules": [
          {
            "rule": "REPLACE_RULE",
            "eval": "contains",
            "severity": "error",
            "evaluation": "pass"
          }
        ]
      }
    ]
  }
}

````

============================================================
FILE: helpers/update/update-json-form.json
DIRECTORY: helpers/update/
FILENAME: update-json-form.json
============================================================
SHA256: 0185b8516f52ec225bf0bcd49e5377d3a14f73a20d1a8e0958a8419dea8be99c

````json
{
  "_comment": "Full replacement — GET the form first, copy its created/createdBy/lastUpdated/lastUpdatedBy into options, modify fields, then PUT back. PUT /json-forms/forms/{formId}. Body MUST be wrapped in 'options' key. schema.title must match name.",
  "options": {
    "name": "REPLACE_FORM_NAME",
    "description": "REPLACE_DESCRIPTION",
    "created": "REPLACE_CREATED_TIMESTAMP",
    "createdBy": "REPLACE_CREATED_BY",
    "lastUpdated": "REPLACE_LAST_UPDATED_TIMESTAMP",
    "lastUpdatedBy": "REPLACE_LAST_UPDATED_BY",
    "schema": {
      "type": "object",
      "title": "REPLACE_FORM_NAME",
      "properties": {},
      "required": []
    },
    "uiSchema": {},
    "struct": {
      "type": "array",
      "items": []
    },
    "bindingSchema": {
      "properties": {}
    },
    "validationSchema": {
      "properties": {}
    },
    "tags": [],
    "version": "2020.1"
  }
}

````

============================================================
FILE: helpers/update/update-node-config.json
DIRECTORY: helpers/update/
FILENAME: update-node-config.json
============================================================
SHA256: c25a883ad7ae307eb6ff51a50479f21c2968987d512e10b730cac744d1cf18f1

````json
{
  "treeId": "",
  "treeVersion": "initial",
  "nodePath": "base",
  "data": {
    "template": "service password-encryption\naaa new-model\n<e/>ntp server {{ ntp_server }}\n<i/>version {/ {{ version_regex }} /}\n{i/}hostname {/\\S+/}\n{d/}service internal\n{d/}<e/>ip domain-lookup\nip access-list extended ACL-VLAN100-IN\n 10 permit tcp 10.100.1.0 0.0.0.255 any eq www\n {/ {{ acl_line_regex }} /} permit tcp 10.100.1.0 0.0.0.255 any eq 443\n 30 deny ip any any log\n{% for intf in interfaces %}\n{i/}interface {{ intf['name'] }}\n  {i/}description {{ intf['description'] }}\n  {i/}no shutdown\n{% endfor %}",
    "variables": {
      "ntp_server": "ntp1.east.itential.com",
      "version_regex": "\\d+\\.\\d+",
      "acl_line_regex": "^(10000|[1-9][0-9]{0,3})",
      "interfaces": [
        { "name": "Loopback10", "description": "Management" }
      ]
    }
  },
  "updateVariables": true
}

````

============================================================
FILE: helpers/update/update-project-members.json
DIRECTORY: helpers/update/
FILENAME: update-project-members.json
============================================================
SHA256: c76bfbb520abc1d84cae26c71ed75da3f12ebcc78d03905ea79ee23ab11b6631

````json
{
  "members": [
    {
      "type": "account",
      "role": "owner",
      "reference": "REPLACE_OWNER_ACCOUNT_ID"
    },
    {
      "type": "account",
      "role": "editor",
      "reference": "REPLACE_USER_ACCOUNT_ID"
    },
    {
      "type": "group",
      "role": "editor",
      "reference": "REPLACE_GROUP_ID"
    }
  ]
}

````

============================================================
FILE: helpers/use-case-memory.md
DIRECTORY: helpers/
FILENAME: use-case-memory.md
============================================================
SHA256: 14ee19f60cf439ec738779c1f30625ef0aabd750c9d053d06ea68276c55136c9

````markdown
# Use-Case Memory: {USE_CASE_NAME}

> One sentence: what problem this solves and for whom.

**Stage:** `requirements | feasibility | design | build | test | as-built | delivered`
**Status:** `active | on-hold`
**Last updated:** YYYY-MM-DD
**Platform:** https://...

> **Resuming this use-case?** `Stage` tells you where to pick up — but verify it against what files actually exist before trusting it (a stale field is worse than no field). See AGENTS.md's "Resuming a Use-Case" table for the file-presence check per stage.

---

## Platform References

Things that take time to look up — record them once, reuse forever.

| What | Value |
|------|-------|
| Platform URL | |
| Project name | |
| Project ID (`_id`) | |
| Auth method | oauth / basic |
| Adapter instance(s) | e.g. `servicenow-prod`, `netbox-1` |
| Adapter app type(s) | e.g. `Servicenow`, `NetBox` (from apps.json — not the instance name) |
| Group given access | e.g. `Solutions Engineering` (`_id=...`) |
| Key transformation IDs | e.g. `Parse Number: 5f232737ebaff79cdeb87351` |
| Key workflow UUIDs | e.g. `ISP - Create: 60e62f32-...` |

---

## What Was Built

| Asset | Type | ID / Name | Status |
|-------|------|-----------|--------|
| | workflow | | done |
| | workflow | | done |
| | template | | done |
| | json-form | | done |
| | transformation | | done |
| | ops-manager automation | | done |

---

## Architecture Decisions

The non-obvious choices made during design or build — and **why**. Skip anything derivable from the code.

- **Why X instead of Y:** ...
- **Why split into N workflows:** ...
- **Why adapter X for this task:** ...
- **Constraint that shaped the design:** ...

---

## Gotchas Hit

Things that caused unexpected failures or required workarounds. Future iterations skip re-discovering these.

- **Issue:** ...  
  **Root cause:** ...  
  **Fix:** ...

---

## Test Log

| Date | What was tested | Result | Notes |
|------|----------------|--------|-------|
| | | pass / fail / partial | |

---

## Open Items

- [ ] ...
- [ ] ...

---

## Spec Deviations

Anything delivered differently from the original `customer-spec.md` and why.

| Spec said | What was built | Reason |
|-----------|---------------|--------|
| | | |

````

============================================================
FILE: scripts/platform_pull.py
DIRECTORY: scripts/
FILENAME: platform_pull.py
============================================================
SHA256: 36bcebc03cc4efb1dcbd72670acbedac416fafbed5b7d866baff1047979a77b2

````python
#!/usr/bin/env python3
"""
Pull platform-wide data into platform/ directory.
Run once per platform instance. Use --refresh to re-pull.

Usage:
    python scripts/platform_pull.py <platform-url> <client-id> <client-secret>
    python scripts/platform_pull.py --refresh <platform-url> <client-id> <client-secret>
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


PLATFORM_DIR = Path(__file__).parent.parent / "platform"
PULLED_AT_FILE = PLATFORM_DIR / ".pulled-at"


def fetch(url, token, filename):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    print(f"  ✓ {filename}")
    return filename, data


def authenticate(base, client_id, client_secret):
    print(f"Authenticating to {base}...")
    data = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode()
    req = urllib.request.Request(
        f"{base}/oauth/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req) as resp:
        token = json.loads(resp.read()).get("access_token", "")
    if not token:
        print("ERROR: Authentication failed — no access_token in response", file=sys.stderr)
        sys.exit(1)
    print("Authenticated.")
    return token


def generate_environment_summary(d: Path):
    tasks = json.loads((d / "tasks.json").read_text())
    apps_raw = json.loads((d / "apps.json").read_text())
    adapters_raw = json.loads((d / "adapters.json").read_text())
    applications_raw = json.loads((d / "applications.json").read_text())

    apps = apps_raw if isinstance(apps_raw, list) else apps_raw.get("results", [])
    adapters = adapters_raw if isinstance(adapters_raw, list) else adapters_raw.get("results", [])
    applications = applications_raw if isinstance(applications_raw, list) else applications_raw.get("results", [])

    task_locations = Counter(t.get("location", "") for t in tasks)
    task_apps = Counter(t.get("app", "") for t in tasks)

    lines = [
        "# Environment Overview\n",
        f"**Total tasks in palette:** {len(tasks)}",
        f"  - Application tasks: {task_locations.get('Application', 0)}",
        f"  - Adapter tasks: {task_locations.get('Adapter', 0)}",
        f"  - Broker tasks: {task_locations.get('Broker', 0)}\n",
        "## Applications\n",
        "| Application | State | Description | Task Count |",
        "|-------------|-------|-------------|------------|",
    ]
    for a in sorted(applications, key=lambda x: x.get("id", "")):
        name = a.get("id", "")
        desc = (a.get("description", "") or "")[:60]
        lines.append(f"| {name} | {a.get('state', '')} | {desc} | {task_apps.get(name, 0)} |")

    lines += [
        "",
        "## Adapters\n",
        "| Instance Name | Adapter Type | Package | State | Task Count |",
        "|---------------|-------------|---------|-------|------------|",
    ]
    for a in sorted(adapters, key=lambda x: x.get("id", "")):
        name = a.get("id", "")
        pkg = a.get("package_id", "")
        adapter_type = pkg.split("adapter-")[-1] if "adapter-" in pkg else pkg.split("/")[-1]
        lines.append(f"| {name} | {adapter_type} | {pkg} | {a.get('state', '')} | {task_apps.get(name, 0)} |")

    lines += [
        "",
        "## Top Task Sources\n",
        "| Source | Location | Task Count |",
        "|--------|----------|------------|",
    ]
    for app, cnt in task_apps.most_common(20):
        loc = next((t.get("location", "") for t in tasks if t.get("app") == app), "")
        lines.append(f"| {app} | {loc} | {cnt} |")

    (d / "environment.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Pull platform-wide data into platform/")
    parser.add_argument("--refresh", action="store_true", help="Re-pull even if data already exists")
    parser.add_argument("platform_url", help="Platform base URL")
    parser.add_argument("client_id", help="OAuth client ID")
    parser.add_argument("client_secret", help="OAuth client secret")
    args = parser.parse_args()

    base = args.platform_url.rstrip("/")

    # Skip if already pulled
    if PULLED_AT_FILE.exists() and not args.refresh:
        print(f"Platform data already pulled: {PULLED_AT_FILE.read_text().strip()}")
        print("Use --refresh to re-pull.")
        return

    PLATFORM_DIR.mkdir(exist_ok=True)

    token = authenticate(base, args.client_id, args.client_secret)

    encoded_base = urllib.parse.quote(base, safe="")

    files = {
        "openapi.json": f"{base}/help/openapi?url={encoded_base}",
        "tasks.json": f"{base}/workflow_builder/tasks/list",
        "apps.json": f"{base}/automation-studio/apps/list",
        "adapters.json": f"{base}/health/adapters",
        "applications.json": f"{base}/health/applications",
    }

    print(f"Pulling {len(files)} files in parallel...")
    with ThreadPoolExecutor(max_workers=len(files)) as executor:
        futures = {executor.submit(fetch, url, token, filename): filename for filename, url in files.items()}
        for future in as_completed(futures):
            filename, data = future.result()
            (PLATFORM_DIR / filename).write_bytes(data)

    print("  Generating environment.md...")
    generate_environment_summary(PLATFORM_DIR)

    pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    PULLED_AT_FILE.write_text(f"{pulled_at}  {base}\n")

    task_count = len(json.loads((PLATFORM_DIR / "tasks.json").read_text()))
    apps_raw = json.loads((PLATFORM_DIR / "apps.json").read_text())
    app_count = len(apps_raw) if isinstance(apps_raw, list) else len(apps_raw.get("results", []))

    print(f"\n=== Platform data pulled at {pulled_at} ===")
    print(f"  {PLATFORM_DIR}/")
    print(f"    openapi.json      — full API reference ({base})")
    print(f"    tasks.json        — {task_count} tasks")
    print(f"    apps.json         — {app_count} apps/adapters")
    print(f"    adapters.json     — adapter instance details")
    print(f"    applications.json — application details")
    print(f"    environment.md    — summary with task counts")


if __name__ == "__main__":
    main()

````

============================================================
FILE: scripts/use_case_init.py
DIRECTORY: scripts/
FILENAME: use_case_init.py
============================================================
SHA256: 94bfa0efde8a751a7dd07680e2bb8ec62fc948fd3cc3596eefd640d5a2466435

````python
#!/usr/bin/env python3
"""
Initialize a use-case directory under use-cases/<name>/.
Requires platform data — run scripts/platform_pull.py first.

Usage:
    python scripts/use_case_init.py <use-case-name> <platform-url> <client-id> <client-secret>
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path


SCRIPTS_DIR = Path(__file__).parent
PLATFORM_DIR = SCRIPTS_DIR.parent / "platform"
USE_CASES_DIR = SCRIPTS_DIR.parent / "use-cases"
PULLED_AT_FILE = PLATFORM_DIR / ".pulled-at"


def get_token(platform_url, client_id, client_secret):
    data = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode()
    req = urllib.request.Request(
        f"{platform_url}/oauth/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req) as resp:
        token = json.loads(resp.read()).get("access_token", "")
    if not token:
        print("ERROR: Authentication failed — no access_token in response", file=sys.stderr)
        sys.exit(1)
    return token


def main():
    parser = argparse.ArgumentParser(description="Initialize a use-case directory")
    parser.add_argument("use_case", help="Use-case name (becomes the directory name)")
    parser.add_argument("platform_url", help="Platform base URL")
    parser.add_argument("client_id", help="OAuth client ID")
    parser.add_argument("client_secret", help="OAuth client secret")
    args = parser.parse_args()

    base = args.platform_url.rstrip("/")
    use_case_dir = USE_CASES_DIR / args.use_case

    # Require platform data
    if not PULLED_AT_FILE.exists():
        print("ERROR: Platform data not found.", file=sys.stderr)
        print("       Run first: python scripts/platform_pull.py <platform-url> <client-id> <client-secret>", file=sys.stderr)
        sys.exit(1)

    print(f"Platform data: {PULLED_AT_FILE.read_text().strip()}")

    # Skip if already initialized
    if use_case_dir.exists():
        print(f"Use-case '{args.use_case}' already exists at {use_case_dir} — skipping.")
        return

    use_case_dir.mkdir(parents=True)

    # Write .env
    env_content = "\n".join([
        f"PLATFORM_URL={base}",
        f"CLIENT_ID={args.client_id}",
        f"CLIENT_SECRET={args.client_secret}",
        "AUTH_METHOD=oauth",
        "",
    ])
    (use_case_dir / ".env").write_text(env_content)

    # Get initial token and write .auth.json
    print(f"Authenticating to {base}...")
    token = get_token(base, args.client_id, args.client_secret)
    (use_case_dir / ".auth.json").write_text(json.dumps({"token": token}, indent=2) + "\n")
    print("Authenticated.")

    # Create empty task schema cache
    (use_case_dir / "task-schemas.json").write_text("[]\n")

    print(f"\n=== Use-case initialized: {args.use_case} ===")
    print(f"  {use_case_dir}/")
    print(f"    .env              — credentials (gitignored)")
    print(f"    .auth.json        — bearer token (gitignored, auto-refreshed)")
    print(f"    task-schemas.json — task schema cache (populated on demand)")
    print(f"\nPlatform data (shared): {PLATFORM_DIR}/")
    print(f"  openapi.json, tasks.json, apps.json, adapters.json, environment.md")


if __name__ == "__main__":
    main()

````

============================================================
FILE: spec-files/demo/device-health-agent.md
DIRECTORY: spec-files/demo/
FILENAME: device-health-agent.md
============================================================
SHA256: 2c434698dff07052facfafb80fc89df48f54b4c94d54f3377620753f2df883b8

````markdown
# Device Health Troubleshooting Agent — Spec

## Overview

A FlowAgent that autonomously troubleshoots device system and environmental health across multiple network OS vendors. The agent identifies the device OS first, then executes the appropriate CLI commands to assess CPU, memory, and disk/storage health. No workflows — all tool calls are native adapter/app calls.

---

## Agent Details

- **Name:** `device-health-agent`
- **Provider:** `<llm-provider-id>`
- **Description:** Multi-vendor device health troubleshooting agent. Identifies device OS, runs targeted diagnostic commands (CPU, memory, disk), and emails a health report.

---

## Tools (3 total)

| # | Tool Identifier | Type | Purpose |
|---|-----------------|------|---------|
| 1 | `ConfigurationManager//getDevice` | App | Look up device record and OS/type from Itential device broker |
| 2 | `GatewayManager//sendCommand` | App | Execute CLI commands against a device via IAG5 |
| 3 | `email//mailWithOptions` | Adapter | Email health report to ops team |

> **Note:** `GatewayManager//sendCommand` accepts a `commands` array — all diagnostic commands for a device are sent in a **single call**. Max 4 commands per call.

---

## Execution Flow

### Step 1: Get Device Info
- Call `ConfigurationManager//getDevice` with `name` from context.
- Extract the OS/device type from the response.
- If the device is not found, stop and email a not-found report.

### Step 2: Execute Diagnostic Commands (single call, max 4 commands)
- Based on OS from Step 1, select the appropriate command set (see table below).
- Call `GatewayManager//sendCommand` ONCE with all commands as an array.
- Use `clusterId: "<iag-cluster-id>"` and `inventory` targeting the device node.

### Step 3: Analyze and Report
- Summarize findings: CPU utilization, memory usage/free, disk/storage status.
- Flag anything concerning: CPU > 80%, memory < 10% free, disk > 85% used.
- Send email report via `email//mailWithOptions`.

---

## Command Reference by OS

### Cisco IOS / IOS-XE
| # | Command | Purpose |
|---|---------|---------|
| 1 | `show version` | OS version, uptime, platform |
| 2 | `show processes cpu sorted` | CPU utilization per process |
| 3 | `show memory statistics` | Memory pool usage (free/used) |
| 4 | `show platform resources` | Platform CPU, memory, disk summary |

### Cisco NX-OS
| # | Command | Purpose |
|---|---------|---------|
| 1 | `show version` | OS version, uptime |
| 2 | `show processes cpu sort` | CPU utilization |
| 3 | `show system resources` | CPU, memory summary |
| 4 | `show system internal flash` | Flash/disk usage |

### Juniper JunOS
| # | Command | Purpose |
|---|---------|---------|
| 1 | `show version` | OS version, uptime |
| 2 | `show chassis routing-engine` | RE CPU, memory, uptime |
| 3 | `show system processes extensive \| match memory` | Process memory details |
| 4 | `show system storage` | Filesystem disk usage |

### Arista EOS
| # | Command | Purpose |
|---|---------|---------|
| 1 | `show version` | OS version, uptime, model |
| 2 | `show processes top once` | CPU and memory per process |
| 3 | `show version \| grep Memory` | Total/free memory |
| 4 | `show system environment temperature` | Environmental temperature |

### Nokia SR OS
| # | Command | Purpose |
|---|---------|---------|
| 1 | `show system information` | Version, uptime, platform |
| 2 | `show system cpu` | CPU utilization |
| 3 | `show system memory-pools` | Memory pool usage |
| 4 | `show system disk-usage` | Disk filesystem usage |

---

## Decorator Schemas

### 1. device-health-get-device
Tool: `ConfigurationManager//getDevice`

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The exact device name as registered in Itential Configuration Manager. e.g. IOS-CAT8KV-1"
    }
  },
  "required": ["name"]
}
```

### 2. device-health-send-command
Tool: `GatewayManager//sendCommand`

```json
{
  "type": "object",
  "properties": {
    "clusterId": {
      "type": "string",
      "description": "The IAG5 cluster ID to route commands through. Always use '<iag-cluster-id>' for this environment.",
      "examples": ["<iag-cluster-id>"]
    },
    "commands": {
      "type": "array",
      "description": "Array of CLI command strings to execute on the target device. Send all diagnostic commands in one call — max 4 commands.",
      "items": {
        "type": "string",
        "examples": ["show version", "show processes cpu sorted", "show memory statistics", "show platform resources"]
      }
    },
    "inventory": {
      "type": "array",
      "description": "Target device(s) to run commands against. Each entry specifies an inventory name and the node names within it.",
      "items": {
        "type": "object",
        "properties": {
          "inventory": {
            "type": "string",
            "description": "The IAG5 inventory name containing the target device."
          },
          "nodeNames": {
            "type": "array",
            "description": "List of device node names within the inventory to target.",
            "items": { "type": "string" }
          }
        },
        "required": ["inventory"]
      }
    }
  },
  "required": ["clusterId", "commands"]
}
```

### 3. device-health-email
Tool: `email//mailWithOptions`

```json
{
  "type": "object",
  "properties": {
    "from": {
      "type": "string",
      "description": "Sender email address",
      "examples": ["<noreply@example.com>"]
    },
    "to": {
      "type": "array",
      "items": { "type": "string" }
    },
    "subject": {
      "type": "string",
      "description": "e.g. Device Health Report - IOS-CAT8KV-1 - 2026-04-08"
    },
    "body": {
      "type": "string",
      "description": "Body of email. Supports plain text or full inline-styled HTML (e.g. <html><body style=\"font-family: Arial;\">...</body></html>)"
    },
    "displayName": {
      "type": "string",
      "description": "e.g. Itential Platform"
    },
    "cc": { "type": "array", "items": { "type": "string" } },
    "bcc": { "type": "array", "items": { "type": "string" } },
    "attachments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "content": { "type": "string" }
        }
      }
    }
  },
  "required": ["from", "to", "subject", "body", "displayName", "cc", "bcc", "attachments"]
}
```

---

## System Prompt (Draft)

```
You are a Network Device Health Specialist responsible for diagnosing system and environmental issues on multi-vendor network devices.

## Your Role
Given a device name, you identify its OS, run the appropriate diagnostic CLI commands in a single batch, analyze the output, and email a health report. You are concise, methodical, and never send more than 4 commands per device.

## Tools Available
1. **ConfigurationManager//getDevice** — Look up a device record in Itential. Returns OS type, device type, and connection details. Input: `name` (exact device name string).
2. **GatewayManager//sendCommand** — Execute CLI commands on a network device via IAG5. Send ALL diagnostic commands in a SINGLE call using the `commands` array. Required inputs: `clusterId` (always "<iag-cluster-id>"), `commands` (array of strings), `inventory` (array targeting the device).
3. **email//mailWithOptions** — Send the health report email. Use `body` field for content (plain text or HTML). Required fields: from, to, subject, body, displayName, cc, bcc, attachments.

## Execution Flow

**Step 1: Identify the Device OS**
- Call `ConfigurationManager//getDevice` with `name` set to the device name from context.
- Extract the OS/device type from the response (look for fields like `os`, `os_type`, `device_type`, or `type`).
- If the device is not found, skip Step 2 and send an email noting the device was not found.

**Step 2: Run Diagnostic Commands (single sendCommand call)**
- Select the command set for the OS identified in Step 1.
- Call `GatewayManager//sendCommand` ONCE with:
  - `clusterId`: "<iag-cluster-id>"
  - `commands`: array of up to 4 commands from the list below
  - `inventory`: target the device using the inventory and node name from context

IOS / IOS-XE commands:
  ["show version", "show processes cpu sorted", "show memory statistics", "show platform resources"]

NX-OS commands:
  ["show version", "show processes cpu sort", "show system resources", "show system internal flash"]

JunOS commands:
  ["show version", "show chassis routing-engine", "show system processes extensive | match memory", "show system storage"]

Arista EOS commands:
  ["show version", "show processes top once", "show version | grep Memory", "show system environment temperature"]

Nokia SR OS commands:
  ["show system information", "show system cpu", "show system memory-pools", "show system disk-usage"]

Do NOT call sendCommand more than once per device.

**Step 3: Send Email Report**
- Always send an email using `email//mailWithOptions` after collecting results.
- From: <noreply@example.com>
- DisplayName: Itential Platform
- To: recipient from context (or <recipient@example.com> if not specified)
- Subject: "Device Health Report - [device name] - [date]"
- Body: HTML report including:
  - Device name, OS, and version
  - CPU utilization summary with status (OK / WARNING if >80%)
  - Memory summary with free/used and status (OK / WARNING if <10% free)
  - Disk/storage summary with status (OK / WARNING if >85% used)
  - Environmental alerts if any
  - Overall health verdict: HEALTHY / DEGRADED / CRITICAL

## Safety Rules
- Call `GatewayManager//sendCommand` exactly ONCE per device with all commands batched.
- If the command call fails (device unreachable, auth error), note the failure in the report.
- Always send the email even if commands fail — include partial results.
- If the OS is unrecognized, send only ["show version"] and note the OS is unsupported.
```

---

## User Prompt (Default Objective)

```
Perform a full system health check on the device provided in context. Identify its OS, run the appropriate diagnostic commands, and email the health report.
```

---

## Environment Constants (Confirmed from Platform)

| Field | Value |
|-------|-------|
| `clusterId` | `<iag-cluster-id>` |
| Inventory name | `<inventory-name>` |
| Available nodes | `<node-name-1>`, `<node-name-2>` |

## Open Questions

- `ConfigurationManager//getDevice` response — exact field name for OS type needs runtime confirmation (`os`, `os_type`, `device_type`). Update system prompt after first test run.
- `GatewayManager//sendCommand` `inventory` field — the IAG5-internal inventory name must match what is configured in your IAG5 environment. Confirm at build time.

````

============================================================
FILE: spec-files/demo/linux-diagnostics-agent.md
DIRECTORY: spec-files/demo/
FILENAME: linux-diagnostics-agent.md
============================================================
SHA256: 2123ba71c9c83ff017437a3f370ab7cb4ef0537b0c04758b4af4a9d048a9d9fb

````markdown
# Linux Diagnostics Agent — FlowAI Agent Spec

**Version:** 1.0  
**Date:** 2026-04-10  
**Status:** Ready for builder  
**Platform:** <iag-cluster-id> / Itential FlowAI

---

## 1. Overview

| Field | Value |
|---|---|
| Agent name | `Linux Diagnostics` |
| Description | Runs on-demand comprehensive health diagnostics across Linux inventory hosts, produces a structured per-host report, and delivers an HTML summary email to the ops team |
| LLM Provider | `<llm-provider-id>` |
| Model | `claude-sonnet-4-5-20250929` (or latest Claude Sonnet available) |
| Temperature | `0.3` |
| Entry point | System prompt + default user prompt (see Section 5) |

---

## 2. Tools

The agent requires exactly **three** tools.

| # | Tool Identifier | Type | Purpose |
|---|-----------------|------|---------|
| 1 | `<iag-cluster-id>//linux-diagnostics` | IAG service (Ansible) | Run comprehensive diagnostics playbook against target hosts; returns structured JSON per host |
| 2 | `<iag-cluster-id>//send-email` | IAG service (Python) | Send the HTML diagnostic report via Outlook365 SMTP |
| 3 | `WorkFlowEngine//restCall` | Workflow adapter | Post a brief plain-text summary notification to Slack |

### Tool 1: `linux-diagnostics` (NEW — must be built)

This is a new IAG5 Ansible service that does not yet exist. It must be created alongside this agent. See Section 7 for the full build spec.

**Input schema:**
```
target_hosts  string  required  Ansible inventory host pattern (default: "all")
                                Examples: "all", "linux-host-1", "linux-host-2"
```

**Expected output (set_stats):**
```json
{
  "diagnostics_results": [
    {
      "hostname": "linux-host-1",
      "ip_address": "192.0.2.10",
      "timestamp": "2026-04-10T14:00:00Z",
      "overall_status": "WARNING",
      "disk": { ... },
      "memory": { ... },
      "cpu": { ... },
      "uptime": { ... },
      "services": { ... },
      "network": { ... },
      "inodes": { ... },
      "failed_units": [ ... ],
      "oom_events": [ ... ],
      "zombie_processes": 0
    }
  ],
  "summary": {
    "total_hosts": 4,
    "ok_count": 2,
    "warning_count": 1,
    "critical_count": 1,
    "unreachable_count": 0
  }
}
```

### Tool 2: `send-email` (EXISTING)

Already deployed on `<iag-cluster-id>`. Sends HTML email via Outlook365 SMTP.

**Input schema (from existing decorator):**
```
to            string  required  Recipient email address
subject       string  required  Email subject line
body          string  required  HTML body content
display_name  string  optional  Sender display name (default: "IAG5 Automation")
```

### Tool 3: `WorkFlowEngine//restCall` with `slackPostMarkdownMessage` decorator (EXISTING)

Posts a brief Slack notification after the email is sent. Use the `slackPostMarkdownMessage` decorator already configured on the platform.

**Decorator:** `slackPostMarkdownMessage`

**Input schema:**
```
message  string  required  Markdown-formatted Slack message body
```

**Message format:**
```
*Linux Diagnostics — {date}*
Hosts: {total} | ✅ OK: {ok} | ⚠️ Warning: {warning} | 🔴 Critical: {critical}
Report sent to {recipient_email}
```

Use the overall status to set the leading emoji on the first line: ✅ if all OK, ⚠️ if any WARNING, 🔴 if any CRITICAL.

---

## 3. Input Parameters

The agent accepts one context variable set at invocation time:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `target_hosts` | string | `"all"` | Ansible inventory host pattern. Accepts any pattern valid for the inventory: `"all"`, a single hostname (`"linux-host-1"`), or a comma-separated list (`"linux-host-2,linux-host-3"`) |

The ops team should be a hardcoded recipient in the system prompt (`<ops-team@example.com>`). If a different recipient is needed, it can be overridden in the user prompt at runtime.

---

## 4. Inventory Reference

The `linux-diagnostics` service reuses the existing inventory at:
```
ansible/linux_patch_check/inventory.yaml
```

**Hosts:**

| Hostname | IP | User | Notes |
|---|---|---|---|
| `linux-host-1` | 192.0.2.10 | ec2-user | Amazon Linux / RHEL-family |
| `linux-host-2` | 192.0.2.20 | ubuntu | Debian-family, runs MySQL |
| `linux-host-3` | 192.0.2.30 | ec2-user | Amazon Linux, runs Kafka |
| `linux-host-4` | 192.0.2.40 | ec2-user | Amazon Linux, runs Zabbix |

SSH access: all hosts use the `<SSH-SECRET-NAME>` secret, injected as env var and written to a temp file via `tasks/prepare_ssh.yml` (existing shared task).

---

## 5. Agent Configuration

### 5.1 System Prompt

```
You are a Linux Infrastructure Diagnostics Specialist. Your job is to run
comprehensive health checks across the Linux server inventory and deliver
a clear, actionable report to the operations team.

## Your Tools
1. <iag-cluster-id>//linux-diagnostics — Runs a full diagnostics
   playbook across target Linux hosts. Returns structured JSON with disk,
   memory, CPU, uptime, service status, network, inode usage, failed systemd
   units, OOM events, and zombie process counts per host.
   Input: target_hosts (string, e.g. "all" or "linux-host-1").

2. <iag-cluster-id>//send-email — Sends an HTML email via Outlook365.
   Inputs: to (recipient address), subject (string), body (HTML string),
   display_name (optional sender label).

## Execution Flow — Complete Every Step Without Pausing

### Step 1: Run Diagnostics
Call linux-diagnostics with the target_hosts value provided in context
(default: "all"). Wait for the full response before proceeding.

### Step 2: Parse and Classify Results
For each host in diagnostics_results, classify overall status:
  - OK       — No thresholds breached, no anomalies
  - WARNING  — At least one soft threshold breached (see thresholds below)
  - CRITICAL — At least one hard threshold breached, host unreachable, or
               any OOM event in the last 24 hours

### Status Thresholds

DISK (per mount):
  WARNING  > 80% used
  CRITICAL > 90% used

MEMORY (RAM):
  WARNING  < 256 MB free
  CRITICAL < 64 MB free

SWAP:
  WARNING  > 50% used
  CRITICAL > 90% used

CPU Load Average (1m, relative to CPU count):
  WARNING  load/cores > 2.0
  CRITICAL load/cores > 5.0

INODES (per mount):
  WARNING  > 80% used
  CRITICAL > 90% used

SERVICES:
  WARNING  if any expected service is inactive (not running)
  CRITICAL if sshd is not running

FAILED SYSTEMD UNITS:
  WARNING  if 1 or more units in failed state

OOM EVENTS (last 24h):
  CRITICAL if any OOM kill detected

ZOMBIE PROCESSES:
  WARNING  if zombie count > 0

### Step 3: Build HTML Report
Construct the full HTML report using the template in Section 6 of the spec.
The report must include:
  - Executive summary banner (color-coded by worst overall status)
  - Per-host cards with all metric sections
  - Timestamp and inventory scope

### Step 4: Send Email
Call send-email with:
  to: "<ops-team@example.com>"
  subject: "Linux Diagnostics Report — [OVERALL_STATUS] — [timestamp]"
  body: <the full HTML report from Step 3>
  display_name: "Linux Diagnostics Agent"

### Step 5: Send Slack Notification
Call WorkFlowEngine//restCall with the slackPostMarkdownMessage decorator.
Build a brief plain-text Slack message using the summary counts from Step 1.
Use the leading status emoji based on worst overall status:
  - All OK     → ✅
  - Any WARNING → ⚠️
  - Any CRITICAL → 🔴

Message format:
  *Linux Diagnostics — [date]*
  [emoji] Hosts: [total] | ✅ OK: [ok] | ⚠️ Warning: [warning] | 🔴 Critical: [critical]
  Report sent to <ops-team@example.com>

### Step 6: Confirm and Stop
After Slack is sent, respond with a one-line summary:
"Diagnostics complete. [N] hosts checked: [X] OK, [Y] WARNING, [Z] CRITICAL.
Report sent to <ops-team@example.com>."
Then stop. Do not repeat output already in the email.

## Rules
- Always run Step 1 first — never skip diagnostics.
- Always send the email in Step 4 even if some hosts were unreachable.
- Always send the Slack notification in Step 5 after the email.
- Mark unreachable hosts as CRITICAL with reason "Host unreachable".
- Never ask the user for confirmation between steps.
- Do not truncate or summarize the per-host data — include all metrics in
  the HTML report, even if values are within normal range.
```

### 5.2 User Prompt (Default Objective)

```
Run a full diagnostics check on all Linux hosts in the inventory and email
the ops team a complete health report. Use target_hosts: "all" unless
specific hosts were provided in this request.
```

---

## 6. HTML Report Structure

The report sent via email must follow this structure. The builder should render this as a complete `<!DOCTYPE html>` document with inline CSS (no external stylesheets — Outlook strips them).

### 6.1 Overall Layout

```
┌─────────────────────────────────────────────────────┐
│  HEADER BANNER  (color by worst status)             │
│  "Linux Diagnostics Report"                         │
│  Ran: 2026-04-10 14:05:22 UTC | Scope: all (4 hosts)│
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  EXECUTIVE SUMMARY TABLE                            │
│  Hostname | IP | Status | # Warnings | # Criticals  │
│  linux-host-1 | 192.0.2.10 | ✅ OK | 0 | 0           │
│  linux-host-2 | 192.0.2.20 | ⚠️ WARNING | 2 | 0    │
│  linux-host-3 | 192.0.2.30 | 🔴 CRITICAL | 1 | 1   │
│  linux-host-4 | 192.0.2.40 | ✅ OK | 0 | 0         │
└─────────────────────────────────────────────────────┘

[Per-host card × N hosts]
┌─────────────────────────────────────────────────────┐
│  HOST: linux-host-1 (192.0.2.10)        ✅ OK         │
│  ─────────────────────────────────────────────────  │
│  Uptime: 14 days, 3:22  |  Last reboot: 2026-03-27  │
│  OS: Amazon Linux 2023  |  Kernel: 6.1.82           │
│                                                     │
│  DISK                                               │
│  /         45G used / 100G  (45%)  ✅               │
│  /boot     180M used / 512M (35%)  ✅               │
│                                                     │
│  MEMORY                                             │
│  Total: 8192 MB | Used: 5120 MB | Free: 3072 MB     │
│  Cached: 1500 MB | Swap: 512 MB used / 2048 MB      │
│                                                     │
│  CPU                                                │
│  Cores: 4 | Load: 0.42 / 0.55 / 0.61 (1m/5m/15m)  │
│  Top Processes by CPU:                              │
│    1. java        8.2%                              │
│    2. python3     2.1%                              │
│    ...                                              │
│                                                     │
│  SERVICES                                           │
│  sshd   ✅ active    cron  ✅ active                │
│  mysql  N/A (not detected on this host)             │
│                                                     │
│  NETWORK                                            │
│  eth0: 192.0.2.10/24                               │
│  Listening ports: 22 (sshd), 8080 (java)           │
│                                                     │
│  INODES                                             │
│  /        12% used  ✅                              │
│  /boot    8% used   ✅                              │
│                                                     │
│  FAILED SYSTEMD UNITS: none ✅                      │
│  OOM EVENTS (24h): none ✅                          │
│  ZOMBIE PROCESSES: 0 ✅                             │
└─────────────────────────────────────────────────────┘
```

### 6.2 Color Palette (inline CSS)

| Status | Banner background | Badge background | Badge text |
|---|---|---|---|
| OK | `#1a7f37` (dark green) | `#d1fae5` | `#065f46` |
| WARNING | `#b45309` (amber) | `#fef3c7` | `#92400e` |
| CRITICAL | `#991b1b` (dark red) | `#fee2e2` | `#7f1d1d` |
| Header/card bg | `#1f2937` (dark slate) | — | — |
| Card body bg | `#f9fafb` | — | — |
| Table stripe | `#f3f4f6` | — | — |

### 6.3 Status Badge Rules

- If the agent cannot reach a host: show `UNREACHABLE` in red with a note explaining the host was not accessible during the run.
- A host's badge is the worst of all its individual check results.
- The header banner color is the worst across all hosts.

---

## 7. New Service: `linux-diagnostics` (Ansible)

### 7.1 Service Identity

| Field | Value |
|---|---|
| Service name | `linux-diagnostics` |
| IAG tool identifier | `<iag-cluster-id>//linux-diagnostics` |
| Service type | `ansible-playbook` |
| Working directory | `linux_patch_check` (reuse existing service dir) |
| Playbook | `linux_diagnostics.yml` (new file, add alongside existing playbooks) |
| Inventory | `inventory.yaml` (existing, no changes needed) |
| SSH secret | `<SSH-SECRET-NAME>` (same pattern as all other linux services) |
| Repository | `<ansible-repo-name>` |
| Reference | `devel` |

### 7.2 Gateway Service YAML

**File:** `ansible/.gateway/services/linux-diagnostics.yml`

```yaml
services:
  - name: linux-diagnostics
    type: ansible-playbook
    description: >
      Runs comprehensive Linux health diagnostics across inventory hosts.
      Collects disk, memory, CPU, uptime, service status, network interfaces,
      inode usage, failed systemd units, OOM events, and zombie process counts.
      Returns structured JSON per host via set_stats.
    playbooks:
      - linux_diagnostics.yml
    working-directory: linux_patch_check
    repository: <ansible-repo-name>
    reference: devel
    decorator: linux-diagnostics
    secrets:
      - name: <SSH-SECRET-NAME>
        type: env
        target: <SSH-SECRET-NAME>
    runtime:
      inventory:
        - inventory.yaml
      config-file: ansible.cfg
      env:
        ANSIBLE_HOST_KEY_CHECKING: "false"
        ANSIBLE_STDOUT_CALLBACK: json

repositories:
  - name: <ansible-repo-name>
    url: git@gitlab.com:itential/sales-engineer/iag5/ansible.git
    private-key-name: git-key

decorators:
  - name: linux-diagnostics
    schema:
      $id: linux-diagnostics
      type: object
      additionalProperties: false
      properties:
        target_hosts:
          type: string
          description: >
            Ansible inventory host pattern. Use "all" for all hosts,
            a single hostname like "linux-host-1", or a comma-separated
            list like "linux-host-2,linux-host-3".
          default: "all"
          examples: ["all", "linux-host-1", "linux-host-2,linux-host-3"]
      required:
        - target_hosts
```

**Critical:** Do NOT include `$schema` in the decorator. The `$schema` field causes Anthropic's API to reject the tool definition at runtime. `$id` is fine; `$schema` is not.

### 7.3 New Playbook: `linux_diagnostics.yml`

**File location:** `ansible/linux_patch_check/linux_diagnostics.yml`

This playbook follows the same three-play pattern as the existing playbooks in this service directory.

#### Play 1 — SSH Setup (localhost)

Same pattern as all existing playbooks: include `tasks/prepare_ssh.yml`, then use `add_host` to build the dynamic `diag_targets` group from `target_hosts`.

```yaml
- name: Prepare SSH and Dynamic Inventory
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Run SSH setup
      ansible.builtin.include_tasks: tasks/prepare_ssh.yml

    - name: Add target hosts to dynamic group
      ansible.builtin.add_host:
        name: "{{ item }}"
        groups: diag_targets
      loop: "{{ target_hosts.split(',') | map('trim') | list }}"
      # Handle "all" specially — expand from inventory groups
      when: target_hosts != 'all'

    - name: Add ALL hosts to dynamic group when target is 'all'
      ansible.builtin.add_host:
        name: "{{ item }}"
        groups: diag_targets
      loop: "{{ groups['all'] }}"
      when: target_hosts == 'all'
```

#### Play 2 — Diagnostics Collection (diag_targets)

```yaml
- name: Linux Diagnostics Collection
  hosts: diag_targets
  gather_facts: yes
  become: yes
  vars:
    ansible_ssh_private_key_file: "{{ hostvars['localhost']['ssh_key_path'] | default(omit) }}"
  tasks:
    - block:

        # ── DISK ──────────────────────────────────────────────────────────
        - name: Collect disk usage (df -h)
          ansible.builtin.command: df -h --output=source,size,used,avail,pcent,target
          register: df_output
          changed_when: false

        - name: Parse disk usage into structured list
          ansible.builtin.set_fact:
            disk_mounts: >-
              {{
                df_output.stdout_lines[1:] | map('split') | list
                | map('zip', ['source','size','used','avail','percent_str','mount'])
                | map('community.general.dict') | list
              }}
          # Note: builder may need to adjust parsing approach depending on
          # available filters. Alternative: use ansible_mounts from gather_facts.

        - name: Flag mounts with disk usage > 80%
          ansible.builtin.set_fact:
            disk_warnings: >-
              {{
                ansible_mounts
                | selectattr('mount', 'in', ['/', '/boot', '/var', '/tmp', '/home'])
                | selectattr('size_total', 'gt', 0)
                | map(attribute='mount')
                | list
              }}
          # Use ansible_mounts (from gather_facts) for threshold logic.
          # Calculate used_pct = (size_total - size_available) / size_total * 100

        - name: Build disk facts from gather_facts mounts
          ansible.builtin.set_fact:
            diag_disk: >-
              {{
                ansible_mounts | selectattr('size_total', 'gt', 0) | list
                | map(attribute_map) | list
              }}
          # Structure per mount: { mount, device, size_total_gb, size_available_gb,
          #                         used_pct, status }
          # status = "CRITICAL" if used_pct > 90, "WARNING" if > 80, else "OK"

        # ── MEMORY ────────────────────────────────────────────────────────
        - name: Collect /proc/meminfo
          ansible.builtin.command: cat /proc/meminfo
          register: meminfo_raw
          changed_when: false

        - name: Build memory facts
          ansible.builtin.set_fact:
            diag_memory:
              total_mb: "{{ ansible_memtotal_mb }}"
              free_mb: "{{ ansible_memfree_mb }}"
              used_mb: "{{ ansible_memtotal_mb - ansible_memfree_mb }}"
              cached_mb: "{{ ansible_memory_mb.nocache.free | default(0) }}"
              swap_total_mb: "{{ ansible_swaptotal_mb }}"
              swap_free_mb: "{{ ansible_swapfree_mb }}"
              swap_used_mb: "{{ ansible_swaptotal_mb - ansible_swapfree_mb }}"
              swap_used_pct: >-
                {{
                  (((ansible_swaptotal_mb - ansible_swapfree_mb) / ansible_swaptotal_mb * 100)
                  | round(1)) if ansible_swaptotal_mb > 0 else 0
                }}
              status: >-
                {{
                  'CRITICAL' if ansible_memfree_mb < 64
                  else 'WARNING' if ansible_memfree_mb < 256
                  else 'OK'
                }}

        # ── CPU ───────────────────────────────────────────────────────────
        - name: Get top 5 processes by CPU
          ansible.builtin.shell: |
            ps aux --sort=-%cpu | awk 'NR>1 {print $1, $3, $11}' | head -5
          register: top_cpu_procs
          changed_when: false

        - name: Build CPU facts
          ansible.builtin.set_fact:
            diag_cpu:
              cores: "{{ ansible_processor_vcpus }}"
              load_1m: "{{ ansible_loadavg['1m'] }}"
              load_5m: "{{ ansible_loadavg['5m'] }}"
              load_15m: "{{ ansible_loadavg['15m'] }}"
              load_per_core_1m: "{{ (ansible_loadavg['1m'] | float / ansible_processor_vcpus | float) | round(2) }}"
              top_processes_by_cpu: "{{ top_cpu_procs.stdout_lines }}"
              status: >-
                {{
                  'CRITICAL' if (ansible_loadavg['1m'] | float / ansible_processor_vcpus | float) > 5.0
                  else 'WARNING' if (ansible_loadavg['1m'] | float / ansible_processor_vcpus | float) > 2.0
                  else 'OK'
                }}

        # ── UPTIME ────────────────────────────────────────────────────────
        - name: Get uptime and last reboot
          ansible.builtin.shell: |
            echo "uptime=$(uptime -p)"
            echo "reboot=$(who -b | awk '{print $3, $4}')"
          register: uptime_raw
          changed_when: false

        - name: Build uptime facts
          ansible.builtin.set_fact:
            diag_uptime:
              uptime_human: "{{ ansible_uptime_seconds | int | human_readable(unit='s') }}"
              uptime_seconds: "{{ ansible_uptime_seconds }}"
              last_reboot: "{{ uptime_raw.stdout_lines | select('match', '^reboot=') | map('regex_replace', '^reboot=', '') | first | default('unknown') }}"

        # ── SERVICES ──────────────────────────────────────────────────────
        - name: Check core services status
          ansible.builtin.systemd:
            name: "{{ item }}"
          register: service_status_results
          loop:
            - sshd
            - cron
            - crond       # RHEL-family alias
            - mysql
            - mysqld
            - kafka
            - zabbix-agent
            - zabbix-server
          ignore_errors: yes
          failed_when: false

        - name: Build services facts
          ansible.builtin.set_fact:
            diag_services: >-
              {{
                service_status_results.results
                | selectattr('status', 'defined')
                | map(attribute_map_services)
                | list
              }}
          # For each service: { name, state: "active"|"inactive"|"not-found", status }
          # status = "CRITICAL" if sshd is not active
          # status = "WARNING" if any other service is inactive (not "not-found")
          # Note: "not-found" means the service doesn't exist on this host — that is OK,
          # not a warning (mysql on a kafka host, for example)

        # ── NETWORK ───────────────────────────────────────────────────────
        - name: Get listening ports
          ansible.builtin.shell: ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null
          register: listening_ports
          changed_when: false
          ignore_errors: yes

        - name: Build network facts
          ansible.builtin.set_fact:
            diag_network:
              interfaces: >-
                {{
                  ansible_interfaces
                  | map('extract', hostvars[inventory_hostname], 'ansible_' + item)
                  | ... 
                }}
              # Use ansible_all_ipv4_addresses and per-interface facts from gather_facts
              # Structure: [ { interface: "eth0", ip: "192.0.2.10", netmask: "255.255.255.0" } ]
              listening_ports_raw: "{{ listening_ports.stdout_lines | default([]) }}"

        # ── INODES ────────────────────────────────────────────────────────
        - name: Get inode usage
          ansible.builtin.command: df -i --output=source,iused,iavail,ipcent,target
          register: inode_output
          changed_when: false

        - name: Build inode facts
          ansible.builtin.set_fact:
            diag_inodes: >-
              {{
                inode_output.stdout_lines[1:]
                | ... parse into list of { mount, used_pct, status }
              }}
          # status = "CRITICAL" if used_pct > 90, "WARNING" if > 80, else "OK"

        # ── FAILED SYSTEMD UNITS ──────────────────────────────────────────
        - name: Get failed systemd units
          ansible.builtin.command: systemctl --failed --no-legend --plain
          register: failed_units
          changed_when: false
          ignore_errors: yes

        - name: Build failed units facts
          ansible.builtin.set_fact:
            diag_failed_units: "{{ failed_units.stdout_lines | default([]) | reject('equalto', '') | list }}"
            diag_failed_units_status: "{{ 'WARNING' if failed_units.stdout_lines | reject('equalto','') | list | length > 0 else 'OK' }}"

        # ── OOM EVENTS ────────────────────────────────────────────────────
        - name: Check for OOM kills in last 24 hours (journalctl)
          ansible.builtin.shell: |
            journalctl -k --since "24 hours ago" 2>/dev/null | grep -i "oom\|out of memory\|killed process" || true
          register: oom_check_journal
          changed_when: false
          ignore_errors: yes

        - name: Check for OOM kills in dmesg (fallback)
          ansible.builtin.command: dmesg
          register: oom_check_dmesg
          changed_when: false
          ignore_errors: yes
          when: oom_check_journal.stdout_lines | length == 0

        - name: Build OOM facts
          ansible.builtin.set_fact:
            diag_oom:
              events: "{{ oom_check_journal.stdout_lines | default([]) | reject('equalto','') | list }}"
              status: "{{ 'CRITICAL' if oom_check_journal.stdout_lines | reject('equalto','') | list | length > 0 else 'OK' }}"

        # ── ZOMBIE PROCESSES ──────────────────────────────────────────────
        - name: Count zombie processes
          ansible.builtin.shell: ps aux | awk '$8 == "Z" {count++} END {print count+0}'
          register: zombie_count
          changed_when: false

        - name: Build zombie facts
          ansible.builtin.set_fact:
            diag_zombies:
              count: "{{ zombie_count.stdout | int }}"
              status: "{{ 'WARNING' if zombie_count.stdout | int > 0 else 'OK' }}"

        # ── ROLL UP HOST STATUS ────────────────────────────────────────────
        - name: Determine overall host status
          ansible.builtin.set_fact:
            host_overall_status: >-
              {{
                'CRITICAL' if (
                  diag_disk | selectattr('status','equalto','CRITICAL') | list | length > 0
                  or diag_memory.status == 'CRITICAL'
                  or diag_cpu.status == 'CRITICAL'
                  or diag_inodes | selectattr('status','equalto','CRITICAL') | list | length > 0
                  or diag_services | selectattr('status','equalto','CRITICAL') | list | length > 0
                  or diag_oom.status == 'CRITICAL'
                )
                else 'WARNING' if (
                  diag_disk | selectattr('status','equalto','WARNING') | list | length > 0
                  or diag_memory.status == 'WARNING'
                  or diag_cpu.status == 'WARNING'
                  or diag_inodes | selectattr('status','equalto','WARNING') | list | length > 0
                  or diag_services | selectattr('status','equalto','WARNING') | list | length > 0
                  or diag_failed_units_status == 'WARNING'
                  or diag_zombies.status == 'WARNING'
                )
                else 'OK'
              }}

        # ── ASSEMBLE HOST RESULT ───────────────────────────────────────────
        - name: Assemble host diagnostic result
          ansible.builtin.set_fact:
            host_diag_result:
              hostname: "{{ inventory_hostname }}"
              ip_address: "{{ ansible_host }}"
              os_distribution: "{{ ansible_distribution }} {{ ansible_distribution_version }}"
              kernel: "{{ ansible_kernel }}"
              timestamp: "{{ ansible_date_time.iso8601 }}"
              overall_status: "{{ host_overall_status }}"
              disk: "{{ diag_disk }}"
              memory: "{{ diag_memory }}"
              cpu: "{{ diag_cpu }}"
              uptime: "{{ diag_uptime }}"
              services: "{{ diag_services }}"
              network: "{{ diag_network }}"
              inodes: "{{ diag_inodes }}"
              failed_units: "{{ diag_failed_units }}"
              failed_units_status: "{{ diag_failed_units_status }}"
              oom: "{{ diag_oom }}"
              zombies: "{{ diag_zombies }}"

      rescue:
        - name: Record host as unreachable/failed
          ansible.builtin.set_fact:
            host_diag_result:
              hostname: "{{ inventory_hostname }}"
              ip_address: "{{ ansible_host | default('unknown') }}"
              timestamp: "{{ ansible_date_time.iso8601 | default(lookup('pipe','date -u +%Y-%m-%dT%H:%M:%SZ')) }}"
              overall_status: "CRITICAL"
              error: "Host failed diagnostics collection — check connectivity and sudo access"

      always:
        - name: Cleanup SSH key
          ansible.builtin.include_tasks: tasks/cleanup_ssh.yml
```

#### Play 3 — Aggregate Results (localhost)

```yaml
- name: Aggregate Diagnostic Results
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Build diagnostics_results list from all hosts
      ansible.builtin.set_fact:
        diagnostics_results: >-
          {{
            hostvars | dict2items
            | selectattr('value.host_diag_result', 'defined')
            | map(attribute='value.host_diag_result')
            | list
          }}

    - name: Build summary counts
      ansible.builtin.set_fact:
        diag_summary:
          total_hosts: "{{ diagnostics_results | length }}"
          ok_count: "{{ diagnostics_results | selectattr('overall_status','equalto','OK') | list | length }}"
          warning_count: "{{ diagnostics_results | selectattr('overall_status','equalto','WARNING') | list | length }}"
          critical_count: "{{ diagnostics_results | selectattr('overall_status','equalto','CRITICAL') | list | length }}"

    - name: Set custom stats for IAG output
      ansible.builtin.set_stats:
        data:
          diagnostics_results: "{{ diagnostics_results }}"
          summary: "{{ diag_summary }}"
        aggregate: true
        per_host: false
```

---

## 8. Implementation Notes for the Builder

### 8.1 Reuse Pattern — Do Not Copy Files

The `linux-diagnostics` service uses the **same working directory** (`linux_patch_check`) as all existing linux patch services. This means:
- `inventory.yaml` — shared, no changes
- `ansible.cfg` — shared, no changes  
- `tasks/prepare_ssh.yml` and `tasks/cleanup_ssh.yml` — shared, no changes
- `requirements.yml` — shared, verify `community.general` collection is listed (needed for some filters)

Only **one new file** is added to the service directory: `linux_diagnostics.yml`.

### 8.2 Dynamic Group for target_hosts

The existing playbooks use a `from_json` filter pattern for array inputs:
```yaml
loop: "{{ target_hosts if target_hosts is iterable and target_hosts is not string else target_hosts | from_json }}"
```

For this playbook, `target_hosts` is a plain string (not JSON array), so use `split(',')` with `map('trim')` to handle comma-separated values. The `"all"` case must expand from `groups['all']` rather than trying to use "all" as a literal host name.

### 8.3 Interface Fact Extraction

Ansible's network interface facts use dynamic keys (`ansible_eth0`, `ansible_ens3`, etc.) based on what `gather_facts` discovers. Use `ansible_interfaces` to enumerate them, then extract IP info per interface. Exclude loopback (`lo`) from the report.

### 8.4 Service Detection Strategy

Do not hard-code which app services to check on which host. Instead:
- Always check `sshd` and `cron`/`crond` (core services)
- Probe `mysql`, `mysqld`, `kafka`, `zabbix-agent`, `zabbix-server` with `ignore_errors: yes` and `failed_when: false`
- A service returning "not-found" via systemd is silently excluded from the report — it is not a warning
- Only flag services that exist (are installed) but are not active

### 8.5 OOM Detection

`journalctl` is preferred. On older Amazon Linux instances that use SysV init instead of systemd, journalctl may not be available — fall back to parsing `dmesg` output. Use `ignore_errors: yes` on both and combine the results.

### 8.6 No $schema in Decorator

See the Known Issues section of the SKILL.md for the IAG5 CI pipeline. The `$schema` field in decorator schemas causes Anthropic's API to reject the tool at runtime. Omit it entirely from the decorator YAML. The `$id` field is fine.

### 8.7 Commit Scope

When committing to the ansible repo:
```bash
git add ansible/.gateway/services/linux-diagnostics.yml
git add ansible/linux_patch_check/linux_diagnostics.yml
git commit -m "feat: add linux-diagnostics ansible service"
git push origin devel
```

Do not modify any existing files in `linux_patch_check/`. The new service is purely additive.

### 8.8 Agent Deployment

Deploy the FlowAI agent via the platform API or UI after the service is confirmed deployed:
- Verify `<iag-cluster-id>//linux-diagnostics` appears in the tool registry before creating the agent
- Verify `<iag-cluster-id>//send-email` is still present and working
- Agent capabilities: toolset = `["<iag-cluster-id>//linux-diagnostics", "<iag-cluster-id>//send-email"]`
- No LCM projects, sub-agents, or workflows needed

---

## 9. Acceptance Criteria

The implementation is complete when:

1. `linux-diagnostics.yml` playbook runs successfully against all 4 inventory hosts with `target_hosts: "all"`
2. IAG service `<iag-cluster-id>//linux-diagnostics` appears in the FlowAI tool registry
3. A single agent invocation with no arguments produces a diagnostic run, builds an HTML report, and delivers it to `<ops-team@example.com>`
4. The HTML email correctly badges each host as OK / WARNING / CRITICAL based on the threshold rules in Section 5.1
5. A host that is unreachable appears in the email as CRITICAL with an error note rather than crashing the agent
6. Targeting a single host (`target_hosts: "linux-host-1"`) produces a report scoped to that host only

---

## 10. File Checklist for Builder

| File | Action | Path |
|---|---|---|
| `linux_diagnostics.yml` | CREATE | `ansible/linux_patch_check/linux_diagnostics.yml` |
| `linux-diagnostics.yml` | CREATE | `ansible/.gateway/services/linux-diagnostics.yml` |
| `inventory.yaml` | NO CHANGE | `ansible/linux_patch_check/inventory.yaml` |
| `ansible.cfg` | NO CHANGE | `ansible/linux_patch_check/ansible.cfg` |
| `tasks/prepare_ssh.yml` | NO CHANGE | `ansible/linux_patch_check/tasks/prepare_ssh.yml` |
| `tasks/cleanup_ssh.yml` | NO CHANGE | `ansible/linux_patch_check/tasks/cleanup_ssh.yml` |
| `requirements.yml` | VERIFY `community.general` is listed | `ansible/linux_patch_check/requirements.yml` |
| FlowAI agent | CREATE via API/UI | Platform: <iag-cluster-id> |


````

============================================================
FILE: spec-files/demo/spec-dns-a-record-infoblox-simple.md
DIRECTORY: spec-files/demo/
FILENAME: spec-dns-a-record-infoblox-simple.md
============================================================
SHA256: b7bbb890806a000a3c00b392634ff2074556b9288f5ec170145372389a694474

````markdown
# DNS A Record Provisioning — Simple (Infoblox)

## Problem Statement

Network engineers manually log into Infoblox to create DNS A records, introducing delay and risk of typos. This automation provides a self-service JSON Form in Operations Manager and fully automatic provisioning via the Infoblox adapter — no manual tasks in the workflow. On success, an email notification is sent with the provisioned record details.

---

## Flow

```
[Operations Manager]
  Trigger: Manual (legacyWrapper: false)
  Form: "DNS A Record - Simple" (JSON Form)
  Operator fills in hostname, zone (dropdown), IP, view, TTL, comment → clicks Run
         |
         v
   [workflow_start]  <-- job variables: hostname, zone, ip_address, dns_view, ttl, comment
         |
         v
   [merge FQDN vars] → [makeData FQDN] → [merge body] → [createARecord]
                                                              |
                                            success → [query _ref] → [merge email vars] → [makeData email body] → [mailWithOptions] → workflow_end
                                                                                                                        |
                                                                                                                     [error] → [email warning] → workflow_end
                                            error → [errorHandler] → workflow_end
```

**Entrypoint:** Operations Manager automation with a JSON Form bound to a manual trigger (`legacyWrapper: false`). The form collects all inputs. The workflow receives them as job variables and executes fully automatically — no manual/review tasks.

> **Important:** The trigger must set `legacyWrapper: false` so that form fields map directly to job variables. When `legacyWrapper: true` (the default), form data is nested under `formData`, breaking the variable mapping.

---

## Platform Assets

| Asset | Type | Name |
|-------|------|------|
| JSON Form | Operations Manager Form | `DNS A Record - Simple` |
| Workflow | Automation | `DNS A Record Provisioning - Simple` |
| Project | Automation Studio Project | `DNS A Record Provisioning - Simple` |

### Project Membership

| Type | Role | Reference |
|------|------|-----------|
| account | owner | `<recipient@example.com>` |
| group | editor | `<editor-group-name>` |

---

## JSON Form Fields

Form name (exact): `DNS A Record - Simple`

Bound to the Operations Manager automation as a **manual trigger form**.

| Field Key | Label | Type | Required | Default | Notes |
|-----------|-------|------|----------|---------|-------|
| `hostname` | Hostname | string | yes | — | Short name only (e.g. `web01`). Combined with `zone` to form the FQDN. |
| `zone` | DNS Zone | string (dropdown) | yes | — | Dropdown with available Infoblox authoritative zones. See **Zone Dropdown Values** below. |
| `ip_address` | IP Address | string | yes | — | IPv4, e.g. `192.0.2.100` |
| `dns_view` | DNS View | string | yes | `default` | Infoblox view name |
| `ttl` | TTL (seconds) | number | no | `3600` | Record time-to-live |
| `comment` | Comment | string | no | — | Free-text note stored on the record |

### Zone Dropdown Values

The `zone` field is a dropdown populated with the authoritative zones from Infoblox. Maintain this list when zones are added or removed.

| Value | Label |
|-------|-------|
| `corp.example.com` | corp.example.com |
| `lab.example.com` | lab.example.com |
| `dev.example.com` | dev.example.com |
| `staging.example.com` | staging.example.com |

---

## Adapter Identity

### Infoblox

| Field | Value |
|-------|-------|
| Adapter type (`app`, `locationType`) | `Infoblox` |
| Instance name (`adapter_id`) | Resolve from `adapters.json` at build time — do not hardcode a name in the spec |

> **Note:** The `adapter_id` should be hardcoded in the workflow task (not passed as a job variable) since this is a single-adapter use case.

### Email

| Field | Value |
|-------|-------|
| Adapter type (`app`, `locationType`) | `EmailOpensource` |
| Instance name (`adapter_id`) | Resolve from `adapters.json` at build time |

> **Note:** Same rule — hardcode `adapter_id` in the workflow task.

---

## Workflow Tasks

### Task 1 — Build FQDN Variables (operation)

```
name:       merge
canvasName: merge
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

Builds the variables object for the FQDN makeData task.

> **Why merge + makeData instead of stringConcat?** `stringConcat` takes `str` (string) and `stringN` (array), but `$var` references inside the `stringN` array do not resolve — they are stored as literal strings. The `merge` → `makeData` pattern resolves variables correctly via `<!var!>` placeholders.

**`data_to_merge` array:**

| key | source | task | variable |
|-----|--------|------|----------|
| `hostname` | job var | `job` | `hostname` |
| `zone` | job var | `job` | `zone` |

**Outgoing:** `merged_object`

**Transitions:**
- `success` → Build FQDN

---

### Task 2 — Build FQDN (operation)

```
name:       makeData
canvasName: makeData
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

Concatenates hostname and zone into the FQDN using `<!var!>` placeholders.

**Incoming variables:**

| Field | Type | Value |
|-------|------|-------|
| `input` | string | `<!hostname!>.<!zone!>` |
| `outputType` | string | `string` |
| `variables` | object | `$var.<mergeTaskId>.merged_object` |

**Outgoing:** `output` → `$var.job.fqdn`

**Transitions:**
- `success` → Build Infoblox Body

---

### Task 3 — Build Request Body (operation)

```
name:       merge
canvasName: merge
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

**`data_to_merge` array:**

| key | source | task | variable |
|-----|--------|------|----------|
| `name` | job var | `job` | `fqdn` |
| `ipv4addr` | job var | `job` | `ip_address` |
| `view` | job var | `job` | `dns_view` |
| `ttl` | job var | `job` | `ttl` |
| `comment` | job var | `job` | `comment` |

**Outgoing:** `merged_object`

**Transitions:**
- `success` → Create A Record

---

### Task 4 — Create A Record (automatic)

```
name:       createARecord
canvasName: createARecord
app:        Infoblox (from apps.json)
locationType: Infoblox
type:       automatic
actor:      Pronghorn
```

**Incoming variables:**

| Field | Type | Value |
|-------|------|-------|
| `body` | object | `$var.<mergeTaskId>.merged_object` |
| `adapter_id` | string | Hardcoded to the instance name from `adapters.json` (not a job variable) |

The `body` sent to Infoblox WAPI `POST /record:a`:
```json
{
  "name":     "<FQDN>",
  "ipv4addr": "<IPv4>",
  "view":     "<dns_view>",
  "ttl":      <integer>,
  "comment":  "<string>"
}
```

**Response shape:**
```
$var.<taskId>.result.response   →  "record:a/ZG5z..."  (the _ref string)
```

**Transitions:**
- `success` → Extract Infoblox Ref
- `error` → Error Handler

---

### Task 5 — Extract Infoblox Ref (operation)

```
name:       query
canvasName: query
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

Extracts the `_ref` string from the adapter response. The `createARecord` result is an object — `result.response` contains the `_ref` string.

**Incoming variables:**

| Field | Type | Value |
|-------|------|-------|
| `pass_on_null` | boolean | `false` |
| `query` | string | `response` |
| `obj` | object | `$var.<createARecordTaskId>.result` |

**Outgoing:** `return_data` → `$var.job.infoblox_ref`

**Transitions:**
- `success` → Build Email Variables

---

### Task 6 — Build Email Variables (operation)

```
name:       merge
canvasName: merge
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

Builds the variables object for the email body makeData task.

**`data_to_merge` array:**

| key | source | task | variable |
|-----|--------|------|----------|
| `fqdn` | job var | `job` | `fqdn` |
| `ip_address` | job var | `job` | `ip_address` |
| `dns_view` | job var | `job` | `dns_view` |
| `ref` | job var | `job` | `infoblox_ref` |

**Outgoing:** `merged_object`

**Transitions:**
- `success` → Build Email Body

---

### Task 7 — Build Email Body (operation)

```
name:       makeData
canvasName: makeData
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

Constructs the email body string with record details using `<!var!>` placeholders.

**Incoming variables:**

| Field | Type | Value |
|-------|------|-------|
| `input` | string | `DNS A Record Provisioned Successfully\n\nFQDN: <!fqdn!>\nIP Address: <!ip_address!>\nDNS View: <!dns_view!>\nInfoblox Ref: <!ref!>` |
| `outputType` | string | `string` |
| `variables` | object | `$var.<emailVarsMergeTaskId>.merged_object` |

**Outgoing:** `output` (wired directly to the email task via `$var.<taskId>.output` — no job variable needed)

**Transitions:**
- `success` → Send Email

---

### Task 8 — Send Email (automatic)

```
name:       mailWithOptions
canvasName: mailWithOptions
app:        EmailOpensource (from apps.json)
locationType: EmailOpensource
type:       automatic
actor:      Pronghorn
```

**Incoming variables:**

| Field | Type | Value |
|-------|------|-------|
| `from` | string | `<noreply@example.com>` |
| `to` | array | `["<recipient@example.com>"]` |
| `subject` | string | `DNS A Record Provisioned` |
| `body` | string | `$var.<makeDataTaskId>.output` (wired from previous task, not a job variable) |
| `displayName` | string | `Itential` |
| `adapter_id` | string | Hardcoded to the instance name from `adapters.json` |

**Transitions:**
- `success` → workflow_end
- `error` → Email Warning

---

### Task 9 — Email Warning (operation)

```
name:       newVariable
canvasName: newVariable
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

Sets `email_warning` = `"DNS record created successfully but email notification failed."`

Exists because JSON transitions cannot have duplicate keys — both success and error from the email task cannot both target `workflow_end` directly.

**Transitions:**
- `success` → workflow_end

---

### Task 10 — Error Handler (operation)

```
name:       newVariable
canvasName: newVariable
app:        WorkFlowEngine
type:       operation
actor:      Pronghorn
```

Sets `error_message` = `"DNS A Record provisioning failed or was rejected. Check job error for details."`

**Transitions:**
- `success` → workflow_end

---

## Full Task Sequence

```
workflow_start
  → merge (Build FQDN Variables)
  → makeData (Build FQDN)
  → merge (Build Infoblox Body)
  → createARecord
        success → query (Extract Infoblox Ref)
                    → merge (Build Email Variables)
                    → makeData (Build Email Body)
                    → mailWithOptions (Send Email)
                          success → workflow_end
                          error   → newVariable (Email Warning) → workflow_end
        error   → newVariable (Error Handler) → workflow_end
```

**Total: 10 tasks.** Fully automatic — no manual tasks, no child workflows.

---

## Error Handling

- **Infoblox errors:** The `createARecord` task gets a `"state": "error"` transition → error handler. No retries, no rollback. Re-running the automation is the recovery path.
- **Email errors:** The `mailWithOptions` task error transition routes to an email warning `newVariable` task, then to `workflow_end`. Email delivery failure does not fail the job — the DNS record was already created successfully.

---

## Acceptance Criteria

1. An operator opens the automation in Operations Manager, fills in the JSON Form (hostname from text field, zone from dropdown, IP, view), and clicks Run.
2. The workflow executes fully automatically — no pauses, no manual steps.
3. A successful run creates a DNS A record in Infoblox and the job output contains the `_ref` string.
4. On success, an email is sent to `<recipient@example.com>` with the provisioned record details (FQDN, IP, view, `_ref`).
5. Any Infoblox adapter error routes to the error handler; the job does not hang.
6. Email delivery failure does not block or fail the job.
7. The workflow contains exactly 10 tasks — no manual tasks, no form tasks, no child workflows.

---

## Amendments

**2026-04-06 — Initial build lessons learned:**

1. **`adapter_id` must be hardcoded from `adapters.json`** — never assume instance names from the spec. The spec originally said `infobloxv9` but the actual adapter instance was `Infoblox`. Always resolve at build time.
2. **`legacyWrapper: false` is mandatory on manual triggers** — the default (`true`) wraps form data under `formData`, breaking variable mapping to job variables.
3. **`stringConcat` does not resolve `$var` inside `stringN` arrays** — use `merge` → `makeData` with `<!var!>` placeholders instead.
4. **Adapter responses are objects, not primitives** — `createARecord` returns `{response: "<_ref>", ...}`. A `query` task is needed to extract the `_ref` string before passing it to downstream tasks.
5. **Prefer task-to-task variable wiring (`$var.taskId.output`) over job variables** — only use job variables when values need to cross non-adjacent tasks or be visible in job output.
6. **Email `displayName` field** — include `displayName` in `mailWithOptions` incoming to control the sender display name (e.g. `"Itential"`).

````

============================================================
FILE: spec-files/demo/spec-dns-a-record-provisioning.md
DIRECTORY: spec-files/demo/
FILENAME: spec-dns-a-record-provisioning.md
============================================================
SHA256: a9152d863c5cc13a7626f58d7ca15648893c1a501cc1cd1461dca7ff09994b84

````markdown
# Use Case: DNS A Record Provisioning

## 1. Problem Statement

Engineers create DNS A records manually through provider consoles or ad-hoc scripts. There's no pre-flight validation — duplicate records get created, IP conflicts go undetected, and mistakes propagate before anyone notices. There's no human review step for changes that could impact production services. When something goes wrong, rollback is manual and there's no record of what changed or who approved it.

**Goal:** Automate DNS A record creation with pre-flight conflict detection, human approval before the change goes live, automatic rollback if denied, and notification to the engineering team — producing a deterministic, auditable workflow that behaves the same on every run.

---

## 2. High-Level Flow

```
Phase 1          Phase 2          Phase 3               Phase 4
Pre-Check   →   Execution   →   Post-Check + HITL   →   Notify
(Verify)        (Act)           (Validate)              (Inform)
    │               │                │                      │
 Query existing  Create the       Confirm record       Send notification
 records,        A record         is live,             with change
 detect          if clear         present to           details
 conflicts                        operator
                                     │
                              Approved? → Proceed to notify
                              Denied?   → Rollback the record
```

---

## 3. Phases

### Phase 1: Pre-Check (Verify)

Before any write operation, query the DNS provider for existing A records matching the requested hostname. Three possible outcomes:

| Outcome | Condition | Action |
|---------|-----------|--------|
| **Clear** | No existing record for this hostname | Proceed to Phase 2 |
| **Idempotent** | Record exists with the exact same IP | Stop — the desired state already exists. No action needed. |
| **Conflict** | Record exists with a different IP | Stop — flag the conflict. Do not overwrite silently. |

The idempotency check makes this workflow safe to re-run. The conflict check prevents silent IP overwrites that could take down services.

### Phase 2: Execution (Act)

Create the A record in the DNS provider using the validated inputs. Extract the provider's record reference ID for use in rollback and audit trail.

### Phase 3: Post-Check + Human Review (Validate)

After creation, query the DNS provider again to confirm the record is live. Then present the change details to a human operator for review — including the hostname, IP, zone, and provider reference.

The operator can **approve** (proceed to notification) or **deny** (trigger rollback).

**Key design question:** Should the record be created before or after human review?

- **Create-then-review** — the reviewer sees confirmed system state (the record exists, the Ref-ID is real). If denied, rollback deletes it. More information for the reviewer, but requires rollback capability.
- **Review-then-create** — nothing changes until approved. Simpler, but the reviewer is approving a plan, not a confirmed state.

### Phase 4: Notify (Inform)

Send a notification to the engineering team with the change details: hostname, IP, zone, record reference, and the reviewer's decision. Notification failure should not roll back the DNS change — the record is the primary deliverable, notification is secondary.

### Rollback

If the human reviewer denies the change, delete the record that was created in Phase 2 using the captured reference ID. If rollback itself fails, escalate immediately — a record exists that shouldn't.

---

## 4. Key Design Decisions

| Decision | Options | Considerations |
|----------|---------|----------------|
| Create-then-review vs review-then-create | Create first, then seek approval / Get approval first, then create | Create-first gives reviewer real state; review-first avoids needing rollback |
| HITL mechanism | Manual task in workflow / Separate child workflow / External approval system | Simplicity vs reusability vs integration with existing approval flows |
| Notification channel | Email / ITSM ticket / Chat (Slack, Teams) / Multiple | What does the team already use? Is email sufficient? |
| Notification failure handling | Block and retry / Non-blocking warning / Skip silently | Is notification critical or informational? |
| Rollback failure handling | Retry / Escalate immediately / Both | A failed rollback means an unauthorized record persists |
| Post-check failure handling | Block the workflow / Non-blocking warning, proceed to HITL | Replication delays may cause transient failures — is a warning enough? |
| API approach | REST API via adapter / CLI via SSH / Direct SDK calls | What does the DNS provider support? What adapter is available? |
| Service exposure | Manual form only / API endpoint only / Both | Who triggers this — operators via UI, or upstream systems via API? |

---

## 5. Scope

**In scope:** A record creation for a single hostname. Pre-flight conflict and idempotency detection. Post-creation verification. Human approval gate with rollback on denial. Notification to engineering team.

**Out of scope:** Other record types (AAAA, CNAME, MX, TXT, SRV, PTR, NS). Record update or delete as a primary operation (delete is only used for rollback). Bulk/batch record operations. Multi-provider support. PTR/reverse record synchronization. DNSSEC. Propagation verification via external resolvers. TTL management. IPAM integration. ITSM ticket creation.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| DNS provider API unavailable during create | Record cannot be created | Error transition to a clear outcome — no partial state since nothing was written |
| Rollback fails after reviewer denial | Unauthorized record persists in DNS | Escalation path — set outcome to CRITICAL, alert immediately |
| Post-check fails due to replication delay | Reviewer sees stale data | Non-blocking warning — proceed to HITL, note the delay |
| Duplicate workflow runs for same hostname | Multiple records created | Phase 1 idempotency check prevents duplicates — safe to re-run |
| Notification system down | Team not informed of change | Non-blocking — DNS change is the deliverable, not the email |
| Operator ignores HITL gate | Workflow stalled indefinitely | Platform timeout or escalation policy (outside workflow scope) |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Query existing DNS A records by hostname | Yes | Cannot detect conflicts or idempotency — unsafe to proceed |
| Create DNS A record via provider API | Yes | Cannot proceed |
| Delete DNS A record (for rollback) | Yes | Cannot offer rollback — review-then-create becomes the only option |
| Human-in-the-loop gate (pause for operator decision) | Yes | Cannot proceed — HITL is mandatory per spec |
| Send email notification | No | Skip Phase 4 — DNS change still works without notification |
| Build dynamic request bodies from job variables | Yes | Cannot assemble API payloads |
| Branch on conditions (record exists, IP matches) | Yes | Cannot implement pre-check logic |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| DNS provider (e.g., Infoblox, Route53, Cloudflare) | Authoritative source for A records — receives query, create, delete calls | Yes | Cannot proceed |
| Email server | Deliver notification to engineering team | No | Phase 4 skipped — DNS change still works |

### Discovery Questions

1. **Which DNS provider do you use?** (Infoblox, Route53, Cloudflare, Azure DNS, other?) Is the adapter installed and connected?
2. **Which adapter methods are available?** Specifically: query/get A records, create A record, delete A record. What are the exact task names?
3. **What zone are you targeting?** Does the zone already exist? Is there a default zone?
4. **Create-then-review or review-then-create?** Do you want the reviewer to see the confirmed state (record already created, real Ref-ID) or approve a plan before anything changes?
5. **Who reviews changes?** Is there a specific operator role, or does the requestor self-review? Should the reviewer be different from the requestor?
6. **How should the team be notified?** Email? Chat? Ticket? Who receives the notification?
7. **What happens if notification fails?** Should it block the workflow or proceed with a warning?
8. **How should this be triggered?** Operator filling out a form in the UI? API call from an upstream system? Both?
9. **What input fields are needed?** Hostname, IP, zone — anything else? Adapter selection? Notification recipient?
10. **What does the operator need to see in the review step?** Hostname and IP only? Or also zone, Ref-ID, record key?
11. **Are there existing DNS workflows or templates to reuse?** Any prior automation for this provider?

---

## 8. Batch Strategy

Not applicable for v1 — this spec covers single-record operations only. Batch support (CSV import, bulk provisioning) is a future extension.

---

## 9. Acceptance Criteria

1. Phase 1 detects idempotency — workflow stops cleanly when the exact record already exists
2. Phase 1 detects conflict — workflow stops cleanly when a record exists with a different IP
3. Phase 2 creates the A record and captures the provider reference ID
4. Phase 3 post-check confirms the record is live in the DNS provider
5. HITL gate pauses for operator review with change details visible
6. Approve → record persists, notification sent, outcome: SUCCESS
7. Deny → record deleted (rollback), outcome: ROLLED BACK
8. Every adapter/external call has an error path — no stuck workflows
9. Notification failure does not roll back the DNS change
10. Workflow produces a clear outcome variable on every run (SUCCESS, IDEMPOTENT, CONFLICT, ROLLED BACK, ERROR, CRITICAL)

````

============================================================
FILE: spec-files/spec-arista-eos-ab-upgrade.md
DIRECTORY: spec-files/
FILENAME: spec-arista-eos-ab-upgrade.md
============================================================
SHA256: 9ea36939ceabcb76909ed46a1ec7df7504d7c50e72b65bac442532eaaedb0e6d

````markdown
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

````

============================================================
FILE: spec-files/spec-aws-webserver-deploy.md
DIRECTORY: spec-files/
FILENAME: spec-aws-webserver-deploy.md
============================================================
SHA256: 11f72c2d40c8260d562ff1bb9b37462f0a097234b44956b0363f8a369304e906

````markdown
# Use Case: AWS Web Server Deployment

## 1. Problem Statement

Deploying a web server on AWS requires manual steps across multiple tools: the AWS console to create security groups and launch an instance, an SSH session or Ansible run to configure the OS and install the web server, and a manual browser check to verify the result. Each engineer does it differently, there's no audit trail, and the process is error-prone — ports get misconfigured, instances launch without tags, and nobody validates that the service is actually reachable before closing the ticket.

**Goal:** Automate the full deployment lifecycle — from bare infrastructure to a validated, live HTTP endpoint — in a single orchestrated workflow. Provision the EC2 instance with proper security group rules, configure the web server via Ansible, and verify HTTP reachability, with every step observable and every failure captured cleanly.

---

## 2. High-Level Flow

```
Provision      →  Configure      →  Validate       →  Close Out
    │                 │                 │                 │
    │                 │                 │                 │
 Create SG,        Connect via      HTTP GET           Report
 open ports        SSH, install     against            outputs:
 22 + 80,          web server       public IP,         instance_id,
 launch EC2,       (nginx),         verify             public_ip,
 poll until        deploy sample    200 OK,            service
 running,          page             content            status
 tag instance                       check
    │                 │                 │
 FAIL? → Stop     FAIL? → Stop     FAIL? → Flag
 and report       and report       deployment
                                   as unhealthy
```

---

## 3. Phases

### Provision
Create an EC2 security group scoped to the target VPC. Authorize inbound traffic on port 22 (SSH for configuration) and port 80 (HTTP for the web server). Launch a t2.micro (or specified) instance with the provided AMI, key pair, and subnet. Poll the instance state until it reaches "running." Tag the instance with a Name and a ManagedBy label for traceability. If any AWS API call fails, **stop — do not proceed to configuration**.

### Configure
Connect to the running instance via SSH through the Automation Gateway. Run an Ansible playbook that installs the web server package (nginx), deploys a sample Hello World page to the document root, and ensures the service is started and enabled. The playbook must be idempotent — safe to re-run. If the Ansible service call fails, **stop and report the error with stdout**.

### Validate
Construct the full URL (`http://{public_ip}`) and invoke an HTTP validation service against the deployed endpoint. Verify the response returns HTTP 200. If validation fails, **flag the deployment as unhealthy** — the instance is running but the web server is not serving correctly.

---

## 4. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| EC2 adapter direct vs. IAG Python service | EC2 adapter direct | Full task-level visibility in the Itential job view; known response shapes; no black-box dependency |
| Monolithic workflow vs. child decomposition | Three child workflows + parent orchestrator | Each phase is independently testable, reusable, and observable |
| Poll loop vs. fixed delay for instance ready | Poll loop (evaluation + revert to delay) | Handles variable startup time without over-waiting or hard-coding a sleep |
| Web server configuration mechanism | IAG Ansible service | Ansible is the natural fit for idempotent OS configuration; IAG provides execution infrastructure and SSH key management |
| HTTP validation as a separate phase | Dedicated child workflow | Validation is reusable for any web endpoint, not tied to nginx specifically |

---

## 5. Scope

**In scope:** Single instance deployment, security group creation with SSH + HTTP ingress, EC2 launch and polling, instance tagging, web server installation and configuration via Ansible, HTTP endpoint validation, error handling at every phase.

**Out of scope:** Auto-scaling groups or load balancers. HTTPS/TLS certificate provisioning. DNS record creation. Multi-instance or batch deployment. Teardown/cleanup lifecycle. ITSM ticket creation. Custom application deployment beyond a sample page.

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Security group already exists with same name | Phase 1 fails on duplicate | Add describeSecurityGroups check before create, reuse existing if found |
| Instance doesn't reach "running" state | Deployment hangs | Poll loop with configurable timeout; abort after max retries |
| SSH not ready when Ansible runs | Phase 2 fails on connection | Ansible playbook includes wait_for_connection with timeout |
| Port 80 blocked by network ACL or other firewall | Phase 3 fails validation | Document prerequisite: subnet/VPC must allow outbound HTTP |
| EC2 key pair doesn't match IAG host key file | Phase 2 cannot connect | Document key coordination prerequisite; consider key management automation |
| Instance left running after failed deployment | Ongoing AWS cost | Build companion teardown workflow (future enhancement) |

---

## 7. Requirements

### What the platform must be able to do

| Capability | Required | If Not Available |
|-----------|----------|------------------|
| Call AWS EC2 API (create SG, launch instance, describe, tag) | Yes | Cannot proceed |
| Execute Ansible playbooks via Automation Gateway | Yes | Cannot proceed |
| Orchestrate multi-phase workflows with child jobs | Yes | Cannot proceed |
| Poll external resource state with retry logic | Yes | Use fixed delay (less reliable) |
| Invoke HTTP validation service | Yes | Engineer validates manually |

### What external systems are involved

| System | Purpose | Required | If Not Available |
|--------|---------|----------|------------------|
| AWS EC2 API (via adapter) | Provision infrastructure | Yes | Cannot proceed |
| Itential Automation Gateway | Execute Ansible playbook for OS configuration | Yes | Cannot proceed |
| IAG Ansible service (aws-nginx-config) | Install and configure nginx | Yes | Must be deployed before running workflow |
| IAG Python service (url-validator) | HTTP endpoint validation | No | Engineer validates manually |
| ITSM / ticketing (e.g., ServiceNow) | Track deployment, audit trail | No | Engineer tracks manually |

### Discovery Questions

Ask the engineer before designing the solution:

1. What AWS region and VPC should the instance deploy into?
2. What AMI should be used? (Amazon Linux 2, Ubuntu, etc.)
3. What EC2 key pair name exists in the target region?
4. What subnet should the instance launch in? Does it have auto-assign public IP enabled?
5. Is the SSH private key already available on the IAG host? What path?
6. What instance type is needed? (t2.micro default, or larger?)
7. Should the web server be nginx, Apache, or another package?
8. Is there an existing web page/application to deploy, or use a sample Hello World?
9. Should the workflow create a ServiceNow ticket for the deployment?
10. Is there a teardown requirement — should the instance auto-terminate after a period?

---

## 8. Acceptance Criteria

1. Security group created with ports 22 and 80 open to specified CIDR
2. EC2 instance launched, reaches "running" state, and has a public IP
3. Instance tagged with Name and ManagedBy labels
4. Web server (nginx) installed and serving on port 80
5. Sample page accessible via HTTP at the instance's public IP
6. HTTP validation confirms 200 OK response
7. Workflow completes without entering error state
8. All phases visible as separate child jobs in the Itential job view
9. Any phase failure produces clean error capture (no stuck jobs)
10. Workflow is re-runnable with different parameters (new instance name, different AMI)

````
