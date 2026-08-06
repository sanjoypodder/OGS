"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import SellSideLiquidity


class SellSideLiquidityValidator(
    BaseValidator[SellSideLiquidity]
):
    """
    Validate Sell-Side Liquidity.
    """

    def validate(
        self,
        pool: SellSideLiquidity,
    ):

        if pool is None:
            raise ValueError(
                "Sell Side Liquidity cannot be None."
            )

        if pool.equal_low is None:
            raise ValueError(
                "Equal Low cannot be None."
            )