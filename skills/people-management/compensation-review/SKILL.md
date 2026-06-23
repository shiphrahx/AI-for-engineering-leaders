---
name: compensation-review
description: >
  Produces a defensible compensation review for a direct report — the proposed increase, the
  new salary positioned against the band, the compa ratio, and any approval flags. Use when the
  user says "review [name]'s comp", "model this raise", "what does an X% increase look like", or
  pastes a current salary, a proposed increase, and the level band. Use this for the band-and-compa
  math behind a single person's raise — use promotion-case to argue a level change and
  offer-justification for a new-hire package.
---

# Compensation Review

Position a proposed pay increase against the level band and compa ratio so the recommendation is defensible — not a number picked in isolation. Surface band breaches and high compa ratios before they reach an approver.

## Inputs to gather

Gather these before calculating. If any are missing, ask in a single batched question — never invent salaries, increases, or band figures. Mark anything genuinely unavailable as **Unknown**.

- **Person** — name, current level
- **Current salary** — base, in the band's currency
- **Proposed increase** — as a fraction (e.g. 0.08 for 8%)
- **Level band** — minimum and maximum for the current level

## Steps

1. Confirm the band matches the person's **current level** — comparing against the wrong band invalidates the compa ratio.
2. Run the calculator (below) to get the new salary, band position, and compa ratio. Use the printed figures verbatim.
3. Write a one-paragraph **recommendation** — the increase, the new salary, where it sits in the band, and the rationale tied to performance or market, not tenure.
4. If the calculator prints FLAGS (above ceiling, below floor, compa > 1.15), surface each explicitly and state the approval or correction needed before the increase can proceed.
5. Run the calculator with the gathered inputs:
   ```
   python scripts/calculate.py --current <value> --increase <value> --band-min <value> --band-max <value>
   ```
   Use the printed figures verbatim — do not recalculate manually. If FLAGS are printed, surface them explicitly to the user before proceeding.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Compensation Review: [Name], [Level]**

| Figure | Value |
|--------|-------|
| Current salary | [amount] |
| Proposed increase | [%] |
| New salary | [amount] |
| Band | [min] – [max] |
| Compa ratio | [ratio] |

**Recommendation**
[The increase, new band position, and rationale tied to performance/market.]

**Flags**
[Any band breach or high compa ratio, with the approval needed — or "None".]
```

## Boundaries

- Never invent current salaries, increases, or band figures — mark unknowns as **Unknown** and ask.
- Never recommend an above-band increase without flagging it for approval — above-band without justification erodes comp integrity.
- Argue the increase from performance, scope, and market — never from tenure alone.
- This is a confidential people document — keep it private until shared through the proper channel.

## Chaining

- If the review surfaces a level change rather than a within-band raise, offer **promotion-case** to argue the move on evidence.
