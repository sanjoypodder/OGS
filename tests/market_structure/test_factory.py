"""
===========================================================

OGS Smart Money AI

Market Structure Factory Tests

===========================================================
"""

from __future__ import annotations

import pytest

from ogs.market_structure import (
    SwingPoint,
    SwingPointFactory,
    SwingStrength,
    SwingType,
)

from tests.fixtures import (
    CandleFactory,
    SwingFactory,
)


# ==========================================================
# Creation
# ==========================================================

def test_create_valid_swing():

    candle = CandleFactory.btc()

    swing = SwingPointFactory.create(
        symbol="BTCUSD",
        candle=candle,
        index=10,
        price=105.0,
        type=SwingType.HIGH,
    )

    assert isinstance(swing, SwingPoint)

    assert swing.symbol == "BTCUSD"
    assert swing.candle == candle
    assert swing.index == 10
    assert swing.price == 105.0
    assert swing.type is SwingType.HIGH
    assert swing.strength is SwingStrength.NORMAL


# ==========================================================
# Strength
# ==========================================================

def test_custom_strength():

    candle = CandleFactory.btc()

    swing = SwingPointFactory.create(
        symbol="BTCUSD",
        candle=candle,
        index=1,
        price=105,
        type=SwingType.HIGH,
        strength=SwingStrength.STRONG,
    )

    assert swing.strength is SwingStrength.STRONG


def test_default_strength():

    candle = CandleFactory.btc()

    swing = SwingPointFactory.create(
        symbol="BTCUSD",
        candle=candle,
        index=0,
        price=100,
        type=SwingType.HIGH,
    )

    assert swing.strength is SwingStrength.NORMAL


# ==========================================================
# Invalid Symbol
# ==========================================================

def test_empty_symbol():

    candle = CandleFactory.btc()

    with pytest.raises(ValueError):

        SwingPointFactory.create(
            symbol="",
            candle=candle,
            index=0,
            price=100,
            type=SwingType.HIGH,
        )


# ==========================================================
# Missing Candle
# ==========================================================

def test_none_candle():

    with pytest.raises(ValueError):

        SwingPointFactory.create(
            symbol="BTCUSD",
            candle=None,
            index=0,
            price=100,
            type=SwingType.HIGH,
        )


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
def test_negative_index(index):

    candle = CandleFactory.btc()

    with pytest.raises(ValueError):

        SwingPointFactory.create(
            symbol="BTCUSD",
            candle=candle,
            index=index,
            price=100,
            type=SwingType.HIGH,
        )


# ==========================================================
# Invalid Price
# ==========================================================

@pytest.mark.parametrize(
    "price",
    [
        0,
        -1,
        -10,
        -100,
    ],
)
def test_invalid_price(price):

    candle = CandleFactory.btc()

    with pytest.raises(ValueError):

        SwingPointFactory.create(
            symbol="BTCUSD",
            candle=candle,
            index=0,
            price=price,
            type=SwingType.HIGH,
        )


# ==========================================================
# None Type
# ==========================================================

def test_none_type():

    candle = CandleFactory.btc()

    with pytest.raises(ValueError):

        SwingPointFactory.create(
            symbol="BTCUSD",
            candle=candle,
            index=0,
            price=100,
            type=None,
        )


# ==========================================================
# None Strength
# ==========================================================

def test_none_strength():

    candle = CandleFactory.btc()

    with pytest.raises(ValueError):

        SwingPointFactory.create(
            symbol="BTCUSD",
            candle=candle,
            index=0,
            price=100,
            type=SwingType.HIGH,
            strength=None,
        )


# ==========================================================
# Boundary Values
# ==========================================================

def test_zero_index():

    candle = CandleFactory.btc()

    swing = SwingPointFactory.create(
        symbol="BTCUSD",
        candle=candle,
        index=0,
        price=1,
        type=SwingType.HIGH,
    )

    assert swing.index == 0


def test_price_one():

    candle = CandleFactory.btc()

    swing = SwingPointFactory.create(
        symbol="BTCUSD",
        candle=candle,
        index=1,
        price=1,
        type=SwingType.HIGH,
    )

    assert swing.price == 1


# ==========================================================
# All Swing Types
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
def test_all_swing_types(swing_type):

    candle = CandleFactory.btc()

    swing = SwingPointFactory.create(
        symbol="BTCUSD",
        candle=candle,
        index=1,
        price=100,
        type=swing_type,
    )

    assert swing.type is swing_type


# ==========================================================
# All Strength Levels
# ==========================================================

@pytest.mark.parametrize(
    "strength",
    [
        SwingStrength.WEAK,
        SwingStrength.NORMAL,
        SwingStrength.STRONG,
    ],
)
def test_all_strengths(strength):

    candle = CandleFactory.btc()

    swing = SwingPointFactory.create(
        symbol="BTCUSD",
        candle=candle,
        index=1,
        price=100,
        type=SwingType.HIGH,
        strength=strength,
    )

    assert swing.strength is strength


# ==========================================================
# Factory Compatibility
# ==========================================================

def test_factory_matches_fixture():

    fixture_swing = SwingFactory.high()

    factory_swing = SwingPointFactory.create(
        symbol=fixture_swing.symbol,
        candle=fixture_swing.candle,
        index=fixture_swing.index,
        price=fixture_swing.price,
        type=fixture_swing.type,
        strength=fixture_swing.strength,
    )

    assert factory_swing == fixture_swing