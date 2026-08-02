#!/usr/bin/env python3
"""Publish generated Hugging Face Space exports to existing repositories."""

from __future__ import annotations

from argparse import ArgumentParser
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO / "huggingface" / "spaces" / "manifest.json"
DIST_ROOT = REPO / "dist" / "huggingface"


def run(cmd: list[str], cwd: Path | None = None, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        check=True,
        capture_output=capture,
    )


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def load_overrides() -> dict[str, str]:
    raw = os.environ.get("HF_SPACE_MANIFEST", "").strip()
    if not raw:
        return {}
    if raw.startswith("{"):
        data = json.loads(raw)
        return {str(key): str(value) for key, value in data.items()}
    path = Path(raw)
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        return {str(key): str(value) for key, value in data.items()}
    raise ValueError("HF_SPACE_MANIFEST must be JSON text or a valid file path")


def env_key_for_slug(slug: str) -> str:
    return f"HF_SPACE_REPO_{slug.upper().replace('-', '_')}"


def resolve_target(space: dict, overrides: dict[str, str], default_org: str | None) -> tuple[str, str]:
    explicit = os.environ.get(env_key_for_slug(space["slug"]), "").strip()
    legacy = os.environ.get("HF_SPACE_REPO", "").strip() if space["slug"] == "organization-home" else ""
    raw_target = explicit or legacy or overrides.get(space["slug"], "") or space["default_repo_name"]
    if "/" in raw_target:
        org, repo = raw_target.split("/", 1)
        return org, repo
    if not default_org:
        raise ValueError(f"Missing HF_ORG for {space['slug']}")
    return default_org, raw_target


def parse_args() -> ArgumentParser:
    parser = ArgumentParser(description="Publish generated Hugging Face Spaces.")
    parser.add_argument("--space", dest="space_slug", help="Publish only one space slug.")
    parser.add_argument("--dry-run", action="store_true", help="Show publication summary without pushing changes.")
    return parser


def changed_files(repo_dir: Path) -> list[str]:
    result = run(["git", "status", "--short"], cwd=repo_dir, capture=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def publish_space(space: dict, org: str, repo_name: str, token: str | None, dry_run: bool, source_commit: str) -> dict:
    dist_dir = DIST_ROOT / space["slug"]
    if not dist_dir.exists():
        raise FileNotFoundError(f"Missing built space export: {dist_dir}")

    live_url = f"https://huggingface.co/spaces/{org}/{repo_name}"
    if dry_run:
        return {
            "space": space["slug"],
            "target_repository": f"{org}/{repo_name}",
            "source_commit": source_commit,
            "files_changed": "dry-run",
            "result": "dry-run",
            "live_url": live_url,
        }

    if not token:
        raise ValueError("HF_TOKEN is required for publication")

    remote = f"https://user:{token}@huggingface.co/spaces/{org}/{repo_name}"
    with tempfile.TemporaryDirectory() as tmp:
        repo_dir = Path(tmp) / repo_name
        run(["git", "clone", remote, str(repo_dir)])
        for item in repo_dir.iterdir():
            if item.name == ".git":
                continue
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
        for item in dist_dir.iterdir():
            target = repo_dir / item.name
            if item.is_dir():
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)
        run(["git", "config", "user.name", "github-actions[bot]"], cwd=repo_dir)
        run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], cwd=repo_dir)
        run(["git", "add", "--all"], cwd=repo_dir)
        files_changed = changed_files(repo_dir)
        if not files_changed:
            return {
                "space": space["slug"],
                "target_repository": f"{org}/{repo_name}",
                "source_commit": source_commit,
                "files_changed": [],
                "result": "no-change",
                "live_url": live_url,
            }
        run(["git", "commit", "-m", f"Publish {space['slug']} from canonical GitHub repo"], cwd=repo_dir)
        run(["git", "push", "origin", "HEAD:main"], cwd=repo_dir)
        return {
            "space": space["slug"],
            "target_repository": f"{org}/{repo_name}",
            "source_commit": source_commit,
            "files_changed": files_changed,
            "result": "published",
            "live_url": live_url,
        }


def main() -> int:
    parser = parse_args()
    args = parser.parse_args()
    manifest = load_manifest()
    overrides = load_overrides()
    default_org = os.environ.get("HF_ORG", "").strip() or None
    if args.dry_run and not default_org:
        default_org = "AEGISLAYER"
    token = os.environ.get("HF_TOKEN", "").strip() or None
    source_commit = run(["git", "rev-parse", "HEAD"], cwd=REPO, capture=True).stdout.strip()

    spaces = manifest["spaces"]
    if args.space_slug:
        spaces = [space for space in spaces if space["slug"] == args.space_slug]
        if not spaces:
            print(f"Unknown space slug: {args.space_slug}")
            return 1

    summary = []
    for space in spaces:
        org, repo_name = resolve_target(space, overrides, default_org)
        summary.append(publish_space(space, org, repo_name, token, args.dry_run, source_commit))

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())