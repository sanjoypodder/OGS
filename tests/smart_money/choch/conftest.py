"""
===========================================================

OGS Smart Money AI

CHOCH Test Fixtures

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
from ogs.smart_money.swing import (
    Swing,
    SwingType,
)


@pytest.fixture
def symbol():
    return Symbol.XAUUSD


@pytest.fixture
def timeframe():
    return Timeframe.M5


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
def sample_swing():

    return Swing(
        index=0,
        candle=create_candle(105),
        swing_type=SwingType.HIGH,
    )


@pytest.fixture
def sample_bos(sample_swing):

    return BOS(
        candle=create_candle(110),
        broken_swing=sample_swing,
        bos_type=BOSType.BULLISH,
    )


@pytest.fixture
def sample_choch(sample_bos):

    return CHOCH(
        candle=create_candle(112),
        broken_bos=sample_bos,
        choch_type=CHOCHType.BULLISH,
    )