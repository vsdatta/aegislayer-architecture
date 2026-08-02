# Policy Evaluation Lifecycle

## Lifecycle

1. Normalize structured action request.
2. Collect policy inputs (identity, authority, target, capability, risk context).
3. Evaluate policy rules and risk class.
4. Produce explicit decision: allow, deny, allow-with-constraints, or require approval.
5. Emit deterministic denial or escalation reasons.
6. Re-evaluate when context materially changes.

## Fail-Closed Defaults

- Missing required input fields -> deny
- Unknown policy profile -> deny
- Unsupported target connector state -> deny

## Output Requirements

- Decision outcome
- Reason codes
- Required approvals (if any)
- Constraints and expiry window

## Diagram

Source: `diagrams/../diagrams/policy-evaluation-lifecycle.mmd`

Related:

- [Governance](GOVERNANCE.md)
- [Threat Model](THREAT_MODEL.md)
