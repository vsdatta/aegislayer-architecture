# Continuous Verification and Monitoring Lifecycle

## Lifecycle

1. Establish baseline trust state at execution start.
2. Monitor identity validity, approval validity, capability validity, and connector trust.
3. Detect trust drift and material context changes.
4. Trigger policy re-evaluation.
5. Revoke capability, pause, deny, or contain execution as required.
6. Record monitoring and enforcement events.

## Typical Triggers

- Approval expiry
- Capability expiry
- Connector health degradation
- Policy profile updates
- Threat signal escalation

## Related ADR

- [ADR-0006](adr/0006-continuous-verification-and-monitoring.md)
