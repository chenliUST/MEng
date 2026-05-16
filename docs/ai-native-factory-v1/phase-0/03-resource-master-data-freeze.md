# 03 Resource Master Data Freeze

## Purpose

Freeze the minimum resource master data needed to create a first-order OEP draft.

This is not a full MES/WMS/QMS master-data program. It is the smallest set that lets Resource Gate, Tool Gate, Fixture Gate, Quality Gate, and command trace work for one validation-machine order.

## Required Resource Records

### Machine

| Field | Example Shape |
|---|---|
| machine_id | MC-VAL-001 |
| machine_capability_version | V1 |
| work_center_id | WC-MILL-001 |
| status | available, staged, executing, maintenance, or down |
| interface_status | offline_ready, connected, verified, blocked |

### Tool Assembly

| Field | Example Shape |
|---|---|
| tool_assembly_id | TASM-D10-001 |
| version | V1 |
| tool_family | end_mill, drill, tap, face_mill, probe, or tool_setter_ref |
| diameter_or_size | Engineering value with unit |
| life_status | available, in_use, worn, blocked |
| preset_evidence | Preset id, measurement record, or manual confirmation |

### Fixture And Pallet

| Field | Example Shape |
|---|---|
| fixture_id | FIX-VAL-001 |
| fixture_version | V1 |
| pallet_id | PAL-VAL-001 |
| pallet_version | V1 |
| clamp_strategy | Vise, modular fixture, zero-point, custom fixture |
| identity_method | Barcode, RFID, HMI confirmation, or controlled manual confirmation |

### Material Lot

| Field | Example Shape |
|---|---|
| material_lot_id | MAT-6061-LOT-001 |
| material_spec | Engineering material specification |
| stock_form | Plate, bar, casting, extrusion, or prepared blank |
| quantity_available | Quantity and unit |
| release_status | received, released, consumed, or blocked |

### Operator

| Field | Example Shape |
|---|---|
| operator_id | OP-VAL-001 |
| skill_tags | validation_machine_setup, probing_macro, first_article_support |
| authority_level | operator, process_owner, machine_owner, quality_owner |
| availability_status | available, assigned, unavailable |

### Inspection Plan

| Field | Example Shape |
|---|---|
| inspection_plan_id | IP-PH0-001 |
| inspection_plan_version | V1 |
| critical_characteristics | Datum, hole pattern, flatness, profile, or other frozen characteristics |
| measurement_method | Probe, CMM, manual gauge, vision, or first-article report |
| quality_owner | Accountable reviewer |

## Freeze Exit

Resource master data is frozen when every required OEP resource field has a record:

- machine_id and machine_capability_version.
- tool_assembly_refs with id and version.
- fixture_id and fixture_version.
- pallet_id and pallet_version.
- material_lot_id.
- operator_id and skill tags.
- inspection_plan_id and inspection_plan_version.

If one required record is missing, the first-order chain may run offline, but Phase 1 release must remain blocked.
