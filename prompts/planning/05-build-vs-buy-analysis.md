# Build vs Buy Analysis

## Situation

Someone wants to adopt a vendor solution. Or your team wants to build something in-house that has commercial alternatives. You need a structured analysis that accounts for total cost of ownership, not just sticker price or initial build effort.

## The Prompt

```
You are an engineering leader evaluating whether to build a capability in-house or buy/adopt a vendor solution. Produce a balanced analysis that considers total cost of ownership over 2 years, engineering opportunity cost, operational burden, and strategic fit. Avoid bias — lay out the trade-offs honestly.

Structure:
1. **Decision summary** — what capability, why now, and your recommendation (stated upfront)
2. **Build option** — estimated effort, ongoing maintenance, team expertise required, advantages
3. **Buy option(s)** — vendor(s) evaluated, pricing, integration effort, limitations, advantages
4. **Comparison matrix** — side-by-side on key dimensions
5. **Hidden costs** — things both options underestimate
6. **Recommendation** — which option and why, with conditions that would reverse the decision

Capability needed: [WHAT_YOU_NEED]
Business context: [WHY_NOW]
Vendors evaluated: [VENDOR_LIST]
Team context: [TEAM_SKILLS_AND_CAPACITY]
```

## Example Input

```
Capability: Feature flagging system — ability to roll out features gradually, run A/B tests, and kill-switch in production
Business context: Currently deploying features to 100% of users simultaneously. Last month a bug in the checkout flow affected all users for 40 minutes. Product wants to run A/B tests for pricing experiments.
Vendors evaluated: LaunchDarkly, Unleash (open source, self-hosted), Flagsmith
Team context: 40 engineers, platform team of 4 could build it, moderate experience with Redis and config management. Current monthly cloud spend is $85K.
```

## Example Output

> **Feature Flagging: Build vs Buy Analysis**
>
> **Recommendation:** Buy (LaunchDarkly) for immediate needs, with a review in 12 months as usage patterns stabilise. The build option is viable but the opportunity cost of the platform team's time outweighs the licensing cost at our scale.
>
> **Build Option**
> - *Effort:* 6-8 weeks for MVP (flag evaluation, percentage rollout, kill switch). Additional 4-6 weeks for A/B testing, audit logging, and UI.
> - *Ongoing maintenance:* ~20% of one platform engineer's time for bug fixes, feature requests, and scaling
> - *Advantages:* Full control over data, no per-seat licensing, can integrate deeply with our deployment pipeline, no vendor dependency
> - *Risks:* Platform team is also tasked with CI/CD improvements this quarter — building flags means deferring that work
>
> **Buy Options**
> | | LaunchDarkly | Unleash (self-hosted) | Flagsmith |
> |---|---|---|---|
> | Cost (annual) | ~$36K (40 seats) | Free (OSS) + hosting ~$6K/yr | ~$18K (40 seats) |
> | Integration effort | 1-2 weeks | 2-3 weeks (+ ops overhead) | 1-2 weeks |
> | A/B testing | Built-in | Plugin/limited | Built-in |
> | Audit logging | Yes | Yes | Yes |
> | SDK quality | Excellent | Good | Good |
> | Self-hosted option | Enterprise tier | Default | Available |
>
> **Comparison Matrix**
> | Dimension | Build | LaunchDarkly | Unleash | Flagsmith |
> |-----------|-------|--------------|---------|-----------|
> | Time to first flag | 6-8 weeks | 1-2 weeks | 2-3 weeks | 1-2 weeks |
> | 2-year total cost | ~$120K (eng time) | ~$72K (license) | ~$50K (ops + eng) | ~$36K (license) |
> | Maintenance burden | Medium-high | Low | Medium | Low |
> | Customisation | Unlimited | Limited | High (OSS) | Moderate |
> | Vendor risk | None | Medium | Low (OSS) | Medium |
> | Opportunity cost | High (platform team blocked) | Low | Low-medium | Low |
>
> **Hidden Costs**
> - *Build:* Edge cases in flag evaluation (percentage bucketing consistency, flag dependencies) are deceptively complex. Most internal systems underinvest in the management UI, creating a support burden on the platform team.
> - *Buy:* Per-seat pricing scales with headcount. At 100 engineers, LaunchDarkly's cost roughly doubles. Vendor SDK lock-in means migration away is a multi-week project.
>
> **Recommendation: LaunchDarkly**
> The 6-8 week build time has high opportunity cost — the platform team's CI/CD work is already committed. LaunchDarkly gets us to first value in under 2 weeks at a cost ($36K/yr) that's well below the engineering cost of building. Revisit in 12 months if: (a) seat costs exceed $60K/yr, or (b) we need custom flag evaluation logic that the vendor can't support.

## Tuning Notes

- **Cost-sensitive startup:** Weight the comparison toward cash cost. Engineering time is expensive but doesn't hit the P&L the same way. Highlight the open-source option more prominently.
- **Enterprise/regulated environment:** Add a "Compliance & Security" dimension to the matrix. Data residency, SOC 2, and audit requirements often eliminate options quickly.
- **Strong internal platform team:** If the team has capacity and this aligns with their charter, build is more attractive. Factor in team morale — platform engineers often prefer building to integrating.
- **Presenting to non-technical stakeholders:** Drop the SDK quality and technical implementation details. Lead with cost, time-to-value, and risk.
