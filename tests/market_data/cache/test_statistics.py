"""
Tests for CacheStatistics.
"""

from ogs.market_data.cache import (
    CacheCollection,
    CacheFactory,
    CacheStatistics,
)


def create_statistics():

    collection = CacheCollection(
        [
            CacheFactory.memory("Memory"),
            CacheFactory.redis("Redis"),
            CacheFactory.disk("Disk"),
        ]
    )

    return CacheStatistics(collection)


def test_count():

    statistics = create_statistics()

    assert statistics.count == 3


def test_active_count():

    statistics = create_statistics()

    assert statistics.active_count == 3


def test_total_capacity():

    statistics = create_statistics()

    assert statistics.total_capacity == 0


def test_hit_rate():

    statistics = create_statistics()

    assert statistics.hit_rate == 0


def test_distribution():

    statistics = create_statistics()

    distribution = (
        statistics.cache_distribution
    )

    assert distribution["MEMORY"] == 1
    assert distribution["REDIS"] == 1
    assert distribution["DISK"] == 1


def test_summary():

    statistics = create_statistics()

    summary = statistics.summary()

    assert summary["count"] == 3
    assert "distribution" in summary