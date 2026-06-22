---
name: system-design-document
description: >
  Produces a comprehensive system design document — a buildable technical blueprint covering
  requirements, architecture, data model, API, data flows, failure modes, operational and security
  concerns, and open questions. Use when the user says "write a system design", "design doc",
  "technical design for [system]", or describes a new service they need to document before coding.
  Use this for the full build-from blueprint of one system; use api-contract-design for the API
  surface in isolation, data-model-design for the schema in isolation, and technical-vision-document
  for multi-system 12-24 month direction rather than one implementation.
---

# System Design Document

Turn a system description into a blueprint detailed enough that a senior engineer could build from it alone — specific about data flows, failure modes, and operations, not just the happy path.

## Inputs to gather

Gather these before writing. If any are missing, ask in a single batched question — never invent scale numbers, constraints, or team facts. Mark anything genuinely unavailable as **Unknown** in the output.

- **System description** — what it does
- **Context** — why it's being built; what it replaces
- **Expected scale** — volume, growth, latency/reliability targets
- **Constraints** — tech stack, regulatory, multi-tenancy, integration requirements
- **Team context** — size, skills, timeline to MVP

## Steps

1. Read all inputs first. List any gap as **Unknown** rather than guessing a number or constraint.
2. Write the **Overview** — what the system does and why, in 2-3 sentences.
3. Capture **Requirements** split into functional (what it does) and non-functional (performance, reliability, security, retention, isolation). Quantify non-functional targets ("p95 < 30s", not "fast") and tie them to the stated scale.
4. Design the **Architecture** — a high-level diagram (ASCII is fine), the components, and how they interact. Name the technology for each component, justified by the constraints/team. Every component you add is something to monitor, deploy, and debug at 3am — justify it.
5. Specify the **Data model** — key entities, fields, types, relationships, indexes, and the source of truth.
6. Define the **API design** — key endpoints/interfaces with request/response shapes and status codes.
7. Walk the **Data flow** step-by-step for each primary use case, including the failure path, not only success. Treat idempotency and retries as first-class.
8. Enumerate **Failure modes** as a table: failure, impact, handling. Assume every external dependency can be slow, down, or duplicate-deliver; cover backlogs and idempotency.
9. Cover **Operational concerns** — deployment, monitoring, alerting thresholds, on-call implications and runbook topics.
10. Cover **Security considerations** — auth, data protection/encryption, PII and retention, rate limits, threat-model highlights.
11. List **Open questions** — unresolved design decisions for the team to discuss.
12. Adapt to context: for a system with no external API, cut API design and data flow and lead with architecture/data model/failure modes. For a distributed team review, add a glossary of non-universal terms. For a non-engineer audience, extract architecture diagram + requirements into a one-page summary. For a living document, add a "deviations from design" section to track where implementation diverged and why.
13. Assemble the output in the format below.

## Output format

```
**System Design: [System Name]**

**Overview**
[What it does and why — 2-3 sentences]

**Requirements**
*Functional:*
- [What it does]
*Non-functional:*
- [Performance / reliability / security / retention target, quantified]

**Architecture**
[Diagram]
Components:
- **[Component]:** [technology — responsibility]

**Data Model**
[Entities with fields, types, keys, indexes]

**API Design**
[Key endpoints with request/response shapes and status codes]

**Data Flow: [Primary Use Case]**
1. [Step]
**Data Flow: [Failure Path]**
[Steps]

**Failure Modes**
| Failure | Impact | Handling |
|---------|--------|----------|
| [failure] | [impact] | [handling] |

**Operational Concerns**
- Deploy / Monitoring / Alerting / On-call: [...]

**Security Considerations**
- [Auth / encryption / PII / rate limits]

**Open Questions**
1. [Unresolved decision]
```

## Boundaries

- Never fabricate scale numbers, constraints, team facts, or targets. Mark them **Unknown** and flag them as inputs to confirm.
- Never document only the happy path — every primary flow must have its failure path, and the failure-modes table is mandatory.
- Never pick a technology the team can't operate without flagging the operational cost and skill gap.
- This is a blueprint, not a decision proposal — document how to build it, not whether to.

## Chaining

- After this, offer **api-contract-design** to flesh out the API surface and **data-model-design** to detail the schema and indexes.
- Before a review board, offer **architecture-review-prep** to prepare the presentation and anticipated questions.
