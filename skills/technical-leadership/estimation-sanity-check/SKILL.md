---
name: estimation-sanity-check
description: >
  Pressure-tests an engineer's or team's estimate against the actual code and scope before a
  leader commits it upward — surfacing the hidden work, unstated assumptions, and risk the
  original number glosses over, and returning a revised range with a confidence level. Use when
  the user says "does this estimate look right", "sanity-check this timeline", "they said two
  weeks — is that real", or must commit a delivery date they didn't produce themselves. Use this
  to stress-test one estimate against reality — use capacity-planning for whole-team bandwidth
  math and sprint-planning-breakdown to slice an epic into estimated tickets.
---

# Estimation Sanity Check

Stress-test an estimate against the real code and scope before you put your name on it upward. The job is not to re-estimate from scratch but to find what the number misses — hidden work, optimistic assumptions, untested integration — and return an honest range with a confidence level, so the commitment is defensible.

## Inputs to gather

Gather these before checking. If any are missing, ask for them in a single batched question — never invent the scope, the team's velocity, or the codebase's state. Mark anything genuinely unavailable as **Unknown**.

- **The estimate** — the number/timeline given, and by whom, and at what granularity (gut feel vs decomposed)
- **The work** — what's being built, and the code/system it touches (agent can inspect if available)
- **Assumptions** — what the estimate assumed (happy path only? tests included? migration? review/QA time?)
- **Track record** — how this team's past estimates have landed, if known (chronic optimism is data)
- **The commitment** — what you're being asked to promise and to whom, so the confidence bar matches the stakes

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Restate the **estimate and its scope** as given, so the check is against a fixed baseline, not a moving one.
2. Inspect the **actual work**: the code paths, integrations, and data involved. Estimates go wrong on what they don't see — untouched-looking code with hidden coupling, an integration that isn't as clean as assumed, missing tests that must be written first.
3. Surface the **hidden work** the estimate likely omits: tests, migrations, edge cases, error handling, review/rework cycles, deployment/rollout, docs, and coordination with other teams. List each and whether it's plausibly in the number or not.
4. Challenge the **assumptions**: is this a happy-path estimate? does it assume the estimator does it (vs a junior)? does it assume no interruptions, no on-call, no context-switching? Name the ones that won't hold.
5. Weigh **track record and uncertainty**: if the team chronically underestimates, say so and widen the range. Distinguish work that's well-understood (tight range) from work that's exploratory (wide range or a spike first).
6. Return a **revised range**, not a false-precision single number — best case / likely / worst case — with the drivers of the spread. Attach a **confidence level** (high/medium/low) and what would raise it.
7. If confidence is low, recommend **de-risking before committing** — a spike, a decomposition, or a smaller first slice — rather than committing a number nobody believes.
8. Keep the tone collaborative, not gotcha — the goal is a commitment that holds, and the estimator is usually closer to the work than you are. Assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Estimate Sanity Check: [work]**

**Original:** [number/timeline, by whom, scope assumed]

**Hidden / likely-omitted work**
- [Item] — [in the number? / not accounted for]

**Assumptions that may not hold**
- [Assumption] — [why it's risky]

**Revised range**
- Best: [..] · Likely: [..] · Worst: [..]
- Spread driven by: [the biggest sources of uncertainty]

**Confidence: [High / Medium / Low]** — [what would raise it]

**Recommendation:** [Commit / commit with buffer / de-risk first ([spike or slice])]
```

## Boundaries

What the skill must never do.

- Never replace the estimator's number with a confident single figure — return a range and name the uncertainty.
- Never invent scope, velocity, or track record — mark **Unknown** and note it widens the range.
- Never ignore the unglamorous work (tests, review, rollout, coordination) — that's where estimates overrun.
- Never inflate confidence to make a deadline look achievable — a number nobody believes helps no one.
- Never turn the check into a blame exercise — it stress-tests the estimate, not the estimator.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **sprint-planning-breakdown** to decompose the work into tickets when the estimate needs a firmer basis.
- After this, offer **prototype-spike-plan** when confidence is low and a spike should de-risk the biggest unknown before committing.
