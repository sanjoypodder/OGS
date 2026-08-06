"""
Tests for Cache domain.
"""

from ogs.market_data.cache import (
    Cache,
    CacheStatus,
    CacheType,
)


def test_cache_creation():

    cache = Cache(
        name="Main Cache",
        cache_type=CacheType.MEMORY,
        status=CacheStatus.ACTIVE,
        capacity=1000,
        used=400,
        hit_count=80,
        miss_count=20,
    )

    assert cache.name == "Main Cache"
    assert cache.cache_type == CacheType.MEMORY
    assert cache.status == CacheStatus.ACTIVE
    assert cache.capacity == 1000
    assert cache.used == 400


def test_active_property():

    cache = Cache(
        name="Cache",
        status=CacheStatus.ACTIVE,
    )

    assert cache.active is True
    assert cache.expired is False


def test_expired_property():

    cache = Cache(
        name="Cache",
        status=CacheStatus.EXPIRED,
    )

    assert cache.expired is True


def test_utilization():

    cache = Cache(
        name="Cache",
        capacity=100,
        used=50,
    )

    assert cache.utilization == 50.0


def test_hit_rate():

    cache = Cache(
        name="Cache",
        hit_count=75,
        miss_count=25,
    )

    assert cache.hit_rate == 75.0
    assert cache.miss_rate == 25.0


def test_to_dict():

    cache = Cache(name="Cache")

    data = cache.to_dict()

    assert data["name"] == "Cache"


def test_valid():

    cache = Cache(name="Cache")

    assert cache.is_valid