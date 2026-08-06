"""
===========================================================

OGS Smart Money AI

Index Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Index
from .enums import IndexType


class IndexCollection(
    BaseCollection[Index],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        index: Index,
    ) -> None:

        self._items.append(index)

    def find(
        self,
        index_code: str,
    ) -> Index | None:

        for item in self._items:

            if item.index_code == index_code:
                return item

        return None

    def by_type(
        self,
        index_type: IndexType,
    ):

        return [
            item
            for item in self._items
            if item.index_type == index_type
        ]

    def active(self):

        return [
            item
            for item in self._items
            if item.is_active
        ]

    def to_list(self):

        return list(self._items)