"""
===========================================================

OGS Smart Money AI

Swing Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.market import CandleSeries
from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import SwingSeries
from .domain import Swing
from .enums import SwingType


class SwingAnalyzer(
    BaseAnalyzer[
        CandleSeries,
        SwingSeries,
    ]
):
    """
    Bill Williams five-candle swing analyzer.
    """

    def analyze(
        self,
        series: CandleSeries,
    ) -> SwingSeries:

        swings: list[Swing] = []

        candles = series.candles

        if len(candles) < 5:
            return SwingSeries([])

        for index in range(2, len(candles) - 2):

            center = candles[index]

            if (
                center.high > candles[index - 1].high
                and center.high > candles[index - 2].high
                and center.high > candles[index + 1].high
                and center.high > candles[index + 2].high
            ):
                swings.append(
                    Swing(
                        index=index,
                        candle=center,
                        swing_type=SwingType.HIGH,
                    )
                )

            if (
                center.low < candles[index - 1].low
                and center.low < candles[index - 2].low
                and center.low < candles[index + 1].low
                and center.low < candles[index + 2].low
            ):
                swings.append(
                    Swing(
                        index=index,
                        candle=center,
                        swing_type=SwingType.LOW,
                    )
                )

        return SwingSeries(swings)