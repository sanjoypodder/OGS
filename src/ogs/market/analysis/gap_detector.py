"""
Gap Detector
"""

from __future__ import annotations

from datetime import timedelta

from ogs.market.collections import CandleSeries
from ogs.market.analysis.base import Analyzer


class GapDetector(Analyzer[CandleSeries, list[int]]):
    """
    Detect missing candles.
    """

    def analyze(self, series: CandleSeries) -> list[int]:

        if len(series) < 2:
            return []

        expected = timedelta(
            seconds=series.first.timeframe.seconds
        )

        gaps: list[int] = []

        candles = series.candles

        for index in range(1, len(candles)):

            difference = (
                candles[index].timestamp -
                candles[index - 1].timestamp
            )

            if difference > expected:
                gaps.append(index)

        return gaps