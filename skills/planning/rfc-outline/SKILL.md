---
name: rfc-outline
description: >
  Produces a reviewer-ready RFC (Request for Comments) for a proposed technical change:
  summary, motivation with data, proposed solution, alternatives considered, risks and
  mitigations, rollout plan, open questions, and measurable success criteria. Use when the
  user says "write an RFC", "draft a design doc", "technical proposal", or describes a
  change needing cross-team buy-in. Use this to propose and socialise a decision before
  committing engineering time — use architecture-decision-record to record a decision
  already made.
---

# RFC Outline

Turn a proposed technical change into an RFC thorough enough to decide on but concise enough that reviewers will actually read it — optimised for clarity and decision-making, not comprehensiveness.

## Inputs to gather

Gather these before drafting. If any are missing, ask for them in a single batched question — never invent the data behind the motivation, the constraints, or reviewer names. Mark anything genuinely unavailable as **Unknown**.

- **Proposed change** — what the user wants to build or change
- **Problem context** — the problem it solves, with supporting data (metrics, complaints, incidents) if available
- **Technical constraints** — existing systems, team experience, backward-compatibility windows, anything fixed
- **Reviewers / audience** — who needs to sign off, if known
- **Decision deadline** — if time-sensitive

## Steps

1. Read the change and problem fully. The RFC must give reviewers enough to evaluate trade-offs without drowning them — favour clarity over completeness.
2. Write **title and metadata** — RFC number (or placeholder), author, date, status (draft/review/approved/rejected), reviewers.
3. Write a **summary** — 3–4 sentences: what's proposed, why, and the expected outcome.
4. Write **motivation** — the problem, backed by data, customer complaints, or incidents that demonstrate the need. Do not invent numbers; mark missing data **Unknown**.
5. Write the **proposed solution** — what to build, with enough technical detail to evaluate trade-offs.
6. Write **alternatives considered** — 2–3 other approaches and why they were not chosen. Be genuinely generous to the alternatives; reviewers trust a proposal more when they see the options were taken seriously.
7. Write **risks and mitigations**, a **rollout plan** (incremental, safe, phased), **open questions** (specific things you want reviewer input on), and **success criteria** (measurable outcomes that tell you it worked).
8. Adapt to context: for a small change, scale down to Summary, Motivation, Proposed Solution, and Rollout Plan — not every RFC needs alternatives and open questions. For a controversial proposal, expand Alternatives Considered substantially. For a time-sensitive one, add a decision deadline to the metadata and a "cost of delay" note in Motivation. If the org doesn't use RFCs, the same format serves as a "Technical Design Doc" or "Architecture Proposal".
9. Assemble the output in the format below.

## Output format

```
**RFC-[NNN]: [Title]**

| Field | Value |
|-------|-------|
| Author | [name or Unknown] |
| Status | Draft |
| Reviewers | [names/roles or Unknown] |
| Date | [date] |
| Decision deadline | [date, if time-sensitive] |

**Summary**
[3–4 sentences: what, why, expected outcome]

**Motivation**
[The problem, with data/complaints/incidents. Mark missing data Unknown.]

**Proposed Solution**
[What to build, with enough technical detail to evaluate trade-offs]

**Alternatives Considered**
1. **[Alternative]** — [how it works; why not chosen]

**Risks and Mitigations**
- *[Risk]:* [mitigation]

**Rollout Plan**
1. [Phase — scope, timing]

**Open Questions**
1. [Specific question for reviewers]

**Success Criteria**
- [Measurable outcome]
```

## Boundaries

- Never fabricate the metrics, incidents, or customer complaints in the motivation — an RFC stands on evidence; mark missing data **Unknown**.
- Never invent reviewer names or a decision deadline — mark **Unknown**.
- Never strawman the alternatives — present them at their strongest.
- Never frame success criteria as outputs ("ship the gateway"); state measurable outcomes ("time-to-interactive < 1.5s").

## Chaining

- After the RFC is approved, offer **architecture-decision-record** to capture the chosen decision and its rationale durably.
- For a deeper technical design behind the proposal, offer the architecture pack's **system-design-document** if available.
