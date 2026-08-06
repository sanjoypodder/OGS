"""
===========================================================

OGS Smart Money AI

Kill Zone Analyzer Edge Case Tests

===========================================================
"""

from datetime import datetime

from ogs.smart_money.kill_zones import (
    KillZoneAnalyzer,
    KillZoneType,
)


def test_exact_transition_asian_to_london():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 3, 1),
    )

    assert zone is None


def test_exact_transition_london_to_new_york():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 10, 1),
    )

    assert zone is None


def test_exact_transition_new_york_to_london_close():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 15, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.NEW_YORK


def test_after_london_close():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 17, 1),
    )

    assert zone is None


def test_midnight_previous_day():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "BTCUSD",
        datetime(2026, 5, 20, 23, 59),
    )

    assert zone is None


def test_midnight_new_day():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "BTCUSD",
        datetime(2026, 5, 21, 0, 0),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.ASIAN


def test_leap_year_date():

    analyzer = KillZoneAnalyzer()

    zone = analyzer.active(
        "EURUSD",
        datetime(2028, 2, 29, 8, 30),
    )

    assert zone is not None

    assert zone.zone is KillZoneType.LONDON


def test_multiple_calls_same_result():

    analyzer = KillZoneAnalyzer()

    first = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 30),
    )

    second = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 30),
    )

    assert first.zone == second.zone

    assert first.status == second.status


def test_different_symbols():

    analyzer = KillZoneAnalyzer()

    gold = analyzer.active(
        "XAUUSD",
        datetime(2026, 1, 1, 13, 0),
    )

    bitcoin = analyzer.active(
        "BTCUSD",
        datetime(2026, 1, 1, 13, 0),
    )

    assert gold.zone == bitcoin.zone

    assert gold.symbol == "XAUUSD"

    assert bitcoin.symbol == "BTCUSD"


def test_analyze_always_returns_four_zones():

    analyzer = KillZoneAnalyzer()

    hours = [
        0,
        2,
        5,
        8,
        12,
        16,
        20,
        23,
    ]

    for hour in hours:

        series = analyzer.analyze(
            "XAUUSD",
            datetime(2026, 1, 1, hour, 0),
        )

        assert len(series) == 4


def test_no_duplicate_active_zones():

    analyzer = KillZoneAnalyzer()

    series = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 1, 13, 0),
    )

    active = [
        zone
        for zone in series
        if zone.active
    ]

    assert len(active) <= 1


def test_zone_order_is_constant():

    analyzer = KillZoneAnalyzer()

    series = analyzer.analyze(
        "XAUUSD",
        datetime(2026, 1, 1, 8, 0),
    )

    expected = [
        KillZoneType.ASIAN,
        KillZoneType.LONDON,
        KillZoneType.NEW_YORK,
        KillZoneType.LONDON_CLOSE,
    ]

    actual = [
        zone.zone
        for zone in series
    ]

    assert actual == expected