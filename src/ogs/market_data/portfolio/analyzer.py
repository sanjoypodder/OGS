"""
OGS Smart Money AI

Portfolio Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import PortfolioCollection
from .statistics import PortfolioStatistics


class PortfolioAnalyzer(BaseAnalyzer):
    """
    Analyzer for Portfolio collections.
    """

    def __init__(
        self,
        collection: PortfolioCollection,
    ):
        self.collection = collection
        self.statistics = PortfolioStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "portfolio_analysis": self.portfolio_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def portfolio_analysis(self) -> dict:
        return {
            "active_count": self.statistics.active_count,
            "inactive_count": self.statistics.inactive_count,
            "live_count": self.statistics.live_count,
            "paper_count": self.statistics.paper_count,
            "backtest_count": self.statistics.backtest_count,
            "total_equity": self.statistics.total_equity,
            "total_market_value": self.statistics.total_market_value,
            "total_cash": self.statistics.total_cash,
            "total_realized_pnl": self.statistics.total_realized_pnl,
            "total_unrealized_pnl": self.statistics.total_unrealized_pnl,
            "total_pnl": self.statistics.total_pnl,
            "average_return": self.statistics.average_return,
        }

    def distribution_analysis(self) -> dict:
        return {
            "status": self.statistics.status_distribution,
            "types": self.statistics.type_distribution,
        }