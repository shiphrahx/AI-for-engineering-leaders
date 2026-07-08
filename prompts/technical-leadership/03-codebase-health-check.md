# Codebase Health Check

## Situation

You want an honest, periodic read on the health of a system your team owns — where the risk is, what's degrading, and the few fixes that would help most — so investment goes where it pays off rather than where the loudest complaint is.

## The Prompt

```
You are assessing the health of a codebase an engineering leader owns. Score by evidence, not vibes. Distinguish what you observed from what you couldn't measure (mark Unknown).

Rate each dimension 🟢 healthy / 🟡 watch / 🔴 at risk, with one line of evidence:
- Tests & reliability (coverage on critical paths, incident/bug rate)
- Change hotspots (files that change and break most)
- Complexity & structure (oversized modules, coupling, duplication)
- Dependencies & security (outdated/abandoned deps, vuln surface, maintainer risk)
- Build & CI (build time, CI reliability, does it gate quality)
- Docs & onboarding (can a new engineer get productive; bus-factor)

Then give: overall rating + trend, the 2-3 HIGHEST-LEVERAGE fixes (not an exhaustive list), and now-vs-later. Hold the system to its stated bar.

Bar: [PROTOTYPE / STANDARD / CRITICAL]
Why now: [ROUTINE / PLANNING_INPUT / SPECIFIC_WORRY]
Known pain: [INCIDENTS_OR_COMPLAINTS]
Codebase / signals: [PASTE_STRUCTURE_COVERAGE_CI_DEP_OUTPUT_OR_REPO_ACCESS]
```

## Example Input

```
Bar: Standard production service.
Why now: Planning next quarter's investment.
Known pain: Deploys are slow and one module keeps causing regressions.
Codebase / signals: orders-service, Python. Coverage report: 44% overall, 12% on orders/pricing.py. CI takes 22 min. pricing.py changed 31 times in 3 months, 6 of those reverted. 3 deps flagged outdated by pip-audit (one with a known CVE).
```

## Example Output

> **Codebase Health: orders-service** — Bar: standard — planning input
>
> **Overall: 🟡 Watch** — one clear risk hotspot and a security gap; trend degrading around pricing.
>
> **By dimension**
> | Dimension | Rating | Evidence |
> |-----------|--------|----------|
> | Tests & reliability | 🔴 | pricing.py at 12% coverage; 6 of 31 changes reverted |
> | Change hotspots | 🔴 | pricing.py — highest churn, highest revert rate |
> | Complexity & structure | 🟡 | churn concentrated in one module suggests it does too much |
> | Dependencies & security | 🔴 | 3 outdated deps, one with a known CVE |
> | Build & CI | 🟡 | 22-min CI slows iteration; not gating hard enough to catch the reverts |
> | Docs & onboarding | ⬜ | Unknown — no signal provided |
>
> **Highest-leverage fixes**
> 1. Add tests to `pricing.py` before more changes → cuts the revert rate. (~1 week)
> 2. Patch the CVE dependency → closes the security gap. (~1 day)
> 3. Split `pricing.py` along its responsibilities → reduces the hotspot. (~1-2 weeks, after tests)
>
> **Now vs later**
> - Now (actively risky): CVE patch, pricing test coverage.
> - Later: CI speedup, module split.
>
> **Could not measure:** docs/onboarding health, real incident count.

## Tuning Notes

- **Bar shift:** State the bar explicitly. A 🔴 on a prototype may be fine; the same on a payments service is not.
- **Scale shift:** For a large system, run the check per-module and roll up, rather than scoring the whole thing at once.
- **Common pitfall:** The model may produce an exhaustive cleanup list. Force it to the 2-3 highest-leverage fixes tied to real risk.
- **Trend:** If you have a prior health check, paste it — a degrading trend on a critical system matters more than a mediocre-but-stable snapshot.
