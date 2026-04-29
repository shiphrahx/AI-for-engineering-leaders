# Interview Rubric

## Situation

You're setting up an interview loop and want structured evaluation criteria so interviewers assess candidates consistently and conversations don't overlap. Each interviewer should know exactly what they're evaluating and what "good" looks like.

## The Prompt

```
You are an engineering leader creating a structured interview rubric. Each interview stage should assess specific competencies with clear criteria for each rating level. Interviewers should be able to use this rubric independently and produce evaluations that are comparable across candidates.

Structure:
1. **Interview loop overview** — stages, interviewers, and what each stage assesses
2. **Per-stage rubric** — competency assessed, questions or areas to explore, and rating criteria (strong no hire / no hire / hire / strong hire) with observable behaviours for each
3. **Debrief guide** — how to combine assessments into a decision

Role: [ROLE_AND_LEVEL]
Key competencies to assess: [COMPETENCY_LIST]
Interview stages: [STAGES]
```

## Example Input

```
Role: Senior Backend Engineer (L5) on Payments team
Key competencies: System design, code quality, payment domain knowledge, collaboration, problem-solving under ambiguity
Stages: Technical screen (45 min), System design (60 min), Code review (45 min), Behavioural (45 min)
```

## Example Output

> **Interview Rubric: Senior Backend Engineer (L5) — Payments**
>
> **Loop Overview**
> | Stage | Duration | Interviewer | Assessing |
> |-------|----------|-------------|-----------|
> | Technical Screen | 45 min | Senior Engineer | Coding fundamentals, problem decomposition |
> | System Design | 60 min | Staff/Principal Eng | Architecture thinking, trade-off analysis, scale awareness |
> | Code Review | 45 min | Team member | Code quality judgment, communication, mentoring signal |
> | Behavioural | 45 min | Hiring Manager | Collaboration, ownership, handling ambiguity, values fit |
>
> ---
>
> **Stage 2: System Design Rubric**
>
> *Prompt:* "Design a payment retry system that handles failed transactions. The system processes 50K transactions/day, and currently 3% fail. Design for reliability, observability, and minimal duplicate charges."
>
> | Rating | Observable Behaviours |
> |--------|----------------------|
> | **Strong Hire** | Asks clarifying questions about failure modes before designing. Proposes idempotency strategy unprompted. Considers at least 2 approaches and articulates trade-offs clearly. Addresses edge cases (partial failures, timeout ambiguity). Discusses monitoring and alerting without prompting. Thinks about the customer experience, not just the system. |
> | **Hire** | Produces a workable design with reasonable components. Addresses idempotency when prompted. Considers scale and explains how the system handles load. Communicates clearly and responds well to interviewer pushback. May miss some edge cases but reasons through them when prompted. |
> | **No Hire** | Jumps to implementation without clarifying requirements. Proposes a design that doesn't address duplicate charges. Struggles to articulate trade-offs between approaches. Doesn't consider failure modes or observability. Communication is unclear or one-directional. |
> | **Strong No Hire** | Cannot produce a coherent system design. Doesn't engage with the problem space. Unable to discuss distributed systems concepts relevant to the role. |
>
> ---
>
> **Stage 3: Code Review Rubric**
>
> *Format:* Show the candidate a real PR (~200 lines) with intentional issues: a subtle correctness bug, a performance concern, a readability issue, and a missing test case.
>
> | Rating | Observable Behaviours |
> |--------|----------------------|
> | **Strong Hire** | Catches the correctness bug and explains the impact. Identifies the performance concern with a concrete suggestion. Frames feedback constructively — review comments are something you'd want to receive. Suggests a missing test case and explains what it would catch. Prioritises their feedback (blocking vs. nit). |
> | **Hire** | Catches 2-3 of the 4 issues. Feedback is clear and constructive. Demonstrates understanding of code quality beyond "it works." Asks about context where appropriate. |
> | **No Hire** | Focuses only on style issues while missing the correctness bug. Feedback is vague or unconstructive. Doesn't consider the broader implications of the code. |
> | **Strong No Hire** | Doesn't find meaningful issues. Feedback would not improve the code. |
>
> ---
>
> **Debrief Guide**
> - Each interviewer shares their rating and top 2-3 observations (not a full replay)
> - Identify any "must-hire" or "must-not-hire" signals
> - Discuss any rating disagreements — focus on what the candidate demonstrated, not on resolving differences of opinion
> - Decision: Hire requires Hire or Strong Hire from at least 3 of 4 stages, with no Strong No Hire from any stage
> - Any concerns about the candidate's ability to succeed specifically on the Payments team should be surfaced explicitly

## Tuning Notes

- **Junior role:** Replace system design with a pair programming exercise. Assess learning speed and coachability, not depth of knowledge.
- **Staff+ role:** Add a "technical strategy" stage where the candidate evaluates a real architectural decision your team faces. Assess their ability to navigate ambiguity and influence without authority.
- **Reducing bias:** Calibrate interviewers before the loop starts by reviewing the rubric together with an example. Score independently before the debrief — don't let the first speaker anchor the room.
- **Small company (no dedicated interviewers):** Combine stages. A 90-minute technical interview covering coding + design + code review is better than four poorly prepared 45-minute sessions.
