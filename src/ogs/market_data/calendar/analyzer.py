"""
===========================================================

OGS Smart Money AI

Calendar Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import CalendarCollection
from .statistics import CalendarStatistics


class CalendarAnalyzer(
    BaseAnalyzer[
        CalendarCollection,
        dict,
    ]
):
    """
    Calendar Analyzer.
    """

    def analyze(
        self,
        data: CalendarCollection,
    ) -> dict:

        statistics = CalendarStatistics(data)

        return {
            "summary": statistics.summary(),
            "calendar_analysis": {
                "total_days": statistics.count,
                "trading_days": statistics.trading_day_count,
                "holidays": statistics.holiday_count,
                "open_days": statistics.open_count,
            },
            "distribution_analysis": {
                "calendar_type": statistics.distribution(),
            },
        }