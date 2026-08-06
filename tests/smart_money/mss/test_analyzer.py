"""
===========================================================

OGS Smart Money AI

MSS Analyzer Tests

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
    BOSType,
)
from ogs.smart_money.choch import (
    CHOCH,
    CHOCHSeries,
    CHOCHType,
)
from ogs.smart_money.mss import (
    MSSAnalyzer,
    MSSType,
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


def create_bullish_choch() -> CHOCH:

    swing = Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )

    bos = BOS(
        candle=create_candle(110),
        broken_swing=swing,
        bos_type=BOSType.BULLISH,
    )

    return CHOCH(
        candle=create_candle(112),
        broken_bos=bos,
        choch_type=CHOCHType.BULLISH,
    )


def create_bearish_choch() -> CHOCH:

    swing = Swing(
        index=0,
        candle=create_candle(95),
        swing_type=SwingType.LOW,
    )

    bos = BOS(
        candle=create_candle(90),
        broken_swing=swing,
        bos_type=BOSType.BEARISH,
    )

    return CHOCH(
        candle=create_candle(88),
        broken_bos=bos,
        choch_type=CHOCHType.BEARISH,
    )


def test_empty():

    analyzer = MSSAnalyzer()

    result = analyzer.analyze(
        CHOCHSeries([])
    )

    assert len(result) == 0


def test_no_choch():

    analyzer = MSSAnalyzer()

    result = analyzer.analyze(
        CHOCHSeries([])
    )

    assert len(result) == 0


def test_bearish_to_bullish_mss():

    analyzer = MSSAnalyzer()

    result = analyzer.analyze(
        CHOCHSeries(
            [
                create_bearish_choch(),
                create_bullish_choch(),
            ]
        )
    )

    assert len(result) == 1
    assert result.first.mss_type == MSSType.BULLISH


def test_bullish_to_bearish_mss():

    analyzer = MSSAnalyzer()

    result = analyzer.analyze(
        CHOCHSeries(
            [
                create_bullish_choch(),
                create_bearish_choch(),
            ]
        )
    )

    assert len(result) == 1
    assert result.first.mss_type == MSSType.BEARISH

def test_same_direction():

    analyzer = MSSAnalyzer()

    result = analyzer.analyze(
        CHOCHSeries(
            [
                create_bullish_choch(),
                create_bullish_choch(),
            ]
        )
    )

    assert len(result) == 0

def test_multiple_reversals():

    analyzer = MSSAnalyzer()

    result = analyzer.analyze(
        CHOCHSeries(
            [
                create_bearish_choch(),
                create_bullish_choch(),
                create_bearish_choch(),
                create_bullish_choch(),
            ]
        )
    )

    assert len(result) == 3