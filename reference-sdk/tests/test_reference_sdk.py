from datetime import timedelta

from aegislayer_reference.evidence import EvidenceBuilder
from aegislayer_reference.incidents import decide_incident_response
from aegislayer_reference.models import (
    ActionRequest,
    ApprovalRecord,
    AuthorityContext,
    ConnectorDescriptor,
    IncidentDecision,
    PolicyRule,
    ReadinessState,
    RequestIdentity,
    utc_now,
)
from aegislayer_reference.monitoring import monitor_and_enforce
from aegislayer_reference.policy import evaluate_policy
from aegislayer_reference.runtime import execute_request
from aegislayer_reference.serialization import canonical_json


def base_request(action: str, risk: str = "low") -> ActionRequest:
    return ActionRequest.new(action=action, target="system-a", risk=risk)


def test_allowed_low_risk_request() -> None:
    now = utc_now()
    req = base_request("read_report")
    identity = RequestIdentity("user-1", "idp", True)
    authority = AuthorityContext("analyst", ("read_report",))
    connector = ConnectorDescriptor("analytics", ("read_report",), ReadinessState.READY)
    decision = evaluate_policy(req, PolicyRule("baseline", ("read_report",)))

    runtime = execute_request(req, identity, authority, connector, decision, None, now)
    assert runtime.state.value == "completed"


def test_denied_unauthorized_request() -> None:
    now = utc_now()
    req = base_request("delete_resource")
    identity = RequestIdentity("user-1", "idp", True)
    authority = AuthorityContext("analyst", ("read_report",))
    connector = ConnectorDescriptor("ops", ("delete_resource",), ReadinessState.READY)
    decision = evaluate_policy(req, PolicyRule("baseline", ("delete_resource",)))

    runtime = execute_request(req, identity, authority, connector, decision, None, now)
    assert runtime.state.value == "denied"
    assert runtime.reason == "authority_scope_mismatch"


def test_high_impact_requires_approval() -> None:
    now = utc_now()
    req = base_request("delete_resource", risk="high")
    identity = RequestIdentity("ops-1", "idp", True)
    authority = AuthorityContext("operator", ("delete_resource",))
    connector = ConnectorDescriptor("ops", ("delete_resource",), ReadinessState.READY)
    decision = evaluate_policy(req, PolicyRule("baseline", ("delete_resource",)))
    approval = ApprovalRecord(
        approver_id="approver-1",
        approved=True,
        scope_action="delete_resource",
        scope_target="system-a",
        expires_at=now + timedelta(minutes=3),
    )

    runtime = execute_request(req, identity, authority, connector, decision, approval, now)
    assert runtime.state.value == "completed"


def test_connector_readiness_failure() -> None:
    now = utc_now()
    req = base_request("read_report")
    identity = RequestIdentity("user-1", "idp", True)
    authority = AuthorityContext("analyst", ("read_report",))
    connector = ConnectorDescriptor("analytics", ("read_report",), ReadinessState.BLOCKED)
    decision = evaluate_policy(req, PolicyRule("baseline", ("read_report",)))

    runtime = execute_request(req, identity, authority, connector, decision, None, now)
    assert runtime.state.value == "denied"
    assert runtime.reason == "connector_not_ready"


def test_capability_expiry_during_execution() -> None:
    now = utc_now()
    from aegislayer_reference.capabilities import issue_capability

    cap = issue_capability("user-1", "read_report", "system-a", now + timedelta(seconds=1))
    updated, event = monitor_and_enforce(cap, now + timedelta(minutes=2), trust_ok=True)
    assert updated.revoked is True
    assert updated.revoke_reason == "capability_expired"
    assert event.status == "revoked"


def test_continuous_verification_revocation() -> None:
    now = utc_now()
    from aegislayer_reference.capabilities import issue_capability

    cap = issue_capability("user-1", "read_report", "system-a", now + timedelta(minutes=5))
    updated, event = monitor_and_enforce(cap, now + timedelta(seconds=30), trust_ok=False)
    assert updated.revoked is True
    assert updated.revoke_reason == "continuous_verification_revocation"
    assert event.details["reason"] == "trust_drift"


def test_evidence_bundle_generation_and_immutability() -> None:
    req = base_request("read_report")
    now = utc_now()
    builder = EvidenceBuilder.start(req)
    builder.append("identity_validated", {"actor": "user-1"}, now)
    bundle = builder.finalize(now)

    assert bundle.finalized is True
    assert len(bundle.records) == 1
    payload = canonical_json(bundle)
    assert "identity_validated" in payload


def test_incident_containment() -> None:
    req = base_request("read_report")
    response = decide_incident_response(req.request_id, severe=False, recoverable=False)
    assert response.decision == IncidentDecision.CONTAIN


def test_incident_severe_close() -> None:
    req = base_request("read_report")
    response = decide_incident_response(req.request_id, severe=True, recoverable=False)
    assert response.decision == IncidentDecision.DENY_AND_CLOSE
