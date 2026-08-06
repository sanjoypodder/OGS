"""
===========================================================

OGS Smart Money AI

Market Structure Analyzer

Pivot Detection Tests

===========================================================
"""

from __future__ import annotations

from ogs.market_structure import MarketStructureAnalyzer

from tests.fixtures import CandleFactory


# ==========================================================
# Helpers
# ==========================================================

def make_candles(highs, lows):
    """
    Build valid candles from high/low arrays.

    Ensures:

        High >= Open
        High >= Close
        Low <= Open
        Low <= Close
    """

    candles = []

    for h, l in zip(highs, lows):

        candles.append(

            CandleFactory.create(

                open=l + 1,
                high=h,
                low=l,
                close=h - 1,

            )

        )

    return candles


# ==========================================================
# Pivot High
# ==========================================================

def test_valid_pivot_high():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[10, 20, 50, 20, 10],
        lows=[1, 2, 3, 2, 1],

    )

    assert analyzer._is_pivot_high(candles, 2)


def test_not_pivot_high_left_higher():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[60, 20, 50, 20, 10],
        lows=[1, 2, 3, 2, 1],

    )

    assert not analyzer._is_pivot_high(candles, 2)


def test_not_pivot_high_right_higher():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[10, 20, 50, 60, 10],
        lows=[1, 2, 3, 2, 1],

    )

    assert not analyzer._is_pivot_high(candles, 2)


def test_equal_high_not_pivot():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[10, 50, 50, 20, 10],
        lows=[1, 2, 3, 2, 1],

    )

    assert not analyzer._is_pivot_high(candles, 2)


# ==========================================================
# Pivot Low
# ==========================================================

def test_valid_pivot_low():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[30, 30, 30, 30, 30],
        lows=[20, 10, 1, 10, 20],

    )

    assert analyzer._is_pivot_low(candles, 2)


def test_not_pivot_low_left_lower():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[30] * 5,
        lows=[0, 10, 1, 10, 20],

    )

    assert not analyzer._is_pivot_low(candles, 2)


def test_not_pivot_low_right_lower():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[30] * 5,
        lows=[20, 10, 1, 0, 20],

    )

    assert not analyzer._is_pivot_low(candles, 2)


def test_equal_low_not_pivot():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(

        highs=[30] * 5,
        lows=[20, 1, 1, 10, 20],

    )

    assert not analyzer._is_pivot_low(candles, 2)


# ==========================================================
# Different Pivot Depths
# ==========================================================

def test_depth_one():

    analyzer = MarketStructureAnalyzer(pivot_depth=1)

    candles = make_candles(

        highs=[10, 50, 10],
        lows=[1, 2, 1],

    )

    assert analyzer._is_pivot_high(candles, 1)


def test_depth_three():

    analyzer = MarketStructureAnalyzer(pivot_depth=3)

    candles = make_candles(

        highs=[10, 20, 30, 100, 30, 20, 10],
        lows=[1] * 7,

    )

    assert analyzer._is_pivot_high(candles, 3)


# ==========================================================
# Smoke
# ==========================================================

def test_pivot_helpers_smoke():

    analyzer = MarketStructureAnalyzer()

    candles = make_candles(
    highs=[12, 20, 30, 20, 12],
    lows=[10, 5, 2, 5, 10],
    )

    analyzer._is_pivot_high(candles, 2)

    analyzer._is_pivot_low(candles, 2)