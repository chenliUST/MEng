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
4. Edge agent requests approved `bind_nc_program` command and records `MachineAgent.CommandRequested`.
5. Edge agent executes or records controlled fallback for `bind_nc_program` and records `MachineAgent.CommandExecuted`.
6. Edge agent records program binding evidence.
7. Edge agent requests `read_machine_state` and records `MachineAgent.CommandRequested`.
8. Edge agent executes `read_machine_state` and records `MachineAgent.CommandExecuted`.
9. Edge agent records `MachineAgent.StateObserved`.
10. OEP trace receives command results, evidence references, and `trace.command_records`.

### Exit Evidence

- One `MachineAgent.StateObserved` event.
- One `MachineAgent.EvidenceRecorded` event for program binding.
- `MachineAgent.CommandRequested` and `MachineAgent.CommandExecuted` events for `bind_nc_program`.
- `MachineAgent.CommandRequested` and `MachineAgent.CommandExecuted` events for `read_machine_state`.
- `trace.command_records` entries for `bind_nc_program` and `read_machine_state`.
- One control-plane evidence record.
- One human-plane evidence record for operator confirmation.
- OEP trace can reconstruct machine, operator, NC program, approval, and command result.

## Slice B: First-Part Validation

### Goal

Run a simple real part and attach quality evidence to the same OEP trace.

### Sequence

1. Operator confirms fixture and pallet identity.
2. Operator confirms tool assembly identity.
3. Edge agent requests approved tool-setting or tool-break check command when available and records `MachineAgent.CommandRequested`.
4. Edge agent executes the approved tool-setting or tool-break check command, or records controlled fallback, and records `MachineAgent.CommandExecuted`.
5. Edge agent requests approved probing macro or measurement write-back command when used and records `MachineAgent.CommandRequested`.
6. Edge agent executes the approved probing or measurement write-back command, or records controlled inspection write-back, and records `MachineAgent.CommandExecuted`.
7. Quality owner records first-part pass/fail disposition.
8. Edge agent records quality-plane evidence.
9. OEP trace receives measurement result, evidence references, and `trace.command_records`.

### Exit Evidence

- Tool or fixture confirmation evidence.
- `MachineAgent.CommandRequested` and `MachineAgent.CommandExecuted` events for tool-setting, tool-break, probe, or measurement write-back commands when used.
- `trace.command_records` entries for each approval-gated command used.
- First-part quality evidence.
- Measurement result in OEP trace.
- Quality owner disposition.
- OEP trace connects produced part, tool, fixture, NC program, operator, and quality result.

## Slice C: Production-Like Replay

### Goal

Capture production-like execution, health evidence, and one controlled exception or simulated exception.

### Containment Criteria

Containment is allowed only when a protective condition is observed, the action is limited to `trigger_feed_hold` or `raise_alarm_stop`, an exception id is opened or linked, a `containment_reason` is recorded, and post-containment review is required.

### Sequence

1. Edge agent records health evidence during a bounded execution window.
2. Operator or edge agent opens or links a controlled exception id.
3. Edge agent records the `containment_reason`.
4. Edge agent requests `trigger_feed_hold` or `raise_alarm_stop` only if containment criteria are met.
5. Edge agent records command result with `command_id` and `exception_id`.
6. Edge agent records `MachineAgent.ContainmentTriggered`.
7. Operator records exception note.
8. Post-containment review records outcome and post-containment review id.
9. Execution / Trace Agent or reviewer reconstructs replay from OEP trace.

### Exit Evidence

- Health-plane evidence record.
- Exception record.
- Containment record when containment is exercised.
- `command_id` for the containment action.
- `exception_id` linked to the containment action.
- `containment_reason` explaining the protective condition.
- Command result for `trigger_feed_hold` or `raise_alarm_stop`.
- Operator note.
- Post-containment review record with post-containment review id.
- Replay shows time order across execution, quality, health, human, command, and exception records.

## Stop Conditions

Stop the sprint when:

- A requested action violates the blocked V1 action list.
- Machine owner rejects the safety boundary for the proposed action.
- OEP package, NC program, machine, operator, tool, or fixture identity cannot be confirmed.
- Quality result cannot be tied to the OEP operation.
- Containment action cannot be reviewed after the event.
