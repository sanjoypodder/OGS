"""
Tests for SessionAnalyzer basic functionality.
"""

from datetime import datetime

from ogs.smart_money.session_engine import (
    SessionAnalyzer,
    SessionSeries,
    SessionType,
)


def test_analyzer_creation():

    analyzer = SessionAnalyzer()

    assert analyzer is not None


def test_analyze_returns_series():

    analyzer = SessionAnalyzer()

    series = analyzer.analyze(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert isinstance(series, SessionSeries)


def test_series_not_empty():

    analyzer = SessionAnalyzer()

    series = analyzer.analyze(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert len(series) > 0


def test_all_sessions_have_symbol():

    analyzer = SessionAnalyzer()

    series = analyzer.analyze(
        symbol="BTCUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    for session in series:
        assert session.symbol == "BTCUSD"


def test_active_session():

    analyzer = SessionAnalyzer()

    session = analyzer.active(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert session is not None
    assert session.session == SessionType.LONDON


def test_tradable_sessions():

    analyzer = SessionAnalyzer()

    sessions = analyzer.tradable(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert len(sessions) == 1
    assert sessions[0].tradable


def test_closed_sessions():

    analyzer = SessionAnalyzer()

    sessions = analyzer.closed(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert len(sessions) >= 1


def test_pre_open_sessions():

    analyzer = SessionAnalyzer()

    sessions = analyzer.pre_open(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert len(sessions) >= 1


def test_active_symbol():

    analyzer = SessionAnalyzer()

    session = analyzer.active(
        symbol="EURUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert session.symbol == "EURUSD"


def test_multiple_calls():

    analyzer = SessionAnalyzer()

    first = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    second = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert len(first) == len(second)


def test_analyzer_default_timezone():

    analyzer = SessionAnalyzer()

    series = analyzer.analyze(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    for session in series:
        assert session.timezone == analyzer.DEFAULT_TIMEZONE


def test_session_types_present():

    analyzer = SessionAnalyzer()

    series = analyzer.analyze(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    session_types = {session.session for session in series}

    assert SessionType.ASIAN in session_types
    assert SessionType.LONDON in session_types
    assert SessionType.NEW_YORK in session_types
    assert SessionType.LONDON_CLOSE in session_types