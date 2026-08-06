"""
Tests for Index domain.
"""

from ogs.market_data.index import (
    Index,
    IndexStatus,
    IndexType,
)


def test_default():

    obj = Index()

    assert obj.index_code == ""
    assert obj.index_name == ""
    assert obj.exchange == ""
    assert obj.market == ""
    assert obj.currency_code == ""
    assert obj.country == ""

    assert obj.index_type == IndexType.UNKNOWN
    assert obj.status == IndexStatus.UNKNOWN

    assert obj.base_value == 0.0
    assert obj.current_value == 0.0
    assert obj.constituent_count == 0

    assert obj.active

    assert not obj.is_valid
    assert not obj.is_active


def test_valid():

    obj = Index(
        index_code="NIFTY50",
        index_name="NIFTY 50",
        exchange="NSE",
    )

    assert obj.is_valid


def test_active():

    obj = Index(
        index_code="NIFTY50",
        index_name="NIFTY 50",
        exchange="NSE",
        status=IndexStatus.ACTIVE,
    )

    assert obj.is_active


def test_to_dict():

    obj = Index()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "index_code" in data
    assert "index_name" in data
    assert "index_type" in data


def test_string():

    obj = Index()

    assert "Index" in str(obj)