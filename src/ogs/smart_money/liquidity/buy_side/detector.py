"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Detector

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseDetector

from ogs.smart_money.liquidity.equal_highs import (
    EqualHighSeries,
)

from .collection import BuySideLiquiditySeries
from .domain import BuySideLiquidity
from .enums import BuySideLiquidityType


class BuySideLiquidityDetector(
    BaseDetector[
        EqualHighSeries,
        BuySideLiquiditySeries,
    ]
):
    """
    Transform Equal Highs into Buy-Side Liquidity pools.
    """

    def detect(
        self,
        equal_highs: EqualHighSeries,
    ) -> BuySideLiquiditySeries:

        if equal_highs is None:
            return BuySideLiquiditySeries([])

        pools: list[BuySideLiquidity] = []

        for zone in equal_highs:

            pools.append(
                BuySideLiquidity(
                    equal_high=zone,
                    liquidity_type=BuySideLiquidityType.ACTIVE,
                )
            )

        return BuySideLiquiditySeries(pools)