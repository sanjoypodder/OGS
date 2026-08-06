"""
===========================================================

OGS Smart Money AI

Displacement Factory

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.order_block.displacement import (
    Displacement,
    DisplacementDirection,
)

from .candle_factory import make_candle


def make_displacement(
    direction: DisplacementDirection = DisplacementDirection.BULLISH,
) -> Displacement:
    """
    Create a displacement object for testing.
    """

    return Displacement(
        candle=make_candle(),
        direction=direction,
    )