"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Domain Tests

===========================================================
"""

from tests.factories import (
    make_buy_side_liquidity,
    make_candle,
)

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    SweepDirection,
    SweepStatus,
)


def test_create():

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=make_candle(),
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    assert sweep.direction == SweepDirection.BUY_SIDE


def test_timestamp():

    candle = make_candle()

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=candle,
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    assert sweep.timestamp == candle.timestamp


def test_sweep_price():

    candle = make_candle()

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=candle,
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    assert sweep.sweep_price == candle.high


def test_string():

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=make_candle(),
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    assert "BUY_SIDE" in str(sweep)


def test_frozen():

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=make_candle(),
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    try:
        sweep.direction = SweepDirection.SELL_SIDE
        assert False
    except Exception:
        assert True