"""
Tests for Candle statistics.
"""

from datetime import datetime

from ogs.market_data.candle import (
    Candle,
    CandleSeries,
    CandleStatistics,
)


def candle(
    open_price,
    high,
    low,
    close,
    volume=100,
):

    return Candle(
        symbol="BTCUSD",
        timeframe="H1",
        timestamp=datetime.now(),
        open=open_price,
        high=high,
        low=low,
        close=close,
        volume=volume,
    )


def build_series():

    series = CandleSeries()

    series.append(candle(100, 120, 90, 110))
    series.append(candle(110, 125, 100, 105))
    series.append(candle(105, 130, 100, 105))

    return series


def test_count():

    stats = CandleStatistics(build_series())

    assert stats.count == 3


def test_direction_counts():

    stats = CandleStatistics(build_series())

    assert stats.bullish_count == 1
    assert stats.bearish_count == 1
    assert stats.doji_count == 1


def test_total_volume():

    stats = CandleStatistics(build_series())

    assert stats.total_volume == 300


def test_highest_price():

    stats = CandleStatistics(build_series())

    assert stats.highest_price == 130


def test_lowest_price():

    stats = CandleStatistics(build_series())

    assert stats.lowest_price == 90


def test_average_range():

    stats = CandleStatistics(build_series())

    expected = ((30 + 25 + 30) / 3)

    assert stats.average_range == expected


def test_average_body():

    stats = CandleStatistics(build_series())

    expected = ((10 + 5 + 0) / 3)

    assert stats.average_body == expected


def test_latest():

    stats = CandleStatistics(build_series())

    assert stats.latest.close == 105


def test_oldest():

    stats = CandleStatistics(build_series())

    assert stats.oldest.open == 100