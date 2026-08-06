"""
Tests for Watchlist collection.
"""

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistCollection,
    WatchlistStatus,
    WatchlistType,
)


def make(
    watchlist_id,
    name,
    watchlist_type,
    status,
):

    return Watchlist(
        watchlist_id=watchlist_id,
        watchlist_name=name,
        watchlist_type=watchlist_type,
        status=status,
    )


def test_add():

    collection = WatchlistCollection()

    collection.add(
        make(
            "WL001",
            "Swing",
            WatchlistType.PERSONAL,
            WatchlistStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = WatchlistCollection()

    obj = make(
        "WL001",
        "Swing",
        WatchlistType.PERSONAL,
        WatchlistStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("WL001") == obj
    assert collection.find("WL999") is None


def test_by_type():

    collection = WatchlistCollection()

    collection.add(
        make(
            "WL001",
            "Swing",
            WatchlistType.PERSONAL,
            WatchlistStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "WL002",
            "SMC",
            WatchlistType.SMART_MONEY,
            WatchlistStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            WatchlistType.PERSONAL
        )
    ) == 1

    assert len(
        collection.by_type(
            WatchlistType.SMART_MONEY
        )
    ) == 1


def test_active():

    collection = WatchlistCollection()

    collection.add(
        make(
            "WL001",
            "Swing",
            WatchlistType.PERSONAL,
            WatchlistStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "WL002",
            "Old",
            WatchlistType.SYSTEM,
            WatchlistStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = WatchlistCollection()

    collection.add(
        make(
            "WL001",
            "Swing",
            WatchlistType.PERSONAL,
            WatchlistStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1