"""
===========================================================

OGS Smart Money AI

Balanced Price Range Factory Tests

===========================================================
"""

from ogs.smart_money.bpr import (
    BalancedPriceRange,
    BalancedPriceRangeDirection,
    BalancedPriceRangeFactory,
)

from tests.factories import (
    make_bullish_fair_value_gap,
    make_bearish_fair_value_gap,
)


def test_create():

    bullish = make_bullish_fair_value_gap()
    bearish = make_bearish_fair_value_gap()

    bpr = BalancedPriceRangeFactory.create(
        bullish_gap=bullish,
        bearish_gap=bearish,
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert isinstance(bpr, BalancedPriceRange)

    assert bpr.bullish_gap == bullish
    assert bpr.bearish_gap == bearish

    assert bpr.direction == BalancedPriceRangeDirection.BULLISH

    assert bpr.top == 105
    assert bpr.bottom == 100
    assert bpr.midpoint == 102.5
    assert bpr.size == 5


def test_factory_returns_domain_object():

    bpr = BalancedPriceRangeFactory.create(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert type(bpr) is BalancedPriceRange