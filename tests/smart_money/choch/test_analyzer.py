"""
===========================================================

OGS Smart Money AI

CHOCH Analyzer Tests

===========================================================
"""

from datetime import UTC, datetime

from ogs.market import (
    Candle,
    Price,
    Symbol,
    Timeframe,
)
from ogs.smart_money.bos import (
    BOS,
    BOSSeries,
    BOSType,
)
from ogs.smart_money.choch import (
    CHOCHAnalyzer,
    CHOCHType,
)
from ogs.smart_money.swing import (
    Swing,
    SwingType,
)


def create_candle(close: float) -> Candle:

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


def create_bullish_bos() -> BOS:

    swing = Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )

    return BOS(
        candle=create_candle(110),
        broken_swing=swing,
        bos_type=BOSType.BULLISH,
    )


def create_bearish_bos() -> BOS:

    swing = Swing(
        index=1,
        candle=create_candle(95),
        swing_type=SwingType.LOW,
    )

    return BOS(
        candle=create_candle(90),
        broken_swing=swing,
        bos_type=BOSType.BEARISH,
    )


def test_empty():

    analyzer = CHOCHAnalyzer()

    result = analyzer.analyze(BOSSeries([]))

    assert len(result) == 0


def test_no_bos():

    analyzer = CHOCHAnalyzer()

    result = analyzer.analyze(BOSSeries([]))

    assert len(result) == 0


def test_bearish_to_bullish_choch():

    analyzer = CHOCHAnalyzer()

    result = analyzer.analyze(
        BOSSeries(
            [
                create_bearish_bos(),
                create_bullish_bos(),
            ]
        )
    )

    assert len(result) == 1
    assert result.first.choch_type == CHOCHType.BULLISH

def test_bullish_to_bearish_choch():

    analyzer = CHOCHAnalyzer()

    result = analyzer.analyze(
        BOSSeries(
            [
                create_bullish_bos(),
                create_bearish_bos(),
            ]
        )
    )

    assert len(result) == 1
    assert result.first.choch_type == CHOCHType.BEARISH

def test_same_direction():

    analyzer = CHOCHAnalyzer()

    result = analyzer.analyze(
        BOSSeries(
            [
                create_bullish_bos(),
                create_bullish_bos(),
            ]
        )
    )

    assert len(result) == 0

def test_multiple_reversals():

    analyzer = CHOCHAnalyzer()

    result = analyzer.analyze(
        BOSSeries(
            [
                create_bearish_bos(),
                create_bullish_bos(),
                create_bearish_bos(),
                create_bullish_bos(),
            ]
        )
    )

    assert len(result) == 3