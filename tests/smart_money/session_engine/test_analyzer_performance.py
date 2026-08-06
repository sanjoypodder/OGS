"""
Performance and scalability tests for SessionAnalyzer.
"""

from datetime import datetime, timedelta
import time

from ogs.smart_money.session_engine import (
    SessionAnalyzer,
    SessionSeries,
)


def test_multiple_analysis_runs():

    analyzer = SessionAnalyzer()

    for _ in range(100):

        series = analyzer.analyze(
            symbol="XAUUSD",
            timestamp=datetime(2026, 1, 1, 8, 0),
        )

        assert isinstance(series, SessionSeries)
        assert len(series) > 0


def test_many_symbols():

    analyzer = SessionAnalyzer()

    for i in range(500):

        symbol = f"SYM{i}"

        series = analyzer.analyze(
            symbol=symbol,
            timestamp=datetime(2026, 1, 1, 8, 0),
        )

        assert series[0].symbol == symbol


def test_many_timestamps():

    analyzer = SessionAnalyzer()

    start = datetime(2026, 1, 1, 0, 0)

    for minute in range(24 * 60):

        ts = start + timedelta(minutes=minute)

        series = analyzer.analyze(
            symbol="XAUUSD",
            timestamp=ts,
        )

        assert len(series) > 0


def test_repeated_active_detection():

    analyzer = SessionAnalyzer()

    ts = datetime(2026, 1, 1, 8, 0)

    for _ in range(1000):

        session = analyzer.active(
            "XAUUSD",
            ts,
        )

        assert session is not None


def test_repeated_tradable_detection():

    analyzer = SessionAnalyzer()

    ts = datetime(2026, 1, 1, 13, 0)

    for _ in range(1000):

        sessions = analyzer.tradable(
            "XAUUSD",
            ts,
        )

        assert len(sessions) == 1


def test_execution_time():

    analyzer = SessionAnalyzer()

    start = time.perf_counter()

    for _ in range(1000):

        analyzer.analyze(
            "XAUUSD",
            datetime(2026, 1, 1, 8, 0),
        )

    elapsed = time.perf_counter() - start

    # Keep this threshold generous so it is stable on CI and slower machines.
    assert elapsed < 5.0


def test_consistent_results():

    analyzer = SessionAnalyzer()

    ts = datetime(2026, 1, 1, 8, 0)

    first = analyzer.analyze("XAUUSD", ts)

    for _ in range(100):

        current = analyzer.analyze("XAUUSD", ts)

        assert len(current) == len(first)

        for a, b in zip(first, current):
            assert a.session == b.session
            assert a.state == b.state
            assert a.symbol == b.symbol