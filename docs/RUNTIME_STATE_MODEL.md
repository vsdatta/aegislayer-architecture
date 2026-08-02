# Runtime State Model

## State Model

- `received`
- `identity_validated`
- `policy_evaluated`
- `awaiting_approval`
- `capability_issued`
- `executing`
- `contained`
- `completed`
- `denied`

## Transition Rules

- No transition to `executing` without policy allow and required approvals.
- Any trust-invalidating event may transition to `contained` or `denied`.
- `completed` requires finalized evidence bundle.

## Fail-Closed Requirement

Undefined transitions are denied by default.

## Diagram

Source: `diagrams/../diagrams/runtime-state-model.mmd`
