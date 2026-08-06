"""
===========================================================

OGS Smart Money AI

BOS Analyzer Tests

===========================================================
"""

from datetime import UTC, datetime

from ogs.market import (
    Candle,
    CandleSeries,
    Price,
    Symbol,
    Timeframe,
)
from ogs.smart_money.bos import (
    BOSAnalyzer,
    BOSType,
)
from ogs.smart_money.swing import (
    Swing,
    SwingSeries,
    SwingType,
)


def create_candle(
    close: float,
) -> Candle:

    symbol = Symbol.XAUUSD

    return Candle(
        symbol=symbol,
        timeframe=Timeframe.M5,
        timestamp=datetime(
            2026,
            1,
            1,
            tzinfo=UTC,
        ),
        open=Price(symbol, 100),
        high=Price(symbol, max(close, 100) + 5),
        low=Price(symbol, min(close, 100) - 5),
        close=Price(symbol, close),
    )


def test_empty():

    analyzer = BOSAnalyzer()

    result = analyzer.analyze(
        (
            None,
            None,
        )
    )

    assert len(result) == 0


def test_no_swings():

    analyzer = BOSAnalyzer()

    candles = CandleSeries([])

    result = analyzer.analyze(
        (
            candles,
            SwingSeries([]),
        )
    )

    assert len(result) == 0


def test_bullish_bos():

    swing = Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )

    candles = CandleSeries(
        [
            create_candle(105),
            create_candle(111),
        ]
    )

    analyzer = BOSAnalyzer()

    result = analyzer.analyze(
        (
            candles,
            SwingSeries([swing]),
        )
    )

    assert len(result) == 1
    assert result.first.bos_type == BOSType.BULLISH
    
def test_bearish_bos():

    swing = Swing(
        index=0,
        candle=create_candle(95),
        swing_type=SwingType.LOW,
    )

    candles = CandleSeries(
        [
            create_candle(95),
            create_candle(89),
        ]
    )

    analyzer = BOSAnalyzer()

    result = analyzer.analyze(
        (
            candles,
            SwingSeries([swing]),
        )
    )

    assert len(result) == 1
    assert result.first.bos_type == BOSType.BEARISH

def test_equal_high_is_not_bos():

    swing = Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )

    candles = CandleSeries(
        [
            create_candle(105),
            create_candle(105),
        ]
    )

    analyzer = BOSAnalyzer()

    result = analyzer.analyze(
        (
            candles,
            SwingSeries([swing]),
        )
    )

    assert len(result) == 0

def test_equal_low_is_not_bos():

    swing = Swing(
        index=0,
        candle=create_candle(95),
        swing_type=SwingType.LOW,
    )

    candles = CandleSeries(
        [
            create_candle(95),
            create_candle(95),
        ]
    )

    analyzer = BOSAnalyzer()

    result = analyzer.analyze(
        (
            candles,
            SwingSeries([swing]),
        )
    )

    assert len(result) == 0

def test_first_break_only():

    swing = Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )

    candles = CandleSeries(
        [
            create_candle(105),
            create_candle(111),
            create_candle(120),
            create_candle(130),
        ]
    )

    analyzer = BOSAnalyzer()

    result = analyzer.analyze(
        (
            candles,
            SwingSeries([swing]),
        )
    )

    assert len(result) == 1