"""
Tests for FeedFactory.
"""

from ogs.market_data.feed import (
    Feed,
    FeedFactory,
    FeedStatus,
    FeedType,
)


def test_create():

    feed = FeedFactory.create(
        name="Feed",
        feed_type=FeedType.LIVE,
        status=FeedStatus.CONNECTED,
        provider="NSE",
        symbol="NIFTY",
        timeframe="1m",
        latency_ms=5.5,
        update_count=100,
        last_price=25000.0,
    )

    assert isinstance(feed, Feed)
    assert feed.name == "Feed"
    assert feed.provider == "NSE"
    assert feed.symbol == "NIFTY"


def test_live():

    feed = FeedFactory.live("Live")

    assert feed.feed_type == FeedType.LIVE
    assert feed.status == FeedStatus.CONNECTED


def test_historical():

    feed = FeedFactory.historical("History")

    assert feed.feed_type == FeedType.HISTORICAL
    assert feed.status == FeedStatus.CONNECTED


def test_simulated():

    feed = FeedFactory.simulated("Sim")

    assert feed.feed_type == FeedType.SIMULATED
    assert feed.status == FeedStatus.CONNECTED


def test_clone():

    feed = FeedFactory.create(
        name="Original",
        provider="NSE",
        symbol="BANKNIFTY",
        latency_ms=2.5,
    )

    clone = FeedFactory.clone(feed)

    assert clone == feed