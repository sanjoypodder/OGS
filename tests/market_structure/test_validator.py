"""
===========================================================

OGS Smart Money AI

Market Structure Validator Tests

===========================================================
"""

from __future__ import annotations

import pytest

from ogs.market_structure import (
    SwingPointValidator,
    SwingStrength,
    SwingType,
)

from tests.fixtures import (
    CandleFactory,
    SwingFactory,
)


# ==========================================================
# Validator Fixture
# ==========================================================

@pytest.fixture
def validator():

    return SwingPointValidator()


# ==========================================================
# Valid Swing
# ==========================================================

def test_valid_swing(validator):

    swing = SwingFactory.high()

    assert validator.validate(swing)


# ==========================================================
# None
# ==========================================================

def test_none_is_invalid(validator):

    assert not validator.validate(None)


# ==========================================================
# Empty Symbol
# ==========================================================

def test_empty_symbol_invalid(validator):

    swing = SwingFactory.create(
        symbol="",
    )

    assert not validator.validate(swing)


# ==========================================================
# Missing Candle
# ==========================================================

def test_none_candle_invalid(validator):

    swing = SwingFactory.create(
        candle=None,
    )

    #
    # SwingFactory automatically creates a candle.
    # Therefore construct manually.
    #

    from ogs.market_structure import SwingPoint

    swing = SwingPoint(
        symbol="BTCUSD",
        candle=None,
        index=0,
        price=100,
        type=SwingType.HIGH,
        strength=SwingStrength.NORMAL,
    )

    assert not validator.validate(swing)


# ==========================================================
# Negative Index
# ==========================================================

@pytest.mark.parametrize(
    "index",
    [
        -1,
        -10,
        -100,
    ],
)
def test_negative_index_invalid(
    validator,
    index,
):

    swing = SwingFactory.create(
        index=index,
    )

    assert not validator.validate(swing)


# ==========================================================
# Invalid Price
# ==========================================================

@pytest.mark.parametrize(
    "price",
    [
        0,
        -1,
        -100,
        -0.01,
    ],
)
def test_invalid_price(
    validator,
    price,
):

    swing = SwingFactory.create(
        price=price,
    )

    assert not validator.validate(swing)


# ==========================================================
# Missing Swing Type
# ==========================================================

def test_none_type_invalid(validator):

    from ogs.market_structure import SwingPoint

    swing = SwingPoint(
        symbol="BTCUSD",
        candle=CandleFactory.btc(),
        index=0,
        price=100,
        type=None,
        strength=SwingStrength.NORMAL,
    )

    assert not validator.validate(swing)


# ==========================================================
# Missing Strength
# ==========================================================

def test_none_strength_invalid(validator):

    from ogs.market_structure import SwingPoint

    swing = SwingPoint(
        symbol="BTCUSD",
        candle=CandleFactory.btc(),
        index=0,
        price=100,
        type=SwingType.HIGH,
        strength=None,
    )

    assert not validator.validate(swing)


# ==========================================================
# Boundary Values
# ==========================================================

def test_zero_index_valid(validator):

    swing = SwingFactory.create(
        index=0,
    )

    assert validator.validate(swing)


def test_price_one_valid(validator):

    swing = SwingFactory.create(
        price=1,
    )

    assert validator.validate(swing)


# ==========================================================
# All Swing Types Valid
# ==========================================================

@pytest.mark.parametrize(
    "swing_type",
    [
        SwingType.HIGH,
        SwingType.LOW,
        SwingType.HIGHER_HIGH,
        SwingType.HIGHER_LOW,
        SwingType.LOWER_HIGH,
        SwingType.LOWER_LOW,
    ],
)
def test_all_swing_types(
    validator,
    swing_type,
):

    swing = SwingFactory.create(
        swing_type=swing_type,
    )

    assert validator.validate(swing)


# ==========================================================
# All Strength Levels Valid
# ==========================================================

@pytest.mark.parametrize(
    "strength",
    [
        SwingStrength.WEAK,
        SwingStrength.NORMAL,
        SwingStrength.STRONG,
    ],
)
def test_all_strengths(
    validator,
    strength,
):

    swing = SwingFactory.create(
        strength=strength,
    )

    assert validator.validate(swing)