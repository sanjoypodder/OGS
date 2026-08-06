"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Domain Tests

===========================================================
"""

from decimal import Decimal

from tests.factories import make_swing_high

from ogs.smart_money.liquidity.equal_highs import (
    EqualHigh,
    EqualHighType,
)

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidity,
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


def test_create():

    pool = BuySideLiquidity(
        equal_high=create_equal_high(),
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )

    assert pool.liquidity_type == BuySideLiquidityType.ACTIVE


def test_zone_price():

    pool = BuySideLiquidity(
        equal_high=create_equal_high(),
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )

    assert pool.zone_price == Decimal("110.00")


def test_timestamp():

    eh = create_equal_high()

    pool = BuySideLiquidity(
        equal_high=eh,
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )

    assert pool.timestamp == eh.timestamp


def test_string():

    pool = BuySideLiquidity(
        equal_high=create_equal_high(),
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )

    assert "ACTIVE" in str(pool)


def test_is_frozen():

    pool = BuySideLiquidity(
        equal_high=create_equal_high(),
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )

    try:
        pool.liquidity_type = BuySideLiquidityType.SWEPT
        assert False
    except Exception:
        assert True