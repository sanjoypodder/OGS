"""
===========================================================

OGS Smart Money AI

Balanced Price Range Factory

===========================================================
"""

from __future__ import annotations

from .domain import BalancedPriceRange
from .enums import BalancedPriceRangeDirection
from ogs.smart_money.fair_value_gap.domain import FairValueGap


class BalancedPriceRangeFactory:
    """
    Factory for creating Balanced Price Ranges.
    """

    @staticmethod
    def create(
        bullish_gap: FairValueGap,
        bearish_gap: FairValueGap,
        direction: BalancedPriceRangeDirection,
        top: float,
        bottom: float,
        midpoint: float,
        size: float,
    ) -> BalancedPriceRange:
        """
        Create a Balanced Price Range.
        """

        return BalancedPriceRange(
            bullish_gap=bullish_gap,
            bearish_gap=bearish_gap,
            direction=direction,
            top=top,
            bottom=bottom,
            midpoint=midpoint,
            size=size,
        )