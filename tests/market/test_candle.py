from datetime import datetime
from decimal import Decimal

import pytest

from ogs.market.candle import Candle
from ogs.market.price import Price
from ogs.market.symbol import Symbol
from ogs.market.timeframe import Timeframe


def create_candle() -> Candle:
    return Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=datetime(2026, 1, 1, 12, 0),
        open=Price(Symbol.XAUUSD, 100),
        high=Price(Symbol.XAUUSD, 105),
        low=Price(Symbol.XAUUSD, 95),
        close=Price(Symbol.XAUUSD, 101),
        volume=Decimal("1000"),
    )


def test_create_candle():
    candle = create_candle()

    assert candle.symbol == Symbol.XAUUSD


def test_volume():
    candle = create_candle()

    assert candle.volume == Decimal("1000")


def test_high_validation():

    with pytest.raises(ValueError):

        Candle(
            symbol=Symbol.XAUUSD,
            timeframe=Timeframe.M5,
            timestamp=datetime.now(),
            open=Price(Symbol.XAUUSD, 100),
            high=Price(Symbol.XAUUSD, 90),
            low=Price(Symbol.XAUUSD, 95),
            close=Price(Symbol.XAUUSD, 99),
        )


def test_symbol_validation():

    with pytest.raises(ValueError):

        Candle(
            symbol=Symbol.XAUUSD,
            timeframe=Timeframe.M5,
            timestamp=datetime.now(),
            open=Price(Symbol.EURUSD, 100),
            high=Price(Symbol.XAUUSD, 105),
            low=Price(Symbol.XAUUSD, 95),
            close=Price(Symbol.XAUUSD, 100),
        )


def test_negative_volume():

    with pytest.raises(ValueError):

        Candle(
            symbol=Symbol.XAUUSD,
            timeframe=Timeframe.M5,
            timestamp=datetime.now(),
            open=Price(Symbol.XAUUSD, 100),
            high=Price(Symbol.XAUUSD, 105),
            low=Price(Symbol.XAUUSD, 95),
            close=Price(Symbol.XAUUSD, 101),
            volume=Decimal("-1"),
        )


def test_immutable():
    candle = create_candle()

    with pytest.raises(Exception):
        candle.volume = Decimal("500")


def test_timeframe():
    candle = create_candle()

    assert candle.timeframe == Timeframe.M5


def test_timestamp():
    candle = create_candle()

    assert candle.timestamp.year == 2026