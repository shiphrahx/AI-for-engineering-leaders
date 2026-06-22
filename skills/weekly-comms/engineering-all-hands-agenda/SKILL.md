---
name: engineering-all-hands-agenda
description: >
  Produces a tight engineering all-hands agenda — a timed table (time / item / owner / format /
  one-line goal), draftable opening remarks to set the tone, and facilitator notes — built so every
  item justifies being live and synchronous, with reserved open Q&A. Use when the user says "plan
  my all-hands", "draft an all-hands agenda", "engineering town hall agenda", or gives topics,
  duration, and audience. Use this for planning a future synchronous meeting — use
  meeting-recap-action-items to write up a meeting that already happened.
---

# Engineering All-Hands Agenda

Build a tight all-hands agenda that respects everyone's time and never devolves into a status meeting that should have been an email — every segment must answer "why does this need to be live and synchronous?"

## Inputs to gather

Gather these before drafting. If any are missing, ask for them in a single batched question — never invent topics, owners, or duration. Mark anything genuinely unavailable as **Unknown** in the output.

- **Audience** — org name, headcount, and format (remote / hybrid / in-person)
- **Frequency** — quarterly / monthly
- **Duration** — total time available
- **Key topics** — the topics to cover
- **Tone to set** — e.g. energising after a hard quarter, celebratory, refocusing after a reorg

## Steps

1. For each proposed topic, apply the test: does this need to be live and synchronous, or could it be an email? Cut or compress pure status updates; keep demos, decisions, structural changes, and anything needing real-time reaction.
2. Draft **opening remarks** (2-3 sentences) the leader can use to set the tone — what the meeting is for and what people should leave with. Match the requested tone honestly (don't sugarcoat a hard quarter).
3. Build the **agenda table**: for each item give a time allocation (running clock), item, owner, format (present / discuss / Q&A / demo), and a one-line goal for the segment.
4. Keep total time within the stated duration and reserve **at least 10 minutes for open Q&A**.
5. Prefer **demo over tell** for shipped work, and pair structural/announcement items with built-in Q&A time.
6. Add **facilitator notes**: seed Q&A with 1-2 anticipated hard questions in case the room goes quiet; open a Slack channel for async questions from remote attendees; share data-heavy slides (e.g. OKRs) in advance so live time isn't spent reading numbers.
7. Adapt to context: **monthly cadence** — drop the OKR review, tighten to 30-45 min, focus on one highlight demo and one change to communicate. **Post-reorg** — give the structural change ~15 min including Q&A; people need to process. **Large org (100+)** — pre-collect questions via a form and designate a co-host to monitor chat. **Low-energy team** — open with wins, even brief, before any bad news.
8. Assemble the output in the format below.

## Output format

```
**[Org] All-Hands — [Period]**
*[Duration] | [Remote/Hybrid/In-person]*

---

**Opening remarks** *([N] min — [Owner])*
"[2-3 sentences setting tone: what this is for, what to leave with, Q&A invitation.]"

---

| Time | Item | Owner | Format | Goal |
|------|------|-------|--------|------|
| 0:00 | [item] | [owner] | [present/discuss/Q&A/demo] | [one-line goal] |
| ...  | Open Q&A | All | Q&A | [goal] |
| ...  | Close | [owner] | Present | [one sentence on what you need from the team] |

---

**Facilitator notes**
- [Seed Q&A / async channel / pre-share slides / etc.]
```

## Boundaries

- Never fabricate topics, owners, or duration — mark anything unavailable as **Unknown**.
- Never include a pure status item that could be an email; every segment must justify being synchronous.
- Never cut open Q&A below 10 minutes.
- Never sugarcoat the tone the user asked for — if the quarter was hard, the opening remarks say so honestly.
- Never overrun the stated total duration — the running clock must add up.

## Chaining

- No natural successor — this is usually a terminal artifact. After the meeting runs, **meeting-recap-action-items** can write up decisions and follow-ups.
