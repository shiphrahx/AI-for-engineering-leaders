**SLO Definition: Checkout API**

**Service:** Handles checkout for all customers; revenue-critical.

**SLIs and SLOs**
| SLI | Definition | SLO Target | Window |
|-----|-----------|------------|--------|
| Availability | non-5xx / total | 99.9% | 30 days |
| Latency | p95 < 300ms | 99.0% | 30 days |

**Error Budget**
At 10M requests/month, 99.9% allows 10,000 failures/month (~333/day).

**Error Budget Policy**
- Budget > 50% remaining: normal development.
- Budget 25–50%: caution, review risky changes.
- Budget < 25%: reliability mode.
- Budget exhausted: leadership review and a reliability sprint.

**Measurement**
Availability from the load-balancer logs, excluding 4xx; latency from APM traces.

**Review Cadence:** Monthly, with target adjustment quarterly.
