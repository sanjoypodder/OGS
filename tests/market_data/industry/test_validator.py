"""
Tests for Industry validator.
"""

import pytest

from ogs.market_data.industry import (
    Industry,
    IndustryValidator,
)


def make():

    return Industry(
        industry_code="PVT_BANK",
        industry_name="Private Banks",
        sector_code="BANK",
    )


def test_success():

    validator = IndustryValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "industry_code",
        "industry_name",
        "sector_code",
    ],
)
def test_required_fields(field):

    obj = make()

    setattr(obj, field, "")

    validator = IndustryValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_industry_type():

    obj = make()

    obj.industry_type = "INVALID"

    validator = IndustryValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)


def test_invalid_status():

    obj = make()

    obj.status = "INVALID"

    validator = IndustryValidator()

    with pytest.raises(ValueError):

        validator.validate(obj)