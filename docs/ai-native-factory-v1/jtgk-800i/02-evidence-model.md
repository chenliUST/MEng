# 02 Evidence Model

## Rule

Every machine-side record must attach to the OEP execution spine. A record that cannot identify package, operation, machine agent, source, timestamp, and evidence plane is not pilot evidence.

## Required Context

Each evidence record carries:

- `evidence_id`
- `package_id`
- `operation_id`
- `machine_agent_id`
- `machine_id`
- `timestamp`
- `evidence_plane`
- `record_type`
- `source`
- `data_quality`
- `context_refs`
- `payload`

## Evidence Planes

| Plane | Meaning | Pilot Examples |
|---|---|---|
| control | Execution state and governed command evidence | active program, alarm state, command result, gate result |
| quality | Setup, tool, measurement, and inspection evidence | probe result, tool break check, first-part result, setup photo |
| health | Machine and process condition evidence | spindle load, current, vibration, air pressure, coolant, temperature |
| human | Operator authority and explanation evidence | scan confirmation, approval, setup note, exception note |

## Data Quality Values

| Value | Meaning |
|---|---|
| direct_read | Read directly from CNC, PLC, DAQ, sensor, or service |
| controlled_manual | Entered by operator through controlled HMI/scanner workflow |
| imported_record | Imported from inspection, CAM, or external record system |
| simulated | Created in dry trace or controlled simulation |

## Context References

Use these keys when known:

- `nc_program_ref`
- `tool_ref`
- `fixture_ref`
- `pallet_ref`
- `operator_ref`
- `part_ref`
- `material_lot_ref`
- `approval_ref`
- `command_ref`
- `exception_ref`

## A/B/C Coverage

| Slice | Required Evidence |
|---|---|
| A Dry Trace | control and human evidence for OEP binding, NC version, machine state, approval, and command result |
| B First-Part Validation | quality evidence for tool check, fixture/tool confirmation, measurement, and first-part result |
| C Production-Like Replay | health evidence, exception evidence, containment record, and replayable operator note |
