"""
===========================================================

OGS Smart Money AI

Mitigation Block Statistics

===========================================================
"""

from __future__ import annotations

from .collection import MitigationBlockSeries


class MitigationBlockStatistics:
    """
    Statistics for Mitigation Blocks.
    """

    def __init__(
        self,
        series: MitigationBlockSeries,
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
    def mitigated(self) -> int:
        return sum(
            item.is_mitigated
            for item in self._series
        )

    @property
    def unmitigated(self) -> int:
        return self.total - self.mitigated