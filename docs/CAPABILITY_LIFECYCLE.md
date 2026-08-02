# Capability Issuance, Expiry, and Revocation Lifecycle

## Lifecycle

1. Policy and approval produce eligible capability scope.
2. Capability token/object is issued with expiry and constraints.
3. Runtime validates scope before each operation.
4. Continuous verification checks trust drift.
5. Capability is revoked on expiry, policy change, anomaly, or incident action.
6. Revocation event is recorded in evidence.

## Capability Attributes

- Subject identity binding
- Allowed actions
- Target binding
- Constraints
- Not-before and expires-at UTC timestamps
- Revocation status and reason

## Fail-Closed Principle

If capability validity cannot be verified, execution does not continue.

Related:

- [Continuous Verification Lifecycle](CONTINUOUS_VERIFICATION_LIFECYCLE.md)
- [Reference Examples](REFERENCE_EXAMPLES.md)
