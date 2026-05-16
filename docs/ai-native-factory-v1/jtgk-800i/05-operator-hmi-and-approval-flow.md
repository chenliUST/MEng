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
| Gate review | gate status, missing evidence | `approval_id` |
| Command request | command type, safety class, command_id, approval_id for approval-gated commands | command request |
| Command result | result, timestamp, machine state, evidence links | command record |
| Exception note | exception_id, reason code, operator note, owner | exception record |
| Containment review | command_id, containment_reason, machine state, reviewer, disposition | post-containment review |

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
2. Edge agent opens or links `exception_id`.
3. Edge agent records `containment_reason` and `command_id` for the protective action.
4. Edge agent triggers `trigger_feed_hold` or `raise_alarm_stop` only when containment criteria are met.
5. Edge agent records command result for `command_id`.
6. Event `MachineAgent.ContainmentTriggered` is recorded with `command_id`, `exception_id`, `containment_reason`, command result, and post-containment review required.
7. Operator note is captured.
8. Post-containment review is required before the run is closed.

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
