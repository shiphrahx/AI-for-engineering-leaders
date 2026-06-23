---
name: slo-definition
description: >
  Produces Service Level Objectives — SLIs, SLO targets over a rolling window, an error budget
  derived from real traffic, an error budget policy, measurement methods, and review cadence. Use
  when the user says "define SLOs", "set reliability targets", "error budget", "what uptime should
  we commit to", or names a service that needs a reliability bar. Use this to set the targets; use
  observability-strategy to build the instrumentation that measures them, and incident-postmortem
  to analyse a breach after it happens — not for SLAs, which are the stricter external promise.
---

# SLO Definition

Define reliability targets that are measurable, meaningful to the business, and actionable by engineering — giving the team a target and stakeholders a shared language for "how reliable is reliable enough?"

## Inputs to gather

Gather these before defining. If any are missing, ask in a single batched question — never invent traffic volumes, current reliability, or business expectations. Mark anything genuinely unavailable as **Unknown** in the output.

- **Service name and what it does**
- **Users/consumers** and traffic volume
- **Current reliability** — success rate, latency
- **Business expectations** — what stakeholders assume "working" means

## Steps

1. Confirm inputs. If traffic volume or business expectations are unstated, ask — the error budget can't be computed without volume. Mark gaps **Unknown**.
2. Write the **Service overview** — what it does, who depends on it, and why reliability matters here.
3. Choose **SLIs** that measure user-facing symptoms (availability, latency, correctness), never internal causes (CPU). Exclude client errors (4xx) from availability — they aren't your failures.
4. Set **SLOs** — a target per SLI over a rolling window. Never target 100%; it removes the budget that lets you ship.
5. Compute the **Error budget** from the traffic volume — translate each percentage into a concrete count ("99.95% → 120 failures/month, 4/day"), which is more visceral than a percentage.
6. Write the **Error budget policy** — what concretely changes at each threshold (normal dev → caution → reliability mode → leadership review). An SLO without this policy is just a number.
7. Specify **Measurement** for each SLI — data source, query, and exclusions; confirm the data actually exists.
8. Set the **Review cadence** — when to review and when to adjust targets up or down.
9. Adapt to context: for a team's first SLOs, start with availability only and add latency/correctness once they're comfortable. For internal services, the "customer" is the dependent team — agree targets together. For customer-facing SLAs, keep the SLO stricter than the SLA to preserve a buffer. If SLOs feel too abstract, recommend a dashboard showing the remaining budget as a count.
10. Assemble the output in the format below.
11. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**SLO Definition: [Service]**

**Service:** [What it does, who depends on it, why reliability matters]

**SLIs and SLOs**
| SLI | Definition | SLO Target | Window |
|-----|-----------|------------|--------|

**Error Budget**
[Traffic volume → allowed failures per window, per SLI, as counts]

**Error Budget Policy**
- **Budget > 50% remaining:** [Normal development]
- **Budget 25-50%:** [Caution]
- **Budget < 25%:** [Reliability mode]
- **Budget exhausted:** [Leadership review, reliability sprint]

**Measurement**
[Per SLI: data source, query, exclusions]

**Review Cadence:** [When and how often]
```

## Boundaries

- Never fabricate traffic volume, current reliability, or stakeholder expectations — mark them **Unknown**; the error budget depends on real volume.
- Never set an SLI on an internal cause (CPU, memory) when a user-facing symptom is available.
- Never target 100%, and never define an SLO without an error budget policy that changes team behaviour.
- Confirm each SLI is actually measurable with existing data before committing to it — don't promise a metric the system can't emit.

## Chaining

- Pairs with **observability-strategy** — the instrumentation there is what makes these SLIs measurable; do one then the other.
- After a breach, offer **incident-postmortem** to analyse the burn and derive action items.
