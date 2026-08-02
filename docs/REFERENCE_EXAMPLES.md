# Reference Examples

This document provides conceptual examples showing how the public AegisLayer governance patterns work together. These examples are illustrative only and intentionally omit implementation details.

## Example 1: Governed AI Request

1. User submits a request.
2. Identity and authority are validated.
3. Policy and risk are evaluated.
4. Approval is requested if required.
5. A scoped capability is issued.
6. Execution occurs in a controlled runtime.
7. Evidence and telemetry are recorded.
8. Results are returned and the request is finalized.

Expected governance outcome:

- Execution proceeds only when trust conditions are satisfied.
- Evidence is sufficient for independent review.

## Example 2: Connector Health Failure

1. Connector selected.
2. Health verification fails.
3. Execution does not proceed.
4. Evidence records the denial.
5. Alternative routing or escalation is considered according to policy.

Expected governance outcome:

- Connector unreadiness fails closed.
- No implicit fallback broadens privileges.

## Example 3: High-Impact Operation

1. Action exceeds governance threshold.
2. Human approval is required.
3. Approval is bound to scope and expiry.
4. Execution proceeds only after approval.
5. All actions are correlated with evidence.

Expected governance outcome:

- Approval remains request-specific, time-bound, and attributable.
- Expired or mismatched approval blocks execution.

## Example 4: Continuous Verification

1. Long-running workflow begins.
2. Monitoring detects approval expiry.
3. Capability is revoked.
4. Runtime pauses or stops execution.
5. Incident and audit records are preserved.

Expected governance outcome:

- Stale trust state triggers containment.
- Recovery decisions are evidence-backed.

## Example-to-Pattern Mapping

| Example | Primary Pattern | Related ADRs |
| --- | --- | --- |
| Governed AI Request | Governed Request Flow | ADR-0001, ADR-0002, ADR-0003, ADR-0004 |
| Connector Health Failure | Connector Invocation | ADR-0004, ADR-0005 |
| High-Impact Operation | High-Impact Action | ADR-0007 |
| Continuous Verification | Continuous Trust | ADR-0006 |

## Related Documentation

- [Governance](GOVERNANCE.md)
- [Threat Model](THREAT_MODEL.md)
- [Control Mapping](CONTROL_MAPPING.md)
- [Pattern Library](PATTERN_LIBRARY.md)
- [ADR Index](adr/README.md)
