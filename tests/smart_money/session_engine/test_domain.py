"""
Tests for Session domain object.
"""

from datetime import datetime, timedelta

from ogs.smart_money.session_engine import (
    Session,
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)


def create_session():

    start = datetime(2026, 1, 1, 7, 0, 0)
    end = start + timedelta(hours=3)

    return Session(
        symbol="XAUUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        timezone=TimeZoneType.UTC,
        start_time=start,
        end_time=end,
        active=True,
        tradable=True,
    )


def test_create_session():

    session = create_session()

    assert session.symbol == "XAUUSD"
    assert session.session == SessionType.LONDON
    assert session.state == SessionState.ACTIVE
    assert session.trading_day == TradingDay.THURSDAY
    assert session.timezone == TimeZoneType.UTC
    assert session.active is True
    assert session.tradable is True


def test_duration_seconds():

    session = create_session()

    assert session.duration_seconds == 10800


def test_duration_minutes():

    session = create_session()

    assert session.duration_minutes == 180


def test_duration_hours():

    session = create_session()

    assert session.duration_hours == 3


def test_contains_inside():

    session = create_session()

    ts = session.start_time + timedelta(minutes=30)

    assert session.contains(ts)


def test_contains_outside():

    session = create_session()

    ts = session.end_time + timedelta(minutes=5)

    assert not session.contains(ts)


def test_is_open():

    session = create_session()

    ts = session.start_time + timedelta(minutes=1)

    assert session.is_open(ts)


def test_is_closed():

    session = create_session()

    ts = session.end_time + timedelta(minutes=1)

    assert session.is_closed(ts)


def test_is_upcoming():

    session = create_session()

    ts = session.start_time - timedelta(minutes=30)

    assert session.is_upcoming(ts)


def test_is_tradable():

    session = create_session()

    assert session.is_tradable()


def test_dataclass_is_frozen():

    session = create_session()

    try:
        session.symbol = "BTCUSD"
        assert False, "Frozen dataclass should not allow assignment."
    except Exception:
        assert True