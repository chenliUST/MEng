# JTGK-800i Execution-Spine Physical Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the machine-specific execution-spine artifact set for the JTGK-800i physical agent so dry trace, first-part validation, and production-like replay can run in quick succession.

**Architecture:** The OEP remains the execution contract. The JTGK-800i edge physical agent binds machine, operator, NC program, quality evidence, health evidence, commands, approvals, and exceptions into one traceable evidence spine while CNC, PLC, safety circuits, and the human operator retain real-time safety and cycle-start authority.

**Tech Stack:** Markdown architecture/runbook artifacts, JSON Schema Draft 2020-12, JSON examples, existing AI Native Factory V1 OEP/event/machine-agent schemas, PowerShell verification commands, Git.

---

## Scope Check

This plan implements one coherent sub-project: the JTGK-800i execution-spine physical agent artifact set. It does not implement live CNC connectivity, hardware procurement, edge runtime code, HMI UI code, or sensor drivers. Those are implementation projects that should use this artifact set as their contract.

The plan produces working, reviewable artifacts:

- Machine profile and interface freeze.
- Execution evidence schema.
- Evidence and event examples.
- Event catalog/schema extension.
- A/B/C pilot sprint runbook.
- Operator approval workflow.
- Acceptance checklist and verification commands.

## File Structure

- Create: `docs/ai-native-factory-v1/jtgk-800i/README.md`
  - Responsibility: index and reading order for the machine-specific package.
- Create: `docs/ai-native-factory-v1/jtgk-800i/01-machine-profile-and-interface-freeze.md`
  - Responsibility: machine facts, interface claims, fallback paths, and safety boundary for the JTGK-800i.
- Create: `docs/ai-native-factory-v1/jtgk-800i/02-evidence-model.md`
  - Responsibility: control, quality, health, and human evidence model attached to OEP trace.
- Create: `schemas/machine-agent/v1/execution-evidence.schema.json`
  - Responsibility: machine-readable schema for one execution evidence record.
- Create: `examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json`
  - Responsibility: concrete evidence examples for dry trace, first-part validation, and health capture.
- Create: `docs/ai-native-factory-v1/jtgk-800i/03-event-and-command-map.md`
  - Responsibility: map OEP states, MachineAgent commands, and new evidence events.
- Modify: `docs/ai-native-factory-v1/03-event-catalog.md`
  - Responsibility: add machine state, evidence, and containment event types to the global catalog.
- Modify: `schemas/events/v1/event-envelope.schema.json`
  - Responsibility: allow the new machine event types.
- Create: `examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json`
  - Responsibility: concrete event examples for the new event types.
- Create: `docs/ai-native-factory-v1/jtgk-800i/04-pilot-sprint-runbook.md`
  - Responsibility: A/B/C concentrated pilot sequence.
- Create: `docs/ai-native-factory-v1/jtgk-800i/05-operator-hmi-and-approval-flow.md`
  - Responsibility: scanner/HMI workflow, approval gates, and containment review.
- Create: `docs/ai-native-factory-v1/jtgk-800i/06-acceptance-checklist.md`
  - Responsibility: pass/fail criteria for dry trace, first-part validation, and production-like replay.

Read first:

- `docs/superpowers/specs/2026-05-16-jtgk-800i-execution-spine-physical-agent-design.md`
- `docs/ai-native-factory-v1/05-machine-physical-agent-spec.md`
- `docs/ai-native-factory-v1/06-validation-machine-bom-and-interfaces.md`
- `schemas/machine-agent/v1/machine-physical-agent.interface.json`
- `schemas/events/v1/event-envelope.schema.json`

## Task 1: Scaffold The JTGK-800i Package

**Files:**
- Create: `docs/ai-native-factory-v1/jtgk-800i/README.md`
- Create directories: `docs/ai-native-factory-v1/jtgk-800i`, `examples/ai-native-factory-v1/jtgk-800i`

- [ ] **Step 1: Create directories**

Run:

```powershell
New-Item -ItemType Directory -Force -Path `
  'docs/ai-native-factory-v1/jtgk-800i', `
  'examples/ai-native-factory-v1/jtgk-800i'
```

Expected: PowerShell prints directory entries or returns without error. Both directories exist.

- [ ] **Step 2: Create the machine package README**

Create `docs/ai-native-factory-v1/jtgk-800i/README.md` with this content:

```markdown
# JTGK-800i Execution-Spine Physical Agent

This folder specializes the AI Native Factory V1 Machine Physical Agent design for the JTGK-800i validation machine.

Read in this order:

1. `01-machine-profile-and-interface-freeze.md`
2. `02-evidence-model.md`
3. `03-event-and-command-map.md`
4. `04-pilot-sprint-runbook.md`
5. `05-operator-hmi-and-approval-flow.md`
6. `06-acceptance-checklist.md`

The machine-specific mission is traceable execution first. Quality and machine-health records are captured as structured evidence attached to the same OEP execution spine.
```

- [ ] **Step 3: Verify scaffold**

Run:

```powershell
Test-Path 'docs/ai-native-factory-v1/jtgk-800i/README.md'
Test-Path 'examples/ai-native-factory-v1/jtgk-800i'
```

Expected:

```text
True
True
```

- [ ] **Step 4: Commit scaffold**

Run:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i/README.md
git commit -m "docs: scaffold JTGK machine agent package"
```

Expected: Git creates one commit for the package README.

## Task 2: Freeze Machine Profile And Interface Claims

**Files:**
- Create: `docs/ai-native-factory-v1/jtgk-800i/01-machine-profile-and-interface-freeze.md`

- [ ] **Step 1: Write the machine profile**

Create `docs/ai-native-factory-v1/jtgk-800i/01-machine-profile-and-interface-freeze.md` with this content:

```markdown
# 01 Machine Profile And Interface Freeze

## Purpose

Freeze the JTGK-800i machine identity, known capability, interface assumptions, fallback paths, and safety boundary before building the execution-spine pilot.

## Machine Identity

| Field | Value |
|---|---|
| machine_id | `MC-JTGK-800I-001` |
| machine_agent_id | `MPA-JTGK-800I-001` |
| machine_make_model | JTGK-800i CNC engraving and milling center |
| cnc_control | JT810 |
| machine_capability_version | `JTGK800I-CAP-V1` |
| primary_mission | Execution-spine traceability |
| pilot_mode | Concentrated A/B/C sprint |

## Machine Capability

| Capability | Value |
|---|---|
| X/Y/Z travel | 700 / 800 / 350 mm |
| work envelope note | 810 x 800 x 410 mm listed in supplied specification |
| table size | 750 x 800 mm |
| table load | 800 kg |
| spindle | 15 kW S6, 24000 rpm |
| spindle taper | BBT30 |
| tool magazine | 24 tools |
| rapid traverse | X/Y/Z 20 / 20 / 20 m/min |
| total installed power | about 20 kW |
| power supply | 380 V +/- 5%, 50 Hz |
| compressed air | 0.6 MPa, 210 L/min |

## Interface Freeze Matrix

| Interface | Target For Pilot | First Verification Method | Fallback If Direct Access Is Limited |
|---|---|---|---|
| CNC state read | mode, active program, alarm, cycle state | read test from JT810 or vendor interface | operator HMI confirmation plus photo evidence |
| PLC/safety state read | door, emergency stop, machine ready where available | PLC/safety status read test | operator checklist confirmation |
| NC program binding | bind OEP to NC program id/version | file path, control program id, or CNC screen confirmation | scanner/HMI entry of NC id/version |
| macro variable read | approved probing/tool/measurement variables | vendor-supported macro variable read | HMI entry from CNC screen |
| macro variable write | approved measurement or handshake variables only | write to documented non-safety variable in dry test | no-write mode with manual measurement write-back |
| command request capture | command id, approval id, actor, result | edge command log | HMI-only command record |
| quality evidence capture | probe, tool setting, inspection result, setup photo | available probe/tool-setter/HMI/camera path | manual inspection record with evidence attachment |
| health evidence capture | spindle load/current, vibration, air, coolant, temperature | DAQ or sensor read test | machine-state and operator note only for Slice A |

## Safety Boundary

Allowed after OEP gate and human approval:

- Bind or download NC program.
- Read machine state.
- Trigger approved probing macro.
- Trigger approved tool-setting macro.
- Trigger approved tool-break check macro.
- Write approved measurement macro variables or documented handshake variables.

Allowed as protective containment:

- Trigger feed hold.
- Raise alarm stop.

Blocked in V1:

- Autonomous CNC cycle start.
- Autonomous NC edit-and-run.
- Closed-loop feed override.
- Writes to safety PLC parameters.
- Writes to CNC safety parameters.
- Quality concession without quality-owner approval.

## Freeze Exit

The machine profile is frozen when every row in the Interface Freeze Matrix has one of these statuses recorded in the implementation tracker:

- `verified_direct`
- `verified_fallback`
- `blocked_with_owner`

The first pilot may run Slice A with fallback confirmations. Slice B and Slice C require direct or controlled fallback evidence for quality and health records.
```

- [ ] **Step 2: Verify machine profile anchors**

Run:

```powershell
rg -n "MC-JTGK-800I-001|JT810|BBT30|24000 rpm|Interface Freeze Matrix|Autonomous CNC cycle start|verified_direct|verified_fallback|blocked_with_owner" docs/ai-native-factory-v1/jtgk-800i/01-machine-profile-and-interface-freeze.md
```

Expected: matches for all listed anchors.

- [ ] **Step 3: Commit machine profile**

Run:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i/01-machine-profile-and-interface-freeze.md
git commit -m "docs: freeze JTGK machine profile"
```

Expected: Git creates one commit for the machine profile and interface freeze.

## Task 3: Define Execution Evidence Schema And Examples

**Files:**
- Create: `docs/ai-native-factory-v1/jtgk-800i/02-evidence-model.md`
- Create: `schemas/machine-agent/v1/execution-evidence.schema.json`
- Create: `examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json`

- [ ] **Step 1: Write the evidence model document**

Create `docs/ai-native-factory-v1/jtgk-800i/02-evidence-model.md` with this content:

```markdown
# 02 Evidence Model

## Rule

Every machine-side record must attach to the OEP execution spine. A record that cannot identify package, operation, machine agent, source, timestamp, and evidence plane is not pilot evidence.

## Required Context

Each evidence record carries:

- `evidence_id`
- `package_id`
- `operation_id`
- `machine_agent_id`
- `machine_id`
- `timestamp`
- `evidence_plane`
- `record_type`
- `source`
- `data_quality`
- `context_refs`
- `payload`

## Evidence Planes

| Plane | Meaning | Pilot Examples |
|---|---|---|
| control | Execution state and governed command evidence | active program, alarm state, command result, gate result |
| quality | Setup, tool, measurement, and inspection evidence | probe result, tool break check, first-part result, setup photo |
| health | Machine and process condition evidence | spindle load, current, vibration, air pressure, coolant, temperature |
| human | Operator authority and explanation evidence | scan confirmation, approval, setup note, exception note |

## Data Quality Values

| Value | Meaning |
|---|---|
| direct_read | Read directly from CNC, PLC, DAQ, sensor, or service |
| controlled_manual | Entered by operator through controlled HMI/scanner workflow |
| imported_record | Imported from inspection, CAM, or external record system |
| simulated | Created in dry trace or controlled simulation |

## Context References

Use these keys when known:

- `nc_program_ref`
- `tool_ref`
- `fixture_ref`
- `pallet_ref`
- `operator_ref`
- `part_ref`
- `material_lot_ref`
- `approval_ref`
- `command_ref`
- `exception_ref`

## A/B/C Coverage

| Slice | Required Evidence |
|---|---|
| A Dry Trace | control and human evidence for OEP binding, NC version, machine state, approval, and command result |
| B First-Part Validation | quality evidence for tool check, fixture/tool confirmation, measurement, and first-part result |
| C Production-Like Replay | health evidence, exception evidence, containment record, and replayable operator note |
```

- [ ] **Step 2: Write the JSON Schema**

Create `schemas/machine-agent/v1/execution-evidence.schema.json` with this content:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ai-native-factory.local/schemas/machine-agent/v1/execution-evidence.schema.json",
  "title": "MachineExecutionEvidence",
  "type": "object",
  "required": [
    "evidence_id",
    "package_id",
    "operation_id",
    "machine_agent_id",
    "machine_id",
    "timestamp",
    "evidence_plane",
    "record_type",
    "source",
    "data_quality",
    "context_refs",
    "payload"
  ],
  "properties": {
    "evidence_id": { "type": "string", "pattern": "^EVD-[A-Z0-9-]+$" },
    "package_id": { "type": "string", "pattern": "^OEP-[A-Z0-9-]+$" },
    "operation_id": { "type": "string" },
    "machine_agent_id": { "type": "string" },
    "machine_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "evidence_plane": {
      "type": "string",
      "enum": ["control", "quality", "health", "human"]
    },
    "record_type": {
      "type": "string",
      "enum": [
        "machine_state",
        "program_binding",
        "gate_result",
        "command_result",
        "tool_check",
        "fixture_confirmation",
        "measurement_result",
        "first_part_result",
        "sensor_sample",
        "exception_note",
        "containment_record",
        "operator_confirmation"
      ]
    },
    "source": {
      "type": "object",
      "required": ["type", "id"],
      "properties": {
        "type": {
          "type": "string",
          "enum": ["cnc", "plc", "sensor", "edge_hmi", "scanner", "operator", "quality_system", "edge_agent", "simulation"]
        },
        "id": { "type": "string" }
      },
      "additionalProperties": false
    },
    "data_quality": {
      "type": "string",
      "enum": ["direct_read", "controlled_manual", "imported_record", "simulated"]
    },
    "context_refs": {
      "type": "object",
      "properties": {
        "nc_program_ref": { "type": ["string", "null"] },
        "tool_ref": { "type": ["string", "null"] },
        "fixture_ref": { "type": ["string", "null"] },
        "pallet_ref": { "type": ["string", "null"] },
        "operator_ref": { "type": ["string", "null"] },
        "part_ref": { "type": ["string", "null"] },
        "material_lot_ref": { "type": ["string", "null"] },
        "approval_ref": { "type": ["string", "null"] },
        "command_ref": { "type": ["string", "null"] },
        "exception_ref": { "type": ["string", "null"] }
      },
      "additionalProperties": false
    },
    "payload": { "type": "object" }
  },
  "additionalProperties": false
}
```

- [ ] **Step 3: Write evidence examples**

Create `examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json` with this content:

```json
[
  {
    "evidence_id": "EVD-JTGK-A-0001",
    "package_id": "OEP-JTGK-PILOT-001",
    "operation_id": "OP10-DRY-TRACE",
    "machine_agent_id": "MPA-JTGK-800I-001",
    "machine_id": "MC-JTGK-800I-001",
    "timestamp": "2026-05-16T09:00:00+08:00",
    "evidence_plane": "control",
    "record_type": "program_binding",
    "source": { "type": "edge_hmi", "id": "HMI-JTGK-001" },
    "data_quality": "controlled_manual",
    "context_refs": {
      "nc_program_ref": "NC-JTGK-DRY-001:V1",
      "tool_ref": null,
      "fixture_ref": "FIX-JTGK-001:V1",
      "pallet_ref": "PAL-JTGK-001:V1",
      "operator_ref": "OP-JTGK-001",
      "part_ref": "PART-JTGK-PILOT-001:V1",
      "material_lot_ref": null,
      "approval_ref": "APP-JTGK-A-001",
      "command_ref": "MCMD-JTGK-A-BIND-001",
      "exception_ref": null
    },
    "payload": {
      "binding_method": "scanner_confirmation",
      "machine_mode": "manual",
      "active_program_confirmed": true
    }
  },
  {
    "evidence_id": "EVD-JTGK-B-0001",
    "package_id": "OEP-JTGK-PILOT-001",
    "operation_id": "OP20-FIRST-PART",
    "machine_agent_id": "MPA-JTGK-800I-001",
    "machine_id": "MC-JTGK-800I-001",
    "timestamp": "2026-05-16T11:20:00+08:00",
    "evidence_plane": "quality",
    "record_type": "first_part_result",
    "source": { "type": "quality_system", "id": "QMS-PILOT" },
    "data_quality": "imported_record",
    "context_refs": {
      "nc_program_ref": "NC-JTGK-FIRSTPART-001:V1",
      "tool_ref": "TASM-D10-001:V1",
      "fixture_ref": "FIX-JTGK-001:V1",
      "pallet_ref": "PAL-JTGK-001:V1",
      "operator_ref": "OP-JTGK-001",
      "part_ref": "PART-JTGK-PILOT-001:V1",
      "material_lot_ref": "MAT-6061-JTGK-001",
      "approval_ref": "APP-JTGK-B-001",
      "command_ref": "MCMD-JTGK-B-PROBE-001",
      "exception_ref": null
    },
    "payload": {
      "inspection_plan_id": "IP-JTGK-FIRSTPART-001",
      "result": "pass",
      "critical_characteristics": [
        { "id": "DATUM_A_FLATNESS", "value": 0.018, "unit": "mm", "status": "pass" },
        { "id": "HOLE_PATTERN_POSITION", "value": 0.032, "unit": "mm", "status": "pass" }
      ]
    }
  },
  {
    "evidence_id": "EVD-JTGK-C-0001",
    "package_id": "OEP-JTGK-PILOT-001",
    "operation_id": "OP30-PRODUCTION-LIKE",
    "machine_agent_id": "MPA-JTGK-800I-001",
    "machine_id": "MC-JTGK-800I-001",
    "timestamp": "2026-05-16T14:05:00+08:00",
    "evidence_plane": "health",
    "record_type": "sensor_sample",
    "source": { "type": "sensor", "id": "SPINDLE-LOAD-JTGK-001" },
    "data_quality": "direct_read",
    "context_refs": {
      "nc_program_ref": "NC-JTGK-PRODLIKE-001:V1",
      "tool_ref": "TASM-D10-001:V1",
      "fixture_ref": "FIX-JTGK-001:V1",
      "pallet_ref": "PAL-JTGK-001:V1",
      "operator_ref": "OP-JTGK-001",
      "part_ref": "PART-JTGK-PILOT-001:V1",
      "material_lot_ref": "MAT-6061-JTGK-001",
      "approval_ref": "APP-JTGK-C-001",
      "command_ref": null,
      "exception_ref": "EXC-JTGK-C-001"
    },
    "payload": {
      "sample_window_ms": 1000,
      "spindle_load_percent_avg": 72.4,
      "spindle_load_percent_max": 88.1,
      "label": "controlled_exception_window"
    }
  }
]
```

- [ ] **Step 4: Verify evidence JSON parses**

Run:

```powershell
Get-Content -Raw 'schemas/machine-agent/v1/execution-evidence.schema.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json' | ConvertFrom-Json | Out-Null
```

Expected: no output and exit code 0.

- [ ] **Step 5: Verify evidence anchors**

Run:

```powershell
rg -n "evidence_plane|control|quality|health|human|direct_read|controlled_manual|EVD-JTGK-A-0001|EVD-JTGK-B-0001|EVD-JTGK-C-0001" docs/ai-native-factory-v1/jtgk-800i/02-evidence-model.md schemas/machine-agent/v1/execution-evidence.schema.json examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json
```

Expected: matches in the document, schema, and example file.

- [ ] **Step 6: Commit evidence model**

Run:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i/02-evidence-model.md schemas/machine-agent/v1/execution-evidence.schema.json examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json
git commit -m "docs: define JTGK execution evidence model"
```

Expected: Git creates one commit for the evidence model, schema, and examples.

## Task 4: Extend Event Catalog And Command Map

**Files:**
- Create: `docs/ai-native-factory-v1/jtgk-800i/03-event-and-command-map.md`
- Modify: `docs/ai-native-factory-v1/03-event-catalog.md`
- Modify: `schemas/events/v1/event-envelope.schema.json`
- Create: `examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json`

- [ ] **Step 1: Write the JTGK event and command map**

Create `docs/ai-native-factory-v1/jtgk-800i/03-event-and-command-map.md` with this content:

```markdown
# 03 Event And Command Map

## Rule

Commands request action. Events record facts. Evidence records attach detailed machine, quality, health, and human data to the OEP trace.

## Command Map

| Pilot Slice | Command Type | Safety Class | Required Evidence |
|---|---|---|---|
| A Dry Trace | `read_machine_state` | `approval_gated` | machine state evidence |
| A Dry Trace | `bind_nc_program` | `approval_gated` | program binding evidence |
| B First-Part Validation | `trigger_tool_setting_macro` | `approval_gated` | tool check evidence |
| B First-Part Validation | `trigger_tool_break_check` | `approval_gated` | tool check evidence |
| B First-Part Validation | `trigger_probe_macro` | `approval_gated` | measurement evidence |
| B First-Part Validation | `write_measurement_macro_variable` | `approval_gated` | measurement write-back evidence |
| C Production-Like Replay | `trigger_feed_hold` | `protective_containment` | containment record and exception note |
| C Production-Like Replay | `raise_alarm_stop` | `protective_containment` | containment record and exception note |

## Event Map

| Event Type | When Emitted | Payload Anchor |
|---|---|---|
| `MachineAgent.StateObserved` | Edge agent records machine state, mode, program, or alarm | `evidence_id` |
| `MachineAgent.EvidenceRecorded` | Edge agent stores control, quality, health, or human evidence | `evidence_id` |
| `MachineAgent.ContainmentTriggered` | Edge agent triggers feed hold or alarm stop as protection | `command_id`, `exception_id`, `containment_reason` |
| `MachineAgent.CommandRequested` | Normal command is requested by HMI, service, or agent | `command_id` |
| `MachineAgent.CommandExecuted` | Command finishes with success, failure, or blocked result | `command_id`, `result` |
| `Inspection.ResultCaptured` | First-part or inspection result is captured | `evidence_id` |

## OEP Trace Write-Back

Each command outcome must write to `trace.command_records`.

Each quality result must write to `trace.measurement_results`.

Each exception or containment case must write to `trace.exceptions`.

Each `evidence_id` must be discoverable from the OEP trace through command, measurement, exception, or execution records.
```

- [ ] **Step 2: Extend the human-readable event catalog**

In `docs/ai-native-factory-v1/03-event-catalog.md`, add these rows to the `V1 Event Types` table immediately after `MachineAgent.CommandExecuted`:

```markdown
| MachineAgent.StateObserved | Machine Physical Agent | Machine | Machine state, mode, active program, alarm, or readiness was observed |
| MachineAgent.EvidenceRecorded | Machine Physical Agent | OperationExecutionPackage | Control, quality, health, or human evidence was recorded against an OEP |
| MachineAgent.ContainmentTriggered | Machine Physical Agent | Machine | Feed Hold or alarm stop containment was triggered with post-containment review required |
```

Expected: the existing rows remain, including `MachineAgent.FeedHoldTriggered` for backward-compatible physical stop events.

- [ ] **Step 3: Extend the event envelope schema enum**

In `schemas/events/v1/event-envelope.schema.json`, replace the `event_type.enum` array with this exact list:

```json
[
  "Order.Received",
  "Drawing.Registered",
  "Quote.Proposed",
  "Quote.HumanReviewed",
  "ProcessPlan.Proposed",
  "ProcessPlan.HumanReviewed",
  "OEP.Drafted",
  "OEP.GateChecked",
  "OEP.Approved",
  "OEP.Released",
  "MachineAgent.CommandRequested",
  "MachineAgent.CommandExecuted",
  "MachineAgent.StateObserved",
  "MachineAgent.EvidenceRecorded",
  "MachineAgent.ContainmentTriggered",
  "MachineAgent.FeedHoldTriggered",
  "Inspection.ResultCaptured",
  "Exception.Opened",
  "Exception.Closed",
  "Decision.Recorded",
  "Knowledge.CandidateCreated"
]
```

- [ ] **Step 4: Write event examples**

Create `examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json` with this content:

```json
[
  {
    "event_id": "EVT-JTGK-000001",
    "event_type": "MachineAgent.StateObserved",
    "source": "Machine Physical Agent",
    "subject": "MC-JTGK-800I-001",
    "time": "2026-05-16T09:01:00+08:00",
    "schema_version": "1.0",
    "correlation_id": "CORR-JTGK-PILOT-001",
    "causation_id": null,
    "actor": { "type": "machine", "id": "MPA-JTGK-800I-001" },
    "payload": {
      "package_id": "OEP-JTGK-PILOT-001",
      "evidence_id": "EVD-JTGK-A-0001",
      "machine_state": "staged",
      "active_program_ref": "NC-JTGK-DRY-001:V1"
    }
  },
  {
    "event_id": "EVT-JTGK-000002",
    "event_type": "MachineAgent.EvidenceRecorded",
    "source": "Machine Physical Agent",
    "subject": "OEP-JTGK-PILOT-001",
    "time": "2026-05-16T11:20:10+08:00",
    "schema_version": "1.0",
    "correlation_id": "CORR-JTGK-PILOT-001",
    "causation_id": "EVT-JTGK-000001",
    "actor": { "type": "machine", "id": "MPA-JTGK-800I-001" },
    "payload": {
      "evidence_id": "EVD-JTGK-B-0001",
      "evidence_plane": "quality",
      "record_type": "first_part_result"
    }
  },
  {
    "event_id": "EVT-JTGK-000003",
    "event_type": "MachineAgent.ContainmentTriggered",
    "source": "Machine Physical Agent",
    "subject": "MC-JTGK-800I-001",
    "time": "2026-05-16T14:05:05+08:00",
    "schema_version": "1.0",
    "correlation_id": "CORR-JTGK-PILOT-001",
    "causation_id": "EVT-JTGK-000002",
    "actor": { "type": "machine", "id": "MPA-JTGK-800I-001" },
    "payload": {
      "package_id": "OEP-JTGK-PILOT-001",
      "command_id": "MCMD-JTGK-C-HOLD-001",
      "exception_id": "EXC-JTGK-C-001",
      "containment_reason": "spindle_load_threshold_exceeded_during_controlled_test",
      "post_containment_review_required": true
    }
  }
]
```

- [ ] **Step 5: Verify event artifacts**

Run:

```powershell
Get-Content -Raw 'schemas/events/v1/event-envelope.schema.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json' | ConvertFrom-Json | Out-Null
rg -n "MachineAgent.StateObserved|MachineAgent.EvidenceRecorded|MachineAgent.ContainmentTriggered" docs/ai-native-factory-v1/03-event-catalog.md schemas/events/v1/event-envelope.schema.json docs/ai-native-factory-v1/jtgk-800i/03-event-and-command-map.md examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json
```

Expected: JSON parsing succeeds; search returns matches in all four paths.

- [ ] **Step 6: Commit event map**

Run:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i/03-event-and-command-map.md docs/ai-native-factory-v1/03-event-catalog.md schemas/events/v1/event-envelope.schema.json examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json
git commit -m "docs: map JTGK machine events and commands"
```

Expected: Git creates one commit for the event catalog/schema extension and examples.

## Task 5: Write The A/B/C Pilot Sprint Runbook

**Files:**
- Create: `docs/ai-native-factory-v1/jtgk-800i/04-pilot-sprint-runbook.md`

- [ ] **Step 1: Write the pilot runbook**

Create `docs/ai-native-factory-v1/jtgk-800i/04-pilot-sprint-runbook.md` with this content:

```markdown
# 04 Pilot Sprint Runbook

## Purpose

Run the JTGK-800i physical agent through dry trace, first-part validation, and production-like replay in one concentrated sprint.

## Preparation

Before Slice A starts:

- Machine identity `MC-JTGK-800I-001` exists.
- Machine agent identity `MPA-JTGK-800I-001` exists.
- OEP `OEP-JTGK-PILOT-001` exists with Plan, Gate, and Trace sections.
- Operator id exists.
- NC program id/version is bound or ready for controlled manual confirmation.
- Fixture, pallet, and tool references exist.
- Edge HMI or scanner can record controlled manual confirmations.
- Event and evidence examples parse.
- Safety boundary is reviewed by machine owner.

## Slice A: Dry Trace

### Goal

Prove traceability without cutting.

### Sequence

1. Operator scans or confirms OEP id.
2. Operator scans or confirms NC program id/version.
3. Edge agent records machine identity and mode.
4. Edge agent requests `read_machine_state`.
5. Edge agent records `MachineAgent.StateObserved`.
6. Edge agent records program binding evidence.
7. OEP trace receives command result and evidence references.

### Exit Evidence

- One `MachineAgent.StateObserved` event.
- One `MachineAgent.EvidenceRecorded` event for program binding.
- One control-plane evidence record.
- One human-plane evidence record for operator confirmation.
- OEP trace can reconstruct machine, operator, NC program, approval, and command result.

## Slice B: First-Part Validation

### Goal

Run a simple real part and attach quality evidence to the same OEP trace.

### Sequence

1. Operator confirms fixture and pallet identity.
2. Operator confirms tool assembly identity.
3. Edge agent requests approved tool-setting or tool-break check command when available.
4. Edge agent requests approved probing macro or records controlled inspection write-back.
5. Quality owner records first-part pass/fail disposition.
6. Edge agent records quality-plane evidence.
7. OEP trace receives measurement result and evidence references.

### Exit Evidence

- Tool or fixture confirmation evidence.
- First-part quality evidence.
- Measurement result in OEP trace.
- Quality owner disposition.
- OEP trace connects produced part, tool, fixture, NC program, operator, and quality result.

## Slice C: Production-Like Replay

### Goal

Capture production-like execution, health evidence, and one controlled exception or simulated exception.

### Sequence

1. Edge agent records health evidence during a bounded execution window.
2. Operator or edge agent opens a controlled exception.
3. Edge agent triggers feed hold or alarm stop only if containment criteria are met.
4. Edge agent records `MachineAgent.ContainmentTriggered`.
5. Operator records exception note.
6. Post-containment review records outcome.
7. Execution / Trace Agent or reviewer reconstructs replay from OEP trace.

### Exit Evidence

- Health-plane evidence record.
- Exception record.
- Containment record when containment is exercised.
- Operator note.
- Post-containment review record.
- Replay shows time order across execution, quality, health, human, command, and exception records.

## Stop Conditions

Stop the sprint when:

- A requested action violates the blocked V1 action list.
- Machine owner rejects the safety boundary for the proposed action.
- OEP package, NC program, machine, operator, tool, or fixture identity cannot be confirmed.
- Quality result cannot be tied to the OEP operation.
- Containment action cannot be reviewed after the event.
```

- [ ] **Step 2: Verify runbook coverage**

Run:

```powershell
rg -n "Slice A: Dry Trace|Slice B: First-Part Validation|Slice C: Production-Like Replay|MachineAgent.StateObserved|MachineAgent.ContainmentTriggered|Stop Conditions" docs/ai-native-factory-v1/jtgk-800i/04-pilot-sprint-runbook.md
```

Expected: matches for every listed phrase.

- [ ] **Step 3: Commit pilot runbook**

Run:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i/04-pilot-sprint-runbook.md
git commit -m "docs: define JTGK pilot sprint runbook"
```

Expected: Git creates one commit for the pilot sprint runbook.

## Task 6: Define Operator HMI And Approval Flow

**Files:**
- Create: `docs/ai-native-factory-v1/jtgk-800i/05-operator-hmi-and-approval-flow.md`

- [ ] **Step 1: Write the operator workflow**

Create `docs/ai-native-factory-v1/jtgk-800i/05-operator-hmi-and-approval-flow.md` with this content:

```markdown
# 05 Operator HMI And Approval Flow

## Purpose

Keep operator workflow fast enough that traceability is used during real machine work.

## HMI Principles

- Prefer scan or tap confirmation over typed entry.
- Display only the current OEP, machine, NC program, tool, fixture, pallet, and next approved action.
- Separate normal approved commands from protective containment.
- Record operator notes only when an exception or review requires explanation.
- Never ask the operator to confirm a fact already read directly from CNC, PLC, sensor, or service with trustworthy quality.

## Required Screens

| Screen | Required Fields | Output |
|---|---|---|
| Package bind | OEP id, part id, operation id, NC program id/version | human-plane evidence |
| Setup confirm | fixture id, pallet id, tool assembly ids, operator id | human-plane evidence |
| Gate review | gate status, missing evidence, approval id | approval reference |
| Command request | command type, safety class, command id, required approval | command request |
| Command result | result, timestamp, machine state, evidence links | command record |
| Exception note | exception id, reason code, operator note, owner | exception record |
| Containment review | command id, containment reason, machine state, reviewer, disposition | post-containment review |

## Normal Command Approval

Normal command path:

1. OEP is released or staged.
2. Required gate is passed or explicitly waived.
3. Human approval exists.
4. Operator sees command type and target context.
5. Edge agent sends command or records controlled fallback.
6. Edge agent records command result and evidence id.

Normal command types:

- `bind_nc_program`
- `download_nc_program`
- `read_machine_state`
- `trigger_probe_macro`
- `trigger_tool_setting_macro`
- `trigger_tool_break_check`
- `write_measurement_macro_variable`

## Protective Containment

Containment path:

1. Edge agent or operator detects protective condition.
2. Edge agent may trigger `trigger_feed_hold` or `raise_alarm_stop`.
3. Event `MachineAgent.ContainmentTriggered` is recorded.
4. Exception is opened.
5. Operator note is captured.
6. Post-containment review is required before the run is closed.

Containment is not production release authority. It is a protective action with mandatory review.

## Scan IDs

Use these stable prefixes:

| Object | Prefix Example |
|---|---|
| OEP | `OEP-JTGK-PILOT-001` |
| Machine | `MC-JTGK-800I-001` |
| Machine Agent | `MPA-JTGK-800I-001` |
| NC Program | `NC-JTGK-FIRSTPART-001:V1` |
| Tool Assembly | `TASM-D10-001:V1` |
| Fixture | `FIX-JTGK-001:V1` |
| Pallet | `PAL-JTGK-001:V1` |
| Operator | `OP-JTGK-001` |
| Approval | `APP-JTGK-B-001` |
| Command | `MCMD-JTGK-B-PROBE-001` |
| Evidence | `EVD-JTGK-B-0001` |
| Exception | `EXC-JTGK-C-001` |
```

- [ ] **Step 2: Verify workflow anchors**

Run:

```powershell
rg -n "Package bind|Setup confirm|Gate review|Command request|Protective Containment|MachineAgent.ContainmentTriggered|MCMD-JTGK-B-PROBE-001" docs/ai-native-factory-v1/jtgk-800i/05-operator-hmi-and-approval-flow.md
```

Expected: matches for every listed phrase.

- [ ] **Step 3: Commit operator workflow**

Run:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i/05-operator-hmi-and-approval-flow.md
git commit -m "docs: define JTGK operator approval flow"
```

Expected: Git creates one commit for the operator workflow.

## Task 7: Define Acceptance Checklist

**Files:**
- Create: `docs/ai-native-factory-v1/jtgk-800i/06-acceptance-checklist.md`

- [ ] **Step 1: Write the checklist**

Create `docs/ai-native-factory-v1/jtgk-800i/06-acceptance-checklist.md` with this content:

```markdown
# 06 Acceptance Checklist

## Artifact Acceptance

| Check | Pass Rule |
|---|---|
| Machine package exists | `docs/ai-native-factory-v1/jtgk-800i/README.md` exists |
| Machine profile exists | JTGK-800i, JT810, `MC-JTGK-800I-001`, and `MPA-JTGK-800I-001` are recorded |
| Evidence schema parses | `execution-evidence.schema.json` parses as JSON |
| Evidence examples parse | `execution-evidence-example.json` parses as JSON |
| Event schema parses | `event-envelope.schema.json` parses after new event types are added |
| Event examples parse | `event-envelope-examples.json` parses as JSON |
| A/B/C runbook exists | Dry Trace, First-Part Validation, and Production-Like Replay sections exist |
| Operator workflow exists | Normal command and containment flows are documented |

## Slice A Dry Trace Acceptance

| Check | Pass Rule |
|---|---|
| OEP binding | OEP id, operation id, machine id, operator id, and NC program id/version are recorded |
| Machine state | Machine state is captured through direct read or controlled manual fallback |
| Approval | Approval id is attached to normal commands |
| Command result | `read_machine_state` and program binding results are recorded |
| Replay | Trace reconstructs package, machine, operator, program, approval, and command result |

## Slice B First-Part Validation Acceptance

| Check | Pass Rule |
|---|---|
| Setup context | Fixture, pallet, tool assembly, operator, part, and material context are recorded |
| Tool check | Tool setting or break-check result is recorded when available |
| Measurement | Probe, inspection, or controlled measurement write-back is recorded |
| Quality result | First-part pass/fail disposition is recorded by quality owner |
| Replay | Trace connects produced part, quality result, tool, fixture, NC program, and operator |

## Slice C Production-Like Replay Acceptance

| Check | Pass Rule |
|---|---|
| Health evidence | At least one health-plane record is attached to OEP |
| Exception | A controlled exception or simulated exception is opened |
| Containment | Feed hold or alarm stop is recorded only when containment criteria are met |
| Review | Post-containment review is recorded when containment occurs |
| Replay | Time-ordered replay includes execution, quality, health, human, command, and exception evidence |

## Safety Acceptance

| Blocked Action | Pass Rule |
|---|---|
| Autonomous CNC cycle start | No command, HMI flow, or runbook step permits it |
| Autonomous NC edit-and-run | No command, HMI flow, or runbook step permits it |
| Closed-loop feed override | No command, HMI flow, or runbook step permits it |
| Safety parameter write | No command, HMI flow, or runbook step permits it |
| Quality concession without approval | Quality owner approval is required |
```

- [ ] **Step 2: Verify checklist coverage**

Run:

```powershell
rg -n "Artifact Acceptance|Slice A Dry Trace Acceptance|Slice B First-Part Validation Acceptance|Slice C Production-Like Replay Acceptance|Safety Acceptance|Autonomous CNC cycle start" docs/ai-native-factory-v1/jtgk-800i/06-acceptance-checklist.md
```

Expected: matches for every listed phrase.

- [ ] **Step 3: Commit acceptance checklist**

Run:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i/06-acceptance-checklist.md
git commit -m "docs: define JTGK pilot acceptance checks"
```

Expected: Git creates one commit for the acceptance checklist.

## Task 8: Final Verification

**Files:**
- Verify: `docs/ai-native-factory-v1/jtgk-800i/*.md`
- Verify: `schemas/machine-agent/v1/execution-evidence.schema.json`
- Verify: `schemas/events/v1/event-envelope.schema.json`
- Verify: `examples/ai-native-factory-v1/jtgk-800i/*.json`

- [ ] **Step 1: Verify all expected files exist**

Run:

```powershell
$paths = @(
  'docs/ai-native-factory-v1/jtgk-800i/README.md',
  'docs/ai-native-factory-v1/jtgk-800i/01-machine-profile-and-interface-freeze.md',
  'docs/ai-native-factory-v1/jtgk-800i/02-evidence-model.md',
  'docs/ai-native-factory-v1/jtgk-800i/03-event-and-command-map.md',
  'docs/ai-native-factory-v1/jtgk-800i/04-pilot-sprint-runbook.md',
  'docs/ai-native-factory-v1/jtgk-800i/05-operator-hmi-and-approval-flow.md',
  'docs/ai-native-factory-v1/jtgk-800i/06-acceptance-checklist.md',
  'schemas/machine-agent/v1/execution-evidence.schema.json',
  'examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json',
  'examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json'
)
$paths | ForEach-Object { "$_ => $(Test-Path $_)" }
```

Expected: every line ends with `True`.

- [ ] **Step 2: Verify JSON parsing**

Run:

```powershell
Get-Content -Raw 'schemas/machine-agent/v1/execution-evidence.schema.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'schemas/events/v1/event-envelope.schema.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'examples/ai-native-factory-v1/jtgk-800i/execution-evidence-example.json' | ConvertFrom-Json | Out-Null
Get-Content -Raw 'examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json' | ConvertFrom-Json | Out-Null
```

Expected: no output and exit code 0.

- [ ] **Step 3: Verify design coverage**

Run:

```powershell
rg -n "traceable execution|quality|health|Dry Trace|First-Part Validation|Production-Like Replay|containment|Autonomous CNC cycle start|JT810|MC-JTGK-800I-001|MPA-JTGK-800I-001" docs/ai-native-factory-v1/jtgk-800i schemas/machine-agent/v1/execution-evidence.schema.json examples/ai-native-factory-v1/jtgk-800i
```

Expected: matches across the machine profile, evidence model, runbook, workflow, checklist, schema, and examples.

- [ ] **Step 4: Verify event schema accepts new event names by search**

Run:

```powershell
rg -n '"MachineAgent.StateObserved"|"MachineAgent.EvidenceRecorded"|"MachineAgent.ContainmentTriggered"' schemas/events/v1/event-envelope.schema.json docs/ai-native-factory-v1/03-event-catalog.md examples/ai-native-factory-v1/jtgk-800i/event-envelope-examples.json
```

Expected: all three event types appear in schema, catalog, and examples.

- [ ] **Step 5: Check git state**

Run:

```powershell
git status --short
```

Expected: only files intentionally modified by the current task sequence are staged or modified. Existing unrelated workspace changes may still appear; do not stage or revert them.

- [ ] **Step 6: Commit final cleanup if verification caused edits**

Run only if final verification led to file edits:

```powershell
git add docs/ai-native-factory-v1/jtgk-800i schemas/machine-agent/v1/execution-evidence.schema.json schemas/events/v1/event-envelope.schema.json examples/ai-native-factory-v1/jtgk-800i docs/ai-native-factory-v1/03-event-catalog.md
git commit -m "docs: complete JTGK execution-spine pilot artifacts"
```

Expected: Git creates a cleanup commit, or reports no changes if every prior task was already committed cleanly.

## Execution Notes

Keep implementation artifact-first. Do not add live CNC control, sensor-driver code, or HMI application code until the machine profile, evidence schema, event mapping, pilot runbook, and acceptance checklist are reviewed.

When execution begins, use one task commit at a time. After each task, run the verification command in that task and inspect `git diff --cached --stat` before committing.
