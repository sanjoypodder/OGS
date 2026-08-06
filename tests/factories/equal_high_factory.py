"""
===========================================================

OGS Smart Money AI

Equal High Factory

===========================================================
"""

from decimal import Decimal

from .swing_factory import make_swing_high

from ogs.smart_money.liquidity.equal_highs import (
    EqualHigh,
    EqualHighType,
)


def make_equal_high():

    return EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )