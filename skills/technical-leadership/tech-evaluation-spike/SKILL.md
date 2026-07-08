---
name: tech-evaluation-spike
description: >
  Evaluates a specific library, framework, service, or vendor by actually exercising it — not
  reading its marketing — and produces a decision memo: what was tested, what held up, what broke,
  the deal-breakers, and a plain adopt / avoid / need-more recommendation. Use when the user says
  "should we use X", "evaluate this library/framework/vendor", "kick the tyres on Y", or is a
  hands-on leader about to trial a tool to inform a technical bet. Use this to judge an external
  technology by running it — use prototype-spike-plan to de-risk your own idea, and
  build-vs-buy-analysis for the full buy-versus-build business case.
variants: [startup, growth, enterprise]
---

# Tech Evaluation Spike

Evaluate a candidate technology by putting it under real load for a bounded time, then report what you actually observed — not what the docs promise. The output is an evidence-based adopt/avoid recommendation a team can act on, honest about what the spike did and did not test.

## Inputs to gather

Gather these before evaluating. If any are missing, ask for them in a single batched question — never invent benchmark numbers, limitations, or pricing. Mark anything genuinely unavailable as **Unknown**.

- **The candidate** — the library/framework/service/vendor and its main alternatives (if a comparison is wanted)
- **The job** — what you need it to do, and the one or two capabilities that actually matter for your use
- **Deal-breakers** — hard requirements (license, self-host, data residency, latency, budget, language/stack fit)
- **Test conditions** — the realistic scenario to exercise it against (data shape, load, integration point)
- **Timebox & environment** — how long you can spend and where you can run it (local, sandbox, trial account)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Restate the **decision and the must-haves** first. List the deal-breakers explicitly — a technology that fails one of these is out regardless of how good it is elsewhere.
2. Define the **test plan**: the specific things to try that map to your real use, not a generic hello-world. Include the capability that matters most and at least one edge that tends to break tools (scale, failure handling, integration seam).
3. **Exercise it for real** — install/wire it up and run the test plan against realistic conditions. Record what you did concretely enough that someone could repeat it. Reading the docs is not evaluating.
4. Capture **evidence**: what worked, what broke, observed numbers (latency, memory, error rates, setup time), and rough edges (DX, docs, error messages). Mark any figure you could not measure as **Unknown** rather than estimating.
5. Check the **deal-breakers** one by one against evidence — license, cost at your scale, data/security posture, maintenance health (last release, open issues, single-maintainer risk), lock-in and exit cost.
6. Compare against the **alternative(s)** or the status quo only on the dimensions that matter — avoid a feature-matrix that hides the two things that decide it.
7. Give a clear **verdict**: Adopt, Avoid, or Need-more (with the specific follow-up that would settle it). Lead with the verdict and its single strongest reason.
8. State **what the spike did NOT test** — the risks left open (production scale, long-term maintenance, team learning curve) so no one over-reads a short trial.
9. Adapt to context (see Variants) and assemble the output in the format below.
10. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Tech Evaluation: [candidate]** — Verdict: [Adopt / Avoid / Need more]

_[One-line strongest reason for the verdict.]_

**Decision & must-haves**
- Deciding: [what call this feeds]
- Deal-breakers: [hard requirements]

**What was tested**
- [Concrete thing tried, against what conditions]

**Evidence**
- ✅ Held up: [with numbers where measured]
- ❌ Broke / rough: [with detail]
- Deal-breaker check: [license / cost / security / maintenance / lock-in — pass or fail each]

**vs [alternative / status quo]**
- [Only the dimensions that decide it]

**Did NOT test:** [Risks left open.]

**Recommendation:** [Adopt/Avoid/Need-more + next step if Need-more.]
```

## Variants

Optional org-size tuning (see [`docs/VARIANTS.md`](../../../docs/VARIANTS.md)). Default to **growth** if the user doesn't state a stage.

- **startup** (≤ ~15 engineers): weight speed-to-value and DX; keep the memo to verdict, evidence, and deal-breakers; accept more lock-in risk for velocity but name it.
- **growth** (~15–80): the full memo above, with the alternative comparison and maintenance-health check.
- **enterprise** (80+): add security/compliance review, vendor viability and support terms, data-residency, and who must sign off before adoption.

## Boundaries

What the skill must never do.

- Never report docs or marketing claims as if observed — only state what the spike actually exercised; mark the rest **Unknown**.
- Never fabricate benchmark numbers, pricing, or limitations — measure or mark Unknown.
- Never bury a deal-breaker — a single hard-requirement failure decides it, say so up front.
- Never hide lock-in or exit cost — name what leaving would take.
- Never over-read a short trial — record what the spike did not cover.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **build-vs-buy-analysis** when the verdict feeds a formal buy-versus-build decision.
- After this, offer **architecture-decision-record** to capture the adopt/avoid decision with its context and trade-offs.
