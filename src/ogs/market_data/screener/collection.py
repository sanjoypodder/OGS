"""
===========================================================

OGS Smart Money AI

Screener Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Screener
from .enums import ScreenerType


class ScreenerCollection(
    BaseCollection[Screener],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        screener: Screener,
    ) -> None:

        self._items.append(screener)

    def find(
        self,
        screener_id: str,
    ) -> Screener | None:

        for screener in self._items:

            if (
                screener.screener_id
                == screener_id
            ):
                return screener

        return None

    def by_type(
        self,
        screener_type: ScreenerType,
    ):

        return [
            screener
            for screener in self._items
            if (
                screener.screener_type
                == screener_type
            )
        ]

    def active(self):

        return [
            screener
            for screener in self._items
            if screener.is_active
        ]

    def to_list(self):

        return list(self._items)