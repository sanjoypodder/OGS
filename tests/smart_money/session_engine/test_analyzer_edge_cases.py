"""
Edge case tests for SessionAnalyzer.
"""

from datetime import datetime

import pytest

from ogs.smart_money.session_engine import (
    SessionAnalyzer,
    SessionState,
    SessionType,
    TradingDay,
)


@pytest.fixture
def analyzer():
    return SessionAnalyzer()


def test_midnight(analyzer):

    session = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 0, 0),
    )

    assert session is not None
    assert session.session == SessionType.ASIAN


def test_last_minute_asian(analyzer):

    session = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 2, 59),
    )

    assert session is not None
    assert session.session == SessionType.ASIAN


def test_exact_london_open(analyzer):

    session = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 7, 0),
    )

    assert session is not None
    assert session.session == SessionType.LONDON


def test_exact_newyork_open(analyzer):

    session = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 12, 0),
    )

    assert session is not None
    assert session.session == SessionType.NEW_YORK


def test_exact_london_close_open(analyzer):

    session = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 15, 0),
    )

    assert session is not None
    assert session.session in (
        SessionType.NEW_YORK,
        SessionType.LONDON_CLOSE,
    )


def test_weekend_saturday(analyzer):

    series = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 3, 8, 0),   # Saturday
    )

    for session in series:
        assert session.trading_day == TradingDay.SATURDAY
        assert not session.tradable


def test_weekend_sunday(analyzer):

    series = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 4, 8, 0),   # Sunday
    )

    for session in series:
        assert session.trading_day == TradingDay.SUNDAY
        assert not session.tradable


def test_far_future(analyzer):

    session = analyzer.active(
        "BTCUSD",
        datetime(2040, 5, 1, 8, 0),
    )

    assert session is not None
    assert session.session == SessionType.LONDON


def test_far_past(analyzer):

    session = analyzer.active(
        "BTCUSD",
        datetime(2020, 5, 1, 8, 0),
    )

    assert session is not None
    assert session.session == SessionType.LONDON


def test_unknown_symbol(analyzer):

    session = analyzer.active(
        "UNKNOWN_SYMBOL",
        datetime(2026, 1, 1, 8, 0),
    )

    assert session is not None
    assert session.symbol == "UNKNOWN_SYMBOL"


def test_no_active_at_night(analyzer):

    session = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 22, 0),
    )

    assert session is None


def test_all_sessions_have_valid_state(analyzer):

    series = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    valid_states = {
        SessionState.PRE_OPEN,
        SessionState.ACTIVE,
        SessionState.CLOSED,
        SessionState.CLOSING,
    }

    for session in series:
        assert session.state in valid_states