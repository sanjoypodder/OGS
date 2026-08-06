"""
===========================================================

OGS Smart Money AI

Displacement Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market import Candle
from ogs.smart_money.base import BaseAnalyzer

from .collection import DisplacementSeries
from .domain import Displacement
from .enums import DisplacementDirection


class DisplacementAnalyzer(
    BaseAnalyzer[
        list[Candle],
        DisplacementSeries,
    ],
):
    """
    Detect displacement candles.
    """

    def analyze(
        self,
        data: list[Candle],
    ) -> DisplacementSeries:
        """
        Analyze candles and detect displacement.
        """

        series = DisplacementSeries()

        for candle in data:

            if candle.close.value > candle.open.value:

                series.append(
                    Displacement(
                        candle=candle,
                        direction=DisplacementDirection.BULLISH,
                    )
                )

            elif candle.close.value < candle.open.value:

                series.append(
                    Displacement(
                        candle=candle,
                        direction=DisplacementDirection.BEARISH,
                    )
                )

            else:
                continue

        return series