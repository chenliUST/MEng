# 05 First Workshop Checklist

## Purpose

Run the first Phase 0 workshop and leave with frozen decisions that can drive the offline first-order chain.

This meeting should not debate the whole factory vision. It should freeze one order, one validation machine, one OEP scope, and the minimum evidence needed to start execution planning.

## Required Attendees

| Role | Must Attend | Decision Authority |
|---|---|---|
| Program owner | Yes | Confirms Phase 0 scope and escalation path |
| System owner | Yes | Owns OEP, event, schema, and data contract decisions |
| Process owner | Yes | Approves part suitability, process assumptions, and operation boundary |
| CAM owner | Yes | Confirms CAM/NC availability and simulation evidence path |
| Machine owner | Yes | Confirms validation-machine feasibility and safe action boundary |
| Quality owner | Yes | Confirms measurable characteristics and inspection plan path |
| Edge/controls owner | Yes | Confirms CNC/PLC interface, sensor, edge, and safety boundary |
| Quote owner | Yes | Confirms quote assumptions and commercial review boundary |
| Operator representative | Recommended | Confirms HMI, scanner, setup, and practical workflow fit |

## Pre-Workshop Evidence Pack

Every file or record brought into the meeting must have an owner.

| Evidence | Owner | Use |
|---|---|---|
| Historical order record | Program or quote owner | CustomerOrder and quotation baseline |
| Drawing revision | Process owner | Engineering Gate |
| CAD revision | Process or CAM owner | Engineering Gate and CAM path |
| Historical process route | Process owner | Process Agent seed |
| Historical NC or CAM reference | CAM owner | NCProgram and simulation path |
| Historical inspection report | Quality owner | InspectionPlan seed |
| Historical exception or rework notes | Quality or machine owner | Risk and knowledge capture |
| Validation-machine capability record | Machine owner | Resource Gate |
| CNC/PLC interface notes | Edge/controls owner | Machine Physical Agent feasibility |
| Tool/fixture/material records | Process and machine owners | Resource, Tool, Fixture Gates |

## Agenda

### 1. Scope Lock

Decision:

- First-order Demo is limited to one L2 Operation Execution Package.
- Physical execution remains blocked until Phase 1 gates and required sensors are ready.
- Autonomous CNC cycle start and Feed Override remain blocked.

Output:

- Confirmed first-order scope statement.

### 2. Order And Part Freeze

Decision:

- Freeze CustomerOrder id/version.
- Freeze Part id/version.
- Freeze Drawing id/revision.
- Freeze CADModel id/revision.
- Confirm part family and complexity class.

Output:

- Completed sample-freeze record.

### 3. Operation Boundary

Decision:

- Select the operation/setup for the first OEP.
- Confirm whether CAM/NC exists, must be regenerated, or must be imported.
- Confirm that one validation machine can execute the selected operation.

Output:

- Operation id/version.
- SetupPlan id/version.
- NCProgram id/version or generation path.

### 4. Gate Evidence Map

Decision:

- List evidence needed for each gate.
- Mark each gate as ready, missing evidence, or blocked.

Output:

| Gate | Evidence Owner | Workshop Status |
|---|---|---|
| Engineering Gate | Process owner | ready, missing evidence, or blocked |
| Resource Gate | Machine owner | ready, missing evidence, or blocked |
| Tool Gate | Process or machine owner | ready, missing evidence, or blocked |
| Fixture Gate | Machine owner | ready, missing evidence, or blocked |
| Simulation Gate | CAM owner | ready, missing evidence, or blocked |
| Quality Gate | Quality owner | ready, missing evidence, or blocked |
| Authority Gate | Program owner | ready, missing evidence, or blocked |

### 5. Validation Machine Freeze

Decision:

- Freeze machine_id and machine_capability_version.
- Confirm required sensing organs and install/verification status.
- Confirm enhanced sensing organs included in build scope.
- Confirm controlled command boundary.

Output:

- Machine freeze record.
- Required sensor readiness list.
- Edge/controls feasibility note.

### 6. Offline Chain Assignment

Decision:

- Assign who runs quote/DFM, process draft, OEP draft, and gate gap review.

Output:

| Work Product | Owner | Review Owner |
|---|---|---|
| Quote / DFM draft | Quote owner | Process owner |
| Process draft | Process owner | CAM owner |
| CAM / NC reference | CAM owner | Machine owner |
| OEP draft | System owner | Process owner |
| Gate gap list | System owner | Program owner |
| Quality plan seed | Quality owner | Process owner |

## Exit Criteria

The workshop is complete only when these decisions are recorded:

- One order is selected or rejected with explicit reason.
- One part definition is frozen or rejected with explicit reason.
- One validation machine is selected or rejected with explicit reason.
- One first-OEP operation boundary is selected or rejected with explicit reason.
- Gate evidence owners are assigned.
- Offline chain owners are assigned.
- Phase 1 physical execution blockers are listed.

## Meeting Failure Conditions

Stop and reschedule when:

- No one can confirm drawing or CAD revision.
- No one owns CAM/NC evidence.
- No validation machine owner can confirm interface feasibility.
- No quality owner can confirm measurable characteristics.
- The selected order requires blocked V1 actions.

## After-Workshop Artifacts

The system owner updates:

- `01-first-order-sample-freeze.md` records.
- `02-validation-machine-freeze.md` records.
- `03-resource-master-data-freeze.md` records.
- `04-offline-chain-runbook.md` gap list.
- Example OEP draft or actual first-order OEP export.

The program owner confirms whether Phase 0 offline chain can start.
