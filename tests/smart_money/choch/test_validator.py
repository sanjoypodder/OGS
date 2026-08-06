"""
===========================================================

OGS Smart Money AI

CHOCH Validator Tests

===========================================================
"""

import pytest

from ogs.smart_money.choch import CHOCHValidator


def test_valid(sample_choch):

    validator = CHOCHValidator()

    validator.validate(sample_choch)


def test_none_choch():

    validator = CHOCHValidator()

    with pytest.raises(ValueError):
        validator.validate(None)


def test_none_candle(sample_choch):

    validator = CHOCHValidator()

    invalid = object.__new__(type(sample_choch))
    object.__setattr__(invalid, "candle", None)
    object.__setattr__(invalid, "broken_bos", sample_choch.broken_bos)
    object.__setattr__(invalid, "choch_type", sample_choch.choch_type)

    with pytest.raises(ValueError):
        validator.validate(invalid)


def test_none_broken_bos(sample_choch):

    validator = CHOCHValidator()

    invalid = object.__new__(type(sample_choch))
    object.__setattr__(invalid, "candle", sample_choch.candle)
    object.__setattr__(invalid, "broken_bos", None)
    object.__setattr__(invalid, "choch_type", sample_choch.choch_type)

    with pytest.raises(ValueError):
        validator.validate(invalid)