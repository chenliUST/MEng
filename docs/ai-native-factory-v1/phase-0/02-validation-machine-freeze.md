# 02 Validation Machine Freeze

## Purpose

Select the first validation machine and freeze the machine-side scope for Phase 0 and Phase 1.

The validation machine must be able to prove L2 controlled execution while installing L3 sensing hardware for evidence and learning.

## Required Machine Record

| Field | Freeze Rule |
|---|---|
| machine_id | Stable id used by OEP and Machine Physical Agent |
| machine_type | Machining center, turning center, mill-turn, grinding, or other controlled type |
| cnc_vendor_and_model | Required for interface feasibility |
| plc_vendor_and_model | Required for interface and safety boundary |
| machine_capability_version | Increment when capability, interface, or safety boundary changes |
| work_envelope | Travel and fixture limits relevant to selected part |
| spindle_capability | Speed, power, torque range relevant to selected operation |
| probing_capability | Workpiece probe availability and macro strategy |
| tool_setting_capability | Laser or contact tool setting and break detection strategy |
| network_boundary | Plant network, edge network, and isolated machine network rule |
| machine_owner | Accountable owner for readiness and safe operation |

## Required Sensing Organs

These must be installed and verified before Phase 1 controlled physical execution:

| Organ | Verification Evidence |
|---|---|
| CNC/PLC data interface | Machine status, program, alarm, load, and macro-variable read test |
| Workpiece probe | Probe macro dry run or controlled test result |
| Laser tool setter / break detection | Tool check result or dry run record |
| Tool identity confirmation | Barcode, RFID, preset record, or controlled manual confirmation |
| Fixture identity confirmation | Barcode, RFID, or controlled manual confirmation |
| Pallet identity confirmation | Barcode, RFID, or controlled manual confirmation |
| Edge HMI / scanner | Operator confirmation and command request capture |

## Enhanced Sensing Organs

These are included in the validation-machine build scope and used first for evidence, labels, offline analysis, and Agent explanation:

| Organ | Phase 1 Use |
|---|---|
| Vibration sensor | Cutting-state evidence and anomaly label |
| Industrial camera or line laser | Setup evidence and visual trace |
| Spindle power/current acquisition | Quote and process calibration evidence |
| Temperature sensor | Machine and environment context |
| Coolant sensor | Process condition trace |
| Air pressure sensor | Fixture and auxiliary condition trace |

## Controlled Action Boundary

Allowed after Gate and approval:

- Bind or download NC program.
- Trigger probing macro.
- Trigger tool setting or tool-break check macro.
- Read machine state.
- Write approved measurement macro variables or handshake variables.

Allowed as immediate containment with post-containment review:

- Trigger Feed Hold.
- Raise alarm stop.

Blocked in V1:

- Autonomous CNC cycle start.
- Autonomous NC edit-and-run.
- Feed Override closed loop.
- Writes to safety PLC parameters or CNC safety parameters.

## Freeze Exit

The validation machine is frozen when machine id, capability version, required sensing readiness, edge hardware choice, interface path, and safety boundary are recorded.
