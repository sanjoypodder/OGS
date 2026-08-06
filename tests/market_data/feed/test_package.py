"""
Tests for feed package exports.
"""

from ogs.market_data.feed import (
    Feed,
    FeedAnalyzer,
    FeedCollection,
    FeedFactory,
    FeedStatistics,
    FeedStatus,
    FeedType,
    FeedValidator,
)


def test_package_imports():

    assert Feed is not None
    assert FeedType is not None
    assert FeedStatus is not None
    assert FeedValidator is not None
    assert FeedFactory is not None
    assert FeedCollection is not None
    assert FeedStatistics is not None
    assert FeedAnalyzer is not None


def test_version_exists():

    import ogs.market_data.feed as feed

    assert hasattr(feed, "__version__")
    assert feed.__version__ == "0.1.0"