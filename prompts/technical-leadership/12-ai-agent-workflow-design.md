# AI Agent Workflow Design

## Situation

You want a deliberate plan for putting AI agents into your team's development loop — where they add leverage, where humans stay in control, what guardrails apply, and how you'll know if it's working — rather than a vague "use more AI".

## The Prompt

```
You are designing how a team wires AI agents into its development loop. Produce a concrete, staged rollout — not a mandate. Tool-neutral. Reference the team's AI coding guidelines for norms rather than restating them.

Produce:
1. Goal — what this improves and the friction it targets.
2. Stage-by-stage posture — for each SDLC stage (planning, code gen, review, tests, triage/on-call, docs/release notes), pick: human-only / AI-assisted (human drives) / AI-led (agent does, human reviews). Higher risk + lower reversibility → more human control.
3. Never unattended — the hard gates: merge to main, deploy to prod, secrets, irreversible changes.
4. Guardrails — review bar, verification (tests run/pass), data handling.
5. Rollout — start with a low-risk, high-toil stage; prove value; then expand. Name the first slice and the expansion path.
6. Success metrics + kill switch — what improvement you expect, and the quality signal (rising defects, rubber-stamped reviews, eroded understanding) that means stop.
7. Human-cost guardrails — skill erosion, review fatigue, over-trust.

Current workflow & friction: [HOW_WORK_FLOWS_TODAY_AND_WHERE_IT_HURTS]
Goal: [WHAT_YOU_WANT_MORE_OF]
Team & risk posture: [SIZE_SENIORITY_DATA_SENSITIVITY]
Constraints: [WHAT_MUST_STAY_HUMAN_CONTROLLED]
```

## Example Input

```
Current workflow & friction: Planning → code → PR review → CI → deploy. Review latency is the bottleneck; PRs sit 1-2 days.
Goal: Cut review latency without dropping quality.
Team & risk posture: 30 engineers, mixed seniority, standard SaaS (some PII).
Constraints: No auto-merge, no auto-deploy to prod.
```

## Example Output

> **AI Agent Workflow — Platform Eng**
>
> **Goal:** Cut PR review latency (currently 1-2 days) without dropping quality.
>
> **Stage-by-stage posture**
> | Stage | Posture | Human gate | Notes |
> |-------|---------|-----------|-------|
> | Planning/breakdown | AI-assisted | Lead approves | Agent drafts ticket breakdowns |
> | Code generation | AI-assisted | Author owns | Per coding guidelines |
> | Code review | AI-assisted | Human approves | Agent does first-pass review; human makes the merge call |
> | Tests | AI-led | Author reviews | Agent scaffolds tests; author verifies they're meaningful |
> | Triage / on-call | AI-assisted | Human decides action | Agent summarises + suggests; human acts |
> | Docs / release notes | AI-led | Skim before publish | Low risk |
>
> **Never unattended:** Merge to main, deploy to prod, touching secrets or customer data.
>
> **Guardrails:** First-pass AI review never approves alone; tests must run and pass; no customer data in prompts. See AI coding guidelines.
>
> **Rollout**
> 1. First slice: AI first-pass PR review + test scaffolding — high-toil, low-risk. Prove: review latency down, defect rate flat.
> 2. Then: expand to triage assistance once review is trusted.
>
> **Success metrics:** PR review latency, escaped-defect rate (must stay flat), reviewer hours saved.
> **Watch for / kill switch:** If escaped defects rise or human reviews become rubber-stamps, pause AI review and re-tighten the human gate.
>
> **Human-cost guardrails:** Rotate who does the final human review so judgment doesn't atrophy; make clear the AI pass is an aid, not the decision.

## Tuning Notes

- **Target real friction:** Automate the painful, high-toil stage — not the one that's easiest to automate. Anchor the design on where time is actually lost.
- **Reversibility drives control:** The less reversible the action, the harder the human gate. Never design AI-led for prod deploys or data changes.
- **Common pitfall:** Skipping metrics and a kill switch. A workflow you can't measure or stop is a liability — insist on both.
- **Human cost is real:** Skill erosion and review rubber-stamping are the quiet failure modes. Design against them explicitly, especially with juniors.
