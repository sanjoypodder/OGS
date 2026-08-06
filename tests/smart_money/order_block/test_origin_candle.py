"""
===========================================================

OGS Smart Money AI

Order Block Origin Candle Tests

===========================================================
"""

from ogs.engine import Analysis
from ogs.market import CandleSeries

from ogs.smart_money.order_block import (
    OrderBlockAnalyzer,
)

from tests.factories import (
    make_bearish_candle,
    make_bullish_candle,
    make_bullish_mss,
)


def test_last_bearish_before_mss():

    analyzer = OrderBlockAnalyzer()

    candles = CandleSeries(
        [
            make_bullish_candle(index=1),
            make_bearish_candle(index=2),
            make_bullish_candle(index=3),
            make_bearish_candle(index=4),
            make_bullish_candle(index=5),
        ]
    )

    mss = make_bullish_mss(index=6)

    candle = analyzer._find_last_bearish_candle(
        candles,
        mss.timestamp,
    )

    assert candle is not None
    assert candle.timestamp == make_bearish_candle(index=4).timestamp


def test_no_bearish_candle():

    analyzer = OrderBlockAnalyzer()

    candles = CandleSeries(
        [
            make_bullish_candle(index=1),
            make_bullish_candle(index=2),
            make_bullish_candle(index=3),
        ]
    )

    mss = make_bullish_mss(index=4)

    candle = analyzer._find_last_bearish_candle(
        candles,
        mss.timestamp,
    )

    assert candle is None