"""
Tests for SubscriptionStatistics.
"""

from ogs.market_data.subscription import (
    SubscriptionCollection,
    SubscriptionFactory,
    SubscriptionStatistics,
)


def create_statistics():

    collection = SubscriptionCollection(
        [
            SubscriptionFactory.live(
                "Live"
            ),
            SubscriptionFactory.historical(
                "History"
            ),
            SubscriptionFactory.simulated(
                "Simulation"
            ),
        ]
    )

    return SubscriptionStatistics(
        collection
    )


def test_count():

    statistics = create_statistics()

    assert statistics.count == 3


def test_active_count():

    statistics = create_statistics()

    assert (
        statistics.active_count == 3
    )


def test_inactive_count():

    statistics = create_statistics()

    assert (
        statistics.inactive_count == 0
    )


def test_distribution():

    statistics = create_statistics()

    distribution = (
        statistics.type_distribution
    )

    assert distribution["LIVE"] == 1
    assert (
        distribution["HISTORICAL"]
        == 1
    )
    assert (
        distribution["SIMULATED"]
        == 1
    )


def test_provider_distribution():

    statistics = create_statistics()

    distribution = (
        statistics.provider_distribution
    )

    assert isinstance(
        distribution,
        dict,
    )


def test_summary():

    statistics = create_statistics()

    summary = statistics.summary()

    assert summary["count"] == 3
    assert summary["active"] == 3
    assert "type_distribution" in summary