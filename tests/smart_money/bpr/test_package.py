"""
===========================================================

OGS Smart Money AI

Balanced Price Range Package Tests

===========================================================
"""

from ogs.smart_money.bpr import (
    BalancedPriceRange,
    BalancedPriceRangeAnalyzer,
    BalancedPriceRangeDirection,
    BalancedPriceRangeFactory,
    BalancedPriceRangeSeries,
    BalancedPriceRangeStatistics,
    BalancedPriceRangeValidator,
)


def test_imports():

    assert BalancedPriceRange is not None
    assert BalancedPriceRangeAnalyzer is not None
    assert BalancedPriceRangeDirection is not None
    assert BalancedPriceRangeFactory is not None
    assert BalancedPriceRangeSeries is not None
    assert BalancedPriceRangeStatistics is not None
    assert BalancedPriceRangeValidator is not None