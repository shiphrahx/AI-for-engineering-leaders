# Interview Debrief Facilitation

## Situation

The interview loop is complete and you're running the debrief meeting. You need to facilitate a structured discussion that produces a clear hire/no-hire decision based on evidence, not anchoring bias or loudest-voice-wins dynamics.

## The Prompt

```
You are a hiring manager facilitating an interview debrief. The debrief should be evidence-based, efficient, and produce a clear decision. Prevent anchoring bias by having each interviewer share independently before group discussion.

Structure:
1. **Pre-debrief setup** — what interviewers should prepare before the meeting
2. **Opening** — set the rules for the debrief
3. **Round-robin** — each interviewer shares their assessment independently
4. **Discussion** — structured discussion of strengths, concerns, and gaps
5. **Decision** — how to reach and document the decision
6. **Post-debrief** — next steps for hire or no-hire

Candidate: [CANDIDATE_NAME]
Role: [ROLE]
Interviewers: [INTERVIEWER_LIST_AND_STAGES]
```

## Example Input

```
Candidate: Alex
Role: Senior Backend Engineer, Payments
Interviewers: Me (phone screen), Priya (system design), Marcus (code review), Suki (behavioural)
```

## Example Output

> **Debrief Facilitation Plan**
>
> **Pre-Debrief (before the meeting)**
> Each interviewer submits their written assessment before the debrief. Include: their rating (Strong No Hire / No Hire / Hire / Strong Hire), top 2 strengths, top 2 concerns, and one memorable signal. No one reads others' assessments until the meeting.
>
> **Opening (2 min)**
> "We're here to decide on Alex for the Senior Backend role. Rules: each interviewer shares their rating and key observations without interruption. No one changes their rating based on what they hear — we discuss disagreements after everyone has shared. I'll go last to avoid anchoring."
>
> **Round-robin (15 min, ~3 min each)**
> Order: Suki (behavioural) → Marcus (code review) → Priya (system design) → Me (screen)
> Each shares: rating, top strength, top concern, one signal.
>
> **Discussion (10 min)**
> - "Where do we agree?"
> - "Where do we disagree? Let's discuss the specific evidence."
> - "Are there any gaps — things we didn't assess that matter for this role?"
> - "If hired, what's the onboarding risk? What would we need to set up for success?"
>
> **Decision (5 min)**
> - Hire requires ≥3 of 4 interviewers at Hire or Strong Hire, with no Strong No Hire
> - If split: discuss the specific disagreement, then I make the final call as hiring manager
> - Document the decision and rationale in the ATS
>
> **Post-Debrief**
> - Hire → I draft the offer justification and send to compensation review within 24 hours
> - No hire → I send a personalised rejection email within 48 hours

## Tuning Notes

- **Strong disagreement:** If one interviewer is Strong Hire and another is Strong No Hire, don't average — dig in. They saw different things. The discussion about what each observed is more valuable than the rating.
- **Anchoring prevention:** The hiring manager shares last. If you share first, you anchor the room.
- **Remote debriefs:** Use a shared doc where everyone pastes their assessment simultaneously, then discuss verbally. This prevents sequential anchoring.
- **Debrief fatigue:** Keep it under 30 minutes. If you're debating for an hour, the signal is mixed — which is itself a signal.
