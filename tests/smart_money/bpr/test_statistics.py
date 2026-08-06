"""
===========================================================

OGS Smart Money AI

Balanced Price Range Statistics Tests

===========================================================
"""

from ogs.smart_money.bpr import (
    BalancedPriceRange,
    BalancedPriceRangeDirection,
    BalancedPriceRangeSeries,
    BalancedPriceRangeStatistics,
)

from tests.factories import (
    make_bullish_fair_value_gap,
    make_bearish_fair_value_gap,
)


def make_bpr(direction, size):

    return BalancedPriceRange(
        bullish_gap=make_bullish_fair_value_gap(),
        bearish_gap=make_bearish_fair_value_gap(),
        direction=direction,
        top=100 + size,
        bottom=100,
        midpoint=100 + size / 2,
        size=size,
    )


def make_series():

    series = BalancedPriceRangeSeries()

    series.append(make_bpr(BalancedPriceRangeDirection.BULLISH, 5))
    series.append(make_bpr(BalancedPriceRangeDirection.BEARISH, 10))
    series.append(make_bpr(BalancedPriceRangeDirection.NEUTRAL, 20))

    return series


def test_count():

    stats = BalancedPriceRangeStatistics(make_series())

    assert stats.count == 3


def test_bullish_count():

    stats = BalancedPriceRangeStatistics(make_series())

    assert stats.bullish_count == 1


def test_bearish_count():

    stats = BalancedPriceRangeStatistics(make_series())

    assert stats.bearish_count == 1


def test_neutral_count():

    stats = BalancedPriceRangeStatistics(make_series())

    assert stats.neutral_count == 1


def test_average_size():

    stats = BalancedPriceRangeStatistics(make_series())

    assert stats.average_size == (5 + 10 + 20) / 3


def test_largest():

    stats = BalancedPriceRangeStatistics(make_series())

    assert stats.largest.size == 20


def test_smallest():

    stats = BalancedPriceRangeStatistics(make_series())

    assert stats.smallest.size == 5