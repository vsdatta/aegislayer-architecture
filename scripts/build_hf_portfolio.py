#!/usr/bin/env python3
"""Build reproducible Hugging Face Spaces from shared canonical content."""

from __future__ import annotations

from argparse import ArgumentParser
from html import escape
import json
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[1]
SPACES_ROOT = REPO / "huggingface" / "spaces"
DIST_ROOT = REPO / "dist" / "huggingface"
LEGACY_EXPORT = REPO / "huggingface" / "hf_space"
MANIFEST_PATH = SPACES_ROOT / "manifest.json"
SITE_DATA_PATH = SPACES_ROOT / "shared" / "data" / "site.json"
LICENSE = "apache-2.0"
SDK = "static"
APP_FILE = "index.html"
TAGLINE = "No analytics. No tracking. No external execution. No secrets required."


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def slug_to_label(slug: str) -> str:
    return slug.replace("-", " ").title()


def render_metadata(space: dict) -> str:
    return "\n".join(
        [
            "---",
            f"title: {space['title']}",
            f"emoji: {space['emoji']}",
            f"colorFrom: {space['colorFrom']}",
            f"colorTo: {space['colorTo']}",
            f"sdk: {SDK}",
            f"app_file: {APP_FILE}",
            f"pinned: {'true' if space['pinned'] else 'false'}",
            f"license: {LICENSE}",
            "tags:",
            *[f"  - {tag}" for tag in space["tags"]],
            f"short_description: {space['short_description']}",
            "---",
            "",
        ]
    )


def render_readme(space: dict, site: dict, spaces: list[dict]) -> str:
    metadata = render_metadata(space)
    cross_links = [
        f"- [{item['title']}](https://huggingface.co/spaces/AEGISLAYER/{item['slug']})"
        for item in spaces
        if item["slug"] != space["slug"]
    ]
    sections = [
        f"## {section['heading']}\n\n{section['body']}"
        + (
            "\n\n" + "\n".join(f"- {entry}" for entry in section.get("items", []))
            if section.get("items")
            else ""
        )
        for section in space["sections"]
    ]
    docs = "\n".join(
        f"- [{entry['title']}]({entry['url']}): {entry['summary']}" for entry in site["documentation"]
    )
    return (
      f"{metadata}## {space['title']}\n\n"
        f"{space['hero_summary']}\n\n"
        "## Canonical Links\n\n"
        f"- GitHub repository: [{site['links']['github_repo']}]({site['links']['github_repo']})\n"
        f"- GitHub Pages docs: [{site['links']['github_pages']}]({site['links']['github_pages']})\n"
        f"- AegisLayer website: [{site['links']['website']}]({site['links']['website']})\n"
        f"- Security policy: [{site['links']['security']}]({site['links']['security']})\n"
        f"- Research program: [{site['links']['research']}]({site['links']['research']})\n"
        f"- Reference SDK: [{site['links']['sdk']}]({site['links']['sdk']})\n\n"
        + "\n\n".join(sections)
        + "\n\n## Documentation Jump Points\n\n"
        + docs
        + "\n\n## Other AegisLayer Spaces\n\n"
        + "\n".join(cross_links)
        + "\n\n## Public Disclaimer\n\n"
        + space["disclaimer"]
        + "\n\n"
        + TAGLINE
        + "\n"
    )


def render_nav(spaces: list[dict], current_slug: str) -> str:
    items = []
    for space in spaces:
        active = ' aria-current="page"' if space["slug"] == current_slug else ""
        items.append(
            f'<li><a href="https://huggingface.co/spaces/AEGISLAYER/{space["slug"]}"{active}>{escape(space["title"])}</a></li>'
        )
    return "\n".join(items)


def render_cards(site: dict, spaces: list[dict], current_slug: str) -> str:
    cards = []
    for space in spaces:
        cards.append(
            "\n".join(
                [
                    '<article class="space-card">',
                    f"  <p class=\"space-emoji\">{escape(space['emoji'])}</p>",
                    f"  <h3>{escape(space['title'])}</h3>",
                    f"  <p>{escape(space['short_description'])}</p>",
                    '  <div class="card-actions">',
                    f'    <a class="button secondary" href="https://huggingface.co/spaces/AEGISLAYER/{space["slug"]}">Open Space</a>',
                    f'    <a class="button ghost" href="{site["links"]["github_repo"]}">Canonical Source</a>',
                    "  </div>",
                    "</article>",
                ]
            )
        )
    return "\n".join(cards)


def render_section(section: dict, site: dict, spaces: list[dict], site_data: dict) -> str:
    section_type = section.get("type")
    if section_type == "space-grid":
        body = f'<div class="space-grid">{render_cards(site, spaces, "")}</div>'
    elif section_type == "architecture-layers":
        body = "".join(
            f'<article class="data-card"><h3>{escape(item["name"])}</h3><p>{escape(item["purpose"])}</p><a href="{item["docs"]}">Read lifecycle</a></article>'
            for item in site_data["architecture_layers"]
        )
    elif section_type == "trust-boundaries":
        body = "".join(
            f'<article class="data-card"><h3>{escape(item["name"])}</h3><p>{escape(item["summary"])}</p><a href="{item["docs"]}">Read boundary detail</a></article>'
            for item in site_data["trust_boundaries"]
        )
    elif section_type in {
      "governance-scenarios",
      "evidence-chain",
      "threat-map",
      "connector-scenarios",
      "runtime-states",
      "governance-library",
    }:
      body = '<div id="interactive-region" class="interactive-region" aria-live="polite"></div>'
    else:
      body = '<article class="data-card"><h3>Static reference section</h3><p>This section intentionally stays static and points readers to the canonical documentation and linked Spaces.</p></article>'

    items = ""
    if section.get("items"):
        items = '<ul class="bullet-list">' + "".join(
            f"<li>{escape(entry)}</li>" for entry in section["items"]
        ) + "</ul>"

    return (
        '<section class="panel section-panel">'
        f"<div class=\"section-header\"><h2>{escape(section['heading'])}</h2><p>{escape(section['body'])}</p></div>"
        f"{items}<div class=\"section-body\">{body}</div></section>"
    )


def render_html(space: dict, site_data: dict, spaces: list[dict]) -> str:
    nav = render_nav(spaces, space["slug"])
    sections = "\n".join(
        render_section(section, site_data, spaces, site_data) for section in space["sections"]
    )
    actions = "\n".join(
        [
            f'<a class="button primary" href="{site_data["links"]["github_pages"]}">Read the documentation</a>',
            f'<a class="button secondary" href="{site_data["links"]["sdk"]}">Explore the SDK</a>',
            f'<a class="button secondary" href="{site_data["links"]["research"]}">View research</a>',
            f'<a class="button ghost" href="{site_data["links"]["contribute"]}">Contribute</a>',
            f'<a class="button ghost" href="{site_data["links"]["security"]}">Report a security issue</a>',
        ]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(space['title'])}</title>
    <meta name="description" content="{escape(space['short_description'])}">
    <link rel="stylesheet" href="assets/css/styles.css">
  </head>
  <body data-space="{escape(space['slug'])}">
    <a class="skip-link" href="#content">Skip to content</a>
    <header class="hero">
      <div class="hero-backdrop"></div>
      <div class="hero-inner">
        <p class="eyebrow">{escape(space['hero_eyebrow'])}</p>
        <h1>{escape(space['hero_title'])}</h1>
        <p class="lede">{escape(space['hero_summary'])}</p>
        <p class="disclaimer">{escape(space['disclaimer'])}</p>
        <div class="action-row">{actions}</div>
      </div>
    </header>

    <div class="page-shell">
      <aside class="panel sidebar" aria-label="Portfolio navigation">
        <h2>Portfolio</h2>
        <nav>
          <ul class="space-nav">{nav}</ul>
        </nav>
        <div class="sidebar-block">
          <h3>Canonical Source</h3>
          <a href="{site_data['links']['github_repo']}">GitHub repository</a>
          <a href="{site_data['links']['github_pages']}">GitHub Pages docs</a>
          <a href="{site_data['links']['website']}">AegisLayer website</a>
        </div>
      </aside>

      <main id="content" class="content" tabindex="-1">
        <section class="panel summary-panel">
          <div class="summary-grid">
            <article>
              <h2>Developer</h2>
              <p>{escape(site_data['organization']['developer'])}</p>
            </article>
            <article>
              <h2>Public Scope</h2>
              <p>{escape(site_data['organization']['scope'])}</p>
            </article>
            <article>
              <h2>Principles</h2>
              <ol>{''.join(f'<li>{escape(item)}</li>' for item in site_data['organization']['principles'])}</ol>
            </article>
          </div>
        </section>
        {sections}
      </main>
    </div>

    <footer class="footer">
      <div>
        <p>{TAGLINE}</p>
        <p>Live Space directory uses deterministic repository-owned content only.</p>
      </div>
      <div class="footer-links">
        <a href="{site_data['links']['release_notes']}">Release notes</a>
        <a href="{site_data['links']['governance']}">Governance docs</a>
        <a href="{site_data['links']['threat_model']}">Threat model</a>
      </div>
    </footer>

    <script src="assets/js/app.js"></script>
  </body>
</html>
"""


def render_css() -> str:
    return """\
:root {
  --bg: #f4f5ef;
  --surface: rgba(255, 255, 255, 0.9);
  --surface-strong: #fbfbf7;
  --ink: #17221c;
  --muted: #445149;
  --line: #cfd6cb;
  --brand: #18543d;
  --brand-strong: #103c2b;
  --signal: #bd7b22;
  --signal-strong: #865410;
  --focus: #0f6fd6;
  --shadow: 0 20px 50px rgba(17, 26, 19, 0.12);
  --sans: "Avenir Next", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  --serif: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
  --mono: "JetBrains Mono", "SFMono-Regular", Consolas, monospace;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at top left, rgba(188, 222, 199, 0.65), transparent 32%),
    radial-gradient(circle at right 15%, rgba(241, 213, 172, 0.45), transparent 28%),
    linear-gradient(180deg, #f7f8f2 0%, #eef1ea 100%);
  font-family: var(--sans);
}

a {
  color: var(--brand-strong);
}

a:focus,
button:focus,
select:focus,
input:focus {
  outline: 3px solid var(--focus);
  outline-offset: 3px;
}

.skip-link {
  position: absolute;
  left: -9999px;
  top: 0;
}

.skip-link:focus {
  left: 1rem;
  top: 1rem;
  z-index: 100;
  padding: 0.75rem 1rem;
  border-radius: 999px;
  background: #ffffff;
}

.hero {
  position: relative;
  overflow: hidden;
  padding: 4rem 1.25rem 3rem;
  background: linear-gradient(135deg, #102b21, #20563e 50%, #87632c 100%);
  color: #f6f8f1;
}

.hero-backdrop {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(75deg, rgba(255, 255, 255, 0.05), transparent 45%),
    repeating-linear-gradient(135deg, transparent, transparent 18px, rgba(255, 255, 255, 0.04) 18px, rgba(255, 255, 255, 0.04) 19px);
}

.hero-inner {
  position: relative;
  max-width: 1120px;
  margin: 0 auto;
}

.eyebrow {
  margin: 0 0 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.78rem;
  font-weight: 700;
}

h1,
h2,
h3 {
  font-family: var(--serif);
}

h1 {
  max-width: 14ch;
  margin: 0;
  font-size: clamp(2.4rem, 5vw, 4.6rem);
  line-height: 0.95;
}

.lede {
  max-width: 68ch;
  font-size: 1.05rem;
  line-height: 1.7;
}

.disclaimer {
  max-width: 72ch;
  padding-left: 1rem;
  border-left: 4px solid rgba(255, 222, 168, 0.95);
}

.action-row,
.card-actions,
.footer-links,
.bullet-list,
.space-nav,
.summary-grid,
.space-grid,
.section-body {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0.8rem 1.1rem;
  border-radius: 999px;
  border: 1px solid transparent;
  text-decoration: none;
  font-weight: 700;
}

.button.primary {
  background: #fff0;
  color: #f8fbf7;
  border-color: rgba(255, 255, 255, 0.55);
}

.button.secondary {
  background: #f5f7f2;
  color: var(--brand-strong);
}

.button.ghost {
  background: transparent;
  border-color: rgba(255, 255, 255, 0.35);
  color: #f8fbf7;
}

.page-shell {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  max-width: 1200px;
  margin: -1.75rem auto 0;
  padding: 0 1rem 2rem;
}

.panel {
  border: 1px solid var(--line);
  border-radius: 24px;
  background: var(--surface);
  box-shadow: var(--shadow);
}

.sidebar,
.summary-panel,
.section-panel {
  padding: 1.25rem;
}

.space-nav,
.bullet-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.space-nav a,
.sidebar-block a {
  display: block;
  padding: 0.7rem 0.8rem;
  border-radius: 16px;
  text-decoration: none;
}

.space-nav a[aria-current="page"] {
  background: #e8eee8;
  font-weight: 700;
}

.sidebar-block {
  display: grid;
  gap: 0.4rem;
  margin-top: 1.5rem;
}

.content {
  display: grid;
  gap: 1rem;
}

.summary-grid > article,
.space-card,
.data-card,
.interactive-card {
  flex: 1 1 220px;
  min-width: 0;
  padding: 1rem;
  border-radius: 18px;
  background: var(--surface-strong);
  border: 1px solid var(--line);
}

.space-card h3,
.data-card h3,
.interactive-card h3 {
  margin-top: 0;
}

.space-emoji {
  margin: 0;
  font-size: 1.6rem;
}

.section-header {
  margin-bottom: 1rem;
}

.section-body {
  align-items: stretch;
}

.interactive-region {
  display: grid;
  gap: 1rem;
  width: 100%;
}

.selector-row {
  display: grid;
  gap: 0.5rem;
}

label,
select,
input,
textarea {
  font: inherit;
}

select {
  width: 100%;
  min-height: 44px;
  padding: 0.75rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: #ffffff;
}

.tag-row,
.timeline,
.definition-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag,
.pill {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  border: 1px solid #d7ddd2;
  background: #eef4ee;
  font-size: 0.92rem;
}

.code-block {
  margin: 0;
  padding: 1rem;
  border-radius: 18px;
  background: #12251a;
  color: #d9efe0;
  font-family: var(--mono);
  overflow-x: auto;
}

.footer {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 1rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem 2rem;
}

@media (min-width: 960px) {
  .page-shell {
    grid-template-columns: minmax(260px, 300px) minmax(0, 1fr);
  }

  .sidebar {
    position: sticky;
    top: 1rem;
    align-self: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }

  *,
  *::before,
  *::after {
    animation: none !important;
    transition: none !important;
  }
}
"""


def base_datasets() -> dict:
    return {
        "governance-scenarios": [
            {
                "name": "Low-risk allow",
                "request_action": "read_report",
                "decision": "allow",
                "reason": "policy_and_authority_match",
                "approval": "not_required",
                "evidence": "identity, policy, connector, runtime_completed",
            },
            {
                "name": "Unauthorized deny",
                "request_action": "delete_resource",
                "decision": "deny",
                "reason": "authority_scope_mismatch",
                "approval": "not_reached",
                "evidence": "identity, authority_denial",
            },
            {
                "name": "High-impact approval required",
                "request_action": "rotate_secret",
                "decision": "conditional",
                "reason": "high_impact_requires_approval",
                "approval": "required",
                "evidence": "identity, policy, approval_request",
            },
            {
                "name": "Connector unavailable",
                "request_action": "sync_inventory",
                "decision": "deny",
                "reason": "connector_not_ready",
                "approval": "not_reached",
                "evidence": "identity, policy, connector_blocked",
            },
            {
                "name": "Capability expired",
                "request_action": "deploy_change",
                "decision": "revoke",
                "reason": "capability_expired",
                "approval": "granted_then_expired",
                "evidence": "capability_issued, monitoring, revoke_event",
            },
            {
                "name": "Capability revoked",
                "request_action": "publish_content",
                "decision": "revoke",
                "reason": "continuous_verification_revocation",
                "approval": "not_required",
                "evidence": "capability_issued, trust_drift, revoke_event",
            },
            {
                "name": "Evidence incomplete",
                "request_action": "approve_budget",
                "decision": "escalate",
                "reason": "evidence_incomplete",
                "approval": "held",
                "evidence": "identity, policy, missing_runtime_record",
            },
            {
                "name": "Containment triggered",
                "request_action": "execute_runbook",
                "decision": "contain",
                "reason": "incident_containment_triggered",
                "approval": "review_required",
                "evidence": "monitoring, containment, incident_review",
            },
        ],
        "evidence-chain": [
            {"event": "request_created", "record_type": "request", "details": "request_id and requested capability captured"},
            {"event": "identity_validated", "record_type": "identity", "details": "actor, issuer, authority mapping confirmed"},
            {"event": "policy_evaluated", "record_type": "policy", "details": "decision, risk, rationale stored"},
            {"event": "approval_recorded", "record_type": "approval", "details": "approver, scope, expiry, outcome stored"},
            {"event": "runtime_transition", "record_type": "runtime", "details": "state change and connector context appended"},
            {"event": "bundle_finalized", "record_type": "evidence", "details": "correlation, causation, hash, completeness summary"},
        ],
        "threat-map": [
            {"threat_id": "T-001", "family": "Unauthorized execution", "asset": "Runtime executor", "control": "Identity-first authorization", "adr": "ADR-0002", "docs": "https://vsdatta.github.io/aegislayer-architecture/THREAT_CONTROL_TRACEABILITY/", "residual_risk": "Stale authority data can still create timing windows until revalidation occurs."},
            {"threat_id": "T-002", "family": "Policy bypass", "asset": "Policy engine", "control": "Policy before execution", "adr": "ADR-0001", "docs": "https://vsdatta.github.io/aegislayer-architecture/POLICY_EVALUATION_LIFECYCLE/", "residual_risk": "Misconfigured policy logic can still produce incorrect outcomes if not reviewed."},
            {"threat_id": "T-003", "family": "Approval bypass", "asset": "Approval service", "control": "Human approval for high-impact actions", "adr": "ADR-0007", "docs": "https://vsdatta.github.io/aegislayer-architecture/APPROVAL_LIFECYCLE/", "residual_risk": "Approver fatigue or poor scope design can weaken effectiveness."},
            {"threat_id": "T-004", "family": "Connector abuse", "asset": "External connector", "control": "Capability-scoped connectors", "adr": "ADR-0005", "docs": "https://vsdatta.github.io/aegislayer-architecture/CONNECTOR_LIFECYCLE/", "residual_risk": "A trusted connector may still misbehave internally outside this architecture's visibility."},
            {"threat_id": "T-005", "family": "Evidence tampering", "asset": "Audit evidence", "control": "Evidence by design", "adr": "ADR-0003", "docs": "https://vsdatta.github.io/aegislayer-architecture/EVIDENCE_LIFECYCLE_DEEP_DIVE/", "residual_risk": "External storage design determines final tamper-resistance guarantees."},
            {"threat_id": "T-006", "family": "Trust drift", "asset": "Running capability", "control": "Continuous verification", "adr": "ADR-0006", "docs": "https://vsdatta.github.io/aegislayer-architecture/CONTINUOUS_VERIFICATION_LIFECYCLE/", "residual_risk": "Monitoring cadence and signal quality determine how quickly drift is detected."},
        ],
        "connector-scenarios": [
            {"connector": "analytics", "readiness": "ready", "scope": "read_report", "health": "healthy", "outcome": "allow", "summary": "Connector readiness and capability scope align."},
            {"connector": "ops", "readiness": "blocked", "scope": "delete_resource", "health": "degraded", "outcome": "deny", "summary": "Readiness failure blocks execution before capability issue."},
            {"connector": "content", "readiness": "ready", "scope": "publish_content", "health": "trust_drift", "outcome": "revoke", "summary": "Continuous verification revokes a previously valid capability."},
        ],
        "runtime-states": [
            {"state": "requested", "summary": "A proposed action is recorded but not yet authorized."},
            {"state": "identity_validated", "summary": "Identity and authority context passes initial checks."},
            {"state": "approval_pending", "summary": "High-impact actions pause until accountable approval resolves."},
            {"state": "executing", "summary": "Connector scope and runtime conditions remain valid."},
            {"state": "revoked", "summary": "Capability or trust posture changed and execution authority was removed."},
            {"state": "contained", "summary": "Incident response contained runtime activity pending recovery review."},
            {"state": "completed", "summary": "Execution ended within approved bounds and evidence was finalized."},
        ],
        "governance-library": [
            {"label": "ADR 0001", "summary": "Separate AI reasoning from execution authority.", "url": "https://vsdatta.github.io/aegislayer-architecture/adr/0001-separate-ai-reasoning-from-execution-authority/"},
            {"label": "ADR 0003", "summary": "Evidence by design underpins auditability and review.", "url": "https://vsdatta.github.io/aegislayer-architecture/adr/0003-evidence-by-design/"},
            {"label": "Glossary", "summary": "Shared terminology for governance, authority, connector, runtime, and evidence concepts.", "url": "https://vsdatta.github.io/aegislayer-architecture/GLOSSARY/"},
            {"label": "Pattern Library", "summary": "Safe patterns and anti-patterns for governed AI action systems.", "url": "https://vsdatta.github.io/aegislayer-architecture/PATTERN_LIBRARY/"},
            {"label": "Release Checklist", "summary": "Public release-readiness checklist for docs and mirrored assets.", "url": "https://vsdatta.github.io/aegislayer-architecture/RELEASE_CHECKLIST/"},
        ],
    }


def render_interactive_cards(space_slug: str) -> str:
    data = base_datasets()[next(key for key in base_datasets() if key in space_slug or key == "governance-library" and space_slug == "governance-library")]
    serialized = json.dumps(data)
    return f"const spaceData = {serialized};\n"


def render_js() -> str:
    return """\
const datasetMap = {
  "policy-playground": {
    label: "Policy scenario",
    kind: "scenario",
    rows: [
      { name: "Low-risk allow", summary: "Identity, authority, policy, and connector checks align.", detail: { outcome: "allow", approval: "not_required", reason: "policy_and_authority_match" }, tags: ["allow", "low-risk", "deterministic"] },
      { name: "Unauthorized deny", summary: "Authority mismatch denies execution before connector use.", detail: { outcome: "deny", approval: "not_reached", reason: "authority_scope_mismatch" }, tags: ["deny", "fail-closed", "identity"] },
      { name: "High-impact approval required", summary: "Policy requires a bounded approval before execution.", detail: { outcome: "conditional", approval: "required", reason: "high_impact_requires_approval" }, tags: ["approval", "high-impact"] },
      { name: "Connector unavailable", summary: "A blocked connector halts execution.", detail: { outcome: "deny", approval: "not_reached", reason: "connector_not_ready" }, tags: ["connector", "deny"] },
      { name: "Capability expired", summary: "Capability expiry revokes execution authority mid-flight.", detail: { outcome: "revoke", approval: "granted_then_expired", reason: "capability_expired" }, tags: ["revocation", "continuous-verification"] },
      { name: "Containment triggered", summary: "Incident handling forces containment and review.", detail: { outcome: "contain", approval: "review_required", reason: "incident_containment_triggered" }, tags: ["containment", "incident"] }
    ]
  },
  "evidence-chain-explorer": {
    label: "Evidence event",
    kind: "evidence",
    rows: [
      { name: "request_created", summary: "Request id and intent recorded.", detail: { record_type: "request", correlation: "REQ-001" }, tags: ["request", "correlation"] },
      { name: "identity_validated", summary: "Identity and authority bindings recorded.", detail: { record_type: "identity", actor: "user-1" }, tags: ["identity", "authority"] },
      { name: "policy_evaluated", summary: "Policy decision and rationale appended.", detail: { record_type: "policy", decision: "conditional" }, tags: ["policy", "rationale"] },
      { name: "approval_recorded", summary: "Approver, scope, expiry, and outcome captured.", detail: { record_type: "approval", approved: true }, tags: ["approval", "scope"] },
      { name: "runtime_transition", summary: "Execution and connector context logged.", detail: { record_type: "runtime", state: "executing" }, tags: ["runtime", "connector"] },
      { name: "bundle_finalized", summary: "Bundle integrity and completeness summary generated.", detail: { record_type: "evidence", finalized: true }, tags: ["finalized", "integrity"] }
    ]
  },
  "threat-control-explorer": {
    label: "Threat family",
    kind: "threat",
    rows: [
      { name: "Unauthorized execution", summary: "Prevent action without explicit authority.", detail: { control: "Identity-first authorization", adr: "ADR-0002", residual_risk: "Stale authority data remains a timing risk." }, tags: ["authorization", "zero-trust"] },
      { name: "Approval bypass", summary: "High-impact execution requires accountable approval.", detail: { control: "Human approval for high-impact actions", adr: "ADR-0007", residual_risk: "Approver fatigue can still weaken review quality." }, tags: ["approval", "accountability"] },
      { name: "Connector abuse", summary: "Capability scoping narrows connector privileges.", detail: { control: "Capability-scoped connectors", adr: "ADR-0005", residual_risk: "Trusted connectors may still misbehave beyond visible state." }, tags: ["connector", "scope"] },
      { name: "Trust drift", summary: "Continuous verification revokes on degraded posture.", detail: { control: "Continuous verification", adr: "ADR-0006", residual_risk: "Signal quality determines detection speed." }, tags: ["runtime", "monitoring"] }
    ]
  },
  "connector-trust-simulator": {
    label: "Connector",
    kind: "connector",
    rows: [
      { name: "analytics", summary: "Ready connector with scoped report-read capability.", detail: { readiness: "ready", scope: "read_report", outcome: "allow" }, tags: ["ready", "allow"] },
      { name: "ops", summary: "Blocked readiness causes fail-closed denial.", detail: { readiness: "blocked", scope: "delete_resource", outcome: "deny" }, tags: ["blocked", "deny"] },
      { name: "content", summary: "Trust drift revokes a valid publishing capability.", detail: { readiness: "ready", scope: "publish_content", outcome: "revoke" }, tags: ["revoke", "trust-drift"] }
    ]
  },
  "runtime-state-visualizer": {
    label: "Runtime state",
    kind: "runtime",
    rows: [
      { name: "requested", summary: "Intent recorded with no execution authority granted.", detail: { next: ["identity_validated"] }, tags: ["requested"] },
      { name: "identity_validated", summary: "Identity and authority resolved before policy branch.", detail: { next: ["approval_pending", "executing", "denied"] }, tags: ["identity"] },
      { name: "approval_pending", summary: "Approval holds the request in a bounded waiting state.", detail: { next: ["executing", "denied"] }, tags: ["approval"] },
      { name: "executing", summary: "Connector trust and capability remain continuously verified.", detail: { next: ["completed", "revoked", "contained"] }, tags: ["executing"] },
      { name: "revoked", summary: "Execution authority removed due to expiry or drift.", detail: { next: ["contained", "closed"] }, tags: ["revoked"] },
      { name: "contained", summary: "Incident response isolates the request pending decision.", detail: { next: ["completed", "closed"] }, tags: ["contained"] },
      { name: "completed", summary: "Execution finished within bounds and evidence finalized.", detail: { next: [] }, tags: ["completed"] }
    ]
  },
  "governance-library": {
    label: "Library entry",
    kind: "library",
    rows: [
      { name: "ADR 0001", summary: "Separate AI reasoning from execution authority.", detail: { url: "https://vsdatta.github.io/aegislayer-architecture/adr/0001-separate-ai-reasoning-from-execution-authority/" }, tags: ["adr", "authority"] },
      { name: "ADR 0003", summary: "Evidence by design as a reviewability anchor.", detail: { url: "https://vsdatta.github.io/aegislayer-architecture/adr/0003-evidence-by-design/" }, tags: ["adr", "evidence"] },
      { name: "Pattern Library", summary: "Reference patterns and anti-patterns.", detail: { url: "https://vsdatta.github.io/aegislayer-architecture/PATTERN_LIBRARY/" }, tags: ["patterns"] },
      { name: "Glossary", summary: "Shared terminology and definitions.", detail: { url: "https://vsdatta.github.io/aegislayer-architecture/GLOSSARY/" }, tags: ["glossary"] }
    ]
  }
};

function renderTags(tags) {
  return `<div class="tag-row">${tags.map((tag) => `<span class="tag">${tag}</span>`).join("")}</div>`;
}

function renderDetail(detail) {
  return `<pre class="code-block">${JSON.stringify(detail, null, 2)}</pre>`;
}

function buildInteractiveRegion(spaceKey) {
  const region = document.getElementById("interactive-region");
  if (!region) {
    return;
  }

  const config = datasetMap[spaceKey];
  if (!config) {
    region.innerHTML = `
      <article class="interactive-card">
        <h3>Static Portfolio</h3>
        <p>This Space is intentionally static and uses cross-linked repository content rather than live interactions.</p>
      </article>
    `;
    return;
  }

  region.innerHTML = `
    <div class="interactive-card selector-row">
      <label for="record-select">Select ${config.label.toLowerCase()}</label>
      <select id="record-select"></select>
    </div>
    <article class="interactive-card">
      <h3 id="record-title"></h3>
      <p id="record-summary"></p>
      <div id="record-tags"></div>
      <div id="record-detail"></div>
    </article>
  `;

  const select = document.getElementById("record-select");
  const title = document.getElementById("record-title");
  const summary = document.getElementById("record-summary");
  const tags = document.getElementById("record-tags");
  const detail = document.getElementById("record-detail");

  config.rows.forEach((row, index) => {
    const option = document.createElement("option");
    option.value = String(index);
    option.textContent = row.name;
    select.appendChild(option);
  });

  function renderRow(index) {
    const row = config.rows[index];
    title.textContent = row.name;
    summary.textContent = row.summary;
    tags.innerHTML = renderTags(row.tags);
    detail.innerHTML = renderDetail(row.detail);
  }

  select.addEventListener("change", () => renderRow(Number(select.value)));
  renderRow(0);
}

buildInteractiveRegion(document.body.dataset.space);
"""


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not content.endswith("\n"):
        content = f"{content}\n"
    path.write_text(content, encoding="utf-8")


def reset_space_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def build_space(space: dict, site_data: dict, spaces: list[dict], *, to_dist: bool) -> None:
    target_root = DIST_ROOT if to_dist else SPACES_ROOT
    space_dir = target_root / space["slug"]
    reset_space_dir(space_dir)
    write_text(space_dir / "README.md", render_readme(space, site_data, spaces))
    write_text(space_dir / "index.html", render_html(space, site_data, spaces))
    write_text(space_dir / "assets" / "css" / "styles.css", render_css())
    write_text(space_dir / "assets" / "js" / "app.js", render_js())


def build_legacy_export(organization_home_dir: Path) -> None:
    if LEGACY_EXPORT.exists():
        shutil.rmtree(LEGACY_EXPORT)
    shutil.copytree(organization_home_dir, LEGACY_EXPORT)


def parse_args() -> ArgumentParser:
    parser = ArgumentParser(description="Build Hugging Face portfolio exports.")
    parser.add_argument("--space", dest="space_slug", help="Build only the requested space slug.")
    parser.add_argument("--dist-only", action="store_true", help="Skip regenerating source space directories.")
    return parser


def main() -> int:
    parser = parse_args()
    args = parser.parse_args()

    manifest = load_json(MANIFEST_PATH)
    site_data = load_json(SITE_DATA_PATH)
    spaces = manifest["spaces"]
    if args.space_slug:
        spaces = [space for space in spaces if space["slug"] == args.space_slug]
        if not spaces:
            print(f"Unknown space slug: {args.space_slug}")
            return 1

    DIST_ROOT.mkdir(parents=True, exist_ok=True)
    if not args.dist_only:
        for space in spaces:
            build_space(space, site_data, manifest["spaces"], to_dist=False)

    for space in spaces:
        build_space(space, site_data, manifest["spaces"], to_dist=True)

    if any(space["slug"] == "organization-home" for space in spaces):
        build_legacy_export(DIST_ROOT / "organization-home")

    print("Built Hugging Face portfolio spaces:")
    for space in spaces:
        print(f"- {space['slug']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())