"""
Tests for Sector statistics.
"""

from ogs.market_data.sector import (
    Sector,
    SectorCollection,
    SectorStatistics,
    SectorStatus,
    SectorType,
)


def make(code, name, sector_type, status):

    return Sector(
        sector_code=code,
        sector_name=name,
        sector_type=sector_type,
        status=status,
    )


def build_collection():

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
            "IT",
            "Information Technology",
            SectorType.TERTIARY,
            SectorStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "AI",
            "Artificial Intelligence",
            SectorType.THEMATIC,
            SectorStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = SectorStatistics(build_collection())

    assert stats.count == 3
    assert stats.active_count == 2


def test_distribution():

    stats = SectorStatistics(build_collection())

    distribution = stats.distribution()

    assert distribution["PRIMARY"] == 1
    assert distribution["TERTIARY"] == 1
    assert distribution["THEMATIC"] == 1


def test_summary():

    stats = SectorStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2