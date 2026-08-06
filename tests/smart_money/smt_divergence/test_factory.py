"""
===========================================================

OGS Smart Money AI

SMT Divergence Factory Tests

===========================================================
"""

from __future__ import annotations

from datetime import datetime

import pytest

from ogs.smart_money.smt_divergence import (
    SMTComparisonType,
    SMTConfidence,
    SMTDivergence,
    SMTDivergenceDirection,
    SMTDivergenceFactory,
)


# ==========================================================
# Valid Creation
# ==========================================================

def test_factory_create_valid():

    divergence = SMTDivergenceFactory.create(
        first_symbol="BTCUSD",
        second_symbol="ETHUSD",
        first_price=100.0,
        second_price=95.0,
        comparison=SMTComparisonType.HIGH,
        direction=SMTDivergenceDirection.BULLISH,
        timestamp=datetime.now(),
        confidence=SMTConfidence.HIGH,
    )

    assert isinstance(divergence, SMTDivergence)

    assert divergence.first_symbol == "BTCUSD"
    assert divergence.second_symbol == "ETHUSD"

    assert divergence.first_price == 100.0
    assert divergence.second_price == 95.0

    assert divergence.direction is SMTDivergenceDirection.BULLISH
    assert divergence.comparison is SMTComparisonType.HIGH
    assert divergence.confidence is SMTConfidence.HIGH


# ==========================================================
# Default Confidence
# ==========================================================

def test_factory_default_confidence():

    divergence = SMTDivergenceFactory.create(
        first_symbol="BTCUSD",
        second_symbol="ETHUSD",
        first_price=100,
        second_price=90,
        comparison=SMTComparisonType.LOW,
        direction=SMTDivergenceDirection.BEARISH,
        timestamp=datetime.now(),
    )

    assert divergence.confidence is SMTConfidence.MEDIUM


# ==========================================================
# Invalid Symbols
# ==========================================================

def test_factory_empty_first_symbol():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="",
            second_symbol="ETHUSD",
            first_price=100,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


def test_factory_empty_second_symbol():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="",
            first_price=100,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


def test_factory_same_symbols():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="BTCUSD",
            first_price=100,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


# ==========================================================
# Invalid Prices
# ==========================================================

def test_factory_negative_first_price():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=-1,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


def test_factory_zero_first_price():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=0,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


def test_factory_negative_second_price():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=100,
            second_price=-1,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


def test_factory_zero_second_price():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=100,
            second_price=0,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


# ==========================================================
# Missing Values
# ==========================================================

def test_factory_none_direction():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=100,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=None,
            timestamp=datetime.now(),
        )


def test_factory_none_comparison():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=100,
            second_price=95,
            comparison=None,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
        )


def test_factory_none_timestamp():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=100,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=None,
        )


def test_factory_none_confidence():

    with pytest.raises(ValueError):

        SMTDivergenceFactory.create(
            first_symbol="BTCUSD",
            second_symbol="ETHUSD",
            first_price=100,
            second_price=95,
            comparison=SMTComparisonType.HIGH,
            direction=SMTDivergenceDirection.BULLISH,
            timestamp=datetime.now(),
            confidence=None,
        )