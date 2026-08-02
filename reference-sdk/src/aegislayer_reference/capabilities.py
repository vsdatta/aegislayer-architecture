"""Capability issuance and lifecycle functions."""

from dataclasses import replace
from datetime import datetime
from uuid import uuid4

from .models import Capability


def issue_capability(subject: str, action: str, target: str, expires_at: datetime) -> Capability:
    return Capability(
        capability_id=f"cap-{uuid4()}",
        subject=subject,
        action=action,
        target=target,
        expires_at=expires_at,
    )


def validate_capability(capability: Capability, action: str, target: str, now: datetime) -> tuple[bool, str | None]:
    if capability.revoked:
        return False, "capability_revoked"
    if now >= capability.expires_at:
        return False, "capability_expired"
    if capability.action != action or capability.target != target:
        return False, "capability_scope_mismatch"
    return True, None


def revoke_capability(capability: Capability, reason: str) -> Capability:
    return replace(capability, revoked=True, revoke_reason=reason)
