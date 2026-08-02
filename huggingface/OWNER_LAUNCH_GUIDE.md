# Owner Launch Guide

## Account-Level Actions Required

These steps still require Hugging Face or GitHub account permissions and remain outside the fully automated launch workflow.

## Hugging Face Organization Profile

1. Open the AEGISLAYER organization profile editor.
2. Paste the approved card copy from `huggingface/ORGANIZATION_CARD.md`.
3. Apply the short and long descriptions from `huggingface/ORGANIZATION_PROFILE_COPY.md`.
4. Add the verified public links from `huggingface/PROFILE_LINKS.md`.

## Pinning Repositories

1. Pin `AEGISLAYER/README`.
2. Pin the most useful supporting Spaces, starting with `architecture-explorer`, `policy-playground`, and `governance-library`.
3. Pin the AegisLayer Core collection after verifying the live URL.

## What Is Automated

- creation or update of the public Static Space repositories
- publication of generated Space assets from `dist/huggingface/<slug>/`
- creation or update of the public dataset repositories
- upload of dataset package contents from `huggingface/datasets/<slug>/`
- creation or update of the AegisLayer Core collection
- repository publication status updates under `huggingface/`

## Live Collection

- AegisLayer Core: <https://huggingface.co/collections/AEGISLAYER/aegislayer-core-6a6f5eafc1742c4f90327c9a>

## GitHub Repository Variables And Secrets

1. Keep secret `HF_TOKEN` configured.
2. Keep variable `HF_ORG` set to `AEGISLAYER` if you want the generic portfolio publish workflows to keep using the organization namespace.
3. Keep variable `HF_SPACE_REPO` set for the preserved `AEGISLAYER/README` Space.

## Triggering Workflows

1. Run `Launch Hugging Face Promotion` for full launch or reconciliation.
2. Run `Publish Hugging Face Space` to republish only `AEGISLAYER/README`.
3. Run `Publish Hugging Face Portfolio` for targeted Space-only republishes.

## Posting Announcements

1. Use the channel copy in `promotion/ANNOUNCEMENT_COPY.md`.
2. Link directly to the live Space, dataset, or collection URLs recorded in `huggingface/PUBLICATION_STATUS.md`.
3. Keep the scope note and feedback prompt intact.

## Rollback

1. Re-run launch or targeted publish workflows from the last known good commit.
2. If a specific Space or dataset is incorrect, republish only that artifact from the prior commit.
3. If profile or pinning changes are incorrect, restore the previous approved copy in the Hugging Face UI.
4. If collection order needs adjustment, update it in the Hugging Face UI and note the correction in the release log.
