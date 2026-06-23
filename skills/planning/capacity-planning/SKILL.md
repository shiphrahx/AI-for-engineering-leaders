---
name: capacity-planning
description: >
  Produces a realistic capacity plan: net engineer-weeks after overhead deductions, committed
  work mapped against it, the capacity gap or surplus stated plainly, trade-off options, and a
  commit/push-back recommendation. Use when the user says "can we take this on", "what's our
  capacity", "what do we have to drop to add X", or pastes team size, a period, absences, and
  committed work. Use this for the bandwidth math behind a quarter or cycle — use
  quarterly-roadmap for the full plan and sprint-planning-breakdown to slice an epic into tickets.
---

# Capacity Planning

Map team bandwidth against committed work for an upcoming quarter or cycle using realistic availability — not idealistic "every engineer codes 40hrs/week" math — to answer "can we take this on?" and "what do we drop to add it?"

## Inputs to gather

Gather these before calculating. If any are missing, ask for them in a single batched question — never invent absences, effort estimates, or velocity. Mark anything genuinely unavailable as **Unknown**.

- **Team** — name and size (with seniority mix if individual-level planning is needed)
- **Period** — the time window and number of weeks
- **Planned absences** — PTO, holidays, company shutdowns, parental leave, on-call rotations
- **Committed work** — already-agreed deliverables with effort estimates
- **Requested additions** — new work being considered

## Steps

1. Calculate **available capacity** transparently, line by line: gross capacity (engineers × weeks), then deduct shutdowns, individual absences, on-call overhead, and a meetings/review/support overhead factor. Show the math; land on net available engineer-weeks.
2. Use a realistic overhead factor: ~20% for an established team; 30–40% for a new or volatile team (more process, learning, coordination). On-call ≈ 0.5 week per engineer per rotation; a full on-call week is roughly 50% reduced capacity. New hires ramp ~25% productive in month 1, ~50% month 2, ~75% month 3.
3. List **committed work** with estimates and a confidence level each. Subtract from net capacity to show remaining.
4. Test **requested additions** against remaining capacity, marking each as fitting or not, and state the **capacity gap or surplus** plainly.
5. If overcommitted, lay out **trade-off options** — what could be cut, deferred, or descoped — and lead with the gap number to force the conversation.
6. Write a **recommendation** — what to commit to, what to push back on, suggested sequencing (smaller/higher-confidence work first), and the caveats (e.g. "if X overruns by 3 weeks, Y slips"). Leave an explicit buffer (10–20%) for unplanned work rather than allocating to 100%.
7. Adapt to context: for individual-level planning, break capacity down per engineer when work needs specific expertise ("only two engineers can do the API integration" changes the math). For stakeholder presentation, keep the math visible — accounting for holidays, overhead, and on-call earns more trust than pretending at 100% utilisation.
8. Assemble the output in the format below.
9. Run the calculator with the gathered inputs:
   ```
   python scripts/calculate.py --engineers <value> --sprint-days <value> --leave-days <value> --ceremony-hours <value> --velocity <value>
   ```
   Use the printed figures verbatim — do not recalculate manually. If FLAGS are printed, surface them explicitly to the user before proceeding.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Team] — [Period] Capacity Plan**

**Available Capacity**
| Factor | Calculation | Engineer-Weeks |
|--------|-------------|----------------|
| Gross capacity | [engineers × weeks] | [N] |
| [absence/shutdown] | [calc] | -[N] |
| On-call overhead | [calc] | -[N] |
| Meetings/review/support overhead | ~[X]% of remaining | -[N] |
| **Net available capacity** | | **[N]** |

**Committed Work**
| Item | Estimate | Confidence |
|------|----------|------------|
| [item] | [N weeks] | [high/medium/low] |
| **Total committed** | **[N weeks]** | |

**Remaining Capacity:** [net] − [committed] = **[N] engineer-weeks**

**New Requests**
| Request | Estimate | Fits? |
|---------|----------|-------|
| [request] | [N weeks] | [✅ Yes ([remaining] left) / ❌ No (gap of [N])] |

**Recommendation**
[What to commit to, what to push back on, sequencing, and caveats. Buffer remaining: [N] (~[X]% of net).]
```

## Boundaries

- Never invent absences, effort estimates, or historical velocity — mark them **Unknown** and use a stated default overhead (25%) only when flagged as an assumption.
- Never plan to 100% utilisation — always reserve explicit buffer for unplanned work.
- Never hide an overcommitment — when work exceeds capacity, state the gap first and force the trade-off conversation.
- Effort estimates come from the user; individual velocity varies — say so rather than implying the math is exact.

## Chaining

- After this, offer **sprint-planning-breakdown** to slice the committed epics into well-scoped, estimated tickets that fit the planned capacity.
