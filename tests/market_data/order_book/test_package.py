"""
Package tests for OrderBook module.
"""

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookAnalyzer,
    OrderBookCollection,
    OrderBookFactory,
    OrderBookStatistics,
    OrderBookStatus,
    OrderBookType,
    OrderBookValidator,
)


def test_package_imports():

    assert OrderBook is not None
    assert OrderBookType is not None
    assert OrderBookStatus is not None
    assert OrderBookValidator is not None
    assert OrderBookFactory is not None
    assert OrderBookCollection is not None
    assert OrderBookStatistics is not None
    assert OrderBookAnalyzer is not None


def test_package_version():

    import ogs.market_data.order_book as module

    assert module.__version__ == "0.1.0"