"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Statistics Tests

===========================================================
"""

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidityStatistics,
)


def test_statistics_creation():

    stats = SellSideLiquidityStatistics()

    assert stats is not None