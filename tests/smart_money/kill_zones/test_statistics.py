"""
===========================================================

OGS Smart Money AI

Kill Zone Statistics Tests

===========================================================
"""

from datetime import datetime, timedelta

import pytest

from ogs.smart_money.kill_zones import (
    KillZone,
    KillZoneSeries,
    KillZoneStatistics,
    KillZoneStatus,
    KillZoneType,
    SessionType,
    TimeZoneType,
)


def make_zone(
    zone_type,
    session,
    status,
    active=False,
):

    start = datetime(2026, 1, 1, 0, 0)
    end = start + timedelta(hours=3)

    return KillZone(
        symbol="XAUUSD",
        zone=zone_type,
        session=session,
        status=status,
        start_time=start,
        end_time=end,
        timezone=TimeZoneType.UTC,
        active=active,
    )


@pytest.fixture
def stats():

    series = KillZoneSeries(
        [
            make_zone(
                KillZoneType.ASIAN,
                SessionType.ASIA,
                KillZoneStatus.COMPLETED,
            ),
            make_zone(
                KillZoneType.LONDON,
                SessionType.EUROPE,
                KillZoneStatus.ACTIVE,
                True,
            ),
            make_zone(
                KillZoneType.NEW_YORK,
                SessionType.AMERICA,
                KillZoneStatus.UPCOMING,
            ),
            make_zone(
                KillZoneType.LONDON_CLOSE,
                SessionType.EUROPE,
                KillZoneStatus.UPCOMING,
            ),
        ]
    )

    return KillZoneStatistics(series)


def test_count(stats):

    assert stats.count == 4


def test_active_count(stats):

    assert stats.active_count == 1


def test_upcoming_count(stats):

    assert stats.upcoming_count == 2


def test_completed_count(stats):

    assert stats.completed_count == 1


def test_asian_count(stats):

    assert stats.asian_count == 1


def test_london_count(stats):

    assert stats.london_count == 1


def test_new_york_count(stats):

    assert stats.new_york_count == 1


def test_london_close_count(stats):

    assert stats.london_close_count == 1


def test_asia_session_count(stats):

    assert stats.asia_session_count == 1


def test_europe_session_count(stats):

    assert stats.europe_session_count == 2


def test_america_session_count(stats):

    assert stats.america_session_count == 1


def test_average_duration(stats):

    assert stats.average_duration_minutes == 180


def test_latest(stats):

    assert stats.latest.zone is KillZoneType.LONDON_CLOSE


def test_oldest(stats):

    assert stats.oldest.zone is KillZoneType.ASIAN


def test_current_active(stats):

    active = stats.current_active

    assert active is not None

    assert active.zone is KillZoneType.LONDON


def test_empty_statistics():

    stats = KillZoneStatistics(KillZoneSeries())

    assert stats.count == 0

    assert stats.active_count == 0

    assert stats.upcoming_count == 0

    assert stats.completed_count == 0

    assert stats.average_duration_minutes == 0.0

    assert stats.latest is None

    assert stats.oldest is None

    assert stats.current_active is None