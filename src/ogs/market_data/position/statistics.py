"""
OGS Smart Money AI

Position Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import PositionCollection


class PositionStatistics(BaseStatistics):
    """
    Statistics for PositionCollection.
    """

    def __init__(
        self,
        collection: PositionCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def long_count(self) -> int:
        return len(self.collection.longs())

    @property
    def short_count(self) -> int:
        return len(self.collection.shorts())

    @property
    def open_count(self) -> int:
        return len(self.collection.open_positions())

    @property
    def closed_count(self) -> int:
        return len(self.collection.closed_positions())

    @property
    def total_market_value(self) -> float:
        return self.collection.total_market_value()

    @property
    def total_cost_basis(self) -> float:
        return self.collection.total_cost_basis()

    @property
    def total_realized_pnl(self) -> float:
        return self.collection.total_realized_pnl()

    @property
    def total_unrealized_pnl(self) -> float:
        return self.collection.total_unrealized_pnl()

    @property
    def total_pnl(self) -> float:
        return self.collection.total_pnl()

    @property
    def average_return(self) -> float:

        if len(self.collection) == 0:
            return 0.0

        return (
            sum(
                position.return_percentage
                for position in self.collection
            )
            / len(self.collection)
        )

    @property
    def provider_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                position.provider
                for position in self.collection
            )
        )

    @property
    def symbol_distribution(self) -> dict[str, int]:

        return dict(
            Counter(
                position.symbol
                for position in self.collection
            )
        )

    def summary(self) -> dict:

        return {
            "count": self.count,
            "long_count": self.long_count,
            "short_count": self.short_count,
            "open_count": self.open_count,
            "closed_count": self.closed_count,
            "total_market_value": self.total_market_value,
            "total_cost_basis": self.total_cost_basis,
            "total_realized_pnl": self.total_realized_pnl,
            "total_unrealized_pnl": self.total_unrealized_pnl,
            "total_pnl": self.total_pnl,
            "average_return": self.average_return,
            "provider_distribution": self.provider_distribution,
            "symbol_distribution": self.symbol_distribution,
        }