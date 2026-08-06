"""
===========================================================

OGS Smart Money AI

Market Structure Domain Tests

===========================================================
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from ogs.market_structure import (
    SwingPoint,
    SwingStrength,
    SwingType,
)

from tests.fixtures import SwingFactory


# ==========================================================
# Creation
# ==========================================================

def test_create_swing_point():

    swing = SwingFactory.create(
        index=10,
        price=105.0,
        swing_type=SwingType.HIGH,
    )

    assert isinstance(swing, SwingPoint)

    assert swing.symbol == "BTCUSD"

    assert swing.index == 10

    assert swing.price == 105.0

    assert swing.type is SwingType.HIGH

    assert swing.strength is SwingStrength.NORMAL


# ==========================================================
# Timestamp
# ==========================================================

def test_timestamp_property():

    swing = SwingFactory.high()

    assert swing.timestamp == swing.candle.timestamp


# ==========================================================
# High Detection
# ==========================================================

def test_high_is_high(high_swing):

    assert high_swing.is_high

    assert not high_swing.is_low


def test_higher_high_is_high(higher_high):

    assert higher_high.is_high

    assert higher_high.is_higher_high

    assert not higher_high.is_lower_high


def test_lower_high_is_high(lower_high):

    assert lower_high.is_high

    assert lower_high.is_lower_high

    assert not lower_high.is_higher_high


# ==========================================================
# Low Detection
# ==========================================================

def test_low_is_low(low_swing):

    assert low_swing.is_low

    assert not low_swing.is_high


def test_higher_low_is_low(higher_low):

    assert higher_low.is_low

    assert higher_low.is_higher_low

    assert not higher_low.is_lower_low


def test_lower_low_is_low(lower_low):

    assert lower_low.is_low

    assert lower_low.is_lower_low

    assert not lower_low.is_higher_low


# ==========================================================
# Swing Classification Helpers
# ==========================================================

def test_is_higher_high(higher_high):

    assert higher_high.is_higher_high

    assert higher_high.is_high

    assert not higher_high.is_lower_high

    assert not higher_high.is_low


def test_is_higher_low(higher_low):

    assert higher_low.is_higher_low

    assert higher_low.is_low

    assert not higher_low.is_lower_low

    assert not higher_low.is_high


def test_is_lower_high(lower_high):

    assert lower_high.is_lower_high

    assert lower_high.is_high

    assert not lower_high.is_higher_high

    assert not lower_high.is_low


def test_is_lower_low(lower_low):

    assert lower_low.is_lower_low

    assert lower_low.is_low

    assert not lower_low.is_higher_low

    assert not lower_low.is_high

    # ==========================================================
# Strength Helpers
# ==========================================================

def test_strong_high(strong_high):

    assert strong_high.is_strong

    assert not strong_high.is_weak

    assert strong_high.strength is SwingStrength.STRONG


def test_weak_high(weak_high):

    assert weak_high.is_weak

    assert not weak_high.is_strong

    assert weak_high.strength is SwingStrength.WEAK


def test_strong_low(strong_low):

    assert strong_low.is_strong

    assert not strong_low.is_weak

    assert strong_low.is_low


def test_weak_low(weak_low):

    assert weak_low.is_weak

    assert not weak_low.is_strong

    assert weak_low.is_low


# ==========================================================
# Equality
# ==========================================================

def test_equality():

    swing1 = SwingFactory.create(
        index=1,
        price=105.0,
        swing_type=SwingType.HIGH,
    )

    swing2 = SwingFactory.create(
        index=1,
        price=105.0,
        swing_type=SwingType.HIGH,
    )

    assert swing1 == swing2


def test_inequality():

    swing1 = SwingFactory.high()

    swing2 = SwingFactory.low()

    assert swing1 != swing2


# ==========================================================
# Hashability
# ==========================================================

def test_hashable():

    swing = SwingFactory.high()

    data = {
        swing: "OK",
    }

    assert data[swing] == "OK"


# ==========================================================
# Frozen Dataclass
# ==========================================================

def test_frozen_dataclass():

    swing = SwingFactory.high()

    with pytest.raises(FrozenInstanceError):

        swing.price = 999.0


# ==========================================================
# String Representation
# ==========================================================

def test_repr():

    swing = SwingFactory.high()

    text = repr(swing)

    assert "SwingPoint" in text

    assert "BTCUSD" in text

    assert "HIGH" in text


# ==========================================================
# Default Strength
# ==========================================================

def test_default_strength():

    swing = SwingFactory.high()

    assert swing.strength is SwingStrength.NORMAL


# ==========================================================
# Timestamp Delegation
# ==========================================================

def test_timestamp_matches_candle():

    swing = SwingFactory.high()

    assert swing.timestamp == swing.candle.timestamp


# ==========================================================
# Dataclass Fields
# ==========================================================

def test_required_fields():

    swing = SwingFactory.high()

    assert hasattr(swing, "symbol")

    assert hasattr(swing, "candle")

    assert hasattr(swing, "index")

    assert hasattr(swing, "price")

    assert hasattr(swing, "type")

    assert hasattr(swing, "strength")


# ==========================================================
# Type Checks
# ==========================================================

def test_property_types():

    swing = SwingFactory.high()

    assert isinstance(swing.symbol, str)

    assert isinstance(swing.index, int)

    assert isinstance(swing.price, float)

    assert isinstance(swing.type, SwingType)

    assert isinstance(swing.strength, SwingStrength)


# ==========================================================
# Factory Sequence
# ==========================================================

def test_factory_sequence():

    swings = SwingFactory.sequence()

    assert len(swings) == 6

    assert swings[0].type is SwingType.LOW

    assert swings[-1].type is SwingType.HIGHER_HIGH


# ==========================================================
# Immutability
# ==========================================================

def test_multiple_instances_are_independent():

    s1 = SwingFactory.high()

    s2 = SwingFactory.high()

    assert s1 == s2

    assert s1 is not s2


# ==========================================================
# Smoke Test
# ==========================================================

def test_factory_returns_swingpoint():

    swing = SwingFactory.high()

    assert isinstance(swing, SwingPoint)