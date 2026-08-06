"""
Tests for CandleAnalyzer detection methods.
"""

from datetime import datetime

from ogs.market_data.candle import (
    Candle,
    CandleAnalyzer,
    CandleSeries,
)


def candle(
    open_price,
    high,
    low,
    close,
):

    return Candle(
        symbol="BTCUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=open_price,
        high=high,
        low=low,
        close=close,
        volume=100,
    )


def build_series():

    series = CandleSeries()

    series.append(candle(100, 120, 90, 110))
    series.append(candle(110, 150, 100, 145))
    series.append(candle(145, 148, 80, 90))

    return series


def test_highest():

    analyzer = CandleAnalyzer()

    highest = analyzer.highest(build_series())

    assert highest.high == 150


def test_lowest():

    analyzer = CandleAnalyzer()

    lowest = analyzer.lowest(build_series())

    assert lowest.low == 80


def test_largest_range():

    analyzer = CandleAnalyzer()

    largest = analyzer.largest_range(build_series())

    assert largest.range == 68


def test_strongest_bullish():

    analyzer = CandleAnalyzer()

    candle = analyzer.strongest_bullish(build_series())

    assert candle.body_size == 35


def test_strongest_bearish():

    analyzer = CandleAnalyzer()

    candle = analyzer.strongest_bearish(build_series())

    assert candle.body_size == 55


def test_direction_summary():

    analyzer = CandleAnalyzer()

    summary = analyzer.direction_summary(build_series())

    assert sum(summary.values()) == 3