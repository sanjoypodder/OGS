"""
OGS FinOS

Unit Tests

Dealing Range Validator
"""

from decimal import Decimal

import pytest

from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)
from ogs.smart_money.dealing_range.validator import (
    DealingRangeValidator,
)


def create_range(**kwargs) -> DealingRange:
    """
    Create a valid dealing range that can be
    overridden for individual test cases.
    """
    defaults = {
        "range_high": Decimal("2100"),
        "range_low": Decimal("2000"),
        "equilibrium": Decimal("2050"),
        "direction": DealingRangeDirection.BULLISH,
        "start_index": 10,
        "end_index": 20,
    }

    defaults.update(kwargs)

    return DealingRange(**defaults)


def test_valid_dealing_range():

    dealing_range = create_range()

    DealingRangeValidator.validate(dealing_range)

    assert DealingRangeValidator.is_valid(dealing_range)


def test_invalid_range_high():

    dealing_range = create_range(
        range_high=Decimal("-1"),
    )

    with pytest.raises(ValueError):
        DealingRangeValidator.validate(
            dealing_range
        )


def test_invalid_range_low():

    dealing_range = create_range(
        range_low=Decimal("-5"),
    )

    with pytest.raises(ValueError):
        DealingRangeValidator.validate(
            dealing_range
        )


def test_high_less_than_low():

    dealing_range = create_range(
        range_high=Decimal("1900"),
        range_low=Decimal("2000"),
    )

    with pytest.raises(ValueError):
        DealingRangeValidator.validate(
            dealing_range
        )


def test_equilibrium_below_range():

    dealing_range = create_range(
        equilibrium=Decimal("1990"),
    )

    with pytest.raises(ValueError):
        DealingRangeValidator.validate(
            dealing_range
        )


def test_equilibrium_above_range():

    dealing_range = create_range(
        equilibrium=Decimal("2200"),
    )

    with pytest.raises(ValueError):
        DealingRangeValidator.validate(
            dealing_range
        )


def test_invalid_index_order():

    dealing_range = create_range(
        start_index=25,
        end_index=20,
    )

    with pytest.raises(ValueError):
        DealingRangeValidator.validate(
            dealing_range
        )


def test_invalid_direction():

    dealing_range = create_range(
        direction="Bullish",
    )

    with pytest.raises(ValueError):
        DealingRangeValidator.validate(
            dealing_range
        )


def test_is_valid_false():

    dealing_range = create_range(
        range_high=Decimal("1900"),
        range_low=Decimal("2000"),
    )

    assert not DealingRangeValidator.is_valid(
        dealing_range
    )


def test_is_valid_true():

    dealing_range = create_range()

    assert DealingRangeValidator.is_valid(
        dealing_range
    )