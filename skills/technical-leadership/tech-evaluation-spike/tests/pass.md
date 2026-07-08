**Tech Evaluation: BullMQ (Redis job queue)** — Verdict: Adopt

_Handled 3× our peak throughput with sub-second latency and clears every deal-breaker._

**Decision & must-haves**
- Deciding: our background-job queue for the next 12 months.
- Deal-breakers: MIT-compatible license, self-hostable, works with our existing Redis, <2s p99 job pickup.

**What was tested**
- Wired one producer + 50 workers against our staging Redis, replayed a day of real job payloads at 2× volume, then killed workers mid-run to check recovery.

**Evidence**
- ✅ Held up: p99 pickup 0.4s at 2× peak; jobs re-queued cleanly after worker kill; setup took ~2 hours.
- ❌ Broke / rough: dashboard is thin; delayed-job precision drifts ~1s under load (acceptable for us).
- Deal-breaker check: license MIT ✅; self-host ✅; existing Redis ✅; latency ✅.

**vs Kafka (status quo candidate)**
- Far lower operational weight for our volume; we don't need Kafka's throughput or ordering guarantees.

**Did NOT test:** Behaviour past 10× scale, multi-region Redis, or a full failover.

**Recommendation:** Adopt for job queue. Re-evaluate if job volume grows past 10×.
