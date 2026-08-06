"""
Tests for CacheFactory.
"""

from ogs.market_data.cache import (
    Cache,
    CacheFactory,
    CacheStatus,
    CacheType,
)


def test_create():

    cache = CacheFactory.create(
        name="Cache",
        cache_type=CacheType.MEMORY,
        status=CacheStatus.ACTIVE,
        capacity=1000,
        used=250,
        hit_count=50,
        miss_count=10,
    )

    assert isinstance(cache, Cache)
    assert cache.name == "Cache"
    assert cache.capacity == 1000
    assert cache.used == 250


def test_memory():

    cache = CacheFactory.memory("Memory")

    assert cache.cache_type == CacheType.MEMORY
    assert cache.status == CacheStatus.ACTIVE


def test_redis():

    cache = CacheFactory.redis("Redis")

    assert cache.cache_type == CacheType.REDIS
    assert cache.status == CacheStatus.ACTIVE


def test_disk():

    cache = CacheFactory.disk("Disk")

    assert cache.cache_type == CacheType.DISK
    assert cache.status == CacheStatus.ACTIVE


def test_clone():

    cache = CacheFactory.create(
        name="Original",
        capacity=500,
        used=200,
    )

    clone = CacheFactory.clone(cache)

    assert clone == cache