"""
Tests for TickStatistics.
"""

from datetime import UTC, datetime

from ogs.market_data.tick import (
    ProviderType,
    Tick,
)
from ogs.market_data.tick.collection import TickCollection
from ogs.market_data.tick.statistics import TickStatistics


def create_statistics():

    collection = TickCollection()

    collection.append(
        Tick(
            symbol="EURUSD",
            timestamp=datetime.now(UTC),
            bid=1.1000,
            ask=1.1002,
            last=1.1001,
            volume=100,
            provider=ProviderType.FYERS,
        )
    )

    collection.append(
        Tick(
            symbol="EURUSD",
            timestamp=datetime.now(UTC),
            bid=1.1010,
            ask=1.1012,
            last=1.1011,
            volume=200,
            provider=ProviderType.FYERS,
        )
    )

    return TickStatistics(collection)


def test_count():

    stats = create_statistics()

    assert stats.count == 2


def test_average_bid():

    stats = create_statistics()

    assert round(stats.average_bid, 4) == 1.1005


def test_average_ask():

    stats = create_statistics()

    assert round(stats.average_ask, 4) == 1.1007


def test_average_last():

    stats = create_statistics()

    assert round(stats.average_last, 4) == 1.1006


def test_total_volume():

    stats = create_statistics()

    assert stats.total_volume == 300


def test_buy_ticks():

    stats = create_statistics()

    assert stats.buy_ticks == 2


def test_sell_ticks():

    stats = create_statistics()

    assert stats.sell_ticks == 0


def test_provider_distribution():

    stats = create_statistics()

    assert stats.provider_distribution == {
        "FYERS": 2
    }


def test_symbol_distribution():

    stats = create_statistics()

    assert stats.symbol_distribution == {
        "EURUSD": 2
    }


def test_summary():

    stats = create_statistics()

    summary = stats.summary()

    assert summary["count"] == 2
    assert summary["total_volume"] == 300