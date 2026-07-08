**Spike: Postgres LISTEN/NOTIFY for job fan-out** — Timebox: 2 days

**Question:** Can a single Postgres LISTEN/NOTIFY channel push jobs to 200 workers at our peak rate without falling behind?

**Decision it unblocks:** Whether we adopt Postgres for the queue or bring in a dedicated broker — feeds the build-vs-buy call next sprint.

**Build (smallest thing)**
- One publisher, N fake workers subscribed to one channel, a load generator at 2× peak rate.
- Skip / fake: auth, retries, dead-letter handling, real job payloads, any UI.

**Success / kill criteria**
- ✅ Proceed if: workers stay under 1s p99 delivery lag at 2× peak for 30 minutes.
- ❌ Stop if: lag grows unbounded or notifications drop under load.
- 🤔 Inconclusive → next smallest spike: test with real payload sizes only.

**Disposal:** Thrown away. Any part that might survive → the load generator could be reused for the real broker test: needs proper rebuild.

**Will NOT tell us:** Behaviour across a failover, long-term connection churn, or cost at full production scale.
