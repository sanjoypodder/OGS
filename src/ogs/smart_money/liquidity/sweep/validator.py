"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Validator

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseValidator

from .domain import LiquiditySweep


class LiquiditySweepValidator(
    BaseValidator[LiquiditySweep]
):
    """
    Validate Liquidity Sweep.
    """

    def validate(
        self,
        sweep: LiquiditySweep,
    ):

        if sweep is None:
            raise ValueError(
                "Liquidity Sweep cannot be None."
            )

        if sweep.liquidity_pool is None:
            raise ValueError(
                "Liquidity pool cannot be None."
            )