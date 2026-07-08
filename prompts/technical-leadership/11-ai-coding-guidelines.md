# AI Coding Guidelines

## Situation

Your team codes with AI assistants and you need clear norms — enabling, not banning — covering when to use them, the review and verification bar, secrets, security, licensing, and who's accountable for the merged code. You want it tool-neutral, so it survives whatever assistant the team uses next.

## The Prompt

```
You are drafting a team's norms for AI-assisted coding. Tool-neutral (any assistant), enabling not restrictive, with clear accountability. Keep it to a one-pager a busy engineer will actually read. Recommend legal/security review for licensing and regulated-data clauses; don't present it as legal advice.

Cover:
1. Stance — AI assistants encouraged; the engineer who merges owns the code.
2. When to use / when to be careful — good fits (boilerplate, tests, refactors, unfamiliar syntax) vs extra scrutiny (security-critical, crypto, auth, novel algorithms, regulated data).
3. Review & verification bar — same review standard as any code; author understands every line; generated code is run and tested, never merged on faith.
4. Secrets & data — what must never be pasted into a tool; which tools/settings are approved.
5. Security — treat generated code as untrusted; verify dependencies exist and are sound (no hallucinated packages).
6. Licensing & attribution — provenance/disclosure handling.
7. Accountability — the submitting engineer is responsible regardless; "the AI wrote it" is never an excuse. Disclosure in commits/PRs: [how].

Team & context: [SIZE_DOMAIN_EXPERIENCE]
Risk posture: [DATA_SENSITIVITY_REGULATION_PROPRIETARY_OR_OPEN]
Current practice: [TOOLS_ALREADY_USED_AND_EXISTING_POLICY]
Non-negotiables: [HARD_LIMITS_FROM_SECURITY_LEGAL]
```

## Example Input

```
Team & context: 25 engineers, B2B SaaS, mixed experience with AI tools.
Risk posture: Store customer PII; SOC 2. Proprietary source.
Current practice: People use Copilot and Claude ad hoc; no policy.
Non-negotiables: No customer data or secrets in third-party tools; only enterprise-plan tools with training opt-out.
```

## Example Output

> **Engineering — AI-Assisted Coding Guidelines**
>
> **Stance:** AI assistants are encouraged. The engineer who merges the code owns it — correctness, security, and licensing.
>
> **When to use / when to be careful**
> - Good fit: boilerplate, tests, refactors, unfamiliar syntax, exploring an API.
> - Extra scrutiny: auth, crypto, anything touching customer PII, novel algorithms.
>
> **Review & verification bar:** AI-generated code is reviewed to the same standard as any code. You must understand every line you submit and must run and test it — never merge on faith.
>
> **Secrets & data:** Never paste secrets, keys, or customer PII into any tool. Only enterprise-plan assistants with training opt-out are approved.
>
> **Security:** Treat generated code as untrusted — check for insecure defaults and verify any suggested dependency actually exists and is maintained before adding it.
>
> **Licensing & attribution:** Flag anything that looks copied from a licensed source; legal confirms provenance handling.
>
> **Accountability:** The submitting engineer is responsible regardless of how the code was produced. "The AI wrote it" is never an excuse for a defect. Disclose AI assistance if a reviewer asks.
>
> _Legal and security should review the data and licensing clauses._

## Tuning Notes

- **Tool-neutral:** Keep it about principles, not one vendor's product — the policy should hold when the team switches assistants.
- **Scale shift:** At a startup, trim to stance + verification bar + secrets rule. At enterprise, add an approved-vendor list, data-classification mapping, and a named policy owner.
- **Common pitfall:** The model may write a ban ("don't use AI for X") instead of safe enablement. Steer it back to "use it, here's the bar."
- **Accountability is the anchor:** The one non-negotiable line — the human who merges owns it. Don't let it get softened.
