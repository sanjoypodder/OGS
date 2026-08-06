"""
CorporateAction analyzer edge cases.
"""

from ogs.market_data.corporate_action import (
    CorporateActionAnalyzer,
    CorporateActionCollection,
)


def test_empty_collection():

    analyzer = CorporateActionAnalyzer()

    result = analyzer.analyze(
        CorporateActionCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = CorporateActionAnalyzer()

    result = analyzer.analyze(
        CorporateActionCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["action_type"]

    assert isinstance(distribution, dict)