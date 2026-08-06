"""
===========================================================

OGS Smart Money AI

SMT Divergence Validator Tests

===========================================================
"""

from __future__ import annotations

from dataclasses import replace
from datetime import datetime

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergence,
    SMTDivergenceDirection,
    SMTDivergenceValidator,
)


def make_divergence() -> SMTDivergence:
    return SMTDivergence(
        first_symbol="BTCUSD",
        second_symbol="ETHUSD",
        first_price=100.0,
        second_price=95.0,
        comparison=SMTComparisonType.HIGH,
        direction=SMTDivergenceDirection.BULLISH,
        timestamp=datetime.now(),
        confidence=SMTConfidence.MEDIUM,
    )


# ==========================================================
# Valid Object
# ==========================================================

def test_validate_valid_divergence():
    validator = SMTDivergenceValidator()

    assert validator.validate(make_divergence()) is True


# ==========================================================
# None Object
# ==========================================================

def test_validate_none():
    validator = SMTDivergenceValidator()

    assert validator.validate(None) is False


# ==========================================================
# Symbols
# ==========================================================

def test_empty_first_symbol():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), first_symbol="")

    assert validator.validate(d) is False


def test_empty_second_symbol():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), second_symbol="")

    assert validator.validate(d) is False


def test_same_symbols():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), second_symbol="BTCUSD")

    assert validator.validate(d) is False


# ==========================================================
# Prices
# ==========================================================

def test_negative_first_price():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), first_price=-1)

    assert validator.validate(d) is False


def test_zero_first_price():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), first_price=0)

    assert validator.validate(d) is False


def test_negative_second_price():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), second_price=-1)

    assert validator.validate(d) is False


def test_zero_second_price():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), second_price=0)

    assert validator.validate(d) is False


# ==========================================================
# Direction
# ==========================================================

def test_none_direction():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), direction=None)

    assert validator.validate(d) is False


# ==========================================================
# Comparison
# ==========================================================

def test_none_comparison():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), comparison=None)

    assert validator.validate(d) is False


# ==========================================================
# Timestamp
# ==========================================================

def test_none_timestamp():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), timestamp=None)

    assert validator.validate(d) is False


# ==========================================================
# Confidence
# ==========================================================

def test_none_confidence():
    validator = SMTDivergenceValidator()

    d = replace(make_divergence(), confidence=None)

    assert validator.validate(d) is False