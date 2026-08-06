"""
OGS Smart Money AI

Provider Domain
"""

from __future__ import annotations

from dataclasses import dataclass

from .enums import (
    ConnectionStatus,
    ProviderType,
)


@dataclass(slots=True, frozen=True)
class Provider:
    """
    Represents a market data provider.

    A Provider may be a broker, exchange,
    simulator, CSV source, or any other
    market data source used by OGS.
    """

    name: str

    provider_type: ProviderType = ProviderType.UNKNOWN

    status: ConnectionStatus = ConnectionStatus.UNKNOWN

    latency_ms: float = 0.0

    supports_live: bool = False

    supports_historical: bool = False

    supports_websocket: bool = False

    supports_order_execution: bool = False

    supports_level2: bool = False

    supports_options: bool = False

    supports_futures: bool = False

    @property
    def connected(self) -> bool:
        """
        Returns True if provider is connected.
        """
        return self.status == ConnectionStatus.CONNECTED

    @property
    def disconnected(self) -> bool:
        """
        Returns True if provider is disconnected.
        """
        return self.status == ConnectionStatus.DISCONNECTED

    @property
    def online(self) -> bool:
        """
        Alias for connected.
        """
        return self.connected

    @property
    def offline(self) -> bool:
        """
        Alias for disconnected.
        """
        return self.disconnected

    @property
    def is_valid(self) -> bool:
        """
        Lightweight validation.
        """
        return (
            bool(self.name.strip())
            and isinstance(self.provider_type, ProviderType)
            and isinstance(self.status, ConnectionStatus)
            and self.latency_ms >= 0
        )

    def to_dict(self) -> dict:
        """
        Convert Provider into dictionary.
        """

        return {
            "name": self.name,
            "provider_type": self.provider_type.value,
            "status": self.status.value,
            "latency_ms": self.latency_ms,
            "supports_live": self.supports_live,
            "supports_historical": self.supports_historical,
            "supports_websocket": self.supports_websocket,
            "supports_order_execution": self.supports_order_execution,
            "supports_level2": self.supports_level2,
            "supports_options": self.supports_options,
            "supports_futures": self.supports_futures,
        }

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"[{self.provider_type.value}] "
            f"{self.status.value}"
        )

    def __repr__(self) -> str:
        return (
            f"Provider("
            f"name='{self.name}', "
            f"type={self.provider_type.value}, "
            f"status={self.status.value})"
        )