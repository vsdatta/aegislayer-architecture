#!/usr/bin/env python3
"""Validate required static demo artifacts and baseline semantics."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
DEMO = REPO / "interactive-demo"
REQUIRED = [
    DEMO / "index.html",
    DEMO / "assets/css/styles.css",
    DEMO / "assets/js/app.js",
    DEMO / "README.md",
]


def main() -> int:
    missing = [str(p.relative_to(REPO)) for p in REQUIRED if not p.exists()]
    if missing:
        print("Missing demo files:")
        for item in missing:
            print(f"- {item}")
        return 1

    html = (DEMO / "index.html").read_text(encoding="utf-8")
    js = (DEMO / "assets/js/app.js").read_text(encoding="utf-8")

    checks = {
        "semantic main element": "<main" in html,
        "accessible skip link": "skip-link" in html,
        "scenario data": "const scenarios" in js,
        "threat explorer": "threatMappings" in js,
    }

    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        print("Demo validation failed:")
        for name in failed:
            print(f"- {name}")
        return 1

    print("Demo validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
