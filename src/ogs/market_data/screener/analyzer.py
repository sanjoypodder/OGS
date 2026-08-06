"""
===========================================================

OGS Smart Money AI

Screener Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import ScreenerCollection
from .statistics import ScreenerStatistics


class ScreenerAnalyzer(
    BaseAnalyzer[
        ScreenerCollection,
        dict,
    ]
):
    """
    Screener Analyzer.
    """

    def analyze(
        self,
        data: ScreenerCollection,
    ) -> dict:

        statistics = ScreenerStatistics(
            data
        )

        return {
            "summary": (
                statistics.summary()
            ),
            "screener_analysis": {
                "total_screeners": (
                    statistics.count
                ),
                "active_screeners": (
                    statistics.active_count
                ),
                "total_filters": (
                    statistics.total_filters
                ),
            },
            "distribution_analysis": {
                "screener_type": (
                    statistics.distribution()
                ),
            },
        }