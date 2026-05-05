# AI Native Factory V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the implementation baseline for AI Native Factory V1 so a real historical machining order can move from order/drawing to quote/DFM, process/CAPP/CAM, Operation Execution Package, simulation/approval, validation-machine execution, traceback, and learning.

**Architecture:** Operation Execution Package is the system spine and production fact contract. Agent Runtime produces structured recommendations and DecisionLog records, while Machine Physical Agent gives the validation machine sensing, edge judgment, controlled actions, and trace write-back. Phase 0 freezes semantics and samples; Phase 1 proves one validation machine; Phase 2 copies to three machines; Phase 3 scales the same pattern toward about twenty machining devices.

**Tech Stack:** Markdown architecture artifacts, JSON Schema Draft 2020-12, OpenAPI-style interface sketches, PowerShell verification commands, Git, future integration targets including CNC/PLC interfaces, OPC UA or MTConnect, CAM outputs, edge IPC, industrial sensors, HMI/scanner devices, and event storage.

---

## Scope

This plan turns the approved architecture into an executable artifact set. The first implementation milestone is not a full factory application; it is a coherent baseline that lets engineering, software, edge hardware, process, and operations teams build the same V1.

The implementation sequence is deliberately artifact-first:

1. Freeze the contract vocabulary.
2. Define the Operation Execution Package schema and lifecycle.
3. Define the minimum object model and event envelope.
4. Define Agent contracts and DecisionLog.
5. Define Machine Physical Agent hardware/software interface.
6. Define the quote/process knowledge base structure.
7. Define the first-order Demo runbook.
8. Define acceptance gates for Phase 0, Phase 1, Phase 2, and Phase 3.

## File Structure

Create these files as the implementation baseline:

- `docs/ai-native-factory-v1/README.md`: index and reading order.
- `docs/ai-native-factory-v1/00-program-charter.md`: mission, boundaries, phases, governance.
- `docs/ai-native-factory-v1/01-oep-schema.md`: human-readable Operation Execution Package definition.
- `docs/ai-native-factory-v1/02-object-model-v1.md`: minimum object model and relationships.
- `docs/ai-native-factory-v1/03-event-catalog.md`: event envelope and V1 event catalog.
- `docs/ai-native-factory-v1/04-agent-contracts.md`: Agent Runtime contract, four decision agents, DecisionLog.
- `docs/ai-native-factory-v1/05-machine-physical-agent-spec.md`: cyber-physical agent capability model.
- `docs/ai-native-factory-v1/06-validation-machine-bom-and-interfaces.md`: first validation machine sensing, edge, interface, and safety boundary.
- `docs/ai-native-factory-v1/07-quote-and-process-knowledge-base.md`: quotation rules, process templates, and knowledge capture.
- `docs/ai-native-factory-v1/08-first-order-demo-runbook.md`: end-to-end first-order execution script.
- `docs/ai-native-factory-v1/09-phase-1-acceptance-checklist.md`: measurable Phase 0 and Phase 1 acceptance.
- `docs/ai-native-factory-v1/10-phase-2-3-expansion-plan.md`: three-machine and twenty-machine expansion rules.
- `schemas/oep/v1/operation-execution-package.schema.json`: machine-readable OEP schema.
- `schemas/events/v1/event-envelope.schema.json`: machine-readable event envelope schema.
- `schemas/agents/v1/agent-contract.schema.json`: machine-readable Agent contract schema.
- `schemas/machine-agent/v1/machine-physical-agent.interface.json`: Machine Physical Agent interface contract.

Use the approved design as the source of truth:

- Read: `docs/superpowers/specs/2026-05-06-ai-native-factory-v1-architecture-design.md`

## Task 1: Scaffold The V1 Artifact Set

**Files:**
- Create: `docs/ai-native-factory-v1/README.md`
- Create directories: `docs/ai-native-factory-v1`, `schemas/oep/v1`, `schemas/events/v1`, `schemas/agents/v1`, `schemas/machine-agent/v1`

- [ ] **Step 1: Create directories**

Run:

```powershell
New-Item -ItemType Directory -Force -Path `
  'docs/ai-native-factory-v1', `
  'schemas/oep/v1', `
  'schemas/events/v1', `
  'schemas/agents/v1', `
  'schemas/machine-agent/v1'
```

Expected: PowerShell prints directory entries or returns without error. All five paths exist.

- [ ] **Step 2: Create the README**

Create `docs/ai-native-factory-v1/README.md` with this content:

```markdown
# AI Native Factory V1 Implementation Baseline

This folder contains the executable baseline for AI Native Factory V1.

Read in this order:

1. `00-program-charter.md`
2. `01-oep-schema.md`
3. `02-object-model-v1.md`
4. `03-event-catalog.md`
5. `04-agent-contracts.md`
6. `05-machine-physical-agent-spec.md`
7. `06-validation-machine-bom-and-interfaces.md`
8. `07-quote-and-process-knowledge-base.md`
9. `08-first-order-demo-runbook.md`
10. `09-phase-1-acceptance-checklist.md`
11. `10-phase-2-3-expansion-plan.md`

The system spine is Operation Execution Package. Agent output must become structured DecisionLog and object updates. Machine Physical Agent must execute only approved actions and write trace evidence back to the OEP.
```

- [ ] **Step 3: Verify scaffold**

Run:

```powershell
Test-Path 'docs/ai-native-factory-v1/README.md'
Test-Path 'schemas/oep/v1'
Test-Path 'schemas/events/v1'
Test-Path 'schemas/agents/v1'
Test-Path 'schemas/machine-agent/v1'
```

Expected:

```text
True
True
True
True
True
```

- [ ] **Step 4: Commit scaffold**

Run:

```powershell
git add docs/ai-native-factory-v1/README.md schemas
git commit -m "docs: scaffold AI native factory v1 baseline"
```

Expected: Git creates one commit containing the README. Empty schema directories are not represented by Git; the schema tasks create tracked files inside those directories.

## Task 2: Write Program Charter And Phase Control

**Files:**
- Create: `docs/ai-native-factory-v1/00-program-charter.md`

- [ ] **Step 1: Write the charter**

Create `docs/ai-native-factory-v1/00-program-charter.md` with these sections and decisions:

```markdown
# 00 Program Charter

## Mission

AI Native Factory V1 proves that a real machining order can be governed by Operation Execution Package and improved by Agent workflow while a validation machine executes controlled physical actions through Machine Physical Agent.

## First Practical Phase

- Order type: real historical order.
- Part type: mainly simple plates, brackets, fixtures, simple housings, with a small number of medium-complexity cases.
- Physical scope: one validation machine first, then three-machine cell, then about twenty machining devices.
- Human scope: human-assisted logistics, tool preparation, fixture preparation, CAM confirmation, and quality inspection.
- System authority: record, recommend, gate/release, and controlled execution after human approval.

## V1 Main Flow

Order/drawing -> quote/DFM -> process/CAPP/CAM -> Operation Execution Package -> simulation/approval -> validation-machine execution -> quality/exception write-back -> knowledge capture.

## Product Kernel

- Object Service
- Operation Execution Package Service
- Event Bus
- Agent Runtime

## Agent Set

- Intake / DFM / Quote Agent
- Process Agent
- Package / Gate Agent
- Execution / Trace Agent

## Physical Agent Set

The first Machine Physical Agent is the validation machine. It has body, sensors, nervous system, edge brain, reflex loop, and OEP interface.

## Non-Goals For Phase 1

- No autonomous CNC cycle start.
- No AI direct edit-and-run of NC programs.
- No Feed Override closed loop.
- No full ERP, MES, WMS, or QMS replacement.
- No full ontology platform before the OEP, event, and object contracts are stable.

## Governance Rules

- OEP is the production fact contract.
- Agent proposals have no production authority until approved and recorded.
- High-risk actions require Gate plus human approval.
- Real-time safety remains with CNC, PLC, and safety PLC.
- Every physical command must link to OEP, approval, actor, result, and exception record.

## Phase Plan

| Phase | Goal | Exit Evidence |
|---|---|---|
| Phase 0 | Freeze semantics and run offline first-order chain | Quote draft, process draft, OEP draft, Machine Physical Agent BOM |
| Phase 1 | Prove one validation-machine first-order loop | Released OEP, controlled execution, quality write-back, DecisionLog replay |
| Phase 2 | Copy to three-machine cell | Resource conflicts, multi-machine OEP trace, deployable machine-agent template |
| Phase 3 | Scale toward about twenty machining devices | Standardized machine-agent rollout, operation governance, cross-resource coordination |
```

- [ ] **Step 2: Verify charter coverage**

Run:

```powershell
rg -n "Operation Execution Package|Machine Physical Agent|Quote Agent|Process Agent|Package / Gate Agent|Execution / Trace Agent|Phase 0|Phase 1|Phase 2|Phase 3" docs/ai-native-factory-v1/00-program-charter.md
```

Expected: At least one match for each listed concept.

- [ ] **Step 3: Commit charter**

Run:

```powershell
git add docs/ai-native-factory-v1/00-program-charter.md
git commit -m "docs: define AI native factory v1 charter"
```

Expected: Git creates one commit for the charter.

## Task 3: Define Operation Execution Package

**Files:**
- Create: `docs/ai-native-factory-v1/01-oep-schema.md`
- Create: `schemas/oep/v1/operation-execution-package.schema.json`

- [ ] **Step 1: Write the human-readable OEP contract**

Create `docs/ai-native-factory-v1/01-oep-schema.md` with these sections:

```markdown
# 01 Operation Execution Package Schema

## Definition

Operation Execution Package is the executable industrial contract for one operation, one setup, and one machine execution context.

OEP is not a file folder. It is a releaseable, executable, auditable, and write-back-capable production fact.

## Package Levels

| Level | Name | Role | Directly Executable |
|---|---|---|---|
| L0 | Order Mission Package | Order or project delivery target | No |
| L1 | Part Lot Package | Manufacturing package for one part lot | No |
| L2 | Operation Execution Package | Operation/setup/machine execution unit | Yes |
| L3 | Auxiliary Execution Package | Tool, fixture, transport, or inspection task | Indirect |

V1 implements L2 as the production-grade unit. L0 and L1 exist as aggregation and trace views.

## Required Sections

### Plan

Plan contains order reference, part reference, operation reference, resources, quality requirements, and linked engineering artifacts.

### Gate

Gate contains engineering version check, resource kitting, tool life, fixture confirmation, simulation, quality readiness, and authority approval.

### Trace

Trace contains execution records, measurement results, exceptions, command records, and DecisionLog references.

## Lifecycle

Draft -> EngineeringReady -> ResourceChecked -> Simulated -> Approved -> Released -> Staged -> Executing -> Paused -> Completed -> Archived

Allowed exception loops:

- Paused -> Executing
- Paused -> ReworkRequired
- ReworkRequired -> Draft
- Released -> Cancelled

## Release Gates

| Gate | Blocks Release When |
|---|---|
| Engineering Gate | Drawing, CAD, process, setup, or NC versions conflict |
| Resource Gate | Machine, tool, fixture, pallet, operator, or material is unavailable |
| Tool Gate | Tool identity, tool life, geometry, or offset is missing |
| Fixture Gate | Fixture, pallet, or clamping confirmation is missing |
| Simulation Gate | Simulation or interference check is missing or failed |
| Quality Gate | Inspection plan or critical characteristics are missing |
| Authority Gate | Approval, authority, or risk record is missing |

## Human Card Rendering

The OEP must render to an operation card with these fields:

- Order and part
- Drawing and CAD version
- Operation and setup
- Machine, NC program, fixture, pallet, tool assemblies
- Critical characteristics and inspection plan
- Gate status
- Operator checklist
- Execution trace
- Exceptions and final disposition

## Change Rule

Human edits become structured diff records. Agent recommendations become DecisionLog records. Neither may silently overwrite released facts.
```

- [ ] **Step 2: Write the JSON Schema**

Create `schemas/oep/v1/operation-execution-package.schema.json` with this content:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ai-native-factory.local/schemas/oep/v1/operation-execution-package.schema.json",
  "title": "OperationExecutionPackage",
  "type": "object",
  "required": ["package_id", "package_type", "schema_version", "status", "parent_refs", "plan", "gate", "trace"],
  "properties": {
    "package_id": { "type": "string", "pattern": "^OEP-[A-Z0-9-]+$" },
    "package_type": { "const": "OperationExecutionPackage" },
    "schema_version": { "const": "1.0" },
    "status": {
      "type": "string",
      "enum": ["Draft", "EngineeringReady", "ResourceChecked", "Simulated", "Approved", "Released", "Staged", "Executing", "Paused", "ReworkRequired", "Completed", "Archived", "Cancelled"]
    },
    "parent_refs": {
      "type": "object",
      "required": ["order_mission_package_id", "part_lot_package_id"],
      "properties": {
        "order_mission_package_id": { "type": "string" },
        "part_lot_package_id": { "type": "string" }
      },
      "additionalProperties": false
    },
    "plan": {
      "type": "object",
      "required": ["order_ref", "part_ref", "operation_ref", "resources", "quality"],
      "properties": {
        "order_ref": {
          "type": "object",
          "required": ["customer_order_id", "quotation_id"],
          "properties": {
            "customer_order_id": { "type": "string" },
            "quotation_id": { "type": "string" }
          },
          "additionalProperties": false
        },
        "part_ref": {
          "type": "object",
          "required": ["part_id", "drawing_id", "cad_model_id"],
          "properties": {
            "part_id": { "type": "string" },
            "drawing_id": { "type": "string" },
            "cad_model_id": { "type": "string" }
          },
          "additionalProperties": false
        },
        "operation_ref": {
          "type": "object",
          "required": ["process_plan_id", "operation_id", "setup_plan_id", "nc_program_id"],
          "properties": {
            "process_plan_id": { "type": "string" },
            "operation_id": { "type": "string" },
            "setup_plan_id": { "type": "string" },
            "nc_program_id": { "type": "string" }
          },
          "additionalProperties": false
        },
        "resources": {
          "type": "object",
          "required": ["machine_id", "tool_assembly_ids", "fixture_id", "pallet_id", "operator_skill_required"],
          "properties": {
            "machine_id": { "type": "string" },
            "tool_assembly_ids": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
            "fixture_id": { "type": "string" },
            "pallet_id": { "type": "string" },
            "operator_skill_required": { "type": "array", "items": { "type": "string" } }
          },
          "additionalProperties": false
        },
        "quality": {
          "type": "object",
          "required": ["inspection_plan_id", "critical_characteristics"],
          "properties": {
            "inspection_plan_id": { "type": "string" },
            "critical_characteristics": { "type": "array", "items": { "type": "string" }, "minItems": 1 }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    },
    "gate": {
      "type": "object",
      "required": ["engineering_version_consistency", "resource_kitting", "tool_life", "fixture_and_pallet_confirmed", "simulation", "quality_plan_ready", "authority_approval"],
      "properties": {
        "engineering_version_consistency": { "$ref": "#/$defs/gateStatus" },
        "resource_kitting": { "$ref": "#/$defs/gateStatus" },
        "tool_life": { "$ref": "#/$defs/gateStatus" },
        "fixture_and_pallet_confirmed": { "$ref": "#/$defs/gateStatus" },
        "simulation": { "$ref": "#/$defs/gateStatus" },
        "quality_plan_ready": { "$ref": "#/$defs/gateStatus" },
        "authority_approval": { "$ref": "#/$defs/gateStatus" }
      },
      "additionalProperties": false
    },
    "trace": {
      "type": "object",
      "required": ["execution_records", "measurement_results", "exceptions", "command_records", "decision_log_refs"],
      "properties": {
        "execution_records": { "type": "array", "items": { "type": "object" } },
        "measurement_results": { "type": "array", "items": { "type": "object" } },
        "exceptions": { "type": "array", "items": { "type": "object" } },
        "command_records": { "type": "array", "items": { "type": "object" } },
        "decision_log_refs": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false,
  "$defs": {
    "gateStatus": {
      "type": "string",
      "enum": ["pending", "passed", "failed", "waived", "required"]
    }
  }
}
```

- [ ] **Step 3: Verify JSON parses**

Run:

```powershell
Get-Content -Raw 'schemas/oep/v1/operation-execution-package.schema.json' | ConvertFrom-Json | Out-Null
```

Expected: no output and exit code 0.

- [ ] **Step 4: Verify OEP terms**

Run:

```powershell
rg -n "Plan|Gate|Trace|DecisionLog|Human Card|L2|Release Gates" docs/ai-native-factory-v1/01-oep-schema.md
```

Expected: matches for all listed terms.

- [ ] **Step 5: Commit OEP contract**

Run:

```powershell
git add docs/ai-native-factory-v1/01-oep-schema.md schemas/oep/v1/operation-execution-package.schema.json
git commit -m "docs: define operation execution package contract"
```

Expected: Git creates one commit for the OEP contract and JSON Schema.

## Task 4: Define Object Model And Event Catalog

**Files:**
- Create: `docs/ai-native-factory-v1/02-object-model-v1.md`
- Create: `docs/ai-native-factory-v1/03-event-catalog.md`
- Create: `schemas/events/v1/event-envelope.schema.json`

- [ ] **Step 1: Write the object model**

Create `docs/ai-native-factory-v1/02-object-model-v1.md` with these object groups:

```markdown
# 02 Object Model V1

## Rule

Objects are versioned production facts. Agents, OEP, events, HMI, and Machine Physical Agent must reference objects by id and version.

## Business Objects

| Object | Required Identity | Required State |
|---|---|---|
| CustomerOrder | customer_order_id | received, quoted, accepted, closed |
| Quotation | quotation_id, version | draft, human_reviewed, committed |

## Engineering Objects

| Object | Required Identity | Required State |
|---|---|---|
| Part | part_id, version | active, superseded |
| Drawing | drawing_id, revision | received, checked, released |
| CADModel | cad_model_id, revision | received, checked, released |
| ManufacturingFeature | feature_id | detected, confirmed, rejected |

## Process Objects

| Object | Required Identity | Required State |
|---|---|---|
| ProcessPlan | process_plan_id, version | draft, reviewed, released |
| Operation | operation_id | draft, reviewed, released |
| SetupPlan | setup_plan_id | draft, reviewed, released |
| Toolpath | toolpath_id, version | generated, simulated, approved |
| NCProgram | nc_program_id, version | generated, simulated, approved, bound |

## Execution Objects

| Object | Required Identity | Required State |
|---|---|---|
| OperationExecutionPackage | package_id | OEP lifecycle states |
| ExecutionRecord | execution_record_id | started, paused, completed, aborted |
| Event | event_id | recorded |
| Exception | exception_id | open, contained, closed |

## Resource Objects

| Object | Required Identity | Required State |
|---|---|---|
| Machine | machine_id | available, staged, executing, maintenance, down |
| WorkCenter | work_center_id | active, inactive |
| Operator | operator_id | available, assigned, unavailable |

## Tooling And Material Objects

| Object | Required Identity | Required State |
|---|---|---|
| ToolAssembly | tool_assembly_id | available, in_use, worn, blocked |
| Fixture | fixture_id | available, staged, in_use, blocked |
| Pallet | pallet_id | available, staged, in_use |
| MaterialLot | material_lot_id | received, released, consumed, blocked |
| Inventory | inventory_id | available, reserved, consumed |
| StorageLocation | storage_location_id | active, blocked |

## Quality Objects

| Object | Required Identity | Required State |
|---|---|---|
| InspectionPlan | inspection_plan_id, version | draft, released |
| MeasurementResult | measurement_result_id | captured, reviewed, accepted, rejected |
| QualityEvent | quality_event_id | open, dispositioned, closed |

## Intelligence Objects

| Object | Required Identity | Required State |
|---|---|---|
| Agent | agent_id, version | active, retired |
| Decision | decision_id | proposed, accepted, modified, rejected |
| KnowledgeItem | knowledge_item_id, version | candidate, approved, retired |
| Model | model_id, version | active, retired |

## Required Relationships

- CustomerOrder has many Part.
- Part has many Drawing, CADModel, ProcessPlan, and OperationExecutionPackage.
- OperationExecutionPackage references exactly one Operation, one SetupPlan, one Machine, one NCProgram, one Fixture, and one Pallet.
- OperationExecutionPackage references one or more ToolAssembly.
- ExecutionRecord belongs to one OperationExecutionPackage.
- MeasurementResult belongs to one InspectionPlan and one OperationExecutionPackage.
- Decision belongs to one Agent and may affect objects, OEP, events, or knowledge items.
```

- [ ] **Step 2: Write the event catalog**

Create `docs/ai-native-factory-v1/03-event-catalog.md` with these sections:

```markdown
# 03 Event Catalog

## Event Rule

Events are facts that have happened. Commands request action; events record command outcomes and object state changes.

## Envelope Fields

- event_id
- event_type
- source
- subject
- time
- schema_version
- correlation_id
- causation_id
- actor
- payload

## V1 Event Types

| Event Type | Source | Subject | Meaning |
|---|---|---|---|
| Order.Received | Object Service | CustomerOrder | A historical or live order entered the system |
| Drawing.Registered | Object Service | Drawing | A drawing revision was registered |
| Quote.Proposed | Intake / DFM / Quote Agent | Quotation | A budget-level quotation was proposed |
| Quote.HumanReviewed | HMI | Quotation | A human reviewed quotation assumptions |
| ProcessPlan.Proposed | Process Agent | ProcessPlan | A process route was proposed |
| ProcessPlan.HumanReviewed | HMI | ProcessPlan | A process engineer reviewed the route |
| OEP.Drafted | Package / Gate Agent | OperationExecutionPackage | An OEP draft was generated |
| OEP.GateChecked | OEP Service | OperationExecutionPackage | One or more gates were evaluated |
| OEP.Approved | HMI | OperationExecutionPackage | A human approved the OEP |
| OEP.Released | OEP Service | OperationExecutionPackage | The OEP entered release state |
| MachineAgent.CommandRequested | Agent Runtime or HMI | Machine Physical Agent | A controlled command was requested |
| MachineAgent.CommandExecuted | Machine Physical Agent | OperationExecutionPackage | A controlled command finished with result |
| MachineAgent.FeedHoldTriggered | Machine Physical Agent | Machine | Feed Hold or protective stop was triggered |
| Inspection.ResultCaptured | Machine Physical Agent or Quality HMI | MeasurementResult | Measurement result was captured |
| Exception.Opened | Any service | Exception | An abnormal condition was opened |
| Exception.Closed | HMI or Agent Runtime | Exception | An abnormal condition was closed |
| Decision.Recorded | Agent Runtime | Decision | A structured agent decision was stored |
| Knowledge.CandidateCreated | Agent Runtime | KnowledgeItem | A reusable rule or template candidate was created |

## Idempotency Rule

The pair `event_id` and `source` is unique. Consumers must ignore repeated delivery of the same event.
```

- [ ] **Step 3: Write the event envelope schema**

Create `schemas/events/v1/event-envelope.schema.json` with this content:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ai-native-factory.local/schemas/events/v1/event-envelope.schema.json",
  "title": "EventEnvelope",
  "type": "object",
  "required": ["event_id", "event_type", "source", "subject", "time", "schema_version", "correlation_id", "actor", "payload"],
  "properties": {
    "event_id": { "type": "string", "pattern": "^EVT-[A-Z0-9-]+$" },
    "event_type": { "type": "string" },
    "source": { "type": "string" },
    "subject": { "type": "string" },
    "time": { "type": "string", "format": "date-time" },
    "schema_version": { "const": "1.0" },
    "correlation_id": { "type": "string" },
    "causation_id": { "type": ["string", "null"] },
    "actor": {
      "type": "object",
      "required": ["type", "id"],
      "properties": {
        "type": { "type": "string", "enum": ["human", "agent", "service", "machine"] },
        "id": { "type": "string" }
      },
      "additionalProperties": false
    },
    "payload": { "type": "object" }
  },
  "additionalProperties": false
}
```

- [ ] **Step 4: Verify event artifacts**

Run:

```powershell
Get-Content -Raw 'schemas/events/v1/event-envelope.schema.json' | ConvertFrom-Json | Out-Null
rg -n "OEP.GateChecked|MachineAgent.CommandExecuted|Decision.Recorded|Knowledge.CandidateCreated" docs/ai-native-factory-v1/03-event-catalog.md
```

Expected: JSON parses; search returns all four event types.

- [ ] **Step 5: Commit object and event contracts**

Run:

```powershell
git add docs/ai-native-factory-v1/02-object-model-v1.md docs/ai-native-factory-v1/03-event-catalog.md schemas/events/v1/event-envelope.schema.json
git commit -m "docs: define factory object model and events"
```

Expected: Git creates one commit for object model and event catalog.

## Task 5: Define Agent Runtime Contracts

**Files:**
- Create: `docs/ai-native-factory-v1/04-agent-contracts.md`
- Create: `schemas/agents/v1/agent-contract.schema.json`

- [ ] **Step 1: Write Agent Runtime document**

Create `docs/ai-native-factory-v1/04-agent-contracts.md` with this content:

```markdown
# 04 Agent Contracts

## Runtime Rule

Agents do not become the production fact spine. Agents propose structured decisions. Object Service, OEP Service, Event Bus, and human approval determine production state.

## Required Agent Output

Every decision agent output must include:

- decision_id
- agent_id
- agent_version
- decision_type
- target_refs
- recommendation
- evidence_refs
- assumptions
- risk_level
- required_approval
- affected_objects
- proposed_events
- adoption_status
- reviewer
- review_notes

## DecisionLog Status

| Status | Meaning |
|---|---|
| proposed | Agent made a recommendation |
| accepted | Human or rule accepted it without material change |
| modified | Human changed it before adoption |
| rejected | Human rejected it |
| expired | Recommendation no longer applies |

## Agents

### Intake / DFM / Quote Agent

Responsibilities:

- Parse order, drawing, CAD metadata, and historical records.
- Identify DFM risk, cost assumptions, material assumptions, process complexity, and delivery risk.
- Propose budget-level quote structure.

Output objects:

- Quotation
- Decision
- KnowledgeItem candidate

Human approval:

- Required for committed quote.

### Process Agent

Responsibilities:

- Propose process route from templates and expert rules.
- Propose machine, tool, fixture, setup, and inspection strategy.
- Explain differences from historical cases.

Output objects:

- ProcessPlan
- Operation
- SetupPlan
- Decision

Human approval:

- Required for released process route.

### Package / Gate Agent

Responsibilities:

- Generate OEP draft.
- Check Engineering, Resource, Tool, Fixture, Simulation, Quality, and Authority gates.
- Block release when required evidence is missing.

Output objects:

- OperationExecutionPackage
- Decision
- Event proposals

Human approval:

- Required before OEP Approved and Released.

### Execution / Trace Agent

Responsibilities:

- Monitor OEP execution trace.
- Summarize measurement, exception, command, and machine-state records.
- Suggest knowledge updates after execution.

Output objects:

- ExecutionRecord summary
- Exception summary
- KnowledgeItem candidate
- Decision

Human approval:

- Required for knowledge promotion and quality disposition.

## Tool Permission Levels

| Level | Capability | Human Approval |
|---|---|---|
| Record | Read/write non-release facts | Not required inside assigned workflow |
| Recommend | Create DecisionLog proposals | Not required |
| Gate | Mark gate pass/fail with evidence | Required for waive and release |
| Controlled Execute | Request physical command | Required |
| Block | Trigger Feed Hold or protective alarm | Recorded immediately, reviewed after containment |

## High-Risk Action Boundary

Agents must not automatically start CNC cycle, change NC program for execution, change Feed Override, commit quotation, release process route, release OEP, substitute material, or grant quality concession.
```

- [ ] **Step 2: Write Agent contract schema**

Create `schemas/agents/v1/agent-contract.schema.json` with this content:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ai-native-factory.local/schemas/agents/v1/agent-contract.schema.json",
  "title": "AgentDecisionContract",
  "type": "object",
  "required": ["decision_id", "agent_id", "agent_version", "decision_type", "target_refs", "recommendation", "evidence_refs", "assumptions", "risk_level", "required_approval", "affected_objects", "adoption_status"],
  "properties": {
    "decision_id": { "type": "string", "pattern": "^DEC-[A-Z0-9-]+$" },
    "agent_id": { "type": "string" },
    "agent_version": { "type": "string" },
    "decision_type": { "type": "string", "enum": ["quote", "dfm", "process_route", "resource_selection", "oep_gate", "execution_trace", "knowledge_candidate"] },
    "target_refs": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
    "recommendation": { "type": "object" },
    "evidence_refs": { "type": "array", "items": { "type": "string" } },
    "assumptions": { "type": "array", "items": { "type": "string" } },
    "risk_level": { "type": "string", "enum": ["low", "medium", "high", "critical"] },
    "required_approval": { "type": "boolean" },
    "affected_objects": { "type": "array", "items": { "type": "string" } },
    "proposed_events": { "type": "array", "items": { "type": "string" } },
    "adoption_status": { "type": "string", "enum": ["proposed", "accepted", "modified", "rejected", "expired"] },
    "reviewer": { "type": ["string", "null"] },
    "review_notes": { "type": ["string", "null"] }
  },
  "additionalProperties": false
}
```

- [ ] **Step 3: Verify Agent artifacts**

Run:

```powershell
Get-Content -Raw 'schemas/agents/v1/agent-contract.schema.json' | ConvertFrom-Json | Out-Null
rg -n "Intake / DFM / Quote Agent|Process Agent|Package / Gate Agent|Execution / Trace Agent|DecisionLog|Controlled Execute" docs/ai-native-factory-v1/04-agent-contracts.md
```

Expected: JSON parses; search returns all listed Agent names and permission terms.

- [ ] **Step 4: Commit Agent contracts**

Run:

```powershell
git add docs/ai-native-factory-v1/04-agent-contracts.md schemas/agents/v1/agent-contract.schema.json
git commit -m "docs: define AI native factory agent contracts"
```

Expected: Git creates one commit for Agent Runtime contracts.

## Task 6: Define Machine Physical Agent

**Files:**
- Create: `docs/ai-native-factory-v1/05-machine-physical-agent-spec.md`
- Create: `docs/ai-native-factory-v1/06-validation-machine-bom-and-interfaces.md`
- Create: `schemas/machine-agent/v1/machine-physical-agent.interface.json`

- [ ] **Step 1: Write Machine Physical Agent specification**

Create `docs/ai-native-factory-v1/05-machine-physical-agent-spec.md` with these sections:

```markdown
# 05 Machine Physical Agent Specification

## Definition

Machine Physical Agent is a cyber-physical agent installed around a machining device. It combines the machine body, sensing organs, nervous system, edge brain, reflex loop, and OEP interface.

## Components

| Component | V1 Meaning |
|---|---|
| Body | Machine tool, CNC, PLC, spindle, magazine, table, fixture, probe, laser tool setter |
| Sensors | CNC/PLC data, probe, laser tool setting, tool identity, fixture identity, pallet identity, spindle load, current, vibration, vision, line laser, coolant, air pressure, temperature |
| Nervous System | OPC UA, MTConnect, vendor API, IO-Link, DAQ, industrial Ethernet, camera trigger, time sync |
| Edge Brain | Edge IPC or edge AI box for state fusion, gate judgment, command orchestration, explanation, trace write-back |
| Reflex Loop | Emergency stop, door interlock, safety PLC, CNC alarm, Feed Hold, tool-life block, fixture confirmation block |
| OEP Interface | Receive OEP, check gates, request approved actions, write Trace |

## Capability Levels

| Level | Name | Goal | Action Boundary |
|---|---|---|---|
| L1 | MVP Sensing | Machine can be observed and explained | No autonomous physical action |
| L2 | Controlled Execution | Machine can act after approval | Human-approved commands, no autonomous spindle start, no Feed Override |
| L3 | Adaptive Enhancement | Machine can suggest local adaptation | Suggestion and offline analysis in V1 |

The first validation machine target is L2 controlled execution with L3 sensing hardware installed.

## Allowed V1 Actions

- Bind or download NC program while CNC cycle start remains human-operated.
- Trigger probing, tool setting, and tool-break macros after approval.
- Read and write CNC execution state, alarms, spindle load, and measurement macro variables.
- Trigger Feed Hold or alarm stop for protection.
- Record all command outcomes into OEP Trace.

## Blocked V1 Actions

- Autonomous CNC cycle start.
- Autonomous NC program edit and run.
- Feed Override closed loop.
- Material substitution without engineering and quality approval.
- Quality concession without quality-owner approval.

## Safety Rule

Real-time safety belongs to CNC, PLC, and safety PLC. Edge AI may understand state, explain risk, request controlled actions, and trigger allowed protective actions, but it must not replace certified safety control.
```

- [ ] **Step 2: Write validation-machine BOM and interface list**

Create `docs/ai-native-factory-v1/06-validation-machine-bom-and-interfaces.md` with these sections:

```markdown
# 06 Validation Machine BOM And Interfaces

## Target

The first validation machine is the physical proof point for Phase 1. It must support L2 controlled execution and install the enhanced sensing hardware needed for L3 data learning.

## Required Sensing Organs

| Item | Purpose | OEP Use |
|---|---|---|
| CNC/PLC data interface | Status, alarms, program, load, macro variables | Gate, Trace, exception |
| Workpiece probe | Setup confirmation and in-process measurement | Gate, quality, Trace |
| Laser tool setter / break detection | Tool geometry and break check | Tool Gate, Trace |
| Tool identity confirmation | Tool assembly match | Resource Gate, Tool Gate |
| Fixture identity confirmation | Fixture match | Fixture Gate |
| Pallet identity confirmation | Pallet match | Fixture Gate |
| Edge HMI / scanner | Human confirmation and barcode binding | Approval, Trace |

## Enhanced Sensing Organs

| Item | Phase 1 Use |
|---|---|
| Vibration sensor | Evidence capture, anomaly label, offline analysis |
| Industrial camera or line laser | Setup evidence, visual trace, future feature verification |
| High-resolution spindle power/current acquisition | Cutting-state evidence and quote/process calibration |
| Temperature sensor | Machine and environment context |
| Coolant sensor | Process condition trace |
| Air pressure sensor | Fixture and auxiliary condition trace |

## Edge Hardware

- Industrial PC or edge AI box.
- Isolated industrial network interface.
- Time synchronization source.
- Local buffer for disconnected operation.
- HMI or scanner input.
- Secure connection to OEP Service and Event Bus.

## Interface Requirements

| Interface | Direction | Minimum Data |
|---|---|---|
| OEP download | Cloud/service to edge | package_id, status, plan, gate |
| Gate query | edge to service | package_id, gate status, evidence refs |
| Command request | service or HMI to edge | command_id, package_id, approval_id, command_type |
| Command result | edge to service | command_id, result, time, machine_state, exception_id |
| Sensor stream | edge to event storage | sensor_id, timestamp, value, quality |
| Trace write-back | edge to OEP Service | execution_records, measurement_results, exceptions, command_records |

## Procurement Decision Boundary

Select devices that can be supported by the validation-machine CNC/PLC vendor interface and by the plant network plan. Prefer industrial supportability over experimental sensor novelty.
```

- [ ] **Step 3: Write Machine Physical Agent interface schema**

Create `schemas/machine-agent/v1/machine-physical-agent.interface.json` with this content:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ai-native-factory.local/schemas/machine-agent/v1/machine-physical-agent.interface.json",
  "title": "MachinePhysicalAgentCommand",
  "type": "object",
  "required": ["command_id", "package_id", "machine_agent_id", "command_type", "approval_id", "requested_by", "requested_at"],
  "properties": {
    "command_id": { "type": "string", "pattern": "^MCMD-[A-Z0-9-]+$" },
    "package_id": { "type": "string", "pattern": "^OEP-[A-Z0-9-]+$" },
    "machine_agent_id": { "type": "string" },
    "command_type": {
      "type": "string",
      "enum": ["bind_nc_program", "download_nc_program", "trigger_probe_macro", "trigger_tool_setting_macro", "trigger_tool_break_check", "read_machine_state", "write_measurement_macro_variable", "trigger_feed_hold", "raise_alarm_stop"]
    },
    "approval_id": { "type": "string" },
    "requested_by": {
      "type": "object",
      "required": ["type", "id"],
      "properties": {
        "type": { "type": "string", "enum": ["human", "agent", "service"] },
        "id": { "type": "string" }
      },
      "additionalProperties": false
    },
    "requested_at": { "type": "string", "format": "date-time" },
    "parameters": { "type": "object" }
  },
  "additionalProperties": false
}
```

- [ ] **Step 4: Verify Machine Physical Agent artifacts**

Run:

```powershell
Get-Content -Raw 'schemas/machine-agent/v1/machine-physical-agent.interface.json' | ConvertFrom-Json | Out-Null
rg -n "L2 controlled execution|Feed Override|Workpiece probe|Laser tool setter|vibration|Industrial camera|spindle power|Trace write-back" docs/ai-native-factory-v1/05-machine-physical-agent-spec.md docs/ai-native-factory-v1/06-validation-machine-bom-and-interfaces.md
```

Expected: JSON parses; search returns matches across both documents.

- [ ] **Step 5: Commit physical agent specification**

Run:

```powershell
git add docs/ai-native-factory-v1/05-machine-physical-agent-spec.md docs/ai-native-factory-v1/06-validation-machine-bom-and-interfaces.md schemas/machine-agent/v1/machine-physical-agent.interface.json
git commit -m "docs: define machine physical agent baseline"
```

Expected: Git creates one commit for physical agent specification and interface schema.

## Task 7: Define Quote And Process Knowledge Base

**Files:**
- Create: `docs/ai-native-factory-v1/07-quote-and-process-knowledge-base.md`

- [ ] **Step 1: Write knowledge-base document**

Create `docs/ai-native-factory-v1/07-quote-and-process-knowledge-base.md` with this content:

```markdown
# 07 Quote And Process Knowledge Base

## V1 Knowledge Strategy

V1 uses a hybrid knowledge layer:

- Documents and retrieval for explanation.
- Structured rule tables for constraints.
- Process templates for draft generation.
- Historical orders for calibration.
- DecisionLog for learning from adoption, modification, and rejection.

## Quotation Model

V1 quotation is budget-level by default. Formal commercial commitment requires human review.

Cost structure:

- Material cost
- Machine-hour cost
- Setup labor cost
- CAM/process engineering labor
- Tooling cost
- Fixture cost
- Inspection cost
- Risk buffer
- Delivery assumption

## Quote Rule Table Fields

| Field | Meaning |
|---|---|
| rule_id | Stable rule identity |
| part_family | Plate, bracket, fixture, simple housing, or medium-complexity case |
| material | Material group |
| feature_condition | Feature or tolerance condition |
| cost_driver | Material, machine_time, setup, tooling, fixture, inspection, risk |
| formula | Deterministic calculation or lookup key |
| evidence | Expert, historical order, supplier quote, or measurement |
| owner | Process or quoting owner |
| status | candidate, approved, retired |

## Process Template Fields

| Field | Meaning |
|---|---|
| template_id | Stable template identity |
| part_family | Part family |
| material | Material group |
| stock_form | Plate, bar, casting, extrusion, prepared blank |
| operation_sequence | Ordered operation list |
| setup_strategy | Setup count and datum strategy |
| machine_capability | Required axes, travel, spindle, probe, and accuracy |
| tool_family | Required tool categories |
| fixture_strategy | Fixture or pallet rule |
| inspection_strategy | First article, in-process, final, or sampling |
| risk_notes | Known process risks |
| owner | Process owner |
| status | candidate, approved, retired |

## Learning Rule

After first-order execution, the system must compare Agent recommendation, human modification, actual execution, measurement, exception, and final disposition.

Learning outputs:

- Quote rule candidate
- Process template candidate
- Resource-selection rule candidate
- Gate rule candidate
- Sensor-derived anomaly label

No candidate becomes approved knowledge without owner review.
```

- [ ] **Step 2: Verify quotation and process priorities**

Run:

```powershell
rg -n "budget-level|Formal commercial commitment|Quote Rule Table|Process Template|DecisionLog|owner review" docs/ai-native-factory-v1/07-quote-and-process-knowledge-base.md
```

Expected: matches for all listed terms.

- [ ] **Step 3: Commit knowledge-base design**

Run:

```powershell
git add docs/ai-native-factory-v1/07-quote-and-process-knowledge-base.md
git commit -m "docs: define quote and process knowledge base"
```

Expected: Git creates one commit for the knowledge-base baseline.

## Task 8: Define First-Order Demo Runbook

**Files:**
- Create: `docs/ai-native-factory-v1/08-first-order-demo-runbook.md`

- [ ] **Step 1: Write the Demo runbook**

Create `docs/ai-native-factory-v1/08-first-order-demo-runbook.md` with this content:

```markdown
# 08 First-Order Demo Runbook

## Demo Objective

Run one real historical machining order through the V1 chain and prove that Agent recommendations, OEP release, Machine Physical Agent execution, quality write-back, and knowledge capture are auditable.

## Entry Criteria

- One historical order selected.
- Drawing and CAD version available.
- Part type is simple plate, bracket, fixture, simple housing, or selected medium-complexity case.
- Validation machine selected.
- CAM owner, process owner, machine owner, quality owner, and system owner assigned.
- Required sensing organs installed or installation date recorded in the Phase 1 schedule.
- Enhanced sensing organs included in the validation-machine build scope.

## Roles

| Role | Responsibility |
|---|---|
| System owner | Owns OEP and event contracts |
| Process owner | Reviews DFM, quote assumptions, process route, setup, tool, fixture |
| CAM owner | Owns CAM and NC generation or import |
| Machine owner | Owns validation-machine readiness and physical safety |
| Quality owner | Owns inspection plan and final disposition |
| Operator | Performs approved machine-side actions |
| Agent operator | Runs Agent workflow and records DecisionLog |

## Run Sequence

### 1. Order And Drawing Intake

Create CustomerOrder, Part, Drawing, CADModel, and attachment records. Record drawing revision and CAD revision.

Evidence:

- Object records
- Attachment refs
- Order intake event

### 2. Quote And DFM

Run Intake / DFM / Quote Agent. Capture DFM risks, quote assumptions, budget-level quote structure, and delivery assumptions. Process owner reviews the result.

Evidence:

- Quotation draft
- DecisionLog
- Human review record

### 3. Process / CAPP / CAM

Run Process Agent. Process owner reviews route, setup, machine, tool, fixture, and inspection strategy. CAM owner generates or imports CAM/NC results.

Evidence:

- ProcessPlan
- Operation
- SetupPlan
- Toolpath or CAM reference
- NCProgram object
- DecisionLog

### 4. OEP Generation

Run Package / Gate Agent. Generate L2 Operation Execution Package for the validation-machine operation/setup.

Evidence:

- OEP Draft
- Parent refs to order and part lot
- Plan/Gate/Trace sections present

### 5. Simulation And Approval

Evaluate Engineering, Resource, Tool, Fixture, Simulation, Quality, and Authority gates. Human approvers sign the release.

Evidence:

- Gate check events
- Approval record
- Released OEP

### 6. Validation-Machine Staging

Machine Physical Agent receives released OEP. Operator confirms fixture, pallet, tools, NC binding, and machine state through HMI/scanner.

Evidence:

- MachineAgent command request records
- Tool, fixture, pallet identity records
- OEP Staged event

### 7. Controlled Execution

Machine Physical Agent may bind or download NC, trigger probe/tool macros, read/write allowed machine variables, and trigger protective Feed Hold if needed. CNC cycle start remains human-operated.

Evidence:

- Command result records
- ExecutionRecord
- Sensor records
- Machine alarms and state records

### 8. Quality And Exception Write-Back

Capture measurement results, exceptions, abnormal stops, human corrections, and final quality disposition.

Evidence:

- MeasurementResult
- Exception records
- Quality owner review
- OEP Completed or ReworkRequired

### 9. Learning Capture

Execution / Trace Agent summarizes what was accepted, modified, rejected, abnormal, and reusable.

Evidence:

- DecisionLog replay
- KnowledgeItem candidates
- First-order retrospective

## Demo Pass Criteria

- OEP replay reconstructs the first-order journey from intake to quality disposition.
- Agent recommendations for quote/DFM, process route, and resource selection have adoption status.
- High-risk actions have Gate plus human approval.
- Physical commands are linked to OEP, approval, actor, result, and exception status.
- At least one quote, process, resource, or gate knowledge candidate is produced from the run.
```

- [ ] **Step 2: Verify runbook has the requested flow**

Run:

```powershell
rg -n "Order And Drawing Intake|Quote And DFM|Process / CAPP / CAM|OEP Generation|Simulation And Approval|Controlled Execution|Quality And Exception Write-Back|Learning Capture" docs/ai-native-factory-v1/08-first-order-demo-runbook.md
```

Expected: matches for all eight sequence headings.

- [ ] **Step 3: Commit Demo runbook**

Run:

```powershell
git add docs/ai-native-factory-v1/08-first-order-demo-runbook.md
git commit -m "docs: define first-order demo runbook"
```

Expected: Git creates one commit for the first-order Demo runbook.

## Task 9: Define Acceptance And Expansion Gates

**Files:**
- Create: `docs/ai-native-factory-v1/09-phase-1-acceptance-checklist.md`
- Create: `docs/ai-native-factory-v1/10-phase-2-3-expansion-plan.md`

- [ ] **Step 1: Write Phase 0 and Phase 1 acceptance checklist**

Create `docs/ai-native-factory-v1/09-phase-1-acceptance-checklist.md` with this content:

```markdown
# 09 Phase 0 And Phase 1 Acceptance Checklist

## Phase 0 Exit

| Check | Evidence | Pass Rule |
|---|---|---|
| Historical order selected | Order id and drawing refs | One order is frozen for Demo |
| Part family confirmed | Part-family note | Mainly simple A-type part, selected B-like complexity allowed |
| OEP schema frozen | `01-oep-schema.md` and JSON Schema | Plan/Gate/Trace are complete |
| Object model frozen | `02-object-model-v1.md` | Required V1 objects listed |
| Event envelope frozen | `03-event-catalog.md` and JSON Schema | Event envelope parses as JSON |
| Agent contracts frozen | `04-agent-contracts.md` and JSON Schema | Four decision agents defined |
| Machine Physical Agent BOM frozen | `06-validation-machine-bom-and-interfaces.md` | Required and enhanced sensors listed |
| Offline first-order chain runs | Runbook evidence | Quote draft, process draft, and OEP draft produced |

## Phase 1 Product Acceptance

| Metric | Target |
|---|---|
| Drawing-to-OEP data chain completeness | 100% for first-order Demo |
| OEP Plan/Gate/Trace completeness | 100% for released OEP |
| High-risk action Gate coverage | 100% |
| Human approval coverage for release and controlled execution | 100% |
| Physical command traceability | 100% |
| Agent recommendation adoption status coverage | 100% |
| Measurement and exception write-back | 100% for captured Demo evidence |
| OEP replayability | Complete replay from intake to quality disposition |

## Phase 1 Intelligence Acceptance

The most important V1 intelligent value is ABC:

- A: DFM and quote recommendation.
- B: Process route recommendation.
- C: Tool, fixture, and machine selection recommendation.

D and E are core future value:

- D: Execution monitoring and adaptive recommendation.
- E: Knowledge learning and continuous improvement.

Phase 1 must record D and E evidence, but acceptance priority is that A, B, and C have visible, reviewable, and adoptable recommendations.

## Safety Acceptance

- No autonomous CNC cycle start.
- No Feed Override closed loop.
- No AI direct edit-and-run of NC programs.
- Feed Hold or alarm stop is allowed only as a recorded protective action.
- Certified safety remains with CNC, PLC, and safety PLC.
```

- [ ] **Step 2: Write Phase 2 and Phase 3 expansion plan**

Create `docs/ai-native-factory-v1/10-phase-2-3-expansion-plan.md` with this content:

```markdown
# 10 Phase 2 And Phase 3 Expansion Plan

## Expansion Rule

Do not redesign the architecture when scaling. Copy the OEP spine, Agent contract, Machine Physical Agent interface, event envelope, and acceptance gates.

## Phase 2: Three-Machine Cell

Goal:

- Connect three machining devices to the same OEP kernel.
- Use machine capability, tool availability, fixture availability, operator availability, and quality resources in resource selection.
- Introduce local scheduling, resource conflict detection, and exception reassignment.
- Convert the first validation-machine installation into a repeatable Machine Physical Agent deployment template.

Entry criteria:

- Phase 1 first-order Demo passed.
- Validation-machine interface stable for at least one complete order.
- Required sensor and command records are traceable.
- Gate failure and exception handling have been exercised at least once in simulation or controlled test.

Exit evidence:

- Multiple OEPs assigned across three devices.
- Resource conflicts detected and recorded.
- At least one exception reassignment or recovery flow recorded.
- Machine Physical Agent deployment package documented for each device.

## Phase 3: About Twenty Machining Devices

Goal:

- Scale standardized Machine Physical Agent deployment.
- Add Toolroom Agent, Inspection Agent, and Logistics/Robot Agent when the OEP and event contracts can absorb them.
- Strengthen operations governance, monitoring, and maintenance.
- Use execution and quality data to improve quote, process, and resource-selection knowledge.

Entry criteria:

- Three-machine cell produces repeatable OEP traces.
- Machine capability model is stable.
- Tool, fixture, material, quality, and operator objects are usable in scheduling and gates.
- Edge deployment template has documented network, security, sensor, and safety boundaries.

Exit evidence:

- About twenty machining devices have standardized identity, capability, status, and trace records.
- Machine Physical Agent installation status is visible per device.
- OEP-driven execution governance covers released production tasks.
- Operations team can replay order, OEP, machine, quality, exception, and DecisionLog history.

## New Agent Admission Rule

Add Robot/Logistics Agent, Toolroom Agent, or Inspection Agent only when:

- The target work can be represented as OEP, auxiliary package, event, object update, or DecisionLog.
- High-risk actions have Gate and human approval.
- The Agent can be tested against first-order or three-machine evidence.
```

- [ ] **Step 3: Verify acceptance and expansion gates**

Run:

```powershell
rg -n "100%|ABC|No autonomous CNC cycle start|Three-Machine Cell|About Twenty Machining Devices|New Agent Admission Rule" docs/ai-native-factory-v1/09-phase-1-acceptance-checklist.md docs/ai-native-factory-v1/10-phase-2-3-expansion-plan.md
```

Expected: matches for all listed terms.

- [ ] **Step 4: Commit acceptance and expansion documents**

Run:

```powershell
git add docs/ai-native-factory-v1/09-phase-1-acceptance-checklist.md docs/ai-native-factory-v1/10-phase-2-3-expansion-plan.md
git commit -m "docs: define AI native factory rollout gates"
```

Expected: Git creates one commit for acceptance and expansion gates.

## Task 10: Final Consistency Verification

**Files:**
- Verify: `docs/ai-native-factory-v1/*.md`
- Verify: `schemas/oep/v1/operation-execution-package.schema.json`
- Verify: `schemas/events/v1/event-envelope.schema.json`
- Verify: `schemas/agents/v1/agent-contract.schema.json`
- Verify: `schemas/machine-agent/v1/machine-physical-agent.interface.json`

- [ ] **Step 1: Verify all expected files exist**

Run:

```powershell
$paths = @(
  'docs/ai-native-factory-v1/README.md',
  'docs/ai-native-factory-v1/00-program-charter.md',
  'docs/ai-native-factory-v1/01-oep-schema.md',
  'docs/ai-native-factory-v1/02-object-model-v1.md',
  'docs/ai-native-factory-v1/03-event-catalog.md',
  'docs/ai-native-factory-v1/04-agent-contracts.md',
  'docs/ai-native-factory-v1/05-machine-physical-agent-spec.md',
  'docs/ai-native-factory-v1/06-validation-machine-bom-and-interfaces.md',
  'docs/ai-native-factory-v1/07-quote-and-process-knowledge-base.md',
  'docs/ai-native-factory-v1/08-first-order-demo-runbook.md',
  'docs/ai-native-factory-v1/09-phase-1-acceptance-checklist.md',
  'docs/ai-native-factory-v1/10-phase-2-3-expansion-plan.md',
  'schemas/oep/v1/operation-execution-package.schema.json',
  'schemas/events/v1/event-envelope.schema.json',
  'schemas/agents/v1/agent-contract.schema.json',
  'schemas/machine-agent/v1/machine-physical-agent.interface.json'
)
$paths | ForEach-Object { "$_ => $(Test-Path $_)" }
```

Expected: every line ends with `True`.

- [ ] **Step 2: Verify JSON artifacts parse**

Run:

```powershell
Get-Content -Raw 'schemas/oep/v1/operation-execution-package.schema.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'schemas/events/v1/event-envelope.schema.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'schemas/agents/v1/agent-contract.schema.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'schemas/machine-agent/v1/machine-physical-agent.interface.json' | ConvertFrom-Json | Out-Null
```

Expected: no output and exit code 0.

- [ ] **Step 3: Verify architecture anchors**

Run:

```powershell
rg -n "Operation Execution Package|Machine Physical Agent|DecisionLog|Plan|Gate|Trace|Phase 1|Feed Override|quote/DFM|process/CAPP/CAM" docs/ai-native-factory-v1 schemas
```

Expected: matches across the OEP, Agent, physical agent, Demo, and acceptance documents.

- [ ] **Step 4: Review against the approved architecture**

Open:

```powershell
Get-Content -Raw 'docs/superpowers/specs/2026-05-06-ai-native-factory-v1-architecture-design.md'
```

Check that the implementation baseline covers:

- OEP as system spine.
- Four product kernels.
- Four decision agents.
- Machine Physical Agent as cyber-physical system.
- L2 controlled execution with L3 sensing hardware installed.
- Required and enhanced sensing organs.
- First-order flow from order/drawing to quote/DFM to process/CAPP/CAM to OEP to simulation/approval to controlled execution to write-back.
- Phase 0, Phase 1, Phase 2, and Phase 3 rollout.
- Safety and authority boundaries.

- [ ] **Step 5: Commit final verification adjustments**

Run:

```powershell
git status --short
git add docs/ai-native-factory-v1 schemas
git commit -m "docs: complete AI native factory v1 implementation baseline"
```

Expected: If previous task commits were already made, Git may report no changes to commit. If refinements were made during final review, Git creates one final cleanup commit.

## Execution Notes

The first implementation pass should create the documents and schemas exactly enough to allow review by five owners:

- System owner reviews OEP, object model, event catalog, and Agent contract.
- Process owner reviews quote/process knowledge and first-order runbook.
- Machine owner reviews Machine Physical Agent and validation-machine BOM.
- Quality owner reviews quality gates, inspection evidence, and final disposition flow.
- Leadership reviews phase gates and investment risk reduction.

The strongest next decision after this plan is whether to execute all artifact tasks inline in this session or dispatch separate workers by domain: OEP/object/event, Agent/knowledge, Machine Physical Agent, and Demo/acceptance.
