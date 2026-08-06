"""
===========================================================

OGS Smart Money AI

Swing Collection Tests

===========================================================
"""

from ogs.smart_money.swing import SwingSeries


def test_create_series(sample_swing):

    series = SwingSeries([sample_swing])

    assert len(series) == 1


def test_first(sample_swing):

    series = SwingSeries([sample_swing])

    assert series.first == sample_swing


def test_last(sample_swing):

    series = SwingSeries([sample_swing])

    assert series.last == sample_swing


def test_is_empty():

    series = SwingSeries([])

    assert series.is_empty is True


def test_not_empty(sample_swing):

    series = SwingSeries([sample_swing])

    assert series.is_empty is False


def test_append(sample_swing):

    series = SwingSeries([])

    series.append(sample_swing)

    assert len(series) == 1


def test_latest(sample_swing):

    series = SwingSeries([])

    series.append(sample_swing)
    series.append(sample_swing)

    latest = series.latest(1)

    assert len(latest) == 1


def test_iteration(sample_swing):

    series = SwingSeries([sample_swing])

    count = 0

    for _ in series:
        count += 1

    assert count == 1


def test_indexing(sample_swing):

    series = SwingSeries([sample_swing])

    assert series[0] == sample_swing