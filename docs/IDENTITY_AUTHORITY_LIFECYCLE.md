# Identity and Authority Lifecycle

## Classification

- **Conceptual** lifecycle
- **Illustrative** sequence and examples

## Lifecycle Stages

1. Receive request with actor identity claims.
2. Validate identity integrity, issuer, and freshness.
3. Resolve authority context (role, scope, delegation constraints).
4. Evaluate least-privilege fit for requested action.
5. Deny, constrain, or continue to policy evaluation.
6. Re-verify during long-running execution when context changes.

## Fail-Closed Conditions

- Missing identity proof
- Unknown issuer
- Expired authority context
- Ambiguous delegated authority

## Evidence Requirements

Record actor identifier class, authority scope, decision basis, UTC decision timestamp, correlation ID, and causation ID.

## Diagram

Source: `diagrams/../diagrams/identity-authority-lifecycle.mmd`

Related ADRs:

- [ADR-0002](adr/0002-identity-first-authorization.md)
- [ADR-0004](adr/0004-fail-closed-execution.md)
