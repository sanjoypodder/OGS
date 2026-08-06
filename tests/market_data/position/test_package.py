"""
Package tests for Position module.
"""

from ogs.market_data.position import (
    Position,
    PositionAnalyzer,
    PositionCollection,
    PositionFactory,
    PositionSide,
    PositionStatistics,
    PositionStatus,
    PositionValidator,
)


def test_package_imports():

    assert Position is not None
    assert PositionSide is not None
    assert PositionStatus is not None
    assert PositionValidator is not None
    assert PositionFactory is not None
    assert PositionCollection is not None
    assert PositionStatistics is not None
    assert PositionAnalyzer is not None


def test_package_version():

    import ogs.market_data.position as module

    assert module.__version__ == "0.1.0"