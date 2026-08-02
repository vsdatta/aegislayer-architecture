"""Incident response decision modeling."""

from .models import IncidentDecision, IncidentResponse


def decide_incident_response(request_id: str, severe: bool, recoverable: bool) -> IncidentResponse:
    if severe:
        return IncidentResponse(
            decision=IncidentDecision.DENY_AND_CLOSE,
            rationale="severe_incident_requires_stop",
            request_id=request_id,
        )
    if recoverable:
        return IncidentResponse(
            decision=IncidentDecision.RESUME_WITH_CONSTRAINTS,
            rationale="recoverable_with_constraints",
            request_id=request_id,
        )
    return IncidentResponse(
        decision=IncidentDecision.CONTAIN,
        rationale="contain_pending_review",
        request_id=request_id,
    )
