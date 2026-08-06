"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.smart_money.liquidity.equal_highs import (
    EqualHighSeries,
)

from .collection import BuySideLiquiditySeries


class BuySideLiquidityDetectorProtocol(
    Protocol,
):

    def detect(
        self,
        equal_highs: EqualHighSeries,
    ) -> BuySideLiquiditySeries:
        ...