"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import BuySideLiquidity


class BuySideLiquidityValidator(
    BaseValidator[BuySideLiquidity]
):
    """
    Validate Buy-Side Liquidity.
    """

    def validate(
        self,
        pool: BuySideLiquidity,
    ):

        if pool is None:
            raise ValueError(
                "Buy Side Liquidity cannot be None."
            )

        if pool.equal_high is None:
            raise ValueError(
                "Equal High cannot be None."
            )