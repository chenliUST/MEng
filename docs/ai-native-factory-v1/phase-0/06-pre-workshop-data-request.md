# 06 Pre-Workshop Data Request

## Purpose

This document defines exactly what the team should prepare before the first Phase 0 workshop.

The goal is not to collect every factory document. The goal is to prepare enough evidence to decide whether one historical order, one part, one validation machine, and one operation/setup can become the first offline OEP chain.

## Preparation Rules

| Rule | Meaning |
|---|---|
| Bring evidence, not memory | Prefer files, records, screenshots, exports, reports, or photos over verbal descriptions |
| Every item has an owner | Each file or record must name the person who can explain and approve it |
| Every version matters | Drawing, CAD, process, CAM, NC, fixture, tool, and inspection records need version or revision |
| Missing data is allowed in Phase 0 | Missing data becomes a named gate gap with owner and due date |
| Missing required sensing is not allowed in Phase 1 execution | Phase 0 may record an installation plan, but controlled physical execution remains blocked |

## Minimum Packet For The First Workshop

The workshop can proceed when these items are available:

1. One candidate historical order record.
2. One drawing revision and one CAD revision for the candidate part.
3. One candidate validation-machine record.
4. One rough process route or historical routing record.
5. One CAM/NC reference or a named CAM owner who can generate it.
6. One list of required tools, fixture/workholding, material, and inspection characteristics.
7. Named owners for quote, process, CAM, machine, edge/controls, quality, and system records.

If any of the seven items is missing, the team should still record the candidate, but the workshop should not declare the sample frozen.

## 1. Candidate Historical Order

### Required

| Item | What To Bring | Owner | Used For |
|---|---|---|---|
| Order identity | Sales order, work order, project id, or internal job id | Program or quote owner | CustomerOrder id/version |
| Order source | Customer, internal owner, or historical production source | Program or quote owner | Scope and accountability |
| Part and quantity | Part number/name, quantity, batch information | Program or process owner | PartLot and quote assumptions |
| Material requirement | Material grade/spec, stock form if known | Process or material owner | Quote, Resource Gate, MaterialLot |
| Delivery assumption | Requested due date, actual due date, or historical lead time | Quote owner | Budget quote assumption |
| Commercial baseline | Historical quote, actual price, cost estimate, or no-price statement | Quote owner | Quote calibration |
| Historical outcome | Completed, reworked, scrapped, delayed, or unknown | Program owner | Risk and learning context |

### Recommended

| Item | What To Bring | Why It Helps |
|---|---|---|
| Historical setup time | Actual or estimated setup hours | Quote and process calibration |
| Historical cycle time | Actual machine time, CAM estimate, or operator estimate | Quote and OEP planning |
| Historical supplier or outsourcing info | If any operation was outsourced | Scope boundary |
| Customer quality notes | Special requirements, concessions, complaints | DFM and Quality Gate |
| Emails or change notes | Engineering/commercial changes during the order | Version and assumption tracking |

### Workshop Decisions

- Is this order simple enough for the first OEP?
- Does the first Demo use the full order quantity or a reduced validation quantity?
- Is the quote module allowed to compare against real historical cost/price?
- Which data is confidential and should be masked in examples?

## 2. Drawing And CAD Version

### Required Drawing Data

| Item | What To Bring | Owner | Used For |
|---|---|---|---|
| Drawing file | PDF is enough for workshop; native drawing file if available | Process owner | Drawing object |
| drawing_id | Drawing number or controlled file id | Process owner | OEP part_ref |
| drawing_revision | Revision shown in title block or document control | Process owner | Engineering Gate |
| Units | mm or inch | Process owner | Process and inspection assumptions |
| Material note | Material specification on drawing | Process owner | Quote and MaterialLot |
| Key tolerances | Tight dimensions, GD&T, surface finish, heat treatment, coating | Process and quality owners | DFM and Quality Gate |
| Critical characteristics | Features that must be inspected in Demo | Quality owner | InspectionPlan |

### Required CAD Data

| Item | What To Bring | Owner | Used For |
|---|---|---|---|
| CAD file | STEP, Parasolid, native CAD, or CAM-readable export | Process or CAM owner | CADModel object |
| cad_model_id | Controlled CAD id or file id | Process or CAM owner | OEP part_ref |
| cad_model_revision | Revision/configuration matching drawing | Process or CAM owner | Engineering Gate |
| Coordinate orientation | Datum, setup orientation, or CAM coordinate note | CAM owner | SetupPlan |
| Model completeness | Solid body, surfaces, assembly refs, missing features | CAM owner | CAM feasibility |

### Recommended

| Item | What To Bring | Why It Helps |
|---|---|---|
| Revision history | What changed between revisions | DFM risk and version consistency |
| Drawing-CAD comparison note | Known mismatch or confirmation of match | Engineering Gate |
| Feature list | Holes, pockets, faces, threads, datum features | Process Agent seed |
| Screenshots | Annotated view of critical features | Faster workshop alignment |

### Workshop Decisions

- Are drawing and CAD revisions consistent?
- Which revision is frozen for Phase 0?
- Which characteristics enter the first OEP quality plan?
- Are any drawing notes impossible to verify on the validation machine?

## 3. Candidate Validation Machine

### Required Machine Data

| Item | What To Bring | Owner | Used For |
|---|---|---|---|
| machine_id | Internal machine id or proposed id | Machine owner | OEP resources |
| Machine make/model | Vendor, model, year if known | Machine owner | Capability record |
| CNC control | Vendor, model, software version if known | Machine and edge/controls owners | Interface feasibility |
| PLC/safety PLC | Vendor/model or access boundary | Edge/controls owner | Safety boundary |
| Axis configuration | 3-axis, 4-axis, 5-axis, turning, mill-turn | Machine owner | Process feasibility |
| Work envelope | Travel, table size, fixture limits | Machine owner | Part feasibility |
| Spindle capability | Speed, power, torque range if available | Machine owner | Process feasibility |
| Tool changer | Capacity, taper/interface, tool length/diameter limits | Machine owner | Tool Gate |
| Probe status | Workpiece probe installed or not; macro availability | Machine owner | Required sensing |
| Tool setter status | Laser/contact tool setter or break detection | Machine owner | Required sensing |
| Network path | How edge IPC can connect to CNC/PLC/HMI network | Edge/controls owner | Machine Physical Agent |
| Safety boundary | What AI/edge can read, request, write, or never touch | Edge/controls owner | Controlled action boundary |

### Required Interface Notes

| Item | What To Bring | Owner | Used For |
|---|---|---|---|
| Available protocol | Vendor API, OPC UA, MTConnect, FOCAS, Siemens interface, file share, HMI export, or manual export | Edge/controls owner | Nervous system |
| Readable data | Status, current program, alarms, spindle load, macro variables, tool data | Edge/controls owner | Trace and Gate |
| Writable data | NC binding/download, macro trigger, measurement variables, handshake variables | Edge/controls owner | Command boundary |
| Blocked writes | Safety PLC parameters, CNC safety parameters, Feed Override, cycle start | Edge/controls owner | Safety |
| Existing edge device | IPC, gateway, scanner, HMI, camera PC, or none | Edge/controls owner | Edge Brain |

### Required Sensor Readiness

| Sensor | Bring Current Status | Phase 1 Rule |
|---|---|---|
| CNC/PLC data interface | Installed, available, planned, blocked | Must be verified before controlled execution |
| Workpiece probe | Installed, available, planned, blocked | Must be verified before controlled execution |
| Laser tool setter / break detection | Installed, available, planned, blocked | Must be verified before controlled execution |
| Tool identity confirmation | Barcode, RFID, preset system, manual confirmation, or none | Must have controlled method |
| Fixture identity confirmation | Barcode, RFID, HMI/manual confirmation, or none | Must have controlled method |
| Pallet identity confirmation | Barcode, RFID, HMI/manual confirmation, or none | Must have controlled method |
| Edge HMI / scanner | Installed, available, planned, blocked | Must be available for operator confirmation |

### Enhanced Sensor Status

| Sensor | Bring Current Status | Phase 0 Decision |
|---|---|---|
| Vibration | Installed, selected, not selected | Install now or defer with reason |
| Industrial camera or line laser | Installed, selected, not selected | Evidence and visual trace plan |
| Spindle power/current acquisition | Available from CNC, external sensor, not available | Quote/process calibration plan |
| Temperature | Installed, selected, not selected | Context data plan |
| Coolant | Installed, selected, not selected | Process condition trace plan |
| Air pressure | Installed, selected, not selected | Fixture/auxiliary trace plan |

### Workshop Decisions

- Is this machine feasible for the selected part and operation?
- Can the required sensing organs be verified before Phase 1?
- Which commands are approval-gated?
- Which commands are protective containment only?
- What cannot be touched by the edge/AI layer?

## 4. Process, CAM, And NC Records

### Required

| Item | What To Bring | Owner | Used For |
|---|---|---|---|
| Historical routing | Operation sequence, work center, setup count | Process owner | ProcessPlan seed |
| Selected operation | Candidate first-OEP operation/setup | Process owner | OEP operation_ref |
| Setup sheet | Workholding, datums, WCS, orientation, photos if available | Process and CAM owners | SetupPlan |
| Tool list | Tool numbers, tool types, holders, diameters, stickout if known | CAM owner | Tool Gate |
| CAM project or export | CAM file, toolpath export, setup sheet, or screenshot | CAM owner | Toolpath and NCProgram |
| NC program | NC file, program number, revision, postprocessor note | CAM owner | NCProgram |
| Simulation evidence | CAM verify, machine simulation, collision check, or explicit gap | CAM owner | Simulation Gate |

### Recommended

| Item | Why It Helps |
|---|---|
| Feeds and speeds | Quote/process calibration |
| Actual cycle time | Quote calibration and OEP estimate |
| Actual setup time | Quote calibration |
| Operator notes | Practical HMI and setup design |
| Photos or video of setup | Fixture and operator workflow understanding |
| Prior NC revisions | Version control and change tracking |

### Workshop Decisions

- Which operation becomes the first L2 OEP?
- Can CAM/NC be reused, regenerated, or imported?
- What simulation evidence is accepted for Phase 0 offline chain?
- What evidence blocks Phase 1 release?

## 5. Tool, Fixture, Pallet, And Material Records

### Tool Assembly

| Item | Required Detail |
|---|---|
| tool_assembly_id | Stable id for each tool assembly |
| version | Increment when cutter, holder, gauge length, or offset basis changes |
| tool type | End mill, drill, tap, face mill, probe, etc. |
| geometry | Diameter, corner radius, length, flute count if known |
| holder | Holder type, taper/interface |
| preset evidence | Preset sheet, tool measurement, or controlled manual confirmation |
| life status | Available, in use, worn, blocked, unknown |
| substitution rule | Allowed replacement or must ask process owner |

### Fixture And Pallet

| Item | Required Detail |
|---|---|
| fixture_id | Stable fixture id |
| fixture_version | Increment when clamp, locator, base, or datum changes |
| pallet_id | Stable pallet id if palletized |
| pallet_version | Increment when pallet setup changes |
| clamping method | Vise, zero-point, modular, soft jaws, custom fixture |
| datum strategy | Which surfaces/features define setup |
| identity method | Barcode, RFID, HMI confirmation, manual confirmation |
| interference risk | Known risk with tool, spindle, probe, or machine travel |

### Material Lot

| Item | Required Detail |
|---|---|
| material_lot_id | Stable lot id or proposed id |
| material spec | Grade, standard, temper, heat treatment if applicable |
| stock form | Plate, bar, casting, extrusion, prepared blank |
| stock size | Dimensions and units |
| quantity available | Count or stock length/area |
| certificate | Mill cert, supplier cert, internal release, or missing |
| release status | Received, released, consumed, blocked |

### Workshop Decisions

- Are all resources representable in the OEP schema?
- Which missing resource data blocks Resource Gate?
- Which tool or fixture substitutions require human approval?

## 6. Inspection And Quality Records

### Required

| Item | What To Bring | Owner | Used For |
|---|---|---|---|
| inspection_plan_id | Existing id or proposed id | Quality owner | OEP quality |
| inspection_plan_version | Version or draft version | Quality owner | Quality Gate |
| Critical characteristics | Dimensions/features for the first OEP | Quality owner | MeasurementResult |
| Measurement method | Probe, CMM, manual gauge, vision, line laser, or report | Quality owner | Quality Gate |
| Acceptance criteria | Tolerance, pass/fail rule, review owner | Quality owner | Final disposition |
| Historical inspection report | First article, final report, CMM report, or manual record | Quality owner | Calibration and risk |

### Recommended

| Item | Why It Helps |
|---|---|
| Nonconformance records | Exception patterns and risk |
| Rework records | Learning candidates |
| Gauge list | Resource planning |
| Measurement program | Probe/CMM integration path |
| Customer quality requirements | Authority and quality boundary |

### Workshop Decisions

- Which characteristics must be measured in Phase 1?
- Which measurement can be done on-machine and which must be off-machine?
- Who can approve final disposition?
- What quality evidence blocks OEP release?

## 7. Historical Execution And Exception Evidence

### Recommended

| Item | What To Bring | Why It Helps |
|---|---|---|
| Actual machine time | Machine log, operator note, ERP/MES record | Quote calibration |
| Actual setup time | Operator note or work order record | Quote calibration |
| Alarm history | CNC alarm, downtime, maintenance notes | Machine risk |
| Tool break or tool wear notes | Tooling records, operator notes | Tool Gate and sensors |
| Scrap or rework notes | NCR, quality notes, operator notes | Exception and learning |
| Photos/videos | Setup, fixture, measurement, defects | Agent explanation and HMI design |

## 8. Owner And Authority Records

### Required

| Role | Required Person |
|---|---|
| Program owner | Confirms first-order Demo scope |
| System owner | Owns OEP, event, schema, and data contract |
| Quote owner | Owns quote assumptions and commercial boundary |
| Process owner | Owns DFM, route, setup, tool/fixture recommendation |
| CAM owner | Owns CAM, NC, simulation evidence |
| Machine owner | Owns validation-machine readiness and safe operation |
| Edge/controls owner | Owns CNC/PLC interface and edge boundary |
| Quality owner | Owns inspection plan and final disposition |
| Operator representative | Confirms machine-side practicality |

## Candidate Scoring

Score each candidate order from 0 to 2.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Data completeness | Key files missing | Some gaps with owners | Core evidence available |
| Part suitability | Too complex or unclear | Medium complexity but bounded | Simple A-type or controlled B-like |
| Machine feasibility | No clear machine path | Machine path likely | Validation machine can run selected operation |
| Quality feasibility | Critical checks unclear | Checks possible with gaps | Characteristics and method clear |
| Safety fit | Requires blocked action | Requires careful boundary | Fits V1 controlled-action boundary |
| Learning value | Little value | Some process/quote value | Strong DFM/process/resource learning value |

Use a candidate when total score is 9 or higher and no criterion is 0 for safety fit, drawing/CAD version, or quality feasibility.

## Folder Structure For The Evidence Pack

Use this structure for the first shared evidence folder:

```text
phase-0-evidence/
  01-order/
  02-drawing-cad/
  03-process-cam-nc/
  04-machine-edge-controls/
  05-tools-fixtures-material/
  06-inspection-quality/
  07-history-exceptions/
  08-owners-approvals/
```

Each file name should start with the evidence category and owner initials:

```text
02-drawing-cad_PROCESSOWNER_DWG-BRACKET-001_REV-A.pdf
03-process-cam-nc_CAMOWNER_NC-OP20-BRACKET-001_REV-V1.nc
04-machine-edge-controls_EDGEOWNER_MC-VAL-001_INTERFACE-NOTES.md
```

## What The Team Should Send Before The Workshop

At least 24 hours before the workshop, send:

- The filled inventory template.
- The evidence folder or links.
- A short note naming the preferred candidate order and backup candidate.
- A list of missing evidence with owners.
- Any safety or confidentiality restrictions.
