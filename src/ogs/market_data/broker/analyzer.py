"""
OGS Smart Money AI

Broker Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import BrokerCollection
from .statistics import BrokerStatistics


class BrokerAnalyzer(BaseAnalyzer):
    """
    Analyzer for Broker collections.
    """

    def __init__(
        self,
        collection: BrokerCollection,
    ):
        self.collection = collection
        self.statistics = BrokerStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "broker_analysis": self.broker_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def broker_analysis(self) -> dict:
        return {
            "active_count": self.statistics.active_count,
            "inactive_count": self.statistics.inactive_count,
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