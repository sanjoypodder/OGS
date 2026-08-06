"""
Tests for SubscriptionAnalyzer basic functionality.
"""

from ogs.market_data.subscription import (
    SubscriptionAnalyzer,
    SubscriptionCollection,
    SubscriptionFactory,
)


def create_analyzer():

    collection = SubscriptionCollection(
        [
            SubscriptionFactory.live("Live"),
            SubscriptionFactory.historical("History"),
            SubscriptionFactory.simulated("Simulation"),
        ]
    )

    return SubscriptionAnalyzer(collection)


def test_summary():

    analyzer = create_analyzer()

    summary = analyzer.summary()

    assert summary["count"] == 3
    assert summary["active"] == 3


def test_activity_analysis():

    analyzer = create_analyzer()

    result = analyzer.activity_analysis()

    assert result["active"] == 3
    assert result["inactive"] == 0
    assert result["total"] == 3


def test_distribution_analysis():

    analyzer = create_analyzer()

    result = analyzer.distribution_analysis()

    assert "type_distribution" in result
    assert "provider_distribution" in result


def test_analyze():

    analyzer = create_analyzer()

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result
    assert "activity" in result
    assert "distribution" in result