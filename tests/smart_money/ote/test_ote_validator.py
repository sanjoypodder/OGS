"""
OGS FinOS

Unit Tests

OTE Validator
"""

from decimal import Decimal

import pytest

from ogs.smart_money.ote.domain import (
    OTE,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)
from ogs.smart_money.ote.validator import (
    OTEValidator,
)


def create_ote(**kwargs) -> OTE:

    defaults = {
        "range_high": Decimal("2100"),
        "range_low": Decimal("2000"),
        "level_62": Decimal("2038"),
        "level_705": Decimal("2029.5"),
        "level_79": Decimal("2021"),
        "zone_low": Decimal("2021"),
        "zone_high": Decimal("2038"),
        "direction": OTEDirection.BULLISH,
    }

    defaults.update(kwargs)

    return OTE(**defaults)


def test_valid_ote():

    ote = create_ote()

    OTEValidator.validate(ote)

    assert OTEValidator.is_valid(ote)


def test_invalid_range_high():

    ote = create_ote(
        range_high=Decimal("-1")
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_invalid_range_low():

    ote = create_ote(
        range_low=Decimal("-1")
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_high_less_than_low():

    ote = create_ote(
        range_high=Decimal("1900"),
        range_low=Decimal("2000"),
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_invalid_level_62():

    ote = create_ote(
        level_62=Decimal("2300")
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_invalid_level_705():

    ote = create_ote(
        level_705=Decimal("2500")
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_invalid_level_79():

    ote = create_ote(
        level_79=Decimal("2600")
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_invalid_zone():

    ote = create_ote(
        zone_low=Decimal("2040"),
        zone_high=Decimal("2030"),
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_invalid_direction():

    ote = create_ote(
        direction="Bullish"
    )

    with pytest.raises(ValueError):
        OTEValidator.validate(ote)


def test_is_valid_false():

    ote = create_ote(
        range_high=Decimal("1900"),
        range_low=Decimal("2000"),
    )

    assert not OTEValidator.is_valid(
        ote
    )


def test_is_valid_true():

    ote = create_ote()

    assert OTEValidator.is_valid(
        ote
    )