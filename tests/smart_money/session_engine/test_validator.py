"""
Tests for SessionValidator.
"""

from datetime import datetime, timedelta

import pytest

from ogs.smart_money.session_engine import (
    Session,
    SessionState,
    SessionType,
    SessionValidator,
    TimeZoneType,
    TradingDay,
)


def create_valid_session():

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


def test_validator_creation():

    validator = SessionValidator()

    assert validator is not None


def test_validate_valid_session():

    validator = SessionValidator()

    session = create_valid_session()

    assert validator.validate(session)


def test_invalid_empty_symbol():

    validator = SessionValidator()

    session = create_valid_session()

    session = Session(
        symbol="",
        session=session.session,
        state=session.state,
        trading_day=session.trading_day,
        timezone=session.timezone,
        start_time=session.start_time,
        end_time=session.end_time,
        active=session.active,
        tradable=session.tradable,
    )

    assert not validator.validate(session)


def test_invalid_none_symbol():

    validator = SessionValidator()

    session = create_valid_session()

    session = Session(
        symbol=None,
        session=session.session,
        state=session.state,
        trading_day=session.trading_day,
        timezone=session.timezone,
        start_time=session.start_time,
        end_time=session.end_time,
        active=session.active,
        tradable=session.tradable,
    )

    assert not validator.validate(session)


def test_invalid_start_after_end():

    validator = SessionValidator()

    end = datetime(2026, 1, 1, 7, 0)
    start = end + timedelta(hours=1)

    session = Session(
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

    assert not validator.validate(session)


def test_invalid_equal_times():

    validator = SessionValidator()

    start = datetime(2026, 1, 1, 7, 0)

    session = Session(
        symbol="XAUUSD",
        session=SessionType.LONDON,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        timezone=TimeZoneType.UTC,
        start_time=start,
        end_time=start,
        active=True,
        tradable=True,
    )

    assert not validator.validate(session)


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
def test_all_session_types(session_type):

    validator = SessionValidator()

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=1)

    session = Session(
        symbol="BTCUSD",
        session=session_type,
        state=SessionState.ACTIVE,
        trading_day=TradingDay.THURSDAY,
        timezone=TimeZoneType.UTC,
        start_time=start,
        end_time=end,
        active=True,
        tradable=True,
    )

    assert validator.validate(session)


@pytest.mark.parametrize(
    "state",
    [
        SessionState.PRE_OPEN,
        SessionState.ACTIVE,
        SessionState.CLOSING,
        SessionState.CLOSED,
    ],
)
def test_all_states(state):

    validator = SessionValidator()

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=1)

    session = Session(
        symbol="BTCUSD",
        session=SessionType.LONDON,
        state=state,
        trading_day=TradingDay.THURSDAY,
        timezone=TimeZoneType.UTC,
        start_time=start,
        end_time=end,
        active=False,
        tradable=False,
    )

    assert validator.validate(session)