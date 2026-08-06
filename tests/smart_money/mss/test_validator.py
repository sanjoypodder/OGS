"""
===========================================================

OGS Smart Money AI

MSS Validator Tests

===========================================================
"""

import pytest

from ogs.smart_money.mss import MSSValidator


def test_valid(sample_mss):

    validator = MSSValidator()

    validator.validate(sample_mss)


def test_none_mss():

    validator = MSSValidator()

    with pytest.raises(ValueError):
        validator.validate(None)


def test_none_candle(sample_mss):

    validator = MSSValidator()

    invalid = object.__new__(type(sample_mss))
    object.__setattr__(invalid, "candle", None)
    object.__setattr__(invalid, "triggering_choch", sample_mss.triggering_choch)
    object.__setattr__(invalid, "mss_type", sample_mss.mss_type)

    with pytest.raises(ValueError):
        validator.validate(invalid)


def test_none_triggering_choch(sample_mss):

    validator = MSSValidator()

    invalid = object.__new__(type(sample_mss))
    object.__setattr__(invalid, "candle", sample_mss.candle)
    object.__setattr__(invalid, "triggering_choch", None)
    object.__setattr__(invalid, "mss_type", sample_mss.mss_type)

    with pytest.raises(ValueError):
        validator.validate(invalid)