---
name: kebab-name-matching-folder
description: >
  [What it produces — third person, e.g. "Produces a ..."]. [Trigger phrases a user
  would actually type — e.g. "Use when the user mentions X, asks for Y, or pastes Z"].
  Use this for [A], not [B or C] (disambiguation against near-neighbour skills in the
  same category).
---

# Skill Title

One sentence on the goal and the tone/framing discipline (e.g. blameless, evidence-led, headline-first, never speculative).

## Inputs to gather

List what the agent needs before acting. If any are missing, ask for them in a single batched question — never invent them. Mark unavailable fields as **Unknown** in the output, not guessed.

- [Input 1 — what it is, why it's needed]
- [Input 2]
- [Input 3]

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. [First action]
2. [Second action]
3. [Adapt for context — audience, scale, severity, etc.]
4. [Assemble the output in the format below]

## Output format

Show the exact structure expected — headers, tables, whatever applies.

```
**[Title] — [Date / Subject]**

**[Section]**
[Content]

**[Section]**
| Column | Column |
|--------|--------|
| ...    | ...    |
```

## Variants

_Optional._ If the skill tunes for org size, declare `variants: [startup, growth, enterprise]`
in the front-matter and add one bullet per stage here. See [`docs/VARIANTS.md`](docs/VARIANTS.md).
Omit this section entirely if the skill is stage-agnostic.

## Boundaries

What the skill must never do.

- Never fabricate inputs, metrics, names, or dates — mark them **Unknown**.
- [Domain-specific boundary, e.g. never name an individual as the cause]
- [Domain-specific boundary, e.g. never soften severity to look better]

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **[next-skill-name]** to [do the natural next thing].
