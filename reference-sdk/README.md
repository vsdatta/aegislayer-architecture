# AegisLayer Reference SDK (Conceptual)

This SDK is a **conceptual public reference implementation** for architecture behavior described in this repository.

It is intentionally non-proprietary and does not include production connectors, secrets, network calls, or deployment internals.

## What It Demonstrates

- Request identity and authority context validation
- Structured action requests
- Deterministic policy decisions with explicit denial reasons
- Human approval requirements for high-impact requests
- Capability issuance, expiry, and revocation
- Connector readiness gating
- Runtime state transitions with fail-closed behavior
- Evidence record and finalized immutable bundle semantics
- Continuous verification and incident containment decisions
- Canonical deterministic JSON serialization

## Installation

```bash
cd reference-sdk
python -m pip install -e .[dev]
```

## Test

```bash
cd reference-sdk
pytest -q
```

## Scope Disclaimer

This SDK illustrates architecture concepts only. It is not the proprietary AegisLayer runtime and does not claim production security assurance.
