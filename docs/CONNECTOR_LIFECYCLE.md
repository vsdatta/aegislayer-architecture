# Connector Lifecycle

## Lifecycle

1. Discover connector descriptor and declared capabilities.
2. Verify readiness state and trust status.
3. Bind request to least-privilege capability scope.
4. Validate connector input constraints.
5. Execute only when trust preconditions hold.
6. Capture connector output and evidence.
7. Continuously monitor trust indicators and revoke when needed.

## Readiness States

- Ready
- Degraded
- Blocked
- Revoked

## Fail-Closed Behavior

Degraded or unknown connector state cannot silently escalate privileges or auto-route to broader access.

## Diagram

Source: `diagrams/../diagrams/connector-lifecycle.mmd`

Related ADR:

- [ADR-0005](adr/0005-capability-scoped-connectors.md)
