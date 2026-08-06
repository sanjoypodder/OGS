"""
===========================================================

OGS Smart Money AI

Balanced Price Range Validator Tests

===========================================================
"""

from ogs.smart_money.bpr import (
    BalancedPriceRange,
    BalancedPriceRangeDirection,
    BalancedPriceRangeValidator,
)

from tests.factories import (
    make_bullish_fair_value_gap,
    make_bearish_fair_value_gap,
)


def make_valid_bpr():

    return BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )


validator = BalancedPriceRangeValidator()


def test_valid():

    assert validator.validate(make_valid_bpr())


def test_missing_bullish_gap():

    bpr = BalancedPriceRange(
        bullish_gap=None,
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert not validator.validate(bpr)


def test_missing_bearish_gap():

    bpr = BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=None,
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert not validator.validate(bpr)


def test_missing_direction():

    bpr = BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=None,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )

    assert not validator.validate(bpr)


def test_invalid_price_range():

    bpr = BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BULLISH,
        top=100,
        bottom=105,
        midpoint=102.5,
        size=5,
    )

    assert not validator.validate(bpr)


def test_invalid_size():

    bpr = BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=-1,
    )

    assert not validator.validate(bpr)