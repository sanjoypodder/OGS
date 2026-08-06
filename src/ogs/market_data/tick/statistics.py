"""
OGS Smart Money AI

Tick Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import TickCollection


class TickStatistics(BaseStatistics):
    """
    Statistical calculations for TickCollection.
    """

    def __init__(self, collection: TickCollection):

        super().__init__(collection)

    @property
    def average_bid(self) -> float:

        if self.empty:
            return 0.0

        return (
            sum(
                tick.bid
                for tick in self.collection
            )
            / self.count
        )

    @property
    def average_ask(self) -> float:

        if self.empty:
            return 0.0

        return (
            sum(
                tick.ask
                for tick in self.collection
            )
            / self.count
        )

    @property
    def average_last(self) -> float:

        if self.empty:
            return 0.0

        return (
            sum(
                tick.last
                for tick in self.collection
            )
            / self.count
        )

    @property
    def average_spread(self) -> float:

        if self.empty:
            return 0.0

        return (
            sum(
                tick.spread
                for tick in self.collection
            )
            / self.count
        )

    @property
    def highest_bid(self) -> float:

        if self.empty:
            return 0.0

        return max(
            tick.bid
            for tick in self.collection
        )

    @property
    def lowest_bid(self) -> float:

        if self.empty:
            return 0.0

        return min(
            tick.bid
            for tick in self.collection
        )

    @property
    def highest_ask(self) -> float:

        if self.empty:
            return 0.0

        return max(
            tick.ask
            for tick in self.collection
        )

    @property
    def lowest_ask(self) -> float:

        if self.empty:
            return 0.0

        return min(
            tick.ask
            for tick in self.collection
        )

    @property
    def highest_trade(self) -> float:

        if self.empty:
            return 0.0

        return max(
            tick.last
            for tick in self.collection
        )

    @property
    def lowest_trade(self) -> float:

        if self.empty:
            return 0.0

        return min(
            tick.last
            for tick in self.collection
        )

    @property
    def total_volume(self) -> float:

        return sum(
            tick.volume
            for tick in self.collection
        )

    @property
    def symbols(self) -> list[str]:

        return sorted(
            {
                tick.symbol
                for tick in self.collection
            }
        )

    @property
    def providers(self) -> list[str]:

        return sorted(
            {
                tick.provider.value
                for tick in self.collection
            }
        )

    @property
    def symbol_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                tick.symbol
                for tick in self.collection
            )
        )

    @property
    def provider_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                tick.provider.value
                for tick in self.collection
            )
        )

    @property
    def buy_ticks(self) -> int:

        return sum(
            tick.is_buy_tick
            for tick in self.collection
        )

    @property
    def sell_ticks(self) -> int:

        return sum(
            tick.is_sell_tick
            for tick in self.collection
        )

    @property
    def max_spread(self) -> float:

        if self.empty:
            return 0.0

        return max(
            tick.spread
            for tick in self.collection
        )

    @property
    def min_spread(self) -> float:

        if self.empty:
            return 0.0

        return min(
            tick.spread
            for tick in self.collection
        )

    def summary(self) -> dict:
        """
        Return complete statistical summary.
        """

        return {
            "count": self.count,
            "average_bid": self.average_bid,
            "average_ask": self.average_ask,
            "average_last": self.average_last,
            "highest_bid": self.highest_bid,
            "lowest_bid": self.lowest_bid,
            "highest_ask": self.highest_ask,
            "lowest_ask": self.lowest_ask,
            "highest_trade": self.highest_trade,
            "lowest_trade": self.lowest_trade,
            "average_spread": self.average_spread,
            "max_spread": self.max_spread,
            "min_spread": self.min_spread,
            "total_volume": self.total_volume,
            "buy_ticks": self.buy_ticks,
            "sell_ticks": self.sell_ticks,
            "symbols": self.symbols,
            "providers": self.providers,
            "symbol_distribution": self.symbol_distribution,
            "provider_distribution": self.provider_distribution,
        }

    def __repr__(self) -> str:

        return (
            f"TickStatistics("
            f"count={self.count}, "
            f"symbols={len(self.symbols)}, "
            f"providers={len(self.providers)})"
        )