# Hugging Face Publishing Guide

## Prerequisites

- GitHub secret: `HF_TOKEN`
- GitHub variable: `HF_SPACE_REPO`

## Publication Flow

1. Build/export static assets into `huggingface/hf_space/`.
2. Validate publication package.
3. Trigger `Publish Hugging Face Space` workflow manually or on release tags.
4. Workflow pushes approved package to configured Hugging Face repository.

## Safety

- Secrets are never printed.
- Missing configuration causes immediate failure.
- Canonical source remains GitHub.
