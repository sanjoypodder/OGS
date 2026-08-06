"""
===========================================================

OGS Smart Money AI

Order Block Statistics Tests

===========================================================
"""

from ogs.smart_money.order_block import (
    OrderBlockStatistics,
)


def test_statistics():

    stats = OrderBlockStatistics()

    assert stats is not None