"""
===========================================================

OGS Smart Money AI

Duplicate Detector

===========================================================
"""

from __future__ import annotations

from ogs.market.analysis.base import Analyzer
from ogs.market.analysis.duplicate import Duplicate
from ogs.market.collections import CandleSeries


class DuplicateDetector(Analyzer[CandleSeries, list[Duplicate]]):
    """
    Detect duplicate candles by timestamp.
    """

    def analyze(
        self,
        series: CandleSeries,
    ) -> list[Duplicate]:

        duplicates: list[Duplicate] = []

        seen = set()

        for index, candle in enumerate(series):

            if candle.timestamp in seen:

                duplicates.append(
                    Duplicate(
                        index=index,
                        timestamp=candle.timestamp,
                    )
                )

            else:

                seen.add(candle.timestamp)

        return duplicates