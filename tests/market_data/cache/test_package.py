"""
Tests for cache package exports.
"""

from ogs.market_data.cache import (
    Cache,
    CacheAnalyzer,
    CacheCollection,
    CacheFactory,
    CacheStatistics,
    CacheStatus,
    CacheType,
    CacheValidator,
)


def test_package_imports():

    assert Cache is not None
    assert CacheType is not None
    assert CacheStatus is not None
    assert CacheValidator is not None
    assert CacheFactory is not None
    assert CacheCollection is not None
    assert CacheStatistics is not None
    assert CacheAnalyzer is not None


def test_version_exists():

    import ogs.market_data.cache as cache

    assert hasattr(cache, "__version__")
    assert cache.__version__ == "0.1.0"