# Deployment Reference Architectures

This page describes conceptual deployment patterns for applying the reference architecture.

## Pattern A: Centralized Governance Plane

- Central identity, policy, approval, and evidence services
- Multiple execution runtimes consume governance decisions

## Pattern B: Federated Governance Domains

- Shared policy baseline
- Domain-specific connectors and approval boundaries
- Standard evidence schema for cross-domain audit

## Pattern C: Regulated High-Impact Domain

- Mandatory multi-party approvals
- Stronger containment defaults
- Additional evidence retention and review controls

## Classification

These patterns are conceptual reference designs. They are not production deployment instructions.

Related:

- [Architecture](ARCHITECTURE.md)
- [Reference Implementation Boundaries](REFERENCE_IMPLEMENTATION_BOUNDARIES.md)
