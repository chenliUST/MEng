# 09 Phase 0 And Phase 1 Acceptance Checklist

## Phase 0 Exit

| Check | Evidence | Pass Rule |
|---|---|---|
| Historical order selected | Order id and drawing refs | One order is frozen for Demo |
| Part family confirmed | Part-family note | Mainly simple A-type part, selected B-like complexity allowed |
| OEP schema frozen | `01-oep-schema.md` and JSON Schema | Plan/Gate/Trace are complete |
| Object model frozen | `02-object-model-v1.md` | Required V1 objects listed |
| Event envelope frozen | `03-event-catalog.md` and JSON Schema | Event envelope schema parses and sample event instances validate against the V1 catalog |
| Agent contracts frozen | `04-agent-contracts.md` and JSON Schema | Four decision agents defined |
| Machine Physical Agent BOM frozen | `06-validation-machine-bom-and-interfaces.md` | Required and enhanced sensors listed |
| Offline first-order chain runs | Runbook evidence | Quote draft, process draft, and OEP draft produced |

## Phase 1 Product Acceptance

| Metric | Denominator | Target | Evidence Query |
|---|---|---|---|
| Drawing-to-OEP data chain completeness | Released first-order OEPs | 100% | Each OEP has order, part, drawing revision, CAD revision, process version, setup version, and NC version |
| OEP Plan/Gate/Trace completeness | Released first-order OEPs | 100% | Each OEP has non-empty Plan, all release gates evaluated, and Trace initialized |
| High-risk action Gate coverage | High-risk release or controlled-execution actions | 100% | Each action has passed or waived Gate evidence before action, except protective containment commands |
| Human approval coverage for release and controlled execution | OEP release actions and approval-gated machine commands | 100% | Each release/action has approval_id and approver record |
| Physical command traceability | Machine Physical Agent command records | 100% | Each command record has command_id, package_id, command_type, actor, result, and approval_id or post_containment_review_id |
| Agent recommendation adoption status coverage | DecisionLog records created during Demo | 100% | Each DecisionLog has adoption_status, reviewer, and review_notes |
| Measurement and exception write-back | Captured measurement results and opened exceptions | 100% | Each result/exception links to package_id and final review status |
| OEP replayability | First-order Demo | Complete replay from intake to quality disposition | Replay uses object records, event records, OEP Trace, DecisionLog, and quality records |

Example pass/fail rule: if the Demo has 6 machine command records and one lacks approval_id or post_containment_review_id, physical command traceability is 5/6 and fails.

## Phase 1 Intelligence Acceptance

The most important V1 intelligent value is ABC:

- A: DFM and quote recommendation.
- B: Process route recommendation.
- C: Tool, fixture, and machine selection recommendation.

D and E are core future value:

- D: Execution monitoring and adaptive recommendation.
- E: Knowledge learning and continuous improvement.

Phase 1 must record D and E evidence, but acceptance priority is that A, B, and C have visible, reviewable, and adoptable recommendations.

## Safety Acceptance

- No autonomous CNC cycle start.
- No Feed Override closed loop.
- No AI direct edit-and-run of NC programs.
- Feed Hold or alarm stop is allowed only as a recorded protective action.
- Certified safety remains with CNC, PLC, and safety PLC.
