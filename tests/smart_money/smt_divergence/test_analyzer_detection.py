"""
===========================================================

OGS Smart Money AI

SMT Divergence Detection Tests

===========================================================
"""

from __future__ import annotations

from datetime import datetime

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTConfidence,
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


def analyze(first, second):

    analyzer = SMTDivergenceAnalyzer()

    result = analyzer.analyze(
        [first],
        [second],
    )

    assert len(result) == 1

    return result[0]


# ==========================================================
# Bearish SMT
# ==========================================================

def test_bearish_divergence():

    d = analyze(
        MockSwing(higher_high=True),
        MockSwing(
            symbol="ETHUSD",
            lower_high=True,
        ),
    )

    assert d.direction is SMTDivergenceDirection.BEARISH


# ==========================================================
# Bullish SMT
# ==========================================================

def test_bullish_divergence():

    d = analyze(
        MockSwing(lower_low=True),
        MockSwing(
            symbol="ETHUSD",
            higher_low=True,
        ),
    )

    assert d.direction is SMTDivergenceDirection.BULLISH


# ==========================================================
# Hidden Bullish
# ==========================================================

def test_hidden_bullish_divergence():

    d = analyze(
        MockSwing(higher_low=True),
        MockSwing(
            symbol="ETHUSD",
            lower_low=True,
        ),
    )

    assert d.direction is SMTDivergenceDirection.HIDDEN_BULLISH


# ==========================================================
# Hidden Bearish
# ==========================================================

def test_hidden_bearish_divergence():

    d = analyze(
        MockSwing(lower_high=True),
        MockSwing(
            symbol="ETHUSD",
            higher_high=True,
        ),
    )

    assert d.direction is SMTDivergenceDirection.HIDDEN_BEARISH


# ==========================================================
# Confidence
# ==========================================================

def test_default_confidence():

    d = analyze(
        MockSwing(higher_high=True),
        MockSwing(
            symbol="ETHUSD",
            lower_high=True,
        ),
    )

    assert d.confidence is SMTConfidence.MEDIUM


# ==========================================================
# Symbol Mapping
# ==========================================================

def test_symbol_mapping():

    d = analyze(
        MockSwing(
            symbol="BTCUSDT",
            higher_high=True,
        ),
        MockSwing(
            symbol="ETHUSDT",
            lower_high=True,
        ),
    )

    assert d.first_symbol == "BTCUSDT"
    assert d.second_symbol == "ETHUSDT"


# ==========================================================
# Price Mapping
# ==========================================================

def test_price_mapping():

    d = analyze(
        MockSwing(
            price=2500.5,
            higher_high=True,
        ),
        MockSwing(
            symbol="ETHUSD",
            price=2490.25,
            lower_high=True,
        ),
    )

    assert d.first_price == 2500.5
    assert d.second_price == 2490.25


# ==========================================================
# Timestamp Mapping
# ==========================================================

def test_timestamp_mapping():

    ts = datetime(2025, 6, 1, 10, 30)

    d = analyze(
        MockSwing(
            timestamp=ts,
            higher_high=True,
        ),
        MockSwing(
            symbol="ETHUSD",
            lower_high=True,
        ),
    )

    assert d.timestamp == ts