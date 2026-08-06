"""
Tests for FeedStatistics.
"""

from ogs.market_data.feed import (
    FeedCollection,
    FeedFactory,
    FeedStatistics,
)


def create_statistics():

    collection = FeedCollection(
        [
            FeedFactory.live("Live"),
            FeedFactory.historical("History"),
            FeedFactory.simulated("Simulation"),
        ]
    )

    return FeedStatistics(collection)


def test_count():

    statistics = create_statistics()

    assert statistics.count == 3


def test_connected_count():

    statistics = create_statistics()

    assert statistics.connected_count == 3


def test_average_latency():

    statistics = create_statistics()

    assert statistics.average_latency == 0.0


def test_total_updates():

    statistics = create_statistics()

    assert statistics.total_updates == 0


def test_distribution():

    statistics = create_statistics()

    distribution = (
        statistics.feed_distribution
    )

    assert distribution["LIVE"] == 1
    assert distribution["HISTORICAL"] == 1
    assert distribution["SIMULATED"] == 1


def test_summary():

    statistics = create_statistics()

    summary = statistics.summary()

    assert summary["count"] == 3
    assert "feed_distribution" in summary