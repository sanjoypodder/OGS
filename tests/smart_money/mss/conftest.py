"""
===========================================================

OGS Smart Money AI

MSS Test Fixtures

===========================================================
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

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


@pytest.fixture
def sample_mss():

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

    choch = CHOCH(
        candle=create_candle(112),
        broken_bos=bos,
        choch_type=CHOCHType.BULLISH,
    )

    return MSS(
        candle=create_candle(118),
        triggering_choch=choch,
        mss_type=MSSType.BULLISH,
    )