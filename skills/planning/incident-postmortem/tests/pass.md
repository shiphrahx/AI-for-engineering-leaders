# Postmortem: Duplicate Charges — 2026-06-10

## Summary
A retry without an idempotency key produced duplicate charges for a subset of EU
customers during a payment-provider slowdown.

## Impact
Roughly 1,200 customers were double-charged over 38 minutes. All charges were reversed
within 24 hours.

## Timeline
| Time | Event | Source |
|------|-------|--------|
| 09:02 | Provider latency rises | Alerting |
| 09:14 | Retries begin firing | Logs |
| 09:40 | Duplicate charges detected | Support |
| 09:52 | Retries disabled, incident contained | Slack |

## Root cause
A missing idempotency key allowed retried requests to create new charges instead of
being deduplicated. The slowdown was the trigger, not the cause.

## What went well
Detection from support signal was fast, and the rollback path was well understood.

## Remediation
- Add an idempotency key to all payment requests (owner: Alice, P0).
- Introduce a retry budget with backoff in the payment client (owner: Bo, P1).
