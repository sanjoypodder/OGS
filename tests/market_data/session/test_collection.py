"""
Tests for Session collection.
"""

from ogs.market_data.session import (
    Session,
    SessionCollection,
    SessionStatus,
    SessionType,
)


def make(
    id_,
    status,
    session_type,
):

    return Session(
        session_id=id_,
        name=id_,
        exchange="NSE",
        market="Cash",
        status=status,
        session_type=session_type,
    )


def test_add():

    collection = SessionCollection()

    collection.add(
        make(
            "1",
            SessionStatus.OPEN,
            SessionType.REGULAR,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = SessionCollection()

    obj = make(
        "ABC",
        SessionStatus.OPEN,
        SessionType.REGULAR,
    )

    collection.add(obj)

    assert collection.find("ABC") == obj

    assert collection.find("XYZ") is None


def test_filters():

    collection = SessionCollection()

    collection.add(
        make(
            "1",
            SessionStatus.OPEN,
            SessionType.REGULAR,
        )
    )

    collection.add(
        make(
            "2",
            SessionStatus.CLOSED,
            SessionType.PRE_MARKET,
        )
    )

    assert len(collection.active()) == 1

    assert len(collection.closed()) == 1

    assert len(collection.regular()) == 1


def test_to_list():

    collection = SessionCollection()

    collection.add(
        make(
            "1",
            SessionStatus.OPEN,
            SessionType.REGULAR,
        )
    )

    assert len(collection.to_list()) == 1