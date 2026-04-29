# Capacity Planning

## Situation

You need to map team bandwidth against committed work for the upcoming quarter or cycle. This helps you answer: "Can we take this on?" and "What do we have to drop to add this?"

## The Prompt

```
You are an engineering leader building a capacity plan for an upcoming quarter or project cycle. Account for realistic availability (holidays, on-call, meetings, support, tech debt maintenance) — not idealistic "every engineer codes 40hrs/week" math.

Structure:
1. **Available capacity** — total engineer-weeks available, with deductions for overhead
2. **Committed work** — already-agreed deliverables with estimated effort
3. **Capacity gap or surplus** — the math, plainly stated
4. **Trade-off options** — if overcommitted, what could be cut, deferred, or descoped
5. **Recommendation** — what to commit to and what to push back on

Team: [TEAM_NAME], [TEAM_SIZE] engineers
Period: [TIME_PERIOD] ([NUM_WEEKS] weeks)
Planned absences: [ABSENCES]
Committed work: [PASTE_COMMITTED_WORK]
Requested additions: [PASTE_NEW_REQUESTS]
```

## Example Input

```
Team: Growth Engineering, 6 engineers
Period: Q2 (13 weeks)
Absences: Li is on holiday for 2 weeks in June. Kara is on-call every 6th week (shared rotation). Company shutdown week in July (1 week).
Committed work:
- Referral program v2 (estimated 8 engineer-weeks)
- Onboarding flow A/B test framework (estimated 5 engineer-weeks)
- Self-serve plan upgrade page (estimated 4 engineer-weeks)
- Ongoing experimentation support / bug fixes (~1 engineer-week per sprint = 6.5 total)

New requests:
- VP Sales wants a custom landing page builder for campaigns (estimated 10 engineer-weeks)
- Product wants to add a "free trial extension" feature (estimated 3 engineer-weeks)
```

## Example Output

> **Growth Engineering — Q2 Capacity Plan**
>
> **Available Capacity**
> | Factor | Calculation | Engineer-Weeks |
> |--------|-------------|----------------|
> | Gross capacity | 6 engineers × 13 weeks | 78.0 |
> | Company shutdown | 6 engineers × 1 week | -6.0 |
> | Li's holiday | 1 engineer × 2 weeks | -2.0 |
> | On-call overhead | ~0.5 week/engineer per on-call rotation, Kara has 2 rotations | -1.0 |
> | Meetings, code review, support overhead | ~20% of remaining time | -13.8 |
> | **Net available capacity** | | **55.2** |
>
> **Committed Work**
> | Item | Estimate | Confidence |
> |------|----------|------------|
> | Referral program v2 | 8 weeks | Medium (new vendor integration, some unknowns) |
> | Onboarding A/B test framework | 5 weeks | High |
> | Self-serve plan upgrade | 4 weeks | High |
> | Ongoing support / bug fixes | 6.5 weeks | High (historical average) |
> | **Total committed** | **23.5 weeks** | |
>
> **Remaining Capacity:** 55.2 - 23.5 = **31.7 engineer-weeks**
>
> **New Requests**
> | Request | Estimate | Fits? |
> |---------|----------|-------|
> | Custom landing page builder | 10 weeks | ✅ Yes (21.7 remaining) |
> | Free trial extension | 3 weeks | ✅ Yes (18.7 remaining) |
>
> **Buffer remaining after all work:** 18.7 engineer-weeks (~34% of net capacity)
>
> **Recommendation**
> We can absorb both new requests and still maintain a healthy buffer. However, the referral program v2 has medium-confidence estimates due to vendor integration unknowns. I'd recommend committing to both new requests with a caveat: if referral v2 blows past its estimate by more than 3 weeks, the landing page builder timeline slips.
>
> Suggested sequencing: onboarding framework and free trial extension in the first half of Q2 (smaller, higher confidence), referral v2 and landing page builder in the second half (larger, more complex).

## Tuning Notes

- **Overcommitted:** Lead with the gap number. "We have 40 engineer-weeks of capacity and 58 engineer-weeks of committed work. Here are the trade-offs." Force a conversation about what to cut.
- **New or volatile team:** Use a 30-40% overhead factor instead of 20%. New teams spend more time on process, learning, and coordination.
- **Individual-level planning:** Break capacity down per engineer when work requires specific expertise. "Only two engineers can work on the API integration" changes the math significantly.
- **Stakeholder presentation:** Show the maths transparently. Stakeholders respect capacity planning that accounts for reality (holidays, overhead, on-call) rather than pretending engineers have 100% utilisation.
