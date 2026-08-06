"""
OGS Smart Money AI

Provider Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import ProviderCollection
from .domain import Provider


class ProviderStatistics(BaseStatistics):
    """
    Computes statistics for ProviderCollection.
    """

    def __init__(self, providers: ProviderCollection):
        self.providers = providers

    @property
    def count(self) -> int:
        return len(self.providers)

    @property
    def connected_count(self) -> int:
        return len(self.providers.connected())

    @property
    def offline_count(self) -> int:
        return len(self.providers.disconnected())

    @property
    def average_latency(self) -> float:
        return self.providers.average_latency()

    @property
    def fastest_provider(self) -> Provider | None:
        return self.providers.fastest()

    @property
    def slowest_provider(self) -> Provider | None:
        return self.providers.slowest()

    @property
    def live_capable(self) -> int:
        return len(self.providers.live_capable())

    @property
    def historical_capable(self) -> int:
        return len(self.providers.historical_capable())

    @property
    def websocket_capable(self) -> int:
        return len(self.providers.websocket_capable())

    @property
    def provider_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                provider.provider_type.value
                for provider in self.providers
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "connected": self.connected_count,
            "offline": self.offline_count,
            "average_latency": self.average_latency,
            "fastest_provider": (
                self.fastest_provider.name
                if self.fastest_provider
                else None
            ),
            "slowest_provider": (
                self.slowest_provider.name
                if self.slowest_provider
                else None
            ),
            "live_capable": self.live_capable,
            "historical_capable": self.historical_capable,
            "websocket_capable": self.websocket_capable,
            "provider_distribution": self.provider_distribution,
        }