# Contributing to AegisLayer Architecture

Thank you for contributing to AegisLayer.

## Scope

This repository is the canonical public source for the AegisLayer reference architecture, governance model, diagram library, conceptual SDK artifacts, and public research outputs.

Contributions must remain public-safe, technically grounded, and aligned to accepted ADRs.

## Public-Release Boundaries

Do not submit:

- Secrets, credentials, private keys, or access tokens
- Customer or personal data
- Confidential infrastructure details
- Proprietary production implementation logic
- Unapproved patent-sensitive implementation details
- Public vulnerability disclosures (report privately through [SECURITY.md](SECURITY.md))

## Branch and Change Model

- `main` is the stable public specification branch.
- Use short-lived feature branches for non-trivial changes.
- Keep pull requests narrow and traceable.
- Material architecture changes must start with an RFC.
- Accepted architecture changes must create or update ADRs.

## Architecture Change Workflow

Use this lifecycle for any material architecture or governance change:

1. Open or update an issue describing scope and impact.
2. Author an RFC in [docs/rfc](docs/rfc).
3. Complete technical, security, and governance review.
4. Record accepted architecture decisions in [docs/adr](docs/adr).
5. Synchronize affected artifacts:
   - Architecture and governance docs
   - Threat model and control mapping
   - Pattern library and examples
   - Mermaid diagrams
   - Glossary terms
   - Changelog and release notes
6. Validate quality gates locally and in CI.

## ADR and RFC Status Governance

### ADR statuses

- **Accepted**: authoritative decision.
- **Superseded**: replaced by a newer accepted ADR.
- **Deprecated**: retained historically but no longer recommended.
- **Rejected**: considered but not adopted.

### RFC statuses

- **Draft**: proposal being authored.
- **Review**: under structured review.
- **Accepted**: approved for implementation.
- **Rejected**: not approved.
- **Withdrawn**: removed by author.
- **Superseded**: replaced by a newer RFC.
- **Implemented**: accepted work completed and verified.

## Release Governance

Documentation releases use Semantic Versioning suitable for reference artifacts:

- **MAJOR** (`X.0.0`): material architecture/governance model shifts, breaking interpretation changes.
- **MINOR** (`1.X.0`): new additive architecture pages, examples, SDK/demo capabilities, or research sections.
- **PATCH** (`1.0.X`): editorial clarifications, link fixes, non-material corrections.

Release controls:

1. Update `release/VERSION.json`.
2. Update [CHANGELOG.md](CHANGELOG.md) and release notes.
3. Run full validation gates.
4. Obtain owner review and public-release review.
5. Publish only after validations pass.

## Contributor Commands

### Documentation

- `mkdocs build --strict`
- `python scripts/validate_mermaid.py`

### Reference SDK

- `cd reference-sdk && python -m pip install -e .[dev]`
- `cd reference-sdk && ruff check src tests`
- `cd reference-sdk && mypy src`
- `cd reference-sdk && pytest -q`

### Interactive Demo

- `python scripts/validate_demo.py`

### Security and Link Hygiene

- `python scripts/scan_secrets.py`
- `python scripts/check_relative_links.py`

## Pull Request Expectations

A pull request should clearly identify:

- What changed and why
- ADR/RFC impact
- Security and governance implications
- Validation performed
- Public-release suitability

Use [Architecture Review Checklist](docs/ARCHITECTURE_REVIEW_CHECKLIST.md) for material changes.

## Review and Ownership

Owner review is required for:

- ADR acceptance/supersession/deprecation
- RFC acceptance/rejection
- Release governance changes
- Security policy changes
- Publication workflow changes

## License

By contributing, you agree your contribution may be distributed under the repository license.

Copyright © VND TECH LLC.
