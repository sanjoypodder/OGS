"""
===========================================================

OGS Smart Money AI

Fair Value Gap Enum Tests

===========================================================
"""

from ogs.smart_money.fair_value_gap import (
    FairValueGapDirection,
)


def test_enum_values():

    assert (
        FairValueGapDirection.BULLISH.value
        == "Bullish"
    )

    assert (
        FairValueGapDirection.BEARISH.value
        == "Bearish"
    )


def test_enum_count():

    assert len(FairValueGapDirection) == 2