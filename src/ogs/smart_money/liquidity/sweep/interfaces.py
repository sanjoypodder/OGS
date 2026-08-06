"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Interfaces

===========================================================
"""

from __future__ import annotations

from typing import Protocol

from ogs.market import CandleSeries
from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquiditySeries,
)
from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquiditySeries,
)

from .collection import LiquiditySweepSeries


class LiquiditySweepAnalyzerProtocol(
    Protocol,
):
    """
    Analyze liquidity pools against future candles.
    """

    def analyze(
        self,
        candles: CandleSeries,
        buy_side: BuySideLiquiditySeries,
        sell_side: SellSideLiquiditySeries,
    ) -> LiquiditySweepSeries:
        ...