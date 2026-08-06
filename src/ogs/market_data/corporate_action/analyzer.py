"""
===========================================================

OGS Smart Money AI

Corporate Action Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import (
    CorporateActionCollection,
)
from .statistics import (
    CorporateActionStatistics,
)


class CorporateActionAnalyzer(
    BaseAnalyzer[
        CorporateActionCollection,
        dict,
    ]
):
    """
    Corporate Action Analyzer.
    """

    def analyze(
        self,
        data: CorporateActionCollection,
    ) -> dict:

        statistics = CorporateActionStatistics(
            data
        )

        return {
            "summary": statistics.summary(),
            "corporate_action_analysis": {
                "total_actions": statistics.count,
                "dividends": (
                    statistics.dividend_count
                ),
                "effective_actions": (
                    statistics.effective_count
                ),
            },
            "distribution_analysis": {
                "action_type": (
                    statistics.distribution()
                ),
            },
        }