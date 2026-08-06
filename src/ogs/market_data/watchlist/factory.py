"""
===========================================================

OGS Smart Money AI

Watchlist Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Watchlist
from .enums import (
    WatchlistStatus,
    WatchlistType,
)


class WatchlistFactory:
    """
    Watchlist Factory.
    """

    @staticmethod
    def create(
        watchlist_id: str,
        watchlist_name: str,
        **kwargs,
    ) -> Watchlist:

        return Watchlist(
            watchlist_id=watchlist_id,
            watchlist_name=watchlist_name,
            **kwargs,
        )

    @staticmethod
    def personal(
        watchlist_id: str,
        watchlist_name: str,
        **kwargs,
    ) -> Watchlist:

        return Watchlist(
            watchlist_id=watchlist_id,
            watchlist_name=watchlist_name,
            watchlist_type=WatchlistType.PERSONAL,
            status=WatchlistStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def smart_money(
        watchlist_id: str,
        watchlist_name: str,
        **kwargs,
    ) -> Watchlist:

        return Watchlist(
            watchlist_id=watchlist_id,
            watchlist_name=watchlist_name,
            watchlist_type=WatchlistType.SMART_MONEY,
            status=WatchlistStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        watchlist: Watchlist,
    ) -> Watchlist:

        return deepcopy(watchlist)