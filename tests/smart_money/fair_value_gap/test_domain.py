"""
===========================================================

OGS Smart Money AI

Fair Value Gap Domain Tests

===========================================================
"""

from tests.factories import (
    make_bullish_candle,
)

from ogs.smart_money.fair_value_gap import (
    FairValueGap,
    FairValueGapDirection,
)


def test_create_bullish():

    gap = FairValueGap(

        first=make_bullish_candle(index=0),

        middle=make_bullish_candle(index=1),

        last=make_bullish_candle(index=2),

        direction=FairValueGapDirection.BULLISH,

        top=120,

        bottom=100,

        midpoint=110,

        size=20,
    )

    assert gap.is_bullish
    assert not gap.is_bearish
    assert gap.top == 120
    assert gap.bottom == 100
    assert gap.midpoint == 110
    assert gap.size == 20
    assert not gap.is_filled
    assert gap.fill_timestamp is None


def test_create_bearish():

    gap = FairValueGap(

        first=make_bullish_candle(index=0),

        middle=make_bullish_candle(index=1),

        last=make_bullish_candle(index=2),

        direction=FairValueGapDirection.BEARISH,

        top=120,

        bottom=100,

        midpoint=110,

        size=20,
    )

    assert gap.is_bearish
    assert not gap.is_bullish