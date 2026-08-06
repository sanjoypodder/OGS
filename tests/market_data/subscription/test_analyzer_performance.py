"""
Performance tests for SubscriptionAnalyzer.
"""

from ogs.market_data.subscription import (
    SubscriptionAnalyzer,
    SubscriptionCollection,
    SubscriptionFactory,
)


def test_large_collection():

    collection = SubscriptionCollection()

    for i in range(1000):
        collection.add(
            SubscriptionFactory.live(
                f"Sub-{i}"
            )
        )

    analyzer = SubscriptionAnalyzer(collection)

    assert analyzer.summary()["count"] == 1000


def test_large_analysis():

    collection = SubscriptionCollection()

    for i in range(500):
        collection.add(
            SubscriptionFactory.historical(
                f"History-{i}"
            )
        )

    analyzer = SubscriptionAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500


def test_distribution_speed():

    collection = SubscriptionCollection()

    for i in range(300):
        collection.add(
            SubscriptionFactory.simulated(
                f"Simulation-{i}"
            )
        )

    analyzer = SubscriptionAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert (
        result["type_distribution"]["SIMULATED"]
        == 300
    )