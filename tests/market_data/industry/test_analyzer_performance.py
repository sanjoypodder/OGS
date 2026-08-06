"""
Tests for Industry analyzer performance.
"""

from ogs.market_data.industry import (
    Industry,
    IndustryAnalyzer,
    IndustryCollection,
    IndustryStatus,
    IndustryType,
)


def test_large_collection():

    collection = IndustryCollection()

    for i in range(1000):

        collection.add(
            Industry(
                industry_code=f"IND{i}",
                industry_name=f"Industry {i}",
                sector_code="TEST",
                industry_type=IndustryType.MANUFACTURING,
                status=IndustryStatus.ACTIVE,
            )
        )

    analyzer = IndustryAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000

    assert (
        result["industry_analysis"]["total_industries"]
        == 1000
    )

    assert (
        result["industry_analysis"]["active_industries"]
        == 1000
    )