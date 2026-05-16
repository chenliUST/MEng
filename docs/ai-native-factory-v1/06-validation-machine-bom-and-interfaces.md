# 06 Validation Machine BOM And Interfaces

## Target

The first validation machine is the physical proof point for Phase 1. It must support L2 controlled execution and install the enhanced sensing hardware needed for L3 data learning.

## Required Sensing Organs

| Item | Purpose | OEP Use |
|---|---|---|
| CNC/PLC data interface | Status, alarms, program, load, macro variables | Gate, Trace, exception |
| Workpiece probe | Setup confirmation and in-process measurement | Gate, quality, Trace |
| Laser tool setter / break detection | Tool geometry and break check | Tool Gate, Trace |
| Tool identity confirmation | Tool assembly match | Resource Gate, Tool Gate |
| Fixture identity confirmation | Fixture match | Fixture Gate |
| Pallet identity confirmation | Pallet match | Fixture Gate |
| Edge HMI / scanner | Human confirmation and barcode binding | Approval, Trace |

## Enhanced Sensing Organs

| Item | Phase 1 Use |
|---|---|
| Vibration sensor | Evidence capture, anomaly label, offline analysis |
| Industrial camera or line laser | Setup evidence, visual trace, future feature verification |
| High-resolution spindle power/current acquisition | Cutting-state evidence and quote/process calibration |
| Temperature sensor | Machine and environment context |
| Coolant sensor | Process condition trace |
| Air pressure sensor | Fixture and auxiliary condition trace |

## Edge Hardware

- Industrial PC or edge AI box.
- Isolated industrial network interface.
- Time synchronization source.
- Local buffer for disconnected operation.
- HMI or scanner input.
- Secure connection to OEP Service and Event Bus.

## Interface Requirements

| Interface | Direction | Minimum Data |
|---|---|---|
| OEP download | Cloud/service to edge | package_id, status, plan, gate |
| Gate query | edge to service | package_id, gate status, evidence refs |
| Command request | service or HMI to edge | command_id, package_id, command_type, safety_class, approval_id or containment_reason |
| Command result | edge to service | command_id, result, time, machine_state, exception_id, post_containment_review_required |
| Sensor stream | edge to event storage | sensor_id, timestamp, value, quality |
| Trace write-back | edge to OEP Service | execution_records, measurement_results, exceptions, command_records |

## Procurement Decision Boundary

Select devices that can be supported by the validation-machine CNC/PLC vendor interface and by the plant network plan. Prefer industrial supportability over experimental sensor novelty.
