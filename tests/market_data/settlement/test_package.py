"""
Tests for Settlement package exports.
"""

from ogs.market_data.settlement import (
    __version__,
    Settlement,
    SettlementAnalyzer,
    SettlementCollection,
    SettlementFactory,
    SettlementStatistics,
    SettlementValidator,
    SettlementType,
    SettlementStatus,
    SettlementCycle,
    SettlementMethod,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Settlement is not None
    assert SettlementAnalyzer is not None
    assert SettlementCollection is not None
    assert SettlementFactory is not None
    assert SettlementStatistics is not None
    assert SettlementValidator is not None
    assert SettlementType is not None
    assert SettlementStatus is not None
    assert SettlementCycle is not None
    assert SettlementMethod is not None