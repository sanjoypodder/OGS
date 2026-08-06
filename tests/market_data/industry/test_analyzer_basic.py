"""
Tests for Industry analyzer.
"""

from ogs.market_data.industry import (
    Industry,
    IndustryAnalyzer,
    IndustryCollection,
    IndustryStatus,
    IndustryType,
)


def test_analyze():

    collection = IndustryCollection()

    collection.add(
        Industry(
            industry_code="PVT_BANK",
            industry_name="Private Banks",
            sector_code="BANK",
            industry_type=IndustryType.FINANCIAL,
            status=IndustryStatus.ACTIVE,
        )
    )

    analyzer = IndustryAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "industry_analysis" in result
    assert "distribution_analysis" in result