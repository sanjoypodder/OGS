"""
===========================================================

OGS Smart Money AI

Order Block Package Tests

===========================================================
"""

from ogs.smart_money.order_block import (
    OrderBlock,
    OrderBlockAnalyzer,
    OrderBlockDirection,
    OrderBlockSeries,
    OrderBlockStatistics,
    OrderBlockStatus,
    OrderBlockValidator,
)


def test_package_exports():

    assert OrderBlock is not None
    assert OrderBlockAnalyzer is not None
    assert OrderBlockSeries is not None
    assert OrderBlockValidator is not None
    assert OrderBlockStatistics is not None
    assert OrderBlockDirection is not None
    assert OrderBlockStatus is not None