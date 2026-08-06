"""
===========================================================

OGS Smart Money AI

Equal High Collection Tests

===========================================================
"""

from ogs.smart_money.liquidity.equal_highs import EqualHighSeries


def test_create_series():

    series = EqualHighSeries([])

    assert len(series) == 0


def test_append(sample_equal_high):

    series = EqualHighSeries([])

    series.append(sample_equal_high)

    assert len(series) == 1


def test_first(sample_equal_high):

    series = EqualHighSeries([sample_equal_high])

    assert series.first == sample_equal_high


def test_last(sample_equal_high):

    series = EqualHighSeries([sample_equal_high])

    assert series.last == sample_equal_high


def test_latest(sample_equal_high):

    series = EqualHighSeries([sample_equal_high])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == sample_equal_high


def test_is_empty():

    series = EqualHighSeries([])

    assert series.is_empty


def test_not_empty(sample_equal_high):

    series = EqualHighSeries([sample_equal_high])

    assert not series.is_empty


def test_iteration(sample_equal_high):

    series = EqualHighSeries([sample_equal_high])

    items = list(series)

    assert len(items) == 1
    assert items[0] == sample_equal_high


def test_indexing(sample_equal_high):

    series = EqualHighSeries([sample_equal_high])

    assert series[0] == sample_equal_high