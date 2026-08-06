"""
===========================================================

OGS Smart Money AI

Order Block Validation Rules Tests

===========================================================
"""

from ogs.smart_money.order_block.validation import (
    OrderBlockRules,
)


def test_defaults():

    rules = OrderBlockRules()

    assert rules.minimum_displacement == 1.0
    assert rules.require_liquidity_sweep
    assert rules.require_fresh_block
    assert rules.require_mss