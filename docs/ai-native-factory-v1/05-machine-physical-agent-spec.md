# 05 Machine Physical Agent Specification

## Definition

Machine Physical Agent is a cyber-physical agent installed around a machining device. It combines the machine body, sensing organs, nervous system, edge brain, reflex loop, and OEP interface.

## Components

| Component | V1 Meaning |
|---|---|
| Body | Machine tool, CNC, PLC, spindle, magazine, table, fixture, probe, laser tool setter |
| Sensors | CNC/PLC data, probe, laser tool setting, tool identity, fixture identity, pallet identity, spindle load, current, vibration, vision, line laser, coolant, air pressure, temperature |
| Nervous System | OPC UA, MTConnect, vendor API, IO-Link, DAQ, industrial Ethernet, camera trigger, time sync |
| Edge Brain | Edge IPC or edge AI box for state fusion, gate judgment, command orchestration, explanation, trace write-back |
| Reflex Loop | Emergency stop, door interlock, safety PLC, CNC alarm, Feed Hold, tool-life block, fixture confirmation block |
| OEP Interface | Receive OEP, check gates, request approved actions, write Trace |

## Capability Levels

| Level | Name | Goal | Action Boundary |
|---|---|---|---|
| L1 | MVP Sensing | Machine can be observed and explained | No autonomous physical action |
| L2 | Controlled Execution | Machine can act after approval | Human-approved commands, no autonomous spindle start, no Feed Override |
| L3 | Adaptive Enhancement | Machine can suggest local adaptation | Suggestion and offline analysis in V1 |

The first validation machine target is L2 controlled execution with L3 sensing hardware installed.

## Allowed V1 Actions

- Bind or download NC program while CNC cycle start remains human-operated.
- Trigger probing, tool setting, and tool-break macros after approval.
- Read CNC execution state, alarms, spindle load, and approved macro variables.
- Write only approved measurement macro variables or documented handshake variables; do not write safety PLC parameters or CNC safety parameters.
- Trigger Feed Hold or alarm stop for protection as immediate containment with post-containment review.
- Record all command outcomes into OEP Trace.

## Blocked V1 Actions

- Autonomous CNC cycle start.
- Autonomous NC program edit and run.
- Feed Override closed loop.
- Material substitution without engineering and quality approval.
- Quality concession without quality-owner approval.

## Safety Rule

Real-time safety belongs to CNC, PLC, and safety PLC. Edge AI may understand state, explain risk, request controlled actions, and trigger allowed protective actions, but it must not replace certified safety control.
