"""
===========================================================

OGS Smart Money AI

Equal High Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import EqualHigh


class EqualHighSeries(
    BaseCollection[EqualHigh]
):
    """
    Collection of Equal High zones.
    """

    @property
    def zones(self) -> list[EqualHigh]:
        return self._items

    def append(
        self,
        zone: EqualHigh,
    ) -> None:

        self._items.append(zone)

    def latest(
        self,
        count: int,
    ) -> "EqualHighSeries":

        return EqualHighSeries(
            self._items[-count:]
        )