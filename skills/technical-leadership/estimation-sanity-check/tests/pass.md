**Estimate Sanity Check: add SSO (SAML) to the admin app**

**Original:** "2 weeks", from the feature's engineer, gut-feel, happy-path only.

**Hidden / likely-omitted work**
- Test coverage for the auth flow — not in the number; must be written first.
- Migrating existing admin accounts to linked identities — not accounted for.
- Handling IdP edge cases (expired assertions, clock skew) — assumed away.
- Security review + rollout behind a flag — not counted.

**Assumptions that may not hold**
- Assumes our session layer is SAML-ready — the code shows it's tightly coupled to password login.
- Assumes the estimator does it uninterrupted — they're on-call week 2.

**Revised range**
- Best: 2.5 weeks · Likely: 4 weeks · Worst: 6 weeks
- Spread driven by: the session-layer coupling and account migration, both under-explored.

**Confidence: Low** — a 2-day spike on the session-layer change would raise it to Medium.

**Recommendation:** De-risk first — spike the session-layer integration before committing a date; then commit the likely case with a one-week buffer.
