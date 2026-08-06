"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.smart_money.liquidity.equal_lows import EqualLow

from .enums import SellSideLiquidityType


@dataclass(frozen=True, slots=True)
class SellSideLiquidity:
    """
    Represents a Sell-Side Liquidity pool.

    Created from a confirmed Equal Low.
    """

    equal_low: EqualLow

    liquidity_type: SellSideLiquidityType

    @property
    def zone_price(self):
        return self.equal_low.zone_price

    @property
    def first_swing(self):
        return self.equal_low.first_swing

    @property
    def second_swing(self):
        return self.equal_low.second_swing

    @property
    def timestamp(self):
        return self.equal_low.timestamp

    def __str__(self):

        return (
            f"{self.liquidity_type.value} "
            f"Sell Side Liquidity @ {self.zone_price}"
        )