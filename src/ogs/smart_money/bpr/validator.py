"""
===========================================================

OGS Smart Money AI

Balanced Price Range Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import BalancedPriceRange


class BalancedPriceRangeValidator(
    BaseValidator[BalancedPriceRange],
):
    """
    Validate Balanced Price Ranges.
    """

    def validate(
        self,
        bpr: BalancedPriceRange,
    ) -> bool:

        if bpr is None:
            return False

        if bpr.bullish_gap is None:
            return False

        if bpr.bearish_gap is None:
            return False

        if bpr.direction is None:
            return False

        if bpr.top <= bpr.bottom:
            return False

        if bpr.size <= 0:
            return False

        return True