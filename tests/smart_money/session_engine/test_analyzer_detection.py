"""
Tests for SessionAnalyzer session detection.
"""

from datetime import datetime

import pytest

from ogs.smart_money.session_engine import (
    SessionAnalyzer,
    SessionState,
    SessionType,
)


@pytest.fixture
def analyzer():
    return SessionAnalyzer()


@pytest.mark.parametrize(
    "hour, expected_session",
    [
        (1, SessionType.ASIAN),
        (8, SessionType.LONDON),
        (13, SessionType.NEW_YORK),
        (16, SessionType.LONDON_CLOSE),
    ],
)
def test_active_session_detection(
    analyzer,
    hour,
    expected_session,
):

    session = analyzer.active(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, hour, 0),
    )

    assert session is not None
    assert session.session == expected_session
    assert session.state == SessionState.ACTIVE


@pytest.mark.parametrize(
    "hour",
    [
        4,
        5,
        6,
        18,
        20,
        23,
    ],
)
def test_no_active_session(
    analyzer,
    hour,
):

    session = analyzer.active(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, hour, 0),
    )

    assert session is None


def test_london_tradable(analyzer):

    sessions = analyzer.tradable(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert len(sessions) == 1
    assert sessions[0].session == SessionType.LONDON


def test_newyork_tradable(analyzer):

    sessions = analyzer.tradable(
        "XAUUSD",
        datetime(2026, 1, 1, 13, 0),
    )

    assert len(sessions) == 1
    assert sessions[0].session == SessionType.NEW_YORK


def test_london_close_tradable(analyzer):

    sessions = analyzer.tradable(
        "XAUUSD",
        datetime(2026, 1, 1, 16, 0),
    )

    assert len(sessions) == 1
    assert sessions[0].session == SessionType.LONDON_CLOSE


def test_asian_tradable(analyzer):

    sessions = analyzer.tradable(
        "BTCUSD",
        datetime(2026, 1, 1, 1, 0),
    )

    assert len(sessions) == 1
    assert sessions[0].session == SessionType.ASIAN


def test_before_london_is_preopen(analyzer):

    sessions = analyzer.pre_open(
        "XAUUSD",
        datetime(2026, 1, 1, 6, 0),
    )

    assert any(
        s.session == SessionType.LONDON
        for s in sessions
    )


def test_after_london_is_closed(analyzer):

    sessions = analyzer.closed(
        "XAUUSD",
        datetime(2026, 1, 1, 11, 0),
    )

    assert any(
        s.session == SessionType.LONDON
        for s in sessions
    )


def test_after_asian_closed(analyzer):

    sessions = analyzer.closed(
        "XAUUSD",
        datetime(2026, 1, 1, 5, 0),
    )

    assert any(
        s.session == SessionType.ASIAN
        for s in sessions
    )


def test_before_newyork_preopen(analyzer):

    sessions = analyzer.pre_open(
        "XAUUSD",
        datetime(2026, 1, 1, 11, 0),
    )

    assert any(
        s.session == SessionType.NEW_YORK
        for s in sessions
    )