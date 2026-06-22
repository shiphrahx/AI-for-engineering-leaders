---
name: engineering-newsletter
description: >
  Produces a readable, jargon-free internal engineering newsletter for a company-wide non-technical
  audience — what we shipped (in plain user/business terms), what we're building next (as outcomes),
  a "behind the scenes" paragraph making one technical thing accessible, and a team spotlight.
  Conversational tone, no corporate filler. Use when the user says "write the engineering
  newsletter", "monthly/bi-weekly eng update for the company", or pastes raw engineering updates to
  make company-readable. Use this for the broad company-wide newsletter — use team-weekly-summary
  for the team-internal Friday wrap-up and exec-status-update for leadership-up status.
---

# Engineering Newsletter

Turn raw engineering updates into a newsletter the whole company — product, design, sales, ops — can read and enjoy, sharing what engineering built and why it matters, with no technical knowledge required to follow along.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent shipped work, metrics, or names. Mark anything genuinely unavailable as **Unknown** in the output.

- **Audience** — who reads it and roughly how many (e.g. whole company, ~200, mostly non-technical)
- **Cadence** — monthly / bi-weekly
- **Period covered** — the date range
- **Raw engineering updates** — what shipped, what's in progress, metrics, notable wins

## Steps

1. Read the raw updates fully. For each, ask "what can a user or the business now do?" and lead with that, not the implementation.
2. **What we shipped** (3-5 bullets) — plain language, focused on the user/business outcome. Bold a short headline per item.
3. **What we're building next** (2-3 items) — framed as outcomes ("making payments more reliable"), not tasks ("refactoring the payment service").
4. **Behind the scenes** — one short paragraph making a single technical thing accessible: a pattern, a lesson, or a tradeoff navigated. Explain the *why it's hard* in human terms.
5. **Team spotlight** — 1-2 sentences recognizing a specific person or team for a specific accomplishment.
6. Keep the tone conversational, curious, not dry. Avoid corporate filler — no "leveraged", "utilised", "synergies".
7. Adapt to context: for a **technical audience**, add a "How we did it" section with implementation detail. For a **short version**, cut to shipped items + spotlight only (works as a Slack post). For a **quarterly edition**, replace "What we shipped" with a themes-based summary (reliability, velocity, new capabilities) and add start-vs-end-of-quarter metrics.
8. Assemble the output in the format below.

## Output format

```
**Engineering Update — [Period]**

**What we shipped**
- **[Plain-language headline]** — [what users/the business can now do]
- [...]

**What we're building next**
- [Outcome-framed item]
- [...]

**Behind the scenes**
[One short, accessible paragraph: a pattern, lesson, or tradeoff — explained for a non-technical reader.]

**Team spotlight**
[1-2 sentences recognizing a specific person/team for a specific accomplishment.]
```

## Boundaries

- Never fabricate shipped work, metrics, or names — mark anything unavailable as **Unknown**.
- Never use jargon or corporate filler — if a non-technical reader can't follow it, rewrite or cut it.
- Never overclaim impact ("revolutionary", "game-changing") — let the plain outcome speak.
- Never give a spotlight to someone for something they didn't do — credit must be accurate.

## Chaining

- No natural successor — this is usually a terminal artifact. Its raw material often overlaps with the inputs to **team-weekly-summary** or **exec-status-update**.
