---
name: ai-coding-guidelines
description: >
  Drafts a team's norms for AI-assisted coding — tool-neutral across any assistant — covering
  when to use it and when not to, the review and verification bar, secrets and data handling,
  security, licensing/attribution, and accountability for merged code. Use when the user says
  "write our AI coding policy", "team guidelines for using coding assistants", "how should my
  team use AI to code", or wants norms now that reports code with AI tools. Use this to set team
  norms for AI-assisted development — use pr-review-for-leaders to apply the bar to one PR, and
  build-vs-buy-analysis to choose a specific tool.
variants: [startup, growth, enterprise]
---

# AI Coding Guidelines

Draft clear, tool-neutral team norms for coding with AI assistants — enabling, not banning — so engineers move faster while the team keeps its bar on review, security, and accountability. The guidelines apply to any assistant (Claude, Codex, Copilot, Cursor, or whatever comes next); they set principles, not tool-specific rules.

## Inputs to gather

Gather these before drafting. If any are missing, ask for them in a single batched question — never invent the team's risk posture, existing policy, or regulatory constraints. Mark anything genuinely unavailable as **Unknown**.

- **Team & context** — team size, domain, and how experienced they are with AI tools already
- **Risk posture** — data sensitivity, regulatory constraints (PII, health, finance), and whether code is proprietary or open
- **Current practice** — what tools people already use and any existing policy to align with or replace
- **Non-negotiables** — hard limits from security, legal, or compliance (e.g. no source in third-party tools, approved-vendor list)
- **Goal** — what the team wants more of (speed, consistency, learning) and what problem prompted writing this now

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Open with a short **stance**: AI assistants are encouraged for the right work; the engineer who merges the code owns it. Set the tone as enabling with clear accountability, not restrictive.
2. Define **when to use / when to be careful**: good fits (boilerplate, tests, refactors, unfamiliar syntax, exploration) vs situations demanding extra scrutiny (security-critical paths, cryptography, auth, novel algorithms, regulated data).
3. Set the **review and verification bar**: AI-generated code is reviewed to the same standard as any code; the author must understand every line they submit; generated code is run and tested, never merged on faith. "The AI wrote it" is never an excuse for a defect.
4. State **secrets and data handling**: what must never be pasted into a tool (secrets, keys, customer/PII data, proprietary source if disallowed) and which tools/settings are approved for what — anchored to the team's non-negotiables.
5. Cover **security**: treat generated code as untrusted input — check for injected vulnerabilities, insecure defaults, and outdated/hallucinated dependencies; do not add a package an assistant invented without verifying it exists and is sound.
6. Cover **licensing and attribution**: risk of generated code resembling licensed sources, how the team handles attribution or disclosure, and any provenance requirements.
7. Fix **accountability**: the submitting engineer is responsible for correctness, security, and licensing regardless of how the code was produced. State how (if at all) AI assistance is disclosed in commits/PRs.
8. Adapt to context (see Variants) and keep it to one page a busy engineer will actually read — principles over exhaustive rules.
9. Assemble the output in the format below.
10. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Team/Org] — AI-Assisted Coding Guidelines**

**Stance:** [Enabling; the engineer who merges owns the code.]

**When to use / when to be careful**
- Good fit: [...]
- Extra scrutiny: [...]

**Review & verification bar**
- [Same review standard; author understands every line; code is run and tested.]

**Secrets & data**
- Never paste: [secrets, keys, PII, disallowed source]
- Approved tools/settings: [...]

**Security**
- [Treat generated code as untrusted; verify dependencies exist and are sound.]

**Licensing & attribution**
- [Provenance / disclosure handling.]

**Accountability**
- [Submitter owns correctness, security, licensing. Disclosure in commits/PRs: [how].]
```

## Variants

Optional org-size tuning (see [`docs/VARIANTS.md`](../../../docs/VARIANTS.md)). Default to **growth** if the user doesn't state a stage.

- **startup** (≤ ~15 engineers): keep it to the stance, the verification bar, and the secrets rule — lightweight, principle-first, trust-heavy.
- **growth** (~15–80): the full one-pager above, with named approved tools and a clear review bar.
- **enterprise** (80+): add the approved-vendor list, data-classification mapping (what class of data may touch which tool), compliance/audit references, and a named owner for keeping the policy current.

## Boundaries

What the skill must never do.

- Never write a tool-specific policy when the team uses several — keep it neutral across assistants.
- Never invent regulatory or legal constraints — mark them **Unknown** and flag that legal/security should confirm.
- Never frame the policy as a ban — the goal is safe enablement, not prohibition.
- Never let "the AI wrote it" stand as an excuse — accountability always lands on the submitting engineer.
- Never present these as legal advice — recommend legal/compliance review for licensing and regulated-data clauses.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **pr-review-for-leaders** to apply the review-and-verification bar to an actual pull request.
- After this, offer **team-values-workshop** when the guidelines should be shaped with the team rather than handed down.
