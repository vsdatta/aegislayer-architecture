"""Authority context evaluation functions."""

from datetime import datetime

from .models import AuthorityContext


def validate_authority(authority: AuthorityContext, action: str, now: datetime) -> tuple[bool, str | None]:
    if authority.expires_at is not None and now >= authority.expires_at:
        return False, "authority_expired"
    if action not in authority.allowed_actions:
        return False, "authority_scope_mismatch"
    return True, None
