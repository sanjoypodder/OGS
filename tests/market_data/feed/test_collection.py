"""
Tests for FeedCollection.
"""

from ogs.market_data.feed import (
    FeedCollection,
    FeedFactory,
    FeedStatus,
    FeedType,
)


def create_collection():

    return FeedCollection(
        [
            FeedFactory.create(
                name="Feed1",
                feed_type=FeedType.LIVE,
                status=FeedStatus.CONNECTED,
                provider="NSE",
                latency_ms=5,
                update_count=100,
            ),
            FeedFactory.create(
                name="Feed2",
                feed_type=FeedType.HISTORICAL,
                status=FeedStatus.CONNECTED,
                provider="BSE",
                latency_ms=15,
                update_count=200,
            ),
            FeedFactory.create(
                name="Feed3",
                feed_type=FeedType.SIMULATED,
                status=FeedStatus.DISCONNECTED,
                provider="NSE",
                latency_ms=30,
                update_count=50,
            ),
        ]
    )


def test_length():

    collection = create_collection()

    assert len(collection) == 3


def test_find():

    collection = create_collection()

    feed = collection.find("Feed1")

    assert feed is not None
    assert feed.name == "Feed1"


def test_connected():

    collection = create_collection()

    assert len(collection.connected()) == 2


def test_disconnected():

    collection = create_collection()

    assert len(collection.disconnected()) == 1


def test_by_type():

    collection = create_collection()

    feeds = collection.by_type(
        FeedType.LIVE
    )

    assert len(feeds) == 1


def test_by_provider():

    collection = create_collection()

    feeds = collection.by_provider("NSE")

    assert len(feeds) == 2


def test_fastest():

    collection = create_collection()

    assert collection.fastest().latency_ms == 5


def test_slowest():

    collection = create_collection()

    assert collection.slowest().latency_ms == 30


def test_average_latency():

    collection = create_collection()

    assert round(
        collection.average_latency(),
        2,
    ) == 16.67


def test_total_updates():

    collection = create_collection()

    assert collection.total_updates() == 350