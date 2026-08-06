"""
===========================================================

OGS Smart Money AI

Swing Analyzer Tests

===========================================================
"""

from datetime import UTC, datetime, timedelta

from ogs.market import (
    Candle,
    CandleSeries,
    Price,
    Symbol,
    Timeframe,
)
from ogs.smart_money.swing import (
    SwingAnalyzer,
    SwingType,
)


def make_candle(
    index: int,
    high: float,
    low: float,
) -> Candle:
    """
    Create a valid candle for testing.

    Open and Close are automatically adjusted so that:

        High >= Open
        High >= Close
        Low <= Open
        Low <= Close

    Therefore every generated candle is valid.
    """

    timestamp = (
        datetime(
            2026,
            1,
            1,
            9,
            0,
            tzinfo=UTC,
        )
        + timedelta(minutes=index * 5)
    )

    open_price = max(low + 1, min(high - 1, 100))
    close_price = open_price

    return Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=timestamp,
        open=Price(Symbol.XAUUSD, open_price),
        high=Price(Symbol.XAUUSD, high),
        low=Price(Symbol.XAUUSD, low),
        close=Price(Symbol.XAUUSD, close_price),
    )


def test_empty_series():

    analyzer = SwingAnalyzer()

    result = analyzer.analyze(
        CandleSeries([])
    )

    assert len(result) == 0


def test_less_than_five_candles():

    candles = [
        make_candle(i, 100 + i, 90 - i)
        for i in range(4)
    ]

    analyzer = SwingAnalyzer()

    result = analyzer.analyze(
        CandleSeries(candles)
    )

    assert len(result) == 0


def test_detect_single_swing_high():

    candles = [
        make_candle(0, 100, 90),
        make_candle(1, 101, 89),
        make_candle(2, 110, 89),
        make_candle(3, 102, 90),
        make_candle(4, 101, 91),
    ]

    analyzer = SwingAnalyzer()

    result = analyzer.analyze(
        CandleSeries(candles)
    )

    assert len(result) == 1
    assert result.first.swing_type == SwingType.HIGH


def test_detect_single_swing_low():

    candles = [
        make_candle(0, 100, 90),
        make_candle(1, 101, 89),
        make_candle(2, 101, 80),
        make_candle(3, 100, 89),
        make_candle(4, 100, 90),
    ]

    analyzer = SwingAnalyzer()

    result = analyzer.analyze(
        CandleSeries(candles)
    )

    assert len(result) == 1
    assert result.first.swing_type == SwingType.LOW


def test_no_swings():

    candles = [
        make_candle(0, 100, 90),
        make_candle(1, 101, 91),
        make_candle(2, 102, 92),
        make_candle(3, 103, 93),
        make_candle(4, 104, 94),
    ]

    analyzer = SwingAnalyzer()

    result = analyzer.analyze(
        CandleSeries(candles)
    )

    assert len(result) == 0


def test_multiple_swings():

    candles = [
        make_candle(0, 100, 90),
        make_candle(1, 101, 89),

        # Swing High
        make_candle(2, 110, 89),

        make_candle(3, 102, 90),
        make_candle(4, 101, 91),

        make_candle(5, 100, 90),

        # Swing Low
        make_candle(6, 101, 80),

        make_candle(7, 100, 89),
        make_candle(8, 100, 90),
    ]

    analyzer = SwingAnalyzer()

    result = analyzer.analyze(
        CandleSeries(candles)
    )

    assert len(result) == 2
    assert result[0].swing_type == SwingType.HIGH
    assert result[1].swing_type == SwingType.LOW