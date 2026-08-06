"""
===========================================================

OGS Smart Money AI

Market Structure Test Fixtures

===========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

import pytest

from ogs.market import Candle


@pytest.fixture
def candle_factory():
    """
    Factory for creating Candle objects for tests.
    """

    def _create(
        *,
        symbol: str = "BTCUSD",
        timestamp: datetime | None = None,
        open: float = 100.0,
        high: float = 105.0,
        low: float = 95.0,
        close: float = 102.0,
        volume: float = 1000.0,
    ) -> Candle:

        return Candle(
            symbol=symbol,
            timestamp=timestamp or datetime(2025, 1, 1),
            open=open,
            high=high,
            low=low,
            close=close,
            volume=volume,
        )

    return _create


@pytest.fixture
def sample_candle(candle_factory):
    """
    Single sample candle.
    """
    return candle_factory()


@pytest.fixture
def candle_series(candle_factory):
    """
    Generate a simple candle series.
    """

    candles = []

    start = datetime(2025, 1, 1)

    for i in range(20):

        candles.append(

            candle_factory(

                timestamp=start + timedelta(minutes=i),

                open=100 + i,

                high=105 + i,

                low=95 + i,

                close=102 + i,

                volume=1000 + i,

            )

        )

    return candles


@pytest.fixture
def pivot_high_series(candle_factory):
    """
    Creates one obvious pivot high.
    """

    highs = [
        100,
        105,
        110,
        130,
        110,
        105,
        100,
    ]

    candles = []

    start = datetime(2025, 1, 1)

    for i, high in enumerate(highs):

        candles.append(

            candle_factory(

                timestamp=start + timedelta(minutes=i),

                open=high - 3,

                high=high,

                low=high - 8,

                close=high - 2,

            )

        )

    return candles


@pytest.fixture
def pivot_low_series(candle_factory):
    """
    Creates one obvious pivot low.
    """

    lows = [
        100,
        95,
        90,
        70,
        90,
        95,
        100,
    ]

    candles = []

    start = datetime(2025, 1, 1)

    for i, low in enumerate(lows):

        candles.append(

            candle_factory(

                timestamp=start + timedelta(minutes=i),

                open=low + 5,

                high=low + 10,

                low=low,

                close=low + 4,

            )

        )

    return candles


@pytest.fixture
def empty_series():
    """
    Empty candle list.
    """

    return []