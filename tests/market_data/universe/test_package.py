"""
Tests for Universe package exports.
"""

from ogs.market_data.universe import (
    __version__,
    Universe,
    UniverseAnalyzer,
    UniverseCollection,
    UniverseFactory,
    UniverseStatistics,
    UniverseStatus,
    UniverseType,
    UniverseValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Universe is not None
    assert UniverseAnalyzer is not None
    assert UniverseCollection is not None
    assert UniverseFactory is not None
    assert UniverseStatistics is not None
    assert UniverseValidator is not None
    assert UniverseType is not None
    assert UniverseStatus is not None