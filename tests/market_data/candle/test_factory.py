"""
Tests for Candle factory.
"""

from datetime import datetime

import pytest

from ogs.market_data.candle import (
    Candle,
    CandleFactory,
)


def test_factory_create():

    candle = CandleFactory.create(
        symbol="XAUUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=100,
        high=120,
        low=90,
        close=110,
        volume=100,
    )

    assert isinstance(candle, Candle)


def test_factory_values():

    candle = CandleFactory.create(
        symbol="BTCUSD",
        timeframe="M5",
        timestamp=datetime.now(),
        open=10,
        high=15,
        low=8,
        close=12,
    )

    assert candle.symbol == "BTCUSD"
    assert candle.timeframe == "M5"
    assert candle.open == 10
    assert candle.close == 12


def test_factory_invalid_high_low():

    with pytest.raises(ValueError):

        CandleFactory.create(
            symbol="BTCUSD",
            timeframe="M5",
            timestamp=datetime.now(),
            open=10,
            high=5,
            low=8,
            close=9,
        )


def test_factory_invalid_open():

    with pytest.raises(ValueError):

        CandleFactory.create(
            symbol="BTCUSD",
            timeframe="M5",
            timestamp=datetime.now(),
            open=20,
            high=15,
            low=8,
            close=10,
        )


def test_factory_invalid_close():

    with pytest.raises(ValueError):

        CandleFactory.create(
            symbol="BTCUSD",
            timeframe="M5",
            timestamp=datetime.now(),
            open=10,
            high=15,
            low=8,
            close=20,
        )


def test_factory_negative_volume():

    with pytest.raises(ValueError):

        CandleFactory.create(
            symbol="BTCUSD",
            timeframe="M5",
            timestamp=datetime.now(),
            open=10,
            high=15,
            low=8,
            close=12,
            volume=-10,
        )