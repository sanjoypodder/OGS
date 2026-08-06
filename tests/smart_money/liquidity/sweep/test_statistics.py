"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Statistics Tests

===========================================================
"""

from ogs.smart_money.liquidity.sweep import (
    LiquiditySweepStatistics,
)


def test_statistics_creation():

    stats = LiquiditySweepStatistics()

    assert stats is not None