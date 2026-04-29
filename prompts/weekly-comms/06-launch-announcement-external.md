# External Launch Announcement

## Situation

You need to draft customer-facing or public communications for a release. This might be a changelog entry, a blog post draft, or a customer email. The audience doesn't care about your architecture — they care about what's better for them now.

## The Prompt

```
You are an engineering leader drafting an external announcement for customers or the public about a new feature or improvement. The writing should be clear, benefit-focused, and free of internal jargon. No one outside your company cares about your tech stack.

Structure:
1. **Headline** — what the customer can now do (not what you built)
2. **The problem this solves** — in the customer's words
3. **What's new** — plain description of the change
4. **How to use it** — 2-3 steps to get started
5. **What's coming next** — tease the roadmap without overcommitting

Format: [BLOG_POST / CHANGELOG_ENTRY / CUSTOMER_EMAIL / SOCIAL_POST]
Audience: [AUDIENCE_DESCRIPTION]
Tone: [PROFESSIONAL / CASUAL / TECHNICAL]

Feature details:
[PASTE_FEATURE_DETAILS]

Customer problem it solves:
[PASTE_CUSTOMER_PROBLEM]
```

## Example Input

```
Format: Changelog entry
Audience: SaaS users, mostly technical PMs and developers
Tone: Casual but informative

Feature details: Added webhook retry logic with exponential backoff. Failed webhooks now retry up to 5 times over 24 hours. Users can see retry status and manually re-trigger from the dashboard. Also added webhook delivery logs with payload inspection.

Customer problem: Users have been losing webhook events when their endpoints are temporarily down. They've asked for retries and better visibility into delivery status.
```

## Example Output

> **Webhook retries and delivery logs are here**
>
> Missed webhooks because your endpoint was briefly down? That shouldn't mean lost data. Starting today, failed webhook deliveries automatically retry up to 5 times over 24 hours with exponential backoff.
>
> **What's new:**
> - **Automatic retries** — failed deliveries retry 5 times over 24 hours. No configuration needed.
> - **Delivery logs** — see the full delivery history for every webhook, including payload, response code, and timing.
> - **Manual re-trigger** — spot a failed delivery? Hit "Retry" from the dashboard to resend it instantly.
>
> **Get started:** Head to Settings → Webhooks. Retries are on by default for all existing endpoints. Check the new "Delivery Log" tab to see your webhook history.
>
> **Coming soon:** Webhook filtering (subscribe to specific event types only) and Slack notifications for repeated delivery failures.

## Tuning Notes

- **Blog post format:** Expand the "problem" section into a narrative. Add a technical aside for developer audiences explaining the backoff strategy.
- **Enterprise audience:** Emphasise reliability and compliance. Add SLA language if applicable.
- **Social post:** Compress to one sentence + key benefit. "Webhooks now auto-retry up to 5x. No more lost events when your endpoint blips. Details →"
- **Breaking change:** Lead with "what's changing" and add a migration section before "how to use it."
