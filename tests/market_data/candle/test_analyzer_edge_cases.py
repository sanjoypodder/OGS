"""
Tests for CandleAnalyzer edge cases.
"""

from datetime import datetime

from ogs.market_data.candle import (
    Candle,
    CandleAnalyzer,
    CandleDirection,
    CandleSeries,
)


def candle(
    open_price,
    high,
    low,
    close,
):

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


def test_empty_series():

    analyzer = CandleAnalyzer()

    series = CandleSeries()

    assert analyzer.highest(series) is None
    assert analyzer.lowest(series) is None
    assert analyzer.largest_range(series) is None
    assert analyzer.strongest_bullish(series) is None
    assert analyzer.strongest_bearish(series) is None
    assert analyzer.average_close(series) == 0.0


def test_single_candle():

    analyzer = CandleAnalyzer()

    series = CandleSeries()

    c = candle(100, 120, 90, 110)

    series.append(c)

    assert analyzer.highest(series) == c
    assert analyzer.lowest(series) == c
    assert analyzer.largest_range(series) == c


def test_all_bullish():

    analyzer = CandleAnalyzer()

    series = CandleSeries()

    series.append(candle(100, 120, 90, 110))
    series.append(candle(110, 130, 100, 125))

    summary = analyzer.direction_summary(series)

    assert summary[CandleDirection.BULLISH] == 2
    assert summary[CandleDirection.BEARISH] == 0
    assert summary[CandleDirection.DOJI] == 0


def test_all_bearish():

    analyzer = CandleAnalyzer()

    series = CandleSeries()

    series.append(candle(120, 130, 100, 110))
    series.append(candle(110, 120, 90, 95))

    summary = analyzer.direction_summary(series)

    assert summary[CandleDirection.BEARISH] == 2


def test_all_doji():

    analyzer = CandleAnalyzer()

    series = CandleSeries()

    series.append(candle(100, 120, 90, 100))
    series.append(candle(110, 130, 100, 110))

    summary = analyzer.direction_summary(series)

    assert summary[CandleDirection.DOJI] == 2