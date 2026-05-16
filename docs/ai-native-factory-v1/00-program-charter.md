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
