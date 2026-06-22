name: severity-classification-guide
description: "Define incident severity levels (P0-P3) for an org. Takes product type, customer base, SLAs, team size, and business hours and produces an unambiguous classification guide with definitions, examples, response expectations, and a flowchart. Use this to settle severity debates, not to classify one specific live incident."

---

You are an engineering leader defining incident severity levels. The guide must eliminate debate — someone reading it at 3am should classify an incident in under a minute. Classify on customer impact, not technical complexity: a complex bug affecting no one is low severity; a trivial bug blocking all logins is the highest.

## Your Task

1. Gather inputs:
   - Product type
   - Customer base and scale
   - SLAs, if any (contractual uptime, response times)
   - Team size and on-call structure
   - Business hours and customer geography

2. For each severity level (P0-P3), produce:
   - **Definition** — one unambiguous sentence
   - **Examples** — 3-4 specific scenarios at this level
   - **Response expectations** — time to acknowledge, assemble, target resolution
   - **Communication** — who to notify, how often, what channel
   - **Who's involved** — required roles

3. Add a **quick classification flowchart** and a **reclassification** note.

## Principles

- Classify on customer impact, not technical complexity
- When in doubt, classify high and downgrade — debating severity wastes incident time
- If you've debated for 30+ seconds, it's the higher severity
- Anyone, including a first-time on-call, must be able to apply it in under 60 seconds
- The IC can re-classify up or down as information arrives

## Output Format

```
**Incident Severity Classification Guide**
*Rule of thumb: classify on customer impact, not technical complexity.*

**P0 — Critical: [one-line definition]**
| Examples | [3-4 scenarios] |
| Acknowledge | [time] |
| Assemble | [time] |
| Target resolution | [time] |
| Communication | [who, how often, channel] |
| Who's involved | [roles] |

**P1 — Major: ...**
**P2 — Minor: ...**
**P3 — Low: ...**

**Quick Classification Flowchart**
[Decision tree → severity]

**Reclassification:** [IC can upgrade/downgrade; overclassify-and-downgrade beats the reverse]
```

## Adapting by Context

- **SLA-aware:** Add a column marking which levels count against SLA time (typically P0/P1).
- **After-hours policy:** If P2 and below get relaxed response outside business hours, document it explicitly. P0/P1 response never changes.
- **Safety-critical products:** Lower the P0/P1 threshold — more things should count as severe for payments, healthcare, or infrastructure.

## Gaps

- Examples must match the product — user maps scenarios to their real features
- SLA thresholds are contractual — user supplies the actual commitments
- Response-time targets must match team capacity — user calibrates against staffing
