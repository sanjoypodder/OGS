"""
===========================================================

OGS Smart Money AI

Market Structure Collection Tests

===========================================================
"""

from __future__ import annotations

import pytest

from ogs.market_structure import SwingSeries

from tests.fixtures import SwingFactory


# ==========================================================
# Construction
# ==========================================================

def test_empty_collection():

    series = SwingSeries()

    assert len(series) == 0


def test_create_with_items():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    assert len(series) == len(swings)

    assert list(series) == swings


# ==========================================================
# Append
# ==========================================================

def test_append_single_swing():

    series = SwingSeries()

    swing = SwingFactory.high()

    series.append(swing)

    assert len(series) == 1
    assert series[0] == swing


def test_append_multiple_swings():

    series = SwingSeries()

    swings = SwingFactory.sequence()

    for swing in swings:
        series.append(swing)

    assert len(series) == len(swings)

    assert list(series) == swings


# ==========================================================
# Latest
# ==========================================================

def test_latest_default():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    latest = series.latest()

    assert latest == [swings[-1]]


@pytest.mark.parametrize("count", [1, 2, 3, 4, 5, 6])
def test_latest_count(count):

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    assert series.latest(count) == swings[-count:]


def test_latest_more_than_length():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    assert series.latest(100) == swings


def test_latest_empty():

    series = SwingSeries()

    assert series.latest() == []


# ==========================================================
# Iteration
# ==========================================================

def test_iteration():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    collected = []

    for swing in series:
        collected.append(swing)

    assert collected == swings


# ==========================================================
# Indexing
# ==========================================================

def test_index_access():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    assert series[0] == swings[0]
    assert series[1] == swings[1]
    assert series[-1] == swings[-1]


# ==========================================================
# Membership
# ==========================================================

def test_contains():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    assert swings[0] in series
    assert swings[-1] in series


# ==========================================================
# Length
# ==========================================================

def test_length_after_append():

    series = SwingSeries()

    assert len(series) == 0

    series.append(SwingFactory.high())
    assert len(series) == 1

    series.append(SwingFactory.low())
    assert len(series) == 2


# ==========================================================
# List Conversion
# ==========================================================

def test_list_conversion():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    assert list(series) == swings


# ==========================================================
# Latest Returns New List
# ==========================================================

def test_latest_returns_new_list():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    latest = series.latest(2)

    latest.pop()

    assert len(series) == len(swings)
    assert len(series.latest(2)) == 2


# ==========================================================
# Duplicate Swings
# ==========================================================

def test_duplicate_swings_allowed():

    swing = SwingFactory.high()

    series = SwingSeries()

    series.append(swing)
    series.append(swing)

    assert len(series) == 2

    assert series[0] == swing
    assert series[1] == swing


# ==========================================================
# Slice Behaviour
# ==========================================================

def test_slice():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    assert series[:3] == swings[:3]
    assert series[2:5] == swings[2:5]


# ==========================================================
# Empty Iteration
# ==========================================================

def test_empty_iteration():

    series = SwingSeries()

    assert list(series) == []


# ==========================================================
# Latest Zero
# ==========================================================

def test_latest_zero():

    swings = SwingFactory.sequence()

    series = SwingSeries(swings)

    # Current implementation follows Python slicing semantics:
    # list[-0:] == list[0:] -> entire list
    assert series.latest(0) == swings


# ==========================================================
# Smoke Test
# ==========================================================

def test_collection_smoke():

    series = SwingSeries()

    series.append(SwingFactory.low())
    series.append(SwingFactory.high())

    assert len(series) == 2

    assert series.latest()[-1] == series[-1]