# Tech Evaluation Spike

## Situation

You're deciding whether to adopt a specific library, framework, service, or vendor. You want an evidence-based verdict from actually exercising it — not a summary of its marketing — with the deal-breakers checked and the risks named.

## The Prompt

```
You are evaluating a candidate technology by exercising it, not by reading its docs. Report only what was actually observed; mark anything unmeasured as Unknown.

Produce:
1. Decision & must-haves — what this feeds, and the deal-breakers (license, self-host, cost, latency, stack fit). A failure on any deal-breaker means it's out.
2. What was tested — concrete things tried against realistic conditions (not hello-world).
3. Evidence — what held up (with numbers), what broke, and a deal-breaker check (license / cost at our scale / security / maintenance health / lock-in).
4. vs alternative — only the dimensions that decide it.
5. Did NOT test — risks a short trial leaves open.
6. Verdict — Adopt / Avoid / Need-more (with the follow-up that would settle it), leading with the strongest reason.

Candidate: [TECH_AND_ALTERNATIVES]
The job: [WHAT_WE_NEED_IT_TO_DO]
Deal-breakers: [HARD_REQUIREMENTS]
What I tried / observed: [PASTE_WHAT_YOU_RAN_AND_SAW]
```

## Example Input

```
Candidate: Temporal (workflow orchestration) vs rolling our own with a job queue.
The job: Reliable multi-step order fulfilment workflows with retries and long waits.
Deal-breakers: Self-hostable, Apache/MIT-compatible license, works with our Go stack, under $2k/mo infra at our scale.
What I tried / observed: Ran the self-hosted server locally, built a 4-step fulfilment workflow with a 24h timer and a failure/retry step. Killed the worker mid-run. Workflow resumed correctly. Setup was fiddly (~1 day). License is MIT. Go SDK is mature. Didn't estimate infra cost at production scale.
```

## Example Output

> **Tech Evaluation: Temporal** — Verdict: Need more
>
> _Functionally excellent and clears most deal-breakers, but production infra cost is untested — the one open must-have._
>
> **Decision & must-haves**
> - Deciding: order-fulfilment orchestration.
> - Deal-breakers: self-host ✅, MIT license ✅, Go SDK ✅, <$2k/mo infra ❓ (untested).
>
> **What was tested**
> - Self-hosted server locally; 4-step workflow with a 24h timer + retry step; killed the worker mid-run.
>
> **Evidence**
> - ✅ Held up: workflow resumed correctly after worker kill; retries and the long timer worked as documented; Go SDK mature.
> - ❌ Rough: setup took ~1 day; operational complexity is real.
> - Deal-breaker check: license ✅, stack ✅, self-host ✅, cost ❓, lock-in — moderate (workflow code is Temporal-specific).
>
> **vs rolling our own:** Temporal gives durable execution we'd otherwise hand-build and get wrong; the cost is operational complexity.
>
> **Did NOT test:** Infra cost at production scale, multi-region, upgrade path.
>
> **Verdict:** Need-more — settle the infra cost with a 1-day sizing spike against production volume before committing.

## Tuning Notes

- **Deal-breaker first:** A single hard-requirement failure decides it regardless of how good the rest is. Make sure the verdict reflects that, not a feature average.
- **Scale shift:** At a startup, weight speed-to-value and DX and accept more lock-in (but name it). At enterprise, add security/compliance and vendor viability.
- **Common pitfall:** The model may report doc/marketing claims as observed. Insist every "held up" line comes from something actually run, or is marked Unknown.
- **Lock-in:** Always ask what leaving would cost — it's the risk teams discover too late.
