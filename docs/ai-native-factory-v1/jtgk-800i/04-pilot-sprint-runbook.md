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
