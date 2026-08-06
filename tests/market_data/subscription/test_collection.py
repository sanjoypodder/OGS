"""
Tests for SubscriptionCollection.
"""

from ogs.market_data.subscription import (
    SubscriptionCollection,
    SubscriptionFactory,
    SubscriptionStatus,
)


def create_collection():

    return SubscriptionCollection(
        [
            SubscriptionFactory.live(
                "Live"
            ),
            SubscriptionFactory.historical(
                "History"
            ),
            SubscriptionFactory.create(
                name="Paused",
                status=SubscriptionStatus.PAUSED,
            ),
        ]
    )


def test_length():

    collection = create_collection()

    assert len(collection) == 3


def test_find():

    collection = create_collection()

    subscription = collection.find(
        "Live"
    )

    assert subscription is not None
    assert subscription.name == "Live"


def test_active():

    collection = create_collection()

    assert (
        len(collection.active()) == 2
    )


def test_inactive():

    collection = create_collection()

    assert (
        len(collection.inactive()) == 1
    )


def test_by_provider():

    collection = SubscriptionCollection(
        [
            SubscriptionFactory.create(
                name="A",
                provider="NSE",
            ),
            SubscriptionFactory.create(
                name="B",
                provider="BSE",
            ),
            SubscriptionFactory.create(
                name="C",
                provider="NSE",
            ),
        ]
    )

    assert (
        len(
            collection.by_provider(
                "NSE"
            )
        )
        == 2
    )


def test_total_active():

    collection = create_collection()

    assert (
        collection.total_active() == 2
    )


def test_to_list():

    collection = create_collection()

    assert isinstance(
        collection.to_list(),
        list,
    )