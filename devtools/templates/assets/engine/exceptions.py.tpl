"""
Engine exception hierarchy for {{PROJECT_NAME}}.

Project      : {{PROJECT_SHORT_NAME}}
Module       : {{MODULE_NAME}}
Organization : {{ORGANIZATION}}
Version      : {{PROJECT_VERSION}}
"""

from __future__ import annotations


class OGSEngineError(Exception):
    """Base exception for all OGS engine framework errors."""


class EngineConfigurationError(OGSEngineError):
    """Raised when an engine has invalid or incomplete configuration."""


class EngineInitializationError(OGSEngineError):
    """Raised when an engine cannot be initialized successfully."""


class EngineExecutionError(OGSEngineError):
    """Raised when an engine execution fails."""


class EngineValidationError(OGSEngineError):
    """Raised when engine input or execution context is invalid."""


class EngineRegistrationError(OGSEngineError):
    """Raised when an engine cannot be registered."""


class EngineNotFoundError(OGSEngineError):
    """Raised when a requested engine is not registered."""


class DuplicateEngineError(EngineRegistrationError):
    """Raised when an engine is registered more than once."""
