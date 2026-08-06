"""
Tests for SessionStatistics.
"""

from datetime import datetime, timedelta

from ogs.smart_money.session_engine import (
    Session,
    SessionSeries,
    SessionStatistics,
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)


def create_session(
    symbol: str,
    session_type: SessionType,
    state: SessionState,
    day: TradingDay,
    active: bool = False,
    tradable: bool = False,
):

    start = datetime(2026, 1, 1, 7, 0)
    end = start + timedelta(hours=2)

    return Session(
        symbol=symbol,
        session=session_type,
        state=state,
        trading_day=day,
        timezone=TimeZoneType.UTC,
        start_time=start,
        end_time=end,
        active=active,
        tradable=tradable,
    )


def create_statistics():

    series = SessionSeries(
        [
            create_session(
                "XAUUSD",
                SessionType.ASIAN,
                SessionState.CLOSED,
                TradingDay.MONDAY,
            ),
            create_session(
                "XAUUSD",
                SessionType.LONDON,
                SessionState.ACTIVE,
                TradingDay.MONDAY,
                active=True,
                tradable=True,
            ),
            create_session(
                "BTCUSD",
                SessionType.NEW_YORK,
                SessionState.PRE_OPEN,
                TradingDay.FRIDAY,
            ),
        ]
    )

    return SessionStatistics(series)


def test_total_count():

    stats = create_statistics()

    assert stats.count == 3


def test_active_count():

    stats = create_statistics()

    assert stats.active_count == 1


def test_tradable_count():

    stats = create_statistics()

    assert stats.tradable_count == 1


def test_closed_count():

    stats = create_statistics()

    assert stats.closed_count == 1


def test_pre_open_count():

    stats = create_statistics()

    assert stats.pre_open_count == 1


def test_session_counts():

    stats = create_statistics()

    assert stats.asian_count == 1
    assert stats.london_count == 1
    assert stats.new_york_count == 1
    assert stats.london_close_count == 0


def test_day_counts():

    stats = create_statistics()

    assert stats.monday_count == 2
    assert stats.friday_count == 1


def test_average_duration():

    stats = create_statistics()

    assert stats.average_duration_minutes == 120


def test_latest():

    stats = create_statistics()

    assert stats.latest.symbol == "BTCUSD"


def test_oldest():

    stats = create_statistics()

    assert stats.oldest.symbol == "XAUUSD"


def test_current_active():

    stats = create_statistics()

    active = stats.current_active

    assert active is not None
    assert active.session == SessionType.LONDON


def test_empty_statistics():

    stats = SessionStatistics(SessionSeries())

    assert stats.count == 0
    assert stats.active_count == 0
    assert stats.tradable_count == 0
    assert stats.average_duration_minutes == 0.0
    assert stats.latest is None
    assert stats.oldest is None
    assert stats.current_active is None