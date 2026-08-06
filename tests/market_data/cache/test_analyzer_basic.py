"""
Tests for CacheAnalyzer basic functionality.
"""

from ogs.market_data.cache import (
    CacheAnalyzer,
    CacheCollection,
    CacheFactory,
)


def create_analyzer():

    collection = CacheCollection(
        [
            CacheFactory.memory("Memory"),
            CacheFactory.redis("Redis"),
            CacheFactory.disk("Disk"),
        ]
    )

    return CacheAnalyzer(collection)


def test_summary():

    analyzer = create_analyzer()

    summary = analyzer.summary()

    assert summary["count"] == 3


def test_capacity_analysis():

    analyzer = create_analyzer()

    result = analyzer.capacity_analysis()

    assert "total_capacity" in result
    assert "total_used" in result


def test_utilization_analysis():

    analyzer = create_analyzer()

    result = analyzer.utilization_analysis()

    assert "utilization" in result
    assert "hit_rate" in result
    assert "miss_rate" in result


def test_performance_analysis():

    analyzer = create_analyzer()

    result = analyzer.performance_analysis()

    assert "distribution" in result
    assert "active" in result


def test_analyze():

    analyzer = create_analyzer()

    result = analyzer.analyze()

    assert isinstance(result, dict)
    assert "summary" in result