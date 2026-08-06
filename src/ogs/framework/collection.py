"""
OGS Generic Collection
"""

from __future__ import annotations

from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import TypeVar

T = TypeVar("T")


class BaseCollection(Generic[T]):
    """
    Generic collection used throughout OGS.
    """

    def __init__(self, items: Iterable[T] | None = None):

        self._items = list(items or [])

    def append(self, item: T) -> None:
        self._items.append(item)

    def extend(self, items: Iterable[T]) -> None:
        self._items.extend(items)

    def clear(self) -> None:
        self._items.clear()

    def first(self) -> T | None:
        return self._items[0] if self._items else None

    def last(self) -> T | None:
        return self._items[-1] if self._items else None

    def to_list(self) -> list[T]:
        return list(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)

    def __contains__(self, item):
        return item in self._items

    def __repr__(self):
        return f"{self.__class__.__name__}(count={len(self)})"

    def __eq__(self, other):

        if type(self) is not type(other):
            return NotImplemented

        return self._items == other._items