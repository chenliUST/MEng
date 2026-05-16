# 04 Offline Chain Runbook

## Purpose

Run the first-order chain offline before controlled physical execution.

Offline means the system may generate quote, process, OEP, DecisionLog, and event records without sending commands to the machine.

## Entry Criteria

- First-order sample is frozen.
- Validation machine candidate is frozen.
- Minimum resource master data exists.
- Process, CAM, machine, quality, system, and Agent operators are assigned.
- OEP schema, event envelope schema, Agent contract schema, and Machine Physical Agent interface schema parse successfully.

## Sequence

### 1. Intake

Create object records for CustomerOrder, Part, Drawing, CADModel, and source attachments.

Evidence:

- Object ids and versions.
- Order.Received event.
- Drawing.Registered event.

### 2. Quote / DFM

Run Intake / DFM / Quote Agent against the frozen sample.

Evidence:

- Quotation draft with version.
- Quote.Proposed event.
- DecisionLog with adoption_status.
- Human review record if the quote is used beyond offline comparison.

### 3. Process / CAPP / CAM

Run Process Agent and process-owner review.

Evidence:

- ProcessPlan version.
- Operation version.
- SetupPlan version.
- NCProgram version or imported CAM/NC reference.
- ProcessPlan.Proposed event.
- DecisionLog with adoption_status.

### 4. OEP Draft

Run Package / Gate Agent to create one L2 Operation Execution Package draft.

Evidence:

- OEP Draft with Plan, Gate, and Trace.
- All gate fields present.
- Gate status values restricted to pending, passed, failed, or waived.
- OEP.Drafted event.

### 5. Offline Gate Check

Evaluate gates without releasing physical execution.

Evidence:

- Engineering Gate checks version consistency.
- Resource Gate checks machine, tool, fixture, pallet, material lot, operator, and skill availability.
- Tool Gate checks identity and life status.
- Fixture Gate checks fixture and pallet identity.
- Simulation Gate records available simulation or explicit missing-evidence failure.
- Quality Gate checks inspection plan and critical characteristics.
- Authority Gate remains pending until formal Phase 1 approval.

### 6. Gap Review

Create a gap list that separates Phase 0 offline gaps from Phase 1 execution blockers.

Evidence:

- Blocking gaps tied to gate names.
- Owner for each gap.
- Date for next review.
- DecisionLog for any Agent recommendation accepted, modified, or rejected.

## Exit Criteria

Phase 0 offline chain passes when:

- One quote draft exists.
- One process draft exists.
- One OEP draft exists and parses as JSON when exported.
- Gate gaps are explicit and owned.
- Agent recommendations have adoption status.
- No physical command has been sent to the validation machine.

## Stop Conditions

Stop the offline chain when:

- Drawing or CAD revision is unresolved.
- The process cannot be bounded to one validation-machine OEP.
- Required OEP resources cannot be represented.
- Quality characteristics cannot be measured.
- A proposed action violates V1 blocked actions.
