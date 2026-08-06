"""
===========================================================

OGS Smart Money AI

Candle Factory

===========================================================
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from ogs.market import (
    Candle,
    Price,
    Symbol,
    Timeframe,
)


DEFAULT_SYMBOL = Symbol.XAUUSD
DEFAULT_TIMEFRAME = Timeframe.M5
DEFAULT_START = datetime(
    2026,
    1,
    1,
    9,
    0,
    tzinfo=UTC,
)


def make_candle(
    *,
    index: int = 0,
    open: float = 100,
    high: float = 105,
    low: float = 95,
    close: float = 100,
    symbol: Symbol = DEFAULT_SYMBOL,
    timeframe: Timeframe = DEFAULT_TIMEFRAME,
) -> Candle:
    """
    Create a valid candle.
    """

    return Candle(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=DEFAULT_START + timedelta(
            minutes=index * timeframe.minutes
        ),
        open=Price(symbol, open),
        high=Price(symbol, high),
        low=Price(symbol, low),
        close=Price(symbol, close),
    )


def make_bullish_candle(
    *,
    index: int = 0,
) -> Candle:
    """
    Create a bullish candle.
    """

    return make_candle(
        index=index,
        open=100,
        high=110,
        low=95,
        close=108,
    )


def make_bearish_candle(
    *,
    index: int = 0,
) -> Candle:
    """
    Create a bearish candle.
    """

    return make_candle(
        index=index,
        open=108,
        high=110,
        low=95,
        close=98,
    )