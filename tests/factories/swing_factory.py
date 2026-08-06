"""
===========================================================

OGS Smart Money AI

Swing Factory

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.swing import (
    Swing,
    SwingType,
)

from .candle_factory import make_candle


def make_swing_high(
    *,
    index: int = 2,
) -> Swing:
    """
    Create a Swing High.
    """

    candle = make_candle(
        index=index,
        open=100,
        high=110,
        low=95,
        close=105,
    )

    return Swing(
        index=index,
        candle=candle,
        swing_type=SwingType.HIGH,
    )


def make_swing_low(
    *,
    index: int = 2,
) -> Swing:
    """
    Create a Swing Low.
    """

    candle = make_candle(
        index=index,
        open=100,
        high=105,
        low=90,
        close=95,
    )

    return Swing(
        index=index,
        candle=candle,
        swing_type=SwingType.LOW,
    )