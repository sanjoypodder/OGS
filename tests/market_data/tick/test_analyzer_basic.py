"""
Tests for TickAnalyzer basic functionality.
"""

from datetime import UTC, datetime, timedelta

from ogs.market_data.tick import (
    ProviderType,
    Tick,
)
from ogs.market_data.tick.analyzer import TickAnalyzer
from ogs.market_data.tick.collection import TickCollection


def create_collection():

    now = datetime.now(UTC)

    collection = TickCollection()

    collection.append(
        Tick(
            symbol="EURUSD",
            timestamp=now,
            bid=1.1000,
            ask=1.1002,
            last=1.1001,
            volume=100,
            provider=ProviderType.FYERS,
        )
    )

    collection.append(
        Tick(
            symbol="BTCUSDT",
            timestamp=now + timedelta(seconds=1),
            bid=100000,
            ask=100010,
            last=100005,
            volume=2,
            provider=ProviderType.BINANCE,
        )
    )

    collection.append(
        Tick(
            symbol="EURUSD",
            timestamp=now + timedelta(seconds=2),
            bid=1.1010,
            ask=1.1012,
            last=1.1011,
            volume=200,
            provider=ProviderType.FYERS,
        )
    )

    return collection


def test_analyze():

    analyzer = TickAnalyzer()

    result = analyzer.analyze(create_collection())

    assert isinstance(result, dict)
    assert result["count"] == 3


def test_statistics():

    analyzer = TickAnalyzer()

    stats = analyzer.statistics(create_collection())

    assert stats.count == 3


def test_latest():

    analyzer = TickAnalyzer()

    assert analyzer.latest(create_collection()).last == 1.1011


def test_oldest():

    analyzer = TickAnalyzer()

    assert analyzer.oldest(create_collection()).last == 1.1001


def test_highest_bid():

    analyzer = TickAnalyzer()

    assert analyzer.highest_bid(create_collection()).symbol == "BTCUSDT"


def test_lowest_bid():

    analyzer = TickAnalyzer()

    assert analyzer.lowest_bid(create_collection()).symbol == "EURUSD"


def test_highest_trade():

    analyzer = TickAnalyzer()

    assert analyzer.highest_trade(create_collection()).symbol == "BTCUSDT"


def test_lowest_trade():

    analyzer = TickAnalyzer()

    assert analyzer.lowest_trade(create_collection()).symbol == "EURUSD"


def test_summary():

    analyzer = TickAnalyzer()

    summary = analyzer.summary(create_collection())

    assert summary["count"] == 3