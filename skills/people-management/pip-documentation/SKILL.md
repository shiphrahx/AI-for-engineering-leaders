---
name: pip-documentation
description: >
  Produces a fair, evidence-based Performance Improvement Plan draft — purpose, dated
  performance gaps, expected standards, measurable improvement goals with deadlines, support
  provided, check-in schedule, and timeline/outcomes. Use when the user says "draft a PIP",
  "performance improvement plan for [name]", or describes documented underperformance after
  coaching has failed. Use this only when prior coaching is documented; use
  difficult-conversation-prep to plan delivery, performance-review-draft for routine reviews,
  and layoff-communication for non-performance separations. Always involve HR before finalising.
---

# PIP Documentation

Draft a serious, fair document that gives an underperforming engineer a genuine chance to succeed while protecting the organisation — specific, evidence-based, and supportive in tone: "here's exactly what success looks like and how we'll help you get there."

## Inputs to gather

Gather these before drafting. If any are missing, ask in a single batched question — never invent a gap, a date, an incident, or a coaching conversation. Mark anything genuinely unavailable as **Unknown**.

- **Employee** — name, role, level, tenure
- **Performance gaps** — specific areas missing expectations, with dated examples
- **Previous coaching** — what feedback was given, when, and what was tried (pairing, reduced scope)
- **Support available** — mentoring, training budget, reduced scope, check-ins you can offer
- **HR contact** — the partner who must review the plan

## Steps

1. Confirm prerequisites: the PIP must never be the first time the person hears these concerns. If there aren't 2-3 documented coaching conversations, say so and recommend coaching first rather than drafting.
2. Write the **Purpose** — why the PIP is being initiated, referencing the prior coaching and support already tried.
3. Document **Performance Gaps** — for each, state the level expectation, then the current performance with dated, specific examples (not impressions). Show a pattern, not isolated incidents.
4. Define **Expected Standards** — what "meeting expectations" looks like for each gap.
5. Set **Improvement Goals** — measurable targets with specific deadlines, in a table. Goals must be achievable, not designed to fail.
6. List **Support Provided** — concrete help: mentor pairing, reduced scope, prioritised review, training budget, manager check-ins.
7. Define a **Check-in Schedule** — weekly manager reviews, HR touchpoints, a mid-point review, and a final review.
8. State **Timeline and Outcomes** — duration and the three possible outcomes (successful completion, partial improvement/extension, insufficient improvement and next steps with HR).
9. Adapt to context: if the user is writing this just to paper-trail a predetermined termination, name that honestly — a real PIP gives a fair shot. Recommend delivering the plan in person or video (never email), leading with care. Remind the user that employment law varies by jurisdiction and HR must review before delivery.
10. Assemble the output in the format below.
11. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Performance Improvement Plan**

**Employee:** [Name] — [Role] ([Level])
**Manager:** [Name]
**Date:** [Date]
**PIP Duration:** [N weeks] ([start] – [end])
**HR Contact:** [HR partner name or Unknown]

---

**Purpose**
[Why initiated, referencing prior coaching and support already tried]

**Performance Gaps**
*1. [Area]*
[Level] expectation: [standard]
Current performance: [dated, specific examples showing a pattern]

**Improvement Goals**
| Area | Goal | Measurement | Deadline |
|------|------|-------------|----------|
| [area] | [measurable goal] | [how measured] | [date/sprints] |

**Support Provided**
- **[Type]:** [Specifics]

**Check-in Schedule**
- [Cadence and milestones]

**Timeline and Outcomes**
[Duration and the three outcome paths]
```

## Boundaries

- **Always involve HR before finalising or delivering.** This produces a draft only. Employment law varies by jurisdiction; HR ensures compliance.
- Base every gap on documented, dated evidence — never impressions, personality, or hearsay. Do not proceed if prior coaching isn't documented.
- Never set goals designed to fail or use a PIP to justify a predetermined termination. A genuine plan is achievable.
- Never fabricate gaps, dates, incidents, metrics, or coaching conversations. Mark unknowns as **Unknown** and ask.
- Keep this document strictly confidential. Never store an unreviewed draft in a shared space; deliver the conversation in person or video, not email.
- Keep gaps job-related and free of bias; ensure the standard applied is the one applied to peers at the same level.

## Chaining

- Before delivery, offer **difficult-conversation-prep** to plan the (in-person) conversation with care.
- If the PIP closes successfully, regular **performance-review-draft** and **one-on-one-prep** resume. If it does not, next steps are an HR-led process, not a further skill in this pack.
