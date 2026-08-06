"""
OGS Smart Money AI

Trade Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import TradeCollection
from .statistics import TradeStatistics


class TradeAnalyzer(BaseAnalyzer):
    """
    Analyzer for Trade collections.
    """

    def __init__(
        self,
        collection: TradeCollection,
    ):
        self.collection = collection
        self.statistics = TradeStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "trade_analysis": self.trade_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def trade_analysis(self) -> dict:
        return {
            "buy_count": self.statistics.buy_count,
            "sell_count": self.statistics.sell_count,
            "filled_count": self.statistics.filled_count,
            "total_value": self.statistics.total_value,
            "total_fees": self.statistics.total_fees,
            "average_price": self.statistics.average_price,
            "average_quantity": self.statistics.average_quantity,
        }

    def distribution_analysis(self) -> dict:
        return {
            "providers": self.statistics.provider_distribution,
            "symbols": self.statistics.symbol_distribution,
        }