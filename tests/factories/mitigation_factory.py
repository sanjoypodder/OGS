"""
===========================================================

OGS Smart Money AI

Mitigation Block Factory

===========================================================
"""

from __future__ import annotations

from ogs.market.candle import Candle
from ogs.smart_money.mitigation import (
    MitigationBlock,
    MitigationBlockDirection,
)

from .candle_factory import make_candle


def make_bullish_mitigation() -> MitigationBlock:
    candle = make_candle(
        open=105,
        high=106,
        low=100,
        close=101,
    )

    return MitigationBlock(
        candle=candle,
        direction=MitigationBlockDirection.BULLISH,
        top=106,
        bottom=100,
        midpoint=103,
        size=6,
        is_mitigated=True,
    )


def make_bearish_mitigation() -> MitigationBlock:
    candle = make_candle(
        open=100,
        high=106,
        low=99,
        close=105,
    )

    return MitigationBlock(
        candle=candle,
        direction=MitigationBlockDirection.BEARISH,
        top=106,
        bottom=99,
        midpoint=102.5,
        size=7,
        is_mitigated=True,
    )
def make_bullish_mitigation_candles() -> list[Candle]:
    return [
        make_candle(
            open=105,
            high=106,
            low=100,
            close=101,
        ),
        make_candle(
            open=106,
            high=110,
            low=105,
            close=108,
        ),
    ]


def make_bearish_mitigation_candles() -> list[Candle]:
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