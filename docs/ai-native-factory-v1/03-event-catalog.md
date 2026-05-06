# 03 Event Catalog

## Event Rule

Events are facts that have happened. Commands request action; events record command outcomes and object state changes.

## Envelope Fields

- event_id
- event_type
- source
- subject
- time
- schema_version
- correlation_id
- causation_id
- actor
- payload

## V1 Event Types

The V1 event envelope schema constrains `event_type` to this catalog. New event types must be added to the catalog and schema together.

| Event Type | Source | Subject | Meaning |
|---|---|---|---|
| Order.Received | Object Service | CustomerOrder | A historical or live order entered the system |
| Drawing.Registered | Object Service | Drawing | A drawing revision was registered |
| Quote.Proposed | Intake / DFM / Quote Agent | Quotation | A budget-level quotation was proposed |
| Quote.HumanReviewed | HMI | Quotation | A human reviewed quotation assumptions |
| ProcessPlan.Proposed | Process Agent | ProcessPlan | A process route was proposed |
| ProcessPlan.HumanReviewed | HMI | ProcessPlan | A process engineer reviewed the route |
| OEP.Drafted | Package / Gate Agent | OperationExecutionPackage | An OEP draft was generated |
| OEP.GateChecked | OEP Service | OperationExecutionPackage | One or more gates were evaluated |
| OEP.Approved | HMI | OperationExecutionPackage | A human approved the OEP |
| OEP.Released | OEP Service | OperationExecutionPackage | The OEP entered release state |
| MachineAgent.CommandRequested | Agent Runtime or HMI | Machine Physical Agent | A controlled command was requested |
| MachineAgent.CommandExecuted | Machine Physical Agent | OperationExecutionPackage | A controlled command finished with result |
| MachineAgent.FeedHoldTriggered | Machine Physical Agent | Machine | Feed Hold or protective stop was triggered |
| Inspection.ResultCaptured | Machine Physical Agent or Quality HMI | MeasurementResult | Measurement result was captured |
| Exception.Opened | Any service | Exception | An abnormal condition was opened |
| Exception.Closed | HMI or Agent Runtime | Exception | An abnormal condition was closed |
| Decision.Recorded | Agent Runtime | Decision | A structured agent decision was stored |
| Knowledge.CandidateCreated | Agent Runtime | KnowledgeItem | A reusable rule or template candidate was created |

## Idempotency Rule

The pair `event_id` and `source` is unique. Consumers must ignore repeated delivery of the same event.
