"""
BOS Collection Tests
"""

from ogs.smart_money.bos import BOSSeries


def test_create_series():

    series = BOSSeries([])

    assert len(series) == 0


def test_append(sample_bos):

    series = BOSSeries([])

    series.append(sample_bos)

    assert len(series) == 1


def test_first(sample_bos):

    series = BOSSeries([sample_bos])

    assert series.first == sample_bos


def test_last(sample_bos):

    series = BOSSeries([sample_bos])

    assert series.last == sample_bos


def test_latest(sample_bos):

    series = BOSSeries([sample_bos])

    assert len(series.latest(1)) == 1