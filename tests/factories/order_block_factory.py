"""
===========================================================

OGS Smart Money AI

Order Block Test Factory

===========================================================
"""

from __future__ import annotations

from tests.factories import (
    make_bearish_candle,
    make_bullish_candle,
    make_bullish_mss,
    make_bearish_mss,
    make_buy_side_liquidity,
    make_equal_low,
)

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidity,
    SellSideLiquidityType,
)

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    SweepDirection,
    SweepStatus,
)

from ogs.smart_money.order_block import (
    OrderBlock,
    OrderBlockDirection,
    OrderBlockStatus,
)


def make_bullish_order_block():

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=make_bearish_candle(),
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    return OrderBlock(
        origin_candle=make_bearish_candle(),
        mss=make_bullish_mss(),
        liquidity_sweep=sweep,
        direction=OrderBlockDirection.BULLISH,
        status=OrderBlockStatus.ACTIVE,
    )


def make_bearish_order_block():

    sell_side = SellSideLiquidity(
        equal_low=make_equal_low(),
        liquidity_type=SellSideLiquidityType.ACTIVE,
    )

    sweep = LiquiditySweep(
        liquidity_pool=sell_side,
        sweep_candle=make_bullish_candle(),
        direction=SweepDirection.SELL_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    return OrderBlock(
        origin_candle=make_bullish_candle(),
        mss=make_bearish_mss(),
        liquidity_sweep=sweep,
        direction=OrderBlockDirection.BEARISH,
        status=OrderBlockStatus.ACTIVE,
    )