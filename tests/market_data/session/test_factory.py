"""
Tests for Session factory.
"""

from ogs.market_data.session import (
    Session,
    SessionFactory,
    SessionStatus,
    SessionType,
)


def test_create():

    obj = SessionFactory.create(
        "1",
        "Regular",
        "NSE",
        "Cash",
    )

    assert isinstance(obj, Session)


def test_regular():

    obj = SessionFactory.regular(
        "1",
        "Regular",
        "NSE",
        "Cash",
    )

    assert obj.session_type == SessionType.REGULAR

    assert obj.status == SessionStatus.OPEN


def test_clone():

    obj = SessionFactory.create(
        "1",
        "Regular",
        "NSE",
        "Cash",
    )

    clone = SessionFactory.clone(obj)

    assert clone == obj

    assert clone is not obj