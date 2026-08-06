"""
Performance-oriented tests for FeedAnalyzer.
"""

from ogs.market_data.feed import (
    FeedAnalyzer,
    FeedCollection,
    FeedFactory,
)


def test_large_collection():

    collection = FeedCollection()

    for i in range(1000):
        collection.add(
            FeedFactory.live(
                f"Feed-{i}"
            )
        )

    analyzer = FeedAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1000


def test_large_analysis():

    collection = FeedCollection()

    for i in range(500):
        collection.add(
            FeedFactory.historical(
                f"History-{i}"
            )
        )

    analyzer = FeedAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500


def test_distribution_speed():

    collection = FeedCollection()

    for i in range(300):
        collection.add(
            FeedFactory.simulated(
                f"Sim-{i}"
            )
        )

    analyzer = FeedAnalyzer(collection)

    result = analyzer.performance_analysis()

    assert (
        result["feed_distribution"]["SIMULATED"]
        == 300
    )