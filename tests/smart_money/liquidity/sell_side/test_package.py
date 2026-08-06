"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Package Tests

===========================================================
"""

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidity,
    SellSideLiquidityDetector,
    SellSideLiquiditySeries,
    SellSideLiquidityStatistics,
    SellSideLiquidityType,
    SellSideLiquidityValidator,
)


def test_package_exports():

    assert SellSideLiquidity is not None
    assert SellSideLiquidityType is not None
    assert SellSideLiquiditySeries is not None
    assert SellSideLiquidityDetector is not None
    assert SellSideLiquidityValidator is not None
    assert SellSideLiquidityStatistics is not None