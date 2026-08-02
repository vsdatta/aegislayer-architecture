# Evidence Lifecycle Deep Dive

## Purpose

Evidence links request intent, trust checks, policy outcomes, approvals, execution results, and containment actions.

## Lifecycle

1. Initialize evidence record with correlation and causation IDs.
2. Append identity, authority, policy, and approval events.
3. Append runtime and connector events.
4. Seal finalized evidence bundle for immutable review context.
5. Support audit and incident analysis.

## Evidence Quality Criteria

- Deterministic serialization
- UTC timestamping
- Explicit reason codes
- Event attribution
- Finalized bundle immutability semantics

## Diagram

Source: `diagrams/../diagrams/evidence-lifecycle.mmd`

Related ADR:

- [ADR-0003](adr/0003-evidence-by-design.md)
