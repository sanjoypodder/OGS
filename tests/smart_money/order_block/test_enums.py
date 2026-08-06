"""
===========================================================

OGS Smart Money AI

Order Block Enum Tests

===========================================================
"""

from ogs.smart_money.order_block import (
    OrderBlockDirection,
    OrderBlockStatus,
)


def test_direction():

    assert (
        OrderBlockDirection.BULLISH.value
        == "BULLISH"
    )

    assert (
        OrderBlockDirection.BEARISH.value
        == "BEARISH"
    )


def test_status():

    assert (
        OrderBlockStatus.ACTIVE.value
        == "ACTIVE"
    )

    assert (
        OrderBlockStatus.MITIGATED.value
        == "MITIGATED"
    )

    assert (
        OrderBlockStatus.INVALIDATED.value
        == "INVALIDATED"
    )


def test_counts():

    assert len(OrderBlockDirection) == 2

    assert len(OrderBlockStatus) == 3