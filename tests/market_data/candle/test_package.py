"""
Tests for Candle package.
"""

from ogs.market_data.candle import (
    Candle,
    CandleAnalyzer,
    CandleDirection,
    CandleFactory,
    CandleSeries,
    CandleSource,
    CandleStatistics,
    CandleStatus,
    CandleValidator,
    PriceType,
    VolumeType,
)


def test_package_imports():

    assert Candle is not None
    assert CandleAnalyzer is not None
    assert CandleFactory is not None
    assert CandleValidator is not None
    assert CandleSeries is not None
    assert CandleStatistics is not None

    assert CandleDirection is not None
    assert CandleSource is not None
    assert CandleStatus is not None
    assert PriceType is not None
    assert VolumeType is not None