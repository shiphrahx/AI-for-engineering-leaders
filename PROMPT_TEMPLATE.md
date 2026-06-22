# Prompt Template

Copy this file when creating a new prompt. Fill in every section.

---

# [Prompt Title]

## Situation

_When would an engineering leader reach for this prompt? Be specific about the trigger moment._

## The Prompt

```
[Paste the full prompt here, with [PLACEHOLDERS] for variable content]
```

**Placeholder convention:**
- Use `[SNAKE_CASE]` for free-form fill-ins the user replaces with their own content — e.g. `[TEAM_NAME]`, `[PASTE_RAW_UPDATES]`. Keep tokens to letters, digits, and underscores (no apostrophes or punctuation).
- Use a slash-separated enum for a fixed choice — e.g. `[PROFESSIONAL / CASUAL / TECHNICAL]`.
- Put illustrative guidance after `e.g.` inside the brackets when an example helps — e.g. `[COMPANY_STAGE, e.g. Series B, pre-IPO]`.
- Keep the field name in the prompt, the placeholder token, and the Example Input label consistent so users can map them 1:1.

## Example Input

_Show a realistic input that someone would paste into the placeholder fields. Use fictional but plausible data._

```
[Example data here]
```

## Example Output

_Show what the AI produces with the example input above. This helps users calibrate their expectations._

> [Example output here]

## Tuning Notes

_Write 3-5 context-specific tuning notes — the situations where someone would adapt this prompt, each with a bold lead-in label. The four dimensions below are a useful starting checklist, but use whatever labels fit the prompt; not every dimension applies to every prompt._

- **Audience shift:** [How to adjust when the audience changes]
- **Tone shift:** [How to adjust for urgency, formality, or bad news]
- **Scale shift:** [How this changes for startups vs. large orgs]
- **Common pitfall:** [What to watch out for in the output]
