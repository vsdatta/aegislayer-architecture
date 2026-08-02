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

## Example 2: Connector Health Failure
1. Connector selected.
2. Health verification fails.
3. Execution does not proceed.
4. Evidence records the denial.
5. Alternative routing or escalation is considered according to policy.

## Example 3: High-Impact Operation
1. Action exceeds governance threshold.
2. Human approval is required.
3. Approval is bound to scope and expiry.
4. Execution proceeds only after approval.
5. All actions are correlated with evidence.

## Example 4: Continuous Verification
1. Long-running workflow begins.
2. Monitoring detects approval expiry.
3. Capability is revoked.
4. Runtime pauses or stops execution.
5. Incident and audit records are preserved.

## Related Documentation
- GOVERNANCE.md
- THREAT_MODEL.md
- CONTROL_MAPPING.md
- PATTERN_LIBRARY.md
- ADR-0001 through ADR-0007
