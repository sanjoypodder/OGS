"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Detector Tests

===========================================================
"""

from tests.factories import (
    make_equal_low,
)

from ogs.smart_money.liquidity.equal_lows import (
    EqualLowSeries,
)

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidityDetector,
    SellSideLiquidityType,
)


def test_empty():

    detector = SellSideLiquidityDetector()

    result = detector.detect(
        EqualLowSeries([])
    )

    assert len(result) == 0


def test_none():

    detector = SellSideLiquidityDetector()

    result = detector.detect(None)

    assert len(result) == 0


def test_single_equal_low():

    detector = SellSideLiquidityDetector()

    result = detector.detect(
        EqualLowSeries(
            [
                make_equal_low(),
            ]
        )
    )

    assert len(result) == 1

    pool = result.first

    assert pool.liquidity_type == SellSideLiquidityType.ACTIVE
    assert pool.equal_low.zone_price == make_equal_low().zone_price


def test_multiple_equal_lows():

    detector = SellSideLiquidityDetector()

    result = detector.detect(
        EqualLowSeries(
            [
                make_equal_low(),
                make_equal_low(),
                make_equal_low(),
            ]
        )
    )

    assert len(result) == 3


def test_preserve_reference():

    detector = SellSideLiquidityDetector()

    zone = make_equal_low()

    result = detector.detect(
        EqualLowSeries([zone])
    )

    assert result.first.equal_low is zone


def test_order_preserved():

    detector = SellSideLiquidityDetector()

    first = make_equal_low()
    second = make_equal_low()

    result = detector.detect(
        EqualLowSeries(
            [
                first,
                second,
            ]
        )
    )

    assert result[0].equal_low is first
    assert result[1].equal_low is second


def test_active_status():

    detector = SellSideLiquidityDetector()

    result = detector.detect(
        EqualLowSeries(
            [
                make_equal_low(),
            ]
        )
    )

    assert (
        result.first.liquidity_type
        == SellSideLiquidityType.ACTIVE
    )