"""
===========================================================

OGS Smart Money AI

Smart Money Engine

===========================================================
"""

from __future__ import annotations

from ogs.market import CandleSeries

from .analysis import Analysis
from .market_structure_engine import MarketStructureEngine
from .liquidity_engine import LiquidityEngine


class SmartMoneyEngine:
    """
    Top-level Smart Money orchestration engine.
    """

    def __init__(self):

        self._market_structure = MarketStructureEngine()
        self._liquidity = LiquidityEngine()

    def analyze(
        self,
        candles: CandleSeries,
    ) -> Analysis:

        analysis = self._market_structure.analyze(candles)

        liquidity = self._liquidity.analyze(
            candles,
            analysis.swings,
        )

        return Analysis(
            swings=analysis.swings,
            bos=analysis.bos,
            choch=analysis.choch,
            mss=analysis.mss,

            equal_highs=liquidity.equal_highs,
            equal_lows=liquidity.equal_lows,

            buy_side=liquidity.buy_side,
            sell_side=liquidity.sell_side,

            sweeps=liquidity.sweeps,
        )