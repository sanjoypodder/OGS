"""
Tests for Candle collection.
"""

from datetime import datetime

from ogs.market_data.candle import (
    Candle,
    CandleDirection,
    CandleSeries,
)


def create_candle(
    open_price: float,
    high: float,
    low: float,
    close: float,
) -> Candle:

    return Candle(
        symbol="XAUUSD",
        timeframe="M15",
        timestamp=datetime.now(),
        open=open_price,
        high=high,
        low=low,
        close=close,
        volume=100,
    )


def test_empty_collection():

    series = CandleSeries()

    assert len(series) == 0


def test_append():

    series = CandleSeries()

    candle = create_candle(100, 110, 90, 105)

    series.append(candle)

    assert len(series) == 1


def test_latest():

    series = CandleSeries()

    c1 = create_candle(100, 110, 90, 105)
    c2 = create_candle(110, 120, 100, 115)

    series.append(c1)
    series.append(c2)

    latest = series.latest()

    assert latest[0] == c2


def test_bullish_filter():

    series = CandleSeries()

    series.append(create_candle(100, 110, 90, 105))
    series.append(create_candle(110, 120, 90, 100))
    series.append(create_candle(100, 110, 90, 100))

    bullish = series.bullish()

    assert len(bullish) == 1
    assert bullish[0].direction is CandleDirection.BULLISH


def test_bearish_filter():

    series = CandleSeries()

    series.append(create_candle(100, 110, 90, 95))
    series.append(create_candle(100, 120, 90, 110))

    bearish = series.bearish()

    assert len(bearish) == 1


def test_doji_filter():

    series = CandleSeries()

    series.append(create_candle(100, 110, 90, 100))
    series.append(create_candle(100, 120, 90, 110))

    doji = series.doji()

    assert len(doji) == 1


def test_highest_high():

    series = CandleSeries()

    series.append(create_candle(100, 110, 90, 100))
    series.append(create_candle(100, 150, 90, 120))
    series.append(create_candle(100, 130, 90, 120))

    assert series.highest_high() == 150


def test_lowest_low():

    series = CandleSeries()

    series.append(create_candle(100, 110, 95, 100))
    series.append(create_candle(100, 120, 80, 110))
    series.append(create_candle(100, 130, 90, 120))

    assert series.lowest_low() == 80


def test_total_volume():

    series = CandleSeries()

    series.append(create_candle(100, 110, 90, 100))
    series.append(create_candle(100, 120, 90, 110))
    series.append(create_candle(100, 130, 90, 120))

    assert series.total_volume() == 300