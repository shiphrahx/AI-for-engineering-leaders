---
name: skip-level-meeting-prep
description: >
  Produces a skip-level 1:1 prep guide for someone who reports to one of your reports — a warm
  specific opener, team-perspective questions, a broader career conversation, gently-phrased
  signal questions, and a close that sets expectations. Use when the user says "prep a
  skip-level", "I'm meeting my report's report", or pastes the person's role, their manager, and
  context. Use this for a skip-level relationship; use one-on-one-prep for your own direct
  report and difficult-conversation-prep for a hard message.
---

# Skip-Level Meeting Prep

Prepare a skip-level that builds a direct relationship, surfaces unfiltered signal about team health, and offers broader career perspective — without undermining the middle manager or creating a shadow-management dynamic.

## Inputs to gather

Gather these before drafting. If any are missing, ask in a single batched question — never invent the person's work, their manager's name, or context. Mark anything genuinely unavailable as **Unknown**.

- **Person** — name, role, level
- **Their manager** — name
- **What they're working on** — current work
- **Context** — anything relevant (it's the first meeting, a concern the manager raised, etc.)
- **Meeting frequency** — how often these happen

## Steps

1. Write an **Opening** — set expectations (low-pressure, confidential, not a check on their manager) and a warm, specific question showing you know their current work.
2. Write **Team Perspective** questions — 2-3 open-ended prompts about team dynamics and culture; instruct the reader to pick a couple, not interrogate.
3. Write **Career Development** questions — a broader conversation that complements (not replaces) their manager's coaching, including offering to watch for org-wide opportunities.
4. Write **Signal Questions** — the questions you're really there to ask (feedback timeliness, ease of getting unblocked, anything not reaching you through normal channels), phrased gently so the person isn't put in an uncomfortable position about their manager.
5. Write a **Close** — what they should expect from these meetings going forward, low-pressure, with an open door.
6. If the manager flagged something, add a private note-to-self: don't lead with it, let it surface naturally; if it doesn't, raise it with the manager as a coaching topic rather than investigating through the report.
7. Adapt to context: for a **first skip-level ever**, spend more time setting expectations and reassuring it's not a check on their manager. For **signals of manager issues**, remember consistent concerns across multiple skip-levels are a coaching conversation with the manager, not something to fix by going around them. For a **high performer**, add retention-risk questions ("are you learning, challenged, anything that'd make you consider leaving?"), asked warmly. For a **large org**, keep notes and look for cross-team themes (3 of 8 mentioning the same problem is an org issue).
8. Assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Skip-Level Prep — [Name] ([First Meeting / cadence])**

**Opening**
"[Expectation-setting + warm, specific question about their work]"

**Team Perspective** *(pick 2-3, don't interrogate)*
- "[Open-ended question]"

**Career Development**
- "[Broader career question]"

**Signal Questions** *(gently phrased)*
- "[Team-health question that doesn't corner them about their manager]"

**Close**
"[What to expect going forward; open door]"

*(Note to self: [how to handle any manager-raised concern])*
```

## Boundaries

- Never use a skip-level to undermine the middle manager, give directives that go around them, or create a shadow-management dynamic.
- Never invent the person's work, their manager's name, or context. Mark unknowns as **Unknown** and ask.
- Honour confidentiality: what's shared stays between you unless they ask you to act. Don't relay specifics back to the manager in a way that identifies the report.
- Surface manager concerns as coaching with that manager, not as an investigation conducted through their reports.
- Don't make promises about org-wide opportunities you can't keep.

## Chaining

- After this, offer **one-on-one-prep** to carry forward any career or development threads in your own 1:1s.
- For a recurring cross-team theme that emerges across several skip-levels, offer **team-health-survey-analysis** to test it more broadly.
