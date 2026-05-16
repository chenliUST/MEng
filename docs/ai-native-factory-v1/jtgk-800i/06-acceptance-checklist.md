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
| Command request events | `MachineAgent.CommandRequested` is recorded for approval-gated `bind_nc_program` and `read_machine_state` commands |
| Command execution events | `MachineAgent.CommandExecuted` is recorded with result for approval-gated `bind_nc_program` and `read_machine_state` commands |
| OEP command records | `trace.command_records` receives write-back entries for `bind_nc_program` and `read_machine_state` command outcomes |
| Command result | `read_machine_state` and `bind_nc_program` results are recorded |
| Replay | Trace reconstructs package, machine, operator, program, approval, and command result |

## Slice B First-Part Validation Acceptance

| Check | Pass Rule |
|---|---|
| Setup context | Fixture, pallet, tool assembly, operator, part, and material context are recorded |
| Tool check | Tool setting or break-check requires direct command evidence, controlled fallback evidence, or `blocked_with_owner` status |
| Command request events | `MachineAgent.CommandRequested` is recorded for each approval-gated B-slice command when used |
| Command execution events | `MachineAgent.CommandExecuted` is recorded with result for each approval-gated B-slice command when used |
| OEP command records | `trace.command_records` receives write-back entries for each B-slice approval-gated command when used |
| Measurement | Probe, inspection, or controlled measurement write-back is recorded |
| Quality result | First-part pass/fail disposition is recorded by quality owner |
| Replay | Trace connects produced part, quality result, tool, fixture, NC program, and operator |

## Slice C Production-Like Replay Acceptance

| Check | Pass Rule |
|---|---|
| Health evidence | At least one health-plane record is attached to OEP |
| Exception | A controlled exception or simulated exception is opened |
| Containment | Feed hold or alarm stop is recorded only when containment criteria are met and includes `command_id`, `exception_id`, `containment_reason`, and command result |
| Containment event | `MachineAgent.ContainmentTriggered` is recorded for the containment action |
| Review | Post-containment review records outcome and post-containment review id when containment occurs |
| Replay | Time-ordered replay includes execution, quality, health, human, command, and exception evidence |

## Safety Acceptance

| Blocked Action | Pass Rule |
|---|---|
| Autonomous CNC cycle start | No command, HMI flow, or runbook step permits it |
| Autonomous NC edit-and-run | No command, HMI flow, or runbook step permits it |
| Closed-loop feed override | No command, HMI flow, or runbook step permits it |
| Safety parameter write | No command, HMI flow, or runbook step permits it |
| Quality concession without approval | Quality owner approval is required |
