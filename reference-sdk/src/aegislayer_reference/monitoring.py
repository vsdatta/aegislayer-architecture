"""Continuous verification monitoring primitives."""

from datetime import datetime

from .capabilities import revoke_capability
from .models import Capability, MonitoringEvent, utc_now


def monitor_and_enforce(
    capability: Capability,
    now: datetime,
    trust_ok: bool,
) -> tuple[Capability, MonitoringEvent]:
    if not trust_ok:
        updated = revoke_capability(capability, "continuous_verification_revocation")
        event = MonitoringEvent(
            category="continuous_verification",
            status="revoked",
            request_id=capability.capability_id,
            observed_at=now,
            details={"reason": "trust_drift"},
        )
        return updated, event

    if now >= capability.expires_at:
        updated = revoke_capability(capability, "capability_expired")
        event = MonitoringEvent(
            category="continuous_verification",
            status="revoked",
            request_id=capability.capability_id,
            observed_at=now,
            details={"reason": "expiry"},
        )
        return updated, event

    event = MonitoringEvent(
        category="continuous_verification",
        status="ok",
        request_id=capability.capability_id,
        observed_at=utc_now(),
        details={"reason": "trust_valid"},
    )
    return capability, event
