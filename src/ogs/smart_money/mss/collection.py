"""
===========================================================

OGS Smart Money AI

MSS Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import MSS


class MSSSeries(BaseCollection[MSS]):
    """
    Collection of MSS objects.
    """

    @property
    def structures(self) -> list[MSS]:
        return self._items

    def append(
        self,
        mss: MSS,
    ) -> None:
        self._items.append(mss)

    def latest(
        self,
        count: int,
    ) -> "MSSSeries":

        return MSSSeries(
            self._items[-count:]
        )