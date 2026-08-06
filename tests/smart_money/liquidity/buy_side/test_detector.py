"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Detector Tests

===========================================================
"""

from decimal import Decimal

from tests.factories import make_swing_high

from ogs.smart_money.liquidity.equal_highs import (
    EqualHigh,
    EqualHighSeries,
    EqualHighType,
)

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidityDetector,
    BuySideLiquidityType,
)


def create_equal_high():

    return EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )


def test_empty():

    detector = BuySideLiquidityDetector()

    result = detector.detect(
        EqualHighSeries([])
    )

    assert len(result) == 0


def test_single_equal_high():

    detector = BuySideLiquidityDetector()

    result = detector.detect(
        EqualHighSeries(
            [
                create_equal_high(),
            ]
        )
    )

    assert len(result) == 1

    pool = result.first

    assert pool.liquidity_type == BuySideLiquidityType.ACTIVE
    assert pool.equal_high.zone_price == Decimal("110.00")


def test_multiple_equal_highs():

    detector = BuySideLiquidityDetector()

    result = detector.detect(
        EqualHighSeries(
            [
                create_equal_high(),
                create_equal_high(),
                create_equal_high(),
            ]
        )
    )

    assert len(result) == 3

def test_none():

    detector = BuySideLiquidityDetector()

    result = detector.detect(None)

    assert len(result) == 0

from tests.factories import make_equal_high


def test_preserve_reference():

    detector = BuySideLiquidityDetector()

    zone = make_equal_high()

    result = detector.detect(
        EqualHighSeries([zone])
    )

    assert result.first.equal_high is zone

def test_order_preserved():

    detector = BuySideLiquidityDetector()

    first = make_equal_high()
    second = make_equal_high()

    result = detector.detect(
        EqualHighSeries(
            [
                first,
                second,
            ]
        )
    )

    assert result[0].equal_high is first
    assert result[1].equal_high is second

def test_active_status():

    detector = BuySideLiquidityDetector()

    result = detector.detect(
        EqualHighSeries(
            [
                make_equal_high(),
            ]
        )
    )

    assert (
        result.first.liquidity_type
        == BuySideLiquidityType.ACTIVE
    )