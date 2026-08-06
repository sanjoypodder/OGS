"""
Tests for Industry statistics.
"""

from ogs.market_data.industry import (
    Industry,
    IndustryCollection,
    IndustryStatistics,
    IndustryStatus,
    IndustryType,
)


def make(code, name, sector, industry_type, status):

    return Industry(
        industry_code=code,
        industry_name=name,
        sector_code=sector,
        industry_type=industry_type,
        status=status,
    )


def build_collection():

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

    collection.add(
        make(
            "PHARMA",
            "Pharmaceuticals",
            "HEALTH",
            IndustryType.HEALTHCARE,
            IndustryStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = IndustryStatistics(build_collection())

    assert stats.count == 3
    assert stats.active_count == 2


def test_distribution():

    stats = IndustryStatistics(build_collection())

    distribution = stats.distribution()

    assert distribution["FINANCIAL"] == 1
    assert distribution["TECHNOLOGY"] == 1
    assert distribution["HEALTHCARE"] == 1


def test_summary():

    stats = IndustryStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2