**Spike Readout: Postgres LISTEN/NOTIFY for job fan-out**

**Question:** Can one Postgres LISTEN/NOTIFY channel push jobs to 200 workers at peak rate without falling behind?
**Answer:** Inconclusive — it held at 2× peak in a 30-minute run, but connection churn crept up and we ran out of timebox before testing failover.

**What we did**
- One publisher, 50 fake workers on one channel, load generator at 2× peak for 30 minutes on staging.

**Evidence**
- Delivery lag stayed under 0.6s p99 at 2× peak. Open connections rose steadily — cause not yet isolated (Unknown). No failover test run.

**Recommendation:** One more spike — a 2-hour run at full worker count with connection-pool monitoring to settle the churn question before committing.

**Still open**
- Behaviour at 200 real workers, over a failover, and whether connection churn becomes a leak.

**Disposal:** Prototype thrown away. The load generator is worth keeping but needs a proper rebuild before reuse.
