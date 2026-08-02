# Architecture Conformance Criteria

Use these criteria to evaluate whether an implementation aligns with the public reference architecture intent.

## Required Criteria

- Identity and authority are validated before policy allow.
- Policy evaluation occurs before external execution.
- High-impact actions require accountable approval where defined.
- Capabilities are scoped, time-bound, and revocable.
- Connector readiness is checked before invocation.
- Runtime enforces fail-closed defaults on trust uncertainty.
- Evidence captures attributable events with UTC timestamps and deterministic fields.
- Continuous verification can trigger revocation or containment.

## Evidence of Conformance

Conformance should be demonstrated through architecture artifacts, tests, traces, or walkthroughs. This repository does not claim conformance for external systems by default.

Related:

- [Architecture Review Checklist](ARCHITECTURE_REVIEW_CHECKLIST.md)
- [Reference SDK](REFERENCE_SDK.md)
