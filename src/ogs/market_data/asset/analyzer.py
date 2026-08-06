"""
OGS Smart Money AI

Asset Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import AssetCollection
from .statistics import AssetStatistics


class AssetAnalyzer(BaseAnalyzer):
    """
    Analyzer for Asset collections.
    """

    def __init__(
        self,
        collection: AssetCollection,
    ):
        self.collection = collection
        self.statistics = AssetStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "asset_analysis": self.asset_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def asset_analysis(self) -> dict:
        return {
            "count": self.statistics.count,
            "active_count": self.statistics.active_count,
            "inactive_count": self.statistics.inactive_count,
            "equity_count": self.statistics.equity_count,
            "crypto_count": self.statistics.crypto_count,
            "forex_count": self.statistics.forex_count,
            "commodity_count": self.statistics.commodity_count,
        }

    def distribution_analysis(self) -> dict:
        return {
            "asset_type": self.statistics.distribution,
        }