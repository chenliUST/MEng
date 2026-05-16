# 01 Operation Execution Package Schema

## Definition

Operation Execution Package is the executable industrial contract for one operation, one setup, and one machine execution context.

OEP is not a file folder. It is a releaseable, executable, auditable, and write-back-capable production fact.

## Package Levels

| Level | Name | Role | Directly Executable |
|---|---|---|---|
| L0 | Order Mission Package | Order or project delivery target | No |
| L1 | Part Lot Package | Manufacturing package for one part lot | No |
| L2 | Operation Execution Package | Operation/setup/machine execution unit | Yes |
| L3 | Auxiliary Execution Package | Tool, fixture, transport, or inspection task | Indirect |

V1 implements L2 as the production-grade unit. L0 and L1 exist as aggregation and trace views.

## Required Sections

### Plan

Plan contains order reference, part reference, operation reference, resources, quality requirements, and linked engineering artifacts.

All references that affect release gates must carry both identity and version or revision. Engineering Gate cannot be checked from bare ids.

### Gate

Gate contains engineering version check, resource kitting, tool life, fixture confirmation, simulation, quality readiness, and authority approval.

Gate status is an evaluated outcome: `pending`, `passed`, `failed`, or `waived`. A required approval is represented as `pending` until evidence exists; `required` is not a gate outcome.

### Trace

Trace contains execution records, measurement results, exceptions, command records, and DecisionLog references.

Command records must link command id, OEP id, command type, approval or post-containment review, actor, request time, result, and exception id when one exists.

## Lifecycle

Draft -> EngineeringReady -> ResourceChecked -> Simulated -> Approved -> Released -> Staged -> Executing -> Paused -> Completed -> Archived

Allowed exception loops:

- Paused -> Executing
- Paused -> ReworkRequired
- ReworkRequired -> Draft
- Released -> Cancelled

## Release Gates

| Gate | Blocks Release When |
|---|---|
| Engineering Gate | Drawing, CAD, process, setup, or NC versions conflict |
| Resource Gate | Machine, tool, fixture, pallet, material lot, operator, or required skill is unavailable |
| Tool Gate | Tool identity, tool life, geometry, or offset is missing |
| Fixture Gate | Fixture, pallet, or clamping confirmation is missing |
| Simulation Gate | Simulation or interference check is missing or failed |
| Quality Gate | Inspection plan or critical characteristics are missing |
| Authority Gate | Approval, authority, or risk record is missing |

## Human Card Rendering

The OEP must render to an operation card with these fields:

- Order and part
- Drawing and CAD version
- Operation and setup
- Machine, NC program, fixture, pallet, tool assemblies, material lot, operator
- Critical characteristics and inspection plan
- Gate status
- Operator checklist
- Execution trace
- Exceptions and final disposition

## Change Rule

Human edits become structured diff records. Agent recommendations become DecisionLog records. Neither may silently overwrite released facts.
