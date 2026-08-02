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
