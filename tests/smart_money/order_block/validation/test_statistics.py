"""
===========================================================

OGS Smart Money AI

Order Block Validation Statistics Tests

===========================================================
"""

from ogs.smart_money.order_block.validation import (
    OrderBlockValidationStatistics,
)


def test_statistics():

    stats = OrderBlockValidationStatistics(
        validated=12,
        rejected=3,
    )

    assert stats.validated == 12
    assert stats.rejected == 3
    assert stats.total == 15