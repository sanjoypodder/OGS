"""
===========================================================

OGS Smart Money AI

Equal Low Statistics Tests

===========================================================
"""

from ogs.smart_money.liquidity.equal_lows import (
    EqualLowStatistics,
)


def test_statistics_creation():

    stats = EqualLowStatistics()

    assert stats is not None