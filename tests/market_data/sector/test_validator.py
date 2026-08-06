"""
Tests for Sector validator.
"""

import pytest

from ogs.market_data.sector import (
    Sector,
    SectorValidator,
)


def make():

    return Sector(
        sector_code="BANK",
        sector_name="Banking",
    )


def test_success():

    validator = SectorValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "sector_code",
        "sector_name",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = SectorValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_sector_type():

    obj = make()

    obj.sector_type = "INVALID"

    validator = SectorValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = SectorValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)