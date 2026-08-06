"""
===========================================================

OGS Smart Money AI

Index Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import IndexCollection
from .statistics import IndexStatistics


class IndexAnalyzer(
    BaseAnalyzer[
        IndexCollection,
        dict,
    ]
):
    """
    Index Analyzer.
    """

    def analyze(
        self,
        data: IndexCollection,
    ) -> dict:

        statistics = IndexStatistics(
            data
        )

        return {
            "summary": statistics.summary(),
            "index_analysis": {
                "total_indices": statistics.count,
                "active_indices": statistics.active_count,
            },
            "distribution_analysis": {
                "index_type": (
                    statistics.distribution()
                ),
            },
        }