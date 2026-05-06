# 01 First-Order Sample Freeze

## Purpose

Select one real historical order and freeze it as the first-order Demo sample.

The sample is not chosen because it is easy to showcase. It is chosen because it can expose whether OEP, Agent workflow, and Machine Physical Agent can govern a real machining order without expanding scope beyond Phase 1.

## Selection Rules

| Rule | Pass Condition |
|---|---|
| Real order | The order came from a real customer, internal job, or historical production case |
| Part type | Plate, bracket, fixture, simple housing, or controlled medium-complexity part |
| Data availability | Drawing, CAD, material, quantity, and historical process evidence are available |
| Process boundedness | The first OEP can be one operation/setup on the validation machine |
| Quality boundedness | Critical characteristics can be listed and measured in Phase 1 |
| Safety boundedness | No autonomous CNC cycle start or Feed Override is required |

## Required Order Record

| Field | Freeze Rule |
|---|---|
| customer_order_id | Stable id used across quote, process, OEP, and events |
| customer_order_version | Increment when commercial or engineering assumptions change |
| customer_name_or_internal_owner | Named owner for review |
| quantity | Frozen first-order Demo quantity |
| delivery_assumption | Recorded as quote/process assumption, not a binding promise |
| material_spec | Must match material lot selection before Phase 1 |
| source_files | Drawing, CAD, historical routing, NC, inspection, quote, and exception records |

## Required Part Record

| Field | Freeze Rule |
|---|---|
| part_id | Stable part id |
| part_version | Increment when manufacturing definition changes |
| drawing_id | Stable drawing id |
| drawing_revision | Must match OEP Engineering Gate |
| cad_model_id | Stable CAD model id |
| cad_model_revision | Must match OEP Engineering Gate |
| part_family | Plate, bracket, fixture, simple housing, or selected medium-complexity case |
| critical_characteristics | Minimum list for the first OEP quality plan |

## Sample Acceptance

The order is frozen when these records exist:

- CustomerOrder with id and version.
- Part with id and version.
- Drawing with id and revision.
- CADModel with id and revision.
- Initial quote assumptions.
- Initial process assumptions.
- Quality characteristics list.
- Explicit owner for missing data resolution.

## Rejection Conditions

Do not use a candidate as the first-order Demo if:

- Drawing or CAD revision cannot be established.
- The first operation cannot be bounded to one validation-machine OEP.
- Required quality evidence cannot be captured.
- The job requires autonomous CNC start, Feed Override, or unapproved NC modification.
- The team cannot assign process, CAM, machine, quality, and system owners.
