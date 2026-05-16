# JTGK-800i Execution-Spine Physical Agent Design

## Context

The first physical agent will be built around a legacy JTGK-800i CNC engraving and milling center. The supplied machine material identifies the machine as a JTGK-800i platform with JT810 CNC, 700/800/350 mm X/Y/Z travel, 15 kW 24000 rpm BBT30 spindle, 24-tool magazine, 750 x 800 mm work table, 800 kg table load, 380 V power, about 20 kW total installed power, and 0.6 MPa compressed air with 210 L/min demand.

The broader AI Native Factory V1 architecture already defines Operation Execution Package, event contracts, agent contracts, and a generic Machine Physical Agent interface. This design specializes that architecture for the first machine retrofit.

## Mission

The first JTGK-800i physical agent is an Execution-Spine Agent. Its primary job is not autonomy. Its job is to make machine execution observable, governed, replayable, and learnable.

The OEP is the execution contract. The physical agent attaches machine facts, quality evidence, health evidence, human confirmations, approvals, commands, exceptions, and outcomes to that contract.

Quality and machine-health data are first-class execution evidence. They are not side telemetry streams.

## Pilot Ramp

The pilot should run as one concentrated sprint with three quick slices.

### Slice A: Dry Trace

Run a no-cut execution package. Prove OEP binding, NC program and version binding, machine identity, operator confirmation, machine state capture, approval records, command and result records, alarm and status capture, and replayable trace.

Exit evidence: one complete OEP trace for a no-cut run.

### Slice B: First-Part Validation

Run a simple real part. Add tool setting or tool-break check, fixture and tool confirmation, probing or inspection write-back, first-part quality evidence, measurement record, and quality exception path if the result fails.

Exit evidence: one complete OEP trace that connects produced part, quality result, tool context, fixture context, and machine execution context.

### Slice C: Production-Like Replay

Run a production-like operation with at least one controlled exception or simulated exception. Capture health signals, containment path if needed, operator note, root-cause tags, DecisionLog entry, and replay showing what happened in time order.

Exit evidence: one replayable run with execution, quality, health, human, approval, and exception evidence attached to the same OEP.

## Architecture

The physical agent has three main zones.

### Machine Body

The machine body includes the JTGK-800i, JT810 CNC, PLC, spindle, 24-tool magazine, work table, fixture, local operator panel, and existing safety and control circuits.

This remains the protected machine boundary. Real-time safety and machine motion authority stay with the CNC, PLC, safety circuits, and human operator.

### Edge Physical Agent

An industrial IPC or edge AI box sits beside the machine. It provides:

- OEP binding.
- Gate judgment.
- Command orchestration.
- Sensor fusion.
- Local event buffer.
- Trace writer.
- Explanation log.
- Edge HMI or scanner integration.

Allowed V1 actions:

- Bind or download NC program while CNC cycle start remains human-operated.
- Read machine state, alarms, active program identity, and approved macro variables.
- Trigger approved probing, tool-setting, and tool-break macros.
- Write approved measurement macro variables or documented handshake variables.
- Trigger feed hold or alarm stop for protective containment, with containment reason and post-containment review.

Blocked V1 actions:

- Autonomous CNC cycle start.
- Autonomous NC edit-and-run.
- Closed-loop feed override.
- Material substitution without engineering and quality approval.
- Quality concession without quality-owner approval.

### Factory Services

Factory services include OEP Service, Object Service, Event Bus, DecisionLog, quality records, and learning store.

They provide:

- Versioned package context.
- Approval state.
- Actor identity.
- Machine, tool, fixture, pallet, material, and part references.
- Event storage.
- Exception review.
- Replay and learning datasets.

## Evidence Model

Every record should be tied to the execution spine. At minimum, records should carry:

- `package_id`
- `operation_id`
- `machine_agent_id`
- `machine_id`
- `timestamp`
- `source`
- `record_type`
- `data_quality`
- `tool_ref` when applicable
- `fixture_ref` when applicable
- `operator_ref` when applicable
- `nc_program_ref` when applicable
- `part_ref` or material context when applicable

Evidence planes:

| Plane | Purpose | Examples |
|---|---|---|
| Control plane | Prove execution state and governed action | CNC state, program, mode, alarm, command result, approval |
| Quality plane | Prove setup and part result | Probe result, tool setter, break check, first-part result, inspection reference, setup photo |
| Health plane | Capture machine and process condition | Spindle load, current, vibration, air pressure, coolant state, temperature, cycle timing |
| Human plane | Capture human authority and context | Operator scan, approval, setup confirmation, exception note |

The design priority is context binding before data volume. High-frequency health data is useful only when it is linked to OEP, operation, tool, fixture, machine state, and time.

## Sensor And Interface Plan

### Minimum For Slice A

- CNC or PLC read path for state, alarms, mode, active program, and available macro variables.
- Edge HMI or scanner for operator, package, NC program, fixture, and tool confirmation.
- Local event buffer.
- OEP trace writer.
- Command result capture for read-state and bind/download actions.

If direct CNC access is limited, manual or scanner-backed confirmation can be used for the first dry trace while preserving the same data contract.

### Minimum For Slice B

- Workpiece probe or inspection write-back path.
- Laser tool setter or tool-break check where available.
- Tool identity confirmation.
- Fixture and pallet identity confirmation.
- First-part quality result capture.
- Setup evidence photo capture if practical.

### Minimum For Slice C

- Spindle load or current capture.
- Vibration capture.
- Air pressure capture.
- Coolant state capture.
- Machine or environment temperature capture.
- Exception event capture.
- Containment action record.
- Operator note capture.

Enhanced sensors should be installed early when they do not block the A/B/C sprint. They should not delay the trace spine.

## Agent Behavior

The edge physical agent runs a controlled loop.

1. Observe machine state, package binding, sensor streams, operator confirmations, and gate status.
2. Interpret the current execution state.
3. Gate commands against OEP, NC program, machine, operator, tool, fixture, and approval context.
4. Request or execute only approved commands for normal action.
5. Contain only for protective cases, such as feed hold or alarm stop, with containment reason and post-containment review.
6. Record observations, commands, results, exceptions, approvals, and explanations into OEP trace and event log.

Execution states:

- unbound
- staged
- ready_for_dry_trace
- ready_for_first_part
- executing
- measuring
- completed
- blocked
- exception
- containment

## Safety And Authority

Safety authority is explicit:

| Authority Area | Owner In V1 |
|---|---|
| Real-time safety | CNC, PLC, safety circuits |
| Physical cycle start | Human operator |
| OEP release and gate state | OEP Service and approved workflow |
| Normal physical commands | Edge agent after gate and approval |
| Protective containment | Edge agent within narrow feed-hold or alarm-stop boundary |
| NC code creation and edit approval | Human engineering or CAM owner |
| Trace, replay, and explanation | Edge agent plus factory services |

The edge agent may explain risk, request action, execute approved commands, and trigger narrow containment. It must not replace certified safety control.

## Preparation Deliverables

Before running the concentrated pilot sprint, prepare:

- Machine identity record for the JTGK-800i.
- OEP fields required for machine execution.
- Event schema mapping for execution, quality, health, and human evidence.
- Command schema mapping for allowed V1 actions.
- Sensor naming convention.
- Network boundary and edge deployment plan.
- Approval and actor identity rules.
- Safety authority statement.
- Local buffer and central trace-store target.
- Operator scan or HMI flow.

## Risks

| Risk | Impact | Mitigation |
|---|---|---|
| CNC/PLC interface uncertainty | Dry trace may stall if direct state read is unavailable | Preserve data contract and use scanner/HMI confirmation as temporary input |
| Sensor overreach | Hardware work delays the sprint | Install enhanced sensors early only when they do not block A/B/C |
| Authority creep | V1 accidentally expands into unsafe autonomy | Keep cycle start, NC edit-and-run, feed override, and certified safety outside edge authority |
| Evidence without context | Quality and health data cannot support replay or learning | Require OEP, operation, machine, time, tool, fixture, and source context on evidence records |
| Operator workflow friction | Operators bypass the system | Use barcode/QR confirmation and keep required inputs minimal |

## Decisions For Implementation Planning

The implementation plan must resolve:

- Exact JT810/JTGK interface available for state, alarms, active program, macro variables, and program transfer.
- Probe and tool setter hardware status.
- Tool, fixture, and pallet identity method: barcode, QR, RFID, or manual fallback.
- First simple part and process used for Slice B and Slice C.
- Minimum machine-health sensor set installed before the pilot sprint starts.
- Event storage target for local buffer and central trace store.
- Approval UI for normal commands and post-containment review.

## Success Criteria

The design is successful when the first machine can produce three replayable OEP traces in quick succession:

- A dry trace with no cutting.
- A first-part validation trace with quality evidence.
- A production-like replay trace with health evidence and at least one exception or simulated exception.

In all three traces, execution, quality, health, human, approval, and exception evidence should share the same OEP execution spine.
