# 02 Object Model V1

## Rule

Objects are versioned production facts. Agents, OEP, events, HMI, and Machine Physical Agent must reference objects by id and version.

## Business Objects

| Object | Required Identity | Required State |
|---|---|---|
| CustomerOrder | customer_order_id | received, quoted, accepted, closed |
| Quotation | quotation_id, version | draft, human_reviewed, committed |

## Engineering Objects

| Object | Required Identity | Required State |
|---|---|---|
| Part | part_id, version | active, superseded |
| Drawing | drawing_id, revision | received, checked, released |
| CADModel | cad_model_id, revision | received, checked, released |
| ManufacturingFeature | feature_id | detected, confirmed, rejected |

## Process Objects

| Object | Required Identity | Required State |
|---|---|---|
| ProcessPlan | process_plan_id, version | draft, reviewed, released |
| Operation | operation_id, version | draft, reviewed, released |
| SetupPlan | setup_plan_id, version | draft, reviewed, released |
| Toolpath | toolpath_id, version | generated, simulated, approved |
| NCProgram | nc_program_id, version | generated, simulated, approved, bound |

## Execution Objects

| Object | Required Identity | Required State |
|---|---|---|
| OperationExecutionPackage | package_id | OEP lifecycle states |
| ExecutionRecord | execution_record_id | started, paused, completed, aborted |
| Event | event_id | recorded |
| Exception | exception_id | open, contained, closed |

## Resource Objects

| Object | Required Identity | Required State |
|---|---|---|
| Machine | machine_id | available, staged, executing, maintenance, down |
| WorkCenter | work_center_id | active, inactive |
| Operator | operator_id | available, assigned, unavailable |

## Tooling And Material Objects

| Object | Required Identity | Required State |
|---|---|---|
| ToolAssembly | tool_assembly_id | available, in_use, worn, blocked |
| Fixture | fixture_id | available, staged, in_use, blocked |
| Pallet | pallet_id | available, staged, in_use |
| MaterialLot | material_lot_id | received, released, consumed, blocked |
| Inventory | inventory_id | available, reserved, consumed |
| StorageLocation | storage_location_id | active, blocked |

## Quality Objects

| Object | Required Identity | Required State |
|---|---|---|
| InspectionPlan | inspection_plan_id, version | draft, released |
| MeasurementResult | measurement_result_id | captured, reviewed, accepted, rejected |
| QualityEvent | quality_event_id | open, dispositioned, closed |

## Intelligence Objects

| Object | Required Identity | Required State |
|---|---|---|
| Agent | agent_id, version | active, retired |
| Decision | decision_id | proposed, accepted, modified, rejected |
| KnowledgeItem | knowledge_item_id, version | candidate, approved, retired |
| Model | model_id, version | active, retired |

## Required Relationships

- CustomerOrder has many Part.
- Part has many Drawing, CADModel, ProcessPlan, and OperationExecutionPackage.
- OperationExecutionPackage references exactly one Operation, one SetupPlan, one Machine, one NCProgram, one Fixture, and one Pallet.
- OperationExecutionPackage references one or more ToolAssembly.
- ExecutionRecord belongs to one OperationExecutionPackage.
- MeasurementResult belongs to one InspectionPlan and one OperationExecutionPackage.
- Decision belongs to one Agent and may affect objects, OEP, events, or knowledge items.
