"""
===========================================================

OGS Smart Money AI

Universe Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import UniverseCollection
from .statistics import UniverseStatistics


class UniverseAnalyzer(
    BaseAnalyzer[
        UniverseCollection,
        dict,
    ]
):
    """
    Universe Analyzer.
    """

    def analyze(
        self,
        data: UniverseCollection,
    ) -> dict:

        statistics = UniverseStatistics(
            data
        )

        return {
            "summary": (
                statistics.summary()
            ),
            "universe_analysis": {
                "total_universes": (
                    statistics.count
                ),
                "active_universes": (
                    statistics.active_count
                ),
                "total_symbols": (
                    statistics.total_symbols
                ),
            },
            "distribution_analysis": {
                "universe_type": (
                    statistics.distribution()
                ),
            },
        }