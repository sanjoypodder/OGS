"""
Tests for Metadata factory.
"""

from ogs.market_data.metadata import (
    Metadata,
    MetadataFactory,
    MetadataStatus,
    MetadataType,
)


def test_create():

    obj = MetadataFactory.create(
        "MD001",
        "Instrument",
        "INFY",
        "sector",
        "IT",
    )

    assert isinstance(obj, Metadata)


def test_system():

    obj = MetadataFactory.system(
        "MD001",
        "Instrument",
        "INFY",
        "sector",
        "IT",
    )

    assert obj.metadata_type == MetadataType.SYSTEM
    assert obj.status == MetadataStatus.ACTIVE


def test_market():

    obj = MetadataFactory.market(
        "MD002",
        "Instrument",
        "INFY",
        "exchange",
        "NSE",
    )

    assert obj.metadata_type == MetadataType.MARKET


def test_smart_money():

    obj = MetadataFactory.smart_money(
        "MD003",
        "Instrument",
        "INFY",
        "ob",
        True,
    )

    assert obj.metadata_type == MetadataType.SMART_MONEY


def test_ai():

    obj = MetadataFactory.ai(
        "MD004",
        "Instrument",
        "INFY",
        "score",
        0.95,
    )

    assert obj.metadata_type == MetadataType.AI


def test_clone():

    obj = MetadataFactory.create(
        "MD001",
        "Instrument",
        "INFY",
        "sector",
        "IT",
    )

    clone = MetadataFactory.clone(obj)

    assert clone == obj
    assert clone is not obj