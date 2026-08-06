"""
===========================================================

OGS Smart Money AI

Fair Value Gap Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market import Candle
from ogs.smart_money.base import BaseAnalyzer

from .collection import FairValueGapSeries
from .domain import FairValueGap
from .enums import FairValueGapDirection


class FairValueGapAnalyzer(
    BaseAnalyzer[
        list[Candle],
        FairValueGapSeries,
    ]
):
    """
    Detect Fair Value Gaps.
    """

    def analyze(
        self,
        data: list[Candle],
    ) -> FairValueGapSeries:

        series = FairValueGapSeries()

        if len(data) < 3:
            return series

        for i in range(len(data) - 2):

            first = data[i]
            middle = data[i + 1]
            last = data[i + 2]

            # -----------------------------
            # Bullish Fair Value Gap
            # -----------------------------

            if last.low.value > first.high.value:

                top = last.low.value
                bottom = first.high.value
                size = top - bottom

                series.append(
                    FairValueGap(
                        first=first,
                        middle=middle,
                        last=last,
                        direction=FairValueGapDirection.BULLISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=size,
                    )
                )

            # -----------------------------
            # Bearish Fair Value Gap
            # -----------------------------

            elif last.high.value < first.low.value:

                top = first.low.value
                bottom = last.high.value
                size = top - bottom

                series.append(
                    FairValueGap(
                        first=first,
                        middle=middle,
                        last=last,
                        direction=FairValueGapDirection.BEARISH,
                        top=top,
                        bottom=bottom,
                        midpoint=(top + bottom) / 2,
                        size=size,
                    )
                )

        return series