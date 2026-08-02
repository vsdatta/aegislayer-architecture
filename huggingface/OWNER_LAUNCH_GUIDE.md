# Owner Launch Guide

## Account-Level Actions Required

These steps require Hugging Face or GitHub account permissions and cannot be fully automated from this repository alone.

## Hugging Face Organization Profile

1. Open the AEGISLAYER organization profile editor.
2. Paste the approved card copy from `huggingface/ORGANIZATION_CARD.md`.
3. Apply the short and long descriptions from `huggingface/ORGANIZATION_PROFILE_COPY.md`.
4. Add the verified public links from `huggingface/PROFILE_LINKS.md`.

## Pinning Repositories

1. Pin `AEGISLAYER/README`.
2. Pin the most useful supporting Spaces, starting with `architecture-explorer`, `policy-playground`, and `governance-library` after they exist.
3. Pin datasets or Collections only after the live links are verified.

## Creating New Space Repositories

1. Create each destination Space repository in the `AEGISLAYER` organization if it does not already exist.
2. Use `Static` as the SDK.
3. Name repositories to match the manifest defaults unless a different approved target is required.

## Creating Collections

1. Open the Hugging Face Collections UI.
2. Create each collection using the matching card in `huggingface/collections/`.
3. Add items in the listed order.
4. Record the live Collection URLs into release notes or launch posts.

## GitHub Repository Variables And Secrets

1. Add secret `HF_TOKEN`.
2. Add variable `HF_ORG` with the target Hugging Face organization, for example `AEGISLAYER`.
3. Add variable `HF_SPACE_REPO` for the preserved legacy Space target, for example `AEGISLAYER/README`.
4. Add variable `HF_SPACE_MANIFEST` only if explicit slug-to-repo overrides are needed.

## Triggering Workflows

1. Run `Validate Hugging Face Assets`.
2. Run `Build Hugging Face Datasets`.
3. Run `Prepare Hugging Face Release`.
4. Run `Publish Hugging Face Space` to update `AEGISLAYER/README`.
5. Run `Publish Hugging Face Portfolio` for additional Spaces.

## Posting Announcements

1. Use the channel copy in `promotion/ANNOUNCEMENT_COPY.md`.
2. Link directly to the relevant Space, dataset, Collection, or documentation page.
3. Keep the scope note and feedback prompt intact.

## Rollback

1. Re-run portfolio publication for the last known good commit using workflow dispatch.
2. If a specific Space is incorrect, republish only that slug from the prior commit.
3. If a profile change is incorrect, restore the previous approved copy from Git history.
4. If a Collection item order is incorrect, update it in the Hugging Face UI and note the correction in the release log.
