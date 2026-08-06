"""
===========================================================

OGS Smart Money AI

Fair Value Gap Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseStatistics

from .collection import FairValueGapSeries
from .enums import FairValueGapDirection


class FairValueGapStatistics(BaseStatistics):
    """
    Statistics for Fair Value Gaps.
    """

    def __init__(
        self,
        series: FairValueGapSeries,
    ) -> None:
        self._series = series

    @property
    def total(self) -> int:
        return len(self._series)

    @property
    def bullish(self) -> int:
        return sum(
            1
            for gap in self._series
            if gap.direction is FairValueGapDirection.BULLISH
        )

    @property
    def bearish(self) -> int:
        return sum(
            1
            for gap in self._series
            if gap.direction is FairValueGapDirection.BEARISH
        )

    @property
    def filled(self) -> int:
        return sum(
            1
            for gap in self._series
            if gap.is_filled
        )

    @property
    def unfilled(self) -> int:
        return sum(
            1
            for gap in self._series
            if not gap.is_filled
        )