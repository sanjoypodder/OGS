"""
===========================================================

OGS Smart Money AI

Equal High Package Tests

===========================================================
"""

from ogs.smart_money.liquidity.equal_highs import (
    EqualHigh,
    EqualHighDetector,
    EqualHighSeries,
    EqualHighStatistics,
    EqualHighType,
    EqualHighValidator,
)


def test_package_exports():

    assert EqualHigh is not None
    assert EqualHighType is not None
    assert EqualHighSeries is not None
    assert EqualHighDetector is not None
    assert EqualHighValidator is not None
    assert EqualHighStatistics is not None