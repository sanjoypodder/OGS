"""
===========================================================

OGS Smart Money AI

CHOCH Factory

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.choch import (
    CHOCH,
    CHOCHType,
)

from .bos_factory import (
    make_bearish_bos,
    make_bullish_bos,
)
from .candle_factory import make_candle


def make_bullish_choch(
    *,
    index: int = 4,
) -> CHOCH:
    """
    Create a Bullish CHOCH.
    """

    return CHOCH(
        candle=make_candle(
            index=index,
            open=112,
            high=120,
            low=110,
            close=118,
        ),
        broken_bos=make_bullish_bos(index=index),
        choch_type=CHOCHType.BULLISH,
    )


def make_bearish_choch(
    *,
    index: int = 4,
) -> CHOCH:
    """
    Create a Bearish CHOCH.
    """

    return CHOCH(
        candle=make_candle(
            index=index,
            open=88,
            high=90,
            low=80,
            close=82,
        ),
        broken_bos=make_bearish_bos(index=index),
        choch_type=CHOCHType.BEARISH,
    )