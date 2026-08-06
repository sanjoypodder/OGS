"""
Tests for Asset package exports.
"""

from ogs.market_data.asset import (
    __version__,
    Asset,
    AssetAnalyzer,
    AssetCollection,
    AssetFactory,
    AssetStatistics,
    AssetType,
    AssetValidator,
)


def test_version():
    assert __version__ == "0.1.0"


def test_exports():
    assert Asset is not None
    assert AssetAnalyzer is not None
    assert AssetCollection is not None
    assert AssetFactory is not None
    assert AssetStatistics is not None
    assert AssetValidator is not None
    assert AssetType is not None