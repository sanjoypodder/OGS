"""
===========================================================

OGS Smart Money AI

SMT Divergence Domain Tests

===========================================================
"""

from __future__ import annotations

from datetime import datetime

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergence,
    SMTDivergenceDirection,
)


def create_divergence(
    *,
    direction=SMTDivergenceDirection.BULLISH,
    comparison=SMTComparisonType.HIGH,
    confidence=SMTConfidence.MEDIUM,
):

    return SMTDivergence(
        first_symbol="BTCUSD",
        second_symbol="ETHUSD",
        first_price=100.0,
        second_price=95.0,
        comparison=comparison,
        direction=direction,
        timestamp=datetime(2025, 1, 1),
        confidence=confidence,
    )


# ==========================================================
# Construction
# ==========================================================


def test_create_divergence():

    divergence = create_divergence()

    assert divergence.first_symbol == "BTCUSD"
    assert divergence.second_symbol == "ETHUSD"

    assert divergence.first_price == 100.0
    assert divergence.second_price == 95.0

    assert divergence.comparison is SMTComparisonType.HIGH

    assert divergence.direction is SMTDivergenceDirection.BULLISH

    assert divergence.confidence is SMTConfidence.MEDIUM


# ==========================================================
# Bullish
# ==========================================================


def test_is_bullish():

    divergence = create_divergence(
        direction=SMTDivergenceDirection.BULLISH,
    )

    assert divergence.is_bullish
    assert not divergence.is_bearish
    assert not divergence.is_hidden_bullish
    assert not divergence.is_hidden_bearish


# ==========================================================
# Bearish
# ==========================================================


def test_is_bearish():

    divergence = create_divergence(
        direction=SMTDivergenceDirection.BEARISH,
    )

    assert divergence.is_bearish
    assert not divergence.is_bullish
    assert not divergence.is_hidden_bullish
    assert not divergence.is_hidden_bearish


# ==========================================================
# Hidden Bullish
# ==========================================================


def test_is_hidden_bullish():

    divergence = create_divergence(
        direction=SMTDivergenceDirection.HIDDEN_BULLISH,
    )

    assert divergence.is_hidden_bullish
    assert not divergence.is_bullish
    assert not divergence.is_bearish
    assert not divergence.is_hidden_bearish


# ==========================================================
# Hidden Bearish
# ==========================================================


def test_is_hidden_bearish():

    divergence = create_divergence(
        direction=SMTDivergenceDirection.HIDDEN_BEARISH,
    )

    assert divergence.is_hidden_bearish
    assert not divergence.is_bullish
    assert not divergence.is_bearish
    assert not divergence.is_hidden_bullish


# ==========================================================
# Confidence
# ==========================================================


def test_high_confidence():

    divergence = create_divergence(
        confidence=SMTConfidence.HIGH,
    )

    assert divergence.confidence is SMTConfidence.HIGH


def test_medium_confidence():

    divergence = create_divergence(
        confidence=SMTConfidence.MEDIUM,
    )

    assert divergence.confidence is SMTConfidence.MEDIUM


def test_low_confidence():

    divergence = create_divergence(
        confidence=SMTConfidence.LOW,
    )

    assert divergence.confidence is SMTConfidence.LOW


# ==========================================================
# Comparison Types
# ==========================================================


def test_high_comparison():

    divergence = create_divergence(
        comparison=SMTComparisonType.HIGH,
    )

    assert divergence.comparison is SMTComparisonType.HIGH


def test_low_comparison():

    divergence = create_divergence(
        comparison=SMTComparisonType.LOW,
    )

    assert divergence.comparison is SMTComparisonType.LOW


def test_close_comparison():

    divergence = create_divergence(
        comparison=SMTComparisonType.CLOSE,
    )

    assert divergence.comparison is SMTComparisonType.CLOSE


# ==========================================================
# Timestamp
# ==========================================================


def test_timestamp():

    ts = datetime(2025, 5, 20, 10, 30)

    divergence = SMTDivergence(
        first_symbol="BTCUSD",
        second_symbol="ETHUSD",
        first_price=100,
        second_price=99,
        comparison=SMTComparisonType.HIGH,
        direction=SMTDivergenceDirection.BEARISH,
        timestamp=ts,
    )

    assert divergence.timestamp == ts


# ==========================================================
# Dataclass Equality
# ==========================================================


def test_dataclass_equality():

    a = create_divergence()

    b = create_divergence()

    assert a == b


def test_dataclass_inequality():

    a = create_divergence()

    b = create_divergence(
        direction=SMTDivergenceDirection.BEARISH,
    )

    assert a != b