"""
OGS FinOS

OTE Collection

Container for immutable OTE objects.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from collections.abc import Iterator
from uuid import UUID

from ogs.smart_money.ote.domain import (
    OTE,
)


class OTECollection:
    """
    Collection of immutable OTE objects.
    """

    def __init__(self) -> None:
        self._items: list[OTE] = []

    def add(
        self,
        ote: OTE,
    ) -> None:
        """
        Add an OTE.
        """
        self._items.append(ote)

    def extend(
        self,
        otes: list[OTE],
    ) -> None:
        """
        Add multiple OTE objects.
        """
        self._items.extend(otes)

    def clear(self) -> None:
        """
        Remove all OTE objects.
        """
        self._items.clear()

    def get_by_id(
        self,
        id: UUID,
    ) -> OTE | None:
        """
        Retrieve an OTE by UUID.
        """
        for item in self._items:
            if item.id == id:
                return item
        return None

    def latest(self) -> OTE | None:
        """
        Return the most recently added OTE.
        """
        if not self._items:
            return None

        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[OTE]:
        return iter(self._items)

    def __getitem__(
        self,
        index: int,
    ) -> OTE:
        return self._items[index]

    def __contains__(
        self,
        item: OTE,
    ) -> bool:
        return item in self._items

    def __bool__(self) -> bool:
        return bool(self._items)