# 04 Agent Contracts

## Runtime Rule

Agents do not become the production fact spine. Agents propose structured decisions. Object Service, OEP Service, Event Bus, and human approval determine production state.

## Required Agent Output

Every decision agent output must include:

- decision_id
- agent_id
- agent_version
- decision_type
- target_refs
- recommendation
- evidence_refs
- assumptions
- risk_level
- required_approval
- affected_objects
- proposed_events
- adoption_status
- reviewer
- review_notes

## DecisionLog Status

| Status | Meaning |
|---|---|
| proposed | Agent made a recommendation |
| accepted | Human or rule accepted it without material change |
| modified | Human changed it before adoption |
| rejected | Human rejected it |
| expired | Recommendation no longer applies |

## Agents

### Intake / DFM / Quote Agent

Responsibilities:

- Parse order, drawing, CAD metadata, and historical records.
- Identify DFM risk, cost assumptions, material assumptions, process complexity, and delivery risk.
- Propose budget-level quote structure.

Output objects:

- Quotation
- Decision
- KnowledgeItem candidate

Human approval:

- Required for committed quote.

### Process Agent

Responsibilities:

- Propose process route from templates and expert rules.
- Propose machine, tool, fixture, setup, and inspection strategy.
- Explain differences from historical cases.

Output objects:

- ProcessPlan
- Operation
- SetupPlan
- Decision

Human approval:

- Required for released process route.

### Package / Gate Agent

Responsibilities:

- Generate OEP draft.
- Check Engineering, Resource, Tool, Fixture, Simulation, Quality, and Authority gates.
- Block release when required evidence is missing.

Output objects:

- OperationExecutionPackage
- Decision
- Event proposals

Human approval:

- Required before OEP Approved and Released.

### Execution / Trace Agent

Responsibilities:

- Monitor OEP execution trace.
- Summarize measurement, exception, command, and machine-state records.
- Suggest knowledge updates after execution.

Output objects:

- ExecutionRecord summary
- Exception summary
- KnowledgeItem candidate
- Decision

Human approval:

- Required for knowledge promotion and quality disposition.

## Tool Permission Levels

| Level | Capability | Human Approval |
|---|---|---|
| Record | Read/write non-release facts | Not required inside assigned workflow |
| Recommend | Create DecisionLog proposals | Not required |
| Gate | Mark gate pass/fail with evidence | Required for waive and release |
| Controlled Execute | Request physical command | Required |
| Block | Trigger Feed Hold or protective alarm | No prior approval when used for containment; post-containment review is required |

Protective containment commands are not release actions. They must still be written to OEP Trace with command id, actor, containment reason, result, exception id when one exists, and post-containment review id after review.

## High-Risk Action Boundary

Agents must not automatically start CNC cycle, change NC program for execution, change Feed Override, commit quotation, release process route, release OEP, substitute material, or grant quality concession.
