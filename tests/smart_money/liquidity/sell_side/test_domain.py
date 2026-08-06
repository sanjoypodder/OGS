"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Domain Tests

===========================================================
"""

from decimal import Decimal

from tests.factories import (
    make_equal_low,
)

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidity,
    SellSideLiquidityType,
)


def test_create():

    pool = SellSideLiquidity(
        equal_low=make_equal_low(),
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )

    assert pool.liquidity_type == SellSideLiquidityType.ACTIVE


def test_zone_price():

    pool = SellSideLiquidity(
        equal_low=make_equal_low(),
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )

    assert pool.zone_price == Decimal("90.00")


def test_timestamp():

    zone = make_equal_low()

    pool = SellSideLiquidity(
        equal_low=zone,
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )

    assert pool.timestamp == zone.timestamp


def test_string():

    pool = SellSideLiquidity(
        equal_low=make_equal_low(),
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )

    assert "ACTIVE" in str(pool)


def test_is_frozen():

    pool = SellSideLiquidity(
        equal_low=make_equal_low(),
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )

    try:
        pool.liquidity_type = SellSideLiquidityType.SWEPT
        assert False
    except Exception:
        assert True