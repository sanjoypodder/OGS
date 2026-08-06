"""
Tests for Session statistics.
"""

from ogs.market_data.session import (
    Session,
    SessionCollection,
    SessionStatistics,
    SessionStatus,
    SessionType,
)


def make(idx, status, session_type):

    return Session(
        session_id=str(idx),
        name=f"Session {idx}",
        exchange="NSE",
        market="Cash",
        status=status,
        session_type=session_type,
    )


def build_collection():

    collection = SessionCollection()

    collection.add(
        make(
            1,
            SessionStatus.OPEN,
            SessionType.REGULAR,
        )
    )

    collection.add(
        make(
            2,
            SessionStatus.CLOSED,
            SessionType.PRE_MARKET,
        )
    )

    collection.add(
        make(
            3,
            SessionStatus.OPEN,
            SessionType.REGULAR,
        )
    )

    return collection


def test_counts():

    stats = SessionStatistics(build_collection())

    assert stats.count == 3
    assert stats.active_count == 2
    assert stats.closed_count == 1
    assert stats.regular_count == 2


def test_distribution():

    stats = SessionStatistics(build_collection())

    distribution = stats.distribution()

    assert distribution["REGULAR"] == 2
    assert distribution["PRE_MARKET"] == 1


def test_summary():

    stats = SessionStatistics(build_collection())

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2
    assert summary["closed"] == 1
    assert summary["regular"] == 2