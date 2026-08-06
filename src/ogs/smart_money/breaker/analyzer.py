"""
===========================================================

OGS Smart Money AI

Breaker Block Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market.candle import Candle
from ogs.smart_money.base import BaseAnalyzer

from .collection import BreakerBlockSeries
from .domain import BreakerBlock
from .enums import BreakerBlockDirection


class BreakerBlockAnalyzer(
    BaseAnalyzer[list[Candle], BreakerBlockSeries]
):
    """
    Detects ICT Breaker Blocks.

    Version 1
    ---------
    Detects the last opposite candle before an
    impulsive structural break.

    Future versions will integrate directly with
    the BOS module.
    """

    def analyze(
        self,
        candles: list[Candle],
    ) -> BreakerBlockSeries:

        series = BreakerBlockSeries()

        if len(candles) < 2:
            return series

        for i in range(1, len(candles)):

            previous = candles[i - 1]
            current = candles[i]

            # --------------------------------
            # Bullish Breaker
            # Last bearish candle before
            # bullish impulse.
            # --------------------------------

            if (
                previous.close.value < previous.open.value
                and current.close.value > previous.high.value
            ):

                top = previous.high.value
                bottom = previous.low.value

                series.append(
                    BreakerBlock(
                        candle=previous,
                        direction=BreakerBlockDirection.BULLISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=top - bottom,
                    )
                )

            # --------------------------------
            # Bearish Breaker
            # Last bullish candle before
            # bearish impulse.
            # --------------------------------

            elif (
                previous.close.value > previous.open.value
                and current.close.value < previous.low.value
            ):

                top = previous.high.value
                bottom = previous.low.value

                series.append(
                    BreakerBlock(
                        candle=previous,
                        direction=BreakerBlockDirection.BEARISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=top - bottom,
                    )
                )

        return series