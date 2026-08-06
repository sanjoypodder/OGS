"""
===========================================================

OGS Smart Money AI

Industry Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import IndustryCollection
from .statistics import IndustryStatistics


class IndustryAnalyzer(
    BaseAnalyzer[
        IndustryCollection,
        dict,
    ]
):
    """
    Industry Analyzer.
    """

    def analyze(
        self,
        data: IndustryCollection,
    ) -> dict:

        statistics = IndustryStatistics(
            data
        )

        return {
            "summary": (
                statistics.summary()
            ),
            "industry_analysis": {
                "total_industries": (
                    statistics.count
                ),
                "active_industries": (
                    statistics.active_count
                ),
            },
            "distribution_analysis": {
                "industry_type": (
                    statistics.distribution()
                ),
            },
        }