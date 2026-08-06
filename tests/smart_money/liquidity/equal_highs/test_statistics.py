"""
===========================================================

OGS Smart Money AI

Equal High Statistics Tests

===========================================================
"""

from ogs.smart_money.liquidity.equal_highs import (
    EqualHighStatistics,
)


def test_statistics_creation():

    stats = EqualHighStatistics()

    assert stats is not None