"""
OGS Smart Money AI

Cache Collection
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator

from ogs.framework import BaseCollection

from .domain import Cache
from .enums import (
    CacheStatus,
    CacheType,
)


class CacheCollection(BaseCollection):
    """
    Collection of Cache objects.
    """

    def __init__(
        self,
        caches: Iterable[Cache] = (),
    ) -> None:
        self._caches = list(caches)

    def __iter__(self) -> Iterator[Cache]:
        return iter(self._caches)

    def __len__(self) -> int:
        return len(self._caches)

    def __getitem__(self, index: int) -> Cache:
        return self._caches[index]

    def add(
        self,
        cache: Cache,
    ) -> None:
        self._caches.append(cache)

    def active(self) -> "CacheCollection":
        return CacheCollection(
            c
            for c in self._caches
            if c.status == CacheStatus.ACTIVE
        )

    def expired(self) -> "CacheCollection":
        return CacheCollection(
            c
            for c in self._caches
            if c.status == CacheStatus.EXPIRED
        )

    def by_type(
        self,
        cache_type: CacheType,
    ) -> "CacheCollection":
        return CacheCollection(
            c
            for c in self._caches
            if c.cache_type == cache_type
        )

    def largest(self) -> Cache | None:
        if not self._caches:
            return None

        return max(
            self._caches,
            key=lambda c: c.capacity,
        )

    def smallest(self) -> Cache | None:
        if not self._caches:
            return None

        return min(
            self._caches,
            key=lambda c: c.capacity,
        )

    def total_capacity(self) -> int:
        return sum(
            c.capacity
            for c in self._caches
        )

    def total_used(self) -> int:
        return sum(
            c.used
            for c in self._caches
        )

    def average_utilization(self) -> float:
        if not self._caches:
            return 0.0

        return (
            sum(
                c.utilization
                for c in self._caches
            )
            / len(self._caches)
        )

    def find(
        self,
        name: str,
    ) -> Cache | None:

        name = name.casefold()

        for cache in self._caches:
            if cache.name.casefold() == name:
                return cache

        return None

    def to_list(self) -> list[Cache]:
        return list(self._caches)