"""
Tests for Industry analyzer distribution.
"""

from ogs.market_data.industry import (
    Industry,
    IndustryAnalyzer,
    IndustryCollection,
    IndustryStatus,
    IndustryType,
)


def test_distribution_detection():

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

    collection.add(
        Industry(
            industry_code="IT_SERVICES",
            industry_name="IT Services",
            sector_code="IT",
            industry_type=IndustryType.TECHNOLOGY,
            status=IndustryStatus.ACTIVE,
        )
    )

    analyzer = IndustryAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert (
        distribution["industry_type"]["FINANCIAL"]
        == 1
    )

    assert (
        distribution["industry_type"]["TECHNOLOGY"]
        == 1
    )