"""
TradingSessionTemplate Analyzer
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import (
    TradingSessionTemplateCollection,
)
from .statistics import (
    TradingSessionTemplateStatistics,
)


class TradingSessionTemplateAnalyzer(
    BaseAnalyzer[
        TradingSessionTemplateCollection,
        dict,
    ]
):
    """
    Trading session template analyzer.
    """

    def analyze(
        self,
        data: TradingSessionTemplateCollection,
    ) -> dict:

        statistics = (
            TradingSessionTemplateStatistics(
                data
            )
        )

        return {
            "summary":
                statistics.summary(),
            "trading_session_template_analysis": {
                "total_templates":
                    statistics.count,
                "active_templates":
                    statistics.active_count,
                "exchange_distribution":
                    statistics.exchange_distribution(),
                "market_distribution":
                    statistics.market_distribution(),
            },
            "distribution_analysis": {
                "session_type":
                    statistics.session_type_distribution(),
            },
        }