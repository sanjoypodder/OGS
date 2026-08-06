"""
===========================================================

OGS Smart Money AI

Balanced Price Range Collection Tests

===========================================================
"""

from ogs.smart_money.bpr import (
    BalancedPriceRange,
    BalancedPriceRangeDirection,
    BalancedPriceRangeSeries,
)

from tests.factories import (
    make_bullish_fair_value_gap,
    make_bearish_fair_value_gap,
)


def make_bpr():

    return BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=BalancedPriceRangeDirection.BULLISH,
        top=105,
        bottom=100,
        midpoint=102.5,
        size=5,
    )


def test_empty_collection():

    series = BalancedPriceRangeSeries()

    assert len(series) == 0
    assert series.is_empty


def test_append():

    series = BalancedPriceRangeSeries()

    bpr = make_bpr()

    series.append(bpr)

    assert len(series) == 1


def test_latest():

    series = BalancedPriceRangeSeries()

    bpr = make_bpr()

    series.append(bpr)

    assert series.latest(1) == [bpr]


def test_first():

    series = BalancedPriceRangeSeries()

    bpr = make_bpr()

    series.append(bpr)

    assert series.first == bpr


def test_last():

    series = BalancedPriceRangeSeries()

    bpr = make_bpr()

    series.append(bpr)

    assert series.last == bpr


def test_iteration():

    series = BalancedPriceRangeSeries()

    bpr = make_bpr()

    series.append(bpr)

    assert list(series) == [bpr]


def test_property():

    series = BalancedPriceRangeSeries()

    bpr = make_bpr()

    series.append(bpr)

    assert series.balanced_price_ranges == [bpr]