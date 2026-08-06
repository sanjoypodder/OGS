"""
Tests for SubscriptionAnalyzer detection.
"""

from ogs.market_data.subscription import (
    SubscriptionAnalyzer,
    SubscriptionCollection,
    SubscriptionFactory,
    SubscriptionStatus,
)


def test_detect_inactive_subscription():

    collection = SubscriptionCollection(
        [
            SubscriptionFactory.live("Live"),
            SubscriptionFactory.create(
                name="Paused",
                status=SubscriptionStatus.PAUSED,
            ),
        ]
    )

    analyzer = SubscriptionAnalyzer(collection)

    result = analyzer.activity_analysis()

    assert result["active"] == 1
    assert result["inactive"] == 1


def test_type_distribution():

    collection = SubscriptionCollection(
        [
            SubscriptionFactory.live("L1"),
            SubscriptionFactory.live("L2"),
            SubscriptionFactory.simulated("S1"),
        ]
    )

    analyzer = SubscriptionAnalyzer(collection)

    result = analyzer.distribution_analysis()

    assert (
        result["type_distribution"]["LIVE"]
        == 2
    )

    assert (
        result["type_distribution"]["SIMULATED"]
        == 1
    )


def test_complete_analysis():

    analyzer = SubscriptionAnalyzer(
        SubscriptionCollection()
    )

    result = analyzer.analyze()

    assert "summary" in result
    assert "activity" in result
    assert "distribution" in result