"""
OGS Smart Money AI

Instrument Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import InstrumentCollection
from .statistics import InstrumentStatistics


class InstrumentAnalyzer(BaseAnalyzer):
    """
    Analyzer for Instrument collections.
    """

    def __init__(
        self,
        collection: InstrumentCollection,
    ):
        self.collection = collection
        self.statistics = InstrumentStatistics(collection)

    def analyze(self) -> dict:
        return {
            "summary": self.summary(),
            "instrument_analysis": self.instrument_analysis(),
            "distribution_analysis": self.distribution_analysis(),
        }

    def summary(self) -> dict:
        return self.statistics.summary()

    def instrument_analysis(self) -> dict:
        return {
            "count": self.statistics.count,
            "active_count": self.statistics.active_count,
            "inactive_count": self.statistics.inactive_count,
            "equity_count": self.statistics.equity_count,
            "crypto_count": self.statistics.crypto_count,
            "forex_count": self.statistics.forex_count,
            "future_count": self.statistics.future_count,
            "option_count": self.statistics.option_count,
        }

    def distribution_analysis(self) -> dict:
        return {
            "instrument_type": self.statistics.distribution,
        }