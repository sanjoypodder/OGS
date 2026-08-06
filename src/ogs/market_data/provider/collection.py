"""
OGS Smart Money AI

Provider Collection
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator

from ogs.framework import BaseCollection

from .domain import Provider
from .enums import (
    ConnectionStatus,
    ProviderType,
)


class ProviderCollection(BaseCollection):
    """
    Collection of Provider objects.
    """

    def __init__(self, providers: Iterable[Provider] = ()) -> None:
        self._providers = list(providers)

    def __iter__(self) -> Iterator[Provider]:
        return iter(self._providers)

    def __len__(self) -> int:
        return len(self._providers)

    def __getitem__(self, index: int) -> Provider:
        return self._providers[index]

    def add(self, provider: Provider) -> None:
        self._providers.append(provider)

    def connected(self) -> "ProviderCollection":
        return ProviderCollection(
            p
            for p in self._providers
            if p.status == ConnectionStatus.CONNECTED
        )

    def disconnected(self) -> "ProviderCollection":
        return ProviderCollection(
            p
            for p in self._providers
            if p.status == ConnectionStatus.DISCONNECTED
        )

    def live_capable(self) -> "ProviderCollection":
        return ProviderCollection(
            p
            for p in self._providers
            if p.supports_live
        )

    def historical_capable(self) -> "ProviderCollection":
        return ProviderCollection(
            p
            for p in self._providers
            if p.supports_historical
        )

    def websocket_capable(self) -> "ProviderCollection":
        return ProviderCollection(
            p
            for p in self._providers
            if p.supports_websocket
        )

    def by_type(
        self,
        provider_type: ProviderType,
    ) -> "ProviderCollection":
        return ProviderCollection(
            p
            for p in self._providers
            if p.provider_type == provider_type
        )

    def find(self, name: str) -> Provider | None:
        name = name.casefold()

        for provider in self._providers:
            if provider.name.casefold() == name:
                return provider

        return None

    def names(self) -> list[str]:
        return sorted(provider.name for provider in self._providers)

    def fastest(self) -> Provider | None:
        if not self._providers:
            return None

        return min(self._providers, key=lambda p: p.latency_ms)

    def slowest(self) -> Provider | None:
        if not self._providers:
            return None

        return max(self._providers, key=lambda p: p.latency_ms)

    def average_latency(self) -> float:
        if not self._providers:
            return 0.0

        return (
            sum(p.latency_ms for p in self._providers)
            / len(self._providers)
        )

    def to_list(self) -> list[Provider]:
        return list(self._providers)