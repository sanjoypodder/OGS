"""
Tests for Sector domain.
"""

from ogs.market_data.sector import (
    Sector,
    SectorStatus,
    SectorType,
)


def test_default():

    obj = Sector()

    assert obj.sector_code == ""
    assert obj.sector_name == ""
    assert obj.market == ""
    assert obj.country == ""
    assert obj.description == ""
    assert obj.parent_sector == ""

    assert obj.sector_type == SectorType.UNKNOWN
    assert obj.status == SectorStatus.UNKNOWN

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active


def test_valid():

    obj = Sector(
        sector_code="BANK",
        sector_name="Banking",
    )

    assert obj.is_valid


def test_active():

    obj = Sector(
        sector_code="BANK",
        sector_name="Banking",
        status=SectorStatus.ACTIVE,
    )

    assert obj.is_active


def test_to_dict():

    obj = Sector()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "sector_code" in data
    assert "sector_name" in data
    assert "sector_type" in data


def test_string():

    obj = Sector()

    assert "Sector" in str(obj)