"""
Tests for SessionFactory.
"""

from datetime import datetime, timedelta

import pytest

from ogs.smart_money.session_engine import (
    Session,
    SessionFactory,
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)


def test_factory_create():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=3)

    session = SessionFactory.create(
        symbol="XAUUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
        timezone=TimeZoneType.UTC,
        active=True,
        tradable=True,
    )

    assert isinstance(session, Session)


def test_factory_symbol():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=3)

    session = SessionFactory.create(
        symbol="BTCUSD",
        session=SessionType.NEW_YORK,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
    )

    assert session.symbol == "BTCUSD"


def test_factory_default_timezone():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=3)

    session = SessionFactory.create(
        symbol="EURUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
    )

    assert session.timezone == TimeZoneType.UTC


def test_factory_default_flags():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=3)

    session = SessionFactory.create(
        symbol="EURUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
    )

    assert session.active is False
    assert session.tradable is False


@pytest.mark.parametrize(
    "session_type",
    [
        SessionType.ASIAN,
        SessionType.LONDON,
        SessionType.NEW_YORK,
        SessionType.LONDON_CLOSE,
        SessionType.CUSTOM,
    ],
)
def test_factory_all_session_types(session_type):

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=2)

    session = SessionFactory.create(
        symbol="XAUUSD",
        session=session_type,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
    )

    assert session.session == session_type


def test_factory_invalid_symbol():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=2)

    with pytest.raises(ValueError):

        SessionFactory.create(
            symbol="",
            session=SessionType.LONDON,
            state=SessionState.ACTIVE,
            trading_day=TradingDay.THURSDAY,
            start_time=start,
            end_time=end,
        )


def test_factory_invalid_time():

    start = datetime(2026, 1, 1, 9, 0)
    end = datetime(2026, 1, 1, 7, 0)

    with pytest.raises(ValueError):

        SessionFactory.create(
            symbol="XAUUSD",
            session=SessionType.LONDON,
            state=SessionState.ACTIVE,
            trading_day=TradingDay.THURSDAY,
            start_time=start,
            end_time=end,
        )


def test_factory_custom_timezone():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=2)

    session = SessionFactory.create(
        symbol="XAUUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
        timezone=TimeZoneType.LONDON,
    )

    assert session.timezone == TimeZoneType.LONDON


def test_factory_flags():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=2)

    session = SessionFactory.create(
        symbol="XAUUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
        active=True,
        tradable=True,
    )

    assert session.active
    assert session.tradable


def test_factory_duration():

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=4)

    session = SessionFactory.create(
        symbol="XAUUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        start_time=start,
        end_time=end,
    )

    assert session.duration_hours == 4