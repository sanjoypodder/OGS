"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.smart_money.liquidity.equal_highs import EqualHigh

from .enums import BuySideLiquidityType


@dataclass(frozen=True, slots=True)
class BuySideLiquidity:
    """
    Represents a Buy-Side Liquidity pool.

    Created from a confirmed Equal High.
    """

    equal_high: EqualHigh

    liquidity_type: BuySideLiquidityType

    @property
    def zone_price(self):
        return self.equal_high.zone_price

    @property
    def first_swing(self):
        return self.equal_high.first_swing

    @property
    def second_swing(self):
        return self.equal_high.second_swing

    @property
    def timestamp(self):
        return self.equal_high.timestamp

    def __str__(self):

        return (
            f"{self.liquidity_type.value} "
            f"Buy Side Liquidity @ {self.zone_price}"
        )