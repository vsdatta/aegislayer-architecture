#!/usr/bin/env python3
"""Validate a curated set of external links used by Hugging Face assets."""

from __future__ import annotations

from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPO = Path(__file__).resolve().parents[1]
URLS = [
    "https://github.com/vsdatta/aegislayer-architecture",
    "https://vsdatta.github.io/aegislayer-architecture/",
    "https://aegislayer.ai",
    "https://github.com/vsdatta/aegislayer-architecture/blob/main/SECURITY.md",
    "https://github.com/vsdatta/aegislayer-architecture/blob/main/CHANGELOG.md",
    "https://vsdatta.github.io/aegislayer-architecture/RESEARCH_PROGRAM/",
    "https://github.com/vsdatta/aegislayer-architecture/tree/main/reference-sdk",
    "https://huggingface.co/spaces/AEGISLAYER/README",
]


def check(url: str) -> tuple[bool, str]:
    request = Request(url, headers={"User-Agent": "aegislayer-link-validator/1.0"})
    try:
        with urlopen(request, timeout=20) as response:
            return 200 <= response.status < 400, f"{response.status}"
    except HTTPError as exc:
        return False, f"HTTP {exc.code}"
    except URLError as exc:
        return False, str(exc.reason)


def main() -> int:
    failures = []
    for url in URLS:
        ok, detail = check(url)
        print(f"{url} -> {detail}")
        if not ok:
            failures.append(url)
    if failures:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())