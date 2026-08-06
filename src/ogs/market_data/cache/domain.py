"""
OGS Smart Money AI

Cache Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    CacheStatus,
    CacheType,
)


@dataclass(slots=True, frozen=True)
class Cache:
    """
    Represents a cache instance.
    """

    name: str

    cache_type: CacheType = CacheType.UNKNOWN

    status: CacheStatus = CacheStatus.UNKNOWN

    capacity: int = 0

    used: int = 0

    hit_count: int = 0

    miss_count: int = 0

    eviction_count: int = 0

    ttl_seconds: int = 0

    last_updated: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def active(self) -> bool:
        return self.status == CacheStatus.ACTIVE

    @property
    def expired(self) -> bool:
        return self.status == CacheStatus.EXPIRED

    @property
    def utilization(self) -> float:
        if self.capacity == 0:
            return 0.0
        return (self.used / self.capacity) * 100

    @property
    def hit_rate(self) -> float:
        total = self.hit_count + self.miss_count
        if total == 0:
            return 0.0
        return (self.hit_count / total) * 100

    @property
    def miss_rate(self) -> float:
        total = self.hit_count + self.miss_count
        if total == 0:
            return 0.0
        return (self.miss_count / total) * 100

    @property
    def is_valid(self) -> bool:
        return (
            bool(self.name.strip())
            and self.capacity >= 0
            and self.used >= 0
            and self.used <= self.capacity
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "cache_type": self.cache_type.value,
            "status": self.status.value,
            "capacity": self.capacity,
            "used": self.used,
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "eviction_count": self.eviction_count,
            "ttl_seconds": self.ttl_seconds,
            "last_updated": self.last_updated.isoformat(),
        }

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"[{self.cache_type.value}] "
            f"{self.used}/{self.capacity}"
        )