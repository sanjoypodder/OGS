"""
Tests for Session domain.
"""

from ogs.market_data.session import (
    Session,
    SessionStatus,
    SessionType,
)


def test_default():

    obj = Session()

    assert obj.session_id == ""
    assert obj.name == ""
    assert obj.exchange == ""
    assert obj.market == ""

    assert obj.session_type == SessionType.UNKNOWN
    assert obj.status == SessionStatus.CLOSED

    assert obj.timezone == "UTC"

    assert not obj.is_active
    assert not obj.is_valid


def test_valid():

    obj = Session(
        session_id="1",
        name="Regular",
        exchange="NSE",
        market="Cash",
    )

    assert obj.is_valid


def test_active():

    obj = Session(
        session_id="1",
        name="Regular",
        exchange="NSE",
        market="Cash",
        status=SessionStatus.OPEN,
    )

    assert obj.is_active


def test_to_dict():

    obj = Session()

    data = obj.to_dict()

    assert isinstance(data, dict)

    assert "session_id" in data


def test_string():

    obj = Session()

    assert "Session" in str(obj)