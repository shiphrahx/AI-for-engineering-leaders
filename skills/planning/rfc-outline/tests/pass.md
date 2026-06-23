# RFC: Introduce a shared feature-flag service

## Problem
Each team ships its own flag logic, causing inconsistent rollout behaviour and no central
audit of what is enabled where.

## Proposal
Build a small feature-flag service with a typed SDK, central dashboard, and audit log.

## Trade-offs
The benefit is consistency, safer rollouts, and a single audit trail. The cost is the
added operational complexity of a new service and the risk of it becoming a hot dependency
on the request path.

## Open questions
- Do we evaluate flags in-process with a cached snapshot, or over the network per request?
- Who owns the service long term?

## Out of scope
Experimentation and A/B analysis — this RFC covers flagging only.
