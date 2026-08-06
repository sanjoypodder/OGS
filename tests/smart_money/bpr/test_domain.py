"""
===========================================================

OGS Smart Money AI

Balanced Price Range Domain Tests

===========================================================
"""

from ogs.smart_money.bpr import (
    BalancedPriceRange,
    BalancedPriceRangeDirection,
)

from tests.factories import (
    make_bullish_fair_value_gap,
    make_bearish_fair_value_gap,
)


def test_create_bpr():

    bullish = make_bullish_fair_value_gap()
    bearish = make_bearish_fair_value_gap()

    bpr = BalancedPriceRange(
        bullish_gap=bullish,
        bearish_gap=bearish,
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert bpr.bullish_gap == bullish
    assert bpr.bearish_gap == bearish
    assert bpr.top == 105
    assert bpr.bottom == 100
    assert bpr.midpoint == 102.5
    assert bpr.size == 5


def test_is_bullish():

    bpr = BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert bpr.is_bullish
    assert not bpr.is_bearish
    assert not bpr.is_neutral


def test_is_bearish():

    bpr = BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BEARISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert bpr.is_bearish
    assert not bpr.is_bullish
    assert not bpr.is_neutral


def test_is_neutral():

    bpr = BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.NEUTRAL,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert bpr.is_neutral
    assert not bpr.is_bullish
    assert not bpr.is_bearish