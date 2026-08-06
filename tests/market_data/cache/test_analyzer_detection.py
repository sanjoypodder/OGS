"""
Tests for CacheAnalyzer detection logic.
"""

from ogs.market_data.cache import (
    CacheAnalyzer,
    CacheCollection,
    CacheFactory,
    CacheStatus,
)


def test_detect_expired_cache():

    collection = CacheCollection(
        [
            CacheFactory.memory("Memory"),
            CacheFactory.create(
                name="Expired",
                status=CacheStatus.EXPIRED,
            ),
        ]
    )

    analyzer = CacheAnalyzer(collection)

    summary = analyzer.summary()

    assert summary["active"] == 1


def test_distribution():

    collection = CacheCollection(
        [
            CacheFactory.memory("M1"),
            CacheFactory.memory("M2"),
            CacheFactory.redis("R1"),
        ]
    )

    analyzer = CacheAnalyzer(collection)

    distribution = analyzer.performance_analysis()["distribution"]

    assert distribution["MEMORY"] == 2
    assert distribution["REDIS"] == 1


def test_analyze_returns_sections():

    analyzer = CacheAnalyzer(
        CacheCollection()
    )

    result = analyzer.analyze()

    assert "summary" in result
    assert "capacity" in result
    assert "utilization" in result
    assert "performance" in result