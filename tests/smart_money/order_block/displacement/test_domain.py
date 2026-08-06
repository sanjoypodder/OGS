"""
===========================================================

OGS Smart Money AI

Displacement Domain Tests

===========================================================
"""

from dataclasses import FrozenInstanceError

import pytest

from ogs.smart_money.order_block.displacement import (
    Displacement,
    DisplacementDirection,
)

from tests.factories import (
    make_bullish_candle,
)


def test_create():

    displacement = Displacement(
        candle=make_bullish_candle(),
        direction=DisplacementDirection.BULLISH,
    )

    assert displacement is not None


def test_timestamp():

    candle = make_bullish_candle()

    displacement = Displacement(
        candle=candle,
        direction=DisplacementDirection.BULLISH,
    )

    assert displacement.timestamp == candle.timestamp


def test_high():

    candle = make_bullish_candle()

    displacement = Displacement(
        candle=candle,
        direction=DisplacementDirection.BULLISH,
    )

    assert displacement.high == candle.high


def test_low():

    candle = make_bullish_candle()

    displacement = Displacement(
        candle=candle,
        direction=DisplacementDirection.BULLISH,
    )

    assert displacement.low == candle.low


def test_string():

    displacement = Displacement(
        candle=make_bullish_candle(),
        direction=DisplacementDirection.BULLISH,
    )

    assert "BULLISH" in str(displacement)


def test_frozen():

    displacement = Displacement(
        candle=make_bullish_candle(),
        direction=DisplacementDirection.BULLISH,
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        displacement.direction = (
            DisplacementDirection.BEARISH
        )