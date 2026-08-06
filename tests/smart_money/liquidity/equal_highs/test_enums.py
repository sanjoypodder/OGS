"""
===========================================================

OGS Smart Money AI

Equal High Enum Tests

===========================================================
"""

from ogs.smart_money.liquidity.equal_highs import (
    EqualHighType,
)


def test_confirmed():

    assert (
        EqualHighType.CONFIRMED.value
        == "CONFIRMED"
    )


def test_developing():

    assert (
        EqualHighType.DEVELOPING.value
        == "DEVELOPING"
    )


def test_enum_count():

    assert len(EqualHighType) == 2