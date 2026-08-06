"""
===========================================================

OGS Smart Money AI

Kill Zone Analyzer Basic Tests

===========================================================
"""

from datetime import datetime

from ogs.smart_money.kill_zones import (
    KillZone,
    KillZoneAnalyzer,
    KillZoneSeries,
    KillZoneStatus,
    KillZoneType,
)


def test_analyze_returns_series():

    analyzer = KillZoneAnalyzer()

    series = analyzer.analyze(
        symbol="XAUUSD",
        timestamp=datetime(2026, 1, 1, 8, 0),
    )

    assert isinstance(series, KillZoneSeries)


def test_analyze_returns_four_zones():

    analyzer = KillZoneAnalyzer()

    series = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert len(series) == 4


def test_active_returns_killzone():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert isinstance(zone, KillZone)


def test_active_is_london():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert zone.zone is KillZoneType.LONDON

    assert zone.status is KillZoneStatus.ACTIVE

    assert zone.active


def test_upcoming_returns_list():

    analyzer = KillZoneAnalyzer()

    zones = analyzer.upcoming(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert isinstance(zones, list)


def test_completed_returns_list():

    analyzer = KillZoneAnalyzer()

    zones = analyzer.completed(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert isinstance(zones, list)


def test_completed_contains_asian():

    analyzer = KillZoneAnalyzer()

    zones = analyzer.completed(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert len(zones) == 1

    assert zones[0].zone is KillZoneType.ASIAN


def test_upcoming_contains_two():

    analyzer = KillZoneAnalyzer()

    zones = analyzer.upcoming(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    assert len(zones) == 2

    assert zones[0].zone is KillZoneType.NEW_YORK

    assert zones[1].zone is KillZoneType.LONDON_CLOSE