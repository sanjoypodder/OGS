"""
===========================================================

OGS Smart Money AI

Market Structure Statistics Tests

===========================================================
"""

from __future__ import annotations

from ogs.market_structure import (
    SwingSeries,
    SwingStatistics,
)

from tests.fixtures import SwingFactory


# ==========================================================
# Empty Statistics
# ==========================================================

def test_empty_statistics():

    stats = SwingStatistics(SwingSeries())

    assert stats.count == 0

    assert stats.high_count == 0
    assert stats.low_count == 0

    assert stats.higher_high_count == 0
    assert stats.higher_low_count == 0
    assert stats.lower_high_count == 0
    assert stats.lower_low_count == 0

    assert stats.strong_count == 0
    assert stats.normal_count == 0
    assert stats.weak_count == 0

    assert stats.latest is None
    assert stats.oldest is None


# ==========================================================
# Count
# ==========================================================

def test_count():

    swings = SwingFactory.sequence()

    stats = SwingStatistics(SwingSeries(swings))

    assert stats.count == len(swings)


# ==========================================================
# High / Low
# ==========================================================

def test_high_low_count():

    swings = [
        SwingFactory.high(),
        SwingFactory.low(),
        SwingFactory.higher_high(),
        SwingFactory.higher_low(),
        SwingFactory.lower_high(),
        SwingFactory.lower_low(),
    ]

    stats = SwingStatistics(SwingSeries(swings))

    assert stats.high_count == 3
    assert stats.low_count == 3


# ==========================================================
# Swing Type Counts
# ==========================================================

def test_higher_high_count():

    stats = SwingStatistics(
        SwingSeries(
            [
                SwingFactory.higher_high(),
                SwingFactory.higher_high(),
                SwingFactory.low(),
            ]
        )
    )

    assert stats.higher_high_count == 2


def test_higher_low_count():

    stats = SwingStatistics(
        SwingSeries(
            [
                SwingFactory.higher_low(),
                SwingFactory.higher_low(),
                SwingFactory.high(),
            ]
        )
    )

    assert stats.higher_low_count == 2


def test_lower_high_count():

    stats = SwingStatistics(
        SwingSeries(
            [
                SwingFactory.lower_high(),
                SwingFactory.lower_high(),
                SwingFactory.low(),
            ]
        )
    )

    assert stats.lower_high_count == 2


def test_lower_low_count():

    stats = SwingStatistics(
        SwingSeries(
            [
                SwingFactory.lower_low(),
                SwingFactory.lower_low(),
                SwingFactory.high(),
            ]
        )
    )

    assert stats.lower_low_count == 2


# ==========================================================
# Strength Counts
# ==========================================================

def test_strength_counts():

    swings = [
        SwingFactory.strong_high(),
        SwingFactory.strong_low(),
        SwingFactory.weak_high(),
        SwingFactory.weak_low(),
        SwingFactory.high(),
        SwingFactory.low(),
    ]

    stats = SwingStatistics(SwingSeries(swings))

    assert stats.strong_count == 2
    assert stats.normal_count == 2
    assert stats.weak_count == 2


# ==========================================================
# Latest / Oldest
# ==========================================================

def test_latest():

    swings = SwingFactory.sequence()

    stats = SwingStatistics(SwingSeries(swings))

    assert stats.latest == swings[-1]


def test_oldest():

    swings = SwingFactory.sequence()

    stats = SwingStatistics(SwingSeries(swings))

    assert stats.oldest == swings[0]


# ==========================================================
# Single Swing
# ==========================================================

def test_single_swing():

    swing = SwingFactory.high()

    stats = SwingStatistics(SwingSeries([swing]))

    assert stats.count == 1

    assert stats.latest == swing
    assert stats.oldest == swing

    assert stats.high_count == 1
    assert stats.low_count == 0


# ==========================================================
# Mixed Dataset
# ==========================================================

def test_mixed_dataset():

    swings = [
        SwingFactory.high(),
        SwingFactory.low(),
        SwingFactory.higher_high(),
        SwingFactory.higher_low(),
        SwingFactory.lower_high(),
        SwingFactory.lower_low(),
        SwingFactory.strong_high(),
        SwingFactory.weak_low(),
    ]

    stats = SwingStatistics(SwingSeries(swings))

    assert stats.count == 8

    assert stats.high_count == 4
    assert stats.low_count == 4

    assert stats.higher_high_count == 1
    assert stats.higher_low_count == 1
    assert stats.lower_high_count == 1
    assert stats.lower_low_count == 1

    assert stats.strong_count == 1
    assert stats.weak_count == 1
    assert stats.normal_count == 6


# ==========================================================
# Smoke Test
# ==========================================================

def test_statistics_smoke():

    stats = SwingStatistics(
        SwingSeries(SwingFactory.sequence())
    )

    assert stats.count > 0

    assert stats.latest is not None
    assert stats.oldest is not None