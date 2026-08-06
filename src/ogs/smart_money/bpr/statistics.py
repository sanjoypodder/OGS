"""
===========================================================

OGS Smart Money AI

Balanced Price Range Statistics

===========================================================
"""

from __future__ import annotations

from .collection import BalancedPriceRangeSeries
from .domain import BalancedPriceRange
from .enums import BalancedPriceRangeDirection


class BalancedPriceRangeStatistics:
    """
    Statistics for Balanced Price Ranges.
    """

    def __init__(
        self,
        series: BalancedPriceRangeSeries,
    ) -> None:

        self._series = series

    @property
    def count(
        self,
    ) -> int:
        """
        Total number of Balanced Price Ranges.
        """
        return len(self._series)

    @property
    def bullish_count(
        self,
    ) -> int:
        """
        Number of bullish Balanced Price Ranges.
        """
        return sum(
            1
            for bpr in self._series
            if bpr.direction
            is BalancedPriceRangeDirection.BULLISH
        )

    @property
    def bearish_count(
        self,
    ) -> int:
        """
        Number of bearish Balanced Price Ranges.
        """
        return sum(
            1
            for bpr in self._series
            if bpr.direction
            is BalancedPriceRangeDirection.BEARISH
        )

    @property
    def neutral_count(
        self,
    ) -> int:
        """
        Number of neutral Balanced Price Ranges.
        """
        return sum(
            1
            for bpr in self._series
            if bpr.direction
            is BalancedPriceRangeDirection.NEUTRAL
        )

    @property
    def average_size(
        self,
    ) -> float:
        """
        Average Balanced Price Range size.
        """

        if self.count == 0:
            return 0.0

        return (
            sum(
                bpr.size
                for bpr in self._series
            )
            / self.count
        )

    @property
    def largest(
        self,
    ) -> BalancedPriceRange | None:
        """
        Largest Balanced Price Range.
        """

        if self.count == 0:
            return None

        return max(
            self._series,
            key=lambda bpr: bpr.size,
        )

    @property
    def smallest(
        self,
    ) -> BalancedPriceRange | None:
        """
        Smallest Balanced Price Range.
        """

        if self.count == 0:
            return None

        return min(
            self._series,
            key=lambda bpr: bpr.size,
        )