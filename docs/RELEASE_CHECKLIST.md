# Release Checklist

Use this checklist before creating a stable release tag.

## Governance and Scope

- [ ] `release/VERSION.json` updated with candidate version.
- [ ] Changelog and release notes updated.
- [ ] Public claims reviewed for accuracy and non-absolute language.
- [ ] ADR/RFC statuses updated when required.
- [ ] Owner review completed.
- [ ] Public-release review completed.

## Content Synchronization

- [ ] Architecture docs updated.
- [ ] Governance docs updated.
- [ ] Threat model and control mapping updated.
- [ ] Diagrams updated and validated.
- [ ] Pattern library and examples updated.
- [ ] Glossary updated for new terms.

## Build and Validation

- [ ] Markdown lint passes.
- [ ] Link checks pass.
- [ ] MkDocs strict build passes.
- [ ] Mermaid validation passes.
- [ ] Reference SDK lint/type/test pass.
- [ ] Interactive demo validation passes.
- [ ] Secret-pattern scan passes.

## Publication

- [ ] GitHub Pages artifact generated.
- [ ] Hugging Face publication package validated.
- [ ] Organization card and profile copy reviewed.
- [ ] Space metadata and tagging reviewed.
- [ ] Dataset packages and schemas validated.
- [ ] Collection package updated.
- [ ] Owner-only launch instructions reviewed.
- [ ] Website and profile links verified.
- [ ] Required secrets and variables are configured.
- [ ] No generated output committed unintentionally.

## Final Gate

- [ ] `git status` reviewed for intentional changes only.
- [ ] Final diff summary reviewed.
- [ ] Commit created with release-candidate message.
- [ ] Push completed to `origin/main`.
