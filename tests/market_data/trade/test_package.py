"""
Package tests for Trade module.
"""

from ogs.market_data.trade import (
    Trade,
    TradeAnalyzer,
    TradeCollection,
    TradeFactory,
    TradeSide,
    TradeStatistics,
    TradeStatus,
    TradeValidator,
)


def test_package_imports():

    assert Trade is not None
    assert TradeSide is not None
    assert TradeStatus is not None
    assert TradeValidator is not None
    assert TradeFactory is not None
    assert TradeCollection is not None
    assert TradeStatistics is not None
    assert TradeAnalyzer is not None


def test_package_version():

    import ogs.market_data.trade as module

    assert module.__version__ == "0.1.0"