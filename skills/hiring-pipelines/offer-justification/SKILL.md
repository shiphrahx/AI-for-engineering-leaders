---
name: offer-justification
description: >
  Produces an offer justification for HR or a compensation committee — candidate summary,
  debrief outcome, level justification mapped to level expectations, a comp proposal (base,
  equity, bonus, sign-on) positioned against the band, market context, and the risk of losing
  the candidate. Use when the user says "justify this offer", "write the comp justification",
  "make the case for this level/package", or gives a candidate, proposed level, comp, and
  market data. Use this to justify level and PACKAGE internally — not to write the candidate-facing
  evaluation (candidate-evaluation-summary), nor to pitch the candidate to accept.
---

# Offer Justification

Connect a candidate's interview performance and experience to a specific level and compensation package, anchored on the band and market data — written for an HR partner or compensation committee.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent comp bands, market data, or debrief outcomes. Mark anything genuinely unavailable as **Unknown** in the output.

- **Candidate and role** — name, role, team
- **Proposed level** — and the level band (comp range) if available
- **Interview outcome** — debrief result and key evidence
- **Comp proposal** — base, equity, bonus, sign-on as applicable
- **Market context** — competing offers or volunteered current comp, if any

## Steps

1. Write the **candidate summary**: who they are, the role, proposed level, relevant experience, and any competing offer in one paragraph.
2. Summarize the **interview performance**: the debrief outcome (rating split) and the headline strengths that justify proceeding.
3. Write the **level justification**: map specific interview evidence to the level's expectations (independence, mentoring, project scope) so the level isn't asserted, it's demonstrated.
4. Build the **comp proposal** as a table: component, proposed value, the band, and position in band (percentile). Then a rationale paragraph — if above midpoint or above band, state the specific reasons (rare skill, competitive pressure, strategic urgency).
5. Write **market context**: position the package against competing offers and total comp (including equity upside). Flag any competing-offer figure as unverified if it wasn't confirmed.
6. Write the **risk if we don't act**: concrete consequences of losing the candidate (project at risk, pipeline depth, weeks to find a comparable hire).
7. Adapt to context: for **above-band comp**, justify explicitly — above-band without justification erodes comp integrity; for a **competing offer you can't match**, don't try — compete on opportunity (equity, scope, growth); with **no competing offer**, still pay fairly for the level — don't anchor to the band's bottom; for **counter-offer risk**, recommend a short decision window.
8. Assemble the output in the format below.
9. Run the calculator with the gathered inputs:
   ```
   python scripts/calculate.py --base <value> --band-min <value> --band-max <value> --bonus <value> --equity <value> --start-date <YYYY-MM-DD>
   ```
   Use the printed figures verbatim — do not recalculate manually. If FLAGS are printed, surface them explicitly to the user before proceeding.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Offer Justification: [Name] — [Role] ([Level])**

**Summary**
[Who they are, role, proposed level, relevant experience, competing offer if any.]

**Interview Performance**
[Debrief outcome (rating split) and headline strengths.]

**Level: [Level]**
[Specific interview evidence mapped to level expectations.]

**Compensation Proposal**
| Component | Proposed | Band ([Level]) | Position in Band |
|-----------|---------|----------------|------------------|
| Base salary | [amount] | [range or Unknown] | [percentile] |
| Equity | [grant] | [grid] | [position] |
| Sign-on bonus | [amount] | [discretionary] | [purpose] |

**Rationale:** [Why this position in band; explicit reasons if above midpoint/band.]

**Market Context**
[Package vs. competing offers and total comp; flag unverified figures.]

**Risk**
[Concrete consequences of losing the candidate.]
```

## Boundaries

- Anchor the offer on the **level band and market data, never on the candidate's current salary** — anchoring on current pay is legally restricted in many US jurisdictions (CA, NYC, CO, WA, MA, and others) and perpetuates pay gaps elsewhere. Use volunteered current comp only as context, never as the basis.
- Never fabricate comp bands, percentiles, market data, or debrief outcomes — mark unknowns as **Unknown**.
- Never present an above-band offer without explicit justification.
- Never report an unverified competing offer as confirmed — label it as the candidate's claim.

## Chaining

- The natural next step is the candidate-facing closing pitch, which lives as a prompt (`09-candidate-closing-pitch`), not a skill — so this is usually a terminal artifact. No natural successor skill in this pack.
