# 07 Quote And Process Knowledge Base

## V1 Knowledge Strategy

V1 uses a hybrid knowledge layer:

- Documents and retrieval for explanation.
- Structured rule tables for constraints.
- Process templates for draft generation.
- Historical orders for calibration.
- DecisionLog for learning from adoption, modification, and rejection.

## Quotation Model

V1 quotation is budget-level by default. Formal commercial commitment requires human review.

Cost structure:

- Material cost
- Machine-hour cost
- Setup labor cost
- CAM/process engineering labor
- Tooling cost
- Fixture cost
- Inspection cost
- Risk buffer
- Delivery assumption

## Quote Rule Table Fields

| Field | Meaning |
|---|---|
| rule_id | Stable rule identity |
| part_family | Plate, bracket, fixture, simple housing, or medium-complexity case |
| material | Material group |
| feature_condition | Feature or tolerance condition |
| cost_driver | Material, machine_time, setup, tooling, fixture, inspection, risk |
| formula | Deterministic calculation or lookup key |
| evidence | Expert, historical order, supplier quote, or measurement |
| owner | Process or quoting owner |
| status | candidate, approved, retired |

## Process Template Fields

| Field | Meaning |
|---|---|
| template_id | Stable template identity |
| part_family | Part family |
| material | Material group |
| stock_form | Plate, bar, casting, extrusion, prepared blank |
| operation_sequence | Ordered operation list |
| setup_strategy | Setup count and datum strategy |
| machine_capability | Required axes, travel, spindle, probe, and accuracy |
| tool_family | Required tool categories |
| fixture_strategy | Fixture or pallet rule |
| inspection_strategy | First article, in-process, final, or sampling |
| risk_notes | Known process risks |
| owner | Process owner |
| status | candidate, approved, retired |

## Learning Rule

After first-order execution, the system must compare Agent recommendation, human modification, actual execution, measurement, exception, and final disposition.

Learning outputs:

- Quote rule candidate
- Process template candidate
- Resource-selection rule candidate
- Gate rule candidate
- Sensor-derived anomaly label

No candidate becomes approved knowledge without owner review.
