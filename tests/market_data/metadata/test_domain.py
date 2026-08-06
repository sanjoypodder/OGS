"""
Tests for Metadata domain.
"""

from ogs.market_data.metadata import (
    Metadata,
    MetadataStatus,
    MetadataType,
    MetadataValueType,
)


def test_default():

    obj = Metadata()

    assert obj.metadata_id == ""
    assert obj.entity_type == ""
    assert obj.entity_id == ""
    assert obj.key == ""
    assert obj.value is None
    assert obj.source == ""

    assert obj.metadata_type == MetadataType.UNKNOWN
    assert obj.status == MetadataStatus.UNKNOWN
    assert obj.value_type == MetadataValueType.STRING

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active


def test_valid():

    obj = Metadata(
        metadata_id="MD001",
        entity_type="Instrument",
        entity_id="INFY",
        key="sector",
    )

    assert obj.is_valid


def test_active():

    obj = Metadata(
        metadata_id="MD001",
        entity_type="Instrument",
        entity_id="INFY",
        key="sector",
        status=MetadataStatus.ACTIVE,
    )

    assert obj.is_active


def test_to_dict():

    obj = Metadata(
        metadata_id="MD001",
        entity_type="Instrument",
        entity_id="INFY",
        key="sector",
        value="IT",
    )

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert data["metadata_id"] == "MD001"
    assert data["entity_type"] == "Instrument"
    assert data["entity_id"] == "INFY"
    assert data["key"] == "sector"
    assert data["value"] == "IT"


def test_string():

    obj = Metadata(
        metadata_id="MD001",
        key="sector",
    )

    assert "Metadata" in str(obj)