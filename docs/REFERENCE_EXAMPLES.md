# Reference Examples

These conceptual examples map architecture behavior to the reference SDK and interactive demo.

## Example 1: Allowed Low-Risk Request

- Identity and authority validate
- Policy returns allow
- Connector readiness is ready
- Runtime completes with evidence

## Example 2: Denied Unauthorized Request

- Identity validates
- Authority scope mismatch triggers deny
- Runtime fails closed before external execution

## Example 3: High-Impact Request Requiring Approval

- Policy returns require approval
- Approval is validated for scope/expiry
- Execution proceeds only while approval remains valid

## Example 4: Connector Readiness Failure

- Connector readiness is blocked
- Runtime denies without privilege broadening

## Example 5: Capability Expiry During Execution

- Capability expires
- Continuous verification revokes capability
- Runtime transitions to contained/denied path

## Example 6: Continuous Verification Revocation

- Trust drift detected
- Capability revoked with explicit reason
- Monitoring event recorded

## Example 7: Evidence Bundle Generation

- Lifecycle events appended with correlation and causation IDs
- Finalized evidence bundle becomes immutable

## Example 8: Incident Containment

- Anomaly detection triggers containment
- Incident decision selects containment/recovery path

## Reference Links

- SDK examples: `reference-sdk/examples/scenarios.py`
- SDK tests: `reference-sdk/tests/test_reference_sdk.py`
- Demo scenarios: `interactive-demo/assets/js/app.js`
