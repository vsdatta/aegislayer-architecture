"""Identity validation functions."""

from .models import RequestIdentity


def validate_identity(identity: RequestIdentity) -> tuple[bool, str | None]:
    if not identity.authenticated:
        return False, "identity_not_authenticated"
    if not identity.actor_id:
        return False, "missing_actor_id"
    if not identity.issuer:
        return False, "missing_identity_issuer"
    return True, None
