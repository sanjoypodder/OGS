"""
===========================================================

OGS Smart Money AI

MSS Test Factory

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.mss import (
    MSS,
    MSSType,
)

from .candle_factory import (
    make_bearish_candle,
    make_bullish_candle,
)
from .choch_factory import (
    make_bearish_choch,
    make_bullish_choch,
)


def make_bullish_mss(
    *,
    index: int = 10,
) -> MSS:
    """
    Create a Bullish MSS.
    """

    return MSS(
        candle=make_bullish_candle(index=index),
        triggering_choch=make_bullish_choch(index=index),
        mss_type=MSSType.BULLISH,
    )


def make_bearish_mss(
    *,
    index: int = 10,
) -> MSS:
    """
    Create a Bearish MSS.
    """

    return MSS(
        candle=make_bearish_candle(index=index),
        triggering_choch=make_bearish_choch(index=index),
        mss_type=MSSType.BEARISH,
    )