"""
Performance-oriented tests for CacheAnalyzer.
"""

from ogs.market_data.cache import (
    CacheAnalyzer,
    CacheCollection,
    CacheFactory,
)


def test_large_collection():

    collection = CacheCollection()

    for i in range(1000):
        collection.add(
            CacheFactory.memory(
                f"Cache-{i}"
            )
        )

    analyzer = CacheAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["count"] == 1000


def test_large_analysis():

    collection = CacheCollection()

    for i in range(500):
        collection.add(
            CacheFactory.redis(
                f"Redis-{i}"
            )
        )

    analyzer = CacheAnalyzer(collection)

    result = analyzer.analyze()

    assert result["summary"]["count"] == 500


def test_distribution_speed():

    collection = CacheCollection()

    for i in range(300):
        collection.add(
            CacheFactory.disk(
                f"Disk-{i}"
            )
        )

    analyzer = CacheAnalyzer(collection)

    distribution = analyzer.performance_analysis()

    assert distribution["distribution"]["DISK"] == 300