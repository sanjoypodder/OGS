"""
===========================================================

OGS Smart Money AI

SMT Divergence Analyzer Edge Case Tests

===========================================================
"""

from __future__ import annotations

from datetime import datetime

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTDivergenceAnalyzer,
    SMTDivergenceDirection,
)


class MockSwing:

    def __init__(
        self,
        *,
        symbol="BTCUSD",
        price=100.0,
        comparison=SMTComparisonType.HIGH,
        timestamp=None,
        higher_high=False,
        lower_high=False,
        higher_low=False,
        lower_low=False,
    ):
        self.symbol = symbol
        self.price = price
        self.comparison = comparison
        self.timestamp = timestamp or datetime(2025, 1, 1)

        self.is_higher_high = higher_high
        self.is_lower_high = lower_high
        self.is_higher_low = higher_low
        self.is_lower_low = lower_low


def test_both_inputs_empty():

    analyzer = SMTDivergenceAnalyzer()

    result = analyzer.analyze([], [])

    assert len(result) == 0


def test_first_empty():

    analyzer = SMTDivergenceAnalyzer()

    result = analyzer.analyze([], [MockSwing()])

    assert len(result) == 0


def test_second_empty():

    analyzer = SMTDivergenceAnalyzer()

    result = analyzer.analyze([MockSwing()], [])

    assert len(result) == 0


def test_multiple_divergences():

    analyzer = SMTDivergenceAnalyzer()

    first = [
        MockSwing(higher_high=True),
        MockSwing(lower_low=True),
    ]

    second = [
        MockSwing(symbol="ETHUSD", lower_high=True),
        MockSwing(symbol="ETHUSD", higher_low=True),
    ]

    result = analyzer.analyze(first, second)

    assert len(result) == 2

    assert result[0].direction is SMTDivergenceDirection.BEARISH
    assert result[1].direction is SMTDivergenceDirection.BULLISH


def test_no_matching_patterns():

    analyzer = SMTDivergenceAnalyzer()

    first = [
        MockSwing(higher_high=True),
        MockSwing(higher_high=True),
    ]

    second = [
        MockSwing(symbol="ETHUSD", higher_high=True),
        MockSwing(symbol="ETHUSD", higher_high=True),
    ]

    result = analyzer.analyze(first, second)

    assert len(result) == 0


def test_equal_length_without_divergence():

    analyzer = SMTDivergenceAnalyzer()

    first = [
        MockSwing(),
        MockSwing(),
        MockSwing(),
    ]

    second = [
        MockSwing(symbol="ETHUSD"),
        MockSwing(symbol="ETHUSD"),
        MockSwing(symbol="ETHUSD"),
    ]

    result = analyzer.analyze(first, second)

    assert len(result) == 0


def test_mismatched_lengths_returns_empty():

    analyzer = SMTDivergenceAnalyzer()

    first = [
        MockSwing(higher_high=True),
        MockSwing(lower_low=True),
    ]

    second = [
        MockSwing(symbol="ETHUSD", lower_high=True),
    ]

    result = analyzer.analyze(first, second)

    assert len(result) == 0


def test_detect_direction_returns_none():

    first = MockSwing()
    second = MockSwing(symbol="ETHUSD")

    direction = SMTDivergenceAnalyzer._detect_direction(first, second)

    assert direction is None


def test_detect_direction_bearish():

    first = MockSwing(higher_high=True)
    second = MockSwing(symbol="ETHUSD", lower_high=True)

    direction = SMTDivergenceAnalyzer._detect_direction(first, second)

    assert direction is SMTDivergenceDirection.BEARISH


def test_detect_direction_bullish():

    first = MockSwing(lower_low=True)
    second = MockSwing(symbol="ETHUSD", higher_low=True)

    direction = SMTDivergenceAnalyzer._detect_direction(first, second)

    assert direction is SMTDivergenceDirection.BULLISH


def test_detect_direction_hidden_bullish():

    first = MockSwing(higher_low=True)
    second = MockSwing(symbol="ETHUSD", lower_low=True)

    direction = SMTDivergenceAnalyzer._detect_direction(first, second)

    assert direction is SMTDivergenceDirection.HIDDEN_BULLISH


def test_detect_direction_hidden_bearish():

    first = MockSwing(lower_high=True)
    second = MockSwing(symbol="ETHUSD", higher_high=True)

    direction = SMTDivergenceAnalyzer._detect_direction(first, second)

    assert direction is SMTDivergenceDirection.HIDDEN_BEARISH