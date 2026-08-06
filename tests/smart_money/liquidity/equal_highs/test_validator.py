"""
===========================================================

OGS Smart Money AI

Equal High Validator Tests

===========================================================
"""

from decimal import Decimal

import pytest

from ogs.smart_money.liquidity.equal_highs import (
    EqualHigh,
    EqualHighType,
    EqualHighValidator,
)
from tests.factories import make_swing_high


def test_valid(sample_equal_high):

    validator = EqualHighValidator()

    validator.validate(sample_equal_high)


def test_none_equal_high():

    validator = EqualHighValidator()

    with pytest.raises(ValueError):
        validator.validate(None)


def test_none_first_swing():

    validator = EqualHighValidator()

    zone = EqualHigh(
        first_swing=None,
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    with pytest.raises(ValueError):
        validator.validate(zone)


def test_none_second_swing():

    validator = EqualHighValidator()

    zone = EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=None,
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    with pytest.raises(ValueError):
        validator.validate(zone)