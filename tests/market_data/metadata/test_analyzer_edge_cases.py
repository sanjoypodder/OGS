"""
Tests for Metadata analyzer edge cases.
"""

from ogs.market_data.metadata import (
    MetadataAnalyzer,
    MetadataCollection,
)


def test_empty_collection():

    analyzer = MetadataAnalyzer()

    result = analyzer.analyze(
        MetadataCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = MetadataAnalyzer()

    result = analyzer.analyze(
        MetadataCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]

    assert isinstance(
        distribution["metadata_type"],
        dict,
    )

    assert isinstance(
        distribution["value_type"],
        dict,
    )