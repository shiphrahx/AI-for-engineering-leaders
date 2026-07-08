---
name: codebase-health-check
description: >
  Runs a periodic health pass on a codebase a leader owns — test coverage and reliability, change
  hotspots, complexity, dependency and security freshness, and build/CI health — and returns a
  scored, evidence-cited snapshot with the few fixes that would most improve it. Use when the user
  says "how healthy is our codebase", "do a health check on this repo", "where's the risk in our
  code", or wants a recurring read on a system their team maintains. Use this to assess the ongoing
  health of code your team owns — use codebase-orientation-brief to get oriented in code you don't
  know, and tech-debt-prioritisation to turn the findings into a ranked, costed backlog.
variants: [startup, growth, enterprise]
---

# Codebase Health Check

Give a leader an honest, evidence-based read on the health of a system their team owns — where the risk is, what's degrading, and the few changes that would help most — so investment goes where it pays off. It measures and cites; it never scores on vibes, and it distinguishes what it observed from what it couldn't.

## Inputs to gather

Gather these before assessing. If any are missing, ask for them in a single batched question — never invent coverage numbers, incident rates, or dependency status. Mark anything genuinely unavailable as **Unknown**.

- **The codebase** — repo/service path the agent can inspect (and git history if available)
- **Purpose of the check** — routine cadence, pre-planning input, a specific worry, or a new owner taking stock
- **What "healthy" means here** — the bar this system is held to (prototype vs critical production) so scoring is fair
- **Known pain** — incidents, slow areas, or complaints the team already feels
- **Access** — whether coverage reports, CI status, and dependency tooling output are available or must be marked Unknown

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Scope the check to the system and its bar. A prototype and a payments service are not held to the same standard — say which this is.
2. Assess each **dimension**, citing evidence (paths, numbers, git signals). Mark any you can't measure as **Unknown** rather than guessing:
   - **Tests & reliability** — coverage where measurable, presence of tests on critical paths, flakiness, recent incident/bug rate.
   - **Change hotspots** — files/modules that change most and break most (git churn × recency); these are where risk concentrates.
   - **Complexity & structure** — oversized modules, deep coupling, duplicated logic, missing boundaries.
   - **Dependencies & security** — outdated/abandoned deps, known-vuln surface, single-maintainer risk, license concerns.
   - **Build & CI** — build time, CI reliability, and whether the pipeline actually gates quality.
   - **Docs & onboarding** — can a new engineer get productive; is critical knowledge in one head.
3. Give each dimension a simple **rating** (🟢 healthy / 🟡 watch / 🔴 at risk) with the one-line evidence behind it — no rating without a reason.
4. Identify the **highest-leverage fixes**: the two or three changes that would most reduce risk or pain, not an exhaustive cleanup list. Tie each to the dimension it improves.
5. Separate **now vs later**: what's actively risky (address soon) from what's cosmetic or deferrable — don't let a red dimension and a nitpick sit at the same priority.
6. Note the **trend** if prior checks or git history show it: improving, stable, or degrading. A degrading trend on a critical system matters more than a mediocre-but-stable snapshot.
7. Adapt to context (see Variants) and assemble the output in the format below. Cite evidence so the leader can verify, not trust blindly.

## Output format

```
**Codebase Health: [system]** — Bar: [prototype / standard / critical] — [date]

**Overall: 🟢/🟡/🔴** — [one-line summary + trend if known]

**By dimension**
| Dimension | Rating | Evidence |
|-----------|--------|----------|
| Tests & reliability | 🟢/🟡/🔴 | [coverage / incident rate / path] |
| Change hotspots | .. | [churny/breaky files] |
| Complexity & structure | .. | [..] |
| Dependencies & security | .. | [..] |
| Build & CI | .. | [..] |
| Docs & onboarding | .. | [..] |

**Highest-leverage fixes**
1. [Fix] → improves [dimension]. [Rough cost.]
2. [..]

**Now vs later**
- Now (actively risky): [..]
- Later (deferrable): [..]

**Could not measure:** [explicit Unknowns]
```

## Variants

Optional org-size tuning (see [`docs/VARIANTS.md`](../../../docs/VARIANTS.md)). Default to **growth** if the user doesn't state a stage.

- **startup** (≤ ~15 engineers): focus on tests-on-critical-paths, hotspots, and security; skip heavier structure analysis; keep it to overall rating + top fixes.
- **growth** (~15–80): the full dimension table above.
- **enterprise** (80+): add cross-team ownership gaps, compliance/security posture, and roll multiple services into a portfolio view with comparable ratings.

## Boundaries

What the skill must never do.

- Never rate a dimension without citing the evidence behind it — no scores on vibes.
- Never fabricate coverage, incident rates, or dependency status — mark **Unknown** and note it limits the check.
- Never produce an exhaustive cleanup list — surface the few highest-leverage fixes.
- Never hold a prototype and a critical service to the same bar — state the bar and score against it.
- Never equate ugly-but-stable with unhealthy — risk is about cost and change, not aesthetics.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **tech-debt-prioritisation** to turn the findings into a ranked, costed backlog.
- After this, offer **legacy-code-assessment** when a 🔴 area needs an invest/rewrite/leave decision of its own.
