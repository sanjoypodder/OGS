"""
Tests for Candle domain.
"""

from datetime import datetime

from ogs.market_data.candle import (
    Candle,
    CandleDirection,
)


def test_create_candle():

    candle = Candle(
        symbol="XAUUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=100.0,
        high=110.0,
        low=95.0,
        close=108.0,
        volume=1000,
    )

    assert candle.symbol == "XAUUSD"
    assert candle.timeframe == "H1"


def test_bullish_direction():

    candle = Candle(
        symbol="BTCUSD",
        timeframe="M15",
        timestamp=datetime.now(),
        open=10,
        high=20,
        low=8,
        close=18,
    )

    assert candle.direction == CandleDirection.BULLISH
    assert candle.is_bullish
    assert not candle.is_bearish
    assert not candle.is_doji


def test_bearish_direction():

    candle = Candle(
        symbol="BTCUSD",
        timeframe="M15",
        timestamp=datetime.now(),
        open=20,
        high=25,
        low=10,
        close=12,
    )

    assert candle.direction == CandleDirection.BEARISH
    assert candle.is_bearish


def test_doji_direction():

    candle = Candle(
        symbol="BTCUSD",
        timeframe="M15",
        timestamp=datetime.now(),
        open=15,
        high=20,
        low=10,
        close=15,
    )

    assert candle.direction == CandleDirection.DOJI
    assert candle.is_doji


def test_body_size():

    candle = Candle(
        symbol="EURUSD",
        timeframe="H4",
        timestamp=datetime.now(),
        open=100,
        high=120,
        low=90,
        close=110,
    )

    assert candle.body_size == 10


def test_range():

    candle = Candle(
        symbol="EURUSD",
        timeframe="H4",
        timestamp=datetime.now(),
        open=100,
        high=130,
        low=90,
        close=110,
    )

    assert candle.range == 40


def test_upper_lower_wick():

    candle = Candle(
        symbol="EURUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=100,
        high=120,
        low=90,
        close=110,
    )

    assert candle.upper_wick == 10
    assert candle.lower_wick == 10


def test_midpoint():

    candle = Candle(
        symbol="EURUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=100,
        high=120,
        low=80,
        close=110,
    )

    assert candle.midpoint == 100


def test_typical_price():

    candle = Candle(
        symbol="EURUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=100,
        high=120,
        low=80,
        close=100,
    )

    assert candle.typical_price == 100


def test_weighted_price():

    candle = Candle(
        symbol="EURUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=100,
        high=120,
        low=80,
        close=100,
    )

    assert candle.weighted_price == 100