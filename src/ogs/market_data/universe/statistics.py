"""
===========================================================

OGS Smart Money AI

Universe Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import UniverseCollection
from .enums import UniverseType


class UniverseStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: UniverseCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def active_count(self):

        return len(
            self.collection.active()
        )

    @property
    def total_symbols(self):

        return sum(
            universe.symbol_count
            for universe in self.collection
        )

    def distribution(self):

        return {
            universe_type.name: sum(
                1
                for universe in self.collection
                if universe.universe_type == universe_type
            )
            for universe_type in UniverseType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
            "symbols": self.total_symbols,
        }