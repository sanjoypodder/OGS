"""
Tests for Industry collection.
"""

from ogs.market_data.industry import (
    Industry,
    IndustryCollection,
    IndustryStatus,
    IndustryType,
)


def make(
    code,
    name,
    sector,
    industry_type,
    status,
):

    return Industry(
        industry_code=code,
        industry_name=name,
        sector_code=sector,
        industry_type=industry_type,
        status=status,
    )


def test_add():

    collection = IndustryCollection()

    collection.add(
        make(
            "PVT_BANK",
            "Private Banks",
            "BANK",
            IndustryType.FINANCIAL,
            IndustryStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = IndustryCollection()

    obj = make(
        "PVT_BANK",
        "Private Banks",
        "BANK",
        IndustryType.FINANCIAL,
        IndustryStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("PVT_BANK") == obj
    assert collection.find("IT_SERVICES") is None


def test_by_type():

    collection = IndustryCollection()

    collection.add(
        make(
            "PVT_BANK",
            "Private Banks",
            "BANK",
            IndustryType.FINANCIAL,
            IndustryStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "IT_SERVICES",
            "IT Services",
            "IT",
            IndustryType.TECHNOLOGY,
            IndustryStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            IndustryType.FINANCIAL
        )
    ) == 1

    assert len(
        collection.by_type(
            IndustryType.TECHNOLOGY
        )
    ) == 1


def test_active():

    collection = IndustryCollection()

    collection.add(
        make(
            "PVT_BANK",
            "Private Banks",
            "BANK",
            IndustryType.FINANCIAL,
            IndustryStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "OLD",
            "Old Industry",
            "BANK",
            IndustryType.SERVICES,
            IndustryStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = IndustryCollection()

    collection.add(
        make(
            "PVT_BANK",
            "Private Banks",
            "BANK",
            IndustryType.FINANCIAL,
            IndustryStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1