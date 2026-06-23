---
name: severity-classification-guide
description: >
  Produces an unambiguous incident severity classification guide (P0–P3) — per-level
  definitions, concrete examples, response/communication expectations, required roles,
  and a 60-second classification flowchart. Use when the user says "define our severity
  levels", "P0 vs P1 vs P2", "stop the severity debates", "incident severity matrix", or
  pastes product/SLA/team context and asks how to classify incidents. Use this to author
  the org-wide standard, not to coordinate a live response (incident-commander-runbook)
  or to set who-gets-paged escalation tiers (escalation-policy-document).
---

# Severity Classification Guide

Produce a severity guide so unambiguous that an engineer reading it at 3am can classify any incident in under a minute — eliminating the war-room debate over "is this a P1 or a P2?"

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a SINGLE batched question — never invent SLAs, customer counts, or business hours. Mark anything genuinely unavailable as **Unknown** in the output rather than guessing.

- **Product type** — what the product is and how customers use it
- **Customer base** — number of customers/users, tiers, and any contractual commitments
- **SLAs** — uptime guarantees and response-time commitments, if any
- **Team size** — engineering headcount and on-call structure (24/7 vs business hours)
- **Business hours** — peak usage windows and customer time zones

## Steps

1. Anchor the whole guide on one principle: **classify by customer impact, not technical complexity.** A complex bug affecting no customers is P3; a one-line bug blocking all logins is P0. State this rule of thumb at the top.
2. For each level **P0, P1, P2, P3**, write all five fields: **Definition** (one unambiguous sentence), **Examples** (3–4 concrete, product-specific scenarios), **Response expectations** (time to acknowledge, time to assemble, target resolution), **Communication** (who to notify, how often, what channel), and **Who's involved** (required roles).
3. Make examples specific to the user's actual product and services — not generic. Map them to the stated key features and known failure modes.
4. Tune the thresholds to the product's risk profile: for payments, healthcare, or anything safety-critical, lower the P0/P1 bar so more things qualify as severe.
5. If the org has contractual SLAs, add which severities count against SLA time (typically P0 and P1, not P2/P3).
6. If the org runs reduced after-hours response, document it explicitly — and state that P0/P1 response never changes regardless of time; only P2 and below may relax.
7. Add a **Quick Classification Flowchart**: a top-down decision tree that yields a level in four questions or fewer.
8. Add a **Reclassification** note: the IC can upgrade or downgrade at any time; overclassify initially and downgrade rather than underclassify and scramble. If a debate runs past ~30 seconds, classify high.
9. Assemble the output in the format below.
10. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Incident Severity Classification Guide**

*Rule of thumb: classify based on customer impact, not technical complexity.*

---

**P0 — Critical: [one-sentence definition]**

| | |
|---|---|
| **Examples** | [3–4 specific scenarios] |
| **Acknowledge** | [time] |
| **Assemble** | [time / mechanism] |
| **Target resolution** | [time] |
| **Communication** | [who, how often, what channel] |
| **Who's involved** | [required roles] |

---

**P1 — Major: [definition]**
[same table shape]

**P2 — Minor: [definition]**
[same table shape]

**P3 — Low: [definition]**
[same table shape]

---

**Quick Classification Flowchart**
  Is the entire product down or is customer data at risk?  → YES → P0
    → NO ↓
  Is a core workflow broken or severely degraded for many users?  → YES → P1
    → NO ↓
  Is a secondary feature broken? Are there workarounds?  → YES → P2
    → NO ↓
  Is the impact cosmetic, internal, or edge-case only?  → YES → P3

**Reclassification:** [IC can re-grade at any time; overclassify and downgrade.]

[If SLAs apply: note which severities count against SLA time.]
[If after-hours policy differs: state it explicitly; P0/P1 unchanged.]
```

## Boundaries

- Never fabricate SLAs, customer counts, uptime numbers, or business hours — mark them **Unknown** and write the guide around what is known.
- Never classify by technical difficulty, effort, or who caused it — only by customer impact.
- Never produce ambiguous definitions that leave a reader debating; if two levels could both apply, the guide has failed its purpose.
- Never relax P0/P1 response expectations for after-hours; only P2 and below may differ.
- This authors the standard — do not use it to make a live severity call on a specific incident in progress.

## Chaining

- After this, offer **incident-commander-runbook** — the runbook references these severity levels to set response level and comms cadence.
- The severity levels defined here also feed **escalation-policy-document** (which tiers engage at which severity).
