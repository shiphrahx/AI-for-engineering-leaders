---
name: escalation-policy-document
description: >
  Produces a single-page escalation policy — escalation tiers with contact methods,
  trigger criteria for moving between tiers, decision authority per tier (rollbacks,
  customer comms, spending, vendor contacts), an after-hours policy, cross-team paging,
  and external vendor support contacts. Use when the user says "write our escalation
  policy", "who do I call at 3am", "escalation tiers", "on-call escalation path", or
  pastes org structure and on-call setup. Use this to define who-gets-paged-and-when,
  not to define severity levels (severity-classification-guide) or the IC's coordination
  steps (incident-commander-runbook).
---

# Escalation Policy Document

Produce a single-page reference that eliminates all ambiguity from "who do I call next?" — covering both technical escalation (getting the right experts) and management escalation (getting decision authority), plus after-hours expectations. It must be followable under stress by anyone on-call.

## Inputs to gather

Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent org structure, names, contact methods, spending limits, or vendor support tiers. Mark unavailable fields as **Unknown** and prefer linking the live PagerDuty schedule over hard-coding names.

- **Org structure** — teams, tech leads, EMs, and the leadership chain
- **Services and owners** — which team owns which service
- **On-call structure** — rotation shape and whether there's a separate IC rotation
- **Communication tools** — PagerDuty, Slack, Zoom, Statuspage, etc.
- **Vendors** — third parties and their support tiers/contacts (AWS, Stripe, etc.)

## Steps

1. Write the policy in these sections: **Escalation Tiers**, **Cross-Team Escalation**, **Vendor Support Contacts**, **After-Hours Policy**. Fold trigger criteria and decision authority into each tier.
2. **Escalation Tiers**: define each tier (typically Tier 1 on-call engineer → Tier 2 IC + tech lead → Tier 3 EM → Tier 4 VP/CTO). For each, state **who**, **contact method** (and the auto-escalation timeout, e.g. PagerDuty escalates after 5 min of no response), **authority** (what they can approve — restarts/scaling/rollbacks at low tiers; war rooms, emergency deploys, customer comms at mid tiers; spending limits and legal/PR/public statements at high tiers), and the **escalate-when** criteria to the next tier.
3. **Cross-Team Escalation**: a table mapping service → owning team → PagerDuty service → Slack channel, with the rule: to engage another team's on-call, trigger their PagerDuty directly — don't Slack first; if it's urgent enough to need them, it's urgent enough to page them.
4. **Vendor Support Contacts**: a table of vendor → support level → how to reach (with severity/case path) → which internal tier is authorised to open the case.
5. **After-Hours Policy** (nights, weekends, holidays): what changes by severity — P0/P1 unchanged; P2 acknowledged and assessed, deferrable if no customer impact; P3 next business day, page no one. Note the one deliberate difference: escalate to Tier 2 sooner after hours (night debugging is slower — get help earlier).
6. Adapt to context as a sub-step: a small startup (<15 eng) may have just two tiers (on-call engineer and CTO) — that's fine, the document still sets expectations and contact methods; recommend printing it / pinning it (people don't search the wiki under stress); recommend testing phone numbers quarterly; and link the live PagerDuty schedule rather than listing names that go stale.
7. Assemble the output in the format below.
8. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Escalation Policy**

**Tier 1: [On-Call Engineer]**
- *Who:* [...]   *Contact:* [method + auto-escalation timeout]
- *Authority:* [what they can approve]
- *Escalate to Tier 2 when:* [criteria]

**Tier 2: [IC + Tech Lead]**  — same shape
**Tier 3: [Engineering Manager]**  — same shape (incl. spending limit)
**Tier 4: [VP Eng / CTO]**  — same shape (all decisions; legal/PR/public)

---

**Cross-Team Escalation**
| Service | On-Call Team | PagerDuty Service | Slack Channel |
|---------|--------------|-------------------|---------------|
[Rule: page the team's PagerDuty directly; don't Slack first.]

**Vendor Support Contacts**
| Vendor | Support Level | How to Reach | Auth Needed |
|--------|---------------|--------------|-------------|

**After-Hours Policy ([hours], weekends, holidays)**
- P0/P1: [unchanged]
- P2: [acknowledge/assess; deferrable if no impact]
- P3: [next business day; page no one]
- *Key difference:* [escalate to Tier 2 sooner]
```

## Boundaries

- Never invent names, phone numbers, spending authority limits, or vendor support tiers — mark **Unknown** and link the live schedule where possible.
- Never leave a tier without an explicit escalate-when trigger or a contact method; ambiguity defeats the document's purpose.
- Never relax P0/P1 after-hours response — only P2/P3 may differ.
- Never hard-code rotation member names where a live schedule link would stay current.

## Chaining

- After this, offer **incident-commander-runbook** — the runbook's escalation steps reference these tiers and authorities.
- The severity levels this policy keys off are defined by **severity-classification-guide**.
