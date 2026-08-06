"""
===========================================================

OGS Smart Money AI

Liquidity Engine

===========================================================
"""

from __future__ import annotations

from ogs.market import CandleSeries

from ogs.smart_money.swing import SwingSeries

from ogs.smart_money.liquidity.equal_highs import (
    EqualHighDetector,
)
from ogs.smart_money.liquidity.equal_lows import (
    EqualLowDetector,
)
from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidityDetector,
)
from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidityDetector,
)
from ogs.smart_money.liquidity.sweep import (
    LiquiditySweepAnalyzer,
)

from .analysis import Analysis


class LiquidityEngine:
    """
    Orchestrates the liquidity pipeline.
    """

    def __init__(self):

        self._equal_high = EqualHighDetector()
        self._equal_low = EqualLowDetector()

        self._buy_side = BuySideLiquidityDetector()
        self._sell_side = SellSideLiquidityDetector()

        self._sweep = LiquiditySweepAnalyzer()

    def analyze(
        self,
        candles: CandleSeries,
        swings: SwingSeries,
    ) -> Analysis:

        equal_highs = self._equal_high.detect(swings)

        equal_lows = self._equal_low.detect(swings)

        buy_side = self._buy_side.detect(equal_highs)

        sell_side = self._sell_side.detect(equal_lows)

        sweeps = self._sweep.analyze(
            candles,
            buy_side,
            sell_side,
        )

        return Analysis(
            equal_highs=equal_highs,
            equal_lows=equal_lows,
            buy_side=buy_side,
            sell_side=sell_side,
            sweeps=sweeps,
        )