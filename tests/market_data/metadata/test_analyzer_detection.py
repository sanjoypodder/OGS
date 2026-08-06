"""
Tests for Metadata analyzer distribution.
"""

from ogs.market_data.metadata import (
    Metadata,
    MetadataAnalyzer,
    MetadataCollection,
    MetadataStatus,
    MetadataType,
)


def test_distribution_detection():

    collection = MetadataCollection()

    collection.add(
        Metadata(
            metadata_id="MD001",
            entity_type="Instrument",
            entity_id="INFY",
            key="sector",
            metadata_type=MetadataType.SYSTEM,
            status=MetadataStatus.ACTIVE,
        )
    )

    collection.add(
        Metadata(
            metadata_id="MD002",
            entity_type="Portfolio",
            entity_id="PF001",
            key="risk",
            metadata_type=MetadataType.RISK,
            status=MetadataStatus.ACTIVE,
        )
    )

    analyzer = MetadataAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result[
        "distribution_analysis"
    ]

    assert (
        distribution["metadata_type"]["SYSTEM"]
        == 1
    )

    assert (
        distribution["metadata_type"]["RISK"]
        == 1
    )