"""
Tests for SubscriptionValidator.
"""

import pytest

from ogs.market_data.subscription import (
    Subscription,
    SubscriptionFactory,
    SubscriptionType,
    SubscriptionValidator,
)


validator = SubscriptionValidator()


def test_valid_subscription():

    subscription = SubscriptionFactory.live(
        "Live Subscription"
    )

    validator.validate(subscription)


def test_empty_name():

    with pytest.raises(ValueError):

        validator.validate(
            Subscription(name="")
        )


def test_invalid_type():

    with pytest.raises(ValueError):

        validator.validate(
            Subscription(
                name="Subscription",
                subscription_type="LIVE",
            )
        )


def test_invalid_status():

    with pytest.raises(ValueError):

        validator.validate(
            Subscription(
                name="Subscription",
                status="ACTIVE",
            )
        )


def test_invalid_object():

    with pytest.raises(TypeError):

        validator.validate("Subscription")


def test_callable():

    subscription = SubscriptionFactory.live(
        "Subscription"
    )

    validator(subscription)