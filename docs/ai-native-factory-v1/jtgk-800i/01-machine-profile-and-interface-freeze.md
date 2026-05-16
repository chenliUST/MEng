# 01 Machine Profile And Interface Freeze

## Purpose

Freeze the JTGK-800i machine identity, known capability, interface assumptions, fallback paths, and safety boundary before building the execution-spine pilot.

## Machine Identity

| Field | Value |
|---|---|
| machine_id | `MC-JTGK-800I-001` |
| machine_agent_id | `MPA-JTGK-800I-001` |
| machine_make_model | JTGK-800i CNC engraving and milling center |
| cnc_control | JT810 |
| machine_capability_version | `JTGK800I-CAP-V1` |
| primary_mission | Execution-spine traceability |
| pilot_mode | Concentrated A/B/C sprint |

## Machine Capability

| Capability | Value |
|---|---|
| X/Y/Z travel | 700 / 800 / 350 mm |
| work envelope note | 810 x 800 x 410 mm listed in supplied specification |
| table size | 750 x 800 mm |
| table load | 800 kg |
| spindle | 15 kW S6, 24000 rpm |
| spindle taper | BBT30 |
| tool magazine | 24 tools |
| rapid traverse | X/Y/Z 20 / 20 / 20 m/min |
| total installed power | about 20 kW |
| power supply | 380 V +/- 5%, 50 Hz |
| compressed air | 0.6 MPa, 210 L/min |

## Interface Freeze Matrix

| Interface | Target For Pilot | First Verification Method | Fallback If Direct Access Is Limited |
|---|---|---|---|
| CNC state read | mode, active program, alarm, cycle state | read test from JT810 or vendor interface | operator HMI confirmation plus photo evidence |
| PLC/safety state read | door, emergency stop, machine ready where available | PLC/safety status read test | operator checklist confirmation |
| NC program binding | bind OEP to NC program id/version | file path, control program id, or CNC screen confirmation | scanner/HMI entry of NC id/version |
| macro variable read | approved probing/tool/measurement variables | vendor-supported macro variable read | HMI entry from CNC screen |
| macro variable write | approved measurement or handshake variables only | write to documented non-safety variable in dry test | no-write mode with manual measurement write-back |
| command request capture | command id, approval id, actor, result | edge command log | HMI-only command record |
| quality evidence capture | probe, tool setting, inspection result, setup photo | available probe/tool-setter/HMI/camera path | manual inspection record with evidence attachment |
| health evidence capture | spindle load/current, vibration, air, coolant, temperature | DAQ or sensor read test | machine-state and operator note only for Slice A |

## Safety Boundary

Allowed after OEP gate and human approval:

- Bind or download NC program.
- Read machine state.
- Trigger approved probing macro.
- Trigger approved tool-setting macro.
- Trigger approved tool-break check macro.
- Write approved measurement macro variables or documented handshake variables.

Allowed as protective containment:

- Trigger feed hold.
- Raise alarm stop.

Blocked in V1:

- Autonomous CNC cycle start.
- Autonomous NC edit-and-run.
- Closed-loop feed override.
- Writes to safety PLC parameters.
- Writes to CNC safety parameters.
- Quality concession without quality-owner approval.

## Freeze Exit

The machine profile is frozen when every row in the Interface Freeze Matrix has one of these statuses recorded in the implementation tracker:

- `verified_direct`
- `verified_fallback`
- `blocked_with_owner`

The first pilot may run Slice A with fallback confirmations. Slice B and Slice C require direct or controlled fallback evidence for quality and health records.
