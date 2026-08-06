"""
OGS Smart Money AI

Tick Collection
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseCollection

from .domain import Tick
from .enums import ProviderType


class TickCollection(BaseCollection[Tick]):
    """
    Collection of Tick objects.
    """

    def __init__(self, items: list[Tick] | None = None):

        super().__init__()

        if items:
            self.extend(items)

    def latest(self) -> Tick | None:
        """Return latest tick."""

        if not self:
            return None

        return max(
            self,
            key=lambda x: x.timestamp,
        )

    def oldest(self) -> Tick | None:
        """Return oldest tick."""

        if not self:
            return None

        return min(
            self,
            key=lambda x: x.timestamp,
        )

    def highest_bid(self) -> Tick | None:
        """Tick with highest bid."""

        if not self:
            return None

        return max(
            self,
            key=lambda x: x.bid,
        )

    def lowest_bid(self) -> Tick | None:
        """Tick with lowest bid."""

        if not self:
            return None

        return min(
            self,
            key=lambda x: x.bid,
        )

    def highest_ask(self) -> Tick | None:
        """Tick with highest ask."""

        if not self:
            return None

        return max(
            self,
            key=lambda x: x.ask,
        )

    def lowest_ask(self) -> Tick | None:
        """Tick with lowest ask."""

        if not self:
            return None

        return min(
            self,
            key=lambda x: x.ask,
        )

    def highest_trade(self) -> Tick | None:
        """Highest traded price."""

        if not self:
            return None

        return max(
            self,
            key=lambda x: x.last,
        )

    def lowest_trade(self) -> Tick | None:
        """Lowest traded price."""

        if not self:
            return None

        return min(
            self,
            key=lambda x: x.last,
        )

    def by_provider(
        self,
        provider: ProviderType,
    ) -> "TickCollection":
        """Filter by provider."""

        return TickCollection(
            [
                tick
                for tick in self
                if tick.provider == provider
            ]
        )

    def by_symbol(
        self,
        symbol: str,
    ) -> "TickCollection":
        """Filter by symbol."""

        symbol = symbol.upper()

        return TickCollection(
            [
                tick
                for tick in self
                if tick.symbol.upper() == symbol
            ]
        )

    def find(
        self,
        symbol: str,
    ) -> Tick | None:
        """Return latest tick for symbol."""

        ticks = self.by_symbol(symbol)

        return ticks.latest()

    def between(
        self,
        start: datetime,
        end: datetime,
    ) -> "TickCollection":
        """Ticks between timestamps."""

        return TickCollection(
            [
                tick
                for tick in self
                if start <= tick.timestamp <= end
            ]
        )

    def latest_n(
        self,
        n: int,
    ) -> "TickCollection":
        """Latest N ticks."""

        return TickCollection(
            sorted(
                self,
                key=lambda x: x.timestamp,
                reverse=True,
            )[:n]
        )

    def first_n(
        self,
        n: int,
    ) -> "TickCollection":
        """Oldest N ticks."""

        return TickCollection(
            sorted(
                self,
                key=lambda x: x.timestamp,
            )[:n]
        )

    def symbols(self) -> list[str]:
        """Unique symbols."""

        return sorted(
            {
                tick.symbol
                for tick in self
            }
        )

    def providers(self) -> list[str]:
        """Unique providers."""

        return sorted(
            {
                tick.provider.value
                for tick in self
            }
        )

    def total_volume(self) -> float:
        """Total traded volume."""

        return sum(
            tick.volume
            for tick in self
        )

    def average_spread(self) -> float:
        """Average spread."""

        if not self:
            return 0.0

        return (
            sum(
                tick.spread
                for tick in self
            )
            / len(self)
        )

    def sort_by_time(
        self,
        reverse: bool = False,
    ) -> "TickCollection":
        """Sort by timestamp."""

        return TickCollection(
            sorted(
                self,
                key=lambda x: x.timestamp,
                reverse=reverse,
            )
        )

    def sort_by_price(
        self,
        reverse: bool = False,
    ) -> "TickCollection":
        """Sort by last traded price."""

        return TickCollection(
            sorted(
                self,
                key=lambda x: x.last,
                reverse=reverse,
            )
        )

    def clear_symbol(
        self,
        symbol: str,
    ) -> None:
        """Remove all ticks for a symbol."""

        symbol = symbol.upper()

        self._items = [
            tick
            for tick in self._items
            if tick.symbol.upper() != symbol
        ]