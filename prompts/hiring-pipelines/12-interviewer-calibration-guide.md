# Interviewer Calibration Guide

## Situation

Your interview panel gives inconsistent evaluations — one interviewer's "Hire" is another's "Strong Hire." New interviewers don't know what "good" looks like. You need a calibration session that aligns your interviewers on standards, reduces bias, and improves decision quality.

## The Prompt

```
You are an engineering leader designing an interviewer calibration session. The goal is to align interviewers on evaluation standards so that assessments are consistent across candidates and across interviewers. Calibration should be practical — not a lecture on bias, but hands-on practice with real examples.

Structure:
1. **Session design** — format, duration, who participates
2. **Calibration exercise** — a practical exercise using sample interview responses
3. **Rubric walkthrough** — align on what each rating level means with concrete examples
4. **Bias awareness** — the 3-4 most common biases in engineering interviews and how to counter them
5. **Practice debrief** — simulate a debrief discussion to practise evidence-based evaluation
6. **Ongoing calibration** — how to maintain alignment over time

Interview stage to calibrate: [STAGE]
Current issues: [CALIBRATION_PROBLEMS]
Team: [INTERVIEWER_POOL]
```

## Example Input

```
Stage: System design interview for Senior Backend roles
Issues: Wide variance in ratings — the same candidate gets "Strong Hire" from one interviewer and "No Hire" from another. Some interviewers over-index on whether the candidate uses the "right" technology. New interviewers don't know what L5 vs L4 system design looks like.
Interviewer pool: 8 engineers who interview regularly, 3 new interviewers being onboarded
```

## Example Output

> **Interviewer Calibration: System Design**
>
> **Session Format**
> - Duration: 90 minutes
> - Participants: All 11 interviewers (experienced + new)
> - Frequency: Once per quarter, plus an onboarding session for every new interviewer
> - Materials: 3 sample system design recordings (anonymised), the rubric, scoring sheets
>
> **Exercise: Rate the Same Candidate**
>
> Play a 15-minute excerpt of a system design interview (recorded from a past candidate who consented, or role-played by a senior engineer).
>
> Each interviewer independently rates the candidate on:
> - Requirement gathering (did they clarify before designing?)
> - Architecture quality (is the design sound?)
> - Trade-off articulation (can they explain why they chose this approach?)
> - Handling pushback (how do they respond when challenged?)
> - Overall rating: Strong No Hire / No Hire / Hire / Strong Hire
>
> Reveal everyone's ratings simultaneously (Google Form or show of hands). Discuss discrepancies.
>
> Repeat with 2 more samples at different quality levels (one clearly strong, one borderline, one weak).
>
> **Rubric Alignment — What Each Rating Means**
>
> | Rating | System Design Signals |
> |--------|--------------------|
> | **Strong Hire** | Drives the design proactively. Considers scale, failure modes, and operational concerns without prompting. Articulates trade-offs between 2+ approaches. Responds well to pushback — adjusts the design, doesn't get defensive. |
> | **Hire** | Produces a reasonable design. Addresses most requirements. Considers trade-offs when prompted. Communicates clearly. May miss some edge cases but reasons through them when pointed out. |
> | **No Hire** | Design is incomplete or has fundamental flaws. Doesn't consider failure modes. Can't articulate trade-offs. Communication is unclear or one-directional. Needs significant prompting to make progress. |
> | **Strong No Hire** | Cannot produce a coherent design. Doesn't engage with the problem. Unable to discuss basic concepts relevant to the level. |
>
> *Key calibration point:* "Hire" doesn't mean "perfect design." It means "this person demonstrated senior-level thinking even if the design has gaps." We're hiring engineers, not evaluating blueprints.
>
> **Common Biases to Watch**
>
> 1. **Technology bias:** Rating higher because the candidate uses the "right" tools (Kafka, Kubernetes) vs. a valid alternative. *Counter:* Evaluate the reasoning, not the technology choice. "Why did you choose X?" matters more than which X they chose.
>
> 2. **Similarity bias:** Rating higher because the candidate's approach matches how you'd do it. *Counter:* Ask yourself: "Is this a valid approach, or just not my approach?"
>
> 3. **Halo/horn effect:** Letting one strong (or weak) moment colour the entire evaluation. *Counter:* Rate each dimension independently before giving an overall rating.
>
> 4. **Confidence bias:** Confusing confident presentation with competent design. Quiet candidates can have excellent ideas. *Counter:* Focus on the content of the design, not the delivery style. Actively draw out quieter candidates with specific questions.
>
> **Practice Debrief**
> After rating the 3 samples, simulate a debrief:
> - Each interviewer shares their rating and top observation (no interruptions)
> - Discuss disagreements with specific evidence: "I rated Hire because they addressed X" not "I thought they were good"
> - Practice making a decision as a group
>
> **Ongoing Calibration**
> - Shadow program: new interviewers shadow 2 interviews, then are shadowed for 2 interviews before interviewing solo
> - Quarterly calibration sessions using new sample recordings
> - After every debrief, the hiring manager flags any rating that seems miscalibrated and follows up with the interviewer 1:1
> - Track interviewer rating distributions: if one interviewer is consistently the harshest or most lenient, calibrate individually

## Tuning Notes

- **No recorded interviews:** Role-play instead. Have a senior engineer play a "borderline Hire" candidate while another runs the interview. The rest of the room evaluates independently.
- **Calibration across levels:** Run separate calibrations for junior, mid, and senior. The bar is fundamentally different — a great L3 answer looks very different from a great L5 answer.
- **Resistance from experienced interviewers:** Frame it as "sharing expertise" not "correcting mistakes." Ask experienced interviewers to share what signals they've learned to look for. They have valuable pattern recognition to teach.
- **Measuring calibration:** Track inter-rater agreement over time. If calibration is working, the variance between interviewers on the same candidate should decrease.
