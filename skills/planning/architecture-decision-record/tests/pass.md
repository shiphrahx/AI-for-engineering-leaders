# ADR 014: Adopt event sourcing for the ledger

## Status
Accepted

## Context
The ledger needs an auditable history of every balance change, and the current
last-write-wins model loses intermediate state needed for reconciliation and disputes.

## Decision
Adopt event sourcing for the ledger domain, with a projected read model for balances.

## Consequences
Full audit trail and easy temporal queries, at the cost of more operational complexity
and a learning curve for the team. Read models must be rebuildable from the event log.

## Alternatives considered
- Append-only audit table alongside the mutable balances table.
- Change-data-capture from the existing database into an audit store.
- Status quo with periodic snapshots.
