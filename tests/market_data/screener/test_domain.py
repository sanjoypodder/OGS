"""
Tests for Screener domain.
"""

from ogs.market_data.screener import (
    Screener,
    ScreenerStatus,
    ScreenerType,
)


def test_default():

    obj = Screener()

    assert obj.screener_id == ""
    assert obj.screener_name == ""
    assert obj.description == ""
    assert obj.market == ""
    assert obj.owner == ""
    assert obj.filters == []
    assert obj.sort_by == ""
    assert obj.sort_order == "ASC"

    assert obj.screener_type == ScreenerType.UNKNOWN
    assert obj.status == ScreenerStatus.UNKNOWN

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active
    assert obj.filter_count == 0


def test_valid():

    obj = Screener(
        screener_id="SCR001",
        screener_name="SMC",
    )

    assert obj.is_valid


def test_active():

    obj = Screener(
        screener_id="SCR001",
        screener_name="SMC",
        status=ScreenerStatus.ACTIVE,
    )

    assert obj.is_active


def test_add_remove_filter():

    obj = Screener()

    rule1 = {
        "field": "volume",
        "operator": ">",
        "value": 100000,
    }

    rule2 = {
        "field": "rsi",
        "operator": "<",
        "value": 30,
    }

    obj.add_filter(rule1)
    obj.add_filter(rule2)

    assert obj.filter_count == 2

    obj.remove_filter(rule1)

    assert obj.filter_count == 1


def test_to_dict():

    obj = Screener()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "screener_id" in data
    assert "screener_name" in data
    assert "filters" in data


def test_string():

    obj = Screener()

    assert "Screener" in str(obj)