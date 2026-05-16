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
