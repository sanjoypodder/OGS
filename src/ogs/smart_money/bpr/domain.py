"""
===========================================================

OGS Smart Money AI

Balanced Price Range Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.smart_money.fair_value_gap.domain import FairValueGap

from .enums import BalancedPriceRangeDirection


@dataclass(frozen=True, slots=True)
class BalancedPriceRange:
    """
    Represents an institutional Balanced Price Range (BPR).

    A Balanced Price Range is formed when a bullish
    Fair Value Gap overlaps with a bearish Fair Value Gap.
    """

    bullish_gap: FairValueGap

    bearish_gap: FairValueGap

    direction: BalancedPriceRangeDirection

    top: float

    bottom: float

    midpoint: float

    size: float

    @property
    def is_bullish(self) -> bool:
        """
        Returns True if bullish.
        """
        return (
            self.direction
            is BalancedPriceRangeDirection.BULLISH
        )

    @property
    def is_bearish(self) -> bool:
        """
        Returns True if bearish.
        """
        return (
            self.direction
            is BalancedPriceRangeDirection.BEARISH
        )

    @property
    def is_neutral(self) -> bool:
        """
        Returns True if neutral.
        """
        return (
            self.direction
            is BalancedPriceRangeDirection.NEUTRAL
        )