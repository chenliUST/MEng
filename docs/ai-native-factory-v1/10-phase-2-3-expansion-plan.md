# 10 Phase 2 And Phase 3 Expansion Plan

## Expansion Rule

Do not redesign the architecture when scaling. Copy the OEP spine, Agent contract, Machine Physical Agent interface, event envelope, and acceptance gates.

## Phase 2: Three-Machine Cell

Goal:

- Connect three machining devices to the same OEP kernel.
- Use machine capability, tool availability, fixture availability, operator availability, and quality resources in resource selection.
- Introduce local scheduling, resource conflict detection, and exception reassignment.
- Convert the first validation-machine installation into a repeatable Machine Physical Agent deployment template.

Entry criteria:

- Phase 1 first-order Demo passed.
- Validation-machine interface stable for at least one complete order.
- Required sensor and command records are traceable.
- Gate failure and exception handling have been exercised at least once in simulation or controlled test.

Exit evidence:

- Multiple OEPs assigned across three devices.
- Resource conflicts detected and recorded.
- At least one exception reassignment or recovery flow recorded.
- Machine Physical Agent deployment package documented for each device.

## Phase 3: About Twenty Machining Devices

Goal:

- Scale standardized Machine Physical Agent deployment.
- Add Toolroom Agent, Inspection Agent, and Logistics/Robot Agent when the OEP and event contracts can absorb them.
- Strengthen operations governance, monitoring, and maintenance.
- Use execution and quality data to improve quote, process, and resource-selection knowledge.

Entry criteria:

- Three-machine cell produces repeatable OEP traces.
- Machine capability model is stable.
- Tool, fixture, material, quality, and operator objects are usable in scheduling and gates.
- Edge deployment template has documented network, security, sensor, and safety boundaries.

Exit evidence:

- About twenty machining devices have standardized identity, capability, status, and trace records.
- Machine Physical Agent installation status is visible per device.
- OEP-driven execution governance covers released production tasks.
- Operations team can replay order, OEP, machine, quality, exception, and DecisionLog history.

## New Agent Admission Rule

Add Robot/Logistics Agent, Toolroom Agent, or Inspection Agent only when:

- The target work can be represented as OEP, auxiliary package, event, object update, or DecisionLog.
- High-risk actions have Gate and human approval.
- The Agent can be tested against first-order or three-machine evidence.
