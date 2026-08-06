"""
===========================================================

OGS Smart Money AI

Screener Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import ScreenerCollection
from .enums import ScreenerType


class ScreenerStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: ScreenerCollection,
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
    def total_filters(self):

        return sum(
            item.filter_count
            for item in self.collection
        )

    def distribution(self):

        return {
            screener_type.name: sum(
                1
                for screener in self.collection
                if (
                    screener.screener_type
                    == screener_type
                )
            )
            for screener_type
            in ScreenerType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
            "filters": self.total_filters,
        }