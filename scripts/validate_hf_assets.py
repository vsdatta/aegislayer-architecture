#!/usr/bin/env python3
"""Validate Hugging Face Space assets, metadata, and publication rules."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
SPACES_ROOT = REPO / "huggingface" / "spaces"
DIST_ROOT = REPO / "dist" / "huggingface"
MANIFEST = json.loads((SPACES_ROOT / "manifest.json").read_text(encoding="utf-8"))
APPROVED_TAGS = {
    "ai-governance",
    "ai-security",
    "agentic-ai",
    "trustworthy-ai",
    "responsible-ai",
    "zero-trust",
    "runtime-security",
    "human-in-the-loop",
    "llm-security",
    "autonomous-agents",
    "cybersecurity",
    "governance",
    "explainability",
    "auditability",
}
REQUIRED_METADATA = [
    "title",
    "emoji",
    "colorFrom",
    "colorTo",
    "sdk",
    "app_file",
    "pinned",
    "license",
    "tags",
    "short_description",
]
PROHIBITED_PATTERNS = [
    r"google-analytics",
    r"gtag\(",
    r"plausible",
    r"mixpanel",
    r"segment",
    r"hotjar",
    r"fetch\(",
    r"XMLHttpRequest",
    r"WebSocket",
    r"navigator\.sendBeacon",
    r"iframe\s+src=\"https?://",
    r"<script[^>]+src=\"https?://",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_front_matter(readme_text: str) -> dict[str, object]:
    match = re.match(r"^---\n(.*?)\n---\n", readme_text, flags=re.DOTALL)
    if not match:
        raise ValueError("Missing YAML front matter")
    metadata: dict[str, object] = {}
    current_key: str | None = None
    for line in match.group(1).splitlines():
        if line.endswith(":") and ": " not in line:
            current_key = line[:-1]
            if current_key == "tags":
                metadata[current_key] = []
            continue
        if line.startswith("  - ") and current_key == "tags":
            metadata.setdefault("tags", []).append(line[4:])
            continue
        if ": " in line:
            key, value = line.split(": ", 1)
            current_key = key
            metadata[key] = value
    return metadata


def validate_metadata(space_dir: Path, slug: str) -> list[str]:
    errors: list[str] = []
    metadata = parse_front_matter(read(space_dir / "README.md"))
    for key in REQUIRED_METADATA:
        if key not in metadata:
            errors.append(f"Missing metadata field {key} in {space_dir.relative_to(REPO)}")
    tags = metadata.get("tags", [])
    if not isinstance(tags, list) or not tags:
        errors.append(f"Missing tags list in {space_dir.relative_to(REPO)}")
    else:
        invalid = [tag for tag in tags if tag not in APPROVED_TAGS]
        if invalid:
            errors.append(f"Invalid tags for {slug}: {', '.join(invalid)}")
    if metadata.get("sdk") != "static":
        errors.append(f"Space {slug} must use sdk: static")
    if metadata.get("app_file") != "index.html":
        errors.append(f"Space {slug} must use app_file: index.html")
    if metadata.get("license") != "apache-2.0":
        errors.append(f"Space {slug} must use license: apache-2.0")
    return errors


def validate_html(space_dir: Path, slug: str, all_slugs: list[str]) -> list[str]:
    errors: list[str] = []
    html = read(space_dir / "index.html")
    js = read(space_dir / "assets" / "js" / "app.js")
    css = read(space_dir / "assets" / "css" / "styles.css")

    required_checks = {
        "viewport": 'name="viewport"' in html,
        "skip-link": "skip-link" in html,
        "main-content": "<main" in html,
        "disclaimer": "conceptual" in html.lower() or "deterministic" in html.lower(),
        "local-css": 'href="assets/css/styles.css"' in html,
        "local-js": 'src="assets/js/app.js"' in html,
        "reduced-motion": "prefers-reduced-motion" in css,
        "focus-styles": ":focus" in css,
    }
    for name, ok in required_checks.items():
        if not ok:
            errors.append(f"Missing {name} requirement in {space_dir.relative_to(REPO)}")

    for pattern in PROHIBITED_PATTERNS:
        if re.search(pattern, html, flags=re.IGNORECASE) or re.search(pattern, js, flags=re.IGNORECASE):
            errors.append(f"Prohibited pattern {pattern!r} found in {space_dir.relative_to(REPO)}")

    for other_slug in all_slugs:
        if other_slug == slug:
            continue
        if f"/AEGISLAYER/{other_slug}" not in html and f"/AEGISLAYER/{other_slug}" not in read(space_dir / "README.md"):
            errors.append(f"Cross-link to {other_slug} missing in {space_dir.relative_to(REPO)}")

    return errors


def validate_space_tree(root: Path, label: str) -> list[str]:
    errors: list[str] = []
    all_slugs = [space["slug"] for space in MANIFEST["spaces"]]
    for space in MANIFEST["spaces"]:
        space_dir = root / space["slug"]
        for relative in [
            Path("README.md"),
            Path("index.html"),
            Path("assets/css/styles.css"),
            Path("assets/js/app.js"),
        ]:
            if not (space_dir / relative).exists():
                errors.append(f"Missing {label} file: {(space_dir / relative).relative_to(REPO)}")
        if errors:
            continue
        errors.extend(validate_metadata(space_dir, space["slug"]))
        errors.extend(validate_html(space_dir, space["slug"], all_slugs))

    return errors


def validate_manifest() -> list[str]:
    errors: list[str] = []
    spaces = MANIFEST.get("spaces")
    if not isinstance(spaces, list) or len(spaces) != 8:
        errors.append("Space manifest must contain exactly 8 spaces")
        return errors
    required_keys = {
        "slug",
        "default_repo_name",
        "title",
        "emoji",
        "colorFrom",
        "colorTo",
        "short_description",
        "pinned",
        "tags",
        "hero_eyebrow",
        "hero_title",
        "hero_summary",
        "disclaimer",
        "sections",
    }
    for space in spaces:
        missing = sorted(required_keys.difference(space))
        if missing:
            errors.append(f"Manifest entry {space.get('slug', '<unknown>')} missing: {', '.join(missing)}")
    return errors


def main() -> int:
    errors = []
    errors.extend(validate_manifest())
    errors.extend(validate_space_tree(SPACES_ROOT, "source"))
    errors.extend(validate_space_tree(DIST_ROOT, "dist"))
    legacy_dir = REPO / "huggingface" / "hf_space"
    if not legacy_dir.exists():
        errors.append("Legacy hf_space export missing")
    for name in ["README.md", "index.html", "assets/css/styles.css", "assets/js/app.js"]:
        if not (legacy_dir / name).exists():
            errors.append(f"Legacy hf_space missing {name}")

    if errors:
        print("Hugging Face asset validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Hugging Face asset validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())