"""
Tests for Screener package exports.
"""

from ogs.market_data.screener import (
    __version__,
    Screener,
    ScreenerAnalyzer,
    ScreenerCollection,
    ScreenerFactory,
    ScreenerStatistics,
    ScreenerStatus,
    ScreenerType,
    ScreenerValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Screener is not None
    assert ScreenerAnalyzer is not None
    assert ScreenerCollection is not None
    assert ScreenerFactory is not None
    assert ScreenerStatistics is not None
    assert ScreenerValidator is not None
    assert ScreenerType is not None
    assert ScreenerStatus is not None