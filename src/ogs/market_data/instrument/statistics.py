"""
OGS Smart Money AI

Instrument Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import InstrumentCollection


class InstrumentStatistics(BaseStatistics):
    """
    Statistics for InstrumentCollection.
    """

    def __init__(
        self,
        collection: InstrumentCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def active_count(self) -> int:
        return len(self.collection.active())

    @property
    def inactive_count(self) -> int:
        return len(self.collection.inactive())

    @property
    def equity_count(self) -> int:
        return len(self.collection.equities())

    @property
    def crypto_count(self) -> int:
        return len(self.collection.crypto())

    @property
    def forex_count(self) -> int:
        return len(self.collection.forex())

    @property
    def future_count(self) -> int:
        return len(self.collection.futures())

    @property
    def option_count(self) -> int:
        return len(self.collection.options())

    @property
    def distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                item.instrument_type.value
                for item in self.collection
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "active_count": self.active_count,
            "inactive_count": self.inactive_count,
            "equity_count": self.equity_count,
            "crypto_count": self.crypto_count,
            "forex_count": self.forex_count,
            "future_count": self.future_count,
            "option_count": self.option_count,
            "distribution": self.distribution,
        }