"""
OGS Smart Money AI
------------------

Market Data - Candle Statistics

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from .collection import CandleSeries
from .domain import Candle
from .enums import CandleDirection


class CandleStatistics:
    """
    Statistics for CandleSeries.
    """

    def __init__(
        self,
        series: CandleSeries,
    ) -> None:

        self._series = series

    @property
    def count(self) -> int:

        return len(self._series)

    @property
    def bullish_count(self) -> int:

        return sum(
            candle.is_bullish
            for candle in self._series
        )

    @property
    def bearish_count(self) -> int:

        return sum(
            candle.is_bearish
            for candle in self._series
        )

    @property
    def doji_count(self) -> int:

        return sum(
            candle.is_doji
            for candle in self._series
        )

    @property
    def total_volume(self) -> float:

        return sum(
            candle.volume
            for candle in self._series
        )

    @property
    def highest_price(self) -> float:

        if len(self._series) == 0:
            return 0.0

        return max(
            candle.high
            for candle in self._series
        )

    @property
    def lowest_price(self) -> float:

        if len(self._series) == 0:
            return 0.0

        return min(
            candle.low
            for candle in self._series
        )

    @property
    def average_range(self) -> float:

        if len(self._series) == 0:
            return 0.0

        return (
            sum(
                candle.range
                for candle in self._series
            )
            / len(self._series)
        )

    @property
    def average_body(self) -> float:

        if len(self._series) == 0:
            return 0.0

        return (
            sum(
                candle.body_size
                for candle in self._series
            )
            / len(self._series)
        )

    @property
    def latest(self) -> Candle | None:

        if len(self._series) == 0:
            return None

        return self._series.last

    @property
    def oldest(self) -> Candle | None:

        if len(self._series) == 0:
            return None

        return self._series.first