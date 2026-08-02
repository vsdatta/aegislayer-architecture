# AegisLayer Governance Pattern Library

## Pattern 1: Governed Request Flow

- Validate identity and authority
- Evaluate policy and risk
- Route to approvals when required
- Issue scoped capability
- Execute in controlled runtime
- Record evidence and monitoring events

## Pattern 2: High-Impact Action

- Trigger approval requirement
- Enforce bounded approval scope and expiry
- Deny on approval mismatch or expiry

## Pattern 3: Connector Invocation

- Verify readiness and supported action
- Validate capability scope against target
- Deny on unknown or degraded trust state

## Pattern 4: Continuous Verification

- Monitor trust signals during runtime
- Re-evaluate policy conditions on drift
- Revoke capability and contain when needed

## Pattern 5: Incident Containment and Recovery

- Contain unsafe runtime execution
- Preserve evidence bundle integrity
- Escalate to authorized incident response role
- Decide constrained recovery or closure

## Pattern 6: Publication Fail-Closed

- Require release-ready artifact validation
- Require configured publication credentials
- Deny publication when required config is missing

## Related

- [Unsafe Patterns](UNSAFE_PATTERNS.md)
- [Control Mapping](CONTROL_MAPPING.md)
- [Reference Examples](REFERENCE_EXAMPLES.md)
