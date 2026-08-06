"""
===========================================================

OGS Smart Money AI

Market Structure Analyzer Tests

Basic Public API Tests

===========================================================
"""

from __future__ import annotations

from ogs.market_structure import (
    MarketStructureAnalyzer,
    SwingSeries,
    SwingType,
)

from tests.fixtures import CandleFactory


# ==========================================================
# Helpers
# ==========================================================

def pivot_high_sequence():

    return [

        CandleFactory.create(
            open=8,
            high=10,
            low=5,
            close=9,
        ),

        CandleFactory.create(
            open=18,
            high=20,
            low=6,
            close=19,
        ),

        CandleFactory.create(
            open=48,
            high=50,
            low=7,
            close=49,
        ),

        CandleFactory.create(
            open=18,
            high=20,
            low=8,
            close=19,
        ),

        CandleFactory.create(
            open=9,
            high=10,
            low=8,
            close=9,
        )

    ]


def pivot_low_sequence():

    return [

        CandleFactory.create(
            open=25,
            high=30,
            low=20,
            close=26,
        ),

        CandleFactory.create(
            open=15,
            high=29,
            low=10,
            close=16,
        ),

        CandleFactory.create(
            open=5,
            high=28,
            low=1,
            close=6,
        ),

        CandleFactory.create(
            open=15,
            high=27,
            low=10,
            close=16,
        ),

        CandleFactory.create(
            open=25,
            high=26,
            low=20,
            close=24,
        ),

    ]


# ==========================================================
# Construction
# ==========================================================

def test_default_constructor():

    analyzer = MarketStructureAnalyzer()

    assert analyzer is not None


def test_custom_pivot_depth():

    analyzer = MarketStructureAnalyzer(pivot_depth=3)

    assert analyzer is not None


# ==========================================================
# Empty Input
# ==========================================================

def test_empty_input():

    analyzer = MarketStructureAnalyzer()

    swings = analyzer.analyze([])

    assert isinstance(swings, SwingSeries)

    assert len(swings) == 0


# ==========================================================
# Not Enough Candles
# ==========================================================

def test_insufficient_candles():

    analyzer = MarketStructureAnalyzer()

    candles = CandleFactory.sequence(4)

    swings = analyzer.analyze(candles)

    assert len(swings) == 0


# ==========================================================
# Exact Minimum
# ==========================================================

def test_exact_minimum_without_pivot():

    analyzer = MarketStructureAnalyzer()

    candles = CandleFactory.sequence(5)

    swings = analyzer.analyze(candles)

    assert isinstance(swings, SwingSeries)


# ==========================================================
# Pivot High
# ==========================================================

def test_detect_single_pivot_high():

    analyzer = MarketStructureAnalyzer()

    swings = analyzer.analyze(
        pivot_high_sequence()
    )

    assert len(swings) == 1

    swing = swings[0]

    assert swing.index == 2

    assert swing.type is SwingType.HIGH


# ==========================================================
# Pivot Low
# ==========================================================

def test_detect_single_pivot_low():

    analyzer = MarketStructureAnalyzer()

    swings = analyzer.analyze(
        pivot_low_sequence()
    )

    assert len(swings) == 1

    swing = swings[0]

    assert swing.index == 2

    assert swing.type is SwingType.LOW


# ==========================================================
# Return Type
# ==========================================================

def test_returns_swing_series():

    analyzer = MarketStructureAnalyzer()

    swings = analyzer.analyze(
        CandleFactory.sequence(20)
    )

    assert isinstance(swings, SwingSeries)


# ==========================================================
# Repeated Calls
# ==========================================================

def test_multiple_calls():

    analyzer = MarketStructureAnalyzer()

    first = analyzer.analyze([])

    second = analyzer.analyze([])

    assert first is not second


# ==========================================================
# Smoke Test
# ==========================================================

def test_smoke():

    analyzer = MarketStructureAnalyzer()

    swings = analyzer.analyze(
        CandleFactory.sequence(50)
    )

    assert isinstance(swings, SwingSeries)