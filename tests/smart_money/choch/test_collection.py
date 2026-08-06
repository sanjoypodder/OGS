"""
===========================================================

OGS Smart Money AI

CHOCH Collection Tests

===========================================================
"""

from ogs.smart_money.choch import CHOCHSeries


def test_create_series():

    series = CHOCHSeries([])

    assert len(series) == 0


def test_append(sample_choch):

    series = CHOCHSeries([])

    series.append(sample_choch)

    assert len(series) == 1


def test_first(sample_choch):

    series = CHOCHSeries([sample_choch])

    assert series.first == sample_choch


def test_last(sample_choch):

    series = CHOCHSeries([sample_choch])

    assert series.last == sample_choch


def test_latest(sample_choch):

    series = CHOCHSeries([sample_choch])

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == sample_choch


def test_is_empty():

    series = CHOCHSeries([])

    assert series.is_empty


def test_not_empty(sample_choch):

    series = CHOCHSeries([sample_choch])

    assert not series.is_empty


def test_iteration(sample_choch):

    series = CHOCHSeries([sample_choch])

    items = list(series)

    assert len(items) == 1
    assert items[0] == sample_choch


def test_indexing(sample_choch):

    series = CHOCHSeries([sample_choch])

    assert series[0] == sample_choch