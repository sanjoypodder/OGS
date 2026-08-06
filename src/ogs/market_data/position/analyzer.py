"""
OGS Smart Money AI

Position Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import PositionCollection
from .statistics import PositionStatistics


class PositionAnalyzer(BaseAnalyzer):
    """
    Analyzer for Position collections.
    """

    def __init__(
        self,
        collection: PositionCollection,
    ):
        self.collection = collection
        self.statistics = PositionStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "position_analysis": self.position_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def position_analysis(self) -> dict:
        return {
            "long_count": self.statistics.long_count,
            "short_count": self.statistics.short_count,
            "open_count": self.statistics.open_count,
            "closed_count": self.statistics.closed_count,
            "total_market_value": self.statistics.total_market_value,
            "total_cost_basis": self.statistics.total_cost_basis,
            "total_realized_pnl": self.statistics.total_realized_pnl,
            "total_unrealized_pnl": self.statistics.total_unrealized_pnl,
            "total_pnl": self.statistics.total_pnl,
            "average_return": self.statistics.average_return,
        }

    def distribution_analysis(self) -> dict:
        return {
            "providers": self.statistics.provider_distribution,
            "symbols": self.statistics.symbol_distribution,
        }