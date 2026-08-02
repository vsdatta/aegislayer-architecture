#!/usr/bin/env python3
"""Launch and verify the public AEGISLAYER Hugging Face portfolio."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
import json
import os
from pathlib import Path
import sys

from huggingface_hub import HfApi

REPO = Path(__file__).resolve().parents[1]
DIST_ROOT = REPO / "dist" / "huggingface"
DATASET_ROOT = REPO / "huggingface" / "datasets"
STATUS_PATH = REPO / "huggingface" / "PUBLICATION_STATUS.md"
PROFILE_LINKS_PATH = REPO / "huggingface" / "PROFILE_LINKS.md"
RELEASE_FEED_PATH = REPO / "huggingface" / "RELEASE_FEED.md"
OWNER_GUIDE_PATH = REPO / "huggingface" / "OWNER_LAUNCH_GUIDE.md"
COLLECTION_GUIDE_PATH = REPO / "huggingface" / "collections" / "COLLECTION_PUBLISHING_GUIDE.md"
SUMMARY_PATH = DIST_ROOT / "launch-summary.json"

NAMESPACE = "AEGISLAYER"
COLLECTION_TITLE = "AegisLayer Core"
COLLECTION_DESCRIPTION = (
    "Public AegisLayer architecture, governance, AI security, interactive "
    "demonstrations, synthetic governance datasets, research, and developer resources."
)

SPACE_SLUGS = [
    "architecture-explorer",
    "policy-playground",
    "evidence-chain-explorer",
    "threat-control-explorer",
    "connector-trust-simulator",
    "runtime-state-visualizer",
    "governance-library",
]
DATASET_SLUGS = [
    "aegislayer-governance-scenarios",
    "threat-control-map",
    "architecture-catalog",
]
COLLECTION_ITEMS = [
    ("space", f"{NAMESPACE}/README"),
    *[("space", f"{NAMESPACE}/{slug}") for slug in SPACE_SLUGS],
    *[("dataset", f"{NAMESPACE}/{slug}") for slug in DATASET_SLUGS],
]


@dataclass
class RepoVerification:
    repo_id: str
    repo_type: str
    url: str
    private: bool
    required_files: list[str]


def require_token() -> str:
    token = os.environ.get("HF_TOKEN", "").strip()
    if not token:
        raise RuntimeError("HF_TOKEN is required")
    return token


def api_client(token: str) -> HfApi:
    return HfApi(token=token)


def space_url(slug: str) -> str:
    return f"https://huggingface.co/spaces/{NAMESPACE}/{slug}"


def dataset_url(slug: str) -> str:
    return f"https://huggingface.co/datasets/{NAMESPACE}/{slug}"


def normalize_collection_url(url: str) -> str:
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return f"https://huggingface.co{url}"


def repo_required_files(path: Path) -> list[str]:
    files = [str(item.relative_to(path)).replace("\\", "/") for item in path.rglob("*") if item.is_file()]
    return sorted(files)


def ensure_space(api: HfApi, token: str, slug: str) -> RepoVerification:
    repo_id = f"{NAMESPACE}/{slug}"
    api.create_repo(
        repo_id=repo_id,
        repo_type="space",
        space_sdk="static",
        private=False,
        exist_ok=True,
        token=token,
    )
    folder = DIST_ROOT / slug
    if not folder.exists():
        raise FileNotFoundError(f"Missing generated Space directory: {folder}")
    api.upload_folder(
        repo_id=repo_id,
        repo_type="space",
        folder_path=folder,
        commit_message=f"Publish {slug} from canonical GitHub repository",
        token=token,
    )
    return RepoVerification(
        repo_id=repo_id,
        repo_type="space",
        url=space_url(slug),
        private=False,
        required_files=["README.md", "index.html"],
    )


def ensure_dataset(api: HfApi, token: str, slug: str) -> RepoVerification:
    repo_id = f"{NAMESPACE}/{slug}"
    api.create_repo(
        repo_id=repo_id,
        repo_type="dataset",
        private=False,
        exist_ok=True,
        token=token,
    )
    folder = DATASET_ROOT / slug
    if not folder.exists():
        raise FileNotFoundError(f"Missing dataset package directory: {folder}")
    api.upload_folder(
        repo_id=repo_id,
        repo_type="dataset",
        folder_path=folder,
        commit_message=f"Publish {slug} dataset from canonical GitHub repository",
        token=token,
    )
    return RepoVerification(
        repo_id=repo_id,
        repo_type="dataset",
        url=dataset_url(slug),
        private=False,
        required_files=repo_required_files(folder),
    )


def ensure_collection(api: HfApi, token: str) -> tuple[str, str]:
    collection = None
    for candidate in api.list_collections(owner=NAMESPACE, limit=100, token=token):
        if candidate.title.strip() == COLLECTION_TITLE:
            collection = candidate
            break

    if collection is None:
        collection = api.create_collection(
            COLLECTION_TITLE,
            namespace=NAMESPACE,
            description=COLLECTION_DESCRIPTION,
            private=False,
            exists_ok=True,
            token=token,
        )
    else:
        collection = api.update_collection_metadata(
            collection.slug,
            title=COLLECTION_TITLE,
            description=COLLECTION_DESCRIPTION,
            private=False,
            token=token,
        )

    for item_type, item_id in COLLECTION_ITEMS:
        api.add_collection_item(
            collection.slug,
            item_id=item_id,
            item_type=item_type,
            exists_ok=True,
            token=token,
        )

    refreshed = api.get_collection(collection.slug, token=token)
    object_ids = {
        (item.item_type, item.item_id): item.item_object_id for item in refreshed.items
    }
    for index, key in enumerate(COLLECTION_ITEMS):
        object_id = object_ids.get(key)
        if object_id:
            api.update_collection_item(
                refreshed.slug,
                object_id,
                position=index,
                token=token,
            )

    final = api.get_collection(refreshed.slug, token=token)
    return final.slug, normalize_collection_url(final.url)


def verify_repo(api: HfApi, token: str, verification: RepoVerification) -> dict:
    info = api.repo_info(verification.repo_id, repo_type=verification.repo_type, token=token)
    files = set(api.list_repo_files(verification.repo_id, repo_type=verification.repo_type, token=token))
    missing = [name for name in verification.required_files if name not in files]
    if missing:
        raise RuntimeError(f"{verification.repo_id} missing files: {', '.join(missing)}")
    if getattr(info, "private", False):
        raise RuntimeError(f"{verification.repo_id} is not public")
    return {
        "repo_id": verification.repo_id,
        "repo_type": verification.repo_type,
        "url": verification.url,
        "private": bool(getattr(info, "private", False)),
        "required_files": verification.required_files,
    }


def verify_collection(api: HfApi, token: str, collection_slug: str) -> dict:
    collection = api.get_collection(collection_slug, token=token)
    actual = {(item.item_type, item.item_id) for item in collection.items}
    expected = set(COLLECTION_ITEMS)
    missing = sorted(expected.difference(actual))
    if missing:
        raise RuntimeError(f"Collection missing items: {missing}")
    return {
        "slug": collection.slug,
        "title": collection.title,
        "url": normalize_collection_url(collection.url),
        "items": [
            {"item_type": item.item_type, "item_id": item.item_id, "position": item.position}
            for item in sorted(collection.items, key=lambda entry: entry.position)
            if (item.item_type, item.item_id) in expected
        ],
    }


def write_status(summary: dict) -> None:
    generated_at = summary["generated_at"]
    spaces = "\n".join(f"- {entry['repo_id']}: <{entry['url']}>" for entry in summary["spaces"])
    datasets = "\n".join(f"- {entry['repo_id']}: <{entry['url']}>" for entry in summary["datasets"])
    STATUS_PATH.write_text(
        "\n".join(
            [
                "# Hugging Face Publication Status",
                "",
                f"Generated at: {generated_at}",
                "",
                "## Spaces",
                "",
                spaces,
                "",
                "## Datasets",
                "",
                datasets,
                "",
                "## Collection",
                "",
                f"- AegisLayer Core: <{summary['collection']['url']}>",
                "",
                "## Verification",
                "",
                "- All listed repositories exist.",
                "- All listed repositories are public.",
                "- All Spaces contain `README.md` and `index.html`.",
                "- All datasets contain `README.md` and their published package files.",
                "- The collection contains the expected Space and dataset items.",
                "",
                "## Remaining Owner-Only Actions",
                "",
                "- Update the AEGISLAYER organization profile and pinned items.",
                "- Post launch announcements using the prepared copy.",
                "- Adjust collection or repo pin ordering in the UI if desired.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def update_profile_links(summary: dict) -> None:
    text = PROFILE_LINKS_PATH.read_text(encoding="utf-8")
    live_space_lines = [
        "## Published Spaces",
        "",
        "- Organization Home: <https://huggingface.co/spaces/AEGISLAYER/README>",
        *[f"- {entry['repo_id'].split('/', 1)[1]}: <{entry['url']}>" for entry in summary["spaces"] if not entry["repo_id"].endswith("/README")],
        "",
        "## Published Datasets",
        "",
        *[f"- {entry['repo_id'].split('/', 1)[1]}: <{entry['url']}>" for entry in summary["datasets"]],
        "",
        "## Published Collection",
        "",
        f"- AegisLayer Core: <{summary['collection']['url']}>",
        "",
    ]
    marker = "If a new public destination is needed, add it to this file first so later profile and workflow content stays aligned.\n"
    if marker not in text:
        raise RuntimeError("PROFILE_LINKS.md marker not found")
    prefix = text.split(marker, 1)[0] + marker + "\n"
    PROFILE_LINKS_PATH.write_text(prefix + "\n".join(live_space_lines), encoding="utf-8")


def update_release_feed(summary: dict) -> None:
    text = RELEASE_FEED_PATH.read_text(encoding="utf-8")
    replacement = "\n".join(
        [
            "## Initial Entries",
            "",
            "1. **Portfolio refresh**",
            "   - Summary: organization-home Space now reflects the full AegisLayer portfolio generated from GitHub.",
            "   - Link: <https://huggingface.co/spaces/AEGISLAYER/README>",
            "   - Feedback prompt: Which public resource should get a deeper guided walkthrough next?",
            "2. **Dataset package release**",
            "   - Summary: three synthetic deterministic datasets now document governance scenarios, threat-to-control mappings, and architecture catalog entries.",
            f"   - Link: <{summary['datasets'][0]['url']}>, <{summary['datasets'][1]['url']}>, <{summary['datasets'][2]['url']}>",
            "   - Feedback prompt: Which additional synthetic fields would improve clarity without implying production telemetry?",
            "3. **Governance library update**",
            "   - Summary: the library Space now indexes ADRs, RFCs, glossary content, patterns, and release materials.",
            f"   - Link: <{next(entry['url'] for entry in summary['spaces'] if entry['repo_id'].endswith('governance-library'))}>",
            "   - Feedback prompt: Which documentation entry points are still difficult to navigate?",
            "4. **Collection published**",
            "   - Summary: the AegisLayer Core collection now groups the public Spaces and dataset packages under one discoverable collection.",
            f"   - Link: <{summary['collection']['url']}>",
            "   - Feedback prompt: Which artifact should be featured more prominently inside the collection?",
            "",
        ]
    )
    if "## Initial Entries\n" not in text:
        raise RuntimeError("RELEASE_FEED.md section not found")
    prefix, _ = text.split("## Initial Entries\n", 1)
    RELEASE_FEED_PATH.write_text(prefix + replacement, encoding="utf-8")


def update_owner_guide(collection_url: str) -> None:
    OWNER_GUIDE_PATH.write_text(
        "\n".join(
            [
                "# Owner Launch Guide",
                "",
                "## Account-Level Actions Required",
                "",
                "These steps still require Hugging Face or GitHub account permissions and remain outside the fully automated launch workflow.",
                "",
                "## Hugging Face Organization Profile",
                "",
                "1. Open the AEGISLAYER organization profile editor.",
                "2. Paste the approved card copy from `huggingface/ORGANIZATION_CARD.md`.",
                "3. Apply the short and long descriptions from `huggingface/ORGANIZATION_PROFILE_COPY.md`.",
                "4. Add the verified public links from `huggingface/PROFILE_LINKS.md`.",
                "",
                "## Pinning Repositories",
                "",
                "1. Pin `AEGISLAYER/README`.",
                "2. Pin the most useful supporting Spaces, starting with `architecture-explorer`, `policy-playground`, and `governance-library`.",
                "3. Pin the AegisLayer Core collection after verifying the live URL.",
                "",
                "## What Is Automated",
                "",
                "- creation or update of the public Static Space repositories",
                "- publication of generated Space assets from `dist/huggingface/<slug>/`",
                "- creation or update of the public dataset repositories",
                "- upload of dataset package contents from `huggingface/datasets/<slug>/`",
                "- creation or update of the AegisLayer Core collection",
                "- repository publication status updates under `huggingface/`",
                "",
                "## Live Collection",
                "",
                f"- AegisLayer Core: <{collection_url}>",
                "",
                "## GitHub Repository Variables And Secrets",
                "",
                "1. Keep secret `HF_TOKEN` configured.",
                "2. Keep variable `HF_ORG` set to `AEGISLAYER` if you want the generic portfolio publish workflows to keep using the organization namespace.",
                "3. Keep variable `HF_SPACE_REPO` set for the preserved `AEGISLAYER/README` Space.",
                "",
                "## Triggering Workflows",
                "",
                "1. Run `Launch Hugging Face Promotion` for full launch or reconciliation.",
                "2. Run `Publish Hugging Face Space` to republish only `AEGISLAYER/README`.",
                "3. Run `Publish Hugging Face Portfolio` for targeted Space-only republishes.",
                "",
                "## Posting Announcements",
                "",
                "1. Use the channel copy in `promotion/ANNOUNCEMENT_COPY.md`.",
                "2. Link directly to the live Space, dataset, or collection URLs recorded in `huggingface/PUBLICATION_STATUS.md`.",
                "3. Keep the scope note and feedback prompt intact.",
                "",
                "## Rollback",
                "",
                "1. Re-run launch or targeted publish workflows from the last known good commit.",
                "2. If a specific Space or dataset is incorrect, republish only that artifact from the prior commit.",
                "3. If profile or pinning changes are incorrect, restore the previous approved copy in the Hugging Face UI.",
                "4. If collection order needs adjustment, update it in the Hugging Face UI and note the correction in the release log.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def update_collection_guide(collection_url: str) -> None:
    COLLECTION_GUIDE_PATH.write_text(
        "\n".join(
            [
                "# Collection Publishing Guide",
                "",
                "## Purpose",
                "",
                "This package prepares the copy and ordering required to create or update Hugging Face Collections for AegisLayer.",
                "",
                "## What Can Be Automated",
                "",
                "- generation of collection descriptions and ordered item manifests in this repository",
                "- release packaging in `dist/huggingface/collections/`",
                "- validation that collection items point to canonical public artifacts",
                "- creation or update of the AegisLayer Core collection through `huggingface_hub`",
                "- insertion of the expected Space and dataset items with stable ordering",
                "",
                "## What Still Requires Owner Action",
                "",
                "- pinning or reordering Collections in the Hugging Face UI if you want a different visual presentation",
                "- deciding whether to create additional thematic Collections beyond AegisLayer Core",
                "",
                "## Current Live Collection",
                "",
                f"- AegisLayer Core: <{collection_url}>",
                "",
                "## Publishing Steps",
                "",
                "1. Run `Launch Hugging Face Promotion` to create or reconcile the collection automatically.",
                "2. Review the collection URL recorded in `huggingface/PUBLICATION_STATUS.md`.",
                "3. If desired, fine-tune pinning or visual order in the Hugging Face UI.",
                "4. Record any owner-side adjustments back into the release notes or launch posts.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_summary(summary: dict) -> None:
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def main() -> int:
    token = require_token()
    api = api_client(token)

    spaces = [ensure_space(api, token, slug) for slug in SPACE_SLUGS]
    datasets = [ensure_dataset(api, token, slug) for slug in DATASET_SLUGS]
    collection_slug, collection_url = ensure_collection(api, token)

    verified_spaces = [
        verify_repo(
            api,
            token,
            RepoVerification(
                repo_id=f"{NAMESPACE}/README",
                repo_type="space",
                url=space_url("README"),
                private=False,
                required_files=["README.md", "index.html"],
            ),
        )
    ]
    verified_spaces.extend(verify_repo(api, token, repo) for repo in spaces)
    verified_datasets = [verify_repo(api, token, repo) for repo in datasets]
    verified_collection = verify_collection(api, token, collection_slug)

    summary = {
        "generated_at": datetime.now(UTC).isoformat(),
        "spaces": verified_spaces,
        "datasets": verified_datasets,
        "collection": verified_collection,
    }

    write_status(summary)
    update_profile_links(summary)
    update_release_feed(summary)
    update_owner_guide(collection_url)
    update_collection_guide(collection_url)
    write_summary(summary)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())