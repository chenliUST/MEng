# 08 First-Order Demo Runbook

## Demo Objective

Run one real historical machining order through the V1 chain and prove that Agent recommendations, OEP release, Machine Physical Agent execution, quality write-back, and knowledge capture are auditable.

## Entry Criteria

- One historical order selected.
- Drawing and CAD version available.
- Part type is simple plate, bracket, fixture, simple housing, or selected medium-complexity case.
- Validation machine selected.
- CAM owner, process owner, machine owner, quality owner, and system owner assigned.
- Required sensing organs installed and verified before controlled physical execution. Phase 0 may record installation dates, but Phase 1 execution cannot pass with missing required sensing organs.
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

Machine Physical Agent may bind or download NC, trigger probe/tool macros, read allowed machine state, write only approved measurement macro variables or handshake variables, and trigger protective Feed Hold if needed. CNC cycle start remains human-operated.

Evidence:

- Command result records
- ExecutionRecord
- Sensor records
- Machine alarms and state records
- Post-containment review record when Feed Hold or alarm stop is triggered

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
