"""
Tests for FeedAnalyzer detection logic.
"""

from ogs.market_data.feed import (
    FeedAnalyzer,
    FeedCollection,
    FeedFactory,
    FeedStatus,
)


def test_detect_disconnected_feed():

    collection = FeedCollection(
        [
            FeedFactory.live("Live"),
            FeedFactory.create(
                name="Offline",
                status=FeedStatus.DISCONNECTED,
            ),
        ]
    )

    analyzer = FeedAnalyzer(collection)

    result = analyzer.connection_analysis()

    assert result["connected"] == 1


def test_distribution():

    collection = FeedCollection(
        [
            FeedFactory.live("L1"),
            FeedFactory.live("L2"),
            FeedFactory.simulated("S1"),
        ]
    )

    analyzer = FeedAnalyzer(collection)

    distribution = analyzer.performance_analysis()

    assert (
        distribution["feed_distribution"]["LIVE"]
        == 2
    )

    assert (
        distribution["feed_distribution"]["SIMULATED"]
        == 1
    )


def test_analyze_sections():

    analyzer = FeedAnalyzer(
        FeedCollection()
    )

    result = analyzer.analyze()

    assert "summary" in result
    assert "latency" in result
    assert "connection" in result
    assert "performance" in result