"""
Tests for TickFactory.
"""

from datetime import datetime

from ogs.market_data.tick import (
    ProviderType,
)
from ogs.market_data.tick.factory import TickFactory


def test_create():

    tick = TickFactory.create(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=1.1000,
        ask=1.1002,
        last=1.1001,
        volume=100,
        provider=ProviderType.FYERS,
    )

    assert tick.symbol == "EURUSD"


def test_symbol_uppercase():

    tick = TickFactory.create(
        symbol="eurusd",
        timestamp=datetime.now(),
        bid=1,
        ask=2,
        last=1.5,
        volume=10,
    )

    assert tick.symbol == "EURUSD"


def test_from_bid_ask():

    tick = TickFactory.from_bid_ask(
        symbol="EURUSD",
        bid=1.1000,
        ask=1.1002,
    )

    assert tick.bid == 1.1000
    assert tick.ask == 1.1002
    assert tick.last == 1.1001


def test_from_trade():

    tick = TickFactory.from_trade(
        symbol="BTCUSDT",
        price=100000,
        volume=2,
    )

    assert tick.bid == 100000
    assert tick.ask == 100000
    assert tick.last == 100000
    assert tick.volume == 2


def test_simulated():

    tick = TickFactory.simulated(
        symbol="ETHUSDT",
        price=3500,
    )

    assert tick.provider == ProviderType.SIMULATION


def test_clone():

    original = TickFactory.create(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=1,
        ask=2,
        last=1.5,
        volume=10,
        provider=ProviderType.FYERS,
    )

    cloned = TickFactory.clone(original)

    assert cloned == original
    assert cloned is not original


def test_invalid_tick():

    try:

        TickFactory.create(
            symbol="",
            timestamp=datetime.now(),
            bid=-1,
            ask=-1,
            last=-1,
            volume=-1,
        )

        assert False

    except ValueError:

        assert True