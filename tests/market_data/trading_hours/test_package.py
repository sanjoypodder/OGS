"""
Tests for TradingHours package exports.
"""

from ogs.market_data.trading_hours import (
    __version__,
    TradingHours,
    TradingHoursAnalyzer,
    TradingHoursCollection,
    TradingHoursFactory,
    TradingHoursStatistics,
    TradingHoursStatus,
    TradingHoursType,
    TradingHoursValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert TradingHours is not None
    assert TradingHoursAnalyzer is not None
    assert TradingHoursCollection is not None
    assert TradingHoursFactory is not None
    assert TradingHoursStatistics is not None
    assert TradingHoursValidator is not None
    assert TradingHoursType is not None
    assert TradingHoursStatus is not None