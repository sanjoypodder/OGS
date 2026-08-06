"""
===========================================================

OGS Smart Money AI

Universe Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Universe
from .enums import UniverseType


class UniverseCollection(
    BaseCollection[Universe],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        universe: Universe,
    ) -> None:

        self._items.append(universe)

    def find(
        self,
        universe_id: str,
    ) -> Universe | None:

        for universe in self._items:

            if universe.universe_id == universe_id:
                return universe

        return None

    def by_type(
        self,
        universe_type: UniverseType,
    ):

        return [
            universe
            for universe in self._items
            if universe.universe_type == universe_type
        ]

    def active(self):

        return [
            universe
            for universe in self._items
            if universe.is_active
        ]

    def to_list(self):

        return list(self._items)