"""
===========================================================

OGS Smart Money AI

Watchlist Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import WatchlistCollection
from .statistics import WatchlistStatistics


class WatchlistAnalyzer(
    BaseAnalyzer[
        WatchlistCollection,
        dict,
    ]
):
    """
    Watchlist Analyzer.
    """

    def analyze(
        self,
        data: WatchlistCollection,
    ) -> dict:

        statistics = WatchlistStatistics(
            data
        )

        return {
            "summary": (
                statistics.summary()
            ),
            "watchlist_analysis": {
                "total_watchlists": (
                    statistics.count
                ),
                "active_watchlists": (
                    statistics.active_count
                ),
                "total_symbols": (
                    statistics.total_symbols
                ),
            },
            "distribution_analysis": {
                "watchlist_type": (
                    statistics.distribution()
                ),
            },
        }