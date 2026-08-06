"""
Tests for Sector analyzer distribution.
"""

from ogs.market_data.sector import (
    Sector,
    SectorAnalyzer,
    SectorCollection,
    SectorStatus,
    SectorType,
)


def test_distribution_detection():

    collection = SectorCollection()

    collection.add(
        Sector(
            sector_code="BANK",
            sector_name="Banking",
            sector_type=SectorType.PRIMARY,
            status=SectorStatus.ACTIVE,
        )
    )

    collection.add(
        Sector(
            sector_code="AI",
            sector_name="Artificial Intelligence",
            sector_type=SectorType.THEMATIC,
            status=SectorStatus.ACTIVE,
        )
    )

    analyzer = SectorAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert (
        distribution["sector_type"]["PRIMARY"]
        == 1
    )

    assert (
        distribution["sector_type"]["THEMATIC"]
        == 1
    )