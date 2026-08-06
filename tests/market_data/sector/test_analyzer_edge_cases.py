"""
Tests for Sector analyzer edge cases.
"""

from ogs.market_data.sector import (
    SectorAnalyzer,
    SectorCollection,
)


def test_empty_collection():

    analyzer = SectorAnalyzer()

    result = analyzer.analyze(
        SectorCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = SectorAnalyzer()

    result = analyzer.analyze(
        SectorCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["sector_type"]

    assert isinstance(distribution, dict)