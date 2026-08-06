"""
Tests for Timeframe validator.
"""

from ogs.market_data.timeframe import (
    Timeframe,
    TimeframeType,
    TimeframeValidator,
)


def test_valid_timeframe():

    timeframe = Timeframe(
        value=TimeframeType.M15,
    )

    validator = TimeframeValidator()

    assert validator.validate(timeframe)


def test_none_timeframe():

    validator = TimeframeValidator()

    assert not validator.validate(None)


def test_invalid_object():

    validator = TimeframeValidator()

    assert not validator.validate("M15")


def test_invalid_enum():

    class Dummy:
        value = "M15"

    validator = TimeframeValidator()

    assert not validator.validate(Dummy())