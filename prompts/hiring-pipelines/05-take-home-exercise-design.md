# Take-Home Exercise Design

## Situation

You want candidates to demonstrate their skills through a take-home exercise rather than (or in addition to) a whiteboard interview. The exercise needs to be fair, well-scoped, realistic, and respectful of the candidate's time.

## The Prompt

```
You are an engineering leader designing a take-home exercise for candidates. It should be completable in 2-3 hours, relevant to the actual work, and evaluable with a rubric. Respect the candidate's time — over-scoped exercises are the #1 reason strong candidates drop out of your pipeline.

Structure:
1. **Exercise brief** — what the candidate will build, with clear requirements
2. **Time expectation** — explicit, and you mean it (2-3 hours max)
3. **What you're evaluating** — the specific skills this exercise assesses
4. **What you're NOT evaluating** — things candidates shouldn't worry about
5. **Evaluation rubric** — criteria and what "strong hire" vs "no hire" looks like for each
6. **Candidate instructions** — what to submit, in what format, and any constraints

Role: [ROLE]
Skills to assess: [SKILLS]
Domain: [TEAM_DOMAIN]
```

## Example Input

```
Role: Senior Backend Engineer, Payments team
Skills: API design, error handling, data consistency, code quality, testing
Domain: Payment processing
```

## Example Output

> **Take-Home Exercise: Payment Retry Service**
>
> **Brief**
> Build a small service that processes payment retries. Given a list of failed payment attempts (provided as a JSON file), the service should: determine which payments are eligible for retry (based on failure reason and attempt count), schedule retries with exponential backoff, execute the retries against a mock payment provider (provided), and log the results.
>
> **Time:** Please spend no more than 3 hours. We mean this. An incomplete-but-well-structured solution is better than a complete-but-rushed one. Tell us what you'd improve with more time.
>
> **What We're Evaluating**
> - API/service design: How do you structure the code? Is it maintainable?
> - Error handling: How do you handle payment provider failures, network errors, and edge cases?
> - Data consistency: How do you prevent duplicate charges? How do you handle partial failures?
> - Testing: Do you write tests? Are they meaningful (not just happy path)?
> - Code quality: Is the code readable, well-organised, and production-minded?
>
> **What We're NOT Evaluating**
> - UI or frontend work
> - Infrastructure or deployment configuration
> - Performance optimisation (correctness over speed)
> - Use of any specific framework (use whatever you're comfortable with)
>
> **Rubric**
> | Criteria | Strong Hire | Hire | No Hire |
> |----------|------------|------|---------|
> | Idempotency | Handles duplicate retries without double-charging, explains approach | Basic duplicate prevention | No consideration of duplicate charges |
> | Error handling | Graceful degradation, different handling for different failure types | Catches errors, basic retry logic | Errors crash the service or are silently swallowed |
> | Code structure | Clean separation of concerns, easy to extend | Organised, readable | Monolithic, hard to follow |
> | Testing | Unit + integration tests, covers edge cases | Tests exist, cover main path | No tests or trivial tests only |
> | Communication | Clear README explaining decisions, trade-offs noted, what they'd improve | README explains how to run the solution | No README or explanation |
>
> **Submission**
> - GitHub repo (public or private with our reviewer added) or zip file
> - Include a README with: how to run it, key design decisions, and what you'd do differently with more time
> - Language: Go preferred, Python or TypeScript also accepted
> - Due: 5 business days from receipt (no penalty for submitting earlier)

## Tuning Notes

- **Candidate complaints about take-homes:** The most common complaint is time. Be brutally honest about the expected hours and respect it. If your exercise takes 6 hours, you're losing good candidates.
- **Alternative: pair programming session:** Some candidates prefer live collaboration over take-homes. Consider offering both options and letting the candidate choose.
- **Reviewing blind:** Remove candidate names before the review panel sees the submissions. This reduces bias significantly.
- **Compensate for time:** Some companies pay for take-home exercises ($200-500). This signals respect for the candidate's time and increases completion rates.
