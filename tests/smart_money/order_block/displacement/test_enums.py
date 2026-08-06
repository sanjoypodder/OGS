"""
===========================================================

OGS Smart Money AI

Displacement Enum Tests

===========================================================
"""

from ogs.smart_money.order_block.displacement import (
    DisplacementDirection,
)


def test_direction():

    assert (
        DisplacementDirection.BULLISH.value
        == "BULLISH"
    )

    assert (
        DisplacementDirection.BEARISH.value
        == "BEARISH"
    )


def test_count():

    assert (
        len(DisplacementDirection)
        == 2
    )