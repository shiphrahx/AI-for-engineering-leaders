---
name: code-to-exec-translation
description: >
  Turns a concrete code change — a diff, PR, merged feature, or migration — into the business
  framing a non-technical audience acts on: what changed in plain terms, why it matters
  (customer, revenue, risk, cost), and what (if anything) is needed from them. Bridges the
  hands-on leader's code reality and the stakeholder/exec narrative. Use when the user says
  "explain this PR to my VP", "what do I tell stakeholders about this change", "translate this
  diff for non-engineers", or pastes a technical change they must communicate upward. Use this to
  translate a specific change upward — use exec-summarizer to compress any dense document, and
  exec-status-update for a recurring weekly team status.
---

# Code to Exec Translation

Translate a specific technical change into the language a busy executive or stakeholder acts on — impact, risk, and timeline — without the diff, the jargon, or the false precision. The translation stays honest to what the code actually does; it reframes, it never inflates.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent business impact, metrics, or a customer benefit the change doesn't deliver. Mark anything genuinely unavailable as **Unknown**.

- **The change** — the diff, PR, or description of what shipped or is shipping (enough to state accurately what it does)
- **Audience** — who reads this (manager, VP, CTO, board, PM, sales, customer) and what they act on
- **Why it was done** — the problem it solves or the goal it serves, so the "so what" is real not invented
- **Impact evidence** — any numbers the user can stand behind (latency, cost, error rate, revenue at stake) — surfaced, never fabricated
- **Sensitivity** — whether this touches an incident, a risk, or bad news that must be framed honestly

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Understand what the change actually does at the code level before translating — don't summarise a description you can't verify against the change.
2. Lead with the **so-what**: one sentence in the audience's terms (faster checkout, lower cost, reduced risk, unblocked launch), not the mechanism. Put the conclusion first.
3. Say **what changed** in plain language — translate the mechanism only as far as the reader needs to trust the claim ("moved image processing off the main path" not "async offload via worker queue").
4. State **why it matters** to this audience: tie it to a customer outcome, a number, a risk retired, or a cost — whichever is true. If the benefit is indirect (paying down risk, enabling future work), say that plainly rather than overselling a user-visible win.
5. Be honest about **status and risk**: shipped vs in progress, what could still go wrong, and what's being watched. Never imply done when it's behind a flag or unverified.
6. State **what's needed** from the reader — a decision, awareness, or nothing — and say "nothing, FYI" explicitly when true.
7. Strip jargon the reader can't act on; keep a technical term only if the decision depends on it and then gloss it once.
8. Assemble the output in the format below, kept tight.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Change] — for [audience]**

**So what:** [One sentence in the reader's terms — the outcome, not the mechanism.]

**What changed:** [Plain language, mechanism only as far as needed to trust the claim.]

**Why it matters:** [Customer / revenue / risk / cost tie-in — honest about indirect benefits.]

**Status & risk:** [Shipped / in progress / behind flag; what's being watched.]

**Needed from you:** [Decision or awareness, or "Nothing — FYI".]
```

## Boundaries

What the skill must never do.

- Never claim a business impact, metric, or customer benefit the change doesn't actually deliver — mark unknowns **Unknown**.
- Never imply "done" when the change is behind a flag, unverified, or partially rolled out.
- Never bury risk or bad news beneath the win — state status honestly.
- Never oversell a risk-paydown or enabling change as a user-visible feature — name it for what it is.
- Never keep jargon the reader can't act on — translate or cut it.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **exec-status-update** when several such translations roll into a recurring weekly leadership update.
- After this, offer **exec-summarizer** when the source is a long document rather than a single code change.
