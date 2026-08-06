"""
===========================================================

OGS Smart Money AI

Breaker Block Factory

===========================================================
"""

from __future__ import annotations

from ogs.market.candle import Candle
from ogs.smart_money.breaker import (
    BreakerBlock,
    BreakerBlockDirection,
)

from .candle_factory import make_candle


def make_bullish_breaker() -> BreakerBlock:
    candle = make_candle(
        open=105,
        high=106,
        low=100,
        close=101,
    )

    return BreakerBlock(
        candle=candle,
        direction=BreakerBlockDirection.BULLISH,
        top=106,
        bottom=100,
        midpoint=103,
        size=6,
    )


def make_bearish_breaker() -> BreakerBlock:
    candle = make_candle(
        open=100,
        high=106,
        low=99,
        close=105,
    )

    return BreakerBlock(
        candle=candle,
        direction=BreakerBlockDirection.BEARISH,
        top=106,
        bottom=99,
        midpoint=102.5,
        size=7,
    )


def make_bullish_breaker_candles() -> list[Candle]:
    return [
        make_candle(
            open=105,
            high=106,
            low=100,
            close=101,
        ),
        make_candle(
            open=102,
            high=110,
            low=101,
            close=108,
        ),
    ]


def make_bearish_breaker_candles() -> list[Candle]:
    return [
        make_candle(
            open=100,
            high=106,
            low=99,
            close=105,
        ),
        make_candle(
            open=104,
            high=105,
            low=95,
            close=97,
        ),
    ]