"""
Tests for FeedAnalyzer basic functionality.
"""

from ogs.market_data.feed import (
    FeedAnalyzer,
    FeedCollection,
    FeedFactory,
)


def create_analyzer():

    collection = FeedCollection(
        [
            FeedFactory.live("Live"),
            FeedFactory.historical("History"),
            FeedFactory.simulated("Simulation"),
        ]
    )

    return FeedAnalyzer(collection)


def test_summary():

    analyzer = create_analyzer()

    summary = analyzer.summary()

    assert summary["count"] == 3


def test_latency_analysis():

    analyzer = create_analyzer()

    result = analyzer.latency_analysis()

    assert "average_latency" in result
    assert "fastest_feed" in result
    assert "slowest_feed" in result


def test_connection_analysis():

    analyzer = create_analyzer()

    result = analyzer.connection_analysis()

    assert result["connected"] == 3
    assert result["total"] == 3


def test_performance_analysis():

    analyzer = create_analyzer()

    result = analyzer.performance_analysis()

    assert "feed_distribution" in result
    assert "provider_distribution" in result
    assert "total_updates" in result


def test_analyze():

    analyzer = create_analyzer()

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result