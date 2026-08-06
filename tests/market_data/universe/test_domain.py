"""
Tests for Universe domain.
"""

from ogs.market_data.universe import (
    Universe,
    UniverseStatus,
    UniverseType,
)


def test_default():

    obj = Universe()

    assert obj.universe_id == ""
    assert obj.universe_name == ""
    assert obj.description == ""
    assert obj.market == ""
    assert obj.owner == ""
    assert obj.symbols == []
    assert obj.source == ""

    assert obj.universe_type == UniverseType.UNKNOWN
    assert obj.status == UniverseStatus.UNKNOWN

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active
    assert obj.symbol_count == 0


def test_valid():

    obj = Universe(
        universe_id="UNI001",
        universe_name="NIFTY500",
    )

    assert obj.is_valid


def test_active():

    obj = Universe(
        universe_id="UNI001",
        universe_name="NIFTY500",
        status=UniverseStatus.ACTIVE,
    )

    assert obj.is_active


def test_add_remove_symbol():

    obj = Universe()

    obj.add_symbol("RELIANCE")
    obj.add_symbol("TCS")

    assert obj.symbol_count == 2

    obj.remove_symbol("RELIANCE")

    assert obj.symbol_count == 1


def test_duplicate_symbol():

    obj = Universe()

    obj.add_symbol("TCS")
    obj.add_symbol("TCS")

    assert obj.symbol_count == 1


def test_to_dict():

    obj = Universe()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "universe_id" in data
    assert "universe_name" in data
    assert "symbols" in data


def test_string():

    obj = Universe()

    assert "Universe" in str(obj)