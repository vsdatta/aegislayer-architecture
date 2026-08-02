"""Approval requirement and validation functions."""

from datetime import datetime

from .models import ApprovalRecord, ApprovalRequirement


def approval_requirement_from_policy(policy_outcome: str) -> ApprovalRequirement:
    if policy_outcome == "require_approval":
        return ApprovalRequirement(required=True, reason="policy_high_impact")
    return ApprovalRequirement(required=False)


def validate_approval(
    approval: ApprovalRecord | None,
    action: str,
    target: str,
    now: datetime,
) -> tuple[bool, str | None]:
    if approval is None:
        return False, "approval_missing"
    if not approval.approved:
        return False, "approval_denied"
    if approval.scope_action != action or approval.scope_target != target:
        return False, "approval_scope_mismatch"
    if now >= approval.expires_at:
        return False, "approval_expired"
    return True, None
