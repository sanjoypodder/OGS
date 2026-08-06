"""
===========================================================

OGS Smart Money AI

Currency Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import CurrencyCollection
from .statistics import CurrencyStatistics


class CurrencyAnalyzer(BaseAnalyzer):
    """
    Analyzer for Currency collections.
    """

    def __init__(
        self,
        collection: CurrencyCollection,
    ):
        self.collection = collection
        self.statistics = CurrencyStatistics(collection)

    def analyze(self) -> dict:
        """
        Perform Currency analysis.
        """

        return {
            "summary": self.summary(),
            "currency_analysis": self.currency_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        """
        Return Currency summary statistics.
        """

        return self.statistics.summary()

    def currency_analysis(self) -> dict:
        """
        Return core Currency statistics.
        """

        return {
            "count": self.statistics.count,
            "fiat_count": self.statistics.fiat_count,
            "crypto_count": self.statistics.crypto_count,
        }

    def distribution_analysis(self) -> dict:
        """
        Return Currency type distribution.
        """

        return {
            "currency_type": self.statistics.distribution(),
        }