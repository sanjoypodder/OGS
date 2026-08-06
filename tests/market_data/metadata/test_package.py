"""
Tests for Metadata package exports.
"""

from ogs.market_data.metadata import (
    __version__,
    Metadata,
    MetadataAnalyzer,
    MetadataCollection,
    MetadataFactory,
    MetadataStatistics,
    MetadataStatus,
    MetadataType,
    MetadataValidator,
    MetadataValueType,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Metadata is not None
    assert MetadataAnalyzer is not None
    assert MetadataCollection is not None
    assert MetadataFactory is not None
    assert MetadataStatistics is not None
    assert MetadataValidator is not None
    assert MetadataType is not None
    assert MetadataStatus is not None
    assert MetadataValueType is not None