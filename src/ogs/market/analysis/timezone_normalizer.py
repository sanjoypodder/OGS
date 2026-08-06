"""
===========================================================

OGS Smart Money AI

Timezone Normalizer

===========================================================
"""

from __future__ import annotations

from dataclasses import replace
from datetime import UTC

from ogs.market.analysis.base import Analyzer
from ogs.market.analysis.timezone_result import TimezoneResult
from ogs.market.candle import Candle
from ogs.market.collections import CandleSeries


class TimezoneNormalizer(
    Analyzer[CandleSeries, tuple[CandleSeries, TimezoneResult]]
):
    """
    Normalize every candle timestamp to UTC.
    """

    def analyze(
        self,
        series: CandleSeries,
    ) -> tuple[CandleSeries, TimezoneResult]:

        normalized = 0
        skipped = 0

        candles: list[Candle] = []

        for candle in series:

            timestamp = candle.timestamp

            if timestamp.tzinfo == UTC:

                skipped += 1

                candles.append(candle)

                continue

            normalized += 1

            candles.append(
                replace(
                    candle,
                    timestamp=timestamp.astimezone(UTC),
                )
            )

        return (
            CandleSeries(candles),
            TimezoneResult(
                normalized=normalized,
                skipped=skipped,
            ),
        )