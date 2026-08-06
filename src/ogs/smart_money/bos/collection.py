"""
===========================================================

OGS Smart Money AI

BOS Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import BOS


class BOSSeries(BaseCollection[BOS]):
    """
    Collection of BOS objects.
    """

    @property
    def structures(self) -> list[BOS]:
        return self._items

    def append(self, bos: BOS) -> None:
        self._items.append(bos)

    def latest(self, count: int) -> "BOSSeries":
        return BOSSeries(self._items[-count:])