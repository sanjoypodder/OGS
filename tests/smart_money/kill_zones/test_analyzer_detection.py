"""
===========================================================

OGS Smart Money AI

Kill Zone Analyzer Detection Tests

===========================================================
"""

from datetime import datetime

from ogs.smart_money.kill_zones import (
    KillZoneAnalyzer,
    KillZoneStatus,
    KillZoneType,
)


def test_detect_asian():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 1, 30),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.ASIAN

    assert zone.status is KillZoneStatus.ACTIVE


def test_detect_london():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 30),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.LONDON

    assert zone.status is KillZoneStatus.ACTIVE


def test_detect_new_york():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 13, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.NEW_YORK

    assert zone.status is KillZoneStatus.ACTIVE


def test_detect_london_close():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 16, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.LONDON_CLOSE

    assert zone.status is KillZoneStatus.ACTIVE


def test_before_first_session():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 23, 30),
    )

    assert zone is None


def test_after_last_session():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 18, 30),
    )

    assert zone is None


def test_boundary_start_asian():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 0, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.ASIAN


def test_boundary_end_asian():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 3, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.ASIAN


def test_boundary_start_london():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 7, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.LONDON


def test_boundary_end_london():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 10, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.LONDON