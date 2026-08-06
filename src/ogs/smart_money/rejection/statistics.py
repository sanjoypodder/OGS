"""
===========================================================

OGS Smart Money AI

Rejection Block Statistics

===========================================================
"""

from __future__ import annotations

from .collection import RejectionBlockSeries


class RejectionBlockStatistics:
    """
    Statistics for Rejection Blocks.
    """

    def __init__(
        self,
        series: RejectionBlockSeries,
    ) -> None:
        self._series = series

    @property
    def total(self) -> int:
        return len(self._series)

    @property
    def bullish(self) -> int:
        return sum(
            item.is_bullish
            for item in self._series
        )

    @property
    def bearish(self) -> int:
        return sum(
            item.is_bearish
            for item in self._series
        )

    @property
    def confirmed(self) -> int:
        return sum(
            item.is_confirmed
            for item in self._series
        )

    @property
    def unconfirmed(self) -> int:
        return self.total - self.confirmed