"""
===========================================================

OGS Smart Money AI

Imbalance Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market import Candle
from ogs.smart_money.base import BaseAnalyzer

from .collection import ImbalanceSeries
from .domain import Imbalance
from .enums import ImbalanceDirection


class ImbalanceAnalyzer(
    BaseAnalyzer[
        list[Candle],
        ImbalanceSeries,
    ]
):
    """
    Detect generic market imbalances.
    """

    def analyze(
        self,
        data: list[Candle],
    ) -> ImbalanceSeries:

        series = ImbalanceSeries()

        if len(data) < 3:
            return series

        for index in range(len(data) - 2):

            first = data[index]
            middle = data[index + 1]
            last = data[index + 2]

            # Bullish imbalance
            if last.low.value > first.high.value:

                series.append(
                    Imbalance(
                        first=first,
                        middle=middle,
                        last=last,
                        direction=ImbalanceDirection.BULLISH,
                    )
                )

            # Bearish imbalance
            elif last.high.value < first.low.value:

                series.append(
                    Imbalance(
                        first=first,
                        middle=middle,
                        last=last,
                        direction=ImbalanceDirection.BEARISH,
                    )
                )

        return series