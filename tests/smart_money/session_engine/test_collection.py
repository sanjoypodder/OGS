"""
Tests for SessionSeries.
"""

from datetime import datetime, timedelta

from ogs.smart_money.session_engine import (
    Session,
    SessionSeries,
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


def create_series():

    return SessionSeries(
        [
            create_session(
                "XAUUSD",
                SessionType.ASIAN,
                SessionState.CLOSED,
                TradingDay.THURSDAY,
            ),
            create_session(
                "XAUUSD",
                SessionType.LONDON,
                SessionState.ACTIVE,
                TradingDay.THURSDAY,
                active=True,
                tradable=True,
            ),
            create_session(
                "BTCUSD",
                SessionType.NEW_YORK,
                SessionState.PRE_OPEN,
                TradingDay.THURSDAY,
            ),
        ]
    )


def test_create_series():

    series = create_series()

    assert len(series) == 3


def test_append():

    series = create_series()

    session = create_session(
        "EURUSD",
        SessionType.LONDON_CLOSE,
        SessionState.ACTIVE,
        TradingDay.THURSDAY,
    )

    series.append(session)

    assert len(series) == 4


def test_latest():

    series = create_series()

    latest = series.latest()

    assert len(latest) == 1
    assert latest[0].symbol == "BTCUSD"


def test_latest_two():

    series = create_series()

    latest = series.latest(2)

    assert len(latest) == 2


def test_active():

    series = create_series()

    active = series.active()

    assert len(active) == 1
    assert active[0].active


def test_tradable():

    series = create_series()

    tradable = series.tradable()

    assert len(tradable) == 1
    assert tradable[0].tradable


def test_by_session():

    series = create_series()

    result = series.by_session(
        SessionType.LONDON
    )

    assert len(result) == 1
    assert result[0].session == SessionType.LONDON


def test_by_state():

    series = create_series()

    result = series.by_state(
        SessionState.ACTIVE
    )

    assert len(result) == 1


def test_by_day():

    series = create_series()

    result = series.by_day(
        TradingDay.THURSDAY
    )

    assert len(result) == 3


def test_empty_series():

    series = SessionSeries()

    assert len(series) == 0
    assert series.active() == []
    assert series.tradable() == []
    assert series.latest() == []


def test_append_multiple():

    series = SessionSeries()

    for i in range(10):

        series.append(
            create_session(
                f"SYM{i}",
                SessionType.ASIAN,
                SessionState.ACTIVE,
                TradingDay.MONDAY,
            )
        )

    assert len(series) == 10