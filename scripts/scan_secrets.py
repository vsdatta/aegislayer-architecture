#!/usr/bin/env python3
"""Lightweight obvious secret-pattern scanner for repository text files."""

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]

PATTERNS = {
    "aws_access_key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private_key_block": re.compile(r"-----BEGIN (RSA|EC|OPENSSH|PRIVATE) KEY-----"),
    "github_pat": re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    "slack_token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
}

SKIP_DIRS = {".git", ".venv", "site", "node_modules", "__pycache__"}


def iter_files() -> list[Path]:
    paths: list[Path] = []
    for path in REPO.rglob("*"):
        if path.is_dir():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".woff", ".woff2"}:
            continue
        paths.append(path)
    return paths


def main() -> int:
    hits: list[str] = []
    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for key, pattern in PATTERNS.items():
            if pattern.search(text):
                hits.append(f"{path.relative_to(REPO)} :: {key}")

    if hits:
        print("Potential secret patterns found:")
        for hit in hits:
            print(f"- {hit}")
        return 1

    print("No obvious secret patterns detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
