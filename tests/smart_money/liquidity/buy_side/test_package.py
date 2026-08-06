"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Package Tests

===========================================================
"""

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidity,
    BuySideLiquidityDetector,
    BuySideLiquiditySeries,
    BuySideLiquidityStatistics,
    BuySideLiquidityType,
    BuySideLiquidityValidator,
)


def test_package_exports():

    assert BuySideLiquidity is not None
    assert BuySideLiquidityType is not None
    assert BuySideLiquiditySeries is not None
    assert BuySideLiquidityDetector is not None
    assert BuySideLiquidityValidator is not None
    assert BuySideLiquidityStatistics is not None