"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Enum Tests

===========================================================
"""

from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidityType,
)


def test_active():

    assert (
        BuySideLiquidityType.ACTIVE.value
        == "ACTIVE"
    )


def test_swept():

    assert (
        BuySideLiquidityType.SWEPT.value
        == "SWEPT"
    )


def test_enum_count():

    assert len(BuySideLiquidityType) == 2