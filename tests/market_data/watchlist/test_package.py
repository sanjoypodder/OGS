"""
Tests for Watchlist package exports.
"""

from ogs.market_data.watchlist import (
    __version__,
    Watchlist,
    WatchlistAnalyzer,
    WatchlistCollection,
    WatchlistFactory,
    WatchlistStatistics,
    WatchlistStatus,
    WatchlistType,
    WatchlistValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Watchlist is not None
    assert WatchlistAnalyzer is not None
    assert WatchlistCollection is not None
    assert WatchlistFactory is not None
    assert WatchlistStatistics is not None
    assert WatchlistValidator is not None
    assert WatchlistType is not None
    assert WatchlistStatus is not None