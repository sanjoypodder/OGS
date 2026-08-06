"""
===========================================================

OGS Smart Money AI

Equal Low Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import EqualLow


class EqualLowSeries(BaseCollection[EqualLow]):
    """
    Collection of Equal Low zones.
    """

    @property
    def zones(self) -> list[EqualLow]:
        return self._items

    def append(
        self,
        zone: EqualLow,
    ) -> None:

        self._items.append(zone)

    def latest(
        self,
        count: int,
    ) -> "EqualLowSeries":

        return EqualLowSeries(
            self._items[-count:]
        )