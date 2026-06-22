---
name: meeting-recap-action-items
description: >
  Produces a structured meeting recap from raw, messy notes — summary, numbered decisions with
  rationale, an action-items table (action / owner / due), open questions, and a parking lot.
  Use when the user says "turn these notes into a recap", "write up the meeting", "extract action
  items", or pastes half-sentence notes, transcript fragments, or scattered bullets after a
  meeting. Use this for documenting a meeting that already happened — not for planning a future
  meeting (use engineering-all-hands-agenda for agendas).
---

# Meeting Recap & Action Items

Extract the signal from messy meeting notes into a recap everyone can reference — decisions, action items with owners and dates, and open questions — ignoring social chat and tangents.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent attendees, owners, dates, or decisions. Mark unavailable owners as **[Unknown — needs assignment]** and unavailable dates as **TBD** rather than guessing.

- **Meeting name** and **date**
- **Attendees**
- **Purpose** — why the meeting was held
- **Raw notes** — in whatever state (half-sentences, bullets, transcript)

## Steps

1. Read the raw notes fully. Separate the signal (decisions, commitments, unresolved questions) from the noise (social chat, tangents) and discard the noise.
2. Write a **summary** (2-3 sentences) covering the purpose and the key outcome.
3. List **decisions made** as a numbered list, with rationale where the notes captured it. Extract implicit decisions ("we agreed to…", "decided:…") and distinguish actual decisions from suggestions that were never resolved.
4. Build the **action items** table: action, owner, due. If a date isn't explicit, mark **TBD**; if an owner isn't clear, mark **[Unknown — needs assignment]**. Anything someone committed to do is an action item.
5. List **open questions** — unresolved items needing follow-up, with brief context and who is investigating.
6. List the **parking lot** — topics raised but deliberately deferred, with the reason if known.
7. Adapt to context: for a **decision-heavy meeting**, expand each decision's rationale — this becomes the "why did we decide X?" reference. For a **brainstorm/ideation**, replace "Decisions" with "Key ideas discussed" and "Themes that emerged" — not every meeting produces decisions. For an **executive meeting**, shorten to decisions + actions only. For a **recurring sync**, add a "Status of previous action items" section at the top.
8. Assemble the output in the format below.

## Output format

```
**[Meeting Name] — Recap ([Date])**

**Summary:** [2-3 sentences: purpose and key outcome]

**Decisions**
1. **[Decision]** — [rationale if captured]

**Action Items**
| Action | Owner | Due |
|--------|-------|-----|
| [task] | [name or **[Unknown — needs assignment]**] | [date or **TBD**] |

**Open Questions**
- [question] (context; who is investigating)

**Parking Lot**
- [deferred topic] (why deferred, if known)
```

## Boundaries

- Never fabricate decisions, action items, owners, dates, or attendee names — mark owners **[Unknown — needs assignment]** and dates **TBD**.
- Never infer a deadline from organizational context (sprint cadence, etc.) the user didn't state.
- Never elevate an unresolved suggestion to a "decision" — if it wasn't agreed, it's an open question or parking lot.
- Never verify attendee names or spellings; surface them as written and let the user confirm.

## Chaining

- No natural successor — this is usually a terminal artifact. Action items it produces may feed a tracking tool, but the recap itself is the deliverable.
