"""
Tests for Sector analyzer performance.
"""

from ogs.market_data.sector import (
    Sector,
    SectorAnalyzer,
    SectorCollection,
    SectorStatus,
    SectorType,
)


def test_large_collection():

    collection = SectorCollection()

    for i in range(1000):

        collection.add(
            Sector(
                sector_code=f"S{i}",
                sector_name=f"Sector {i}",
                sector_type=SectorType.PRIMARY,
                status=SectorStatus.ACTIVE,
            )
        )

    analyzer = SectorAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000

    assert (
        result["sector_analysis"]["total_sectors"]
        == 1000
    )

    assert (
        result["sector_analysis"]["active_sectors"]
        == 1000
    )