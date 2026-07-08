---
name: spike-readout
description: >
  Turns a finished spike or prototype into a short decision memo: the answer to the question the
  spike asked, the evidence behind it, a clear recommendation, and what's still open — so the
  learning converts into a decision instead of evaporating. Use when the user says "write up my
  spike", "the prototype's done, now what", "summarise what we learned", or has run an experiment
  and must report the result to decide. Use this to close out a spike with a decision — use
  prototype-spike-plan to set one up beforehand, and architecture-decision-record to record the
  decision it produces.
---

# Spike Readout

Convert a completed spike into a decision. A spike that isn't written up is wasted — the readout states plainly whether the question was answered, what the evidence says, what to do next, and what remains uncertain. It reports what happened, honestly, including "inconclusive" when that's the truth.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent a result the spike didn't produce or a confidence it doesn't warrant. Mark anything genuinely unavailable as **Unknown**.

- **The question** — what the spike set out to answer (ideally the one from the spike plan)
- **What was built & done** — what was actually tried, and against what conditions
- **Findings** — the observations, numbers, and surprises (measured, not assumed)
- **The decision waiting** — what call this readout feeds and by when
- **Time spent** — whether the spike ran to its timebox or was cut short (affects confidence)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Restate the **question** the spike asked in one sentence, so the reader judges the answer against what was actually being tested.
2. Give the **answer** up front: yes / no / inconclusive, in one or two sentences. Lead with it — the reader wants the conclusion, not the journey. "Inconclusive" is a valid, honest answer; don't manufacture certainty.
3. Summarise **what was done** briefly — enough to trust the answer, not a play-by-play.
4. Lay out the **evidence**: the observations and numbers that support the answer, marking anything not measured as **Unknown**. Distinguish what you saw from what you inferred.
5. Give a clear **recommendation** for the decision this feeds: proceed / don't / proceed-with-conditions / run-one-more-spike (and which). Tie it directly to the answer.
6. State **what's still open** — the risks and questions the spike did not resolve, so the decision-maker isn't falsely reassured by a short experiment.
7. Note the **disposal reality** if code was written: what gets thrown away and what (if anything) needs a proper build — a spike readout that quietly greenlights merging prototype code creates debt.
8. Keep it to a page. Assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Spike Readout: [name]**

**Question:** [What the spike asked.]
**Answer:** [Yes / No / Inconclusive — one or two sentences.]

**What we did**
- [Briefly, enough to trust the answer.]

**Evidence**
- [Observation / number — measured, or marked Unknown.]

**Recommendation:** [Proceed / Don't / Proceed with conditions / One more spike ([which]).]

**Still open**
- [Risk or question the spike did not resolve.]

**Disposal:** [What's thrown away; what needs a proper build, or "no code kept".]
```

## Boundaries

What the skill must never do.

- Never manufacture a definite answer when the spike was inconclusive — say so and recommend the next smallest step.
- Never report inferred results as measured — mark what wasn't measured **Unknown**.
- Never overstate confidence from a short or cut-short spike — note the time actually spent.
- Never let the readout quietly greenlight merging throwaway code as production.
- Never hide the open risks behind a clean recommendation.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **architecture-decision-record** to record the decision the readout produced with its context and trade-offs.
- After this, offer **prototype-spike-plan** when the answer was "one more spike" and the next experiment needs framing.
