"""
Tests for Metadata analyzer performance.
"""

from ogs.market_data.metadata import (
    Metadata,
    MetadataAnalyzer,
    MetadataCollection,
    MetadataStatus,
    MetadataType,
)


def test_large_collection():

    collection = MetadataCollection()

    for i in range(1000):

        collection.add(
            Metadata(
                metadata_id=f"MD{i}",
                entity_type="Instrument",
                entity_id=f"SYM{i}",
                key="sector",
                value="IT",
                metadata_type=MetadataType.SYSTEM,
                status=MetadataStatus.ACTIVE,
            )
        )

    analyzer = MetadataAnalyzer()

    result = analyzer.analyze(collection)

    assert (
        result["summary"]["count"]
        == 1000
    )

    assert (
        result["metadata_analysis"][
            "total_metadata"
        ]
        == 1000
    )

    assert (
        result["metadata_analysis"][
            "active_metadata"
        ]
        == 1000
    )

    assert (
        result["metadata_analysis"][
            "entity_types"
        ]["Instrument"]
        == 1000
    )