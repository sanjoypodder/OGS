"""
OGS Smart Money AI

Market Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import MarketCollection
from .statistics import MarketStatistics


class MarketAnalyzer(BaseAnalyzer):
    """
    Analyzer for Market collections.
    """

    def __init__(
        self,
        collection: MarketCollection,
    ):
        self.collection = collection
        self.statistics = MarketStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "market_analysis": self.market_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def market_analysis(self) -> dict:
        return {
            "exchange_count": self.statistics.exchange_count,
            "broker_count": self.statistics.broker_count,
            "account_count": self.statistics.account_count,
            "total_equity": self.statistics.total_equity,
            "total_cash": self.statistics.total_cash,
            "total_buying_power": self.statistics.total_buying_power,
            "total_margin_used": self.statistics.total_margin_used,
        }

    def distribution_analysis(self) -> dict:
        return {
            "status": self.statistics.status_distribution,
        }