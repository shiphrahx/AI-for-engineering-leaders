---
name: architecture-review-prep
description: >
  Produces a review-ready package for presenting a technical design — a timed presentation outline,
  the key decisions to highlight, 10-15 anticipated tough questions with prepared answers, an honest
  "I don't know yet" list, and the specific feedback to ask reviewers for. Use when the user says
  "prep for an architecture review", "present my design to staff/the board", "what will they ask",
  or has a design to defend. Use this to PREPARE the defence of an existing design; use
  system-design-document to write the design itself first.
---

# Architecture Review Prep

Prepare not just the design but for the tough questions — the best-prepared presenter has already thought through every objection and rehearsed a concise answer.

## Inputs to gather

Gather these before preparing. If any are missing, ask in a single batched question — never invent the design details, the audience, or the controversial points. Mark anything genuinely unavailable as **Unknown** in the output.

- **Design** — what's being proposed (or a link to the system design doc)
- **Audience** — who the reviewers are and their experience level
- **Controversial aspects** — what people are most likely to disagree with

## Steps

1. Confirm inputs. If the design or its controversial aspects aren't given, ask — the value is in anticipating the specific objections. Mark gaps **Unknown**.
2. Build a timed **Presentation outline** for a 30-minute review with 15 minutes of Q&A — problem statement, proposed architecture, data-flow walkthrough of the key use cases, alternatives considered and rejected, migration/rollback plan, then open questions.
3. Identify the **Key decisions to highlight** — the 3-4 choices most likely to generate discussion, each framed with the trade-off it makes.
4. Write **Anticipated questions** — 10-15 tough questions reviewers will ask, each with a prepared, concise answer. Cover the obvious "why not the simpler thing?" ("why not just optimise the existing DB?"), the team-capability question, the failure-mode and consistency questions, and the "why this technology not that one?" question. Ground answers in specifics and numbers.
5. Write the **"I don't know yet" list** — questions genuinely unresolved. Saying this honestly beats bluffing; the worst answer in an adversarial review is "I haven't thought about that."
6. Write **What you need from reviewers** — the specific feedback being asked for, so the review produces decisions, not just discussion.
7. Adapt to context: for a friendly review (own team), prepare less to deflect objections and more to gather input — bring options, not a finished proposal. For an adversarial review (principal engineers, architecture board), over-prepare and know your numbers. For a remote review, recommend sending the design doc 48 hours ahead so reviewers arrive with specific questions. (If the user is the reviewer rather than the presenter, the two highest-yield questions are "what's the simplest version that achieves the goal?" and "what happens when X fails?")
8. Assemble the output in the format below.

## Output format

```
**Architecture Review Prep: [Design Name]**

**Presentation Outline (30 minutes)**
- 0-5 min: [Problem statement + why current approach won't scale]
- 5-12 min: [Proposed architecture]
- 12-18 min: [Data-flow walkthrough of key use cases]
- 18-23 min: [Alternatives considered and rejected]
- 23-27 min: [Migration plan with rollback]
- 27-30 min: [Open questions + what you need]

**Key Decisions to Highlight**
1. [Decision — the trade-off it makes]

**Anticipated Questions and Prepared Answers**
*"[Tough question]"*
→ "[Concise, specific answer]"

**"I Don't Know Yet" List**
- [Genuinely unresolved question]

**What I Need From Reviewers**
1. [Specific feedback requested]
```

## Boundaries

- Never fabricate the design's metrics, alternatives, or the audience — mark them **Unknown**; prepared answers must rest on real numbers.
- Never bluff an answer in the prep — if it's unresolved, it belongs on the "I don't know yet" list, not in the answers.
- Never present only the chosen design — reviewers will ask what was rejected and why, so prepare the alternatives.
- This prepares a defence; it does not re-decide the design — surface weaknesses for the presenter, don't silently fix them.

## Chaining

- This commonly follows **system-design-document** (the design being reviewed).
- No natural successor in this pack — incorporate the review feedback back into the design doc.
