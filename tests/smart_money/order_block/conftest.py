"""
===========================================================

OGS Smart Money AI

Order Block Fixtures

===========================================================
"""

import pytest

from tests.factories import (
    make_bullish_choch,
    make_bearish_candle,
    make_buy_side_liquidity,
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


@pytest.fixture
def sample_order_block():

    sweep = LiquiditySweep(
        liquidity_pool=make_buy_side_liquidity(),
        sweep_candle=make_bearish_candle(),
        direction=SweepDirection.BUY_SIDE,
        status=SweepStatus.CONFIRMED,
    )

    return OrderBlock(
        origin_candle=make_bearish_candle(),
        mss=make_bullish_choch(),   # temporary placeholder
        liquidity_sweep=sweep,
        direction=OrderBlockDirection.BULLISH,
        status=OrderBlockStatus.ACTIVE,
    )