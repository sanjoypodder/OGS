"""
CorporateEvent Analyzer
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import CorporateEventCollection
from .statistics import (
    CorporateEventStatistics,
)


class CorporateEventAnalyzer(
    BaseAnalyzer[
        CorporateEventCollection,
        dict,
    ]
):
    """
    Corporate event analyzer.
    """

    def analyze(
        self,
        data: CorporateEventCollection,
    ) -> dict:

        statistics = (
            CorporateEventStatistics(data)
        )

        return {
            "summary":
                statistics.summary(),
            "corporate_event_analysis": {
                "total_events":
                    statistics.count,
                "active_events":
                    statistics.active_count,
                "exchange_distribution":
                    statistics.exchange_distribution(),
                "market_distribution":
                    statistics.market_distribution(),
            },
            "distribution_analysis": {
                "event_type":
                    statistics.event_type_distribution(),
                "event_status":
                    statistics.status_distribution(),
            },
        }