"""
Tests for subscription package exports.
"""

from ogs.market_data.subscription import (
    Subscription,
    SubscriptionAnalyzer,
    SubscriptionCollection,
    SubscriptionFactory,
    SubscriptionStatistics,
    SubscriptionStatus,
    SubscriptionType,
    SubscriptionValidator,
)


def test_package_imports():

    assert Subscription is not None
    assert SubscriptionType is not None
    assert SubscriptionStatus is not None
    assert SubscriptionValidator is not None
    assert SubscriptionFactory is not None
    assert SubscriptionCollection is not None
    assert SubscriptionStatistics is not None
    assert SubscriptionAnalyzer is not None


def test_version_exists():

    import ogs.market_data.subscription as subscription

    assert hasattr(subscription, "__version__")
    assert subscription.__version__ == "0.1.0"