"""
===========================================================

OGS Smart Money AI

Sector Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import SectorCollection
from .statistics import SectorStatistics


class SectorAnalyzer(
    BaseAnalyzer[
        SectorCollection,
        dict,
    ]
):
    """
    Sector Analyzer.
    """

    def analyze(
        self,
        data: SectorCollection,
    ) -> dict:

        statistics = SectorStatistics(
            data
        )

        return {
            "summary": statistics.summary(),
            "sector_analysis": {
                "total_sectors": statistics.count,
                "active_sectors": (
                    statistics.active_count
                ),
            },
            "distribution_analysis": {
                "sector_type": (
                    statistics.distribution()
                ),
            },
        }