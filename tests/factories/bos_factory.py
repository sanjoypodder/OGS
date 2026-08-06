"""
===========================================================

OGS Smart Money AI

BOS Factory

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.bos import (
    BOS,
    BOSType,
)

from .candle_factory import make_candle
from .swing_factory import (
    make_swing_high,
    make_swing_low,
)


def make_bullish_bos(
    *,
    index: int = 3,
) -> BOS:
    """
    Create a Bullish BOS.
    """

    return BOS(
        candle=make_candle(
            index=index,
            open=106,
            high=115,
            low=105,
            close=112,
        ),
        broken_swing=make_swing_high(index=index),
        bos_type=BOSType.BULLISH,
    )


def make_bearish_bos(
    *,
    index: int = 3,
) -> BOS:
    """
    Create a Bearish BOS.
    """

    return BOS(
        candle=make_candle(
            index=index,
            open=94,
            high=95,
            low=85,
            close=88,
        ),
        broken_swing=make_swing_low(index=index),
        bos_type=BOSType.BEARISH,
    )