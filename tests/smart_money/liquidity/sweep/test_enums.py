"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Enum Tests

===========================================================
"""

from ogs.smart_money.liquidity.sweep import (
    SweepDirection,
    SweepStatus,
)


def test_buy_side():

    assert SweepDirection.BUY_SIDE.value == "BUY_SIDE"


def test_sell_side():

    assert SweepDirection.SELL_SIDE.value == "SELL_SIDE"


def test_confirmed():

    assert SweepStatus.CONFIRMED.value == "CONFIRMED"


def test_pending():

    assert SweepStatus.PENDING.value == "PENDING"


def test_direction_count():

    assert len(SweepDirection) == 2


def test_status_count():

    assert len(SweepStatus) == 2