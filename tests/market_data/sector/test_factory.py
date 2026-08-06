"""
Tests for Sector factory.
"""

from ogs.market_data.sector import (
    Sector,
    SectorFactory,
    SectorStatus,
    SectorType,
)


def test_create():

    obj = SectorFactory.create(
        "BANK",
        "Banking",
    )

    assert isinstance(obj, Sector)


def test_primary():

    obj = SectorFactory.primary(
        "BANK",
        "Banking",
    )

    assert obj.sector_type == SectorType.PRIMARY
    assert obj.status == SectorStatus.ACTIVE


def test_thematic():

    obj = SectorFactory.thematic(
        "AI",
        "Artificial Intelligence",
    )

    assert obj.sector_type == SectorType.THEMATIC
    assert obj.status == SectorStatus.ACTIVE


def test_clone():

    obj = SectorFactory.create(
        "BANK",
        "Banking",
    )

    clone = SectorFactory.clone(obj)

    assert clone == obj
    assert clone is not obj