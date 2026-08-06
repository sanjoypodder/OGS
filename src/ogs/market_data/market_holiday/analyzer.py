"""
OGS Smart Money AI

MarketHoliday Analyzer
"""

from __future__ import annotations

from .collection import MarketHolidayCollection
from .statistics import MarketHolidayStatistics


class MarketHolidayAnalyzer:
    """
    Analyzer for MarketHoliday collections.
    """

    def analyze(
        self,
        holidays: MarketHolidayCollection,
    ) -> dict:
        """
        Perform complete market holiday analysis.
        """

        return {
            "summary": (
                MarketHolidayStatistics.summary(
                    holidays
                )
            ),
            "holiday_analysis": (
                self.analyze_holidays(
                    holidays
                )
            ),
            "distribution_analysis": (
                self.analyze_distribution(
                    holidays
                )
            ),
        }

    def analyze_holidays(
        self,
        holidays: MarketHolidayCollection,
    ) -> dict:
        """
        Analyze general holiday information.
        """

        summary = (
            MarketHolidayStatistics.summary(
                holidays
            )
        )

        return {
            "count": summary["count"],
            "active_count": summary["active"],
            "half_day_count": summary["half_day"],
            "special_trading_count": (
                summary["special_trading"]
            ),
            "emergency_count": (
                summary["emergency"]
            ),
        }

    def analyze_distribution(
        self,
        holidays: MarketHolidayCollection,
    ) -> dict:
        """
        Analyze holiday distributions.
        """

        return {
            "holiday_type": (
                MarketHolidayStatistics
                .type_distribution(
                    holidays
                )
            ),
            "status": (
                MarketHolidayStatistics
                .status_distribution(
                    holidays
                )
            ),
            "exchange": (
                MarketHolidayStatistics
                .exchange_distribution(
                    holidays
                )
            ),
        }