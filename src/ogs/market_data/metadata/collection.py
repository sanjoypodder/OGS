"""
===========================================================

OGS Smart Money AI

Metadata Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import (
    BaseCollection,
)

from .domain import Metadata
from .enums import MetadataType


class MetadataCollection(
    BaseCollection[Metadata],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        metadata: Metadata,
    ) -> None:

        self._items.append(metadata)

    def find(
        self,
        metadata_id: str,
    ) -> Metadata | None:

        for item in self._items:

            if item.metadata_id == metadata_id:
                return item

        return None

    def by_entity(
        self,
        entity_type: str,
        entity_id: str,
    ) -> list[Metadata]:

        return [
            item
            for item in self._items
            if (
                item.entity_type == entity_type
                and item.entity_id == entity_id
            )
        ]

    def by_key(
        self,
        key: str,
    ) -> list[Metadata]:

        return [
            item
            for item in self._items
            if item.key == key
        ]

    def by_type(
        self,
        metadata_type: MetadataType,
    ) -> list[Metadata]:

        return [
            item
            for item in self._items
            if item.metadata_type == metadata_type
        ]

    def active(self) -> list[Metadata]:

        return [
            item
            for item in self._items
            if item.is_active
        ]

    def to_list(self) -> list[Metadata]:

        return list(self._items)