# Internal Launch Announcement

## Situation

Your team shipped something. You want to tell the company in a way that gives credit to the team, explains why it matters to the business, and tells other teams what (if anything) they need to do.

## The Prompt

```
You are an engineering leader writing an internal company announcement about a feature, service, or system your team just shipped. The audience is the entire company — engineers, PMs, sales, support, execs. Make it celebratory but informative.

Structure:
1. **Headline** — one sentence that a salesperson could repeat to a customer
2. **What we shipped** — plain-language description of what changed for users/customers
3. **Why it matters** — business impact, metrics, or customer pain it solves
4. **How it works** (brief) — 2-3 sentences for the technically curious, skip jargon
5. **What this means for you** — actions for specific teams (sales: new talking point, support: updated docs, etc.)
6. **Team credit** — name everyone who contributed
7. **What's next** — what's coming in the next iteration

Context:
- What shipped: [FEATURE_DESCRIPTION]
- Business impact: [BUSINESS_IMPACT]
- Team members involved: [TEAM_MEMBERS]
- Relevant links: [LINKS]
```

## Example Input

```
- What shipped: Real-time order tracking for our e-commerce platform. Customers can now see live updates on their order status from purchase through delivery, including estimated arrival times that update dynamically based on carrier data.
- Business impact: #1 support request was "where's my order?" (38% of all tickets). This should significantly reduce that. Also a competitive feature — our top 3 competitors have had this for 6+ months.
- Team members: Lena (tech lead), Kai, Sofia, Marcel, Ines (backend), Tomás (frontend), Amir (design), Jun (QA)
- Links: internal demo video, support docs, Datadog dashboard
```

## Example Output

> **🚀 Shipped: Real-Time Order Tracking Is Live**
>
> Customers can now track their orders from purchase to doorstep with live status updates and dynamic delivery estimates.
>
> **What We Shipped**
> Every order now has a tracking page that updates in real time. Customers see where their order is, what stage it's in (processing → shipped → out for delivery → delivered), and an estimated arrival time that adjusts based on live carrier data. No more guessing, no more "where's my order?" emails.
>
> **Why This Matters**
> "Where's my order?" made up 38% of all support tickets last quarter. This directly addresses our highest-volume customer pain point and closes a competitive gap — our top three competitors have had this feature for 6+ months. We expect a measurable reduction in support ticket volume within the first two weeks.
>
> **How It Works**
> We built a carrier integration layer that polls for status updates and pushes them to a real-time event stream. The tracking page subscribes to that stream, so customers see updates within seconds of a status change. No page refresh needed.
>
> **What This Means For You**
> - **Sales:** "Real-time order tracking" is now a feature you can highlight in demos and proposals. [Link to one-pager]
> - **Support:** Updated help articles are live. You should see ticket volume on order status start to drop this week. [Link to docs]
> - **Product/Design:** Feedback channel is open — we want to hear what customers say in the first two weeks. Drop observations in #order-tracking-feedback.
>
> **Team Credit**
> Huge thanks to: Lena (tech lead and architecture), Kai, Sofia, Marcel, and Ines (backend and carrier integrations), Tomás (frontend tracking page), Amir (design), and Jun (QA — caught 23 edge cases before launch). This was a true full-stack team effort.
>
> **What's Next**
> - Proactive SMS/email notifications when status changes (next sprint)
> - Tracking page localisation for our EU markets (Q3)
> - Carrier-specific delivery windows with hourly precision (exploring)

## Tuning Notes

- **Infrastructure/invisible launch:** Skip the customer-impact framing. Lead with "what this unblocks for other teams" and internal metrics (latency, reliability, cost savings).
- **Sensitive launch (migration, deprecation):** Add a "what's changing for existing users" section and a clear migration timeline.
- **Slack announcement:** Compress to headline + 3-line summary + team credit + link to full write-up.
- **Exec audience only:** Lead with the metric ("38% ticket reduction expected"), then the feature in one line.
