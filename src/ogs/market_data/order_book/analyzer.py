"""
OGS Smart Money AI

OrderBook Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import OrderBookCollection
from .statistics import OrderBookStatistics


class OrderBookAnalyzer(BaseAnalyzer):
    """
    Analyzer for OrderBook collections.
    """

    def __init__(
        self,
        collection: OrderBookCollection,
    ):
        self.collection = collection
        self.statistics = OrderBookStatistics(collection)

    def analyze(self) -> dict:
        """
        Complete analysis.
        """
        return {
            "summary": self.summary(),
            "spread_analysis": self.spread_analysis(),
            "distribution_analysis": self.distribution_analysis(),
            "imbalance_analysis": self.imbalance_analysis(),
        }

    def summary(self) -> dict:
        """
        Summary statistics.
        """
        return self.statistics.summary()

    def spread_analysis(self) -> dict:
        """
        Spread analysis.
        """
        return {
            "average_spread": self.statistics.average_spread,
        }

    def imbalance_analysis(self) -> dict:
        """
        Order book imbalance analysis.
        """
        return {
            "average_imbalance": self.statistics.average_imbalance,
        }

    def distribution_analysis(self) -> dict:
        """
        Distribution analysis.
        """
        return {
            "types": self.statistics.type_distribution,
            "status": self.statistics.status_distribution,
            "providers": self.statistics.provider_distribution,
        }