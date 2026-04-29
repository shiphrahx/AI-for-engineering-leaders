# Customer Apology Email

## Situation

A customer-impacting incident has been resolved and you need to send a follow-up email to affected customers (or all customers). This email needs to rebuild trust — acknowledge what happened, take responsibility, and explain what you're doing to prevent recurrence. No corporate speak.

## The Prompt

```
You are an engineering leader drafting a customer apology email following an incident. Be direct, honest, and specific. Customers respect transparency far more than spin. Never blame a third party without context, never say "brief" if it wasn't brief, and always explain what you're doing to prevent it from happening again.

Structure:
1. **Subject line** — clear and honest, not alarming
2. **What happened** — plain language, customer-centric (what they experienced, not your internal details)
3. **Impact** — who was affected, for how long, and any data/financial implications
4. **What we've done** — immediate fix and longer-term preventive measures
5. **What this means for you** — any action the customer needs to take (if none, say so)
6. **Apology and commitment** — genuine, not boilerplate

Incident: [DESCRIBE_INCIDENT]
Customer impact: [DESCRIBE_IMPACT]
Remediation: [WHAT_YOU_DID_AND_WILL_DO]
Audience: [ALL_CUSTOMERS / AFFECTED_CUSTOMERS / ENTERPRISE_ACCOUNTS]
Tone: [FORMAL / CONVERSATIONAL]
```

## Example Input

```
Incident: Our payment processing was down for 47 minutes during peak hours. Customers couldn't complete purchases. Some customers were charged but didn't receive order confirmation — their orders were actually processed but the confirmation email was delayed by 3 hours.
Customer impact: ~2,300 customers attempted purchases during the window. ~180 saw errors. ~45 were charged without immediate confirmation.
Remediation: Fixed the underlying database issue, added auto-scaling, added earlier monitoring alerts, coordinating with team on load testing before marketing campaigns.
Audience: All customers (we don't know exactly who was affected vs who just saw the error)
Tone: Conversational (we're a B2C startup, our brand is approachable)
```

## Example Output

> **Subject: What happened on Tuesday — and what we're doing about it**
>
> Hi,
>
> On Tuesday afternoon, our payment system was down for 47 minutes between 2:13pm and 3:00pm GMT. If you tried to make a purchase during that window, you may have seen an error at checkout. We're sorry — that's not the experience you should have with us.
>
> **What happened**
> A surge in traffic overwhelmed part of our payment infrastructure. For 47 minutes, purchases couldn't be completed normally.
>
> **If you were charged but didn't get a confirmation:** Your order went through. Confirmation emails were delayed by up to 3 hours for some customers, but all orders placed during this period have been processed and are on their way. You don't need to do anything — but if your order looks wrong, reply to this email and we'll sort it out immediately.
>
> **If you saw an error and gave up:** We understand. Your cart is still saved if you'd like to come back and complete your purchase.
>
> **What we're doing to prevent this**
> We've already fixed the immediate issue and added safeguards so our systems scale automatically during traffic spikes. We've also added earlier warning alerts so our team is notified well before things reach a breaking point — not after.
>
> We know that reliability is earned, not promised. We take this seriously and we're investing in making sure it doesn't happen again.
>
> Sorry for the hassle, and thank you for your patience.
>
> [Name]
> [Title]

## Tuning Notes

- **Enterprise customers:** More formal tone. Add a timeline of events. Offer a call with the account team to discuss. Consider SLA credit language if applicable.
- **Data breach:** This template is NOT suitable for security incidents involving customer data. Those require legal review, may have regulatory notification requirements, and need a very different structure.
- **Recurring issue:** Don't pretend it's the first time. "We know this is the second time in [period] that [issue] has affected your experience. Here's what's different about our response this time: [specific new measures]."
- **No customer action needed:** State this explicitly. The most reassuring sentence in an incident email is "You don't need to do anything."
