"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Package Tests

===========================================================
"""

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
    LiquiditySweepAnalyzer,
    LiquiditySweepSeries,
    LiquiditySweepStatistics,
    LiquiditySweepValidator,
    SweepDirection,
    SweepStatus,
)


def test_package_exports():

    assert LiquiditySweep is not None
    assert LiquiditySweepAnalyzer is not None
    assert LiquiditySweepSeries is not None
    assert LiquiditySweepValidator is not None
    assert LiquiditySweepStatistics is not None
    assert SweepDirection is not None
    assert SweepStatus is not None