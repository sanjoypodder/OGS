"""
===========================================================

OGS Smart Money AI

SMT Divergence Analyzer Basic Tests

===========================================================
"""

from __future__ import annotations

from datetime import datetime

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergenceSeries,
    SMTDivergenceAnalyzer,
)


class MockSwing:
    """
    Minimal mock swing object for analyzer testing.
    """

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
        self.timestamp = timestamp or datetime.now()

        self.is_higher_high = higher_high
        self.is_lower_high = lower_high
        self.is_higher_low = higher_low
        self.is_lower_low = lower_low


# ==========================================================
# Construction
# ==========================================================

def test_create_analyzer():

    analyzer = SMTDivergenceAnalyzer()

    assert analyzer is not None


# ==========================================================
# Empty Inputs
# ==========================================================

def test_empty_inputs():

    analyzer = SMTDivergenceAnalyzer()

    result = analyzer.analyze([], [])

    assert isinstance(result, SMTDivergenceSeries)
    assert len(result) == 0


# ==========================================================
# Length Mismatch
# ==========================================================

def test_length_mismatch():

    analyzer = SMTDivergenceAnalyzer()

    first = [MockSwing()]
    second = []

    result = analyzer.analyze(first, second)

    assert len(result) == 0


# ==========================================================
# No Divergence
# ==========================================================

def test_no_divergence():

    analyzer = SMTDivergenceAnalyzer()

    first = [
        MockSwing(),
    ]

    second = [
        MockSwing(symbol="ETHUSD"),
    ]

    result = analyzer.analyze(first, second)

    assert len(result) == 0


# ==========================================================
# Bearish Detection
# ==========================================================

def test_bearish_detection():

    analyzer = SMTDivergenceAnalyzer()

    first = [
        MockSwing(
            higher_high=True,
        )
    ]

    second = [
        MockSwing(
            symbol="ETHUSD",
            lower_high=True,
        )
    ]

    result = analyzer.analyze(first, second)

    assert len(result) == 1

    divergence = result[0]

    assert divergence.first_symbol == "BTCUSD"
    assert divergence.second_symbol == "ETHUSD"

    from ogs.smart_money.smt_divergence import SMTDivergenceDirection

    assert divergence.direction is SMTDivergenceDirection.BEARISH
    assert divergence.confidence is SMTConfidence.MEDIUM


# ==========================================================
# Returned Collection
# ==========================================================

def test_return_type():

    analyzer = SMTDivergenceAnalyzer()

    result = analyzer.analyze([], [])

    assert isinstance(result, SMTDivergenceSeries)