"""
===========================================================

OGS Smart Money AI

Swing Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Swing


class SwingSeries(BaseCollection[Swing]):
    """
    Collection of Swing objects.
    """

    @property
    def swings(self) -> list[Swing]:
        return self._items

    def append(self, swing: Swing) -> None:
        self._items.append(swing)

    def latest(self, count: int) -> "SwingSeries":
        return SwingSeries(self._items[-count:])