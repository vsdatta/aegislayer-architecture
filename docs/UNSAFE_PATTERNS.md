# Commonly Misused or Unsafe Patterns

This page catalogs anti-patterns that conflict with AegisLayer governance principles.

## Anti-Patterns

- Implicit authority inferred only from prompt text
- Connector invocation without explicit capability scope
- Policy evaluation after external execution
- Reusable approvals without scope or expiry binding
- Silent fallback from denied state to broader privilege path
- Evidence records without stable identifiers or timestamps
- Trust monitoring without enforcement actions

## Safer Replacements

- Identity-first validation with explicit authority context
- Fail-closed connector readiness checks
- Policy-before-execution control point
- Request-bound and time-bound approvals
- Immutable finalized evidence bundles

Related:

- [Pattern Library](PATTERN_LIBRARY.md)
- [Security Design Principles](SECURITY_DESIGN_PRINCIPLES.md)
