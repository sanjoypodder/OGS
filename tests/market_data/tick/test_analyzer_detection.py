"""
Tests for TickAnalyzer detection methods.
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


def test_find():

    analyzer = TickAnalyzer()

    tick = analyzer.find(
        create_collection(),
        "EURUSD",
    )

    assert tick.last == 1.1011


def test_largest_spread():

    analyzer = TickAnalyzer()

    tick = analyzer.largest_spread(
        create_collection()
    )

    assert tick is not None


def test_smallest_spread():

    analyzer = TickAnalyzer()

    tick = analyzer.smallest_spread(
        create_collection()
    )

    assert tick is not None


def test_provider_analysis():

    analyzer = TickAnalyzer()

    result = analyzer.provider_analysis(
        create_collection()
    )

    assert result["FYERS"] == 2
    assert result["BINANCE"] == 1


def test_symbol_analysis():

    analyzer = TickAnalyzer()

    result = analyzer.symbol_analysis(
        create_collection()
    )

    assert result["EURUSD"] == 2
    assert result["BTCUSDT"] == 1


def test_volume_analysis():

    analyzer = TickAnalyzer()

    result = analyzer.volume_analysis(
        create_collection()
    )

    assert result["total_volume"] == 302


def test_price_distribution():

    analyzer = TickAnalyzer()

    result = analyzer.price_distribution(
        create_collection()
    )

    assert result["maximum"] == 100005
    assert result["minimum"] == 1.1001


def test_spread_analysis():

    analyzer = TickAnalyzer()

    result = analyzer.spread_analysis(
        create_collection()
    )

    assert result["average_spread"] > 0