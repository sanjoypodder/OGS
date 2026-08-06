"""
Tests for Metadata analyzer.
"""

from ogs.market_data.metadata import (
    Metadata,
    MetadataAnalyzer,
    MetadataCollection,
    MetadataStatus,
    MetadataType,
)


def test_analyze():

    collection = MetadataCollection()

    collection.add(
        Metadata(
            metadata_id="MD001",
            entity_type="Instrument",
            entity_id="INFY",
            key="sector",
            value="IT",
            metadata_type=MetadataType.SYSTEM,
            status=MetadataStatus.ACTIVE,
        )
    )

    analyzer = MetadataAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "metadata_analysis" in result
    assert "distribution_analysis" in result