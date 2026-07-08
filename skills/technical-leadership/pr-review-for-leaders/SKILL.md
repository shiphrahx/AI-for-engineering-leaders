---
name: pr-review-for-leaders
description: >
  Reviews a report's pull request with a leadership lens — correctness and design, but also
  scope creep, risk, mentoring feedback, and an explicit call on what to fix now versus delegate
  or teach. Produces prioritised review comments plus a short private coaching note for the
  author's growth. Use when the user says "review this PR for me", "my report opened this PR",
  "give feedback on this diff", or pastes a diff/PR link they need to respond to as the author's
  manager or tech lead. Use this for reviewing another engineer's code as their leader — use
  code-to-exec-translation to summarise a change upward, and incident-code-triage to read a
  failing code path under pressure.
---

# PR Review for Leaders

Review a report's pull request the way a good engineering leader does: catch the real correctness and design issues, but also weigh scope, risk, and what the author needs to learn — and decide deliberately what to fix in-line, what to delegate back, and what to let go. Feedback is specific, kind, and prioritised; the goal is a better engineer, not just a better diff.

## Inputs to gather

Gather these before reviewing. If any are missing, ask for them in a single batched question — never invent the author's seniority, the PR's intent, or facts about the codebase. Mark anything genuinely unavailable as **Unknown**.

- **The change** — the diff, PR link, or files (with enough surrounding context to judge correctness, not just the hunks)
- **Intent** — what the PR is supposed to do and the linked issue/ticket if any
- **Author** — seniority and your relationship (direct report, skip, peer), so feedback lands at the right level
- **Bar** — the merge bar for this repo/change (prototype vs production, hotfix vs feature) and any team conventions
- **Your time** — whether this is a deep review or a fast unblock, so the depth matches

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Read the PR intent first, then the diff in full with surrounding context. Never review hunks in isolation — a correct-looking change can break a caller off-screen.
2. Assess **correctness and design**: logic errors, edge cases, missing tests, security/secrets, data-loss or migration risk, and whether the approach fits the codebase. Flag the highest-impact issues first.
3. Separate **must-fix** (blocks merge: correctness, security, data risk) from **should-fix** (design, clarity, tests) from **optional** (style, preference). Label every comment with which it is — an unlabelled review reads as all-blocking.
4. Judge **scope**: is the PR doing more than its intent (drive-by refactors, unrelated changes)? Call scope creep out; suggest splitting rather than expanding review surface.
5. Apply the **delegate-vs-fix** call: for a junior author, teach the pattern and let them fix it (link the principle, don't rewrite it for them); for a senior author, be terse and trust judgement; for a hotfix, fix forward and note follow-ups. Never silently rewrite a report's code when the lesson is the point.
6. Write **review comments** as `path:line — [must-fix/should-fix/optional] problem, then the fix or question`. Ask questions where intent is unclear rather than asserting. Note at least one thing done well — specific, not flattery.
7. Write a short **coaching note** (private, for the user as manager): the one pattern worth reinforcing or correcting with this author over time, and whether this PR is a teaching moment, a delegation opportunity, or just a merge.
8. Give a clear **verdict**: approve, approve-with-nits, or request-changes — with the single reason.
9. Assemble the output in the format below.

## Output format

```
**PR Review: [title / link]** — Verdict: [Approve / Approve with nits / Request changes]

_[One-line reason for the verdict.]_

**Must-fix**
- `path:line` — [problem]. [Fix or question.]

**Should-fix**
- `path:line` — [problem]. [Fix or question.]

**Optional**
- `path:line` — [suggestion].

**Done well**
- [Specific, genuine — a good decision, test, or clarity.]

**Coaching note (private)**
[One pattern to reinforce/correct with this author, and whether to fix, delegate, or teach here.]
```

## Boundaries

What the skill must never do.

- Never invent code behaviour, callers, or test results you haven't seen — if context is missing, ask or mark **Unknown**, don't assume.
- Never let every comment read as blocking — label severity or the author can't prioritise.
- Never rewrite a junior's code wholesale when the learning is the point — teach the fix instead.
- Never soften a real correctness, security, or data-loss issue to spare feelings — say it plainly, kindly.
- Never expand scope in review ("while you're here, also…") — flag it as a separate follow-up.
- Keep the coaching note private to the manager — it is about the author's growth, not a public comment.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **code-to-exec-translation** when the merged change needs summarising upward to stakeholders or leadership.
- After this, offer **feedback-synthesis** when the coaching notes across several PRs should roll into structured performance feedback.
