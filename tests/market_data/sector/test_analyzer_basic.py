"""
Tests for Sector analyzer.
"""

from ogs.market_data.sector import (
    Sector,
    SectorAnalyzer,
    SectorCollection,
    SectorStatus,
    SectorType,
)


def test_analyze():

    collection = SectorCollection()

    collection.add(
        Sector(
            sector_code="BANK",
            sector_name="Banking",
            sector_type=SectorType.PRIMARY,
            status=SectorStatus.ACTIVE,
        )
    )

    analyzer = SectorAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "sector_analysis" in result
    assert "distribution_analysis" in result