"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Enum Tests

===========================================================
"""

from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidityType,
)


def test_active():

    assert (
        SellSideLiquidityType.ACTIVE.value
        == "ACTIVE"
    )


def test_swept():

    assert (
        SellSideLiquidityType.SWEPT.value
        == "SWEPT"
    )


def test_enum_count():

    assert len(SellSideLiquidityType) == 2