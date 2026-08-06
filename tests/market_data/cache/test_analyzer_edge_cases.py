"""
Edge-case tests for CacheAnalyzer.
"""

from ogs.market_data.cache import (
    CacheAnalyzer,
    CacheCollection,
)


def test_empty_collection():

    analyzer = CacheAnalyzer(
        CacheCollection()
    )

    summary = analyzer.summary()

    assert summary["count"] == 0
    assert summary["active"] == 0


def test_empty_analysis():

    analyzer = CacheAnalyzer(
        CacheCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0


def test_empty_capacity():

    analyzer = CacheAnalyzer(
        CacheCollection()
    )

    result = analyzer.capacity_analysis()

    assert result["largest_cache"] is None
    assert result["smallest_cache"] is None


def test_zero_utilization():

    analyzer = CacheAnalyzer(
        CacheCollection()
    )

    result = analyzer.utilization_analysis()

    assert result["utilization"] == 0.0