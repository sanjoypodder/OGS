"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Statistics Tests

===========================================================
"""

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidityStatistics,
)


def test_statistics_creation():

    stats = BuySideLiquidityStatistics()

    assert stats is not None