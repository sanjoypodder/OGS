"""
===========================================================

OGS Smart Money AI

Kill Zone Analyzer Performance Tests

===========================================================
"""

from datetime import datetime
from time import perf_counter

from ogs.smart_money.kill_zones import (
    KillZoneAnalyzer,
    KillZoneSeries,
)


def test_single_analysis():

    analyzer = KillZoneAnalyzer()

    series = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert isinstance(series, KillZoneSeries)

    assert len(series) == 4


def test_1000_analyses():

    analyzer = KillZoneAnalyzer()

    for _ in range(1000):

        series = analyzer.analyze(
            "XAUUSD",
            datetime(2026, 1, 1, 13, 0),
        )

        assert len(series) == 4


def test_active_1000_times():

    analyzer = KillZoneAnalyzer()

    for _ in range(1000):

        zone = analyzer.active(
            "XAUUSD",
            datetime(2026, 1, 1, 8, 30),
        )

        assert zone is not None


def test_upcoming_1000_times():

    analyzer = KillZoneAnalyzer()

    for _ in range(1000):

        zones = analyzer.upcoming(
            "XAUUSD",
            datetime(2026, 1, 1, 8, 30),
        )

        assert len(zones) == 2


def test_completed_1000_times():

    analyzer = KillZoneAnalyzer()

    for _ in range(1000):

        zones = analyzer.completed(
            "XAUUSD",
            datetime(2026, 1, 1, 8, 30),
        )

        assert len(zones) == 1


def test_execution_speed():

    analyzer = KillZoneAnalyzer()

    start = perf_counter()

    for _ in range(5000):

        analyzer.analyze(
            "XAUUSD",
            datetime(2026, 1, 1, 13, 0),
        )

    elapsed = perf_counter() - start

    # Conservative threshold to avoid flaky failures
    assert elapsed < 2.0