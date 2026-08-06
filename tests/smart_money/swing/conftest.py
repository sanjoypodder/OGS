"""
===========================================================

OGS Smart Money AI

Swing Test Fixtures

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
def sample_symbol() -> Symbol:
    return Symbol.XAUUSD


@pytest.fixture
def sample_timeframe() -> Timeframe:
    return Timeframe.M5


@pytest.fixture
def sample_candle(
    sample_symbol: Symbol,
    sample_timeframe: Timeframe,
) -> Candle:

    return Candle(
        symbol=sample_symbol,
        timeframe=sample_timeframe,
        timestamp=datetime(
            2026,
            1,
            1,
            12,
            0,
            tzinfo=UTC,
        ),
        open=Price(sample_symbol, 100),
        high=Price(sample_symbol, 110),
        low=Price(sample_symbol, 90),
        close=Price(sample_symbol, 105),
    )


@pytest.fixture
def sample_swing(
    sample_candle: Candle,
) -> Swing:

    return Swing(
        index=1,
        candle=sample_candle,
        swing_type=SwingType.HIGH,
    )


@pytest.fixture
def sample_series(
    sample_swing: Swing,
) -> SwingSeries:

    return SwingSeries(
        [sample_swing],
    )


@pytest.fixture
def candle_series(
    sample_candle: Candle,
) -> CandleSeries:

    candles = [sample_candle] * 5

    return CandleSeries(
        candles,
    )