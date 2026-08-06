"""
Tests for Feed domain.
"""

from ogs.market_data.feed import (
    Feed,
    FeedStatus,
    FeedType,
)


def test_feed_creation():

    feed = Feed(
        name="NSE Live",
        feed_type=FeedType.LIVE,
        status=FeedStatus.CONNECTED,
        provider="NSE",
        symbol="NIFTY",
        timeframe="1m",
        latency_ms=25.5,
        update_count=100,
        last_price=25125.30,
    )

    assert feed.name == "NSE Live"
    assert feed.feed_type == FeedType.LIVE
    assert feed.status == FeedStatus.CONNECTED
    assert feed.provider == "NSE"
    assert feed.symbol == "NIFTY"


def test_connected_property():

    feed = Feed(
        name="Feed",
        status=FeedStatus.CONNECTED,
    )

    assert feed.connected is True
    assert feed.disconnected is False


def test_disconnected_property():

    feed = Feed(
        name="Feed",
        status=FeedStatus.DISCONNECTED,
    )

    assert feed.disconnected is True


def test_healthy():

    feed = Feed(
        name="Feed",
        status=FeedStatus.CONNECTED,
        latency_ms=5,
    )

    assert feed.healthy


def test_to_dict():

    feed = Feed(name="Feed")

    data = feed.to_dict()

    assert data["name"] == "Feed"


def test_valid():

    feed = Feed(name="Feed")

    assert feed.is_valid


def test_string():

    feed = Feed(name="Feed")

    assert "Feed" in str(feed)