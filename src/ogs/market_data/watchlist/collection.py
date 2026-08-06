"""
===========================================================

OGS Smart Money AI

Watchlist Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Watchlist
from .enums import WatchlistType


class WatchlistCollection(
    BaseCollection[Watchlist],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        watchlist: Watchlist,
    ) -> None:

        self._items.append(watchlist)

    def find(
        self,
        watchlist_id: str,
    ) -> Watchlist | None:

        for watchlist in self._items:

            if (
                watchlist.watchlist_id
                == watchlist_id
            ):
                return watchlist

        return None

    def by_type(
        self,
        watchlist_type: WatchlistType,
    ):

        return [
            watchlist
            for watchlist in self._items
            if (
                watchlist.watchlist_type
                == watchlist_type
            )
        ]

    def active(self):

        return [
            watchlist
            for watchlist in self._items
            if watchlist.is_active
        ]

    def to_list(self):

        return list(self._items)