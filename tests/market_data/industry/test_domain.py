"""
Tests for Industry domain.
"""

from ogs.market_data.industry import (
    Industry,
    IndustryStatus,
    IndustryType,
)


def test_default():

    obj = Industry()

    assert obj.industry_code == ""
    assert obj.industry_name == ""
    assert obj.sector_code == ""
    assert obj.market == ""
    assert obj.country == ""
    assert obj.description == ""

    assert obj.industry_type == IndustryType.UNKNOWN
    assert obj.status == IndustryStatus.UNKNOWN

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active


def test_valid():

    obj = Industry(
        industry_code="PVT_BANK",
        industry_name="Private Banks",
        sector_code="BANK",
    )

    assert obj.is_valid


def test_active():

    obj = Industry(
        industry_code="PVT_BANK",
        industry_name="Private Banks",
        sector_code="BANK",
        status=IndustryStatus.ACTIVE,
    )

    assert obj.is_active


def test_to_dict():

    obj = Industry()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "industry_code" in data
    assert "industry_name" in data
    assert "industry_type" in data


def test_string():

    obj = Industry()

    assert "Industry" in str(obj)