"""
Edge-case tests for FeedAnalyzer.
"""

from ogs.market_data.feed import (
    FeedAnalyzer,
    FeedCollection,
)


def test_empty_collection():

    analyzer = FeedAnalyzer(
        FeedCollection()
    )

    summary = analyzer.summary()

    assert summary["count"] == 0
    assert summary["connected"] == 0


def test_empty_analysis():

    analyzer = FeedAnalyzer(
        FeedCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_empty_latency():

    analyzer = FeedAnalyzer(
        FeedCollection()
    )

    result = analyzer.latency_analysis()

    assert result["average_latency"] == 0.0
    assert result["fastest_feed"] is None
    assert result["slowest_feed"] is None


def test_zero_updates():

    analyzer = FeedAnalyzer(
        FeedCollection()
    )

    result = analyzer.performance_analysis()

    assert result["total_updates"] == 0