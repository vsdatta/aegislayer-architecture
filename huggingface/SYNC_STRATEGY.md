# Hugging Face Synchronization Strategy

## Canonical Rule

GitHub is canonical. Hugging Face receives mirrored release-ready artifacts only.

## Fail-Closed Requirements

- `HF_TOKEN` must be configured as a GitHub Secret.
- `HF_SPACE_REPO` must be configured as a repository variable (for example `org/space-name`).
- Publication directory must pass validation checks before sync.

If any requirement is missing, synchronization fails with a clear error and does not publish.

## Controlled Publication Scope

Publish only approved static artifacts from `huggingface/hf_space/`.

Do not pull changes from Hugging Face back into `main`.
