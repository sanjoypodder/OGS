"""
OGS FinOS

Dealing Range Collection

Container for DealingRange objects.

Author : OGS FinOS
Version : 0.0.2
"""

from __future__ import annotations

from collections.abc import Iterator
from uuid import UUID

from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)


class DealingRangeCollection:
    """
    Collection of immutable DealingRange objects.
    """

    def __init__(self) -> None:
        self._items: list[DealingRange] = []

    def add(
        self,
        dealing_range: DealingRange,
    ) -> None:
        """
        Add a dealing range.
        """
        self._items.append(dealing_range)

    def extend(
        self,
        dealing_ranges: list[DealingRange],
    ) -> None:
        """
        Add multiple dealing ranges.
        """
        self._items.extend(dealing_ranges)

    def clear(self) -> None:
        """
        Remove all dealing ranges.
        """
        self._items.clear()

    def get_by_id(
        self,
        id: UUID,
    ) -> DealingRange | None:
        """
        Retrieve a dealing range by UUID.
        """
        for item in self._items:
            if item.id == id:
                return item
        return None

    def latest(self) -> DealingRange | None:
        """
        Return the most recently added dealing range.
        """
        if not self._items:
            return None

        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[DealingRange]:
        return iter(self._items)

    def __getitem__(
        self,
        index: int,
    ) -> DealingRange:
        return self._items[index]

    def __contains__(
        self,
        item: DealingRange,
    ) -> bool:
        return item in self._items

    def __bool__(self) -> bool:
        return bool(self._items)