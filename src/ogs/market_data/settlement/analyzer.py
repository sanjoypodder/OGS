"""
Settlement Analyzer
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import SettlementCollection
from .statistics import SettlementStatistics


class SettlementAnalyzer(
    BaseAnalyzer[
        SettlementCollection,
        dict,
    ]
):
    """
    Settlement analyzer.
    """

    def analyze(
        self,
        data: SettlementCollection,
    ) -> dict:

        statistics = SettlementStatistics(
            data
        )

        return {
            "summary": (
                statistics.summary()
            ),
            "settlement_analysis": {
                "total_settlements":
                    statistics.count,
                "active_settlements":
                    statistics.active_count,
                "exchange_distribution":
                    statistics.exchange_distribution(),
                "market_distribution":
                    statistics.market_distribution(),
            },
            "distribution_analysis": {
                "settlement_cycle":
                    statistics.cycle_distribution(),
                "settlement_type":
                    statistics.type_distribution(),
            },
        }