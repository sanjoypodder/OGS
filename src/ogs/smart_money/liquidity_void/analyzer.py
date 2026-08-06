"""
Liquidity Void Analyzer
"""

from ogs.market.candle import Candle
from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import LiquidityVoidSeries
from .domain import LiquidityVoid
from .enums import LiquidityVoidDirection


class LiquidityVoidAnalyzer(
    BaseAnalyzer[list[Candle], LiquidityVoidSeries]
):
    """
    Detects Liquidity Voids.

    Version 1:
        Three-candle institutional imbalance.

    Future:
        Multi-candle expansion detection.
    """

    def analyze(
        self,
        candles: list[Candle],
    ) -> LiquidityVoidSeries:

        series = LiquidityVoidSeries()

        if len(candles) < 3:
            return series

        for i in range(2, len(candles)):
            first = candles[i - 2]
            middle = candles[i - 1]
            last = candles[i]

            # ----------------------------
            # Bullish Liquidity Void
            # ----------------------------
            if last.low.value > first.high.value:

                top = last.low.value
                bottom = first.high.value

                series.append(
                    LiquidityVoid(
                        first=first,
                        last=last,
                        direction=LiquidityVoidDirection.BULLISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=top - bottom,
                        candle_count=3,
                    )
                )

            # ----------------------------
            # Bearish Liquidity Void
            # ----------------------------
            elif last.high.value < first.low.value:

                top = first.low.value
                bottom = last.high.value

                series.append(
                    LiquidityVoid(
                        first=first,
                        last=last,
                        direction=LiquidityVoidDirection.BEARISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=top - bottom,
                        candle_count=3,
                    )
                )

        return series