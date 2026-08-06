"""
OGS Smart Money AI

Cache Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Cache
from .enums import (
    CacheStatus,
    CacheType,
)


class CacheValidator(BaseValidator):
    """
    Cache validator.
    """

    def validate(
        self,
        cache: Cache,
    ) -> None:

        if not isinstance(cache, Cache):
            raise TypeError(
                "cache must be Cache."
            )

        if not cache.name.strip():
            raise ValueError(
                "Cache name cannot be empty."
            )

        if not isinstance(
            cache.cache_type,
            CacheType,
        ):
            raise TypeError(
                "Invalid cache type."
            )

        if not isinstance(
            cache.status,
            CacheStatus,
        ):
            raise TypeError(
                "Invalid cache status."
            )

        if cache.capacity < 0:
            raise ValueError(
                "Capacity cannot be negative."
            )

        if cache.used < 0:
            raise ValueError(
                "Used cannot be negative."
            )

        if cache.used > cache.capacity:
            raise ValueError(
                "Used exceeds capacity."
            )

        if cache.hit_count < 0:
            raise ValueError(
                "Hit count cannot be negative."
            )

        if cache.miss_count < 0:
            raise ValueError(
                "Miss count cannot be negative."
            )

        if cache.eviction_count < 0:
            raise ValueError(
                "Eviction count cannot be negative."
            )

        if cache.ttl_seconds < 0:
            raise ValueError(
                "TTL cannot be negative."
            )

        if not isinstance(
            cache.last_updated,
            datetime,
        ):
            raise TypeError(
                "Invalid datetime."
            )

    def __call__(
        self,
        cache: Cache,
    ) -> Cache:

        self.validate(cache)

        return cache