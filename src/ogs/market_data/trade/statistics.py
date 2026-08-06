"""
OGS Smart Money AI

Trade Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import TradeCollection


class TradeStatistics(BaseStatistics):
    """
    Statistics for TradeCollection.
    """

    def __init__(
        self,
        collection: TradeCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def buy_count(self) -> int:
        return len(self.collection.buys())

    @property
    def sell_count(self) -> int:
        return len(self.collection.sells())

    @property
    def filled_count(self) -> int:
        return len(self.collection.filled())

    @property
    def total_value(self) -> float:
        return self.collection.total_value()

    @property
    def total_fees(self) -> float:
        return self.collection.total_fees()

    @property
    def average_price(self) -> float:

        if len(self.collection) == 0:
            return 0.0

        return (
            sum(
                trade.price
                for trade in self.collection
            )
            / len(self.collection)
        )

    @property
    def average_quantity(self) -> float:

        if len(self.collection) == 0:
            return 0.0

        return (
            sum(
                trade.quantity
                for trade in self.collection
            )
            / len(self.collection)
        )

    @property
    def provider_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                trade.provider
                for trade in self.collection
            )
        )

    @property
    def symbol_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                trade.symbol
                for trade in self.collection
            )
        )

    def summary(self) -> dict:

        return {
            "count": self.count,
            "buy_count": self.buy_count,
            "sell_count": self.sell_count,
            "filled_count": self.filled_count,
            "total_value": self.total_value,
            "total_fees": self.total_fees,
            "average_price": self.average_price,
            "average_quantity": self.average_quantity,
            "provider_distribution": self.provider_distribution,
            "symbol_distribution": self.symbol_distribution,
        }