"""
===========================================================

OGS Smart Money AI

BOS Domain Tests

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
        high=Price(symbol, max(100, close) + 5),
        low=Price(symbol, min(100, close) - 5),
        close=Price(symbol, close),
    )


def create_swing() -> Swing:

    return Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )


def test_create_bos():

    bos = BOS(
        candle=create_candle(110),
        broken_swing=create_swing(),
        bos_type=BOSType.BULLISH,
    )

    assert bos.bos_type == BOSType.BULLISH


def test_timestamp():

    bos = BOS(
        candle=create_candle(110),
        broken_swing=create_swing(),
        bos_type=BOSType.BULLISH,
    )

    assert bos.timestamp.year == 2026


def test_price():

    bos = BOS(
        candle=create_candle(110),
        broken_swing=create_swing(),
        bos_type=BOSType.BULLISH,
    )

    assert bos.price.value == 110


def test_string():

    bos = BOS(
        candle=create_candle(110),
        broken_swing=create_swing(),
        bos_type=BOSType.BULLISH,
    )

    assert "BULLISH" in str(bos)