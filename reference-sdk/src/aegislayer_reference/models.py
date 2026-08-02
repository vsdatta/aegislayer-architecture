"""Typed domain models for the conceptual AegisLayer reference SDK."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from uuid import uuid4


class DecisionOutcome(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    ALLOW_WITH_CONSTRAINTS = "allow_with_constraints"
    REQUIRE_APPROVAL = "require_approval"


class ReadinessState(str, Enum):
    READY = "ready"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVOKED = "revoked"


class RuntimeState(str, Enum):
    RECEIVED = "received"
    IDENTITY_VALIDATED = "identity_validated"
    POLICY_EVALUATED = "policy_evaluated"
    AWAITING_APPROVAL = "awaiting_approval"
    CAPABILITY_ISSUED = "capability_issued"
    EXECUTING = "executing"
    CONTAINED = "contained"
    COMPLETED = "completed"
    DENIED = "denied"


class IncidentDecision(str, Enum):
    CONTAIN = "contain"
    RESUME_WITH_CONSTRAINTS = "resume_with_constraints"
    DENY_AND_CLOSE = "deny_and_close"


def utc_now() -> datetime:
    """Return timezone-aware UTC timestamp."""
    return datetime.now(UTC)


@dataclass(frozen=True)
class RequestIdentity:
    actor_id: str
    issuer: str
    authenticated: bool


@dataclass(frozen=True)
class AuthorityContext:
    role: str
    allowed_actions: tuple[str, ...]
    delegated: bool = False
    expires_at: datetime | None = None


@dataclass(frozen=True)
class ActionRequest:
    request_id: str
    action: str
    target: str
    risk: str
    correlation_id: str
    causation_id: str | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)

    @staticmethod
    def new(action: str, target: str, risk: str, causation_id: str | None = None) -> ActionRequest:
        request_id = f"req-{uuid4()}"
        correlation_id = f"corr-{uuid4()}"
        return ActionRequest(
            request_id=request_id,
            action=action,
            target=target,
            risk=risk,
            correlation_id=correlation_id,
            causation_id=causation_id,
        )


@dataclass(frozen=True)
class PolicyRule:
    name: str
    allow_actions: tuple[str, ...]
    deny_actions: tuple[str, ...] = ()
    high_impact_risks: tuple[str, ...] = ("high", "critical")


@dataclass(frozen=True)
class PolicyDecision:
    outcome: DecisionOutcome
    reasons: tuple[str, ...]
    constraints: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class ApprovalRequirement:
    required: bool
    reason: str | None = None


@dataclass(frozen=True)
class ApprovalRecord:
    approver_id: str
    approved: bool
    scope_action: str
    scope_target: str
    expires_at: datetime
    recorded_at: datetime = field(default_factory=utc_now)
    rationale: str = ""


@dataclass(frozen=True)
class Capability:
    capability_id: str
    subject: str
    action: str
    target: str
    expires_at: datetime
    revoked: bool = False
    revoke_reason: str | None = None


@dataclass(frozen=True)
class ConnectorDescriptor:
    name: str
    supported_actions: tuple[str, ...]
    readiness: ReadinessState


@dataclass(frozen=True)
class RuntimeDecision:
    state: RuntimeState
    reason: str


@dataclass(frozen=True)
class EvidenceRecord:
    event_type: str
    request_id: str
    correlation_id: str
    causation_id: str | None
    timestamp_utc: datetime
    payload: Mapping[str, str]


@dataclass(frozen=True)
class EvidenceBundle:
    request_id: str
    records: tuple[EvidenceRecord, ...]
    finalized: bool
    finalized_at: datetime | None = None


@dataclass(frozen=True)
class MonitoringEvent:
    category: str
    status: str
    request_id: str
    observed_at: datetime
    details: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class IncidentResponse:
    decision: IncidentDecision
    rationale: str
    request_id: str
    recorded_at: datetime = field(default_factory=utc_now)


def to_tuple(values: Sequence[str]) -> tuple[str, ...]:
    return tuple(values)
