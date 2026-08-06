"""
Tests for SubscriptionFactory.
"""

from ogs.market_data.subscription import (
    Subscription,
    SubscriptionFactory,
    SubscriptionStatus,
    SubscriptionType,
)


def test_create():

    subscription = SubscriptionFactory.create(
        name="Subscription",
        subscription_type=SubscriptionType.LIVE,
        status=SubscriptionStatus.ACTIVE,
        provider="NSE",
        symbol="NIFTY",
        timeframe="1m",
        active=True,
    )

    assert isinstance(subscription, Subscription)
    assert subscription.name == "Subscription"
    assert subscription.provider == "NSE"
    assert subscription.symbol == "NIFTY"


def test_live():

    subscription = SubscriptionFactory.live(
        "Live"
    )

    assert (
        subscription.subscription_type
        == SubscriptionType.LIVE
    )
    assert (
        subscription.status
        == SubscriptionStatus.ACTIVE
    )
    assert subscription.active


def test_historical():

    subscription = SubscriptionFactory.historical(
        "History"
    )

    assert (
        subscription.subscription_type
        == SubscriptionType.HISTORICAL
    )
    assert (
        subscription.status
        == SubscriptionStatus.ACTIVE
    )


def test_simulated():

    subscription = SubscriptionFactory.simulated(
        "Simulation"
    )

    assert (
        subscription.subscription_type
        == SubscriptionType.SIMULATED
    )


def test_clone():

    subscription = SubscriptionFactory.live(
        "Original"
    )

    clone = SubscriptionFactory.clone(
        subscription
    )

    assert clone == subscription
    assert clone is not subscription