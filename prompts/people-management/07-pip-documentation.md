# PIP Documentation

## Situation

A direct report is underperforming despite coaching and feedback, and you need to draft a Performance Improvement Plan. This is a serious document — it needs to be fair, specific, and give the person a genuine chance to succeed while protecting the organisation. Always involve HR before finalising.

## The Prompt

```
You are an engineering manager drafting a Performance Improvement Plan (PIP). The document must be specific, evidence-based, and fair. Every expectation should be measurable and every gap should be documented with examples. The tone should be professional and supportive — a PIP should communicate "here's exactly what success looks like and how we'll help you get there."

Structure:
1. **Purpose** — why the PIP is being initiated
2. **Performance gaps** — specific areas where expectations aren't being met, with dated examples
3. **Expected standards** — what "meeting expectations" looks like for each gap area
4. **Improvement goals** — measurable targets with specific deadlines
5. **Support provided** — what the company/manager will do to help (mentoring, training, reduced scope, etc.)
6. **Check-in schedule** — when and how progress will be reviewed
7. **Timeline and outcomes** — PIP duration and what happens at the end (successful completion or next steps)

Employee: [NAME], [ROLE], [LEVEL], [TENURE]
Performance gaps: [DESCRIBE_GAPS_WITH_EXAMPLES]
Previous coaching: [WHAT_FEEDBACK_HAS_BEEN_GIVEN]
Support available: [WHAT_HELP_CAN_YOU_OFFER]
```

## Example Input

```
Employee: Jamie, Backend Engineer, L4, 18 months at company
Performance gaps:
- Delivery: Last 3 sprints, Jamie completed 40-50% of committed story points (team average is 80%). Two features were delivered 3+ weeks late.
- Code quality: 4 production bugs in the last quarter traced to Jamie's PRs. Two were P1 incidents. PR review feedback is consistently about missing error handling and no tests.
- Communication: Missed 3 standup updates in the last month. Team lead didn't know Jamie was blocked on the auth integration until the sprint review.

Previous coaching: Discussed delivery concerns in 1:1s on Jan 15, Feb 2, and Feb 20. Paired Jamie with a senior engineer for 2 weeks in February. Reduced scope in Sprint 12 to 60% of normal load. Issues persisted.

Support available: Senior engineer mentor, reduced scope, weekly check-ins, optional training budget for relevant courses.
```

## Example Output

> **Performance Improvement Plan**
>
> **Employee:** Jamie — Backend Engineer (L4)
> **Manager:** [Your name]
> **Date:** March 10, 2025
> **PIP Duration:** 6 weeks (March 10 – April 21)
> **HR Contact:** [HR partner name]
>
> ---
>
> **Purpose**
> This Performance Improvement Plan is being initiated because Jamie's performance has not met L4 expectations in three areas — delivery, code quality, and communication — despite coaching conversations on January 15, February 2, and February 20, a pairing arrangement with a senior engineer, and a scope reduction in Sprint 12. The purpose of this plan is to set clear, measurable expectations and provide structured support to help Jamie meet them.
>
> **Performance Gaps**
>
> *1. Delivery*
> L4 expectation: Complete 75%+ of sprint-committed work consistently.
> Current performance: 40-50% of committed story points completed in Sprints 10, 11, and 12. The user notification feature (committed Feb 1) was delivered March 3. The API rate limiting work (committed Jan 20) was delivered February 14. These represent a pattern, not isolated incidents.
>
> *2. Code Quality*
> L4 expectation: Code passes review with minor feedback; production bugs are rare and not due to missing fundamentals (error handling, test coverage).
> Current performance: Four production bugs in Q1 traced to Jamie's PRs, including two P1 incidents (order processing failure on Feb 8, data sync corruption on March 2). Consistent PR feedback across reviewers about missing error handling and absent test coverage.
>
> *3. Communication*
> L4 expectation: Provide daily standup updates, surface blockers within 24 hours, and keep the team informed on progress.
> Current performance: Missed standup updates on Feb 5, Feb 18, and March 4. The auth integration blocker was not communicated until sprint review on February 28, despite being stuck since February 19.
>
> **Improvement Goals**
>
> | Area | Goal | Measurement | Deadline |
> |------|------|-------------|----------|
> | Delivery | Complete 70%+ of committed story points for 3 consecutive sprints | Sprint velocity report | Sprints 13, 14, 15 |
> | Code quality | Zero P1/P2 production bugs from Jamie's PRs | Incident tracker | 6-week period |
> | Code quality | All PRs include unit tests covering primary and error paths | PR review records | Every PR during PIP |
> | Communication | Attend daily standup and provide status update (or async message if unable to attend) | Standup attendance log | Daily during PIP |
> | Communication | Flag blockers within 24 hours via standup or direct message to team lead | Team lead confirmation | Ongoing during PIP |
>
> **Support Provided**
> - **Mentor pairing:** Alex (senior engineer) will pair with Jamie for 1 hour twice weekly to review work in progress and provide early feedback on approach
> - **Reduced scope:** Sprint commitments will be set at 60% of team average for the first 3 weeks, ramping to 75% for weeks 4-6
> - **Code review support:** Jamie's PRs will receive prioritised review with constructive, detailed feedback
> - **Training:** Access to company training budget for any relevant courses Jamie identifies
> - **Manager support:** Weekly 30-minute check-ins (in addition to regular 1:1) focused specifically on PIP progress
>
> **Check-in Schedule**
> - **Weekly:** 30-minute PIP progress review with manager (Wednesdays)
> - **Bi-weekly:** 15-minute check-in with HR partner
> - **Week 3:** Formal mid-point review — written assessment of progress against goals
> - **Week 6:** Final review — formal determination of PIP outcome
>
> **Timeline and Outcomes**
> This PIP runs for 6 weeks. At the end of the period:
> - **Successful completion:** All goals met — PIP closes, regular performance management resumes
> - **Partial improvement:** Significant progress but not all goals met — PIP may be extended by 2-4 weeks at manager's discretion
> - **Insufficient improvement:** Goals not met — the next step will be discussed with HR, up to and including separation
>
> Jamie is encouraged to ask questions, provide feedback on the support offered, and raise any concerns during check-ins or at any time with their manager or HR partner.

## Tuning Notes

- **Always involve HR:** This prompt generates a draft. Do not finalise or deliver a PIP without HR review. Employment law varies by jurisdiction and your HR team will ensure compliance.
- **Document everything before the PIP:** The PIP should never be the first time someone hears about performance concerns. If you haven't had at least 2-3 documented coaching conversations, you're not ready for a PIP.
- **Genuine improvement plan vs. "paper trail":** If you're writing a PIP just to document before termination, be honest with yourself. A real PIP gives the person a fair shot. Set goals that are achievable, not designed to fail.
- **Sensitivity:** This is one of the most stressful documents a manager writes. Have the delivery conversation in person (or video), not email. Lead with care: "I want you to succeed, and here's the specific plan to get there."
