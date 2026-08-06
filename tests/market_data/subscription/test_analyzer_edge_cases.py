"""
Edge-case tests for SubscriptionAnalyzer.
"""

from ogs.market_data.subscription import (
    SubscriptionAnalyzer,
    SubscriptionCollection,
)


def test_empty_collection():

    analyzer = SubscriptionAnalyzer(
        SubscriptionCollection()
    )

    summary = analyzer.summary()

    assert summary["count"] == 0
    assert summary["active"] == 0
    assert summary["inactive"] == 0


def test_empty_analysis():

    analyzer = SubscriptionAnalyzer(
        SubscriptionCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = SubscriptionAnalyzer(
        SubscriptionCollection()
    )

    result = analyzer.distribution_analysis()

    assert result["type_distribution"] == {}
    assert result["provider_distribution"] == {}


def test_zero_active():

    analyzer = SubscriptionAnalyzer(
        SubscriptionCollection()
    )

    result = analyzer.activity_analysis()

    assert result["active"] == 0
    assert result["inactive"] == 0