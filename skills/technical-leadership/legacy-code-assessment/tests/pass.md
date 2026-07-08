**Legacy Assessment: billing-exporter service** — Verdict: Leave

_It's stable, rarely touched, and a rewrite would risk revenue reporting for no real gain today._

**Cost of ownership now**
- Change frequency / difficulty: touched ~twice a year; changes are awkward but rare.
- Incidents / time lost: zero incidents in 18 months; ~1 engineer-day/year of maintenance.

**Business role & blast radius**
- Feeds finance's monthly revenue report. Wrong output is high-cost, but the code has been correct for years.

**Changeability**
- Tests: thin but the output is reconciled monthly by finance. Coupling: low, single entry point. Understanding: one engineer knows it well.

**The three paths**
| Path | Cost | Risk | Notes |
|------|------|------|-------|
| Invest | ~2 weeks to add tests | Low | Marginal — it rarely changes |
| Rewrite | ~6 weeks + parallel-run | High | Risks revenue reporting for no functional gain |
| Leave | 0 | Accept: bus-factor of 1 | Document it; keep the reconciliation check |

**Verdict:** Leave — stable, low-change, high-cost-to-touch. Add light documentation to reduce bus-factor risk.
**Trigger to reassess:** If we adopt multi-currency billing or the sole owner leaves, reassess for targeted Invest.
