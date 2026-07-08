---
name: codebase-orientation-brief
description: >
  Turns a walk of an unfamiliar repo or module into a leader's orientation brief — what the
  system does, its shape and entry points, the risky and load-bearing parts, how work flows, and
  the questions to ask the team — so a leader can speak to it credibly in a review, incident, or
  planning meeting. Use when the user says "help me understand this codebase", "I inherited this
  repo", "orient me on this service before the meeting", or points an agent at a directory/repo
  they don't know. Use this to get oriented in code you don't own — use legacy-code-assessment to
  decide invest/rewrite/leave, and incident-code-triage to chase a live failure.
---

# Codebase Orientation Brief

Get a hands-on leader oriented in an unfamiliar codebase fast — enough to ask sharp questions, judge risk, and speak to the system credibly, without pretending to the depth of the engineers who own it. The brief maps the territory and marks the unknowns; it never guesses at behaviour it hasn't read.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent architecture, ownership, or behaviour you can't see in the code. Mark anything genuinely unavailable as **Unknown**.

- **The code** — repo or module path the agent can read (or pasted structure/key files)
- **Why now** — the reason for orienting: upcoming review, incident, inherited team, build-vs-buy, planning — this sets what to foreground
- **Depth** — a 5-minute meeting-prep skim vs a deeper map for a decision
- **What you already know** — so the brief adds signal instead of repeating the obvious
- **Team access** — whether you can ask the owning engineers follow-ups (shapes the "questions to ask" section)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Survey the top level first: README, package/build manifests, directory layout, entry points (main, routes, handlers, jobs). State what the system does in two sentences before any detail.
2. Map the **shape**: major components/modules and how they relate, the primary data flow (request → handler → data store, or job → queue → worker), and the external dependencies and integrations. Keep it to the load-bearing structure, not every file.
3. Identify **entry points and hot paths** — where execution starts and where the important work happens — so the leader knows where to look when something breaks.
4. Flag **risk and load-bearing parts**: complex or god modules, sparse tests, TODO/FIXME clusters, custom-vs-standard patterns, migration or data-loss surface, and anything that reads as fragile. Distinguish "I read this and it's risky" from "I couldn't tell — ask the team".
5. Note **conventions and gaps**: how the code is tested, built, and deployed as far as visible; and explicitly list what you could NOT determine from the code alone.
6. Write **questions to ask the team** — the specific, informed questions that close the biggest unknowns (ownership, why a surprising choice was made, what breaks most often).
7. Match depth to the reason: for meeting-prep, keep it to the summary, shape, and questions; for a decision, add the risk map and conventions in full.
8. Assemble the output in the format below. Cite file paths for claims so the leader can verify and go deeper.

## Output format

```
**Orientation: [repo/module]** — [why now]

**What it does:** [Two sentences.]

**Shape**
- [Component] — [role] (`path`)
- Primary flow: [A → B → C]
- External deps: [list]

**Entry points & hot paths**
- [Where execution starts / where the real work happens] (`path`)

**Risk & load-bearing**
- ⚠️ [Fragile/complex/untested area] (`path`) — [why it matters | or "unclear, ask team"]

**Conventions & gaps**
- Tests/build/deploy: [what's visible]
- Could not determine: [explicit unknowns]

**Questions to ask the team**
- [Specific, informed question]
```

## Boundaries

What the skill must never do.

- Never assert behaviour, ownership, or architecture you haven't read in the code — mark it **Unknown** and turn it into a question for the team.
- Never present a skim as deep understanding — the brief is for orientation, not to override the engineers who own the system.
- Never map every file — foreground the load-bearing structure and the risks; omit the rest.
- Always cite paths for claims so the leader can verify rather than trust the summary blindly.
- Never invent a git history, incident record, or test-coverage number — read it or mark it Unknown.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **legacy-code-assessment** when the orientation surfaces a system that needs an invest/rewrite/leave decision.
- After this, offer **prototype-spike-plan** when a question the brief raised is best answered by a small throwaway build.
