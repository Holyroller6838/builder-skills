# Builder Skills Repository Transfer — Part 009 of 011

**Git commit:** `982d97c1573ca7ea892b39acced9b0d15955c4a9` on branch `main`  
**Generated:** 2026-08-31 21:28:30 UTC  
**See also:** `builder-skills-transfer-manifest.md` for the full repository manifest, directory tree, and complete checksum index across all parts.

This part contains **2** file(s):

- `helpers/assets/vendor-infoblox-nios-ddi.json`
- `helpers/assets/vendor-juniper-junos.json`

---

============================================================
FILE: helpers/assets/vendor-infoblox-nios-ddi.json
DIRECTORY: helpers/assets/
FILENAME: vendor-infoblox-nios-ddi.json
============================================================
SHA256: 71e8dfb5a4c5cee7de5e32c905f31753769dff286f13394ee4b39e92567450aa

````json
{
  "_id": "66cf708821161b4df271748b",
  "name": "Infoblox NIOS DDI",
  "description": "Infoblox NIOS DDI Project has assets for Create Network, Create Network Container, Create DNS A Record, Create CNS CNAME Record, Create DNS Fixed Address Record, Create DNS NS Record, Create DNS PRT Record",
  "components": [
    {
      "iid": 0,
      "reference": "9fa050c2-903e-4976-a9f3-8618c1166203",
      "type": "workflow",
      "folder": "/",
      "document": {
        "name": "Assign Next IP",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -2100,
              "y": -2232
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -2100,
              "y": -1968
            }
          },
          "6fa": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
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
              "x": -2460,
              "y": -2088
            }
          },
          "ee17": {
            "name": "assignNextIP2",
            "canvasName": "assignNextIP2",
            "summary": "assignNextIP2",
            "description": "assignNextIP2 will register the IP in the system",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "networkIP": "$var.job.networkIP",
                "hostName": "$var.job.hostName",
                "comment": "$var.job.comment",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.assignedNextIp"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2100,
              "y": -2100
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "ee17": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "6fa": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "ee17": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "6fa": {
              "type": "standard",
              "state": "error"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {},
          "3c0c": {},
          "2f5f": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "networkIP": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "hostName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comment": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["networkIP", "hostName", "comment", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "networkIP": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "hostName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comment": {
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
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "assignedNextIp": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.012Z",
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
      "reference": "6b93df36-f87d-424a-8278-bf62e9a86dbc",
      "type": "workflow",
      "folder": "/DNS PTR Record",
      "document": {
        "name": "Modify DNS PTR Record",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1524,
              "y": -2880
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -1488,
              "y": -1968
            }
          },
          "b1dc": {
            "name": "merge",
            "summary": "Build PTR Query Payload",
            "description": "Build PTR Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "currentIpAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "ptrdname",
                    "value": {
                      "task": "job",
                      "variable": "currentHostname",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1524,
              "y": -2760
            }
          },
          "26fb": {
            "name": "getObject",
            "summary": "Get PTR Record",
            "description": "Get PTR Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:ptr",
                "queryObject": "$var.b1dc.merged_object",
                "returnFields": "name,ipv4addr",
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
              "x": -1524,
              "y": -2652
            }
          },
          "3b": {
            "name": "query",
            "summary": "Query PTR Record _ref",
            "description": "Query PTR Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.26fb.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -1524,
              "y": -2520
            }
          },
          "77b8": {
            "name": "merge",
            "summary": "Build PTR Modify Payload",
            "description": "Build PTR Modify Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "newIpAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "ptrdname",
                    "value": {
                      "task": "job",
                      "variable": "newHostname",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1512,
              "y": -2280
            }
          },
          "46b8": {
            "name": "updateObject",
            "summary": "Update PTR Record",
            "description": "Update PTR Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.3b.return_data",
                "body": "$var.77b8.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedPTRRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -1500,
              "y": -2148
            }
          },
          "db34": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "PTR Record Not Found",
            "description": "PTR Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "PTR Record Not Found",
                "message": "",
                "body": "The PTR record for <!ipv4addr!>/<!ptrdname!> was not found in Infoblox.",
                "variables": "$var.b1dc.merged_object",
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
              "x": -936,
              "y": -2364
            }
          },
          "b2bb": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if PTR Record _ref Exists",
            "description": "Check if PTR record _ref exists",
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
                          "task": "3b",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -1524,
              "y": -2412
            }
          },
          "1d3c": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -1896,
              "y": -2136
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "b1dc": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "b1dc": {
            "26fb": {
              "type": "standard",
              "state": "success"
            }
          },
          "26fb": {
            "3b": {
              "type": "standard",
              "state": "success"
            }
          },
          "3b": {
            "b2bb": {
              "state": "success",
              "type": "standard"
            }
          },
          "77b8": {
            "46b8": {
              "type": "standard",
              "state": "success"
            }
          },
          "46b8": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "1d3c": {
              "type": "standard",
              "state": "error"
            }
          },
          "db34": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "b2bb": {
            "77b8": {
              "state": "success",
              "type": "standard"
            },
            "db34": {
              "type": "standard",
              "state": "failure"
            }
          },
          "1d3c": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {},
          "b825": {},
          "419b": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "currentIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "currentIpAddress",
            "currentHostname",
            "dnsView",
            "adapterId",
            "newIpAddress",
            "newHostname"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "currentIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "updatedPTRRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.016Z",
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
      "reference": "d370c28a-cbe2-4f70-be7d-e0ba6062611b",
      "type": "workflow",
      "folder": "/DNS NS Record",
      "document": {
        "name": "Modify DNS NS Record",
        "tasks": {
          "833": {
            "name": "getObject",
            "summary": "Get NS Record",
            "description": "Get NS Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:ns",
                "queryObject": "$var.35fa.merged_object",
                "returnFields": "name,nameserver",
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
              "x": 1008,
              "y": 4992
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 1008,
              "y": 4740
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 1008,
              "y": 5712
            }
          },
          "35fa": {
            "name": "merge",
            "summary": "Build NS Query Payload",
            "description": "Build NS Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "currentNsRecord",
                      "editable": true
                    }
                  },
                  {
                    "key": "nameserver",
                    "value": {
                      "task": "job",
                      "variable": "currentNameServer",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": 1008,
              "y": 4872
            }
          },
          "7ea9": {
            "name": "query",
            "summary": "Query NS Record _ref",
            "description": "Query NS Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.833.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": 1008,
              "y": 5124
            }
          },
          "fe74": {
            "name": "updateObject",
            "summary": "Update NS Record",
            "description": "Update NS Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.7ea9.return_data",
                "body": "$var.102a.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedNSRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 1008,
              "y": 5520
            }
          },
          "102a": {
            "name": "merge",
            "summary": "Build NS Update Payload",
            "description": "Build NS Update Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "nameserver",
                    "value": {
                      "task": "job",
                      "variable": "newNameServer",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": 1008,
              "y": 5388
            }
          },
          "cd86": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "NS Record Not Found",
            "description": "NS Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NS Record Not Found",
                "message": "",
                "body": "The NS record for <!name!>/<!nameserver!> was not found in Infoblox.",
                "variables": "$var.35fa.merged_object",
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
              "x": 1428,
              "y": 5256
            }
          },
          "a74f": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if NS Record _ref Exists",
            "description": "Check if NS record _ref exists",
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
                          "task": "7ea9",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": 1008,
              "y": 5256
            }
          },
          "0e55": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": 660,
              "y": 5532
            }
          }
        },
        "transitions": {
          "220": {},
          "346": {},
          "833": {
            "7ea9": {
              "type": "standard",
              "state": "success"
            }
          },
          "3973": {},
          "5806": {},
          "7588": {},
          "9200": {},
          "9296": {},
          "workflow_start": {
            "35fa": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "35fa": {
            "833": {
              "type": "standard",
              "state": "success"
            }
          },
          "7ea9": {
            "a74f": {
              "state": "success",
              "type": "standard"
            }
          },
          "fe74": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "0e55": {
              "type": "standard",
              "state": "error"
            }
          },
          "102a": {
            "fe74": {
              "type": "standard",
              "state": "success"
            }
          },
          "cd86": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "a74f": {
            "102a": {
              "state": "success",
              "type": "standard"
            },
            "cd86": {
              "type": "standard",
              "state": "failure"
            }
          },
          "0e55": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "b1dc": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "cde7": {},
          "a1d5": {},
          "26fb": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentNsRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentNameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newNameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "adapterId",
            "currentNsRecord",
            "currentNameServer",
            "dnsView",
            "newNameServer"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentNsRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentNameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newNameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "updatedNSRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.014Z",
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
      "iid": 3,
      "reference": "cd3160bc-323a-4992-96fc-e8ae646bdd49",
      "type": "workflow",
      "folder": "/DNS Fixed Address Record",
      "document": {
        "name": "Modify DNS Fixed Address Record",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -72,
              "y": 2700
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -72,
              "y": 3552
            }
          },
          "38b6": {
            "name": "merge",
            "summary": "Build Fixed Address Query Payload",
            "description": "Build Fixed Address Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "currentIpAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "mac",
                    "value": {
                      "task": "job",
                      "variable": "currentMacAddress",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -72,
              "y": 2820
            }
          },
          "a3c4": {
            "name": "getObject",
            "summary": "Get Fixed Address Record",
            "description": "Get Fixed Address Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "fixedaddress",
                "queryObject": "$var.38b6.merged_object",
                "returnFields": "ipv4addr,mac",
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
              "x": -72,
              "y": 2928
            }
          },
          "97a5": {
            "name": "query",
            "summary": "Query Fixed Address Record _ref",
            "description": "Query Fixed Address Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.a3c4.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -72,
              "y": 3048
            }
          },
          "ada6": {
            "name": "updateObject",
            "summary": "Update Fixed Address Record",
            "description": "Update Fixed Address Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.97a5.return_data",
                "body": "$var.631a.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedFixedAddress"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -72,
              "y": 3384
            }
          },
          "631a": {
            "name": "merge",
            "summary": "Build Fixed Address Modify Payload",
            "description": "Build Fixed Address Modify Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "newIpAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "mac",
                    "value": {
                      "task": "job",
                      "variable": "newMacAddress",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -72,
              "y": 3276
            }
          },
          "1c7f": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Fixed Address Record Not Found",
            "description": "Fixed Address Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Fixed Address Record Not Found",
                "message": "",
                "body": "The fixed address record for <!ipv4addr!>/<!mac!> was not found in Infoblox.",
                "variables": "$var.38b6.merged_object",
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
              "x": -504,
              "y": 3168
            }
          },
          "d778": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if Fixed Address Record _ref Exists",
            "description": "Check if fixed address record _ref exists",
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
                          "task": "97a5",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -72,
              "y": 3168
            }
          },
          "d20e": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": 288,
              "y": 3384
            }
          }
        },
        "transitions": {
          "220": {},
          "2088": {},
          "3962": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "38b6": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "38b6": {
            "a3c4": {
              "type": "standard",
              "state": "success"
            }
          },
          "a3c4": {
            "97a5": {
              "type": "standard",
              "state": "success"
            }
          },
          "97a5": {
            "d778": {
              "state": "success",
              "type": "standard"
            }
          },
          "ada6": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "d20e": {
              "type": "standard",
              "state": "error"
            }
          },
          "631a": {
            "ada6": {
              "type": "standard",
              "state": "success"
            }
          },
          "1c7f": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "d778": {
            "631a": {
              "state": "success",
              "type": "standard"
            },
            "1c7f": {
              "type": "standard",
              "state": "failure"
            }
          },
          "d20e": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "fc1d": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "cde7": {},
          "a63c": {},
          "acba": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "currentIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentMacAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newMacAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "currentIpAddress",
            "currentMacAddress",
            "adapterId",
            "newIpAddress",
            "newMacAddress"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "currentIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentMacAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newMacAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "updatedFixedAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.016Z",
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
      "iid": 4,
      "reference": "35b053a8-5587-494b-a501-c156510472a6",
      "type": "workflow",
      "folder": "/DNS CNAME Record",
      "document": {
        "name": "Modify DNS CNAME Record",
        "tasks": {
          "5806": {
            "name": "merge",
            "summary": "Build CNAME Query Payload",
            "description": "Build CNAME Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "currentAliasName",
                      "editable": true
                    }
                  },
                  {
                    "key": "canonical",
                    "value": {
                      "task": "job",
                      "variable": "currentCanonicalName",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1764,
              "y": -12
            }
          },
          "7275": {
            "name": "query",
            "summary": "Query CNAME Record _ref",
            "description": "Query CNAME Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.7ae7.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -1764,
              "y": 204
            }
          },
          "8520": {
            "name": "updateObject",
            "summary": "Update CNAME Record",
            "description": "Update CNAME Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.7275.return_data",
                "body": "$var.a102.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedCnameRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -1752,
              "y": 528
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1764,
              "y": -120
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -1752,
              "y": 684
            }
          },
          "7ae7": {
            "name": "getObject",
            "summary": "Get CNAME Record",
            "description": "Get CNAME Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:cname",
                "queryObject": "$var.5806.merged_object",
                "returnFields": "name,canonical",
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
              "x": -1764,
              "y": 84
            }
          },
          "a102": {
            "name": "merge",
            "summary": "Build CNAME Modify Payload",
            "description": "Build CNAME Modify Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "newAliasName",
                      "editable": true
                    }
                  },
                  {
                    "key": "canonical",
                    "value": {
                      "task": "job",
                      "variable": "newCanonicalName",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1752,
              "y": 420
            }
          },
          "a150": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "CNAME Record Not Found",
            "description": "CNAME Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "CNAME Record Not Found",
                "message": "",
                "body": "The CNAME record for <!name!>/<!canonical!> was not found in Infoblox.",
                "variables": "$var.5806.merged_object",
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
              "x": -2112,
              "y": 324
            }
          },
          "3dd2": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if CNAME Record _ref Exists",
            "description": "Check if CNAME record _ref exists",
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
                          "task": "7275",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -1764,
              "y": 312
            }
          },
          "d484": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -1428,
              "y": 540
            }
          }
        },
        "transitions": {
          "220": {},
          "3962": {},
          "3973": {},
          "5806": {
            "7ae7": {
              "type": "standard",
              "state": "success"
            }
          },
          "7275": {
            "3dd2": {
              "state": "success",
              "type": "standard"
            }
          },
          "7588": {},
          "7780": {},
          "8520": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "d484": {
              "type": "standard",
              "state": "error"
            }
          },
          "workflow_start": {
            "5806": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "7ae7": {
            "7275": {
              "type": "standard",
              "state": "success"
            }
          },
          "a102": {
            "8520": {
              "type": "standard",
              "state": "success"
            }
          },
          "a150": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "3dd2": {
            "a102": {
              "state": "success",
              "type": "standard"
            },
            "a150": {
              "type": "standard",
              "state": "failure"
            }
          },
          "d484": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "5da8": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "36e8": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "38b6": {},
          "426c": {},
          "cde7": {},
          "79ff": {},
          "b02e": {},
          "a1d5": {},
          "ad70": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "currentAliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentCanonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newAliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newCanonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "currentAliasName",
            "currentCanonicalName",
            "dnsView",
            "adapterId",
            "newAliasName",
            "newCanonicalName"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "currentAliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentCanonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newAliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "newCanonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "updatedCnameRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.016Z",
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
      "reference": "e4af82a1-e756-42ed-ae32-3432494a25fe",
      "type": "workflow",
      "folder": "/DNS A Record",
      "document": {
        "name": "Modify DNS A Record",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -60,
              "y": -4404
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -72,
              "y": -3420
            }
          },
          "36e8": {
            "name": "merge",
            "summary": "Build A Record Query Object",
            "description": "Build A Record Query Object",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "currentHostname",
                      "editable": true
                    }
                  },
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "currentIpAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -60,
              "y": -4260
            }
          },
          "5dfb": {
            "name": "getObject",
            "summary": "Get DNS A Record",
            "description": "Get DNS A Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:a",
                "queryObject": "$var.36e8.merged_object",
                "returnFields": "name,ipv4addr",
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
              "x": -60,
              "y": -4140
            }
          },
          "654b": {
            "name": "updateObject",
            "summary": "Update DNS A Record",
            "description": "Update DNS A Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.f77e.return_data",
                "body": "$var.138d.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.updatedARecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -60,
              "y": -3648
            }
          },
          "138d": {
            "name": "merge",
            "summary": "Build A Record Modify Payload",
            "description": "Build A Record Modify Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "updatedHostname",
                      "editable": true
                    }
                  },
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "updatedIpAddress",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -60,
              "y": -3768
            }
          },
          "4a41": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "DNS A Record Not Found",
            "description": "DNS A Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "DNS A Record Not Found",
                "message": "",
                "body": "The DNS A record for <!ipv4addr!>/<!name!> was not found in Infoblox.",
                "variables": "$var.36e8.merged_object",
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
              "x": -384,
              "y": -3900
            }
          },
          "f77e": {
            "name": "query",
            "canvasName": "query",
            "summary": "Query A Record _ref",
            "description": "Query A Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.5dfb.result"
              },
              "outgoing": {
                "return_data": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -60,
              "y": -4020
            }
          },
          "e17c": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if A Record _ref Exists",
            "description": "Check if A record _ref exists",
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
                          "task": "f77e",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -60,
              "y": -3900
            }
          },
          "c315": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": 252,
              "y": -3660
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "36e8": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "36e8": {
            "5dfb": {
              "type": "standard",
              "state": "success"
            }
          },
          "5dfb": {
            "f77e": {
              "state": "success",
              "type": "standard"
            }
          },
          "654b": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "c315": {
              "type": "standard",
              "state": "error"
            }
          },
          "138d": {
            "654b": {
              "type": "standard",
              "state": "success"
            }
          },
          "4a41": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "f77e": {
            "e17c": {
              "state": "success",
              "type": "standard"
            }
          },
          "e17c": {
            "4a41": {
              "type": "standard",
              "state": "failure"
            },
            "138d": {
              "state": "success",
              "type": "standard"
            }
          },
          "c315": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "be54": {},
          "73f4": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "cde7": {},
          "39a4": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "currentHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "currentHostname",
            "currentIpAddress",
            "dnsView",
            "adapterId",
            "updatedHostname",
            "updatedIpAddress"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "currentHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "currentIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedHostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "updatedIpAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "updatedARecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "4.5.3-2019.2.7.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.014Z",
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
      "iid": 6,
      "reference": "b2308a09-e7ab-4782-a471-0fc3a1c4ed56",
      "type": "workflow",
      "folder": "/Network Container",
      "document": {
        "name": "Delete Network Container",
        "tasks": {
          "1261": {
            "name": "getNetworkContainerDetails",
            "canvasName": "getNetworkContainerDetails",
            "summary": "getNetworkContainerDetails",
            "description": "getNetworkContainerDetails will get the container details",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "networkIP": "$var.job.networkIP",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": null
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -3012,
              "y": -2196
            }
          },
          "3441": {
            "name": "substring",
            "canvasName": "substring",
            "summary": "Get Valid Network Container ref",
            "description": "Get Network Container ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "automatic",
            "displayName": "String",
            "variables": {
              "incoming": {
                "str": "$var.b02e.return_data",
                "indexStart": 17,
                "indexEnd": ""
              },
              "outgoing": {
                "substring": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -3012,
              "y": -1836
            }
          },
          "4081": {
            "name": "deleteNetworkContainer",
            "canvasName": "deleteNetworkContainer",
            "summary": "Delete Network Container",
            "description": "",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "networkRef": "$var.3441.substring",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletedNetworkContainer"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -3012,
              "y": -1692
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -3012,
              "y": -2364
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -3012,
              "y": -1452
            }
          },
          "b02e": {
            "name": "query",
            "summary": "Query Network Container _ref",
            "description": "Query Network Container _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.1261.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -3012,
              "y": -2076
            }
          },
          "a21b": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Network Container Not Found",
            "description": "",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Network Container Not Found",
                "message": "",
                "body": "Network container was not found in Infoblox.",
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
              "x": -3468,
              "y": -1968
            }
          },
          "4ffb": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
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
              "x": -2580,
              "y": -2196
            }
          },
          "6d60": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if Network Container _ref Exists",
            "description": "Check if network container _ref exists",
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
                          "task": "b02e",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -3012,
              "y": -1956
            }
          }
        },
        "transitions": {
          "220": {},
          "1261": {
            "b02e": {
              "type": "standard",
              "state": "success"
            },
            "4ffb": {
              "state": "error",
              "type": "standard"
            }
          },
          "1599": {},
          "3441": {
            "4081": {
              "state": "success",
              "type": "standard"
            }
          },
          "3973": {},
          "4081": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "4ffb": {
              "type": "standard",
              "state": "error"
            }
          },
          "7588": {},
          "7780": {},
          "workflow_start": {
            "1261": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "b02e": {
            "6d60": {
              "state": "success",
              "type": "standard"
            }
          },
          "a21b": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "4ffb": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "6d60": {
            "3441": {
              "state": "success",
              "type": "standard"
            },
            "a21b": {
              "type": "standard",
              "state": "failure"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {},
          "170f": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "networkIP": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["networkIP", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "networkIP": {
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
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "deletedNetworkContainer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.28.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.015Z",
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
      "reference": "d33684b6-9bcc-4298-9816-0a5ad08e7ce7",
      "type": "workflow",
      "folder": "/Network",
      "document": {
        "name": "Delete Network",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -3132,
              "y": -2244
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -3144,
              "y": -1956
            }
          },
          "6fa": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
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
              "x": -3480,
              "y": -2088
            }
          },
          "694a": {
            "name": "deleteNetworkv2",
            "canvasName": "deleteNetworkv2",
            "summary": "Delete Network",
            "description": "",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "networkIP": "$var.job.networkIP",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletedNetwork"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -3144,
              "y": -2100
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "694a": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "6fa": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "694a": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "6fa": {
              "type": "standard",
              "state": "error"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {},
          "3c0c": {},
          "efca": {},
          "dbad": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "networkIP": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["networkIP", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "networkIP": {
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
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "deletedNetwork": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.28.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.017Z",
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
      "reference": "6f0bc552-bb38-4e1e-bd3c-191835b1df4d",
      "type": "workflow",
      "folder": "/DNS PTR Record",
      "document": {
        "name": "Delete DNS PTR Record",
        "tasks": {
          "1485": {
            "name": "getObject",
            "summary": "Get PTR Record",
            "description": "Get PTR Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:ptr",
                "queryObject": "$var.b1dc.merged_object",
                "returnFields": "name,ptrdname,ipv4addr",
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
              "x": -1776,
              "y": -2472
            }
          },
          "3057": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if PTR Record _ref Exists",
            "description": "Check if PTR Record _ref exists",
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
                          "task": "b02e",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -1776,
              "y": -2232
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1776,
              "y": -2712
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -1788,
              "y": -1932
            }
          },
          "b1dc": {
            "name": "merge",
            "summary": "Build PTR Query Payload",
            "description": "Build PTR Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ptrdname",
                    "value": {
                      "task": "job",
                      "variable": "hostname",
                      "editable": true
                    }
                  },
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "ipAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1776,
              "y": -2592
            }
          },
          "b02e": {
            "name": "query",
            "summary": "Query PTR Record _ref",
            "description": "Query PTR Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.1485.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -1776,
              "y": -2364
            }
          },
          "f3c": {
            "name": "deleteObject",
            "summary": "Delete PTR Record",
            "description": "Delete PTR Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.b02e.return_data",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletedPTRRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -1776,
              "y": -2112
            }
          },
          "348f": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "PTR Record Not Found",
            "description": "PTR Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "PTR Record Not Found",
                "message": "",
                "body": "The PTR record for <!ipv4addr!>/<!ptrdname!> was not found in Infoblox.",
                "variables": "$var.b1dc.merged_object",
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
              "x": -2136,
              "y": -2232
            }
          },
          "18b0": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -1464,
              "y": -2112
            }
          }
        },
        "transitions": {
          "220": {},
          "1485": {
            "b02e": {
              "type": "standard",
              "state": "success"
            }
          },
          "1599": {},
          "3057": {
            "f3c": {
              "state": "success",
              "type": "standard"
            },
            "348f": {
              "type": "standard",
              "state": "failure"
            }
          },
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "b1dc": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "b1dc": {
            "1485": {
              "type": "standard",
              "state": "success"
            }
          },
          "b02e": {
            "3057": {
              "state": "success",
              "type": "standard"
            }
          },
          "f3c": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "18b0": {
              "type": "standard",
              "state": "error"
            }
          },
          "348f": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "18b0": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["adapterId", "hostname", "ipAddress", "dnsView"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "deletedPTRRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.018Z",
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
      "reference": "ae0a78db-b35b-486f-b089-778cac55cc23",
      "type": "workflow",
      "folder": "/DNS NS Record",
      "document": {
        "name": "Delete DNS NS Record",
        "tasks": {
          "8073": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -1860,
              "y": 4692
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1488,
              "y": 4044
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -1488,
              "y": 4884
            }
          },
          "ac8b": {
            "name": "getObject",
            "summary": "Get NS Record",
            "description": "Get NS Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:ns",
                "queryObject": "$var.6b90.merged_object",
                "returnFields": "name,nameserver",
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
              "x": -1488,
              "y": 4284
            }
          },
          "fcb1": {
            "name": "query",
            "summary": "Query NS Record _ref",
            "description": "Query NS Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.ac8b.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -1488,
              "y": 4404
            }
          },
          "16fe": {
            "name": "deleteObject",
            "summary": "Delete NS Record",
            "description": "Delete NS Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.fcb1.return_data",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletedNSRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -1488,
              "y": 4692
            }
          },
          "6b90": {
            "name": "merge",
            "summary": "Build NS Query Payload",
            "description": "Build NS Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "nsRecord",
                      "editable": true
                    }
                  },
                  {
                    "key": "nameserver",
                    "value": {
                      "task": "job",
                      "variable": "nameServer",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1488,
              "y": 4164
            }
          },
          "892a": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "NS Record Not Found",
            "description": "NS Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "NS Record Not Found",
                "message": "",
                "body": "The NS record for <!name!>/<!nameserver!> was not found in Infoblox.",
                "variables": "$var.6b90.merged_object",
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
              "x": -1056,
              "y": 4548
            }
          },
          "c7bb": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if NS Record _ref Exists",
            "description": "Check if NS record _ref exists",
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
                          "task": "fcb1",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -1488,
              "y": 4536
            }
          }
        },
        "transitions": {
          "220": {},
          "346": {},
          "3973": {},
          "5806": {},
          "7588": {},
          "8073": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "9200": {},
          "9296": {},
          "workflow_start": {
            "6b90": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "ac8b": {
            "fcb1": {
              "type": "standard",
              "state": "success"
            }
          },
          "fcb1": {
            "c7bb": {
              "state": "success",
              "type": "standard"
            }
          },
          "16fe": {
            "8073": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "6b90": {
            "ac8b": {
              "type": "standard",
              "state": "success"
            }
          },
          "892a": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "c7bb": {
            "16fe": {
              "state": "success",
              "type": "standard"
            },
            "892a": {
              "type": "standard",
              "state": "failure"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "b1dc": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "cde7": {},
          "a1d5": {},
          "26fb": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nsRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["adapterId", "nsRecord", "nameServer", "dnsView"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nsRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "deletedNSRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.018Z",
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
      "iid": 10,
      "reference": "42b54555-d889-48a5-9436-dafc777a646d",
      "type": "workflow",
      "folder": "/DNS Fixed Address Record",
      "document": {
        "name": "Delete DNS Fixed Address Record",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1896,
              "y": 2004
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -1908,
              "y": 2808
            }
          },
          "38b6": {
            "name": "merge",
            "summary": "Build Fixed Address Query Payload",
            "description": "Build Fixed Address Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "ipAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "mac",
                    "value": {
                      "task": "job",
                      "variable": "macAddress",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1896,
              "y": 2124
            }
          },
          "71a7": {
            "name": "getObject",
            "summary": "Get Fixed Address Record",
            "description": "Get Fixed Address Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "fixedaddress",
                "queryObject": "$var.38b6.merged_object",
                "returnFields": "ipv4addr,mac",
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
              "x": -1896,
              "y": 2244
            }
          },
          "ac62": {
            "name": "query",
            "summary": "Query Fixed Address Record _ref",
            "description": "Query Fixed Address Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.71a7.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -1896,
              "y": 2364
            }
          },
          "444a": {
            "name": "deleteObject",
            "summary": "Delete Fixed Address Record",
            "description": "Delete Fixed Address Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.ac62.return_data",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletedFixedAddress"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -1896,
              "y": 2628
            }
          },
          "f425": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Fixed Address Record Not Found",
            "description": "Fixed Address Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Fixed Address Record Not Found",
                "message": "",
                "body": "The fixed address record for <!ipv4addr!>/<!mac!> was not found in Infoblox.",
                "variables": "$var.38b6.merged_object",
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
              "x": -2268,
              "y": 2484
            }
          },
          "e187": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if Fixed Address Record _ref Exists",
            "description": "Check if fixed address record _ref exists",
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
                          "task": "ac62",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -1896,
              "y": 2484
            }
          },
          "eb4b": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -1512,
              "y": 2616
            }
          }
        },
        "transitions": {
          "220": {},
          "2088": {},
          "3962": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "38b6": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "38b6": {
            "71a7": {
              "type": "standard",
              "state": "success"
            }
          },
          "71a7": {
            "ac62": {
              "type": "standard",
              "state": "success"
            }
          },
          "ac62": {
            "e187": {
              "state": "success",
              "type": "standard"
            }
          },
          "444a": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "eb4b": {
              "type": "standard",
              "state": "error"
            }
          },
          "f425": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "e187": {
            "444a": {
              "state": "success",
              "type": "standard"
            },
            "f425": {
              "type": "standard",
              "state": "failure"
            }
          },
          "eb4b": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "fc1d": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "cde7": {},
          "a63c": {},
          "acba": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "macAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["ipAddress", "macAddress", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "macAddress": {
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
            "deletedFixedAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.019Z",
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
      "iid": 11,
      "reference": "861e3dfa-c674-40a5-8fbb-e8f1869e1a06",
      "type": "workflow",
      "folder": "/DNS CNAME Record",
      "document": {
        "name": "Delete DNS CNAME Record",
        "tasks": {
          "5806": {
            "name": "merge",
            "summary": "Build CNAME Query Payload",
            "description": "Build CNAME Query Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "aliasName",
                      "editable": true
                    }
                  },
                  {
                    "key": "canonical",
                    "value": {
                      "task": "job",
                      "variable": "canonicalName",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1908,
              "y": 108
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1908,
              "y": -12
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -1920,
              "y": 768
            }
          },
          "2cb3": {
            "name": "getObject",
            "summary": "Get CNAME Record",
            "description": "Get CNAME Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:cname",
                "queryObject": "$var.5806.merged_object",
                "returnFields": "name,canonical",
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
              "x": -1908,
              "y": 216
            }
          },
          "eab9": {
            "name": "query",
            "summary": "Query CNAME Record _ref",
            "description": "Query CNAME Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.2cb3.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -1908,
              "y": 336
            }
          },
          "12a1": {
            "name": "deleteObject",
            "summary": "Delete CNAME Record",
            "description": "Delete CNAME Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.eab9.return_data",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletedCnameRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -1908,
              "y": 576
            }
          },
          "a20f": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "CNAME Record Not Found",
            "description": "CNAME Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "CNAME Record Not Found",
                "message": "",
                "body": "The CNAME record for <!name!>/<!canonical!> was not found in Infoblox.",
                "variables": "$var.5806.merged_object",
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
              "x": -2232,
              "y": 468
            }
          },
          "2e2d": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if CNAME Record _ref Exists",
            "description": "Check if CNAME record _ref exists",
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
                          "task": "eab9",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -1908,
              "y": 456
            }
          },
          "b179": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -1596,
              "y": 576
            }
          }
        },
        "transitions": {
          "220": {},
          "3962": {},
          "3973": {},
          "5806": {
            "2cb3": {
              "type": "standard",
              "state": "success"
            }
          },
          "7588": {},
          "7780": {},
          "workflow_start": {
            "5806": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "2cb3": {
            "eab9": {
              "type": "standard",
              "state": "success"
            }
          },
          "eab9": {
            "2e2d": {
              "state": "success",
              "type": "standard"
            }
          },
          "12a1": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "b179": {
              "type": "standard",
              "state": "error"
            }
          },
          "a20f": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "2e2d": {
            "12a1": {
              "state": "success",
              "type": "standard"
            },
            "a20f": {
              "type": "standard",
              "state": "failure"
            }
          },
          "b179": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "5da8": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "36e8": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "38b6": {},
          "426c": {},
          "cde7": {},
          "79ff": {},
          "b02e": {},
          "a1d5": {},
          "ad70": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "aliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "canonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["aliasName", "canonicalName", "dnsView", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "aliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "canonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
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
            "deletedCnameRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.020Z",
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
      "iid": 12,
      "reference": "e2c06a2e-db81-4124-a410-cb8aae9eda08",
      "type": "workflow",
      "folder": "/DNS A Record",
      "document": {
        "name": "Delete DNS A Record",
        "tasks": {
          "5227": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build A Record Query Object",
            "description": "Build A Record Query Object",
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
                      "variable": "hostname",
                      "editable": true
                    }
                  },
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "ipAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView",
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
              "x": -2364,
              "y": -5028
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -2364,
              "y": -5148
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -2364,
              "y": -4308
            }
          },
          "c287": {
            "name": "getObject",
            "summary": "Get DNS A Record",
            "description": "Get DNS A Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectType": "record:a",
                "queryObject": "$var.5227.merged_object",
                "returnFields": "name,ipv4addr",
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
              "x": -2364,
              "y": -4896
            }
          },
          "5a0f": {
            "name": "query",
            "summary": "Query A Record _ref",
            "description": "Query A Record _ref",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "pass_on_null": false,
                "query": "response.result[0]._ref",
                "obj": "$var.c287.result"
              },
              "outgoing": {
                "return_data": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "scheduled": false,
            "canvasName": "query",
            "nodeLocation": {
              "x": -2364,
              "y": -4764
            }
          },
          "4f72": {
            "name": "deleteObject",
            "summary": "Delete DNS A Record",
            "description": "Delete DNS A Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "objectReference": "$var.5a0f.return_data",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.deletedARecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2364,
              "y": -4500
            }
          },
          "8a0": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "DNS A Record Not Found",
            "description": "DNS A Record Not Found",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "DNS A Record Not Found",
                "message": "",
                "body": "The DNS A record for <!ipv4addr!>/<!name!> was not found in Infoblox.",
                "variables": "$var.5227.merged_object",
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
              "x": -2724,
              "y": -4632
            }
          },
          "c614": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Check if A Record _ref Exists",
            "description": "Check if A record _ref exists",
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
                          "task": "5a0f",
                          "variable": "return_data"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": null
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
              "x": -2364,
              "y": -4632
            }
          },
          "16b7": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -2004,
              "y": -4512
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "5227": {
            "c287": {
              "type": "standard",
              "state": "success"
            }
          },
          "7588": {},
          "7780": {},
          "workflow_start": {
            "5227": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "c287": {
            "5a0f": {
              "type": "standard",
              "state": "success"
            }
          },
          "5a0f": {
            "c614": {
              "state": "success",
              "type": "standard"
            }
          },
          "4f72": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "16b7": {
              "type": "standard",
              "state": "error"
            }
          },
          "8a0": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "c614": {
            "4f72": {
              "state": "success",
              "type": "standard"
            },
            "8a0": {
              "type": "standard",
              "state": "failure"
            }
          },
          "16b7": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "73f4": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "cde7": {},
          "36b9": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["hostname", "ipAddress", "dnsView", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
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
            "deletedARecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.020Z",
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
      "iid": 13,
      "reference": "eca02aca-d44a-428b-a52d-05a3366dab75",
      "type": "workflow",
      "folder": "/Network Container",
      "document": {
        "name": "Create Network Container",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -3900,
              "y": -2220
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -3900,
              "y": -1884
            }
          },
          "6fa": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
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
              "x": -4212,
              "y": -1992
            }
          },
          "f30c": {
            "name": "createNetworkContainer",
            "canvasName": "createNetworkContainer",
            "summary": "createNetworkContainer",
            "description": "createNetworkContainer will create a new network container",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "payload": "$var.976e.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdNetworkContainer"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -3900,
              "y": -1992
            }
          },
          "976e": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Build Input to Create Network Container",
            "description": "Builds input to create network container",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "network",
                    "value": {
                      "task": "job",
                      "variable": "network",
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
              "x": -3900,
              "y": -2100
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "976e": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "6fa": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "f30c": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "6fa": {
              "type": "standard",
              "state": "error"
            }
          },
          "976e": {
            "f30c": {
              "type": "standard",
              "state": "success"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {},
          "3c0c": {},
          "99e5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "network": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["adapterId", "network"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "network": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "createdNetworkContainer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.28.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.021Z",
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
      "iid": 14,
      "reference": "af5f455d-0a4a-4420-bd66-cfb0ce755c7f",
      "type": "workflow",
      "folder": "/Network",
      "document": {
        "name": "Create Network",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -2256,
              "y": -2268
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -2244,
              "y": -1956
            }
          },
          "6fa": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
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
              "x": -2580,
              "y": -2100
            }
          },
          "710e": {
            "name": "createNetwork",
            "canvasName": "createNetwork",
            "summary": "createNetwork",
            "description": "createNetwork will create a network",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "network": "$var.job.network",
                "comment": "$var.job.comment",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdNetwork"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2244,
              "y": -2112
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "710e": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "6fa": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "710e": {
            "6fa": {
              "type": "standard",
              "state": "error"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {},
          "3c0c": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "network": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comment": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["network", "comment", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "network": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "comment": {
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
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "createdNetwork": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.28.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.021Z",
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
      "iid": 15,
      "reference": "55e92522-b9b6-40a7-bf78-cfb6f2a7e641",
      "type": "workflow",
      "folder": "/DNS PTR Record",
      "document": {
        "name": "Create DNS PTR Record",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -2424,
              "y": -2700
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -2424,
              "y": -2196
            }
          },
          "8a5a": {
            "name": "createPtrRecord",
            "summary": "Create PTR Record",
            "description": "Creates a PTR record, e.g. for 'server1' in the zone 'info.com'",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "body": "$var.b1dc.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.ptrRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2772,
              "y": -2328
            }
          },
          "b1dc": {
            "name": "merge",
            "summary": "Build PTR Payload",
            "description": "Build PTR Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ptrdname",
                    "value": {
                      "task": "job",
                      "variable": "hostname",
                      "editable": true
                    }
                  },
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "ipAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -2424,
              "y": -2580
            }
          },
          "f8a1": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "PTR Record Already Exists?",
            "description": "PTR Record Already Exists?",
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
                        "query": "response.result",
                        "operand_1": {
                          "variable": "result",
                          "task": "b519"
                        },
                        "operator": ">",
                        "operand_2": {
                          "variable": 0,
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
              "x": -2424,
              "y": -2328
            }
          },
          "b519": {
            "name": "getObject",
            "canvasName": "getObject",
            "summary": "Get PTR Record",
            "description": "Get PTR Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "objectType": "record:ptr",
                "queryObject": "$var.b1dc.merged_object",
                "returnFields": "name,ptrdname,ipv4addr",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.ptrRecord"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2424,
              "y": -2460
            }
          },
          "d276": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -2772,
              "y": -2196
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "b1dc": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "8a5a": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "d276": {
              "type": "standard",
              "state": "error"
            }
          },
          "b1dc": {
            "b519": {
              "type": "standard",
              "state": "success"
            }
          },
          "f8a1": {
            "8a5a": {
              "type": "standard",
              "state": "failure"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "b519": {
            "f8a1": {
              "type": "standard",
              "state": "success"
            }
          },
          "d276": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "426c": {},
          "cde7": {},
          "acba": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["adapterId", "hostname", "ipAddress", "dnsView"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "ptrRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.022Z",
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
      "iid": 16,
      "reference": "6b441c40-4e82-4393-8ead-fc4d13d4bf60",
      "type": "workflow",
      "folder": "/DNS NS Record",
      "document": {
        "name": "Create DNS NS Record",
        "tasks": {
          "1405": {
            "name": "getObject",
            "canvasName": "getObject",
            "summary": "Get NS Record",
            "description": "Get NS Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "objectType": "record:ns",
                "queryObject": "$var.01c2.merged_object",
                "returnFields": "name,nameserver",
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
              "x": -1152,
              "y": 4692
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -1152,
              "y": 4308
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -1152,
              "y": 4980
            }
          },
          "35fa": {
            "name": "merge",
            "summary": "Build NS Record Payload",
            "description": "Build NS Record Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "nsRecord",
                      "editable": true
                    }
                  },
                  {
                    "key": "nameserver",
                    "value": {
                      "task": "job",
                      "variable": "nameServer",
                      "editable": true
                    }
                  },
                  {
                    "key": "addresses",
                    "value": {
                      "task": "job",
                      "variable": "addresses",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1152,
              "y": 4440
            }
          },
          "c0e5": {
            "name": "createNsRecord",
            "summary": "Create NS Record",
            "description": "Creates a NS record, e.g. for the zone 'info.com'",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "body": "$var.35fa.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdNSRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -1512,
              "y": 4824
            }
          },
          "def1": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "NS Record Already Exists?",
            "description": "NS Record Already Exists?",
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
                        "query": "response.result",
                        "operand_1": {
                          "variable": "result",
                          "task": "1405"
                        },
                        "operator": ">",
                        "operand_2": {
                          "variable": 0,
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
              "x": -1152,
              "y": 4812
            }
          },
          "21d2": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -1512,
              "y": 4968
            }
          },
          "01c2": {
            "name": "merge",
            "summary": "Build Get NS Record Query",
            "description": "Build Get NS Record Query",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "nsRecord",
                      "editable": true
                    }
                  },
                  {
                    "key": "nameserver",
                    "value": {
                      "task": "job",
                      "variable": "nameServer",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -1152,
              "y": 4572
            }
          }
        },
        "transitions": {
          "220": {},
          "346": {},
          "1405": {
            "def1": {
              "type": "standard",
              "state": "success"
            }
          },
          "3973": {},
          "5806": {},
          "7588": {},
          "9200": {},
          "9296": {},
          "workflow_start": {
            "35fa": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "35fa": {
            "01c2": {
              "state": "success",
              "type": "standard"
            }
          },
          "c0e5": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "21d2": {
              "type": "standard",
              "state": "error"
            }
          },
          "def1": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "c0e5": {
              "type": "standard",
              "state": "failure"
            }
          },
          "21d2": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "01c2": {
            "1405": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "b1dc": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "cde7": {},
          "a1d5": {},
          "26fb": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nsRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "addresses": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": [
            "adapterId",
            "nsRecord",
            "nameServer",
            "addresses",
            "dnsView"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nsRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "nameServer": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "addresses": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "createdNSRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.022Z",
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
      "iid": 17,
      "reference": "100132cf-a7b9-454f-b1d8-88803fa5201a",
      "type": "workflow",
      "folder": "/DNS Fixed Address Record",
      "document": {
        "name": "Create DNS Fixed Address Record",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -2640,
              "y": 2100
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -2640,
              "y": 2568
            }
          },
          "b4b3": {
            "name": "createFixedAddress",
            "summary": "Create Fixed Address",
            "description": "Creates a fixed address",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "body": "$var.38b6.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.fixedAddressRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2988,
              "y": 2436
            }
          },
          "38b6": {
            "name": "merge",
            "summary": "Build Fixed Address Payload",
            "description": "Build Fixed Address Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "ipAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "mac",
                    "value": {
                      "task": "job",
                      "variable": "macAddress",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -2640,
              "y": 2208
            }
          },
          "8b87": {
            "name": "getObject",
            "canvasName": "getObject",
            "summary": "Get Fixed Address Record",
            "description": "Get Fixed Address Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "objectType": "fixedaddress",
                "queryObject": "$var.38b6.merged_object",
                "returnFields": "ipv4addr,mac",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.fixedAddressRecord"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2640,
              "y": 2316
            }
          },
          "38ba": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Fixed Address Already Exists?",
            "description": "Fixed Address Already Exists?",
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
                        "query": "response.result",
                        "operand_1": {
                          "variable": "result",
                          "task": "8b87"
                        },
                        "operator": ">",
                        "operand_2": {
                          "variable": 0,
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
              "x": -2640,
              "y": 2424
            }
          },
          "9b11": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -2976,
              "y": 2580
            }
          }
        },
        "transitions": {
          "220": {},
          "2088": {},
          "3962": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "38b6": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "b4b3": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "9b11": {
              "type": "standard",
              "state": "error"
            }
          },
          "38b6": {
            "8b87": {
              "type": "standard",
              "state": "success"
            }
          },
          "8b87": {
            "38ba": {
              "type": "standard",
              "state": "success"
            }
          },
          "38ba": {
            "b4b3": {
              "type": "standard",
              "state": "failure"
            },
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "9b11": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "fc1d": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "3e61": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "cde7": {},
          "a63c": {},
          "acba": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "macAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["adapterId", "ipAddress", "macAddress"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "macAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "fixedAddressRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.024Z",
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
      "iid": 18,
      "reference": "8043f69c-3f21-42e2-a24d-ad3b18ea51e7",
      "type": "workflow",
      "folder": "/DNS CNAME Record",
      "document": {
        "name": "Create DNS CNAME Record",
        "tasks": {
          "1018": {
            "name": "getObject",
            "canvasName": "getObject",
            "summary": "Get CNAME Record",
            "description": "Get CNAME Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "objectType": "record:cname",
                "queryObject": "$var.5806.merged_object",
                "returnFields": "name,canonical",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.cnameRecord"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2328,
              "y": 336
            }
          },
          "5806": {
            "name": "merge",
            "summary": "Build CNAME Payload",
            "description": "Build CNAME Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "aliasName",
                      "editable": true
                    }
                  },
                  {
                    "key": "canonical",
                    "value": {
                      "task": "job",
                      "variable": "canonicalName",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView"
                    }
                  }
                ]
              },
              "outgoing": {
                "merged_object": null
              }
            },
            "groups": [],
            "canvasName": "merge",
            "nodeLocation": {
              "x": -2328,
              "y": 216
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -2328,
              "y": 84
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -2328,
              "y": 612
            }
          },
          "e19f": {
            "name": "createCNAMERecord",
            "summary": "Create CNAME Record",
            "description": "Creates a cname record, e.g. 'cnametest.demo' in the zone 'info.com' with a canonical name 'demo'",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "body": "$var.5806.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.cnameRecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "job",
            "scheduled": false,
            "nodeLocation": {
              "x": -2676,
              "y": 456
            }
          },
          "44e4": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "CNAME Already Exists?",
            "description": "CNAME Already Exists?",
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
                        "query": "response.result",
                        "operand_1": {
                          "variable": "result",
                          "task": "1018"
                        },
                        "operator": ">",
                        "operand_2": {
                          "variable": 0,
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
              "x": -2328,
              "y": 444
            }
          },
          "63da": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "View Infoblox Error",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -2676,
              "y": 624
            }
          }
        },
        "transitions": {
          "220": {},
          "1018": {
            "44e4": {
              "type": "standard",
              "state": "success"
            }
          },
          "3962": {},
          "3973": {},
          "5806": {
            "1018": {
              "type": "standard",
              "state": "success"
            }
          },
          "7588": {},
          "7780": {},
          "workflow_start": {
            "5806": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "e19f": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "63da": {
              "type": "standard",
              "state": "error"
            }
          },
          "44e4": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "e19f": {
              "type": "standard",
              "state": "failure"
            }
          },
          "63da": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "5da8": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "36e8": {},
          "be54": {},
          "57a1": {},
          "762c": {},
          "38b6": {},
          "426c": {},
          "cde7": {},
          "79ff": {},
          "b02e": {},
          "a1d5": {},
          "ad70": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "aliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "canonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["adapterId", "aliasName", "canonicalName", "dnsView"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "aliasName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "canonicalName": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "cnameRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.025Z",
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
      "iid": 19,
      "reference": "0ce6819c-e755-4be8-9943-ab8c23007daf",
      "type": "workflow",
      "folder": "/DNS A Record",
      "document": {
        "name": "Create DNS A Record",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": -3000,
              "y": -4548
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": -3000,
              "y": -3972
            }
          },
          "36e8": {
            "name": "merge",
            "summary": "Build A Record Payload",
            "description": "Build A Record Payload",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "operation",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "name",
                    "value": {
                      "task": "job",
                      "variable": "hostname",
                      "editable": true
                    }
                  },
                  {
                    "key": "ipv4addr",
                    "value": {
                      "task": "job",
                      "variable": "ipAddress",
                      "editable": true
                    }
                  },
                  {
                    "key": "view",
                    "value": {
                      "task": "job",
                      "variable": "dnsView",
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
            "canvasName": "merge",
            "nodeLocation": {
              "x": -3000,
              "y": -4400
            }
          },
          "b4ad": {
            "name": "createARecord",
            "summary": "Create DNS A Record",
            "description": "Create DNS A Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "displayName": "Infoblox",
            "type": "automatic",
            "variables": {
              "incoming": {
                "body": "$var.36e8.merged_object",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.createdARecord"
              },
              "error": "$var.job.infobloxError",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -2688,
              "y": -4152
            }
          },
          "cc69": {
            "name": "getObject",
            "canvasName": "getObject",
            "summary": "Get DNS A Record",
            "description": "Get DNS A Record",
            "location": "Adapter",
            "locationType": "Infoblox",
            "app": "Infoblox",
            "type": "automatic",
            "displayName": "Infoblox",
            "variables": {
              "incoming": {
                "objectType": "record:a",
                "queryObject": "$var.36e8.merged_object",
                "returnFields": "name,ipv4addr",
                "adapter_id": "$var.job.adapterId"
              },
              "outgoing": {
                "result": "$var.job.aRecord"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -3000,
              "y": -4284
            }
          },
          "6d9d": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "DNS A Record Already Exists?",
            "description": "DNS A Record Already Exists?",
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
                        "query": "response.result",
                        "operand_1": {
                          "variable": "result",
                          "task": "cc69"
                        },
                        "operator": ">",
                        "operand_2": {
                          "variable": 0,
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
              "x": -3000,
              "y": -4152
            }
          },
          "00ca": {
            "name": "ViewData",
            "canvasName": "ViewData",
            "summary": "Infoblox Error",
            "description": "",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "WorkFlowEngine",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "Infoblox Error",
                "message": "",
                "body": "$var.job.infobloxError",
                "variables": "",
                "btn_success": "Continue",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewData",
            "groups": [],
            "nodeLocation": {
              "x": -2688,
              "y": -3996
            }
          }
        },
        "transitions": {
          "220": {},
          "1599": {},
          "3973": {},
          "7588": {},
          "7780": {},
          "workflow_start": {
            "36e8": {
              "type": "standard",
              "state": "success"
            }
          },
          "workflow_end": {},
          "36e8": {
            "cc69": {
              "type": "standard",
              "state": "success"
            }
          },
          "b4ad": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "00ca": {
              "type": "standard",
              "state": "error"
            }
          },
          "cc69": {
            "6d9d": {
              "type": "standard",
              "state": "success"
            }
          },
          "6d9d": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            },
            "b4ad": {
              "type": "standard",
              "state": "failure"
            }
          },
          "00ca": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "4cd0": {},
          "f695": {},
          "b11a": {},
          "ea5a": {},
          "bca": {},
          "61c7": {},
          "a5b6": {},
          "e9e0": {},
          "c233": {},
          "24a4": {},
          "9d3e": {},
          "ecf": {},
          "1a0c": {},
          "b6a2": {},
          "d470": {},
          "6ba6": {},
          "168c": {},
          "32da": {},
          "b133": {},
          "86f4": {},
          "7cd2": {},
          "4a91": {},
          "50a1": {},
          "e847": {},
          "4cb": {},
          "c5bd": {},
          "f50e": {},
          "98e0": {},
          "adc5": {},
          "d54a": {},
          "462d": {},
          "333c": {},
          "b03e": {},
          "e50": {},
          "5c83": {},
          "a11c": {},
          "be54": {},
          "73f4": {},
          "57a1": {},
          "762c": {},
          "a005": {},
          "cde7": {},
          "36b9": {},
          "a1d5": {}
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "adapterId": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          },
          "required": ["hostname", "ipAddress", "dnsView", "adapterId"]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "hostname": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "ipAddress": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "dnsView": {
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
            "createdARecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "infobloxError": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            },
            "aRecord": {
              "type": ["array", "boolean", "null", "number", "object", "string"]
            }
          }
        },
        "createdVersion": "5.40.5-2021.1.52.0",
        "font_size": 22,
        "lastUpdatedVersion": "5.55.2-2023.2.13",
        "last_updated": "2025-01-24T11:00:39.025Z",
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
    }
  ],
  "folders": [
    {
      "iid": 0,
      "nodeType": "component"
    },
    {
      "nodeType": "folder",
      "name": "Network",
      "children": [
        {
          "iid": 14,
          "nodeType": "component"
        },
        {
          "iid": 7,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Network Container",
      "children": [
        {
          "iid": 13,
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
      "name": "DNS A Record",
      "children": [
        {
          "iid": 19,
          "nodeType": "component"
        },
        {
          "iid": 5,
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
      "name": "DNS CNAME Record",
      "children": [
        {
          "iid": 18,
          "nodeType": "component"
        },
        {
          "iid": 4,
          "nodeType": "component"
        },
        {
          "iid": 11,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "DNS Fixed Address Record",
      "children": [
        {
          "iid": 17,
          "nodeType": "component"
        },
        {
          "iid": 3,
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
      "name": "DNS NS Record",
      "children": [
        {
          "iid": 16,
          "nodeType": "component"
        },
        {
          "iid": 2,
          "nodeType": "component"
        },
        {
          "iid": 9,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "DNS PTR Record",
      "children": [
        {
          "iid": 15,
          "nodeType": "component"
        },
        {
          "iid": 1,
          "nodeType": "component"
        },
        {
          "iid": 8,
          "nodeType": "component"
        }
      ]
    }
  ],
  "created": "2024-08-28T18:46:32.736Z",
  "createdBy": {
    "_id": "6786b32af921f091fd105007",
    "provenance": "Local AAA",
    "username": "admin@itential"
  },
  "lastUpdated": "2025-01-24T11:00:38.997Z",
  "lastUpdatedBy": {
    "_id": "66d1e2b552e6dc384b5d6626",
    "provenance": "Okta",
    "username": "admin@itential"
  },
  "iid": 51,
  "thumbnail": "data:image/png;base64,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",
  "backgroundColor": "#FFFFFF"
}

````

============================================================
FILE: helpers/assets/vendor-juniper-junos.json
DIRECTORY: helpers/assets/
FILENAME: vendor-juniper-junos.json
============================================================
SHA256: 8b364175a33ea0d16c25092d3f7f2fa88dd09b7c3ca588badf1f2208ef7e3a10

````json
{
  "_id": "6a138e0000000000ffff0001",
  "name": "Juniper JUNOS",
  "description": "Juniper JUNOS inventory using NETCONF, software upgrade, and golden configuration",
  "components": [
    {
      "iid": 22,
      "reference": "6a13848a75bc43e3a0bf3492",
      "type": "jsonForm",
      "folder": "/Software Upgrade",
      "document": {
        "id": "6a13848a75bc43e3a0bf3492",
        "created": "2026-05-24T23:06:50.250Z",
        "createdBy": "mike.elrom@itential.com",
        "lastUpdated": "2026-06-25T09:21:14.878Z",
        "lastUpdatedBy": "mike.elrom@itential.com",
        "name": "Upgrade Form",
        "description": "Form input for the Juniper software upgrade automation.",
        "struct": {
          "type": "array",
          "items": [
            {
              "nodeId": "fp-juno-001",
              "type": "string",
              "title": "Device",
              "description": "Inventory device name (e.g. 'Itential Lab JUNOS::aws-lab-junos')",
              "placeholder": "Itential Lab JUNOS::aws-lab-junos",
              "required": true,
              "default": "Itential Lab JUNOS::aws-lab-junos",
              "customKey": "device"
            },
            {
              "nodeId": "fp-juno-002",
              "type": "string",
              "title": "Target Junos Version",
              "description": "Version string the upgrade targets, e.g. 22.4R2.8",
              "placeholder": "22.4R2.8",
              "required": true,
              "customKey": "target_version",
              "default": ""
            },
            {
              "nodeId": "8454772e-f885-4a0a-8562-9ae24b741a72",
              "type": "string",
              "title": "Image Path on Device",
              "description": "",
              "placeholder": "Select an item",
              "required": true,
              "enum": [
                {
                  "id": "90e2b5e7-fb50-4848-9cfc-da5d426f5802",
                  "label": "/var/tmp/junos-install-vsrx3-x86-64-22.4R1.10.tgz",
                  "value": "/var/tmp/junos-install-vsrx3-x86-64-22.4R1.10.tgz"
                },
                {
                  "id": "b1a057bb-1b9a-42c1-8fcb-c2c0c724e8c5",
                  "label": "/var/tmp/junos-install-vsrx3-x86-64-22.4R2.8.tgz",
                  "value": "/var/tmp/junos-install-vsrx3-x86-64-22.4R2.8.tgz"
                }
              ],
              "enumNames": [
                {
                  "id": "91b4cb0f-54fe-4a10-b38c-f25651d96247",
                  "label": "",
                  "value": ""
                },
                {
                  "id": "408c79cc-5288-4448-9511-26c7c7e9027d",
                  "label": "",
                  "value": ""
                }
              ],
              "binding": false,
              "rel": "collection",
              "targetPointer": "/enum",
              "customKey": "image_path",
              "default": "/var/tmp/junos-install-vsrx3-x86-64-22.4R2.8.tgz"
            },
            {
              "nodeId": "200a7ad4-9906-41f2-90e5-26dc2b2f656e",
              "type": "string",
              "title": "Expected Image SHA-256 x",
              "description": "Lowercase 64-char hex hash. Used by Verify Image to confirm the staged image matches.",
              "placeholder": "Select an item",
              "required": true,
              "enum": [
                {
                  "id": "32ed7b87-f41a-4eed-bdff-f410c39d22ba",
                  "label": "9528d02f3ce5958616d5fff140314c013b41e9d34997acd413a15761baa06448",
                  "value": "9528d02f3ce5958616d5fff140314c013b41e9d34997acd413a15761baa06448"
                },
                {
                  "id": "4d0bde74-b59e-4c35-9dbe-a84b4cc7de9a",
                  "label": "8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2",
                  "value": "8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2"
                }
              ],
              "enumNames": [
                {
                  "id": "f356a543-2657-4b20-8de8-fe6e5b68d4ce",
                  "label": "22.4R1.10.tgz - 9528d02f3ce5958616d5fff140314c013b41e9d34997acd413a15761baa06448",
                  "value": "22.4R1.10.tgz - 9528d02f3ce5958616d5fff140314c013b41e9d34997acd413a15761baa06448"
                },
                {
                  "id": "7afdb25d-5e1c-4160-92da-1cf1ecf6b5b3",
                  "label": "22.4R2.8.tgz - 8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2",
                  "value": "22.4R2.8.tgz - 8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2"
                }
              ],
              "binding": false,
              "rel": "collection",
              "targetPointer": "/enum",
              "default": "8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2",
              "customKey": "image_sha256"
            }
          ]
        },
        "schema": {
          "title": "Upgrade Form",
          "description": "Form input for the Juniper software upgrade automation.",
          "type": "object",
          "required": [
            "device",
            "target_version",
            "image_path",
            "image_sha256"
          ],
          "properties": {
            "device": {
              "type": "string",
              "title": "Device",
              "_id": "/properties/device",
              "description": "Inventory device name (e.g. 'Itential Lab JUNOS::aws-lab-junos')",
              "default": "Itential Lab JUNOS::aws-lab-junos"
            },
            "target_version": {
              "type": "string",
              "title": "Target Junos Version",
              "_id": "/properties/target_version",
              "description": "Version string the upgrade targets, e.g. 22.4R2.8",
              "default": ""
            },
            "image_path": {
              "type": "string",
              "title": "Image Path on Device",
              "_id": "/properties/image_path",
              "description": "",
              "default": "/var/tmp/junos-install-vsrx3-x86-64-22.4R2.8.tgz",
              "enum": [
                "/var/tmp/junos-install-vsrx3-x86-64-22.4R1.10.tgz",
                "/var/tmp/junos-install-vsrx3-x86-64-22.4R2.8.tgz"
              ],
              "enumNames": [
                "",
                ""
              ]
            },
            "image_sha256": {
              "type": "string",
              "title": "Expected Image SHA-256 x",
              "_id": "/properties/image_sha256",
              "description": "Lowercase 64-char hex hash. Used by Verify Image to confirm the staged image matches.",
              "default": "8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2",
              "enum": [
                "9528d02f3ce5958616d5fff140314c013b41e9d34997acd413a15761baa06448",
                "8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2"
              ],
              "enumNames": [
                "22.4R1.10.tgz - 9528d02f3ce5958616d5fff140314c013b41e9d34997acd413a15761baa06448",
                "22.4R2.8.tgz - 8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2"
              ]
            }
          }
        },
        "uiSchema": {
          "device": {
            "ui:placeholder": "Itential Lab JUNOS::aws-lab-junos"
          },
          "target_version": {
            "ui:placeholder": "22.4R2.8"
          },
          "image_path": {
            "ui:placeholder": "Select an item"
          },
          "image_sha256": {
            "ui:placeholder": "Select an item"
          },
          "ui:order": [
            "device",
            "target_version",
            "image_path",
            "image_sha256",
            "*"
          ]
        },
        "bindingSchema": {},
        "validationSchema": {},
        "version": "2020.1"
      }
    },
    {
      "iid": 42,
      "reference": "6a1de30f62b073861f971611",
      "type": "jsonForm",
      "folder": "/Golden Configuration",
      "document": {
        "id": "6a1de30f62b073861f971611",
        "created": "2026-06-01T19:52:47.654Z",
        "createdBy": "mike.elrom@itential.com",
        "lastUpdated": "2026-06-24T20:03:06.833Z",
        "lastUpdatedBy": "mike.elrom@itential.com",
        "name": "Compliance Form",
        "description": "",
        "struct": {
          "type": "array",
          "items": [
            {
              "nodeId": "95e19ca7-6692-4f15-b362-2d4c8fa0d1f4",
              "type": "string",
              "title": "Tree Name",
              "description": "",
              "placeholder": "Select an item",
              "required": true,
              "enum": [],
              "enumNames": [],
              "binding": true,
              "rel": "collection",
              "targetPointer": "/enum",
              "customKey": "tree_name",
              "readOnly": false,
              "method": "GET",
              "uniqueItems": false,
              "base": "/configuration_manager",
              "href": "/configs",
              "sourcePointer": "/",
              "sourceKeyPointer": "/name"
            },
            {
              "nodeId": "0e0602fd-c568-4f7e-81c6-5f4accaf4752",
              "type": "string",
              "title": "Tree Version",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "customKey": "version",
              "default": "initial"
            }
          ]
        },
        "schema": {
          "title": "Compliance Form",
          "description": "",
          "type": "object",
          "required": [
            "tree_name",
            "version"
          ],
          "properties": {
            "tree_name": {
              "type": "string",
              "title": "Tree Name",
              "_id": "/properties/tree_name",
              "description": "",
              "enum": [],
              "enumNames": []
            },
            "version": {
              "type": "string",
              "title": "Tree Version",
              "_id": "/properties/version",
              "description": "",
              "default": "initial"
            }
          }
        },
        "uiSchema": {
          "tree_name": {
            "ui:placeholder": "Select an item"
          },
          "version": {
            "ui:placeholder": "Enter text"
          },
          "ui:order": [
            "tree_name",
            "version",
            "*"
          ]
        },
        "bindingSchema": {
          "properties": {
            "tree_name": {
              "binding:method": "GET",
              "binding:link": {
                "$ref": "/links",
                "rel": "collection"
              },
              "binding:target": {
                "propertyPointer": "/enum"
              },
              "binding:hyperSchema": {
                "type": "object",
                "base": "/configuration_manager",
                "links": [
                  {
                    "rel": "collection",
                    "href": "/configs",
                    "targetMediaType": "application/json",
                    "targetSchema": {
                      "$ref": "#"
                    },
                    "variables": []
                  }
                ]
              },
              "binding:source": {
                "propertyPointer": "/",
                "keyPointer": "/name"
              }
            }
          }
        },
        "validationSchema": {},
        "version": "2020.1"
      }
    },
    {
      "iid": 46,
      "reference": "6a1e325462b073861f971612",
      "type": "jsonForm",
      "folder": "/Port Turn Up",
      "document": {
        "id": "6a1e325462b073861f971612",
        "created": "2026-06-02T01:31:00.689Z",
        "createdBy": "mike.elrom@itential.com",
        "lastUpdated": "2026-06-25T09:10:42.623Z",
        "lastUpdatedBy": "mike.elrom@itential.com",
        "name": "8021.Q Sub Interface Form",
        "description": "",
        "struct": {
          "type": "array",
          "items": [
            {
              "nodeId": "1ce2213f-8804-41a3-961b-4fe82d1834f5",
              "type": "string",
              "title": "Device",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "default": "Itential Lab JUNOS::aws-lab-junos"
            },
            {
              "nodeId": "152dff76-28ec-4162-8dca-338dd7e17bb1",
              "type": "string",
              "title": "Interface",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "default": "ge-0/0/0"
            },
            {
              "nodeId": "6b723497-01b2-46f8-b2f6-976a3ffdf714",
              "type": "string",
              "title": "VLAN ID",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "customKey": "vlan_id",
              "default": "100"
            },
            {
              "nodeId": "6eaf9ad6-5633-4a26-852d-a8d6be11fc88",
              "type": "string",
              "title": "Description",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "default": "CORP LAN"
            },
            {
              "nodeId": "b73ebfd6-0dd9-4036-82b5-666bceddbde2",
              "type": "string",
              "title": "IP Address",
              "description": "",
              "placeholder": "Enter text",
              "required": false,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "customKey": "ip_address",
              "pattern": "^(\\d{1,3}\\.){3}\\d{1,3}\\/(8|16|24|2[89]|3[012])$",
              "default": "192.168.100.1/24"
            },
            {
              "nodeId": "c30b8f00-6de8-46bb-96d9-6126d117e10d",
              "type": "string",
              "title": "zone",
              "description": "",
              "placeholder": "Enter text",
              "required": true,
              "readOnly": false,
              "binding": false,
              "rel": "item",
              "targetPointer": "/default",
              "default": "trust"
            }
          ]
        },
        "schema": {
          "title": "8021.Q Sub Interface Form",
          "description": "",
          "type": "object",
          "required": [
            "device",
            "interface",
            "vlan_id",
            "description",
            "zone"
          ],
          "properties": {
            "device": {
              "type": "string",
              "title": "Device",
              "_id": "/properties/device",
              "description": "",
              "default": "Itential Lab JUNOS::aws-lab-junos"
            },
            "interface": {
              "type": "string",
              "title": "Interface",
              "_id": "/properties/interface",
              "description": "",
              "default": "ge-0/0/0"
            },
            "vlan_id": {
              "type": "string",
              "title": "VLAN ID",
              "_id": "/properties/vlan_id",
              "description": "",
              "default": "100"
            },
            "description": {
              "type": "string",
              "title": "Description",
              "_id": "/properties/description",
              "description": "",
              "default": "CORP LAN"
            },
            "ip_address": {
              "type": "string",
              "title": "IP Address",
              "_id": "/properties/ip_address",
              "description": "",
              "default": "192.168.100.1/24",
              "pattern": "^(\\d{1,3}\\.){3}\\d{1,3}\\/(8|16|24|2[89]|3[012])$"
            },
            "zone": {
              "type": "string",
              "title": "zone",
              "_id": "/properties/zone",
              "description": "",
              "default": "trust"
            }
          }
        },
        "uiSchema": {
          "device": {
            "ui:placeholder": "Enter text"
          },
          "interface": {
            "ui:placeholder": "Enter text"
          },
          "vlan_id": {
            "ui:placeholder": "Enter text"
          },
          "description": {
            "ui:placeholder": "Enter text"
          },
          "ip_address": {
            "ui:placeholder": "Enter text"
          },
          "zone": {
            "ui:placeholder": "Enter text"
          },
          "ui:order": [
            "device",
            "interface",
            "vlan_id",
            "description",
            "ip_address",
            "zone",
            "*"
          ]
        },
        "bindingSchema": {},
        "validationSchema": {},
        "version": "2020.1"
      }
    },
    {
      "iid": 48,
      "reference": "@6a138e0000000000ffff0001: Port Turn Up Post Check",
      "type": "mopCommandTemplate",
      "folder": "/Port Turn Up",
      "document": {
        "tags": [],
        "name": "Port Turn Up Post Check",
        "description": "Captures pre/post device state for a Junos device. Runs show version, show system storage, show interfaces terse, and show route summary. Rules are sanity-only \u2014 the workflow reads commands_results[].response for the actual diff inputs.",
        "os": "juniper_junos",
        "passRule": true,
        "ignoreWarnings": null,
        "commands": [
          {
            "command": "show configuration interfaces <!interface!>",
            "passRule": true,
            "rules": [
              {
                "rule": "",
                "eval": "contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "show security zones <!zone!>",
            "passRule": true,
            "rules": [
              {
                "rule": "",
                "eval": "contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "show route table inet.0",
            "passRule": true,
            "rules": [
              {
                "rule": "",
                "eval": "contains",
                "severity": "error"
              }
            ]
          }
        ],
        "created": 1780367306548,
        "createdBy": "6a0c557474e890f65883e175",
        "lastUpdated": 1782331386951,
        "lastUpdatedBy": "mike.elrom@itential.com"
      }
    },
    {
      "iid": 47,
      "reference": "@6a138e0000000000ffff0001: Port Turn Up Pre Check",
      "type": "mopCommandTemplate",
      "folder": "/Port Turn Up",
      "document": {
        "tags": [],
        "name": "Port Turn Up Pre Check",
        "description": "Captures pre/post device state for a Junos device. Runs show version, show system storage, show interfaces terse, and show route summary. Rules are sanity-only \u2014 the workflow reads commands_results[].response for the actual diff inputs.",
        "os": "juniper_junos",
        "passRule": true,
        "ignoreWarnings": null,
        "commands": [
          {
            "command": "show configuration interfaces <!interface!>",
            "passRule": true,
            "rules": [
              {
                "rule": "",
                "eval": "contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "show security zones <!zone!>",
            "passRule": true,
            "rules": [
              {
                "rule": "",
                "eval": "contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "show route table inet.0",
            "passRule": true,
            "rules": [
              {
                "rule": "",
                "eval": "contains",
                "severity": "error"
              }
            ]
          }
        ],
        "created": 1780364670141,
        "createdBy": "6a0c557474e890f65883e175",
        "lastUpdated": 1782331387307,
        "lastUpdatedBy": "mike.elrom@itential.com"
      }
    },
    {
      "iid": 31,
      "reference": "@6a138e0000000000ffff0001: Pre and Post Checks",
      "type": "mopCommandTemplate",
      "folder": "/Software Upgrade",
      "document": {
        "tags": [],
        "name": "Pre and Post Checks",
        "description": "Captures pre/post device state for a Junos device. Runs show version, show system storage, show interfaces terse, and show route summary. Rules are sanity-only \u2014 the workflow reads commands_results[].response for the actual diff inputs.",
        "os": "juniper_junos",
        "passRule": true,
        "ignoreWarnings": null,
        "commands": [
          {
            "command": "show version",
            "passRule": true,
            "rules": [
              {
                "rule": "Junos:",
                "eval": "contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "show system storage",
            "passRule": true,
            "rules": [
              {
                "rule": "/dev/gpt/junos",
                "eval": "contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "show interfaces terse",
            "passRule": true,
            "rules": [
              {
                "rule": "",
                "eval": "contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "show route summary",
            "passRule": true,
            "rules": [
              {
                "rule": "destinations",
                "eval": "contains",
                "severity": "error"
              }
            ]
          }
        ],
        "created": 1779675515376,
        "createdBy": "itential-02",
        "lastUpdated": 1782331387033,
        "lastUpdatedBy": "mike.elrom@itential.com"
      }
    },
    {
      "iid": 36,
      "reference": "@6a138e0000000000ffff0001: Reboot",
      "type": "mopCommandTemplate",
      "folder": "/Software Upgrade",
      "document": {
        "tags": [],
        "name": "Reboot",
        "description": "Runs request system software add <image_path> no-validate no-copy, then request system reboot. Reboot response may be partial because SSH terminates.",
        "os": "juniper_junos",
        "passRule": true,
        "ignoreWarnings": null,
        "commands": [
          {
            "command": "request system reboot",
            "passRule": true,
            "rules": [
              {
                "rule": "Shutdown NOW!",
                "eval": "contains",
                "severity": "warn"
              }
            ]
          }
        ],
        "created": 1779719937714,
        "createdBy": "6a0c557474e890f65883e175",
        "lastUpdated": 1782331387198,
        "lastUpdatedBy": "mike.elrom@itential.com"
      }
    },
    {
      "iid": 32,
      "reference": "@6a138e0000000000ffff0001: Stage Upgrade",
      "type": "mopCommandTemplate",
      "folder": "/Software Upgrade",
      "document": {
        "tags": [],
        "name": "Stage Upgrade",
        "description": "Runs request system software add <image_path> no-validate no-copy, then request system reboot. Reboot response may be partial because SSH terminates.",
        "os": "juniper_junos",
        "passRule": true,
        "ignoreWarnings": null,
        "commands": [
          {
            "command": "request system software add <!image_path!> no-validate no-copy",
            "passRule": true,
            "rules": [
              {
                "rule": "set will be activated at next reboot",
                "eval": "contains",
                "severity": "warn"
              }
            ]
          }
        ],
        "created": 1779675515780,
        "createdBy": "itential-02",
        "lastUpdated": 1782331387095,
        "lastUpdatedBy": "mike.elrom@itential.com"
      }
    },
    {
      "iid": 27,
      "reference": "@6a138e0000000000ffff0001: Verify Image",
      "type": "mopCommandTemplate",
      "folder": "/Software Upgrade",
      "document": {
        "tags": [],
        "name": "Verify Image",
        "description": "Confirms staged image exists at the specified path and sha-256 matches expected hash.",
        "os": "juniper_junos",
        "passRule": true,
        "ignoreWarnings": false,
        "commands": [
          {
            "command": "file list <!image_path!>",
            "passRule": true,
            "rules": [
              {
                "rule": "No such file",
                "eval": "!contains",
                "severity": "error"
              }
            ]
          },
          {
            "command": "file checksum sha-256 <!image_path!>",
            "passRule": true,
            "rules": [
              {
                "rule": "<!image_sha256!>",
                "eval": "contains",
                "severity": "error"
              }
            ]
          }
        ],
        "created": 1779674845008,
        "createdBy": "itential-02",
        "lastUpdated": 1782331387155,
        "lastUpdatedBy": "mike.elrom@itential.com"
      }
    },
    {
      "iid": 30,
      "reference": "@6a138e0000000000ffff0001: Version Check",
      "type": "mopCommandTemplate",
      "folder": "/Software Upgrade",
      "document": {
        "tags": [],
        "name": "Version Check",
        "description": "Verifies the running Junos version matches an expected string.",
        "os": "juniper_junos",
        "passRule": true,
        "ignoreWarnings": false,
        "commands": [
          {
            "command": "show version",
            "passRule": true,
            "rules": [
              {
                "rule": "<!target_version!>",
                "eval": "contains",
                "severity": "error",
                "evaluation": "pass"
              },
              {
                "rule": "Service execution failed (exit code 1): No error output",
                "eval": "!contains",
                "severity": "error",
                "evaluation": "pass"
              }
            ]
          }
        ],
        "created": 1779674846087,
        "createdBy": "itential-02",
        "lastUpdated": 1782331387264,
        "lastUpdatedBy": "mike.elrom@itential.com"
      }
    },
    {
      "iid": 33,
      "reference": "d7825e52-44a8-4aaf-a485-341981d34e01",
      "type": "workflow",
      "folder": "/Software Upgrade",
      "document": {
        "name": "JUNOS Upgrade",
        "description": "Sample Input\n  {\n  \"device\": \"Itential Lab JUNOS::aws-lab-junos\",\n  \"target_version\": \"22.4R2.8\",\n  \"image_path\": \"/var/tmp/junos-install-vsrx3-x86-64-22.4R2.8.tgz\",\n  \"image_sha256\": \"8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2\"\n}",
        "tasks": {
          "1784": {
            "name": "runCode",
            "canvasName": "runCode",
            "summary": "Check Already Upgraded",
            "description": "Execute code (e.g. Python) on a Gateway5 cluster without requiring a pre-configured service. The code is sent directly to the gateway for execution.",
            "location": "Application",
            "locationType": null,
            "app": "GatewayManager",
            "type": "automatic",
            "displayName": "GatewayManager",
            "variables": {
              "incoming": {
                "clusterId": "cluster-itential",
                "language": "python",
                "code": "import sys\nimport json\nimport re\n\n# \u2500\u2500 Read inputs from stdin (IAG runCode standard) \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\ndata = json.load(sys.stdin)\n\ndevice_results = data.get('device_results', {})\ntarget_version  = data.get('target_version', '')\n\n# \u2500\u2500 Extract device name and version from 'show version' output \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\ncommands    = device_results.get('commands_results', [])\ndevice_name = commands[0].get('device') if commands else None\n\nfound_version = None\nfor cmd in commands:\n    if cmd.get('raw', '').strip().lower() == 'show version':\n        response = cmd.get('response', '')\n        match = re.search(r'^Junos:\\s+(\\S+)', response, re.MULTILINE)\n        if match:\n            found_version = match.group(1)\n        break\n\n# \u2500\u2500 Build result \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\nif found_version is None:\n    result = {\n        'passed':  False,\n        'found':   None,\n        'target':  target_version,\n        'device':  device_name,\n        'message': \"Could not extract Junos version \u2014 'show version' output missing or malformed.\"\n    }\nelse:\n    passed = found_version == target_version\n    result = {\n        'passed':  passed,\n        'found':   found_version,\n        'target':  target_version,\n        'device':  device_name,\n        'message': (\n            f\"Device '{device_name}' is running Junos {found_version} \u2014 matches target {target_version}.\"\n            if passed else\n            f\"Device '{device_name}' is running Junos {found_version} \u2014 expected {target_version}.\"\n        )\n    }\n\n# \u2500\u2500 Emit JSON to stdout (captured as stdout_json by the platform) \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\nprint(json.dumps(result))",
                "data": {
                  "target_version": "$var.job.target_version",
                  "device_results": "$var.a2.mop_template_results"
                },
                "safety": {
                  "timeout": 1
                },
                "packages": []
              },
              "outgoing": {
                "result": ""
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 144
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -300
            }
          },
          "a2": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Pre Check",
            "description": "Captures show version, system storage, interfaces, route summary",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Pre and Post Checks",
                "variables": "$var.b63a.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.preCheckOutput"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": -72
            }
          },
          "b1": {
            "name": "backUpDevice",
            "canvasName": "backUpDevice",
            "summary": "Backup Running Config (pre)",
            "description": "",
            "location": "Application",
            "locationType": null,
            "app": "ConfigurationManager",
            "type": "automatic",
            "displayName": "ConfigurationManager",
            "variables": {
              "incoming": {
                "name": "$var.job.device",
                "options": {}
              },
              "outgoing": {
                "status": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 312
            }
          },
          "d1": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Verify Image",
            "description": "",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Verify Image",
                "variables": "$var.b63a.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.verifyImageResults"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 456
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 1788
            }
          },
          "d768": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Pre-check",
            "description": "Run an evaluation",
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
                          "task": "a2",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 36
            }
          },
          "f3ca": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Verify",
            "description": "Run an evaluation",
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
                          "task": "d1",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 570
            }
          },
          "c681": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Stage Upgrade",
            "description": "",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Stage Upgrade",
                "variables": "$var.b63a.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.stageUpgradeResults"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 672
            }
          },
          "6c10": {
            "name": "reattempt",
            "canvasName": "reattempt",
            "summary": "Reattempt",
            "description": "Workflow will follow reattempt task's outgoing transition after n minutes of delay.",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "job_id": "$var.job._id",
                "attemptID": "reboot",
                "minutes": 1,
                "attempts": 30
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -372,
              "y": 1224
            }
          },
          "926a": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Version Check",
            "description": "Captures show version, system storage, interfaces, route summary",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Version Check",
                "variables": "$var.b63a.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.versionCheckResults"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 1116
            }
          },
          "80da": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Stage Upgrade",
            "description": "Run an evaluation",
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
                          "task": "c681",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 792
            }
          },
          "908f": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Version Check",
            "description": "Run an evaluation",
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
                          "task": "926a",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 1224
            }
          },
          "e5fb": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Reboot",
            "description": "",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Reboot",
                "variables": "$var.b63a.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.rebootResults"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 900
            }
          },
          "20d5": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Reboot",
            "description": "Run an evaluation",
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
                          "task": "e5fb",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 1008
            }
          },
          "f215": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Post Check",
            "description": "Captures show version, system storage, interfaces, route summary",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Pre and Post Checks",
                "variables": "$var.b63a.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.postCheckResults"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 1344
            }
          },
          "6d1a": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Post-check",
            "description": "Run an evaluation",
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
                          "task": "f215",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 1464
            }
          },
          "0761": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Already Upgraded",
            "description": "Run an evaluation",
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
                          "task": "1784",
                          "variable": "result"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "stdout_json.passed",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 336,
              "y": 324
            }
          },
          "0193": {
            "name": "renderJinja2ContextWithCast",
            "canvasName": "renderJinja2ContextWithCast",
            "summary": "Response: Failed Attempts",
            "description": "Renders jinja2 Context output with data cast.",
            "location": "Application",
            "locationType": null,
            "app": "TemplateBuilder",
            "type": "automatic",
            "displayName": "TemplateBuilder",
            "variables": {
              "incoming": {
                "template": "{\"response\":\"failure\", \"message\": \"The software upgrade exhausted attempts, please review for more details.\"}",
                "variables": {},
                "castDataType": "object"
              },
              "outgoing": {
                "renderedTemplate": "$var.job.response"
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -372,
              "y": 1620
            }
          },
          "e8a2": {
            "name": "renderJinja2ContextWithCast",
            "canvasName": "renderJinja2ContextWithCast",
            "summary": "Response: Success",
            "description": "Renders jinja2 Context output with data cast.",
            "location": "Application",
            "locationType": null,
            "app": "TemplateBuilder",
            "type": "automatic",
            "displayName": "TemplateBuilder",
            "variables": {
              "incoming": {
                "template": "{\"response\":\"success\", \"message\": \"The software upgrade was successful.\"}",
                "variables": {},
                "castDataType": "object"
              },
              "outgoing": {
                "renderedTemplate": "$var.job.response"
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 1620
            }
          },
          "799d": {
            "name": "renderJinja2ContextWithCast",
            "canvasName": "renderJinja2ContextWithCast",
            "summary": "Response: Not Needed",
            "description": "Renders jinja2 Context output with data cast.",
            "location": "Application",
            "locationType": null,
            "app": "TemplateBuilder",
            "type": "automatic",
            "displayName": "TemplateBuilder",
            "variables": {
              "incoming": {
                "template": "{\"response\":\"success\", \"message\": \"The software upgrade was not needed. The device version matches requested version.\"}",
                "variables": {},
                "castDataType": "object"
              },
              "outgoing": {
                "renderedTemplate": "$var.job.response"
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 336,
              "y": 1620
            }
          },
          "b63a": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Variable Object",
            "description": "Merge data into a single object",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "device",
                    "value": {
                      "task": "job",
                      "variable": "device"
                    }
                  },
                  {
                    "key": "target_version",
                    "value": {
                      "task": "job",
                      "variable": "target_version"
                    }
                  },
                  {
                    "key": "image_path",
                    "value": {
                      "task": "job",
                      "variable": "image_path"
                    }
                  },
                  {
                    "key": "image_sha256",
                    "value": {
                      "task": "job",
                      "variable": "image_sha256"
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
              "x": 0,
              "y": -180
            }
          }
        },
        "transitions": {
          "1784": {
            "0761": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_start": {
            "b63a": {
              "state": "success",
              "type": "standard"
            }
          },
          "a2": {
            "d768": {
              "state": "success",
              "type": "standard"
            }
          },
          "b1": {
            "d1": {
              "state": "success",
              "type": "standard"
            }
          },
          "d1": {
            "f3ca": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "d768": {
            "1784": {
              "state": "success",
              "type": "standard"
            }
          },
          "f3ca": {
            "c681": {
              "state": "success",
              "type": "standard"
            }
          },
          "c681": {
            "80da": {
              "state": "success",
              "type": "standard"
            }
          },
          "6c10": {
            "926a": {
              "state": "success",
              "type": "revert"
            },
            "0193": {
              "state": "failure",
              "type": "standard"
            }
          },
          "926a": {
            "908f": {
              "state": "success",
              "type": "standard"
            },
            "6c10": {
              "type": "standard",
              "state": "error"
            }
          },
          "80da": {
            "e5fb": {
              "state": "success",
              "type": "standard"
            }
          },
          "908f": {
            "6c10": {
              "type": "standard",
              "state": "failure"
            },
            "f215": {
              "state": "success",
              "type": "standard"
            }
          },
          "e5fb": {
            "20d5": {
              "state": "success",
              "type": "standard"
            }
          },
          "20d5": {
            "926a": {
              "state": "success",
              "type": "standard"
            }
          },
          "f215": {
            "6d1a": {
              "state": "success",
              "type": "standard"
            }
          },
          "6d1a": {
            "e8a2": {
              "state": "success",
              "type": "standard"
            }
          },
          "0761": {
            "b1": {
              "type": "standard",
              "state": "failure"
            },
            "799d": {
              "state": "success",
              "type": "standard"
            }
          },
          "0193": {
            "workflow_end": {
              "type": "standard",
              "state": "success"
            }
          },
          "e8a2": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "799d": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "b63a": {
            "a2": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "target_version": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "device": {
              "anyOf": [
                {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "examples": [
                      "Cisco ASA",
                      "Cisco NX-OS"
                    ]
                  }
                },
                {
                  "title": "name",
                  "type": "string",
                  "examples": [
                    "xr9kv-atl"
                  ]
                }
              ]
            },
            "_id": {
              "title": "job_id",
              "type": "string",
              "examples": [
                "12476bef62224efb97684e43"
              ]
            },
            "image_path": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "image_sha256": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            }
          },
          "required": [
            "target_version",
            "device",
            "_id",
            "image_path",
            "image_sha256"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "target_version": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "device": {
              "anyOf": [
                {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "examples": [
                      "Cisco ASA",
                      "Cisco NX-OS"
                    ]
                  }
                },
                {
                  "title": "name",
                  "type": "string",
                  "examples": [
                    "xr9kv-atl"
                  ]
                }
              ]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "image_path": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "image_sha256": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "initiator": {
              "type": "string"
            },
            "preCheckOutput": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            },
            "verifyImageResults": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            },
            "stageUpgradeResults": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            },
            "versionCheckResults": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            },
            "rebootResults": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            },
            "postCheckResults": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            },
            "response": {
              "title": "renderedTemplate",
              "type": "object",
              "examples": [
                {
                  "renderedTemplate": "John was born in year 2000"
                }
              ]
            }
          }
        },
        "scenarios": [],
        "type": "automation",
        "font_size": 12,
        "createdVersion": "6.4.0",
        "lastUpdatedVersion": "5.55.5",
        "last_updated": "2026-06-25T10:18:09.852Z",
        "last_updated_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "created": "1970-01-01T00:00:00.000Z",
        "preAutomationTime": 0,
        "sla": 0,
        "uuid": "a63333bf-5479-46a8-a3c0-1dacdfa96c03",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 8
      }
    },
    {
      "iid": 38,
      "reference": "e12afde2-c824-492f-b76a-794d1eeda432",
      "type": "workflow",
      "folder": "/Golden Configuration",
      "document": {
        "name": "Run Compliance",
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "x": 0,
            "y": 0.5,
            "nodeLocation": {
              "x": -420,
              "y": -996
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "x": 1,
            "y": 0.5,
            "nodeLocation": {
              "x": -420,
              "y": -336
            }
          },
          "509b": {
            "name": "runComplianceForTree",
            "canvasName": "runComplianceForTree",
            "summary": "Run Golden Config Tree Compliance",
            "description": "Run Golden Config Tree Compliance",
            "location": "Application",
            "locationType": null,
            "app": "ConfigurationManager",
            "type": "automatic",
            "displayName": "ConfigurationManager",
            "variables": {
              "incoming": {
                "treeId": "$var.67fa.result#/stdout_json/tree/id",
                "version": "$var.job.version",
                "variables": "",
                "grading": ""
              },
              "outgoing": {
                "runComplianceBatchResult": null
              },
              "error": "",
              "decorators": [
                {
                  "type": "query",
                  "pointer": "/incoming/treeId",
                  "displayPath": ".stdout_json.tree.id"
                }
              ]
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": -420,
              "y": -660
            }
          },
          "5f5f": {
            "name": "getGoldenConfigTrees",
            "canvasName": "getGoldenConfigTrees",
            "summary": "Get All Golden Config Trees",
            "description": "Get All Golden Config Trees",
            "location": "Application",
            "locationType": null,
            "app": "ConfigurationManager",
            "type": "automatic",
            "displayName": "ConfigurationManager",
            "variables": {
              "incoming": {},
              "outgoing": {
                "goldenConfigTrees": null
              }
            },
            "groups": [],
            "actor": "Pronghorn",
            "nodeLocation": {
              "x": -420,
              "y": -876
            }
          },
          "67fa": {
            "name": "runCode",
            "canvasName": "runCode",
            "summary": "Get treeId",
            "description": "Execute code (e.g. Python) on a Gateway5 cluster without requiring a pre-configured service. The code is sent directly to the gateway for execution.",
            "location": "Application",
            "locationType": null,
            "app": "GatewayManager",
            "type": "automatic",
            "displayName": "GatewayManager",
            "variables": {
              "incoming": {
                "clusterId": "cluster-itential",
                "language": "python",
                "code": "import sys\nimport json\n\ndata = json.load(sys.stdin)\n\ntree_name = data.get('tree_name', '')\ntrees = data.get('golden_config_trees', [])\n\nmatched_tree = next((t for t in trees if t.get('name') == tree_name), None)\n\nif matched_tree:\n    print(f\"Matched tree: {matched_tree.get('name')} ({matched_tree.get('id')})\", file=sys.stderr)\n    print(json.dumps({\"tree\": matched_tree}))\nelse:\n    print(f\"No tree found matching name: '{tree_name}'\", file=sys.stderr)\n    print(json.dumps({\"error\": f\"No tree found with name '{tree_name}'\"}))",
                "data": {
                  "golden_config_trees": "$var.5f5f.goldenConfigTrees",
                  "tree_name": "$var.job.tree_name"
                },
                "safety": {
                  "timeout": 1
                },
                "packages": []
              },
              "outgoing": {
                "result": ""
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -420,
              "y": -768
            }
          },
          "cad0": {
            "name": "renderJinja2ContextWithCast",
            "canvasName": "renderJinja2ContextWithCast",
            "summary": "Render HTML View",
            "description": "Renders jinja2 Context output with data cast.",
            "location": "Application",
            "locationType": null,
            "app": "TemplateBuilder",
            "type": "automatic",
            "displayName": "TemplateBuilder",
            "variables": {
              "incoming": {
                "template": "<h2 style=\"font-size:16px;font-family:Arial,sans-serif;margin:0 0 8px 0;\">Golden Config Compliance Report</h2>\n<p style=\"font-size:12px;color:#555;font-family:Arial,sans-serif;\">Batch ID: <strong>{{ batchId }}</strong> &nbsp;|&nbsp; Status: <strong>{{ status }}</strong> &nbsp;|&nbsp; {{ reports | length }} device report(s)</p>\n\n<h3 style=\"font-size:14px;font-family:Arial,sans-serif;border-bottom:1px solid #ddd;padding-bottom:4px;\">Summary</h3>\n<table style=\"border-collapse:collapse;width:100%;font-size:12px;font-family:Arial,sans-serif;margin-bottom:16px;\">\n  <thead>\n    <tr>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Device</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Node Path</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Score</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Grade</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Warnings</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Errors</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Passes</th>\n    </tr>\n  </thead>\n  <tbody>\n  {% for report in reports %}\n    {% if report.grade == 'fail' %}\n      {% set scoreColor = '#c0392b' %}\n      {% set badgeBg = '#fdecea' %}\n      {% set badgeColor = '#c0392b' %}\n      {% set badgeBorder = '#e5b4b1' %}\n    {% else %}\n      {% set scoreColor = '#27ae60' %}\n      {% set badgeBg = '#eafaf1' %}\n      {% set badgeColor = '#27ae60' %}\n      {% set badgeBorder = '#a9dfbf' %}\n    {% endif %}\n    <tr>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ report.device }}</td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ report.nodePath }}</td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;color:{{ scoreColor }};\">{{ report.score }}%</td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">\n        <span style=\"display:inline-block;padding:2px 7px;border-radius:3px;font-size:11px;font-weight:bold;background:{{ badgeBg }};color:{{ badgeColor }};border:1px solid {{ badgeBorder }};\">{{ report.grade }}</span>\n      </td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ report.totals.warnings }}</td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ report.totals.errors }}</td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ report.totals.passes }}</td>\n    </tr>\n  {% endfor %}\n  </tbody>\n</table>\n\n{% for report in reports %}\n  {% if report.grade == 'fail' %}\n    {% set scoreColor = '#c0392b' %}\n    {% set badgeBg = '#fdecea' %}\n    {% set badgeColor = '#c0392b' %}\n    {% set badgeBorder = '#e5b4b1' %}\n  {% else %}\n    {% set scoreColor = '#27ae60' %}\n    {% set badgeBg = '#eafaf1' %}\n    {% set badgeColor = '#27ae60' %}\n    {% set badgeBorder = '#a9dfbf' %}\n  {% endif %}\n<h3 style=\"font-size:14px;font-family:Arial,sans-serif;border-bottom:1px solid #ddd;padding-bottom:4px;margin-top:16px;\">{{ report.device }} \u2014 {{ report.nodePath }}</h3>\n<div style=\"background:#f9f9f9;border:1px solid #ddd;border-radius:4px;padding:10px 14px;margin-bottom:12px;font-family:Arial,sans-serif;font-size:12px;\">\n  Score: <strong style=\"color:{{ scoreColor }};\">{{ report.score }}%</strong> &nbsp;|&nbsp;\n  Grade: <strong style=\"color:{{ badgeColor }};\">{{ report.grade }}</strong> &nbsp;|&nbsp;\n  Warnings: <strong>{{ report.totals.warnings }}</strong> &nbsp;|&nbsp;\n  Errors: <strong>{{ report.totals.errors }}</strong> &nbsp;|&nbsp;\n  Passes: <strong>{{ report.totals.passes }}</strong> &nbsp;|&nbsp;\n  Device Type: <strong>{{ report.deviceType }}</strong> &nbsp;|&nbsp;\n  Timestamp: <strong>{{ report.timestamp }}</strong>\n</div>\n\n{% if report.issues %}\n<table style=\"border-collapse:collapse;width:100%;font-size:12px;font-family:Arial,sans-serif;margin-bottom:16px;\">\n  <thead>\n    <tr>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Severity</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Type</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Required Config (set command)</th>\n      <th style=\"background:#f0f0f0;text-align:left;padding:6px 8px;border:1px solid #ccc;\">Fix Mode</th>\n    </tr>\n  </thead>\n  <tbody>\n  {% for issue in report.issues %}\n    <tr>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ issue.severity }}</td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ issue.type }}</td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\"><code style=\"font-family:monospace;font-size:11px;background:#f8f8f8;padding:2px 5px;border:1px solid #e0e0e0;border-radius:2px;\">{{ issue.spec.words | join(\" \", \"value\") }}</code></td>\n      <td style=\"padding:6px 8px;border:1px solid #ddd;font-size:12px;\">{{ issue.spec.fixMode }}</td>\n    </tr>\n  {% endfor %}\n  </tbody>\n</table>\n{% else %}\n<p style=\"color:#27ae60;font-family:Arial,sans-serif;font-size:12px;\">No issues found.</p>\n{% endif %}\n\n{% endfor %}",
                "variables": "$var.509b.runComplianceBatchResult",
                "castDataType": "string"
              },
              "outgoing": {
                "renderedTemplate": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -420,
              "y": -552
            }
          },
          "562a": {
            "name": "ViewHTML",
            "canvasName": "ViewHTML",
            "summary": "View HTML",
            "description": "Displays HTML.",
            "location": "Application",
            "app": "WorkFlowEngine",
            "displayName": "Tools",
            "type": "manual",
            "variables": {
              "incoming": {
                "header": "",
                "body": "$var.cad0.renderedTemplate",
                "variables": "",
                "btn_success": "",
                "btn_failure": ""
              },
              "outgoing": {}
            },
            "view": "/workflow_engine/task/ViewHTML",
            "groups": [],
            "nodeLocation": {
              "x": -420,
              "y": -444
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "5f5f": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "509b": {
            "cad0": {
              "state": "success",
              "type": "standard"
            }
          },
          "5f5f": {
            "67fa": {
              "state": "success",
              "type": "standard"
            }
          },
          "67fa": {
            "509b": {
              "state": "success",
              "type": "standard"
            }
          },
          "cad0": {
            "562a": {
              "state": "success",
              "type": "standard"
            }
          },
          "562a": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "version": {
              "title": "version",
              "type": "string",
              "examples": [
                "initial",
                "v2",
                "v3",
                "draft-v4"
              ]
            },
            "tree_name": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            }
          },
          "required": [
            "version",
            "tree_name"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "version": {
              "title": "version",
              "type": "string",
              "examples": [
                "initial",
                "v2",
                "v3",
                "draft-v4"
              ]
            },
            "tree_name": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            }
          }
        },
        "scenarios": [],
        "type": "automation",
        "font_size": 12,
        "last_updated": "2026-06-24T20:03:06.844Z",
        "last_updated_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "lastUpdatedVersion": "4.69.69",
        "uuid": "9d48564f-80c2-40c5-a95e-b897050c0314",
        "created": "2026-05-31T20:05:43.869Z",
        "created_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "createdVersion": "5.55.5",
        "canvasVersion": 3,
        "tags": [],
        "groups": [],
        "migrationVersion": 8
      }
    },
    {
      "iid": 39,
      "reference": "8d63cf1e-a93a-419f-bde8-a42a3bf20244",
      "type": "workflow",
      "folder": "/Inventory Management",
      "document": {
        "description": "Create inventory in Itential Inventory Manager from NetBox as a source of truth",
        "tasks": {
          "7291": {
            "name": "populateInventory",
            "canvasName": "populateInventory",
            "summary": "Populate inventory with nodes (clears existing nodes first)",
            "description": "Bulk insert nodes into an inventory. All existing nodes in the inventory are cleared before the new nodes are inserted.",
            "location": "Application",
            "locationType": null,
            "app": "InventoryManager",
            "type": "automatic",
            "displayName": "InventoryManager",
            "variables": {
              "incoming": {
                "inventory_identifier": "$var.job.inventoryName",
                "nodes": "$var.d628.response"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -48,
              "y": 48
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "x": 0,
            "y": 0.5,
            "nodeLocation": {
              "x": -48,
              "y": -480
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "x": 1,
            "y": 0.5,
            "nodeLocation": {
              "x": -48,
              "y": 180
            }
          },
          "880d": {
            "name": "dcim_devices_list",
            "canvasName": "dcim_devices_list",
            "summary": "Get a list of device objects",
            "description": "Get a list of device objects.",
            "location": "Adapter",
            "locationType": "NetBox REST API:4.6.0 (4.6)",
            "app": "NetBox REST API:4.6.0 (4.6)",
            "type": "automatic",
            "displayName": "NetBox-Itential-Lab",
            "variables": {
              "incoming": {
                "airflow": "",
                "airflow__empty": "",
                "airflow__ic": "",
                "airflow__ie": "",
                "airflow__iew": "",
                "airflow__iregex": "",
                "airflow__isw": "",
                "airflow__n": "",
                "airflow__nic": "",
                "airflow__nie": "",
                "airflow__niew": "",
                "airflow__nisw": "",
                "airflow__regex": "",
                "asset_tag": "",
                "asset_tag__empty": "",
                "asset_tag__ic": "",
                "asset_tag__ie": "",
                "asset_tag__iew": "",
                "asset_tag__iregex": "",
                "asset_tag__isw": "",
                "asset_tag__n": "",
                "asset_tag__nic": "",
                "asset_tag__nie": "",
                "asset_tag__niew": "",
                "asset_tag__nisw": "",
                "asset_tag__regex": "",
                "cluster_group": "",
                "cluster_group__n": "",
                "cluster_group_id": "",
                "cluster_group_id__n": "",
                "cluster_id": "",
                "cluster_id__n": "",
                "config_template_id": "",
                "config_template_id__n": "",
                "console_port_count": "",
                "console_port_count__empty": "",
                "console_port_count__gt": "",
                "console_port_count__gte": "",
                "console_port_count__lt": "",
                "console_port_count__lte": "",
                "console_port_count__n": "",
                "console_ports": "",
                "console_server_port_count": "",
                "console_server_port_count__empty": "",
                "console_server_port_count__gt": "",
                "console_server_port_count__gte": "",
                "console_server_port_count__lt": "",
                "console_server_port_count__lte": "",
                "console_server_port_count__n": "",
                "console_server_ports": "",
                "contact": "",
                "contact__n": "",
                "contact_group": "",
                "contact_group__n": "",
                "contact_role": "",
                "contact_role__n": "",
                "created": "",
                "created__empty": "",
                "created__gt": "",
                "created__gte": "",
                "created__lt": "",
                "created__lte": "",
                "created__n": "",
                "created_by_request": "",
                "description": "",
                "description__empty": "",
                "description__ic": "",
                "description__ie": "",
                "description__iew": "",
                "description__iregex": "",
                "description__isw": "",
                "description__n": "",
                "description__nic": "",
                "description__nie": "",
                "description__niew": "",
                "description__nisw": "",
                "description__regex": "",
                "device_bay_count": "",
                "device_bay_count__empty": "",
                "device_bay_count__gt": "",
                "device_bay_count__gte": "",
                "device_bay_count__lt": "",
                "device_bay_count__lte": "",
                "device_bay_count__n": "",
                "device_bays": "",
                "device_type": "",
                "device_type__n": "",
                "device_type_id": "",
                "device_type_id__n": "",
                "face": "",
                "face__empty": "",
                "face__ic": "",
                "face__ie": "",
                "face__iew": "",
                "face__iregex": "",
                "face__isw": "",
                "face__n": "",
                "face__nic": "",
                "face__nie": "",
                "face__niew": "",
                "face__nisw": "",
                "face__regex": "",
                "front_port_count": "",
                "front_port_count__empty": "",
                "front_port_count__gt": "",
                "front_port_count__gte": "",
                "front_port_count__lt": "",
                "front_port_count__lte": "",
                "front_port_count__n": "",
                "has_oob_ip": "",
                "has_primary_ip": "",
                "has_virtual_device_context": "",
                "id": "",
                "id__empty": "",
                "id__gt": "",
                "id__gte": "",
                "id__lt": "",
                "id__lte": "",
                "id__n": "",
                "interface_count": "",
                "interface_count__empty": "",
                "interface_count__gt": "",
                "interface_count__gte": "",
                "interface_count__lt": "",
                "interface_count__lte": "",
                "interface_count__n": "",
                "interfaces": "",
                "inventory_item_count": "",
                "inventory_item_count__empty": "",
                "inventory_item_count__gt": "",
                "inventory_item_count__gte": "",
                "inventory_item_count__lt": "",
                "inventory_item_count__lte": "",
                "inventory_item_count__n": "",
                "is_full_depth": "",
                "last_updated": "",
                "last_updated__empty": "",
                "last_updated__gt": "",
                "last_updated__gte": "",
                "last_updated__lt": "",
                "last_updated__lte": "",
                "last_updated__n": "",
                "latitude": "",
                "latitude__empty": "",
                "latitude__gt": "",
                "latitude__gte": "",
                "latitude__lt": "",
                "latitude__lte": "",
                "latitude__n": "",
                "limit": "",
                "local_context_data": "",
                "location": "",
                "location__n": "",
                "location_id": "",
                "location_id__n": "",
                "longitude": "",
                "longitude__empty": "",
                "longitude__gt": "",
                "longitude__gte": "",
                "longitude__lt": "",
                "longitude__lte": "",
                "longitude__n": "",
                "mac_address": "",
                "mac_address__ic": "",
                "mac_address__ie": "",
                "mac_address__iew": "",
                "mac_address__iregex": "",
                "mac_address__isw": "",
                "mac_address__n": "",
                "mac_address__nic": "",
                "mac_address__nie": "",
                "mac_address__niew": "",
                "mac_address__nisw": "",
                "mac_address__regex": "",
                "manufacturer": "",
                "manufacturer__n": "",
                "manufacturer_id": "",
                "manufacturer_id__n": "",
                "model": "",
                "model__n": "",
                "modified_by_request": "",
                "module_bay_count": "",
                "module_bay_count__empty": "",
                "module_bay_count__gt": "",
                "module_bay_count__gte": "",
                "module_bay_count__lt": "",
                "module_bay_count__lte": "",
                "module_bay_count__n": "",
                "module_bays": "",
                "name": "",
                "name__empty": "",
                "name__ic": "",
                "name__ie": "",
                "name__iew": "",
                "name__iregex": "",
                "name__isw": "",
                "name__n": "",
                "name__nic": "",
                "name__nie": "",
                "name__niew": "",
                "name__nisw": "",
                "name__regex": "",
                "offset": "",
                "oob_ip_id": "",
                "oob_ip_id__n": "",
                "ordering": "",
                "owner": "",
                "owner__n": "",
                "owner_group": "",
                "owner_group__n": "",
                "owner_group_id": "",
                "owner_group_id__n": "",
                "owner_id": "",
                "owner_id__n": "",
                "parent_bay_id": "",
                "parent_bay_id__n": "",
                "parent_device_id": "",
                "parent_device_id__n": "",
                "pass_through_ports": "",
                "platform": "",
                "platform__n": "",
                "platform_id": "",
                "platform_id__n": "",
                "position": "",
                "position__empty": "",
                "position__gt": "",
                "position__gte": "",
                "position__lt": "",
                "position__lte": "",
                "position__n": "",
                "power_outlet_count": "",
                "power_outlet_count__empty": "",
                "power_outlet_count__gt": "",
                "power_outlet_count__gte": "",
                "power_outlet_count__lt": "",
                "power_outlet_count__lte": "",
                "power_outlet_count__n": "",
                "power_outlets": "",
                "power_port_count": "",
                "power_port_count__empty": "",
                "power_port_count__gt": "",
                "power_port_count__gte": "",
                "power_port_count__lt": "",
                "power_port_count__lte": "",
                "power_port_count__n": "",
                "power_ports": "",
                "primary_ip4": "",
                "primary_ip4__n": "",
                "primary_ip4_id": "",
                "primary_ip4_id__n": "",
                "primary_ip6": "",
                "primary_ip6__n": "",
                "primary_ip6_id": "",
                "primary_ip6_id__n": "",
                "q": "",
                "rack_id": "",
                "rack_id__n": "",
                "rear_port_count": "",
                "rear_port_count__empty": "",
                "rear_port_count__gt": "",
                "rear_port_count__gte": "",
                "rear_port_count__lt": "",
                "rear_port_count__lte": "",
                "rear_port_count__n": "",
                "region": "",
                "region__n": "",
                "region_id": "",
                "region_id__n": "",
                "role": "",
                "role__n": "",
                "role_id": "",
                "role_id__n": "",
                "serial": "",
                "serial__empty": "",
                "serial__ic": "",
                "serial__ie": "",
                "serial__iew": "",
                "serial__iregex": "",
                "serial__isw": "",
                "serial__n": "",
                "serial__nic": "",
                "serial__nie": "",
                "serial__niew": "",
                "serial__nisw": "",
                "serial__regex": "",
                "site": "",
                "site__n": "",
                "site_group": "",
                "site_group__n": "",
                "site_group_id": "",
                "site_group_id__n": "",
                "site_id": "",
                "site_id__n": "",
                "start": "",
                "status": "",
                "status__empty": "",
                "status__ic": "",
                "status__ie": "",
                "status__iew": "",
                "status__iregex": "",
                "status__isw": "",
                "status__n": "",
                "status__nic": "",
                "status__nie": "",
                "status__niew": "",
                "status__nisw": "",
                "status__regex": "",
                "tag": "",
                "tag__n": "",
                "tag_id": "",
                "tag_id__n": "",
                "tenant": "",
                "tenant__n": "",
                "tenant_group": "",
                "tenant_group__n": "",
                "tenant_group_id": "",
                "tenant_group_id__n": "",
                "tenant_id": "",
                "tenant_id__n": "",
                "updated_by_request": "",
                "vc_position": "",
                "vc_position__empty": "",
                "vc_position__gt": "",
                "vc_position__gte": "",
                "vc_position__lt": "",
                "vc_position__lte": "",
                "vc_position__n": "",
                "vc_priority": "",
                "vc_priority__empty": "",
                "vc_priority__gt": "",
                "vc_priority__gte": "",
                "vc_priority__lt": "",
                "vc_priority__lte": "",
                "vc_priority__n": "",
                "virtual_chassis_id": "",
                "virtual_chassis_id__n": "",
                "virtual_chassis_member": "",
                "adapter_id": "NetBox-Itential-Lab"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -48,
              "y": -336
            }
          },
          "b532": {
            "name": "renderJinja2ContextWithCast",
            "canvasName": "renderJinja2ContextWithCast",
            "summary": "Inventory Payload",
            "description": "Renders jinja2 Context output with data cast.",
            "location": "Application",
            "locationType": null,
            "app": "TemplateBuilder",
            "type": "automatic",
            "displayName": "TemplateBuilder",
            "variables": {
              "incoming": {
                "template": "{#-\n  NetBox -> IAG5 Inventory Template \u2014 JUNOS / Hybrid\n  Filters: active Junos devices with an IP.\nAdjust as desired, make sure to set passwords with SECRETS\n-#}\n\n{% set junos_slugs = ['juniper-junos', 'vsrx'] %}\n\n{% set credentials = {'user': 'itential', 'password': 'password'} %}\n\n{% set device_overrides = {} %}\n\n{% set netmiko_opts = {\n    'banner_timeout':        60,\n    'session_timeout':       300,\n    'read_timeout_override': 600,\n    'conn_timeout':          60,\n    'global_delay_factor':   3,\n    'enable_fast_mode':      false\n} %}\n\n{% set netconf_opts = {\n    'port':               830,\n    'timeout':            30,\n    'lock_timeout':       60,\n    'lock_poll_interval': 2,\n    'command_timeout': 600,\n    'config_format':  'set'\n} %}\n\n[\n{%- set ns = namespace(first=true) %}\n{%- for device in body.results %}\n\n  {%- set nb_platform = (device.platform.slug if device.platform else device.device_type.slug) or '' %}\n\n  {%- if device.primary_ip4 %}\n    {%- set ip_address = device.primary_ip4.address.split('/')[0] %}\n  {%- elif device.config_context and device.config_context.ipAddress %}\n    {%- set ip_address = device.config_context.ipAddress %}\n  {%- else %}\n    {%- set ip_address = '' %}\n  {%- endif %}\n\n  {%- set creds = device_overrides.get(device.name, credentials) %}\n\n  {%- set driver_options = {'netmiko': netmiko_opts, 'netconf': netconf_opts} %}\n\n  {%- if ip_address and nb_platform in junos_slugs and device.status and device.status.value == 'active' %}\n{{ \",\" if not ns.first else \"\" }}\n{%- set ns.first = false %}\n  {\n    \"name\": \"{{ device.name }}\",\n    \"attributes\": {\n      \"itential_host\":           \"{{ ip_address }}\",\n      \"itential_port\":           22,\n      \"itential_driver\":         \"netmiko\",\n      \"itential_platform\":       \"juniper_junos\",\n      \"itential_user\":           \"{{ creds.user }}\",\n      \"itential_password\":       \"{{ creds.password }}\",\n      \"itential_driver_options\": {{ driver_options | tojson }}\n    },\n    \"tags\": [\n      \"{{ (device.role.slug if device.role else 'unknown') }}\",\n      \"{{ (device.site.slug if device.site else 'unknown') }}\",\n      \"{{ (device.status.value if device.status else 'unknown') }}\",\n      \"driver:netmiko\",\n      \"platform:juniper_junos\",\n      \"transport:cli+netconf\"\n    ]\n  }\n  {%- endif %}\n{%- endfor %}\n]\n",
                "variables": {},
                "castDataType": "object"
              },
              "outgoing": {
                "renderedTemplate": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -48,
              "y": -216
            }
          },
          "d628": {
            "name": "getInventoryByIdentifier",
            "canvasName": "getInventoryByIdentifier",
            "summary": "Get a single inventory by identifier",
            "description": "Returns a single inventory document by ID or name",
            "location": "Application",
            "locationType": null,
            "app": "InventoryManager",
            "type": "automatic",
            "displayName": "InventoryManager",
            "variables": {
              "incoming": {
                "identifier": "$var.job.inventoryName"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": -228,
              "y": -72
            }
          },
          "f091": {
            "name": "createInventory",
            "canvasName": "createInventory",
            "summary": "Create a new inventory",
            "description": "Creates a new inventory with the specified name and optional properties",
            "location": "Application",
            "locationType": null,
            "app": "InventoryManager",
            "type": "automatic",
            "displayName": "InventoryManager",
            "variables": {
              "incoming": {
                "name": "",
                "description": "JUNOS NETCONF Inventory",
                "groups": [
                  "admins"
                ],
                "tags": [
                  "JUNOS"
                ],
                "actions": [
                  {
                    "name": "run-command",
                    "action_type": "iag5-service",
                    "action_config": {
                      "service_name": "junos-netconf-run-command",
                      "cluster_id": "cluster-itential"
                    },
                    "action_parameters": {}
                  },
                  {
                    "name": "get-config",
                    "action_type": "iag5-service",
                    "action_config": {
                      "service_name": "junos-netconf-get-config",
                      "cluster_id": "cluster-itential"
                    },
                    "action_parameters": {}
                  },
                  {
                    "name": "set-config",
                    "action_type": "iag5-service",
                    "action_config": {
                      "service_name": "junos-netconf-set-config",
                      "cluster_id": "cluster-itential"
                    },
                    "action_parameters": {}
                  },
                  {
                    "name": "is-alive",
                    "action_type": "iag5-service",
                    "action_config": {
                      "service_name": "junos-netconf-is-alive",
                      "cluster_id": "cluster-itential"
                    },
                    "action_parameters": {}
                  }
                ],
                "createBrokerActions": true,
                "defaultClusterId": "cluster-itential"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 132,
              "y": -72
            }
          }
        },
        "transitions": {
          "7291": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_start": {
            "880d": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "880d": {
            "b532": {
              "state": "success",
              "type": "standard"
            }
          },
          "b532": {
            "d628": {
              "state": "success",
              "type": "standard"
            },
            "f091": {
              "state": "success",
              "type": "standard"
            }
          },
          "d628": {
            "7291": {
              "state": "success",
              "type": "standard"
            },
            "f091": {
              "state": "error",
              "type": "standard"
            }
          },
          "f091": {
            "7291": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "inventoryName": {
              "type": "string",
              "minLength": 1,
              "description": "The ID or name of the inventory to populate with nodes"
            }
          },
          "required": [
            "inventoryName"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "inventoryName": {
              "type": "string",
              "minLength": 1,
              "description": "The ID or name of the inventory to populate with nodes"
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            }
          }
        },
        "scenarios": [],
        "type": "automation",
        "font_size": 12,
        "last_updated": "2026-06-24T20:03:06.844Z",
        "lastUpdatedVersion": "4.69.69",
        "uuid": "512b9055-e2c8-4a17-b3f2-d34dd8f5afa5",
        "createdVersion": "5.55.5",
        "name": "Create & Update Inventory from NetBox",
        "last_updated_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 8
      }
    },
    {
      "iid": 40,
      "reference": "2494ad56-105b-44e6-96c8-6120b442f60d",
      "type": "workflow",
      "folder": "/Inventory Management",
      "document": {
        "tasks": {
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "x": 0,
            "y": 0.5,
            "nodeLocation": {
              "x": 0,
              "y": -420
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "x": 1,
            "y": 0.5,
            "nodeLocation": {
              "x": 0,
              "y": -24
            }
          },
          "e29b": {
            "name": "deleteInventory",
            "canvasName": "deleteInventory",
            "summary": "Delete an inventory",
            "description": "Deletes an inventory by ID",
            "location": "Application",
            "locationType": null,
            "app": "InventoryManager",
            "type": "automatic",
            "displayName": "InventoryManager",
            "variables": {
              "incoming": {
                "identifier": "$var.job.inventoryName"
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
          "1c0f": {
            "name": "clearInventory",
            "canvasName": "clearInventory",
            "summary": "Clear all nodes from an inventory",
            "description": "Removes all nodes from the specified inventory",
            "location": "Application",
            "locationType": null,
            "app": "InventoryManager",
            "type": "automatic",
            "displayName": "InventoryManager",
            "variables": {
              "incoming": {
                "identifier": "$var.job.inventoryName"
              },
              "outgoing": {
                "response": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -276
            }
          }
        },
        "transitions": {
          "workflow_start": {
            "1c0f": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "e29b": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "1c0f": {
            "e29b": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "inventoryName": {
              "title": "inventoryIdentifier",
              "description": "Inventory identifier - can be ObjectId or name",
              "oneOf": [
                {
                  "description": "A string which is formatted like an ObjectId",
                  "type": "string",
                  "pattern": "^[0-9a-fA-F]{24}$"
                },
                {
                  "type": "string",
                  "minLength": 1,
                  "description": "The name of the document",
                  "not": {
                    "description": "A string which is formatted like an ObjectId",
                    "type": "string",
                    "pattern": "^[0-9a-fA-F]{24}$"
                  }
                }
              ],
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            }
          },
          "required": [
            "inventoryName"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "inventoryName": {
              "title": "inventoryIdentifier",
              "description": "Inventory identifier - can be ObjectId or name",
              "oneOf": [
                {
                  "description": "A string which is formatted like an ObjectId",
                  "type": "string",
                  "pattern": "^[0-9a-fA-F]{24}$"
                },
                {
                  "type": "string",
                  "minLength": 1,
                  "description": "The name of the document",
                  "not": {
                    "description": "A string which is formatted like an ObjectId",
                    "type": "string",
                    "pattern": "^[0-9a-fA-F]{24}$"
                  }
                }
              ],
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            }
          }
        },
        "scenarios": [],
        "type": "automation",
        "font_size": 12,
        "last_updated": "2026-06-24T20:03:06.844Z",
        "lastUpdatedVersion": "4.69.69",
        "uuid": "970643a5-f94e-4bc8-a896-c93665f550c6",
        "createdVersion": "5.55.5",
        "name": "Clear & Delete Inventory",
        "last_updated_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 8
      }
    },
    {
      "iid": 44,
      "reference": "3e29ac6b-ef29-4728-b164-d4ab594526a6",
      "type": "workflow",
      "folder": "/Port Turn Up",
      "document": {
        "name": "Port Turn Up",
        "description": "make sure when this is called that the input is an object called formData. That formData object will have the following as it's JSON object {\n  \"device\": \"aws-lab-junos\",\n  \"target_version\": \"22.4R2.8\",\n  \"image_path\": \"/var/tmp/junos-install-vsrx3-x86-64-22.4R2.8.tgz\",\n  \"image_sha256\": \"8d486921598bb89afd3ab54dcf8fa7cb80423c3977ddaa86dd15e84f13d465b2\"\n}",
        "tasks": {
          "6476": {
            "name": "getDevice",
            "canvasName": "getDevice",
            "summary": "Get Device Details",
            "description": "Get detailed information for a specific device, based on its device name",
            "location": "Application",
            "locationType": null,
            "app": "ConfigurationManager",
            "type": "automatic",
            "displayName": "ConfigurationManager",
            "variables": {
              "incoming": {
                "name": "$var.job.device"
              },
              "outgoing": {
                "device": ""
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -360
            }
          },
          "workflow_start": {
            "name": "workflow_start",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -576
            }
          },
          "a2": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Port Turn Up Pre Check",
            "description": "Captures show version, system storage, interfaces, route summary",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Port Turn Up Pre Check",
                "variables": "$var.d009.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.preCheckOutput"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": -156
            }
          },
          "b1": {
            "name": "backUpDevice",
            "canvasName": "backUpDevice",
            "summary": "Backup Running Config (pre)",
            "description": "",
            "location": "Application",
            "locationType": null,
            "app": "ConfigurationManager",
            "type": "automatic",
            "displayName": "ConfigurationManager",
            "variables": {
              "incoming": {
                "name": "$var.job.device",
                "options": {}
              },
              "outgoing": {
                "status": null
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 84
            }
          },
          "workflow_end": {
            "name": "workflow_end",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 876
            }
          },
          "d768": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Pre-check",
            "description": "Run an evaluation",
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
                          "task": "a2",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -36
            }
          },
          "f215": {
            "name": "RunCommandTemplate",
            "canvasName": "RunCommandTemplate",
            "summary": "Post Check",
            "description": "Captures show version, system storage, interfaces, route summary",
            "location": "Application",
            "locationType": null,
            "app": "MOP",
            "type": "automatic",
            "displayName": "MOP",
            "variables": {
              "incoming": {
                "template": "@6a138e0000000000ffff0001: Port Turn Up Post Check",
                "variables": "$var.d009.merged_object",
                "devices": "$var.job.device"
              },
              "outgoing": {
                "mop_template_results": "$var.job.postCheckResults"
              },
              "error": "",
              "decorators": []
            },
            "groups": [],
            "actor": "Pronghorn",
            "scheduled": false,
            "nodeLocation": {
              "x": 0,
              "y": 648
            }
          },
          "6d1a": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Post-check",
            "description": "Run an evaluation",
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
                          "task": "f215",
                          "variable": "mop_template_results"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": "result",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 768
            }
          },
          "3cf3": {
            "name": "runService",
            "canvasName": "runService",
            "summary": "Send Config",
            "description": "Run an IAG5 service given its name and any parameters passed to the service itself.",
            "location": "Application",
            "locationType": null,
            "app": "GatewayManager",
            "type": "automatic",
            "displayName": "GatewayManager",
            "variables": {
              "incoming": {
                "serviceName": "junos-netconf-send-config",
                "clusterId": "cluster-itential",
                "params": {
                  "config": "$var.ac95.renderedTemplate",
                  "confirm_timeout": 10,
                  "confirmed": false,
                  "dry_run": false,
                  "lock_timeout": 30
                },
                "inventory": "$var.26a0.renderedTemplate"
              },
              "outgoing": {
                "result": ""
              },
              "decorators": []
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 300
            }
          },
          "ac95": {
            "name": "renderJinja2TemplateWithCast",
            "canvasName": "renderJinja2TemplateWithCast",
            "summary": "Render Jinja2 Template With Data Cast",
            "description": "Renders jinja2 template output with data cast.",
            "location": "Application",
            "locationType": null,
            "app": "TemplateBuilder",
            "type": "automatic",
            "displayName": "TemplateBuilder",
            "variables": {
              "incoming": {
                "name": "@6a138e0000000000ffff0001: 802.1Q Sub Interface",
                "variables": "$var.d009.merged_object",
                "castDataType": "string"
              },
              "outgoing": {
                "renderedTemplate": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 192
            }
          },
          "26a0": {
            "name": "renderJinja2ContextWithCast",
            "canvasName": "renderJinja2ContextWithCast",
            "summary": "Inventory Object",
            "description": "Renders jinja2 Context output with data cast.",
            "location": "Application",
            "locationType": null,
            "app": "TemplateBuilder",
            "type": "automatic",
            "displayName": "TemplateBuilder",
            "variables": {
              "incoming": {
                "template": "[\n  { \n    \"inventory\": \"{{name.split('::')[0]}}\",\n    \"nodeNames\": [\n        \"{{name.split('::')[1]}}\"\n    ]\n  }\n]",
                "variables": "$var.6476.device",
                "castDataType": "object"
              },
              "outgoing": {
                "renderedTemplate": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": -264
            }
          },
          "908f": {
            "name": "evaluation",
            "canvasName": "evaluation",
            "summary": "Eval Send Config",
            "description": "Run an evaluation",
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
                          "task": "962d",
                          "variable": "textObject"
                        },
                        "operand_2": {
                          "task": "static",
                          "variable": true
                        },
                        "operator": "==",
                        "query": ".success",
                        "rightQuery": ""
                      }
                    ]
                  }
                ],
                "options": ""
              },
              "outgoing": {
                "return_value": ""
              }
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 540
            }
          },
          "962d": {
            "name": "parse",
            "canvasName": "parse",
            "summary": "Parse stdout",
            "description": "Parses a JSON string, constructing the JavaScript value or object described by the string.",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "automatic",
            "displayName": "String",
            "variables": {
              "incoming": {
                "text": "$var.3cf3.result#/result/stdout"
              },
              "outgoing": {
                "textObject": ""
              },
              "decorators": [
                {
                  "type": "query",
                  "pointer": "/incoming/text",
                  "displayPath": ".result.stdout"
                }
              ]
            },
            "actor": "Pronghorn",
            "groups": [],
            "nodeLocation": {
              "x": 0,
              "y": 420
            }
          },
          "d009": {
            "name": "merge",
            "canvasName": "merge",
            "summary": "Variables Object",
            "description": "Merge data into a single object",
            "location": "Application",
            "locationType": null,
            "app": "WorkFlowEngine",
            "type": "operation",
            "displayName": "WorkFlowEngine",
            "variables": {
              "incoming": {
                "data_to_merge": [
                  {
                    "key": "device",
                    "value": {
                      "task": "job",
                      "variable": "device"
                    }
                  },
                  {
                    "key": "interface",
                    "value": {
                      "task": "job",
                      "variable": "interface"
                    }
                  },
                  {
                    "key": "vlan_id",
                    "value": {
                      "task": "job",
                      "variable": "vlan_id"
                    }
                  },
                  {
                    "key": "description",
                    "value": {
                      "task": "job",
                      "variable": "description"
                    }
                  },
                  {
                    "key": "ip_address",
                    "value": {
                      "task": "job",
                      "variable": "ip_address"
                    }
                  },
                  {
                    "key": "zone",
                    "value": {
                      "task": "job",
                      "variable": "zone"
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
              "x": 0,
              "y": -468
            }
          }
        },
        "transitions": {
          "6476": {
            "26a0": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_start": {
            "d009": {
              "state": "success",
              "type": "standard"
            }
          },
          "a2": {
            "d768": {
              "state": "success",
              "type": "standard"
            }
          },
          "b1": {
            "ac95": {
              "state": "success",
              "type": "standard"
            }
          },
          "workflow_end": {},
          "d768": {
            "b1": {
              "state": "success",
              "type": "standard"
            }
          },
          "f215": {
            "6d1a": {
              "state": "success",
              "type": "standard"
            }
          },
          "6d1a": {
            "workflow_end": {
              "state": "success",
              "type": "standard"
            }
          },
          "3cf3": {
            "962d": {
              "state": "success",
              "type": "standard"
            }
          },
          "ac95": {
            "3cf3": {
              "state": "success",
              "type": "standard"
            }
          },
          "26a0": {
            "a2": {
              "state": "success",
              "type": "standard"
            }
          },
          "908f": {
            "f215": {
              "state": "success",
              "type": "standard"
            }
          },
          "962d": {
            "908f": {
              "state": "success",
              "type": "standard"
            }
          },
          "d009": {
            "6476": {
              "state": "success",
              "type": "standard"
            }
          }
        },
        "inputSchema": {
          "type": "object",
          "properties": {
            "device": {
              "anyOf": [
                {
                  "title": "name",
                  "type": "string",
                  "examples": [
                    "xr9kv-atl"
                  ]
                },
                {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "examples": [
                      "Cisco ASA",
                      "Cisco NX-OS"
                    ]
                  }
                }
              ]
            },
            "interface": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "vlan_id": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "description": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "ip_address": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "zone": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            }
          },
          "required": [
            "device",
            "interface",
            "vlan_id",
            "description",
            "ip_address",
            "zone"
          ]
        },
        "outputSchema": {
          "type": "object",
          "properties": {
            "device": {
              "anyOf": [
                {
                  "title": "name",
                  "type": "string",
                  "examples": [
                    "xr9kv-atl"
                  ]
                },
                {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "examples": [
                      "Cisco ASA",
                      "Cisco NX-OS"
                    ]
                  }
                }
              ]
            },
            "interface": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "vlan_id": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "description": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "ip_address": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "zone": {
              "type": [
                "array",
                "boolean",
                "null",
                "number",
                "object",
                "string"
              ]
            },
            "_id": {
              "type": "string",
              "pattern": "^[0-9a-f]{24}$"
            },
            "initiator": {
              "type": "string"
            },
            "preCheckOutput": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            },
            "postCheckResults": {
              "type": "object",
              "properties": {
                "raw": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "all_pass_flag": {
                  "type": "boolean"
                },
                "evaluated": {
                  "type": "string",
                  "examples": [
                    "show version"
                  ]
                },
                "parameters": {
                  "type": "object",
                  "properties": {}
                },
                "rules": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "rule": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "eval": {
                        "type": "string",
                        "examples": [
                          "contains"
                        ]
                      },
                      "raw": {
                        "type": "string",
                        "examples": [
                          "show version"
                        ]
                      },
                      "result": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "rule",
                      "eval"
                    ]
                  }
                },
                "device": {
                  "type": "string",
                  "examples": [
                    "Nokia SR-OS"
                  ]
                },
                "response": {
                  "type": "string",
                  "examples": [
                    "version: 10.0.0"
                  ]
                },
                "result": {
                  "type": "boolean"
                }
              }
            }
          }
        },
        "scenarios": [],
        "type": "automation",
        "font_size": 12,
        "createdVersion": "6.4.0",
        "lastUpdatedVersion": "5.55.5",
        "last_updated": "2026-06-25T09:16:13.314Z",
        "preAutomationTime": 0,
        "sla": 0,
        "uuid": "9769f0c9-2da1-4061-a009-1c1459849733",
        "last_updated_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "created": "1970-01-01T00:00:00.000Z",
        "canvasVersion": 3,
        "created_by": {
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false
        },
        "tags": [],
        "groups": [],
        "migrationVersion": 8
      }
    },
    {
      "iid": 45,
      "reference": "6a1e30c698f25fd9d4056ca4",
      "type": "template",
      "folder": "/Port Turn Up",
      "document": {
        "_id": "6a1e30c698f25fd9d4056ca4",
        "name": "802.1Q Sub Interface",
        "type": "jinja2",
        "command": "",
        "template": "set interfaces {{ interface }} vlan-tagging\nset interfaces {{ interface }} unit {{ vlan_id }} description \"{{ description }}\"\nset interfaces {{ interface }} unit {{ vlan_id }} vlan-id {{ vlan_id }}\nset interfaces {{ interface }} unit {{ vlan_id }} family inet address {{ ip_address }}\nset security zones security-zone {{ zone }} interfaces {{ interface }}.{{ vlan_id }}\n",
        "data": "{\n  \"interface\": \"ge-0/0/0\",\n  \"vlan_id\": 100,\n  \"description\": \"CORP LAN\",\n  \"ip_address\": \"192.168.100.1/24\",\n  \"zone\": \"trust\"\n}\n",
        "group": "Juniper JUNOS",
        "description": "",
        "version": 1,
        "created": "2026-06-02T01:24:22.337Z",
        "lastUpdated": "2026-06-24T20:03:06.837Z",
        "createdBy": {
          "_id": "6a3c303cdd8730559c46dc8b",
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false,
          "email": "mike.elrom@itential.com"
        },
        "lastUpdatedBy": {
          "_id": "6a3c303cdd8730559c46dc8b",
          "provenance": "CloudAAA",
          "username": "mike.elrom@itential.com",
          "firstname": "Mike",
          "inactive": false,
          "email": "mike.elrom@itential.com"
        }
      }
    }
  ],
  "created": "2026-05-24T23:30:00.000Z",
  "createdBy": {
    "_id": "6a3c303cdd8730559c46dc8b",
    "provenance": "CloudAAA",
    "username": "mike.elrom@itential.com"
  },
  "lastUpdated": "2026-06-30T12:03:25.471Z",
  "lastUpdatedBy": {
    "_id": "6a3c303cdd8730559c46dc8b",
    "provenance": "CloudAAA",
    "username": "mike.elrom@itential.com"
  },
  "folders": [
    {
      "nodeType": "folder",
      "name": "Inventory Management",
      "children": [
        {
          "iid": 39,
          "nodeType": "component"
        },
        {
          "iid": 40,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Software Upgrade",
      "children": [
        {
          "iid": 22,
          "nodeType": "component"
        },
        {
          "iid": 33,
          "nodeType": "component"
        },
        {
          "iid": 31,
          "nodeType": "component"
        },
        {
          "iid": 27,
          "nodeType": "component"
        },
        {
          "iid": 32,
          "nodeType": "component"
        },
        {
          "iid": 36,
          "nodeType": "component"
        },
        {
          "iid": 30,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Golden Configuration",
      "children": [
        {
          "iid": 42,
          "nodeType": "component"
        },
        {
          "iid": 38,
          "nodeType": "component"
        }
      ]
    },
    {
      "nodeType": "folder",
      "name": "Port Turn Up",
      "children": [
        {
          "iid": 46,
          "nodeType": "component"
        },
        {
          "iid": 44,
          "nodeType": "component"
        },
        {
          "iid": 47,
          "nodeType": "component"
        },
        {
          "iid": 45,
          "nodeType": "component"
        },
        {
          "iid": 48,
          "nodeType": "component"
        }
      ]
    }
  ],
  "iid": 5,
  "thumbnail": "",
  "backgroundColor": "#FFFFFF",
  "referencedComponentHashes": [
    {
      "type": "automation",
      "reference": "6a13a94c84f0ff3625737607",
      "name": "JUNOS Software Upgrade",
      "hash": "4f4a11f259a6f112431a7b3a82b5165a3ad46805"
    },
    {
      "type": "automation",
      "reference": "6a1de1efc48aa7c8f6876601",
      "name": "JUNOS Compliance",
      "hash": "ea95339ad5a4a9f6d040347ad59742160403c756"
    },
    {
      "type": "trigger",
      "reference": "6a13a94c84f0ff3625737608",
      "name": "JUNOS Upgrade",
      "hash": "5e9c74418df6c7b1c6ce201e119b61694ff2157a"
    },
    {
      "type": "automation",
      "reference": "6a1e409ac48aa7c8f6876603",
      "name": "JUNOS Port Turn Up",
      "hash": "0c05f69e55ccb75738d500b9dbf81ccdd24bec5f"
    },
    {
      "type": "trigger",
      "reference": "6a1de360c48aa7c8f6876602",
      "name": "Version",
      "hash": "01132025fff4f6049f1a0adf4f89f5fcf7602dd7"
    },
    {
      "type": "trigger",
      "reference": "6a1e40afc48aa7c8f6876604",
      "name": "Port Turn Up",
      "hash": "b9658d1ae385811dde0be0a47d6f55f13a642237"
    }
  ]
}

````
