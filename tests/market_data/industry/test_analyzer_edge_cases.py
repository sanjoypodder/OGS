"""
Tests for Industry analyzer edge cases.
"""

from ogs.market_data.industry import (
    IndustryAnalyzer,
    IndustryCollection,
)


def test_empty_collection():

    analyzer = IndustryAnalyzer()

    result = analyzer.analyze(
        IndustryCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = IndustryAnalyzer()

    result = analyzer.analyze(
        IndustryCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["industry_type"]

    assert isinstance(distribution, dict)