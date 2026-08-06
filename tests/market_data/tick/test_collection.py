"""
Tests for TickCollection.
"""

from datetime import UTC, datetime, timedelta

from ogs.market_data.tick import (
    ProviderType,
    Tick,
)
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


def test_append():

    collection = create_collection()

    assert len(collection) == 3


def test_latest():

    collection = create_collection()

    assert collection.latest().last == 1.1011


def test_oldest():

    collection = create_collection()

    assert collection.oldest().last == 1.1001


def test_highest_bid():

    collection = create_collection()

    assert collection.highest_bid().symbol == "BTCUSDT"


def test_lowest_bid():

    collection = create_collection()

    assert collection.lowest_bid().symbol == "EURUSD"


def test_highest_trade():

    collection = create_collection()

    assert collection.highest_trade().symbol == "BTCUSDT"


def test_lowest_trade():

    collection = create_collection()

    assert collection.lowest_trade().symbol == "EURUSD"


def test_find():

    collection = create_collection()

    tick = collection.find("EURUSD")

    assert tick.last == 1.1011


def test_find_case_insensitive():

    collection = create_collection()

    tick = collection.find("eurusd")

    assert tick.symbol == "EURUSD"


def test_by_provider():

    collection = create_collection()

    fyers = collection.by_provider(
        ProviderType.FYERS
    )

    assert len(fyers) == 2


def test_by_symbol():

    collection = create_collection()

    eur = collection.by_symbol("EURUSD")

    assert len(eur) == 2


def test_total_volume():

    collection = create_collection()

    assert collection.total_volume() == 302


def test_average_spread():

    collection = create_collection()

    assert collection.average_spread() > 0


def test_symbols():

    collection = create_collection()

    assert collection.symbols() == [
        "BTCUSDT",
        "EURUSD",
    ]


def test_providers():

    collection = create_collection()

    assert collection.providers() == [
        "BINANCE",
        "FYERS",
    ]