"""
===========================================================

OGS Smart Money AI

MSS Collection Tests

===========================================================
"""

from ogs.smart_money.mss import MSSSeries


def test_create_series():

    series = MSSSeries([])

    assert len(series) == 0


def test_append(sample_mss):

    series = MSSSeries([])

    series.append(sample_mss)

    assert len(series) == 1


def test_first(sample_mss):

    series = MSSSeries([sample_mss])

    assert series.first == sample_mss


def test_last(sample_mss):

    series = MSSSeries([sample_mss])

    assert series.last == sample_mss


def test_latest(sample_mss):

    series = MSSSeries([sample_mss])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == sample_mss


def test_is_empty():

    series = MSSSeries([])

    assert series.is_empty


def test_not_empty(sample_mss):

    series = MSSSeries([sample_mss])

    assert not series.is_empty


def test_iteration(sample_mss):

    series = MSSSeries([sample_mss])

    items = list(series)

    assert len(items) == 1
    assert items[0] == sample_mss


def test_indexing(sample_mss):

    series = MSSSeries([sample_mss])

    assert series[0] == sample_mss