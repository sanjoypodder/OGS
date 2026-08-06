"""
===========================================================

OGS Smart Money AI

Imbalance Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseStatistics

from .collection import ImbalanceSeries
from .enums import ImbalanceDirection


class ImbalanceStatistics(BaseStatistics):
    """
    Statistics for imbalance collections.
    """

    def __init__(
        self,
        series: ImbalanceSeries,
    ) -> None:
        self._series = series

    @property
    def total(self) -> int:
        return len(self._series)

    @property
    def bullish(self) -> int:
        return sum(
            1
            for imbalance in self._series
            if imbalance.direction
            is ImbalanceDirection.BULLISH
        )

    @property
    def bearish(self) -> int:
        return sum(
            1
            for imbalance in self._series
            if imbalance.direction
            is ImbalanceDirection.BEARISH
        )