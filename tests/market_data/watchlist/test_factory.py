"""
Tests for Watchlist factory.
"""

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistFactory,
    WatchlistStatus,
    WatchlistType,
)


def test_create():

    obj = WatchlistFactory.create(
        "WL001",
        "Swing",
    )

    assert isinstance(obj, Watchlist)


def test_personal():

    obj = WatchlistFactory.personal(
        "WL001",
        "Personal",
    )

    assert obj.watchlist_type == WatchlistType.PERSONAL
    assert obj.status == WatchlistStatus.ACTIVE


def test_smart_money():

    obj = WatchlistFactory.smart_money(
        "WL002",
        "SMC",
    )

    assert obj.watchlist_type == WatchlistType.SMART_MONEY
    assert obj.status == WatchlistStatus.ACTIVE


def test_clone():

    obj = WatchlistFactory.create(
        "WL001",
        "Swing",
    )

    clone = WatchlistFactory.clone(obj)

    assert clone == obj
    assert clone is not obj