"""
OGS Smart Money AI
------------------

Market Data - Candle Analyzer

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import CandleSeries
from .domain import Candle
from .enums import CandleDirection



class CandleAnalyzer(BaseAnalyzer):
    """
    Analyzer for CandleSeries.
    """

    def analyze(
        self,
        series: CandleSeries,
    ) -> dict:
        """
        Perform a generic analysis of a candle series.
        """

        return {
            "count": len(series),
            "bullish": len(self.bullish(series)),
            "bearish": len(self.bearish(series)),
            "doji": len(self.doji(series)),
            "highest": self.highest(series),
            "lowest": self.lowest(series),
            "average_close": self.average_close(series),
        }


    def bullish(
        self,
        series: CandleSeries,
    ) -> list[Candle]:

        return [
            candle
            for candle in series
            if candle.is_bullish
        ]

    def bearish(
        self,
        series: CandleSeries,
    ) -> list[Candle]:

        return [
            candle
            for candle in series
            if candle.is_bearish
        ]

    def doji(
        self,
        series: CandleSeries,
    ) -> list[Candle]:

        return [
            candle
            for candle in series
            if candle.is_doji
        ]

    def highest(
        self,
        series: CandleSeries,
    ) -> Candle | None:

        if len(series) == 0:
            return None

        return max(
            series,
            key=lambda candle: candle.high,
        )

    def lowest(
        self,
        series: CandleSeries,
    ) -> Candle | None:

        if len(series) == 0:
            return None

        return min(
            series,
            key=lambda candle: candle.low,
        )

    def strongest_bullish(
        self,
        series: CandleSeries,
    ) -> Candle | None:

        bullish = self.bullish(series)

        if not bullish:
            return None

        return max(
            bullish,
            key=lambda candle: candle.body_size,
        )

    def strongest_bearish(
        self,
        series: CandleSeries,
    ) -> Candle | None:

        bearish = self.bearish(series)

        if not bearish:
            return None

        return max(
            bearish,
            key=lambda candle: candle.body_size,
        )

    def largest_range(
        self,
        series: CandleSeries,
    ) -> Candle | None:

        if len(series) == 0:
            return None

        return max(
            series,
            key=lambda candle: candle.range,
        )

    def average_close(
        self,
        series: CandleSeries,
    ) -> float:

        if len(series) == 0:
            return 0.0

        return (
            sum(
                candle.close
                for candle in series
            )
            / len(series)
        )

    def direction_summary(
        self,
        series: CandleSeries,
    ) -> dict[CandleDirection, int]:

        summary = {
            CandleDirection.BULLISH: 0,
            CandleDirection.BEARISH: 0,
            CandleDirection.DOJI: 0,
        }

        for candle in series:
            summary[candle.direction] += 1

        return summary