"""
Tests for Symbol package.
"""

from ogs.market_data.symbol import (
    Symbol,
    SymbolAnalyzer,
    SymbolCollection,
    SymbolFactory,
    SymbolStatistics,
    SymbolValidator,
    SymbolType,
    Exchange,
    Currency,
    TradingStatus,
)


def test_package_imports():

    assert Symbol is not None
    assert SymbolAnalyzer is not None
    assert SymbolCollection is not None
    assert SymbolFactory is not None
    assert SymbolStatistics is not None
    assert SymbolValidator is not None
    assert SymbolType is not None
    assert Exchange is not None
    assert Currency is not None
    assert TradingStatus is not None