"""
Tests for Watchlist analyzer edge cases.
"""

from ogs.market_data.watchlist import (
    WatchlistAnalyzer,
    WatchlistCollection,
)


def test_empty_collection():

    analyzer = WatchlistAnalyzer()

    result = analyzer.analyze(
        WatchlistCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = WatchlistAnalyzer()

    result = analyzer.analyze(
        WatchlistCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["watchlist_type"]

    assert isinstance(distribution, dict)