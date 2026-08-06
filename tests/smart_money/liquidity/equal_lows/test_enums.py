"""
===========================================================

OGS Smart Money AI

Equal Low Enum Tests

===========================================================
"""

from ogs.smart_money.liquidity.equal_lows import (
    EqualLowType,
)


def test_confirmed():

    assert (
        EqualLowType.CONFIRMED.value
        == "CONFIRMED"
    )


def test_developing():

    assert (
        EqualLowType.DEVELOPING.value
        == "DEVELOPING"
    )


def test_enum_count():

    assert len(EqualLowType) == 2