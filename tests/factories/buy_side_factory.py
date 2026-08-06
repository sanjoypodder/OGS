"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Factory

===========================================================
"""

from .equal_high_factory import make_equal_high

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidity,
    BuySideLiquidityType,
)


def make_buy_side_liquidity():

    return BuySideLiquidity(
        equal_high=make_equal_high(),
        liquidity_type=BuySideLiquidityType.ACTIVE,
    )

    