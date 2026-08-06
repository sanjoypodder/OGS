"""
===========================================================

OGS Smart Money AI

Fair Value Gap Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import FairValueGap


class FairValueGapSeries(BaseCollection[FairValueGap]):
    """
    Collection of Fair Value Gaps.
    """

    def __init__(self) -> None:
        self._items: list[FairValueGap] = []

    @property
    def fair_value_gaps(self) -> list[FairValueGap]:
        return self._items

    def append(
        self,
        gap: FairValueGap,
    ) -> None:
        self._items.append(gap)

    def latest(
        self,
        count: int = 1,
    ) -> list[FairValueGap]:
        return self._items[-count:]