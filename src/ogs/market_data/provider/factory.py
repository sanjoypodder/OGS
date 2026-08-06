"""
OGS Smart Money AI

Provider Factory
"""

from __future__ import annotations

from ogs.framework import BaseFactory

from .domain import Provider
from .enums import (
    ConnectionStatus,
    ProviderType,
)
from .validator import ProviderValidator


class ProviderFactory(BaseFactory):
    """
    Factory for creating Provider objects.
    """

    _validator = ProviderValidator()

    @classmethod
    def create(
        cls,
        *,
        name: str,
        provider_type: ProviderType = ProviderType.UNKNOWN,
        status: ConnectionStatus = ConnectionStatus.UNKNOWN,
        latency_ms: float = 0.0,
        supports_live: bool = False,
        supports_historical: bool = False,
        supports_websocket: bool = False,
        supports_order_execution: bool = False,
        supports_level2: bool = False,
        supports_options: bool = False,
        supports_futures: bool = False,
    ) -> Provider:
        """
        Create and validate a Provider.
        """

        provider = Provider(
            name=name,
            provider_type=provider_type,
            status=status,
            latency_ms=latency_ms,
            supports_live=supports_live,
            supports_historical=supports_historical,
            supports_websocket=supports_websocket,
            supports_order_execution=supports_order_execution,
            supports_level2=supports_level2,
            supports_options=supports_options,
            supports_futures=supports_futures,
        )

        return cls._validator(provider)

    @classmethod
    def simulated(cls, name: str = "Simulation") -> Provider:
        """
        Create a simulated provider.
        """

        return cls.create(
            name=name,
            provider_type=ProviderType.SIMULATION,
            status=ConnectionStatus.CONNECTED,
            supports_live=True,
            supports_historical=True,
        )

    @classmethod
    def offline(cls, name: str) -> Provider:
        """
        Create an offline provider.
        """

        return cls.create(
            name=name,
            status=ConnectionStatus.DISCONNECTED,
        )

    @classmethod
    def clone(cls, provider: Provider) -> Provider:
        """
        Clone an existing Provider.
        """

        return cls.create(
            name=provider.name,
            provider_type=provider.provider_type,
            status=provider.status,
            latency_ms=provider.latency_ms,
            supports_live=provider.supports_live,
            supports_historical=provider.supports_historical,
            supports_websocket=provider.supports_websocket,
            supports_order_execution=provider.supports_order_execution,
            supports_level2=provider.supports_level2,
            supports_options=provider.supports_options,
            supports_futures=provider.supports_futures,
        )