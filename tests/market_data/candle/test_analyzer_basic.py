"""
Tests for CandleAnalyzer basic functionality.
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


def build_series():

    series = CandleSeries()

    series.append(candle(100, 120, 90, 110))   # Bullish
    series.append(candle(110, 125, 100, 105))  # Bearish
    series.append(candle(105, 130, 100, 105))  # Doji

    return series


def test_bullish():

    analyzer = CandleAnalyzer()

    result = analyzer.bullish(build_series())

    assert len(result) == 1
    assert result[0].direction is CandleDirection.BULLISH


def test_bearish():

    analyzer = CandleAnalyzer()

    result = analyzer.bearish(build_series())

    assert len(result) == 1
    assert result[0].direction is CandleDirection.BEARISH


def test_doji():

    analyzer = CandleAnalyzer()

    result = analyzer.doji(build_series())

    assert len(result) == 1
    assert result[0].direction is CandleDirection.DOJI


def test_average_close():

    analyzer = CandleAnalyzer()

    avg = analyzer.average_close(build_series())

    assert avg == (110 + 105 + 105) / 3