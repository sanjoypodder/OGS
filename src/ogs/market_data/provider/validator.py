"""
OGS Smart Money AI

Provider Validator
"""

from __future__ import annotations

from ogs.framework import BaseValidator

from .domain import Provider
from .enums import (
    ConnectionStatus,
    ProviderType,
)


class ProviderValidator(BaseValidator):
    """
    Validator for Provider objects.
    """

    MIN_LATENCY_MS = 0.0
    MAX_LATENCY_MS = 60_000.0

    def validate(self, provider: Provider) -> None:
        """
        Validate a Provider instance.

        Raises
        ------
        TypeError
            If an attribute has an invalid type.

        ValueError
            If an attribute contains an invalid value.
        """

        if not isinstance(provider, Provider):
            raise TypeError("provider must be a Provider instance.")

        if not isinstance(provider.name, str):
            raise TypeError("name must be a string.")

        if not provider.name.strip():
            raise ValueError("name cannot be empty.")

        if not isinstance(provider.provider_type, ProviderType):
            raise TypeError("provider_type must be ProviderType.")

        if not isinstance(provider.status, ConnectionStatus):
            raise TypeError("status must be ConnectionStatus.")

        if not isinstance(provider.latency_ms, (int, float)):
            raise TypeError("latency_ms must be numeric.")

        if not (
            self.MIN_LATENCY_MS
            <= provider.latency_ms
            <= self.MAX_LATENCY_MS
        ):
            raise ValueError(
                f"latency_ms must be between "
                f"{self.MIN_LATENCY_MS} and "
                f"{self.MAX_LATENCY_MS}."
            )

        bool_fields = (
            provider.supports_live,
            provider.supports_historical,
            provider.supports_websocket,
            provider.supports_order_execution,
            provider.supports_level2,
            provider.supports_options,
            provider.supports_futures,
        )

        if not all(isinstance(value, bool) for value in bool_fields):
            raise TypeError("Capability fields must be bool.")

    def __call__(self, provider: Provider) -> Provider:
        """
        Validate and return the Provider.
        """
        self.validate(provider)
        return provider