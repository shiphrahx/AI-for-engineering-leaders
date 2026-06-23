# Org-Size Variants

Engineering-leadership advice rarely fits every company stage. A capacity plan for a
five-person startup and a 200-engineer org differ in defaults, rigour, and tone. Rather
than fork a skill per stage, skills carry **variants** inline.

This keeps the pack DRY and fully LLM-agnostic — the variant guidance is plain prose the
agent reads and applies; no runtime feature or provider API is involved.

## The convention

A skill MAY declare which stages it tunes for in its front-matter:

```yaml
---
name: capacity-planning
description: >
  ...
variants: [startup, growth, enterprise]
---
```

A skill MAY then add an optional `## Variants` section (placed after `## Output format`,
before `## Boundaries`) with one bullet per stage:

```markdown
## Variants

- **startup** (≤ ~15 engineers): [what to simplify, which steps to skip, lighter defaults]
- **growth** (~15–80): [the default assumptions the skill already makes]
- **enterprise** (80+): [extra rigour — RACI, cross-org dependencies, formal sign-off]
```

## Stage definitions

| Stage | Rough size | Posture |
|-------|-----------|---------|
| `startup` | ≤ ~15 engineers | Speed over process; one page; explicit "not doing" |
| `growth` | ~15–80 engineers | Balanced; the pack's default assumptions |
| `enterprise` | 80+ engineers | Formal: dependencies, approvals, audit trails |

## How an agent selects a variant

1. If the user states their org size or stage, map it to the nearest stage above.
2. Otherwise default to `growth` (the pack's baseline) and state the assumption.
3. Apply the matching `## Variants` bullet on top of the normal Steps.

## Backward compatibility

Both the `variants:` key and the `## Variants` section are **optional**. Skills without
them behave exactly as before and pass the linter unchanged. See
[`capacity-planning`](../skills/planning/capacity-planning/SKILL.md) for a worked example.
