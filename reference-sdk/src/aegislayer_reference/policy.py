"""Deterministic policy evaluation."""

from .models import ActionRequest, DecisionOutcome, PolicyDecision, PolicyRule


def evaluate_policy(request: ActionRequest, rule: PolicyRule) -> PolicyDecision:
    if request.action in rule.deny_actions:
        return PolicyDecision(DecisionOutcome.DENY, ("action_explicitly_denied",))
    if request.action not in rule.allow_actions:
        return PolicyDecision(DecisionOutcome.DENY, ("action_not_allowed",))
    if request.risk in rule.high_impact_risks:
        return PolicyDecision(
            DecisionOutcome.REQUIRE_APPROVAL,
            ("high_impact_requires_approval",),
            constraints={"approval": "required"},
        )
    return PolicyDecision(DecisionOutcome.ALLOW, ("policy_allow",))
