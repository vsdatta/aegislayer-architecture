# Getting Started

## Purpose

Use this page to navigate the AegisLayer public reference architecture repository and run local validation.

## Recommended Reading

1. [REFERENCE_ARCHITECTURE_GUIDE.md](REFERENCE_ARCHITECTURE_GUIDE.md)
2. [ARCHITECTURE.md](ARCHITECTURE.md)
3. [THREAT_MODEL.md](THREAT_MODEL.md)
4. [GOVERNANCE.md](GOVERNANCE.md)
5. Lifecycle pages
6. ADR and RFC indices

## Contributor Workflow

1. Open an issue or RFC when required.
2. Implement focused changes in a short-lived branch.
3. Update affected ADR/doc/diagram/control/example artifacts.
4. Run local validation commands.
5. Submit pull request with checklist completion.

## Local Validation Commands

### Docs and links

- `mkdocs build --strict`
- `python scripts/validate_mermaid.py`
- `python scripts/check_relative_links.py`
- `python scripts/check_nav_reachability.py`

### SDK

- `cd reference-sdk && python -m pip install -e .[dev]`
- `cd reference-sdk && ruff check src tests`
- `cd reference-sdk && mypy src`
- `cd reference-sdk && pytest -q`

### Demo and security scan

- `python scripts/validate_demo.py`
- `python scripts/scan_secrets.py`

## Public Scope Reminder

Contributions must avoid secrets, customer data, and proprietary implementation internals.
