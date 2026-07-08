**Checkout latency incident — Exec Summary**

**Bottom line:** Checkout was 40% slower for ~90 minutes on Tuesday, costing an estimated $18k in dropped carts; root cause is fixed and a guardrail ships Friday. No further action needed from you.

**What matters**
- Impact: 2,100 customers hit slow checkout; ~310 abandoned. Revenue exposure ~$18k, one-off.
- Cause: a cache config change bypassed the pricing cache under load — reverted in 12 minutes once detected.
- Detection gap: alert fired 25 minutes late. New latency alert lands Friday to close it.

**What's needed:** Nothing — FYI only. Full postmortem in the incident doc if you want the detail.
