"""
Tests for Watchlist statistics.
"""

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistCollection,
    WatchlistStatistics,
    WatchlistStatus,
    WatchlistType,
)


def make(
    watchlist_id,
    name,
    watchlist_type,
    status,
    symbols,
):

    return Watchlist(
        watchlist_id=watchlist_id,
        watchlist_name=name,
        watchlist_type=watchlist_type,
        status=status,
        symbols=symbols,
    )


def build_collection():

    collection = WatchlistCollection()

    collection.add(
        make(
            "WL001",
            "Swing",
            WatchlistType.PERSONAL,
            WatchlistStatus.ACTIVE,
            ["RELIANCE", "TCS"],
        )
    )

    collection.add(
        make(
            "WL002",
            "Smart Money",
            WatchlistType.SMART_MONEY,
            WatchlistStatus.ACTIVE,
            ["SBIN"],
        )
    )

    collection.add(
        make(
            "WL003",
            "Archived",
            WatchlistType.SYSTEM,
            WatchlistStatus.INACTIVE,
            [],
        )
    )

    return collection


def test_counts():

    stats = WatchlistStatistics(build_collection())

    assert stats.count == 3
    assert stats.active_count == 2
    assert stats.total_symbols == 3


def test_distribution():

    stats = WatchlistStatistics(build_collection())

    distribution = stats.distribution()

    assert distribution["PERSONAL"] == 1
    assert distribution["SMART_MONEY"] == 1
    assert distribution["SYSTEM"] == 1


def test_summary():

    stats = WatchlistStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2
    assert summary["symbols"] == 3