"""
===========================================================

OGS Smart Money AI

MSS Domain Tests

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
from ogs.smart_money.mss import (
    MSS,
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


def create_choch() -> CHOCH:

    return CHOCH(
        candle=create_candle(112),
        broken_bos=create_bos(),
        choch_type=CHOCHType.BULLISH,
    )


def test_create_mss():

    mss = MSS(
        candle=create_candle(118),
        triggering_choch=create_choch(),
        mss_type=MSSType.BULLISH,
    )

    assert mss.mss_type == MSSType.BULLISH


def test_timestamp():

    mss = MSS(
        candle=create_candle(118),
        triggering_choch=create_choch(),
        mss_type=MSSType.BULLISH,
    )

    assert mss.timestamp.year == 2026


def test_price():

    mss = MSS(
        candle=create_candle(118),
        triggering_choch=create_choch(),
        mss_type=MSSType.BULLISH,
    )

    # Price propagates from:
    # MSS -> CHOCH -> BOS -> Swing High
    assert mss.price.value == 110


def test_string():

    mss = MSS(
        candle=create_candle(118),
        triggering_choch=create_choch(),
        mss_type=MSSType.BULLISH,
    )

    assert "BULLISH" in str(mss)