"""Connector readiness and compatibility checks."""

from .models import ConnectorDescriptor, ReadinessState


def validate_connector(connector: ConnectorDescriptor, action: str) -> tuple[bool, str | None]:
    if connector.readiness != ReadinessState.READY:
        return False, "connector_not_ready"
    if action not in connector.supported_actions:
        return False, "connector_action_not_supported"
    return True, None
