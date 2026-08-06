"""
OGS FinOS

Unit Tests

Dealing Range Domain
"""

from decimal import Decimal

from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)


def create_range() -> DealingRange:
    return DealingRange(
        range_high=Decimal("2100"),
        range_low=Decimal("2000"),
        equilibrium=Decimal("2050"),
        direction=DealingRangeDirection.BULLISH,
        start_index=10,
        end_index=20,
    )


def test_create_dealing_range():

    dealing_range = create_range()

    assert dealing_range.range_high == Decimal("2100")
    assert dealing_range.range_low == Decimal("2000")
    assert dealing_range.equilibrium == Decimal("2050")


def test_range_size():

    dealing_range = create_range()

    assert dealing_range.range_size == Decimal("100")


def test_is_bullish():

    dealing_range = create_range()

    assert dealing_range.is_bullish is True
    assert dealing_range.is_bearish is False
    assert dealing_range.is_sideways is False


def test_string_representation():

    dealing_range = create_range()

    assert "2100" in str(dealing_range)
    assert "2000" in str(dealing_range)


def test_repr():

    dealing_range = create_range()

    assert "DealingRange" in repr(dealing_range)


def test_metadata_default():

    dealing_range = create_range()

    assert isinstance(dealing_range.metadata, dict)


def test_created_at_exists():

    dealing_range = create_range()

    assert dealing_range.created_at is not None


def test_unique_id_exists():

    dealing_range = create_range()

    assert dealing_range.id is not None