"""
===========================================================

OGS Smart Money AI

Base Collection

===========================================================
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseCollection(
    Generic[T],
):
    """
    Base collection class.
    """

    def __init__(
        self,
        items: list[T] | None = None,
    ):
        self._items = items or []

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(
        self,
        index: int,
    ) -> T:
        return self._items[index]

    @property
    def first(self) -> T:
        return self._items[0]

    @property
    def last(self) -> T:
        return self._items[-1]

    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0