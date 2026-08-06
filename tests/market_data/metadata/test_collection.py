"""
Tests for Metadata collection.
"""

from ogs.market_data.metadata import (
    Metadata,
    MetadataCollection,
    MetadataStatus,
    MetadataType,
)


def make(
    metadata_id,
    entity_type,
    entity_id,
    key,
    metadata_type,
    status,
):

    return Metadata(
        metadata_id=metadata_id,
        entity_type=entity_type,
        entity_id=entity_id,
        key=key,
        metadata_type=metadata_type,
        status=status,
    )


def test_add():

    collection = MetadataCollection()

    collection.add(
        make(
            "MD001",
            "Instrument",
            "INFY",
            "sector",
            MetadataType.SYSTEM,
            MetadataStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = MetadataCollection()

    obj = make(
        "MD001",
        "Instrument",
        "INFY",
        "sector",
        MetadataType.SYSTEM,
        MetadataStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("MD001") == obj
    assert collection.find("UNKNOWN") is None


def test_by_entity():

    collection = MetadataCollection()

    collection.add(
        make(
            "MD001",
            "Instrument",
            "INFY",
            "sector",
            MetadataType.SYSTEM,
            MetadataStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "MD002",
            "Instrument",
            "INFY",
            "industry",
            MetadataType.SYSTEM,
            MetadataStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_entity(
            "Instrument",
            "INFY",
        )
    ) == 2


def test_by_key():

    collection = MetadataCollection()

    collection.add(
        make(
            "MD001",
            "Instrument",
            "INFY",
            "sector",
            MetadataType.SYSTEM,
            MetadataStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_key(
            "sector",
        )
    ) == 1


def test_by_type():

    collection = MetadataCollection()

    collection.add(
        make(
            "MD001",
            "Instrument",
            "INFY",
            "sector",
            MetadataType.SYSTEM,
            MetadataStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            MetadataType.SYSTEM,
        )
    ) == 1


def test_active():

    collection = MetadataCollection()

    collection.add(
        make(
            "MD001",
            "Instrument",
            "INFY",
            "sector",
            MetadataType.SYSTEM,
            MetadataStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "MD002",
            "Instrument",
            "TCS",
            "sector",
            MetadataType.SYSTEM,
            MetadataStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = MetadataCollection()

    collection.add(
        make(
            "MD001",
            "Instrument",
            "INFY",
            "sector",
            MetadataType.SYSTEM,
            MetadataStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1