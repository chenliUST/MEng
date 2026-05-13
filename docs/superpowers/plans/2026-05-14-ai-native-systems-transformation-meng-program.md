# AI-Native Systems Transformation MEng Program Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete first-version proposal and operating artifact package for the Studio-Centered MEng in AI-Native Systems Transformation.

**Architecture:** The approved design spec remains the source of truth. Implementation produces a coherent document suite under `docs/ai-native-systems-transformation-meng/`: proposal narrative, competency rubric, personas, curriculum map, course and studio designs, AI operating discipline, industry/co-op model, assessment handbook, and launch roadmap. Each artifact is independently reviewable but linked through the same program spine: domain-open AI-native systems transformation, continuous PBL, continuous industry immersion, and evidence-based graduation.

**Tech Stack:** Markdown program artifacts, PowerShell verification commands, `rg` search checks, Git. No software runtime is required for this implementation phase.

---

## Scope

This plan turns the approved design spec into a usable institutional proposal package and operating blueprint. It does not launch the program, recruit partners, approve courses, or build marketing materials. It creates the documents needed for faculty review, leadership discussion, partner conversations, and the next proposal-drafting cycle.

Source of truth:

- `docs/superpowers/specs/2026-05-13-ai-native-systems-transformation-meng-design.md`

## Execution Status

This plan was executed on 2026-05-14 via grouped subagent-driven execution, with artifacts reviewed by spec and quality reviewers. Individual task commit steps were consolidated into a final package commit, so per-task commit checkboxes remain as implementation instructions rather than a literal execution log.

## File Structure

Create this artifact set:

- `docs/ai-native-systems-transformation-meng/README.md`: reading order and artifact map.
- `docs/ai-native-systems-transformation-meng/00-proposal-narrative.md`: executive proposal narrative for leadership and program approval.
- `docs/ai-native-systems-transformation-meng/01-competency-model-and-rubric.md`: layered competencies, graduate promises, evidence rubric.
- `docs/ai-native-systems-transformation-meng/02-student-personas-and-bridging.md`: canonical personas, admissions baseline, diagnostics, bridging.
- `docs/ai-native-systems-transformation-meng/03-curriculum-map.md`: two-year structure, semester rhythm, core blocks, electives.
- `docs/ai-native-systems-transformation-meng/04-course-and-workshop-designs.md`: course outlines and workshop series.
- `docs/ai-native-systems-transformation-meng/05-pbl-studio-and-gate-system.md`: studio sequence, Semester 1 gate package, review gates.
- `docs/ai-native-systems-transformation-meng/06-ai-operating-discipline.md`: AI work log, evaluation harness, responsibility memo.
- `docs/ai-native-systems-transformation-meng/07-industry-partnership-and-coop-model.md`: partner tiers, co-op/residency model, partner requirements.
- `docs/ai-native-systems-transformation-meng/08-assessment-portfolio-and-defense.md`: portfolio architecture, sponsor evidence, final defense.
- `docs/ai-native-systems-transformation-meng/09-launch-roadmap-and-governance.md`: first-three-year rollout, governance, risks, decisions.

## Task 1: Scaffold The Program Artifact Set

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/README.md`
- Create directory: `docs/ai-native-systems-transformation-meng`

- [ ] **Step 1: Create the artifact directory**

Run:

```powershell
New-Item -ItemType Directory -Force -Path 'docs/ai-native-systems-transformation-meng'
```

Expected: PowerShell returns a directory entry for `docs/ai-native-systems-transformation-meng` or returns without error.

- [ ] **Step 2: Create the README**

Create `docs/ai-native-systems-transformation-meng/README.md` with this content:

```markdown
# AI-Native Systems Transformation MEng Program Package

This folder contains the first-version proposal and operating blueprint for the Studio-Centered Master of Engineering in AI-Native Systems Transformation.

Read in this order:

1. `00-proposal-narrative.md`
2. `01-competency-model-and-rubric.md`
3. `02-student-personas-and-bridging.md`
4. `03-curriculum-map.md`
5. `04-course-and-workshop-designs.md`
6. `05-pbl-studio-and-gate-system.md`
7. `06-ai-operating-discipline.md`
8. `07-industry-partnership-and-coop-model.md`
9. `08-assessment-portfolio-and-defense.md`
10. `09-launch-roadmap-and-governance.md`

Source design:

- `../superpowers/specs/2026-05-13-ai-native-systems-transformation-meng-design.md`

Program spine:

- Public umbrella: AI-Native Systems Transformation.
- Graduate identity: Hybrid Transformation Engineer.
- Learning model: Studio-centered, project-based, industry-immersed.
- Evidence model: portfolio, deep challenge, AI operating evidence, prototype validation, sponsor evidence, and final competency defense.
```

- [ ] **Step 3: Verify scaffold**

Run:

```powershell
Test-Path 'docs/ai-native-systems-transformation-meng/README.md'
rg -n "AI-Native Systems Transformation|Hybrid Transformation Engineer|Studio-centered|final competency defense" docs/ai-native-systems-transformation-meng/README.md
```

Expected: `Test-Path` prints `True`; `rg` returns matches for all listed phrases.

- [ ] **Step 4: Commit scaffold**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/README.md
git commit -m "docs: scaffold AI-native systems transformation MEng package"
```

Expected: Git creates one commit containing the README.

## Task 2: Write The Proposal Narrative

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/00-proposal-narrative.md`

- [ ] **Step 1: Write the proposal narrative**

Create `docs/ai-native-systems-transformation-meng/00-proposal-narrative.md` with this content:

```markdown
# 00 Proposal Narrative

## Program Title

Master of Engineering in AI-Native Systems Transformation

## One-Sentence Definition

The program prepares STEM-plus graduates to diagnose complex systems, integrate AI responsibly, learn continuously, prototype practical interventions, and drive evidence-based transformation across domains.

## Rationale

AI technologies are changing how engineering, service, technology, industrial, and organizational work is performed. Graduates who only know how to use AI tools will not be distinctive. Graduates who only know traditional disciplinary methods may struggle to diagnose and implement transformation across data, workflows, people, organizations, and external partners.

The program responds to five capability gaps:

1. Systems-level diagnosis.
2. Trusted data collaboration.
3. Implementation and prototyping.
4. AI-guided professional judgment.
5. Authentic project execution and work readiness.

## Public Umbrella

AI-Native Systems Transformation is the public umbrella. It is intentionally domain-open. Manufacturing, logistics, healthcare operations, technology services, finance operations, public-service systems, and other complex settings can all provide project contexts.

## Graduate Identity

Graduates are Hybrid Transformation Engineers. They are not defined merely as AI users, model builders, traditional engineering specialists, or general managers. They are professionals who can connect systems diagnosis, AI integration, data collaboration, implementation, human workflows, and professional responsibility.

## Internal Pillars

### Engineering Judgment in the AI Era

Students learn to guide, verify, challenge, and take responsibility for AI-enabled work.

### Problem-Based Transformation Practice

Students learn through sustained real problems, not only case studies or classroom exercises.

### Human-AI-Organization Integration

Students learn that transformation involves people, AI agents, workflows, data, incentives, routines, governance, and adoption.

## Program Model

The program is a Studio-Centered MEng. Courses remain visible and academically credible, but the real spine is a sequence of supervised PBL studios connected to industry problems.

Students begin industry immersion in Semester 1. They commit to a deep challenge by the end of Semester 1 and continue that challenge through prototype, field implementation, co-op or residency, scale planning, portfolio, and final defense.

## Graduate Promises

1. See the whole system.
2. Work with AI responsibly and rigorously.
3. Learn continuously as AI evolves.
4. Turn problems into validated prototypes.
5. Bridge people, data, and implementation.
6. Build evidence of transformation capability.

## Differentiation

The program is distinct from traditional engineering master's programs, AI/data science programs, engineering management programs, short AI bootcamps, and conventional co-op programs.

Its central promise is evidence-based transformation capability:

- Students diagnose real systems.
- Students use and evaluate AI with professional discipline.
- Students prototype and validate interventions.
- Students work with sponsors and domain experts.
- Students graduate with portfolio evidence and a competency defense.
```

- [ ] **Step 2: Verify proposal narrative coverage**

Run:

```powershell
rg -n "Systems-level diagnosis|Trusted data collaboration|AI-Native Systems Transformation|Hybrid Transformation Engineers|Studio-Centered MEng|Graduate Promises|Differentiation" docs/ai-native-systems-transformation-meng/00-proposal-narrative.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit proposal narrative**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/00-proposal-narrative.md
git commit -m "docs: write MEng proposal narrative"
```

Expected: Git creates one commit for the proposal narrative.

## Task 3: Write The Competency Model And Rubric

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/01-competency-model-and-rubric.md`

- [ ] **Step 1: Write the competency model and rubric**

Create `docs/ai-native-systems-transformation-meng/01-competency-model-and-rubric.md` with this content:

```markdown
# 01 Competency Model And Rubric

## Competency Architecture

The program uses a layered competency model:

1. Foundational competencies.
2. Transformation competencies.
3. Professional judgment competencies.
4. Evidence of mastery.

Every student must meet the common core. Students then demonstrate differentiated excellence in one or two signature areas.

## Graduate Promises

| Promise | Graduate Can Do |
|---|---|
| See the whole system | Map technical processes, data flows, human workflows, incentives, and external dependencies |
| Work with AI responsibly and rigorously | Use AI tools while checking outputs, documenting assumptions, evaluating risks, and overriding automation when needed |
| Learn continuously as AI evolves | Evaluate emerging AI capabilities, update methods, and transfer learning across unfamiliar domains |
| Turn problems into validated prototypes | Move from diagnosis to prototype and test technical, workflow, and value assumptions |
| Bridge people, data, and implementation | Communicate with engineers, domain experts, managers, users, and partners |
| Build evidence of transformation capability | Produce portfolio, sponsor evidence, AI work logs, evaluation artifacts, and defense evidence |

## Layer 1: Foundational Competencies

| Competency | Baseline Evidence |
|---|---|
| AI systems literacy and integration | Explains ML, LLM, and agent architecture choices in a project context |
| Data and digital systems literacy | Maps data sources, quality limits, APIs, schemas, security, and interoperability needs |
| Systems thinking | Produces a system map with boundaries, stakeholders, dependencies, feedback, and constraints |
| Communication and collaboration | Produces sponsor-facing summaries, technical memos, and team decision records |

## Layer 2: Transformation Competencies

| Competency | Baseline Evidence |
|---|---|
| Systems diagnosis | Identifies bottlenecks, root causes, constraints, and opportunity thesis |
| Trusted data collaboration | Defines data access, governance, sovereignty, incentives, compliance, and responsible use |
| Implementation/prototyping | Builds software/data, cyber-physical/process, or service/product prototype matched to the project |
| Human-AI work design | Defines workflows, decision rights, handoffs, accountability, and adoption routines |

## Layer 3: Professional Judgment Competencies

| Competency | Baseline Evidence |
|---|---|
| AI-guided engineering judgment | Verifies AI outputs using domain knowledge, evidence, ethics, safety, and constraints |
| Responsibility and risk judgment | Identifies failure modes, affected stakeholders, privacy, safety, and accountability boundaries |
| Adaptive learning and technology renewal | Documents how emerging AI tools were assessed, accepted, rejected, or integrated |
| Work-readiness | Manages ambiguity, milestones, sponsor communication, decision records, and evidence capture |

## Signature Excellence Areas

| Excellence Area | Distinctive Evidence |
|---|---|
| AI Systems Integration | AI workflow architecture, evaluation harness, deployment logic, governance plan |
| Systems Diagnosis | Strong system maps, root-cause analysis, value/risk logic, transformation roadmap |
| Implementation/Prototyping | Validated prototype, user/workflow testing, field constraints, iteration records |
| Practical Transformation Leadership | Sponsor coordination, stakeholder communication, project governance, adoption planning |

## Four-Level Rubric

| Level | Meaning | Evidence Standard |
|---|---|---|
| 1 Emerging | Student can explain concepts but needs heavy guidance | Course assignments and partial studio evidence |
| 2 Developing | Student can apply methods to bounded project work | Studio gate evidence with instructor correction |
| 3 Proficient | Student can integrate methods under real project ambiguity | Sponsor-facing project evidence and defensible decisions |
| 4 Distinctive | Student shows leadership or excellence in a signature area | Portfolio evidence recognized by faculty and sponsor reviewers |

## Minimum Graduation Standard

Each graduate must reach Level 3 in all common-core competency families and Level 4 in at least one signature excellence area.
```

- [ ] **Step 2: Verify competency anchors**

Run:

```powershell
rg -n "Adaptive learning|AI Systems Integration|Systems Diagnosis|Implementation/Prototyping|Practical Transformation Leadership|Minimum Graduation Standard|Level 4" docs/ai-native-systems-transformation-meng/01-competency-model-and-rubric.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit competency model**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/01-competency-model-and-rubric.md
git commit -m "docs: define MEng competency rubric"
```

Expected: Git creates one commit for the competency model and rubric.

## Task 4: Write Student Personas And Bridging Model

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/02-student-personas-and-bridging.md`

- [ ] **Step 1: Write personas and bridging model**

Create `docs/ai-native-systems-transformation-meng/02-student-personas-and-bridging.md` with this content:

```markdown
# 02 Student Personas And Bridging

## Admissions Baseline

The first few years use a STEM-plus admissions baseline. Eligible backgrounds include engineering, computer science, data science, applied science, architecture, industrial design, operations, systems, supply chain, HCI, and related technical fields.

## Persona Model

The program uses starting personas for admissions, bridging, team formation, advising, and employer communication.

## Persona 1: AI-Strong Technologist

Starting strengths:

- AI, software, data science, automation, or applied computing.
- Ability to build or understand technical systems.

Development needs:

- Systems diagnosis.
- Domain immersion.
- Stakeholder communication.
- Responsible implementation.
- Value and workflow validation.

Likely excellence areas:

- AI Systems Integration.
- Implementation/Prototyping.

## Persona 2: Domain/Engineering Practitioner

Starting strengths:

- Engineering fundamentals and physical or technical system constraints.
- Discipline-based problem solving.

Development needs:

- AI systems literacy.
- Data collaboration.
- Digital prototyping.
- Agent/tool operating discipline.
- Cross-domain transformation language.

Likely excellence areas:

- Systems Diagnosis.
- Implementation/Prototyping.

## Persona 3: Systems/Operations Thinker

Starting strengths:

- Processes, optimization, logistics, operations, systems, analytics, or supply chain.
- Ability to reason about flows and tradeoffs.

Development needs:

- AI/data integration.
- Human-centered implementation.
- Prototyping practice.
- Sponsor-facing evidence.

Likely excellence areas:

- Systems Diagnosis.
- Practical Transformation Leadership.

## Persona 4: Design/Product/Change-Oriented Integrator

Starting strengths:

- User needs, product thinking, service design, HCI, innovation, or technical integration.
- Ability to connect people, workflows, and solutions.

Development needs:

- Technical AI/data foundations.
- Systems rigor.
- Engineering validation.
- Evidence-based decision discipline.

Likely excellence areas:

- Implementation/Prototyping.
- Practical Transformation Leadership.

## Bridging Model

The program uses a hybrid bridging model:

1. Common foundation bootcamp for all students.
2. Entry diagnostics for AI/data, systems, prototyping, communication, and project readiness.
3. Persona-based bridging modules.
4. Advising review after the Semester 1 gate package.

## Common Foundation Bootcamp

All students complete short modules in:

- AI systems and responsible AI use.
- Data and digital systems basics.
- Systems mapping.
- PBL and studio expectations.
- Sponsor communication.
- Evidence capture and portfolio practice.

## Persona-Based Bridging

| Persona | Required Bridging Focus |
|---|---|
| AI-Strong Technologist | Systems diagnosis, domain immersion, sponsor communication |
| Domain/Engineering Practitioner | AI/data integration, software/data prototyping, AI operating discipline |
| Systems/Operations Thinker | AI systems integration, implementation prototyping, human-AI work design |
| Design/Product/Change-Oriented Integrator | Technical AI/data foundations, systems rigor, engineering validation |

## Team Formation Rule

Project teams should mix AI, domain, systems, and integration strengths. No team should rely on one student to own all AI work or one student to own all sponsor communication.
```

- [ ] **Step 2: Verify persona coverage**

Run:

```powershell
rg -n "AI-Strong Technologist|Domain/Engineering Practitioner|Systems/Operations Thinker|Design/Product/Change-Oriented Integrator|STEM-plus|Common Foundation Bootcamp|Team Formation Rule" docs/ai-native-systems-transformation-meng/02-student-personas-and-bridging.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit personas and bridging**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/02-student-personas-and-bridging.md
git commit -m "docs: define MEng personas and bridging"
```

Expected: Git creates one commit for personas and bridging.

## Task 5: Write Curriculum Map

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/03-curriculum-map.md`

- [ ] **Step 1: Write the curriculum map**

Create `docs/ai-native-systems-transformation-meng/03-curriculum-map.md` with this content:

```markdown
# 03 Curriculum Map

## Curriculum Principle

The curriculum is a layered hybrid. Course names remain recognizable for academic approval, but sequencing follows the transformation lifecycle and assessment is competency-based.

## Two-Year Rhythm

| Term | Theme | PBL Focus | Industry Immersion | Main Evidence |
|---|---|---|---|---|
| Semester 1 | Foundations, Discovery, Commitment | Problem discovery and diagnosis | Site visits, sponsor clinics, challenge marketplace | Gate package |
| Semester 2 | Model, Prototype, Validate | First serious intervention | Sponsor reviews, workflow/data access, prototype feedback | Prototype validation review |
| Semester 3 | Field Implementation / Co-op Residency | High-contact implementation | Full-time, near-full-time, or equivalent high-contact project | Sponsor evaluation and field log |
| Semester 4 | Scale, Govern, Defend | Synthesis and scale planning | Final sponsor board and handoff | Portfolio and competency defense |

## Common Six-Block Core

1. Systems diagnosis.
2. AI systems integration.
3. Data collaboration/governance.
4. Implementation/prototyping.
5. Human-AI-organization work design.
6. Professional communication/project practice.

## Course And Studio Sequence

| Term | Core Courses | Studio | Workshops |
|---|---|---|---|
| Semester 1 | AI Systems Foundations; Systems Diagnosis And Transformation Mapping; Professional Practice Foundations | Studio 1: Problem Discovery And Transformation Diagnosis | AI Operating Discipline I; Sponsor Interviewing; Responsibility Foundations |
| Semester 2 | AI Systems Integration; Trusted Data Collaboration And Governance; Implementation And Prototyping Methods; Human-AI Work Design | Studio 2: AI-Enabled Prototype And Validation | Data Access Negotiation; Evaluation Harness Design; Prototype Review Clinic |
| Semester 3 | Field Seminar; Excellence-Area Elective 1 | Studio 3: Field Implementation / Co-op Residency | Field Evidence Capture; Risk Review; Sponsor Communication Clinic |
| Semester 4 | Excellence-Area Elective 2; Scale And Governance Seminar | Studio 4: Scale, Governance, Portfolio, And Competency Defense | Portfolio Writing; Defense Preparation; Career Translation |

## Semester 1 Gate Package

By the end of Semester 1, each student or team produces:

- Transformation diagnosis report.
- Project charter.
- Learning contract.
- Small feasibility demonstration.

## Prototype Validation Standard

Every substantial prototype must address:

- Technical soundness.
- User/workflow fit.
- Operational/value logic.

## Co-op / Residency Placement

The high-intensity co-op or residency window is designed for Semester 3, but industry immersion begins in Semester 1 and continues across all terms.
```

- [ ] **Step 2: Verify curriculum anchors**

Run:

```powershell
rg -n "Semester 1|Semester 2|Semester 3|Semester 4|Common Six-Block Core|Gate package|Prototype Validation Standard|Co-op / Residency" docs/ai-native-systems-transformation-meng/03-curriculum-map.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit curriculum map**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/03-curriculum-map.md
git commit -m "docs: map MEng curriculum spine"
```

Expected: Git creates one commit for the curriculum map.

## Task 6: Write Course And Workshop Designs

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/04-course-and-workshop-designs.md`

- [ ] **Step 1: Write course and workshop designs**

Create `docs/ai-native-systems-transformation-meng/04-course-and-workshop-designs.md` with this content:

```markdown
# 04 Course And Workshop Designs

## Core Course Design Rule

Every core course must feed the studio spine. Each course produces methods, artifacts, or evidence that students use in their PBL challenge.

## Core Courses

### AI Systems Foundations

Purpose: build common language for ML, LLMs, agents, AI limitations, and responsible use.

Student outputs:

- AI system concept map.
- AI risk checklist.
- First AI work log entry.

### Systems Diagnosis And Transformation Mapping

Purpose: teach students to map systems before proposing solutions.

Student outputs:

- System boundary map.
- Stakeholder map.
- Bottleneck and root-cause analysis.
- Opportunity thesis.

### Professional Practice Foundations

Purpose: establish sponsor communication, teamwork, project documentation, and technical writing habits.

Student outputs:

- Sponsor interview protocol.
- Team working agreement.
- Decision record template.
- Project communication memo.

### AI Systems Integration

Purpose: teach students to design, evaluate, and govern AI-enabled workflows.

Student outputs:

- AI workflow architecture.
- Model or agent evaluation plan.
- Human-in-the-loop decision map.

### Trusted Data Collaboration And Governance

Purpose: connect data engineering basics with trust, governance, sovereignty, standards, compliance, incentives, cybersecurity awareness, and responsible use.

Student outputs:

- Data landscape map.
- Data access plan.
- Data risk and governance memo.

### Implementation And Prototyping Methods

Purpose: teach disciplined prototyping across software/data, cyber-physical/process, and service/product contexts.

Student outputs:

- Prototype plan.
- Validation plan.
- Iteration log.

### Field Seminar

Purpose: support the Semester 3 co-op, residency, or equivalent high-contact field implementation phase by structuring evidence capture, reflection, sponsor communication, and risk review while students work in real implementation contexts.

Student outputs:

- Field implementation log.
- Sponsor communication update.
- Risk review memo.
- Field reflection on implementation constraints, decisions, and evidence.

### Human-AI Work Design

Purpose: redesign workflows, decision rights, roles, handoffs, accountability, adoption routines, and human factors around AI-enabled systems.

Student outputs:

- Current-state workflow.
- Future-state human-AI workflow.
- Adoption risk memo.

### Scale And Governance Seminar

Purpose: prepare students to move from prototype evidence to implementation recommendation, governance model, and scale plan.

Student outputs:

- Scale plan.
- Governance plan.
- Residual risk register.

## Required Workshop Series

### AI Operating Discipline I

Topics:

- Prompting and task decomposition.
- Human verification of AI outputs.
- AI work log format.
- When not to use AI.

Output: first AI work log.

### Evaluation Harness Design

Topics:

- Rubrics for AI output quality.
- Test cases for agentic workflows.
- Failure mode capture.
- Human review thresholds.

Output: project-specific evaluation harness.

### Responsibility Foundations

Topics:

- Ethics.
- Safety.
- Privacy.
- Accountability.
- Affected stakeholders.
- Failure modes.

Output: responsibility memo draft.

### Data Access Negotiation

Topics:

- Data access expectations.
- Data minimization.
- Security.
- Partner trust.
- Compliance.

Output: data/access plan for sponsor review.

### Portfolio Writing

Topics:

- Evidence selection.
- Reflection.
- Competency claims.
- Sponsor-facing storytelling.

Output: portfolio evidence map.

### Defense Preparation

Topics:

- Competency defense structure.
- Evidence argument.
- Sponsor and faculty question handling.

Output: defense outline.
```

- [ ] **Step 2: Verify course and workshop anchors**

Run:

```powershell
rg -n "AI Systems Foundations|Trusted Data Collaboration|Implementation And Prototyping Methods|Field Seminar|Human-AI Work Design|AI Operating Discipline I|Evaluation Harness Design|Responsibility Foundations|Defense Preparation" docs/ai-native-systems-transformation-meng/04-course-and-workshop-designs.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit course and workshop designs**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/04-course-and-workshop-designs.md
git commit -m "docs: outline MEng courses and workshops"
```

Expected: Git creates one commit for course and workshop designs.

## Task 7: Write PBL Studio And Gate System

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/05-pbl-studio-and-gate-system.md`

- [ ] **Step 1: Write the studio and gate system**

Create `docs/ai-native-systems-transformation-meng/05-pbl-studio-and-gate-system.md` with this content:

```markdown
# 05 PBL Studio And Gate System

## Studio Principle

The studio is the program spine. Courses supply methods; studios force integration under real ambiguity.

Studios are credit-bearing and repeated every semester. Each studio ends in a gate review with required evidence that must be reviewed before students proceed to the next phase.

## Studio 1: Problem Discovery And Transformation Diagnosis

Timing: Semester 1.

Purpose:

- Expose students to multiple real problem contexts.
- Build diagnosis capability.
- Match students or teams to one deep challenge by the end of Semester 1.

Required activities:

- Site visits or equivalent field exposure.
- Sponsor clinics.
- Expert interviews.
- Problem comparison.
- System mapping.
- Feasibility demonstration.

Gate package:

- Transformation diagnosis report.
- Project charter.
- Learning contract.
- Small feasibility demonstration.

## Studio 2: AI-Enabled Prototype And Validation

Timing: Semester 2.

Purpose:

- Convert the selected challenge into a meaningful intervention.
- Test technical soundness, user/workflow fit, and operational/value logic.

Required evidence:

- Prototype artifact.
- Validation plan.
- AI work log.
- Evaluation harness.
- Sponsor feedback.
- Prototype iteration record.

## Studio 3: Field Implementation / Co-op Residency Studio

Timing: Semester 3.

Purpose:

- Conduct high-contact field implementation through co-op, residency, or equivalent applied project.
- Capture evidence from real constraints, users, workflows, and sponsors.

Required evidence:

- Field implementation log.
- Sponsor review.
- Risk review.
- Revised system map.
- Implementation decision record.
- Responsibility memo update.

## Studio 4: Scale, Governance, Portfolio, And Competency Defense

Timing: Semester 4.

Purpose:

- Synthesize the project.
- Prepare scale and governance recommendations.
- Complete portfolio.
- Defend competency claims.

Required evidence:

- Final project report.
- Scale plan.
- Governance plan.
- Residual risk register.
- Portfolio.
- Final competency defense.

## Review Gates

| Gate | Timing | Required Reviewers | Required Evidence |
|---|---|---|---|
| Gate 1: Challenge Commitment | End of Semester 1 | Faculty advisor, sponsor, studio lead | Diagnosis report, charter, learning contract, feasibility demo |
| Gate 2: Prototype Validation | End of Semester 2 | Faculty advisor, technical reviewer, sponsor | Prototype, validation evidence, AI work log, evaluation harness |
| Gate 3: Field Implementation Review | End of Semester 3 | Faculty advisor, sponsor, program reviewer | Field log, sponsor evaluation, risk review, implementation evidence |
| Gate 4: Final Defense | End of Semester 4 | Faculty panel, sponsor representative, program reviewer | Portfolio, final report, defense evidence, competency rubric |
```

- [ ] **Step 2: Verify studio gate coverage**

Run:

```powershell
rg -n "Studio 1|Studio 2|Studio 3|Studio 4|Challenge Commitment|Prototype Validation|Field Implementation Review|Final Defense" docs/ai-native-systems-transformation-meng/05-pbl-studio-and-gate-system.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit studio system**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/05-pbl-studio-and-gate-system.md
git commit -m "docs: define MEng PBL studio gates"
```

Expected: Git creates one commit for the PBL studio and gate system.

## Task 8: Write AI Operating Discipline

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/06-ai-operating-discipline.md`

- [ ] **Step 1: Write the AI operating discipline**

Create `docs/ai-native-systems-transformation-meng/06-ai-operating-discipline.md` with this content:

```markdown
# 06 AI Operating Discipline

## Purpose

Students must learn to work with AI as a professional operating discipline, not as casual tool use.

## Required Student Habits

- Decompose tasks before using AI.
- State assumptions and constraints.
- Keep human responsibility visible.
- Check outputs against evidence, domain knowledge, and project constraints.
- Reject AI outputs when they are unsafe, unsupported, irrelevant, or misleading.
- Document what AI contributed and what humans changed.
- Evaluate new AI tools critically as technologies evolve.

## AI Work Log

Each substantial AI-assisted task must record:

- Date.
- Task goal.
- AI tool or agent used.
- Input context.
- Key prompts or task instructions.
- Output summary.
- Human checks performed.
- Errors or weaknesses found.
- Decision: accepted, modified, rejected, or escalated.
- Evidence retained.

## Evaluation Harness

Each deep project must define a project-specific evaluation harness for AI-enabled outputs.

Minimum components:

- Output quality criteria.
- Test cases or review cases.
- Failure modes.
- Human review thresholds.
- Safety, privacy, and responsibility checks.
- Decision rule for accepting, modifying, rejecting, or escalating outputs.

## Responsibility Memo

Each student or team must maintain a responsibility memo covering:

- Where AI was used.
- Where AI was rejected.
- What risks remain.
- Who is accountable for final decisions.
- What affected stakeholders should know.
- What evidence supports the final recommendation.

## Required Evidence By Studio

| Studio | AI Operating Evidence |
|---|---|
| Studio 1 | First AI work log and AI risk checklist |
| Studio 2 | Evaluation harness and prototype AI work logs |
| Studio 3 | Field-use AI work logs and responsibility memo update |
| Studio 4 | Final AI operating evidence package for defense |
```

- [ ] **Step 2: Verify AI operating evidence**

Run:

```powershell
rg -n "AI Work Log|Evaluation Harness|Responsibility Memo|accepted, modified, rejected, or escalated|technologies evolve" docs/ai-native-systems-transformation-meng/06-ai-operating-discipline.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit AI operating discipline**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/06-ai-operating-discipline.md
git commit -m "docs: define MEng AI operating discipline"
```

Expected: Git creates one commit for the AI operating discipline.

## Task 9: Write Industry Partnership And Co-op Model

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/07-industry-partnership-and-coop-model.md`

- [ ] **Step 1: Write the partnership and co-op model**

Create `docs/ai-native-systems-transformation-meng/07-industry-partnership-and-coop-model.md` with this content:

```markdown
# 07 Industry Partnership And Co-op Model

## Partnership Principle

Industry partners are part of the learning architecture. They provide problem contexts, review evidence, support field access, and help validate whether student work is useful.

## Partner Tiers

| Tier | Name | Partner Role |
|---|---|---|
| 1 | Problem Sponsor | Provides project brief, context, limited data or examples, milestone feedback, final review |
| 2 | Co-Educator | Provides Tier 1 support plus mentoring, guest workshops, site access, expert interviews, data/workflow access, project clinics |
| 3 | Residency Host | Provides Tier 2 support plus co-op or residency supervision, workplace performance evaluation, deeper implementation access |

## Deep Challenge Commitment Requirements

Before students commit to a deep challenge at the end of Semester 1, the partner must provide:

- Problem brief.
- Sponsor contact.
- Review schedule.
- Data/access plan.
- Expected value statement.

## Continuous Immersion Model

| Term | Industry Engagement |
|---|---|
| Semester 1 | Problem marketplace, site visits, sponsor clinics, interviews, scoping |
| Semester 2 | Regular sponsor reviews, prototype feedback, user/workflow validation, data access |
| Semester 3 | High-intensity co-op, residency, or equivalent high-contact implementation |
| Semester 4 | Final sponsor board, implementation handoff, portfolio evidence, defense input |

## Co-op Design Principle

The co-op is not detached work experience. It is the field implementation phase of the PBL spine.

Students enter co-op or residency with:

- Diagnosis.
- Charter.
- Learning contract.
- Prototype direction.
- AI operating discipline.
- Evidence plan.

## Partner Value Proposition

Partners receive:

- Structured diagnosis of transformation opportunities.
- Prototypes or workflow interventions.
- Student teams trained in responsible AI use.
- Documented evidence and implementation recommendations.
- Access to future talent.
- Low-risk exploration of AI-native transformation.

## Program Governance Needs

The program needs a partnership function to manage:

- Challenge intake.
- Partner tiering.
- Data/access expectations.
- Student matching.
- Review schedules.
- Sponsor feedback.
- Co-op quality.
- Project risk escalation.
```

- [ ] **Step 2: Verify partnership model**

Run:

```powershell
rg -n "Problem Sponsor|Co-Educator|Residency Host|Deep Challenge Commitment Requirements|Continuous Immersion Model|field implementation phase|Partner Value Proposition" docs/ai-native-systems-transformation-meng/07-industry-partnership-and-coop-model.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit partnership and co-op model**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/07-industry-partnership-and-coop-model.md
git commit -m "docs: define MEng partnership and co-op model"
```

Expected: Git creates one commit for the industry partnership and co-op model.

## Task 10: Write Assessment, Portfolio, And Defense Handbook

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/08-assessment-portfolio-and-defense.md`

- [ ] **Step 1: Write the assessment handbook**

Create `docs/ai-native-systems-transformation-meng/08-assessment-portfolio-and-defense.md` with this content:

```markdown
# 08 Assessment, Portfolio, And Defense

## Assessment Principle

Students pass by producing defensible evidence of transformation capability, not by merely completing courses.

## Graduation Evidence

Each student must complete:

1. Longitudinal project portfolio.
2. Deep industry, co-op, or capstone challenge.
3. AI operating evidence.
4. Prototype validation evidence.
5. Sponsor or field evidence.
6. Final competency defense.

## Portfolio Structure

Each portfolio contains:

- Student profile and starting persona.
- Learning contract.
- Competency map.
- System diagnosis evidence.
- AI operating evidence.
- Prototype artifacts.
- Validation evidence.
- Sponsor or field evidence.
- Reflection on adaptive learning and technology renewal.
- Final competency claim.

## Final Defense Structure

The final defense includes:

1. Program identity statement.
2. Project context and system diagnosis.
3. AI integration and operating discipline evidence.
4. Prototype and validation evidence.
5. Field constraints and sponsor feedback.
6. Responsibility, safety, privacy, and risk judgment.
7. Adaptive learning evidence.
8. Signature excellence claim.
9. Faculty and sponsor questions.

## Defense Panel

The defense panel includes:

- Faculty chair.
- Technical reviewer.
- Studio lead or advisor.
- Sponsor representative or external reviewer.

## Pass Standard

Each student must demonstrate:

- Level 3 proficiency in all common-core competency families.
- Level 4 distinctive evidence in at least one signature excellence area.
- Complete AI work log, evaluation harness, and responsibility memo.
- Prototype validation across technical soundness, user/workflow fit, and operational/value logic.
```

- [ ] **Step 2: Verify assessment anchors**

Run:

```powershell
rg -n "defensible evidence|Longitudinal project portfolio|Final Defense Structure|adaptive learning|Level 3 proficiency|Level 4 distinctive evidence|AI work log" docs/ai-native-systems-transformation-meng/08-assessment-portfolio-and-defense.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit assessment handbook**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/08-assessment-portfolio-and-defense.md
git commit -m "docs: define MEng assessment and defense"
```

Expected: Git creates one commit for assessment, portfolio, and defense.

## Task 11: Write Launch Roadmap And Governance

**Files:**
- Create: `docs/ai-native-systems-transformation-meng/09-launch-roadmap-and-governance.md`

- [ ] **Step 1: Write the launch roadmap and governance model**

Create `docs/ai-native-systems-transformation-meng/09-launch-roadmap-and-governance.md` with this content:

```markdown
# 09 Launch Roadmap And Governance

## Launch Principle

The first few years should protect quality by using a STEM-plus admissions baseline, a controlled partner model, and a manageable number of deep challenges.

## Year 0: Proposal And Pilot Preparation

Goals:

- Finalize proposal narrative.
- Secure faculty alignment.
- Define course ownership.
- Build partner challenge intake process.
- Prepare studio rubrics.
- Select pilot partner problems.

Exit evidence:

- Proposal package.
- Draft course syllabi.
- Studio gate rubrics.
- Partner challenge templates.
- Initial partner list.

## Year 1: First Cohort Launch

Goals:

- Run common bootcamp.
- Run Studio 1 challenge marketplace.
- Commit student teams to deep challenges.
- Run first prototype cycle.
- Test AI operating discipline.

Exit evidence:

- Semester 1 gate packages.
- Prototype validation reviews.
- AI work logs and evaluation harnesses.
- Partner feedback.

## Year 2: Co-op And Defense Validation

Goals:

- Run high-intensity co-op or residency window.
- Validate sponsor supervision model.
- Run first final defenses.
- Review competency rubric against actual evidence.

Exit evidence:

- Field implementation logs.
- Sponsor evaluations.
- Final portfolios.
- Defense outcomes.
- Program improvement report.

## Year 3: Scale And Refine

Goals:

- Expand partner tiers.
- Refine admissions diagnostics.
- Add excellence-area electives.
- Improve co-op matching.
- Strengthen employer communication.

Exit evidence:

- Revised curriculum map.
- Partner tier report.
- Graduate outcome evidence.
- Updated competency rubric.

## Governance Roles

| Role | Responsibility |
|---|---|
| Program director | Owns program identity, governance, partner alignment, and quality |
| Curriculum lead | Owns course sequence, learning outcomes, and academic coherence |
| Studio lead | Owns PBL studios, gate reviews, and evidence standards |
| Partnership lead | Owns challenge intake, partner tiering, co-op quality, and sponsor feedback |
| Assessment lead | Owns competency rubric, portfolio requirements, and final defense quality |
| Faculty advisors | Guide student teams and evaluate evidence |

## Risk Register

| Risk | Mitigation |
|---|---|
| Program becomes too broad | Keep common competency baseline and studio gate evidence strict |
| PBL becomes secondary to courses | Make studios credit-bearing and require gate evidence each semester |
| Partners provide vague problems | Require problem brief, sponsor contact, review schedule, data/access plan, expected value statement |
| AI use becomes casual tool use | Require AI work log, evaluation harness, and responsibility memo |
| Co-op quality varies by partner | Use partner tiers, supervision expectations, and sponsor evaluations |
| Students have uneven technical foundations | Use common bootcamp plus diagnostic/persona-based bridging |
| Leadership expects narrow AI training | Use proposal narrative to stress systems transformation, responsible integration, and evidence-based practice |
```

- [ ] **Step 2: Verify launch roadmap**

Run:

```powershell
rg -n "Year 0|Year 1|Year 2|Year 3|Program director|Curriculum lead|Studio lead|Partnership lead|Risk Register" docs/ai-native-systems-transformation-meng/09-launch-roadmap-and-governance.md
```

Expected: matches for all listed phrases.

- [ ] **Step 3: Commit launch roadmap**

Run:

```powershell
git add docs/ai-native-systems-transformation-meng/09-launch-roadmap-and-governance.md
git commit -m "docs: define MEng launch roadmap"
```

Expected: Git creates one commit for launch roadmap and governance.

## Task 12: Final Consistency Verification

**Files:**
- Verify: `docs/ai-native-systems-transformation-meng/*.md`
- Verify: `docs/superpowers/specs/2026-05-13-ai-native-systems-transformation-meng-design.md`

- [ ] **Step 1: Verify expected files exist**

Run:

```powershell
$paths = @(
  'docs/ai-native-systems-transformation-meng/README.md',
  'docs/ai-native-systems-transformation-meng/00-proposal-narrative.md',
  'docs/ai-native-systems-transformation-meng/01-competency-model-and-rubric.md',
  'docs/ai-native-systems-transformation-meng/02-student-personas-and-bridging.md',
  'docs/ai-native-systems-transformation-meng/03-curriculum-map.md',
  'docs/ai-native-systems-transformation-meng/04-course-and-workshop-designs.md',
  'docs/ai-native-systems-transformation-meng/05-pbl-studio-and-gate-system.md',
  'docs/ai-native-systems-transformation-meng/06-ai-operating-discipline.md',
  'docs/ai-native-systems-transformation-meng/07-industry-partnership-and-coop-model.md',
  'docs/ai-native-systems-transformation-meng/08-assessment-portfolio-and-defense.md',
  'docs/ai-native-systems-transformation-meng/09-launch-roadmap-and-governance.md'
)
$paths | ForEach-Object { "$_ => $(Test-Path $_)" }
```

Expected: every line ends with `True`.

- [ ] **Step 2: Verify core design anchors across the package**

Run:

```powershell
rg -n "AI-Native Systems Transformation|Hybrid Transformation Engineer|Studio-Centered MEng|continuous|co-op|portfolio|evaluation harness|responsibility memo|adaptive learning|final competency defense" docs/ai-native-systems-transformation-meng
```

Expected: matches across multiple package files, including proposal, curriculum, AI operating discipline, partnership, and assessment documents.

- [ ] **Step 3: Verify no unfinished-marker terms remain in created artifacts**

Run:

```powershell
$markers = @('TB' + 'D', 'TO' + 'DO', 'FIX' + 'ME', 'place' + 'holder', 'fill' + ' in', 'implement' + ' in a future pass', 'un' + 'clear')
$pattern = $markers -join '|'
rg -n $pattern docs/ai-native-systems-transformation-meng
```

Expected: no matches.

- [ ] **Step 4: Compare artifact package against the approved spec**

Run:

```powershell
rg -n "Graduate Promises|Student Personas|Two-Year Curriculum|Course Design|Industry Partnership|Graduation Evidence|Program Differentiation" docs/superpowers/specs/2026-05-13-ai-native-systems-transformation-meng-design.md
```

Expected: matches for all listed spec sections. Confirm each spec section maps to at least one created artifact:

| Spec Section | Artifact |
|---|---|
| Program Positioning | `00-proposal-narrative.md` |
| High-Level Student Competency Vision | `00-proposal-narrative.md`, `01-competency-model-and-rubric.md` |
| Competency Model | `01-competency-model-and-rubric.md` |
| Student Personas | `02-student-personas-and-bridging.md` |
| Two-Year Curriculum And PBL Architecture | `03-curriculum-map.md`, `05-pbl-studio-and-gate-system.md` |
| Course Design And Assessment | `04-course-and-workshop-designs.md`, `08-assessment-portfolio-and-defense.md` |
| Industry Partnership And Co-op Model | `07-industry-partnership-and-coop-model.md` |
| Graduation Evidence And Program Differentiation | `08-assessment-portfolio-and-defense.md`, `00-proposal-narrative.md` |

- [ ] **Step 5: Commit final verification adjustments**

Run:

```powershell
git status --short
git add docs/ai-native-systems-transformation-meng
git commit -m "docs: complete MEng program package"
```

Expected: If earlier task commits captured every artifact, Git may report no changes to commit. If final review caused refinements, Git creates one final cleanup commit.

## Execution Notes

The first execution pass should produce documents that are clear enough for five review audiences:

- University leadership reviewing the program rationale and differentiation.
- Faculty reviewing curriculum coherence and course ownership.
- Industry partners reviewing project, co-op, and sponsor expectations.
- Students reviewing program identity, learning journey, and graduation evidence.
- Program administrators reviewing launch governance, partner intake, and risk control.

The strongest execution approach is to split work by artifact boundary:

- Proposal and competency package.
- Personas, curriculum, and courses.
- Studios, AI discipline, and assessment.
- Partnership, co-op, launch roadmap, and final verification.
