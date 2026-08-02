# Public Reference SDK

The `reference-sdk/` directory contains a conceptual Python 3.12 SDK that demonstrates architecture behavior without exposing proprietary runtime logic.

## Scope

- Typed models and deterministic behavior
- Policy and approval decision flow
- Capability issuance, expiry, and revocation
- Connector readiness checks
- Runtime state decisioning
- Evidence bundle generation
- Monitoring and incident response decision helpers

## Out of Scope

- Production connector execution
- Real network/cloud/payment/browser/email/database operations
- Secrets and deployment internals

## Key Paths

- `reference-sdk/src/aegislayer_reference/`
- `reference-sdk/tests/`
- `reference-sdk/examples/`

## Validation

- `cd reference-sdk && ruff check src tests`
- `cd reference-sdk && mypy src`
- `cd reference-sdk && pytest -q`

## Classification

Conceptual reference implementation only.
