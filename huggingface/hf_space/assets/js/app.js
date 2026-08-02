const scenarios = [
  {
    key: "governed-request",
    title: "Governed Request Simulator",
    summary: "Low-risk request proceeds after identity, policy, connector, and capability checks.",
    tags: ["conceptual", "deterministic", "low-risk"],
    steps: [
      "Validate identity and authority context.",
      "Evaluate policy and risk profile.",
      "Verify connector readiness.",
      "Issue short-lived scoped capability.",
      "Execute controlled action and record evidence.",
    ],
    output: { outcome: "allow", runtime_state: "completed", reason: "execution_completed" },
  },
  {
    key: "unauthorized-deny",
    title: "Identity and Authority Validation Flow",
    summary: "Unauthorized action is denied with explicit reason.",
    tags: ["fail-closed", "identity", "authority"],
    steps: [
      "Request action exceeds authority scope.",
      "Authority check fails.",
      "Policy/connector stages are not executed.",
      "Evidence records explicit denial reason.",
    ],
    output: { outcome: "deny", runtime_state: "denied", reason: "authority_scope_mismatch" },
  },
  {
    key: "approval-required",
    title: "Human Approval Workflow",
    summary: "High-impact request requires bounded approval before runtime execution.",
    tags: ["approval", "high-impact"],
    steps: [
      "Policy marks request as high impact.",
      "Approval request is issued with scope and expiry.",
      "Approver decision is validated.",
      "Execution continues only while approval remains valid.",
    ],
    output: { outcome: "require_approval", runtime_state: "completed", reason: "approved_and_executed" },
  },
  {
    key: "connector-failure",
    title: "Connector Readiness Simulator",
    summary: "Connector trust degradation blocks execution.",
    tags: ["connector", "readiness"],
    steps: [
      "Connector reports blocked readiness state.",
      "Runtime fails closed.",
      "No fallback to broader privileges occurs.",
    ],
    output: { outcome: "deny", runtime_state: "denied", reason: "connector_not_ready" },
  },
  {
    key: "capability-expiry",
    title: "Continuous Verification and Revocation",
    summary: "Capability expiry or trust drift revokes execution authority during runtime.",
    tags: ["continuous-verification", "revocation"],
    steps: [
      "Capability issued with short expiry.",
      "Monitoring detects expiry/trust drift.",
      "Capability is revoked.",
      "Execution transitions to contained/denied.",
    ],
    output: { outcome: "revoke", runtime_state: "contained", reason: "capability_expired" },
  },
  {
    key: "evidence-chain",
    title: "Evidence-Chain Viewer",
    summary: "Request lifecycle events are serialized into a finalized immutable evidence bundle.",
    tags: ["evidence", "auditability"],
    steps: [
      "Initialize request evidence with correlation and causation IDs.",
      "Append policy and approval events.",
      "Append runtime and monitoring events.",
      "Finalize immutable bundle for review.",
    ],
    output: { outcome: "recorded", bundle_finalized: true, records: 6 },
  },
  {
    key: "incident-containment",
    title: "Incident Containment Walkthrough",
    summary: "Anomaly detection triggers containment and controlled recovery decision.",
    tags: ["incident", "containment", "recovery"],
    steps: [
      "Monitoring signals anomaly.",
      "Containment revokes active capabilities.",
      "Incident role reviews evidence.",
      "System resumes with constraints or remains denied.",
    ],
    output: { outcome: "contain", runtime_state: "contained", reason: "contain_pending_review" },
  },
];

const diagrams = [
  {
    name: "Identity/Authority Lifecycle",
    desc: "Sequence diagram for identity validation and authority scope resolution.",
    href: "../diagrams/identity-authority-lifecycle.mmd",
  },
  {
    name: "Policy Evaluation Lifecycle",
    desc: "Flow diagram for input completeness, decision outcomes, and approval branch.",
    href: "../diagrams/policy-evaluation-lifecycle.mmd",
  },
  {
    name: "Approval Lifecycle",
    desc: "Approval queue, approver decision, and runtime verification sequence.",
    href: "../diagrams/approval-lifecycle.mmd",
  },
  {
    name: "Connector Lifecycle",
    desc: "State transitions across discovered, ready, blocked, and revoked connector states.",
    href: "../diagrams/connector-lifecycle.mmd",
  },
  {
    name: "Runtime State Model",
    desc: "Core runtime transition states and fail-closed denial paths.",
    href: "../diagrams/runtime-state-model.mmd",
  },
  {
    name: "Incident Containment and Recovery",
    desc: "Containment to recovery decision flow for runtime incidents.",
    href: "../diagrams/incident-containment-recovery.mmd",
  },
];

const threatMappings = {
  "Unauthorized execution": {
    controls: ["Identity-first authorization", "Policy before execution", "Fail-closed execution"],
    evidence: "Identity and policy decision records",
  },
  "Connector abuse": {
    controls: ["Capability-scoped connectors", "Connector readiness checks"],
    evidence: "Connector readiness and invocation evidence",
  },
  "Approval bypass": {
    controls: ["Risk-based human approvals", "Scope and expiry-bound approval"],
    evidence: "Approval request and decision records",
  },
  "Long-running trust drift": {
    controls: ["Continuous verification", "Capability revocation"],
    evidence: "Revocation and containment events",
  },
};

const scenarioList = document.getElementById("scenario-list");
const scenarioTitle = document.getElementById("scenario-title");
const scenarioSummary = document.getElementById("scenario-summary");
const scenarioTags = document.getElementById("scenario-tags");
const scenarioSteps = document.getElementById("scenario-steps");
const scenarioOutput = document.getElementById("scenario-output");
const diagramSelect = document.getElementById("diagram-select");
const diagramDesc = document.getElementById("diagram-desc");
const diagramLink = document.getElementById("diagram-link");
const threatSelect = document.getElementById("threat-select");
const threatOutput = document.getElementById("threat-output");

function renderScenario(scenario) {
  scenarioTitle.textContent = scenario.title;
  scenarioSummary.textContent = scenario.summary;
  scenarioTags.innerHTML = scenario.tags.map((tag) => `<span class="badge">${tag}</span>`).join("");
  scenarioSteps.innerHTML = scenario.steps.map((step) => `<li>${step}</li>`).join("");
  scenarioOutput.textContent = JSON.stringify(scenario.output, null, 2);
}

function initScenarios() {
  scenarios.forEach((scenario, index) => {
    const li = document.createElement("li");
    const button = document.createElement("button");
    button.className = "scenario-btn";
    button.type = "button";
    button.textContent = `${index + 1}. ${scenario.title}`;
    button.addEventListener("click", () => renderScenario(scenario));
    li.appendChild(button);
    scenarioList.appendChild(li);
  });
  renderScenario(scenarios[0]);
}

function initDiagrams() {
  diagrams.forEach((diagram, index) => {
    const option = document.createElement("option");
    option.value = String(index);
    option.textContent = diagram.name;
    diagramSelect.appendChild(option);
  });

  function renderSelectedDiagram() {
    const selected = diagrams[Number(diagramSelect.value) || 0];
    diagramDesc.textContent = selected.desc;
    diagramLink.href = selected.href;
  }

  diagramSelect.addEventListener("change", renderSelectedDiagram);
  renderSelectedDiagram();
}

function initThreatExplorer() {
  const threats = Object.keys(threatMappings);
  threats.forEach((threat) => {
    const option = document.createElement("option");
    option.value = threat;
    option.textContent = threat;
    threatSelect.appendChild(option);
  });

  function renderThreat() {
    const selected = threatMappings[threatSelect.value];
    threatOutput.innerHTML = `
      <strong>Controls:</strong> ${selected.controls.join(", ")}<br />
      <strong>Evidence:</strong> ${selected.evidence}
    `;
  }

  threatSelect.addEventListener("change", renderThreat);
  threatSelect.value = threats[0];
  renderThreat();
}

initScenarios();
initDiagrams();
initThreatExplorer();
