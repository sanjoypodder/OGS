"""
===========================================================

OGS Smart Money AI

Rejection Block Factory

===========================================================
"""

from __future__ import annotations

from ogs.market.candle import Candle
from ogs.smart_money.rejection import (
    RejectionBlock,
    RejectionBlockDirection,
)

from .candle_factory import make_candle


def make_bullish_rejection() -> RejectionBlock:
    candle = make_candle(
        open=104,
        high=106,
        low=98,
        close=105,
    )

    return RejectionBlock(
        candle=candle,
        direction=RejectionBlockDirection.BULLISH,
        top=106,
        bottom=98,
        midpoint=102,
        size=8,
        is_confirmed=True,
    )


def make_bearish_rejection() -> RejectionBlock:
    candle = make_candle(
        open=102,
        high=110,
        low=101,
        close=103,
    )

    return RejectionBlock(
        candle=candle,
        direction=RejectionBlockDirection.BEARISH,
        top=110,
        bottom=101,
        midpoint=105.5,
        size=9,
        is_confirmed=True,
    )


def make_bullish_rejection_candles() -> list[Candle]:
    return [
        make_candle(
            open=104,
            high=106,
            low=98,
            close=105,
        ),
        make_candle(
            open=106,
            high=112,
            low=105,
            close=110,
        ),
    ]


def make_bearish_rejection_candles() -> list[Candle]:
    return [
        make_candle(
            open=102,
            high=110,
            low=101,
            close=103,
        ),
        make_candle(
            open=100,
            high=101,
            low=95,
            close=98,
        ),
    ]