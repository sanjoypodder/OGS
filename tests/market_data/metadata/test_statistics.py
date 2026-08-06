"""
Tests for Metadata statistics.
"""

from ogs.market_data.metadata import (
    Metadata,
    MetadataCollection,
    MetadataStatistics,
    MetadataStatus,
    MetadataType,
    MetadataValueType,
)


def make(
    metadata_id,
    entity_type,
    entity_id,
    key,
    value,
    metadata_type,
    value_type,
    status,
):

    return Metadata(
        metadata_id=metadata_id,
        entity_type=entity_type,
        entity_id=entity_id,
        key=key,
        value=value,
        metadata_type=metadata_type,
        value_type=value_type,
        status=status,
    )


def build_collection():

    collection = MetadataCollection()

    collection.add(
        make(
            "MD001",
            "Instrument",
            "INFY",
            "sector",
            "IT",
            MetadataType.SYSTEM,
            MetadataValueType.STRING,
            MetadataStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "MD002",
            "Instrument",
            "TCS",
            "market_cap",
            100,
            MetadataType.MARKET,
            MetadataValueType.INTEGER,
            MetadataStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "MD003",
            "Portfolio",
            "PF001",
            "risk",
            "HIGH",
            MetadataType.RISK,
            MetadataValueType.STRING,
            MetadataStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = MetadataStatistics(
        build_collection()
    )

    assert stats.count == 3
    assert stats.active_count == 2


def test_entity_distribution():

    stats = MetadataStatistics(
        build_collection()
    )

    distribution = stats.entity_distribution()

    assert distribution["Instrument"] == 2
    assert distribution["Portfolio"] == 1


def test_metadata_distribution():

    stats = MetadataStatistics(
        build_collection()
    )

    distribution = stats.metadata_distribution()

    assert distribution["SYSTEM"] == 1
    assert distribution["MARKET"] == 1
    assert distribution["RISK"] == 1


def test_value_distribution():

    stats = MetadataStatistics(
        build_collection()
    )

    distribution = stats.value_distribution()

    assert distribution["STRING"] == 2
    assert distribution["INTEGER"] == 1


def test_summary():

    stats = MetadataStatistics(
        build_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2