"""
Tests for Subscription domain.
"""

from ogs.market_data.subscription import (
    Subscription,
    SubscriptionStatus,
    SubscriptionType,
)


def test_subscription_creation():

    subscription = Subscription(
        name="NSE Live",
        subscription_type=SubscriptionType.LIVE,
        status=SubscriptionStatus.ACTIVE,
        provider="NSE",
        symbol="NIFTY",
        timeframe="1m",
        active=True,
    )

    assert subscription.name == "NSE Live"
    assert subscription.subscription_type == SubscriptionType.LIVE
    assert subscription.status == SubscriptionStatus.ACTIVE
    assert subscription.provider == "NSE"
    assert subscription.symbol == "NIFTY"


def test_active_property():

    subscription = Subscription(
        name="Live",
        status=SubscriptionStatus.ACTIVE,
    )

    assert subscription.is_active


def test_is_valid():

    subscription = Subscription(
        name="Subscription"
    )

    assert subscription.is_valid


def test_to_dict():

    subscription = Subscription(
        name="Subscription"
    )

    data = subscription.to_dict()

    assert data["name"] == "Subscription"
    assert data["subscription_type"] == "UNKNOWN"
    assert data["status"] == "UNKNOWN"


def test_string():

    subscription = Subscription(
        name="Subscription"
    )

    assert "Subscription" in str(subscription)