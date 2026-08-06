"""
OGS Smart Money AI

Exchange Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import ExchangeCollection
from .statistics import ExchangeStatistics


class ExchangeAnalyzer(BaseAnalyzer):
    """
    Analyzer for Exchange collections.
    """

    def __init__(
        self,
        collection: ExchangeCollection,
    ):
        self.collection = collection
        self.statistics = ExchangeStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "exchange_analysis": self.exchange_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def exchange_analysis(self) -> dict:
        return {
            "open_count": self.statistics.open_count,
            "closed_count": self.statistics.closed_count,
            "total_brokers": self.statistics.total_brokers,
            "total_accounts": self.statistics.total_accounts,
            "total_equity": self.statistics.total_equity,
            "total_cash": self.statistics.total_cash,
            "total_buying_power": self.statistics.total_buying_power,
            "total_margin_used": self.statistics.total_margin_used,
        }

    def distribution_analysis(self) -> dict:
        return {
            "status": self.statistics.status_distribution,
        }