"""
===========================================================

OGS Smart Money AI

Watchlist Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import WatchlistCollection
from .enums import WatchlistType


class WatchlistStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: WatchlistCollection,
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
            item.symbol_count
            for item in self.collection
        )

    def distribution(self):

        return {
            watchlist_type.name: sum(
                1
                for watchlist in self.collection
                if (
                    watchlist.watchlist_type
                    == watchlist_type
                )
            )
            for watchlist_type
            in WatchlistType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
            "symbols": self.total_symbols,
        }