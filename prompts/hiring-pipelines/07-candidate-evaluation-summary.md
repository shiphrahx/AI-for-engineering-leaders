# Candidate Evaluation Summary

## Situation

The interviews are done and you need to synthesise all feedback into a coherent evaluation. This document supports the hiring decision and goes into the candidate's file. It should be fair, specific, and useful for future reference.

## The Prompt

```
You are a hiring manager synthesising interview feedback into a candidate evaluation summary. Be specific and evidence-based. Every strength and concern should be tied to an interview observation. The summary should be useful to someone who wasn't in the interviews.

Structure:
1. **Candidate snapshot** — name, role applied for, interview dates, overall recommendation
2. **Strengths** — 3-5 strengths with evidence from interviews
3. **Concerns** — 2-3 concerns with evidence and severity assessment
4. **Level assessment** — does the candidate meet the bar for the target level?
5. **Team fit** — how they'd complement the existing team
6. **Recommendation** — hire/no-hire with confidence level and any conditions

Candidate: [NAME]
Role: [ROLE]
Interview feedback: [PASTE_ALL_FEEDBACK]
```

## Example Input

```
Candidate: Jordan, applied for Senior Backend Engineer (L5)
Phone screen (me): Strong communication, clear explanation of past work, motivated by the billing problem. Technical questions were solid but not exceptional.
System design (Priya): Designed a webhook system. Good architecture instincts — started with requirements, considered failure modes. Struggled slightly with the scaling discussion but recovered well with prompting. Rating: Hire.
Code review (Marcus): Found the correctness bug and the performance issue. Missed the missing test case. Feedback was constructive and well-framed. "This is someone I'd want reviewing my code." Rating: Strong Hire.
Behavioural (Suki): Great examples of technical leadership — drove a migration at previous company. Conflict resolution example was a bit surface-level. Clearly collaborative. Rating: Hire.
```

## Example Output

> **Candidate Evaluation: Jordan — Senior Backend Engineer**
>
> **Recommendation: Hire (High Confidence)**
>
> **Strengths**
> - **Code quality judgment (Strong signal):** In the code review exercise, Jordan identified both the correctness bug and the performance issue. Marcus noted that Jordan's review comments were constructive and explanatory — "someone I'd want reviewing my code."
> - **Architectural thinking:** System design demonstrated strong instincts. Started by clarifying requirements (unprompted), considered failure modes, and proposed a clean component breakdown. The webhook design was practical and production-minded.
> - **Technical leadership experience:** Provided a concrete example of leading a database migration at their previous company — 6-month project, 3 engineers, zero-downtime cutover. This maps well to our upcoming billing engine project.
> - **Communication:** Consistently clear across all interviews. Explains technical concepts without jargon. This is important for cross-team work in our payments domain.
>
> **Concerns**
> - **Scaling depth (Minor):** Needed prompting in the system design to address how the webhook system would handle 100x traffic growth. Once prompted, the answers were reasonable but not instinctive. Severity: minor — this is coachable and our current scale doesn't require deep expertise here yet.
> - **Conflict resolution (Minor):** Behavioural example of handling disagreement was somewhat surface-level. Couldn't clearly articulate the resolution approach. Severity: minor — the example may have been poorly chosen rather than indicating a skill gap.
>
> **Level Assessment**
> Jordan meets the L5 bar. Demonstrates project-level ownership, mentoring instinct (visible in code review style), and cross-team collaboration. Not yet showing L6/Staff signals, which is expected and appropriate.
>
> **Team Fit**
> Complements the team well. Our code review culture will benefit from Jordan's constructive review style. The migration experience is directly relevant to the billing engine project. Fills a gap in our team's senior capacity.
>
> **Conditions:** None. Recommend proceeding to offer.

## Tuning Notes

- **Borderline candidate:** Be explicit about what tips the balance. "Despite the concern about X, we recommend hiring because Y." Future readers need to understand the reasoning.
- **Internal candidate:** Same rigour. Don't give a softer evaluation because you know the person. Document strengths and concerns with the same evidence standard.
- **Storing evaluations:** This document should be factual and professional. It may be reviewed by HR, legal, or the candidate themselves in some jurisdictions.
- **Rejected candidate who might reapply:** Note specific areas for growth. "If Jordan reapplies in 12 months, look for improved depth in distributed systems scaling."
