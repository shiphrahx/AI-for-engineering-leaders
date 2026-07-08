---
name: ai-agent-workflow-design
description: >
  Designs how a team wires AI agents into its actual development loop — which stages to automate
  (codegen, review, tests, triage, docs), where humans stay in the loop, the guardrails, and how
  to measure whether it helps — producing a concrete rollout, not a vague "use more AI". Use when
  the user says "how should my team use AI agents", "design our AI dev workflow", "where does AI
  fit in our pipeline", or wants a deliberate plan for AI in the SDLC. Use this to design the
  workflow and rollout — use ai-coding-guidelines for the norms/policy engineers follow, and
  build-vs-buy-analysis to choose a specific agent or tool.
variants: [startup, growth, enterprise]
---

# AI Agent Workflow Design

Design a deliberate, staged plan for putting AI agents into a team's development loop — where they add real leverage, where a human must stay in control, what guardrails keep it safe, and how you'll know if it's working. The output is a concrete rollout with gates and metrics, tool-neutral, not a mandate to "use AI more".

## Inputs to gather

Gather these before designing. If any are missing, ask for them in a single batched question — never invent the team's current workflow, tolerance for risk, or tooling. Mark anything genuinely unavailable as **Unknown**.

- **Current workflow** — how work flows today (planning → code → review → test → deploy) and where the friction is
- **Goal** — what the team wants more of (throughput, faster review, fewer toil tasks, better test coverage) and the problem prompting this
- **Team & risk posture** — size, seniority mix, domain, data sensitivity, and appetite for change
- **Existing AI use** — what agents/tools people already use, formally or informally
- **Constraints** — security/compliance limits, approved tools, and what must stay human-controlled (e.g. production deploys)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Map the **current loop** and mark the friction points — where time is lost to toil, waiting, or context-switching. AI should target real friction, not the stages that happen to be easy to automate.
2. For each SDLC stage, decide the **automation posture** — human-only, AI-assisted (human drives, AI helps), or AI-led (agent does it, human reviews). Candidate stages: planning/breakdown, code generation, code review, test writing, bug triage, docs, release notes, on-call/runbook assistance.
3. Fix the **human-in-the-loop gates**: what an agent may never do unattended (merge to main, deploy to prod, touch secrets/customer data, make an irreversible change). Higher risk and lower reversibility → more human control. State each gate explicitly.
4. Define **guardrails**: review bar for AI-generated code, verification requirements (tests must run/pass), secrets/data handling, and how agent output is checked before it counts. Reference the team's `ai-coding-guidelines` rather than restating them.
5. Sequence a **staged rollout**: start with a low-risk, high-toil stage (e.g. test scaffolding or PR summaries), prove value, then expand. Don't automate the riskiest stage first. Name the first slice and the expansion path.
6. Define **success metrics and a kill switch**: what improvement you expect (cycle time, review latency, escaped-defect rate, toil hours) and the signal that would tell you it's hurting quality (rising defect rate, review rubber-stamping, eroded understanding) — and what you'll do then.
7. Address the **human cost**: guard against skill erosion (juniors who can't work without the agent), review fatigue, and over-trust. Design for engineers staying accountable and capable, not dependent.
8. Adapt to context (see Variants) and assemble the output in the format below.

## Output format

```
**AI Agent Workflow — [team]**

**Goal:** [What this is meant to improve, and the friction it targets.]

**Stage-by-stage posture**
| Stage | Posture | Human gate | Notes |
|-------|---------|-----------|-------|
| Planning/breakdown | human-only / assisted / AI-led | [..] | [..] |
| Code generation | .. | [..] | [..] |
| Code review | .. | [..] | [..] |
| Tests | .. | [..] | [..] |
| Triage / on-call | .. | [..] | [..] |
| Docs / release notes | .. | [..] | [..] |

**Never unattended:** [Merge, deploy, secrets, irreversible changes — the hard gates.]

**Guardrails:** [Review bar, verification, data handling — ref ai-coding-guidelines.]

**Rollout**
1. First slice: [low-risk, high-toil stage] — prove [metric].
2. Then: [expansion path].

**Success metrics:** [What improves — cycle time, review latency, toil hours.]
**Watch for / kill switch:** [Quality signals that mean stop, and the response.]

**Human cost guardrails:** [Skill erosion, review fatigue, over-trust — mitigations.]
```

## Variants

Optional org-size tuning (see [`docs/VARIANTS.md`](../../../docs/VARIANTS.md)). Default to **growth** if the user doesn't state a stage.

- **startup** (≤ ~15 engineers): keep it lightweight — pick one or two high-leverage stages, minimal gates beyond "don't auto-deploy", move fast and watch quality.
- **growth** (~15–80): the full stage table and staged rollout with metrics.
- **enterprise** (80+): add security/compliance sign-off per stage, data-classification limits on what agents may touch, audit/traceability of agent actions, and a named owner for the workflow.

## Boundaries

What the skill must never do.

- Never design an AI-led posture for irreversible or high-blast-radius actions (prod deploy, data changes) without a human gate.
- Never recommend automating a stage just because it's easy — target real friction and real leverage.
- Never omit success metrics and a kill switch — a workflow you can't measure or stop is a liability.
- Never ignore the human cost — skill erosion and review rubber-stamping are real failure modes, design against them.
- Never restate the coding policy here — reference **ai-coding-guidelines** and keep this about workflow.
- Never lock the design to one vendor's agent — keep it tool-neutral.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **ai-coding-guidelines** to write the norms engineers follow within this workflow.
- After this, offer **build-vs-buy-analysis** when a stage needs a specific agent or tool chosen.
