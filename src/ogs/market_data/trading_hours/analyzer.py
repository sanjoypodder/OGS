"""
TradingHours Analyzer
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import TradingHoursCollection
from .statistics import TradingHoursStatistics


class TradingHoursAnalyzer(
    BaseAnalyzer[
        TradingHoursCollection,
        dict,
    ]
):

    def analyze(
        self,
        data: TradingHoursCollection,
    ) -> dict:

        statistics = TradingHoursStatistics(
            data
        )

        return {
            "summary": (
                statistics.summary()
            ),
            "trading_hours_analysis": {
                "total_trading_hours":
                    statistics.count,
                "active_trading_hours":
                    statistics.active_count,
                "exchange_distribution":
                    statistics.exchange_distribution(),
                "market_distribution":
                    statistics.market_distribution(),
            },
            "distribution_analysis": {
                "trading_hours_type":
                    statistics.type_distribution(),
            },
        }