# Hugging Face Publishing Guide

## Prerequisites

- GitHub secret: `HF_TOKEN`
- GitHub variable: `HF_SPACE_REPO` for the legacy `AEGISLAYER/README` destination
- GitHub variable: `HF_ORG` for organization-scoped portfolio publishing
- Optional GitHub variable: `HF_SPACE_MANIFEST` for explicit slug-to-repository mapping JSON or file path

## Publication Flow

1. Build/export the full portfolio into `dist/huggingface/<space-slug>/`.
2. Mirror `organization-home` into `huggingface/hf_space/` to preserve the existing `AEGISLAYER/README` workflow.
3. Validate Spaces, datasets, links, metadata, and release assets.
4. Trigger `Publish Hugging Face Space` for the preserved legacy Space or `Publish Hugging Face Portfolio` for single-Space or full-portfolio publication.
5. Workflows clone existing Hugging Face repositories, copy approved generated files only, commit only when changes exist, and push without force.

## Safety

- Secrets are never printed.
- Missing configuration causes immediate failure.
- Canonical source remains GitHub.
- Collections remain owner-created unless Hugging Face adds stable automation support for them.
