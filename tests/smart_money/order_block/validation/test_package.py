"""
===========================================================

OGS Smart Money AI

Validation Package Tests

===========================================================
"""

from ogs.smart_money.order_block.validation import (
    OrderBlockCandidateValidator,
    OrderBlockRules,
    OrderBlockValidationStatistics,
)


def test_exports():

    assert OrderBlockCandidateValidator is not None
    assert OrderBlockRules is not None
    assert OrderBlockValidationStatistics is not None