"""
===========================================================

OGS Smart Money AI

CHOCH Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import CHOCH


class CHOCHSeries(BaseCollection[CHOCH]):
    """
    Collection of CHOCH objects.
    """

    @property
    def structures(self) -> list[CHOCH]:
        return self._items

    def append(
        self,
        choch: CHOCH,
    ) -> None:
        self._items.append(choch)

    def latest(
        self,
        count: int,
    ) -> "CHOCHSeries":
        return CHOCHSeries(
            self._items[-count:]
        )