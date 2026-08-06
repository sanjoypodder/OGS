"""
===========================================================

OGS Smart Money AI

Metadata Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import (
    BaseAnalyzer,
)

from .collection import MetadataCollection
from .statistics import MetadataStatistics


class MetadataAnalyzer(
    BaseAnalyzer[
        MetadataCollection,
        dict,
    ]
):
    """
    Metadata Analyzer.
    """

    def analyze(
        self,
        data: MetadataCollection,
    ) -> dict:

        statistics = MetadataStatistics(
            data
        )

        return {
            "summary": (
                statistics.summary()
            ),
            "metadata_analysis": {
                "total_metadata": (
                    statistics.count
                ),
                "active_metadata": (
                    statistics.active_count
                ),
                "entity_types": (
                    statistics.entity_distribution()
                ),
            },
            "distribution_analysis": {
                "metadata_type": (
                    statistics.metadata_distribution()
                ),
                "value_type": (
                    statistics.value_distribution()
                ),
            },
        }