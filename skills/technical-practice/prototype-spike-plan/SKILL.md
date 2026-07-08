---
name: prototype-spike-plan
description: >
  Turns a fuzzy technical question into a disciplined throwaway-prototype plan — the single
  question the spike must answer, the smallest thing to build to answer it, a hard timebox, and
  explicit kill/success criteria so the spike ends in a decision instead of quietly becoming
  production. Use when the user says "let me spike this", "build a quick prototype to test X",
  "de-risk this before we commit", or is a hands-on leader about to code an experiment to inform
  a call. Use this to plan a time-boxed experiment — use build-vs-buy-analysis for the full
  vendor decision and rfc-outline once the answer justifies a real proposal.
variants: [startup, growth, enterprise]
---

# Prototype Spike Plan

Plan a throwaway prototype that answers one question and then dies — not a stealth start on the real system. A good spike is framed by a single question, the smallest build that answers it, a hard timebox, and criteria that force a decision at the end. The output is learning and a recommendation, not code to keep.

## Inputs to gather

Gather these before planning. If any are missing, ask for them in a single batched question — never invent the decision at stake, the timebox, or the team's constraints. Mark anything genuinely unavailable as **Unknown**.

- **The question** — the decision or uncertainty the spike exists to resolve (feasibility, performance, integration, developer-experience)
- **Decision it feeds** — what call this unblocks and by when (build-vs-buy, architecture, estimate)
- **Constraints** — how much time you can spend, who's doing it, and any hard limits (stack, data access, security)
- **What "answered" looks like** — the evidence that would settle the question either way
- **Disposal reality** — whether this genuinely gets thrown away or there's pressure to keep it (name it, it changes the plan)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Sharpen the **single question** to one sentence, answerable yes/no or with a number. If there are several questions, pick the one that most blocks the decision and note the rest as out of scope — a spike answers one thing.
2. Define the **smallest build** that produces that evidence: hardcode, stub, and fake everything not under test. Explicitly list what to skip (auth, error handling, persistence, UI polish) so the spike stays small.
3. Set a **hard timebox** (hours or a few days, not weeks) and name what happens when it's hit: decide with what you have, don't extend by default.
4. Write **success and kill criteria** up front: what result means "yes, proceed", what means "no", and what means "inconclusive — here's the next smallest spike". Deciding these before building prevents motivated interpretation after.
5. State the **disposal plan**: the code is reference, not foundation. If any part might survive, name that part now and flag that it needs a proper rebuild — a spike merged as-is is how prototypes become tech debt.
6. Note **what the spike will NOT tell you** — the risks it leaves open (scale, edge cases, long-term maintenance) so the decision-maker isn't falsely reassured.
7. Adapt to context (see Variants). Match rigor to the stakes: a reversible internal call needs less ceremony than a one-way-door platform bet.
8. Assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Spike: [name]** — Timebox: [N hours/days]

**Question:** [The one thing this spike answers, in a sentence.]

**Decision it unblocks:** [What call this feeds, by when.]

**Build (smallest thing)**
- [What to build]
- Skip / fake: [auth, persistence, UI, error handling, …]

**Success / kill criteria**
- ✅ Proceed if: [result]
- ❌ Stop if: [result]
- 🤔 Inconclusive → [next smallest spike]

**Disposal:** [Thrown away. Any part that might survive → needs proper rebuild: [part].]

**Will NOT tell us:** [Risks left open — scale, edge cases, maintenance.]
```

## Variants

Optional org-size tuning (see [`docs/VARIANTS.md`](../../../docs/VARIANTS.md)). Default to **growth** if the user doesn't state a stage.

- **startup** (≤ ~15 engineers): keep it to Question, Build, and a tight timebox; move fast and accept a rougher disposal story, but still write the kill criterion.
- **growth** (~15–80): the full plan above — explicit success/kill criteria and disposal plan.
- **enterprise** (80+): add who signs off on the decision the spike feeds, security/data constraints on the throwaway environment, and an explicit note that spike code must not enter a production repo without a rebuild.

## Boundaries

What the skill must never do.

- Never let a spike lack a hard timebox or kill criteria — without them it becomes an open-ended project.
- Never plan a spike to answer more than one primary question — split it.
- Never imply the throwaway code is production-ready — name what must be rebuilt.
- Never fabricate performance numbers or feasibility claims — the spike produces those; the plan only frames how.
- Never overstate what a spike proves — record the risks it leaves open.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **build-vs-buy-analysis** when the spike's answer feeds a buy-or-build decision.
- After this, offer **rfc-outline** when the answer justifies a real proposal that needs cross-team buy-in.
