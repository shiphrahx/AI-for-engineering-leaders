**Escalation Policy**

**Tier 1: On-Call Engineer**
- *Contact:* PagerDuty, auto-escalates after 5 minutes.
- *Authority:* restarts, scaling, rollbacks.
- *Escalate to Tier 2 when:* customer impact confirmed or no fix in 15 minutes.

**Tier 2: IC + Tech Lead**
- *Authority:* declare war room, emergency deploys.
- *Escalate to Tier 3 when:* multi-team or > 30 minutes.

**Tier 3: Engineering Manager**
- *Authority:* customer comms, spend up to £5k.

**Tier 4: VP Eng / CTO**
- *Authority:* all decisions, legal/PR/public statements.

**Cross-Team Escalation**
| Service | On-Call Team | PagerDuty Service | Slack Channel |
|---------|--------------|-------------------|---------------|
| Payments | Payments | pd-payments | #payments-oncall |

**After-Hours Policy**
- P0/P1: unchanged. P2: assess, deferrable. P3: next business day.
