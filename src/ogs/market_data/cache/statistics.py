"""
OGS Smart Money AI

Cache Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import CacheCollection
from .domain import Cache


class CacheStatistics(BaseStatistics):
    """
    Cache statistics.
    """

    def __init__(
        self,
        caches: CacheCollection,
    ):
        self.caches = caches

    @property
    def count(self) -> int:
        return len(self.caches)

    @property
    def active_count(self) -> int:
        return len(self.caches.active())

    @property
    def total_capacity(self) -> int:
        return self.caches.total_capacity()

    @property
    def total_used(self) -> int:
        return self.caches.total_used()

    @property
    def utilization_percentage(self) -> float:

        if self.total_capacity == 0:
            return 0.0

        return (
            self.total_used
            / self.total_capacity
        ) * 100

    @property
    def hit_rate(self) -> float:

        hits = sum(
            c.hit_count
            for c in self.caches
        )

        misses = sum(
            c.miss_count
            for c in self.caches
        )

        total = hits + misses

        if total == 0:
            return 0.0

        return (hits / total) * 100

    @property
    def miss_rate(self) -> float:

        hits = sum(
            c.hit_count
            for c in self.caches
        )

        misses = sum(
            c.miss_count
            for c in self.caches
        )

        total = hits + misses

        if total == 0:
            return 0.0

        return (misses / total) * 100

    @property
    def largest_cache(self) -> Cache | None:
        return self.caches.largest()

    @property
    def smallest_cache(self) -> Cache | None:
        return self.caches.smallest()

    @property
    def cache_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                c.cache_type.value
                for c in self.caches
            )
        )

    def summary(self) -> dict:

        return {
            "count": self.count,
            "active": self.active_count,
            "total_capacity": self.total_capacity,
            "total_used": self.total_used,
            "utilization": round(
                self.utilization_percentage,
                2,
            ),
            "hit_rate": round(
                self.hit_rate,
                2,
            ),
            "miss_rate": round(
                self.miss_rate,
                2,
            ),
            "distribution": self.cache_distribution,
        }