"""
Tests for Watchlist analyzer.
"""

from ogs.market_data.watchlist import (
    Watchlist,
    WatchlistAnalyzer,
    WatchlistCollection,
    WatchlistStatus,
    WatchlistType,
)


def test_analyze():

    collection = WatchlistCollection()

    collection.add(
        Watchlist(
            watchlist_id="WL001",
            watchlist_name="Swing",
            watchlist_type=WatchlistType.PERSONAL,
            status=WatchlistStatus.ACTIVE,
            symbols=["RELIANCE"],
        )
    )

    analyzer = WatchlistAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "watchlist_analysis" in result
    assert "distribution_analysis" in result