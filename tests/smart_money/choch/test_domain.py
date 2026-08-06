"""
===========================================================

OGS Smart Money AI

CHOCH Domain Tests

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


def create_swing() -> Swing:

    return Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )


def create_bos() -> BOS:

    return BOS(
        candle=create_candle(110),
        broken_swing=create_swing(),
        bos_type=BOSType.BULLISH,
    )


def test_create_choch():

    choch = CHOCH(
        candle=create_candle(112),
        broken_bos=create_bos(),
        choch_type=CHOCHType.BULLISH,
    )

    assert choch.choch_type == CHOCHType.BULLISH


def test_timestamp():

    choch = CHOCH(
        candle=create_candle(112),
        broken_bos=create_bos(),
        choch_type=CHOCHType.BULLISH,
    )

    assert choch.timestamp.year == 2026


def test_price():

    choch = CHOCH(
        candle=create_candle(112),
        broken_bos=create_bos(),
        choch_type=CHOCHType.BULLISH,
    )

    # Price should come from the broken BOS
    # which itself comes from the Swing High.
    assert choch.price.value == 110


def test_string():

    choch = CHOCH(
        candle=create_candle(112),
        broken_bos=create_bos(),
        choch_type=CHOCHType.BULLISH,
    )

    assert "BULLISH" in str(choch)