"""
Tests for Index analyzer edge cases.
"""

from ogs.market_data.index import (
    IndexAnalyzer,
    IndexCollection,
)


def test_empty_collection():

    analyzer = IndexAnalyzer()

    result = analyzer.analyze(
        IndexCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = IndexAnalyzer()

    result = analyzer.analyze(
        IndexCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["index_type"]

    assert isinstance(distribution, dict)