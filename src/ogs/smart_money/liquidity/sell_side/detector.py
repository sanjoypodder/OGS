"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Detector

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseDetector

from ogs.smart_money.liquidity.equal_lows import (
    EqualLowSeries,
)

from .collection import SellSideLiquiditySeries
from .domain import SellSideLiquidity
from .enums import SellSideLiquidityType


class SellSideLiquidityDetector(
    BaseDetector[
        EqualLowSeries,
        SellSideLiquiditySeries,
    ]
):
    """
    Transform Equal Lows into Sell-Side Liquidity pools.
    """

    def detect(
        self,
        equal_lows: EqualLowSeries,
    ) -> SellSideLiquiditySeries:

        if equal_lows is None:
            return SellSideLiquiditySeries([])

        pools: list[SellSideLiquidity] = []

        for zone in equal_lows:

            pools.append(
                SellSideLiquidity(
                    equal_low=zone,
                    liquidity_type=SellSideLiquidityType.ACTIVE,
                )
            )

        return SellSideLiquiditySeries(pools)