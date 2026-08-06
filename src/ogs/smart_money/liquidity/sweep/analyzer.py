"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market import CandleSeries
from ogs.smart_money.base import BaseAnalyzer
from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquiditySeries,
)
from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquiditySeries,
)

from .collection import LiquiditySweepSeries
from .domain import LiquiditySweep
from .enums import (
    SweepDirection,
    SweepStatus,
)


class LiquiditySweepAnalyzer(BaseAnalyzer):
    """
    Analyze liquidity sweeps.
    """

    def analyze(
        self,
        candles: CandleSeries,
        buy_side: BuySideLiquiditySeries,
        sell_side: SellSideLiquiditySeries,
    ) -> LiquiditySweepSeries:

        sweeps: list[LiquiditySweep] = []

        if candles is None:
            return LiquiditySweepSeries([])

        # -----------------------------------------
        # Buy-side sweeps
        # -----------------------------------------

        for pool in buy_side:

            zone = pool.zone_price

            for candle in candles:

                if (
                    candle.high.value > zone
                    and candle.close.value < zone
                ):

                    sweeps.append(
                        LiquiditySweep(
                            liquidity_pool=pool,
                            sweep_candle=candle,
                            direction=SweepDirection.BUY_SIDE,
                            status=SweepStatus.CONFIRMED,
                        )
                    )

                    break

        # -----------------------------------------
        # Sell-side sweeps
        # -----------------------------------------

        for pool in sell_side:

            zone = pool.zone_price

            for candle in candles:

                if (
                    candle.low.value < zone
                    and candle.close.value > zone
                ):

                    sweeps.append(
                        LiquiditySweep(
                            liquidity_pool=pool,
                            sweep_candle=candle,
                            direction=SweepDirection.SELL_SIDE,
                            status=SweepStatus.CONFIRMED,
                        )
                    )

                    break

        return LiquiditySweepSeries(sweeps)