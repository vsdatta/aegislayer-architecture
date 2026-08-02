"""Reference runtime orchestration for governed request execution."""

from datetime import datetime, timedelta

from .approval import validate_approval
from .authority import validate_authority
from .capabilities import issue_capability, validate_capability
from .connectors import validate_connector
from .identity import validate_identity
from .models import (
    ActionRequest,
    ApprovalRecord,
    AuthorityContext,
    ConnectorDescriptor,
    PolicyDecision,
    RequestIdentity,
    RuntimeDecision,
    RuntimeState,
)


def execute_request(
    request: ActionRequest,
    identity: RequestIdentity,
    authority: AuthorityContext,
    connector: ConnectorDescriptor,
    policy_decision: PolicyDecision,
    approval: ApprovalRecord | None,
    now: datetime,
) -> RuntimeDecision:
    id_ok, id_reason = validate_identity(identity)
    if not id_ok:
        return RuntimeDecision(RuntimeState.DENIED, id_reason or "identity_denied")

    auth_ok, auth_reason = validate_authority(authority, request.action, now)
    if not auth_ok:
        return RuntimeDecision(RuntimeState.DENIED, auth_reason or "authority_denied")

    if policy_decision.outcome.value == "deny":
        return RuntimeDecision(RuntimeState.DENIED, ",".join(policy_decision.reasons))

    if policy_decision.outcome.value == "require_approval":
        approval_ok, approval_reason = validate_approval(approval, request.action, request.target, now)
        if not approval_ok:
            return RuntimeDecision(RuntimeState.DENIED, approval_reason or "approval_denied")

    connector_ok, connector_reason = validate_connector(connector, request.action)
    if not connector_ok:
        return RuntimeDecision(RuntimeState.DENIED, connector_reason or "connector_denied")

    capability = issue_capability(
        subject=identity.actor_id,
        action=request.action,
        target=request.target,
        expires_at=now + timedelta(minutes=10),
    )
    cap_ok, cap_reason = validate_capability(capability, request.action, request.target, now)
    if not cap_ok:
        return RuntimeDecision(RuntimeState.DENIED, cap_reason or "capability_denied")

    return RuntimeDecision(RuntimeState.COMPLETED, "execution_completed")
