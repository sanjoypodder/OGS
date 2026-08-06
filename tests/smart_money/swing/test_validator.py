"""
===========================================================

OGS Smart Money AI

Swing Validator Tests

===========================================================
"""

import pytest

from ogs.smart_money.swing import (
    Swing,
    SwingType,
    SwingValidator,
)


def test_valid_swing(sample_candle):

    swing = Swing(
        index=1,
        candle=sample_candle,
        swing_type=SwingType.HIGH,
    )

    SwingValidator().validate(swing)


def test_negative_index(sample_candle):

    swing = Swing(
        index=-1,
        candle=sample_candle,
        swing_type=SwingType.HIGH,
    )

    with pytest.raises(ValueError):
        SwingValidator().validate(swing)


def test_none_candle():

    swing = Swing(
        index=1,
        candle=None,
        swing_type=SwingType.HIGH,
    )

    with pytest.raises(ValueError):
        SwingValidator().validate(swing)