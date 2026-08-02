"""Domain exceptions for the conceptual reference SDK."""


class AegisReferenceError(Exception):
    """Base exception for reference SDK errors."""


class ValidationError(AegisReferenceError):
    """Raised when required validation inputs are missing or invalid."""
