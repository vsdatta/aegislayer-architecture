"""Reference scenarios for conceptual SDK usage."""

from datetime import timedelta

from aegislayer_reference.evidence import EvidenceBuilder
from aegislayer_reference.models import (
    ActionRequest,
    ApprovalRecord,
    AuthorityContext,
    ConnectorDescriptor,
    PolicyRule,
    ReadinessState,
    RequestIdentity,
    utc_now,
)
from aegislayer_reference.policy import evaluate_policy
from aegislayer_reference.runtime import execute_request


def allowed_low_risk() -> str:
    now = utc_now()
    request = ActionRequest.new("read_report", "analytics", "low")
    identity = RequestIdentity(actor_id="user-1", issuer="idp", authenticated=True)
    authority = AuthorityContext(role="analyst", allowed_actions=("read_report",))
    connector = ConnectorDescriptor("analytics", ("read_report",), ReadinessState.READY)
    rule = PolicyRule("baseline", allow_actions=("read_report",))
    decision = evaluate_policy(request, rule)
    runtime = execute_request(request, identity, authority, connector, decision, None, now)
    builder = EvidenceBuilder.start(request)
    builder.append("runtime_decision", {"state": runtime.state.value, "reason": runtime.reason}, now)
    return runtime.state.value


def high_impact_with_approval() -> str:
    now = utc_now()
    request = ActionRequest.new("delete_resource", "system-a", "high")
    identity = RequestIdentity(actor_id="ops-1", issuer="idp", authenticated=True)
    authority = AuthorityContext(role="operator", allowed_actions=("delete_resource",))
    connector = ConnectorDescriptor("ops", ("delete_resource",), ReadinessState.READY)
    rule = PolicyRule("baseline", allow_actions=("delete_resource",))
    decision = evaluate_policy(request, rule)
    approval = ApprovalRecord(
        approver_id="approver-1",
        approved=True,
        scope_action="delete_resource",
        scope_target="system-a",
        expires_at=now + timedelta(minutes=5),
        rationale="approved_for_controlled_maintenance",
    )
    runtime = execute_request(request, identity, authority, connector, decision, approval, now)
    return runtime.state.value
