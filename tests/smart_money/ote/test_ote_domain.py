"""
OGS FinOS

Unit Tests

OTE Domain
"""

from decimal import Decimal

from ogs.smart_money.ote.domain import (
    OTE,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)


def create_ote() -> OTE:

    return OTE(
        range_high=Decimal("2100"),
        range_low=Decimal("2000"),
        level_62=Decimal("2038"),
        level_705=Decimal("2029.5"),
        level_79=Decimal("2021"),
        zone_low=Decimal("2021"),
        zone_high=Decimal("2038"),
        direction=OTEDirection.BULLISH,
    )


def test_create_ote():

    ote = create_ote()

    assert ote.range_high == Decimal("2100")
    assert ote.range_low == Decimal("2000")
    assert ote.level_62 == Decimal("2038")
    assert ote.level_705 == Decimal("2029.5")
    assert ote.level_79 == Decimal("2021")


def test_zone_size():

    ote = create_ote()

    assert ote.zone_size == Decimal("17")


def test_is_bullish():

    ote = create_ote()

    assert ote.is_bullish is True
    assert ote.is_bearish is False


def test_string_representation():

    ote = create_ote()

    assert "OTE" in str(ote)
    assert "62=" in str(ote)


def test_repr():

    ote = create_ote()

    assert "OTE" in repr(ote)


def test_metadata_default():

    ote = create_ote()

    assert isinstance(
        ote.metadata,
        dict,
    )


def test_created_at():

    ote = create_ote()

    assert ote.created_at is not None


def test_uuid():

    ote = create_ote()

    assert ote.id is not None