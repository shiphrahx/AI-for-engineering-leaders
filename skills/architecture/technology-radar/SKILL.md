---
name: technology-radar
description: >
  Produces an opinionated technology radar — technologies sorted into Adopt / Trial / Assess / Hold
  rings, each with a rationale (and a migration path for Hold), plus a recently-changed section and
  review cadence. Use when the user says "build a tech radar", "what should we standardise on",
  "adopt/trial/assess/hold", "we have four web frameworks in prod", or asks for guidance on what
  technology to use or stop using. Use this for the catalogue of tooling decisions; use
  technical-vision-document for the multi-year direction the radar serves, and database-selection-guide
  for a single deep datastore choice.
---

# Technology Radar

Build an opinionated decision-making tool that sorts technologies into Adopt / Trial / Assess / Hold with a rationale for every placement — not a catalogue, a set of recommendations the team can act on.

## Inputs to gather

Gather these before building. If any are missing, ask in a single batched question — never invent the current stack, team skills, or pain points. Mark anything genuinely unavailable as **Unknown** in the output.

- **Current stack** — languages, frameworks, infra, tooling in use
- **Team skills** — strengths and growing interests
- **Pain points** — what's causing friction or proliferation
- **Upcoming needs** — future requirements that may need new technology

## Steps

1. Confirm inputs. If the current stack or pain points aren't given, ask — the radar exists to resolve real confusion, not to inventory everything. Mark gaps **Unknown**.
2. Write the **Radar overview** — what it covers, who it's for, and how to use each ring: Adopt = use freely in production; Trial = use with tech-lead approval on non-critical work; Assess = research only, don't build yet; Hold = stop adopting, plan migration.
3. Fill **Adopt** — endorsed production technologies, each with a one-line rationale grounded in team expertise and fit.
4. Fill **Trial** — technologies being actively experimented with, scoped to where and with what evaluation criteria before broader rollout.
5. Fill **Assess** — technologies worth watching, with the question being evaluated and why the migration cost demands caution.
6. Fill **Hold** — technologies to stop adopting, each with a rationale AND a concrete migration path (rewrite target, boy-scout rule, upgrade-in-place, CI gating).
7. Add **Recently changed** — technologies that moved rings since the last radar, so the team sees the deltas.
8. Set the **Review cadence** — how often it's updated and how anyone proposes a change.
9. Adapt to context: for a first radar, don't cover everything — focus on the decisions actively causing debate ("Flask or FastAPI for this new service?"). To get buy-in, make placements collaborative with staff engineers and tech leads — an imposed radar gets ignored. Frame it as advisory: "Hold" means "strong recommendation against", not "prohibited", but repeated ignoring of Hold items is a coaching conversation. Offer the Thoughtworks concentric-ring visual for presentations while keeping the table for reference.
10. Assemble the output in the format below.

## Output format

```
**Engineering Technology Radar — [Quarter/Date]**

**How to use this radar:** [One line per ring]

**Adopt**
| Technology | Category | Rationale |
|-----------|----------|-----------|

**Trial**
| Technology | Category | Rationale |
|-----------|----------|-----------|

**Assess**
| Technology | Category | Rationale |
|-----------|----------|-----------|

**Hold**
| Technology | Category | Rationale | Migration Path |
|-----------|----------|-----------|----------------|

**Recently Changed**
- [Technology: ring → ring, why]

**Review:** [Cadence and how to propose changes]
```

## Boundaries

- Never fabricate the current stack, team skills, or pain points — mark them **Unknown**; placements must reflect this team, not generic best practice.
- Never place a technology without a rationale, and never put one on Hold without a concrete migration path.
- Never produce a neutral catalogue — the radar must take positions; a placement everyone already agrees on adds nothing.
- Frame the radar as advisory guidance, not policy — overstating it as a mandate undermines adoption.

## Chaining

- This commonly follows **technical-vision-document** (the radar operationalises its "boring technology" principle and "what we stop doing").
- For a single high-stakes datastore decision flagged Assess/Trial, offer **database-selection-guide**.
