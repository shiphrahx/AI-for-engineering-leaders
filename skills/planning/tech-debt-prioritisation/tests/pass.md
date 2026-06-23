**Platform Team — Tech Debt Assessment**

**Summary:** 4 items. Estimated velocity tax: ~1.5 engineer-days/week. One active security item.

**Prioritised Backlog**
| Priority | Item | Risk if Unaddressed | Effort | Business Case |
|----------|------|---------------------|--------|---------------|
| P0 | Rotate leaked service token | Credential compromise | S | Security exposure, compliance |
| P1 | Remove the legacy auth path | Duplicate logic, bugs | M | Cuts auth incidents, speeds delivery |
| P2 | Consolidate config loaders | Confusing onboarding | M | Faster ramp for new hires |
| P3 | Delete dead feature flags | Minor clutter | S | Cleaner codebase |

**Recommended Investment**
20% of sprint capacity for 3 sprints. Sequencing: P0 in Sprint 1, P1 across Sprints 1–2.

**Quick Wins (< 1 day each)**
- Delete dead feature flags.
