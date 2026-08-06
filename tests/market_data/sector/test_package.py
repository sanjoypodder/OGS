"""
Tests for Sector package exports.
"""

from ogs.market_data.sector import (
    __version__,
    Sector,
    SectorAnalyzer,
    SectorCollection,
    SectorFactory,
    SectorStatistics,
    SectorStatus,
    SectorType,
    SectorValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Sector is not None
    assert SectorAnalyzer is not None
    assert SectorCollection is not None
    assert SectorFactory is not None
    assert SectorStatistics is not None
    assert SectorValidator is not None
    assert SectorType is not None
    assert SectorStatus is not None