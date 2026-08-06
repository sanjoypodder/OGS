"""
Tests for Exchange package exports.
"""

from ogs.market_data.exchange import (
    __version__,
    Exchange,
    ExchangeAnalyzer,
    ExchangeCollection,
    ExchangeFactory,
    ExchangeStatistics,
    ExchangeStatus,
    ExchangeValidator,
    TradingSession,
)


def test_version():
    assert __version__ == "0.1.0"


def test_exports():
    assert Exchange is not None
    assert ExchangeAnalyzer is not None
    assert ExchangeCollection is not None
    assert ExchangeFactory is not None
    assert ExchangeStatistics is not None
    assert ExchangeValidator is not None
    assert ExchangeStatus is not None
    assert TradingSession is not None