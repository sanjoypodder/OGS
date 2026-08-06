"""
OGS Smart Money AI

Quote Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import QuoteCollection
from .statistics import QuoteStatistics


class QuoteAnalyzer(BaseAnalyzer):
    """
    Analyzer for Quote collections.
    """

    def __init__(
        self,
        collection: QuoteCollection,
    ):
        self.collection = collection
        self.statistics = QuoteStatistics(
            collection
        )

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "spread_analysis": self.spread_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def spread_analysis(self) -> dict:
        return {
            "average_spread": self.statistics.average_spread,
        }

    def distribution_analysis(self) -> dict:
        return {
            "types": self.statistics.type_distribution,
            "status": self.statistics.status_distribution,
            "providers": self.statistics.provider_distribution,
        }