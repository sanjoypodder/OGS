"""
Tests for Sector collection.
"""

from ogs.market_data.sector import (
    Sector,
    SectorCollection,
    SectorStatus,
    SectorType,
)


def make(
    code,
    name,
    sector_type,
    status,
):

    return Sector(
        sector_code=code,
        sector_name=name,
        sector_type=sector_type,
        status=status,
    )


def test_add():

    collection = SectorCollection()

    collection.add(
        make(
            "BANK",
            "Banking",
            SectorType.PRIMARY,
            SectorStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = SectorCollection()

    obj = make(
        "BANK",
        "Banking",
        SectorType.PRIMARY,
        SectorStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("BANK") == obj
    assert collection.find("IT") is None


def test_by_type():

    collection = SectorCollection()

    collection.add(
        make(
            "BANK",
            "Banking",
            SectorType.PRIMARY,
            SectorStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "AI",
            "Artificial Intelligence",
            SectorType.THEMATIC,
            SectorStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            SectorType.PRIMARY
        )
    ) == 1

    assert len(
        collection.by_type(
            SectorType.THEMATIC
        )
    ) == 1


def test_active():

    collection = SectorCollection()

    collection.add(
        make(
            "BANK",
            "Banking",
            SectorType.PRIMARY,
            SectorStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "OLD",
            "Old Sector",
            SectorType.SECONDARY,
            SectorStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = SectorCollection()

    collection.add(
        make(
            "BANK",
            "Banking",
            SectorType.PRIMARY,
            SectorStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1