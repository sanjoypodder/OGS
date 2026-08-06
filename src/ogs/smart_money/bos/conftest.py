"""
===========================================================

OGS Smart Money AI

BOS Test Fixtures

===========================================================
"""

from __future__ import annotations

from datetime import UTC, datetime

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
def symbol():
    return Symbol.XAUUSD


@pytest.fixture
def timeframe():
    return Timeframe.M5


@pytest.fixture
def swing_high(symbol, timeframe):

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

    return Swing(
        index=2,
        candle=candle,
        swing_type=SwingType.HIGH,
    )


@pytest.fixture
def swing_low(symbol, timeframe):

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
        high=Price(symbol, 105),
        low=Price(symbol, 90),
        close=Price(symbol, 95),
    )

    return Swing(
        index=2,
        candle=candle,
        swing_type=SwingType.LOW,
    )


@pytest.fixture
def swing_series(swing_high):

    return SwingSeries(
        [swing_high],
    )


@pytest.fixture
def candle_series(symbol, timeframe):

    candles = []

    for i in range(10):

        candles.append(
            Candle(
                symbol=symbol,
                timeframe=timeframe,
                timestamp=datetime(
                    2026,
                    1,
                    1,
                    9,
                    i * 5,
                    tzinfo=UTC,
                ),
                open=Price(symbol, 100),
                high=Price(symbol, 105),
                low=Price(symbol, 95),
                close=Price(symbol, 100),
            )
        )

    return CandleSeries(candles)