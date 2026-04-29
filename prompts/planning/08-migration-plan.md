# Migration Plan

## Situation

You need to move from System A to System B — a database migration, framework upgrade, service decomposition, or cloud provider switch. The plan needs to be phased, safe, and communicate clearly to stakeholders what to expect and when.

## The Prompt

```
You are an engineering leader creating a phased migration plan. The plan must prioritise safety (zero data loss, minimal downtime), be reversible at each phase, and communicate clearly to both technical and non-technical stakeholders.

Structure:
1. **Migration overview** — what's moving, from where to where, and why
2. **Success criteria** — what "done" looks like, with measurable targets
3. **Phases** — each phase includes: scope, duration, rollback plan, go/no-go criteria for the next phase, and who's responsible
4. **Risk register** — top risks with mitigations
5. **Communication plan** — who needs to know what, and when
6. **Resource requirements** — people, tools, budget

Migration: [FROM_SYSTEM] → [TO_SYSTEM]
Reason: [WHY_MIGRATING]
Scale: [SCALE_DATA]
Constraints: [CONSTRAINTS]
Team: [TEAM]
```

## Example Input

```
Migration: PostgreSQL 12 on self-managed EC2 → Aurora PostgreSQL 15 (managed)
Reason: PG 12 EOL in November, self-managed DB ops consuming 30% of one SRE's time, need read replicas for analytics workloads
Scale: 2.3TB database, 12K queries/sec at peak, serves 8 application services
Constraints: Maximum 5 minutes downtime for cutover, no data loss, must maintain same connection strings (apps shouldn't need code changes), compliance requires data stays in eu-west-1
Team: 2 SREs, 1 DBA consultant (part-time), 8 application engineers for testing
```

## Example Output

> **Migration Plan: PostgreSQL 12 (EC2) → Aurora PostgreSQL 15**
>
> **Overview**
> Migrate our primary PostgreSQL database from self-managed EC2 instances to AWS Aurora PostgreSQL 15. This addresses the PG 12 end-of-life (November), frees ~30% of SRE capacity from database ops, and enables read replicas for analytics workloads. The database serves 8 application services, holds 2.3TB of data, and handles 12K queries/sec at peak.
>
> **Success Criteria**
> - All 8 services running on Aurora with no code changes
> - Zero data loss during migration
> - Downtime < 5 minutes during final cutover
> - Query latency within 10% of current baseline
> - Read replica available for analytics team within 1 week of cutover
>
> **Phase 1: Preparation (Weeks 1-2)**
> - Set up Aurora cluster in eu-west-1 with matching configuration
> - Benchmark Aurora performance with representative query workload
> - Set up AWS DMS for continuous replication from EC2 PG to Aurora
> - Create monitoring dashboards comparing old and new database metrics
> - *Go/no-go for Phase 2:* Aurora benchmarks within 10% of current performance, DMS replication running without errors for 48 hours
> - *Rollback:* Tear down Aurora cluster. No production impact.
> - *Owner:* SRE team + DBA consultant
>
> **Phase 2: Shadow Migration (Weeks 3-4)**
> - Enable continuous replication via DMS (EC2 → Aurora)
> - Route read-only analytics queries to Aurora read replica
> - Run automated query comparison: same queries against both databases, flag discrepancies
> - Application teams run integration tests against Aurora
> - *Go/no-go for Phase 3:* Replication lag < 1 second, zero data discrepancies in comparison tests, all 8 services pass integration tests
> - *Rollback:* Stop DMS replication, point analytics back to primary. No production impact.
> - *Owner:* SRE team, application engineers for testing
>
> **Phase 3: Cutover (Week 5, scheduled maintenance window)**
> - Announce maintenance window (Saturday 02:00-02:30 GMT)
> - Stop application writes to current database
> - Wait for DMS replication to reach zero lag
> - Update connection strings (via DNS CNAME flip)
> - Verify all 8 services connected and functioning
> - Run data integrity spot checks
> - Open for traffic
> - *Rollback:* Flip DNS back to EC2 database. DMS reverse replication catches any writes made to Aurora during the window.
> - *Owner:* SRE team lead (incident commander), all application on-call engineers on standby
>
> **Phase 4: Decommission (Weeks 6-8)**
> - Monitor Aurora for 2 weeks post-cutover
> - Enable read replicas for analytics team
> - Decommission EC2 database instances (after 2-week bake period)
> - Update runbooks and documentation
> - Close migration project
>
> **Risk Register**
> | Risk | Likelihood | Impact | Mitigation |
> |------|-----------|--------|------------|
> | Replication lag spike during cutover | Medium | High | Schedule cutover during lowest-traffic window. Pre-test with simulated write freeze. |
> | Query performance regression on Aurora | Low | High | Phase 2 benchmarking catches this before cutover. Have PG 12 config tuning parameters mapped to Aurora equivalents. |
> | Application connection string caching | Medium | Medium | Ensure all services use DNS-based connection strings with low TTL. Test DNS flip in staging first. |
> | Compliance: data residency | Low | High | Aurora cluster provisioned in eu-west-1 from day one. Verified with compliance team before starting. |
>
> **Communication Plan**
> - Week 1: Email all application team leads with migration timeline and testing expectations
> - Week 3: Slack update when shadow migration begins; ask teams to flag any anomalies
> - Week 4: Announce maintenance window (3 business days notice minimum)
> - Cutover night: Real-time updates in #db-migration Slack channel
> - Week 6: All-clear email confirming migration complete
>
> **Resources:** 2 SREs (full-time weeks 1-6), 1 DBA consultant (10 hrs/week), application engineers (~2 hrs each for testing), Aurora costs (~$2,400/month estimated, offset by EC2 decommission savings of ~$1,800/month)

## Tuning Notes

- **Application-level migration (e.g., framework upgrade):** Replace the DMS/replication phases with a feature-flag-based rollout. Phase 1 is the new stack running in shadow mode, Phase 2 is canary traffic, Phase 3 is full cutover.
- **Cloud-to-cloud migration:** Add a "data transfer cost" line item. Cross-cloud data egress can be surprisingly expensive.
- **Smaller migration:** Condense to 3 phases: prep, migrate, verify. Not every migration needs a shadow period.
- **Multiple stakeholders:** Add a RACI table showing who's responsible, accountable, consulted, and informed for each phase.
