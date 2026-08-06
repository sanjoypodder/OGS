"""
OGS Smart Money AI

Tick Analyzer
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseAnalyzer

from .collection import TickCollection
from .domain import Tick
from .statistics import TickStatistics


class TickAnalyzer(BaseAnalyzer):
    """
    High-level analysis utilities for TickCollection.
    """

    def analyze(self, collection: TickCollection) -> dict:
        """
        Return complete analysis.
        """
        stats = TickStatistics(collection)

        return stats.summary()

    def statistics(
        self,
        collection: TickCollection,
    ) -> TickStatistics:
        """
        Return statistics object.
        """
        return TickStatistics(collection)

    def latest(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.latest()

    def oldest(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.oldest()

    def find(
        self,
        collection: TickCollection,
        symbol: str,
    ) -> Tick | None:
        return collection.find(symbol)

    def highest_bid(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.highest_bid()

    def lowest_bid(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.lowest_bid()

    def highest_ask(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.highest_ask()

    def lowest_ask(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.lowest_ask()

    def highest_trade(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.highest_trade()

    def lowest_trade(
        self,
        collection: TickCollection,
    ) -> Tick | None:
        return collection.lowest_trade()

    def largest_spread(
        self,
        collection: TickCollection,
    ) -> Tick | None:

        if not collection:
            return None

        return max(
            collection,
            key=lambda tick: tick.spread,
        )

    def smallest_spread(
        self,
        collection: TickCollection,
    ) -> Tick | None:

        if not collection:
            return None

        return min(
            collection,
            key=lambda tick: tick.spread,
        )

    def volume_analysis(
        self,
        collection: TickCollection,
    ) -> dict:

        stats = TickStatistics(collection)

        return {
            "total_volume": stats.total_volume,
            "buy_ticks": stats.buy_ticks,
            "sell_ticks": stats.sell_ticks,
        }

    def spread_analysis(
        self,
        collection: TickCollection,
    ) -> dict:

        stats = TickStatistics(collection)

        return {
            "average_spread": stats.average_spread,
            "maximum_spread": stats.max_spread,
            "minimum_spread": stats.min_spread,
        }

    def provider_analysis(
        self,
        collection: TickCollection,
    ) -> dict:

        return dict(
            Counter(
                tick.provider.value
                for tick in collection
            )
        )

    def symbol_analysis(
        self,
        collection: TickCollection,
    ) -> dict:

        return dict(
            Counter(
                tick.symbol
                for tick in collection
            )
        )

    def price_distribution(
        self,
        collection: TickCollection,
    ) -> dict:

        if not collection:
            return {}

        prices = [tick.last for tick in collection]

        return {
            "minimum": min(prices),
            "maximum": max(prices),
            "average": sum(prices) / len(prices),
        }

    def summary(
        self,
        collection: TickCollection,
    ) -> dict:
        """
        Alias for analyze().
        """
        return self.analyze(collection)

    def __call__(
        self,
        collection: TickCollection,
    ) -> dict:
        """
        Callable interface.
        """
        return self.analyze(collection)