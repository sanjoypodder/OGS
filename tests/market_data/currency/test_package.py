"""
Tests for Currency package exports.
"""

from ogs.market_data.currency import (
    __version__,
    Currency,
    CurrencyAnalyzer,
    CurrencyCollection,
    CurrencyFactory,
    CurrencyStatistics,
    CurrencyStatus,
    CurrencyType,
    CurrencyValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Currency is not None
    assert CurrencyAnalyzer is not None
    assert CurrencyCollection is not None
    assert CurrencyFactory is not None
    assert CurrencyStatistics is not None
    assert CurrencyValidator is not None
    assert CurrencyType is not None
    assert CurrencyStatus is not None