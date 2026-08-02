#!/usr/bin/env python3
"""Check Markdown relative links resolve to existing files."""

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def main() -> int:
    failures: list[str] = []
    for md in REPO.rglob("*.md"):
        if any(part in {".venv", "site", "node_modules"} for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip()
            if raw.startswith(SKIP_PREFIXES):
                continue
            target = raw.split("#", maxsplit=1)[0]
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                failures.append(f"{md.relative_to(REPO)} -> {raw}")

    if failures:
        print("Broken relative links:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Relative link audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
