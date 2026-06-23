---
name: interview-rubric
description: >
  Produces a structured interview rubric for a role — a loop overview, per-stage rubrics with
  competencies and observable behaviours at each rating level (strong no hire → strong hire),
  and a debrief/decision guide. Use when the user says "create an interview rubric", "scorecard
  for [role]", "structure our interview loop", or pastes a role, competencies, and interview
  stages. Use this to design how candidates are evaluated; use job-description to attract them,
  and hiring-pipelines/candidate-evaluation-summary to synthesise a completed loop into a
  decision.
---

# Interview Rubric

Build evaluation criteria so interviewers assess candidates consistently, stages don't overlap, and every interviewer knows exactly what they're evaluating and what "good" looks like.

## Inputs to gather

Gather these before drafting. If any are missing, ask in a single batched question — never invent the role's competencies or the interview stages. Mark anything genuinely unavailable as **Unknown**.

- **Role** — title and level
- **Key competencies** — what the loop must assess
- **Interview stages** — the stages and their durations

## Steps

1. Build a **Loop Overview** table: each stage, duration, interviewer, and what it assesses — ensuring stages don't redundantly cover the same competency.
2. For each stage, write a **rubric**: the competency assessed, the prompt or areas to explore, and a rating table with observable behaviours for **Strong Hire**, **Hire**, **No Hire**, and **Strong No Hire**. Make behaviours observable ("proposes idempotency unprompted"), not vague ("good system thinking").
3. Write a **Debrief Guide**: how interviewers share ratings and top observations, how to handle disagreement (focus on what the candidate demonstrated, not resolving opinions), and the explicit decision rule (e.g. Hire requires Hire+ from 3 of 4 stages with no Strong No Hire).
4. Adapt to context: for a **junior role**, replace system design with a pair-programming exercise assessing learning speed and coachability, not depth. For a **staff+ role**, add a technical-strategy stage where the candidate evaluates a real architectural decision, assessing influence without authority. For **reducing bias**, add a calibration step (review the rubric together with an example before the loop) and require independent scoring before debrief so the first speaker doesn't anchor the room. For a **small company without dedicated interviewers**, combine stages — one well-prepared 90-minute session beats four rushed 45-minute ones.
5. Assemble the output in the format below.
6. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Interview Rubric: [Role and Level]**

**Loop Overview**
| Stage | Duration | Interviewer | Assessing |
|-------|----------|-------------|-----------|
| [stage] | [time] | [role] | [competency] |

---

**Stage [N]: [Name] Rubric**

*Prompt/Format:* [What the interviewer runs]

| Rating | Observable Behaviours |
|--------|----------------------|
| **Strong Hire** | [Specific, observable behaviours] |
| **Hire** | [...] |
| **No Hire** | [...] |
| **Strong No Hire** | [...] |

---
[repeat per stage]

**Debrief Guide**
- [How ratings and observations are shared]
- [How disagreements are handled]
- Decision: [explicit rule]
```

## Boundaries

- Never invent the role's competencies or stages. Mark unknowns as **Unknown** and ask.
- Keep criteria job-related and observable. Never include "culture fit" as a vague catch-all, or any proxy for age, gender, race, nationality, accent, or other protected characteristics — assess demonstrated skills and behaviours only.
- Don't design questions that advantage a particular background or pedigree over demonstrated ability.
- The rubric supports a decision; it does not make one for a specific candidate — that synthesis belongs in candidate-evaluation-summary.

## Chaining

- After the loop runs, offer **hiring-pipelines/candidate-evaluation-summary** to synthesise interviewer scores into an evidence-based decision.
- This typically follows **job-description** — design the JD first, then the rubric that evaluates against it.
