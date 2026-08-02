# Approval Lifecycle

## Lifecycle

1. Policy flags approval requirement.
2. Approval request is formed with bounded scope and expiry.
3. Authorized approver reviews contextual evidence.
4. Approver records allow/deny decision and rationale.
5. Runtime verifies approval validity before and during execution.
6. Approval can be revoked or expire.

## Approval Constraints

- Request-specific
- Scope-specific
- Target-specific
- Time-bound
- Attributable to accountable identity

## Fail-Closed Behavior

If required approval is absent, expired, mismatched, or revoked, execution is denied or contained.

## Diagram

Source: `diagrams/../diagrams/approval-lifecycle.mmd`

Related ADR:

- [ADR-0007](adr/0007-human-approval-for-high-impact-actions.md)
