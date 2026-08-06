"""
OGS Smart Money AI

OrderBook Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import OrderBookCollection


class OrderBookStatistics(BaseStatistics):
    """
    Statistics for OrderBookCollection.
    """

    def __init__(
        self,
        collection: OrderBookCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def active_count(self) -> int:
        return len(self.collection.active())

    @property
    def inactive_count(self) -> int:
        return len(self.collection.inactive())

    @property
    def average_spread(self) -> float:

        spreads = [
            ob.spread
            for ob in self.collection
        ]

        if not spreads:
            return 0.0

        return sum(spreads) / len(spreads)

    @property
    def average_imbalance(self) -> float:

        values = [
            ob.imbalance_ratio
            for ob in self.collection
        ]

        if not values:
            return 0.0

        return sum(values) / len(values)

    @property
    def type_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                ob.orderbook_type.value
                for ob in self.collection
            )
        )

    @property
    def status_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                ob.status.value
                for ob in self.collection
            )
        )

    @property
    def provider_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                ob.provider
                for ob in self.collection
            )
        )

    def summary(self) -> dict:

        return {
            "count": self.count,
            "active": self.active_count,
            "inactive": self.inactive_count,
            "average_spread": self.average_spread,
            "average_imbalance": self.average_imbalance,
            "type_distribution": self.type_distribution,
            "status_distribution": self.status_distribution,
            "provider_distribution": self.provider_distribution,
        }