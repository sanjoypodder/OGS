"""
===========================================================

OGS Smart Money AI

Equal Low Collection Tests

===========================================================
"""

from ogs.smart_money.liquidity.equal_lows import EqualLowSeries


def test_create_series():

    series = EqualLowSeries([])

    assert len(series) == 0


def test_append(sample_equal_low):

    series = EqualLowSeries([])

    series.append(sample_equal_low)

    assert len(series) == 1


def test_first(sample_equal_low):

    series = EqualLowSeries([sample_equal_low])

    assert series.first == sample_equal_low


def test_last(sample_equal_low):

    series = EqualLowSeries([sample_equal_low])

    assert series.last == sample_equal_low


def test_latest(sample_equal_low):

    series = EqualLowSeries([sample_equal_low])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == sample_equal_low


def test_is_empty():

    series = EqualLowSeries([])

    assert series.is_empty


def test_not_empty(sample_equal_low):

    series = EqualLowSeries([sample_equal_low])

    assert not series.is_empty


def test_iteration(sample_equal_low):

    series = EqualLowSeries([sample_equal_low])

    items = list(series)

    assert len(items) == 1
    assert items[0] == sample_equal_low


def test_indexing(sample_equal_low):

    series = EqualLowSeries([sample_equal_low])

    assert series[0] == sample_equal_low