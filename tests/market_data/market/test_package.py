"""
Tests for Market package exports.
"""

from ogs.market_data.market import (
    __version__,
    Market,
    MarketAnalyzer,
    MarketCollection,
    MarketFactory,
    MarketStatistics,
    MarketStatus,
    MarketType,
    MarketValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Market is not None
    assert MarketAnalyzer is not None
    assert MarketCollection is not None
    assert MarketFactory is not None
    assert MarketStatistics is not None
    assert MarketValidator is not None
    assert MarketStatus is not None
    assert MarketType is not None