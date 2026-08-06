"""
Tests for Watchlist analyzer distribution.
"""

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistAnalyzer,
    WatchlistCollection,
    WatchlistStatus,
    WatchlistType,
)


def test_distribution_detection():

    collection = WatchlistCollection()

    collection.add(
        Watchlist(
            watchlist_id="WL001",
            watchlist_name="Personal",
            watchlist_type=WatchlistType.PERSONAL,
            status=WatchlistStatus.ACTIVE,
        )
    )

    collection.add(
        Watchlist(
            watchlist_id="WL002",
            watchlist_name="SMC",
            watchlist_type=WatchlistType.SMART_MONEY,
            status=WatchlistStatus.ACTIVE,
        )
    )

    analyzer = WatchlistAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert (
        distribution["watchlist_type"]["PERSONAL"]
        == 1
    )

    assert (
        distribution["watchlist_type"]["SMART_MONEY"]
        == 1
    )