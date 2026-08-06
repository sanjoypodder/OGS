"""
Tests for Contract package exports.
"""

from ogs.market_data.contract import (
    __version__,
    Contract,
    ContractAnalyzer,
    ContractCollection,
    ContractFactory,
    ContractStatistics,
    ContractStatus,
    ContractType,
    ContractValidator,
    ExerciseStyle,
    OptionType,
    SettlementType,
)


def test_version():
    assert __version__ == "0.1.0"


def test_exports():
    assert Contract is not None
    assert ContractAnalyzer is not None
    assert ContractCollection is not None
    assert ContractFactory is not None
    assert ContractStatistics is not None
    assert ContractValidator is not None
    assert ContractType is not None
    assert OptionType is not None
    assert SettlementType is not None
    assert ExerciseStyle is not None
    assert ContractStatus is not None