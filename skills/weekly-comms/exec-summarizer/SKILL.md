---
name: exec-summarizer
description: >
  Compresses any dense technical material — a postmortem, RFC, design doc, long Slack/email
  thread, dashboard dump, or vendor report — into a headline-first executive summary: bottom
  line up front, the few points that actually matter, and what (if anything) is needed from the
  reader. Use when the user says "summarize this for my VP/CTO", "TL;DR this", "make this exec-
  ready", "too long, cut it down", or pastes a wall of technical text. Use this to compress an
  existing artifact of any shape — use exec-status-update for a structured weekly team status,
  and board-engineering-summary for an investor-level board section.
---

# Exec Summarizer

Turn dense technical material into a summary a busy, sophisticated executive reads in under a minute — leading with the conclusion, keeping only what changes a decision, and stripping every word that does not earn its place. Substance stays; overhead dies.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent facts, numbers, or a conclusion the source doesn't support. Mark anything genuinely unavailable as **Unknown**.

- **Source material** — the text to compress (paste it in full; summarize what's given, don't guess at what's cut off)
- **Reader** — recipient's role (manager, VP, CTO, board) and what they act on (timelines, cost, customer/revenue impact, risk)
- **The ask** — why they're reading this: a decision to make, a heads-up, or a status check. Shapes what the summary must foreground.
- **Length ceiling** — target word count if the reader has one (default: keep it tight, well under 250 words)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Read the entire source before writing a word. Identify the single most consequential fact — the conclusion, result, recommendation, or number the reader would want if they read nothing else.
2. Write the **bottom line** first: 1–2 sentences stating what happened, why it matters, or what to do. If a reader stops here, they must still have the answer. No preamble, no "this document describes", no scene-setting.
3. Select **only the points that change a decision** — impact, cost, risk, timeline, the number that moved. Cut methodology, chronology, caveats, and background unless omitting them would mislead. Order most-consequential first, never chronologically.
4. State **what's needed** from the reader — a decision, an approval, an FYI — with a recommendation attached. If nothing is needed, say so explicitly ("Nothing — FYI only") so they don't hunt for a hidden ask.
5. Translate or delete jargon the reader can't act on ("serialisation rewrite" → "backend change to cut response times"). Keep technical precision only where the reader's decision depends on it.
6. Cut throat-clearing, hedging, and filler: no "as you know", "it's worth noting", "in order to", "basically". Prefer short words and short sentences. Skeptical, forward-looking voice — say what's true and what happens next, not what's comfortable.
7. Adapt to context: for a **board/C-suite** reader, lead with the metric tied to a company goal and drop all implementation detail; for a **decision ask**, put the recommendation in the bottom line; for a **bad-news** source, state the problem and impact first — never bury it under wins.
8. Assemble the output in the format below, respecting the length ceiling.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Subject] — Exec Summary**

**Bottom line:** [1–2 sentences — the conclusion, result, or recommendation. Answer first.]

**What matters**
- [Most consequential point — impact / number / risk / cost, not method]
- [Next most consequential]
- [...]

**What's needed:** [Decision or approval + your recommendation, or "Nothing — FYI only".]
```

## Boundaries

What the skill must never do.

- Never fabricate a fact, number, name, date, or conclusion the source doesn't support — mark gaps **Unknown** rather than smoothing them over.
- Never overstate confidence the source doesn't have — if the material is uncertain, the summary says so in one clause, not five.
- Never bury bad news, a risk, or the ask below softer content — the reader must hit it in the first two lines.
- Never pad to look thorough — length is a cost, not a virtue; if it fits in three sentences, stop at three.
- Never preserve jargon the reader can't act on — translate it or cut it.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **exec-status-update** when the compressed material is a recurring team status that should follow the standard weekly structure.
- After this, offer **board-engineering-summary** when the reader is the board and the summary needs investor framing.
