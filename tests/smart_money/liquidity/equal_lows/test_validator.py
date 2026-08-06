"""
===========================================================

OGS Smart Money AI

Equal Low Validator Tests

===========================================================
"""

from decimal import Decimal

import pytest

from tests.factories import make_swing_low

from ogs.smart_money.liquidity.equal_lows import (
    EqualLow,
    EqualLowType,
    EqualLowValidator,
)


def test_valid(sample_equal_low):

    validator = EqualLowValidator()

    validator.validate(sample_equal_low)


def test_none_equal_low():

    validator = EqualLowValidator()

    with pytest.raises(ValueError):
        validator.validate(None)


def test_none_first_swing():

    validator = EqualLowValidator()

    zone = EqualLow(
        first_swing=None,
        second_swing=make_swing_low(index=8),
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )

    with pytest.raises(ValueError):
        validator.validate(zone)


def test_none_second_swing():

    validator = EqualLowValidator()

    zone = EqualLow(
        first_swing=make_swing_low(index=2),
        second_swing=None,
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )

    with pytest.raises(ValueError):
        validator.validate(zone)