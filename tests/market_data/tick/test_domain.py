"""
Tests for Tick domain model.
"""

from datetime import datetime

from ogs.market_data.tick import (
    ProviderType,
    Tick,
)


def create_tick():

    return Tick(
        symbol="EURUSD",
        timestamp=datetime(2026, 1, 1, 9, 0, 0),
        bid=1.1000,
        ask=1.1002,
        last=1.1001,
        volume=1000,
        provider=ProviderType.FYERS,
    )


def test_create_tick():

    tick = create_tick()

    assert tick.symbol == "EURUSD"


def test_spread():

    tick = create_tick()

    assert round(tick.spread, 4) == 0.0002


def test_mid_price():

    tick = create_tick()

    assert round(tick.mid_price, 4) == 1.1001


def test_buy_tick():

    tick = create_tick()

    assert tick.is_buy_tick


def test_sell_tick():

    tick = Tick(
        symbol="EURUSD",
        timestamp=datetime.now(),
        bid=100,
        ask=102,
        last=100,
        volume=10,
        provider=ProviderType.FYERS,
    )

    assert tick.is_sell_tick


def test_has_volume():

    tick = create_tick()

    assert tick.has_volume


def test_valid():

    tick = create_tick()

    assert tick.is_valid


def test_to_dict():

    tick = create_tick()

    data = tick.to_dict()

    assert data["symbol"] == "EURUSD"
    assert data["provider"] == "FYERS"


def test_str():

    tick = create_tick()

    assert "EURUSD" in str(tick)


def test_repr():

    tick = create_tick()

    assert "Tick(" in repr(tick)