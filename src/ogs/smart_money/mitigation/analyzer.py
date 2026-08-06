"""
===========================================================

OGS Smart Money AI

Mitigation Block Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market.candle import Candle
from ogs.smart_money.base import BaseAnalyzer

from .collection import MitigationBlockSeries
from .domain import MitigationBlock
from .enums import MitigationBlockDirection


class MitigationBlockAnalyzer(
    BaseAnalyzer[list[Candle], MitigationBlockSeries]
):
    """
    Detects ICT Mitigation Blocks.

    Version 1
    ---------
    Detects a mitigation after a strong impulsive move.

    Future versions will integrate with:
        • BOS
        • CHOCH
        • Order Block
        • Fair Value Gap
    """

    def analyze(
        self,
        candles: list[Candle],
    ) -> MitigationBlockSeries:

        series = MitigationBlockSeries()

        if len(candles) < 2:
            return series

        for i in range(1, len(candles)):

            previous = candles[i - 1]
            current = candles[i]

            # --------------------------------
            # Bullish Mitigation
            # --------------------------------

            if (
                previous.close.value < previous.open.value
                and current.low.value <= previous.high.value
                and current.close.value > previous.high.value
            ):

                top = previous.high.value
                bottom = previous.low.value

                series.append(
                    MitigationBlock(
                        candle=previous,
                        direction=MitigationBlockDirection.BULLISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=top - bottom,
                        is_mitigated=True,
                    )
                )

            # --------------------------------
            # Bearish Mitigation
            # --------------------------------

            elif (
                previous.close.value > previous.open.value
                and current.high.value >= previous.low.value
                and current.close.value < previous.low.value
            ):

                top = previous.high.value
                bottom = previous.low.value

                series.append(
                    MitigationBlock(
                        candle=previous,
                        direction=MitigationBlockDirection.BEARISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=top - bottom,
                        is_mitigated=True,
                    )
                )

        return series