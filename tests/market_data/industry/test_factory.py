"""
Tests for Industry factory.
"""

from ogs.market_data.industry import (
    Industry,
    IndustryFactory,
    IndustryStatus,
    IndustryType,
)


def test_create():

    obj = IndustryFactory.create(
        "PVT_BANK",
        "Private Banks",
        "BANK",
    )

    assert isinstance(obj, Industry)


def test_manufacturing():

    obj = IndustryFactory.manufacturing(
        "CEMENT",
        "Cement",
        "MATERIAL",
    )

    assert obj.industry_type == IndustryType.MANUFACTURING
    assert obj.status == IndustryStatus.ACTIVE


def test_technology():

    obj = IndustryFactory.technology(
        "IT_SERVICES",
        "IT Services",
        "IT",
    )

    assert obj.industry_type == IndustryType.TECHNOLOGY
    assert obj.status == IndustryStatus.ACTIVE


def test_clone():

    obj = IndustryFactory.create(
        "PVT_BANK",
        "Private Banks",
        "BANK",
    )

    clone = IndustryFactory.clone(obj)

    assert clone == obj
    assert clone is not obj