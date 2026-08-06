"""
OGS Smart Money AI

Cache Factory
"""

from __future__ import annotations

from datetime import UTC, datetime

from ogs.framework import BaseFactory

from .domain import Cache
from .enums import (
    CacheStatus,
    CacheType,
)
from .validator import CacheValidator


class CacheFactory(BaseFactory):
    """
    Factory for Cache objects.
    """

    _validator = CacheValidator()

    @classmethod
    def create(
        cls,
        *,
        name: str,
        cache_type: CacheType = CacheType.UNKNOWN,
        status: CacheStatus = CacheStatus.UNKNOWN,
        capacity: int = 0,
        used: int = 0,
        hit_count: int = 0,
        miss_count: int = 0,
        eviction_count: int = 0,
        ttl_seconds: int = 0,
        last_updated: datetime | None = None,
    ) -> Cache:

        cache = Cache(
            name=name,
            cache_type=cache_type,
            status=status,
            capacity=capacity,
            used=used,
            hit_count=hit_count,
            miss_count=miss_count,
            eviction_count=eviction_count,
            ttl_seconds=ttl_seconds,
            last_updated=(
                last_updated
                if last_updated is not None
                else datetime.now(UTC)
            ),
        )

        return cls._validator(cache)

    @classmethod
    def memory(
        cls,
        name: str,
    ) -> Cache:
        return cls.create(
            name=name,
            cache_type=CacheType.MEMORY,
            status=CacheStatus.ACTIVE,
        )

    @classmethod
    def redis(
        cls,
        name: str,
    ) -> Cache:
        return cls.create(
            name=name,
            cache_type=CacheType.REDIS,
            status=CacheStatus.ACTIVE,
        )

    @classmethod
    def disk(
        cls,
        name: str,
    ) -> Cache:
        return cls.create(
            name=name,
            cache_type=CacheType.DISK,
            status=CacheStatus.ACTIVE,
        )

    @classmethod
    def clone(
        cls,
        cache: Cache,
    ) -> Cache:
        return cls.create(
            name=cache.name,
            cache_type=cache.cache_type,
            status=cache.status,
            capacity=cache.capacity,
            used=cache.used,
            hit_count=cache.hit_count,
            miss_count=cache.miss_count,
            eviction_count=cache.eviction_count,
            ttl_seconds=cache.ttl_seconds,
            last_updated=cache.last_updated,
        )