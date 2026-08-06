"""
Tests for Watchlist analyzer performance.
"""

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistAnalyzer,
    WatchlistCollection,
    WatchlistStatus,
    WatchlistType,
)


def test_large_collection():

    collection = WatchlistCollection()

    for i in range(1000):

        collection.add(
            Watchlist(
                watchlist_id=f"WL{i}",
                watchlist_name=f"Watchlist {i}",
                watchlist_type=WatchlistType.PERSONAL,
                status=WatchlistStatus.ACTIVE,
                symbols=["AAPL", "MSFT"],
            )
        )

    analyzer = WatchlistAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000

    assert (
        result["watchlist_analysis"]["total_watchlists"]
        == 1000
    )

    assert (
        result["watchlist_analysis"]["active_watchlists"]
        == 1000
    )

    assert (
        result["watchlist_analysis"]["total_symbols"]
        == 2000
    )