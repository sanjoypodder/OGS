"""
===========================================================

OGS Smart Money AI

BOS Test Fixtures

===========================================================
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta


import pytest

from ogs.market import (
    Candle,
    CandleSeries,
    Price,
    Symbol,
    Timeframe,
)
from ogs.smart_money.swing import (
    Swing,
    SwingSeries,
    SwingType,
)


@pytest.fixture
def symbol() -> Symbol:
    return Symbol.XAUUSD


@pytest.fixture
def timeframe() -> Timeframe:
    return Timeframe.M5


@pytest.fixture
def candle_series(
    symbol: Symbol,
    timeframe: Timeframe,
) -> CandleSeries:

    candles = []

    start = datetime(
        2026,
        1,
        1,
        9,
        0,
        tzinfo=UTC,
    )

    for i in range(10):

        candles.append(
            Candle(
                symbol=symbol,
                timeframe=timeframe,
                timestamp=start + timedelta(minutes=i * 5),
                open=Price(symbol, 100),
                high=Price(symbol, 105),
                low=Price(symbol, 95),
                close=Price(symbol, 100),
            )
        )

    return CandleSeries(candles)


@pytest.fixture
def swing_series(
    symbol: Symbol,
    timeframe: Timeframe,
) -> SwingSeries:

    candle = Candle(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=datetime(
            2026,
            1,
            1,
            tzinfo=UTC,
        ),
        open=Price(symbol, 100),
        high=Price(symbol, 110),
        low=Price(symbol, 95),
        close=Price(symbol, 105),
    )

    swing = Swing(
        index=2,
        candle=candle,
        swing_type=SwingType.HIGH,
    )

    return SwingSeries([swing])


from ogs.smart_money.bos import BOS, BOSType

@pytest.fixture
def sample_bos(swing_series, candle_series):

    return BOS(
        candle=candle_series.first,
        broken_swing=swing_series.first,
        bos_type=BOSType.BULLISH,
    )