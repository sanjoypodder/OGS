"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.smart_money.liquidity.equal_lows import (
    EqualLowSeries,
)

from .collection import SellSideLiquiditySeries


class SellSideLiquidityDetectorProtocol(
    Protocol,
):

    def detect(
        self,
        equal_lows: EqualLowSeries,
    ) -> SellSideLiquiditySeries:
        ...