"""
===========================================================

OGS Smart Money AI

Kill Zone Domain Tests

===========================================================
"""

from datetime import datetime, timedelta

import pytest

from ogs.smart_money.kill_zones import (
    KillZone,
    KillZoneStatus,
    KillZoneType,
    SessionType,
    TimeZoneType,
)


@pytest.fixture
def zone():

    start = datetime(2026, 1, 1, 7, 0, 0)
    end = start + timedelta(hours=3)

    return KillZone(
        symbol="XAUUSD",
        zone=KillZoneType.LONDON,
        session=SessionType.EUROPE,
        status=KillZoneStatus.ACTIVE,
        start_time=start,
        end_time=end,
        timezone=TimeZoneType.UTC,
        active=True,
    )


def test_symbol(zone):
    assert zone.symbol == "XAUUSD"


def test_zone(zone):
    assert zone.zone is KillZoneType.LONDON


def test_session(zone):
    assert zone.session is SessionType.EUROPE


def test_status(zone):
    assert zone.status is KillZoneStatus.ACTIVE


def test_timezone(zone):
    assert zone.timezone is TimeZoneType.UTC


def test_active(zone):
    assert zone.active is True


def test_duration_seconds(zone):
    assert zone.duration_seconds == 10800


def test_duration_minutes(zone):
    assert zone.duration_minutes == 180


def test_duration_hours(zone):
    assert zone.duration_hours == 3


def test_contains_true(zone):

    t = zone.start_time + timedelta(minutes=30)

    assert zone.contains(t)


def test_contains_false(zone):

    t = zone.end_time + timedelta(minutes=1)

    assert not zone.contains(t)


def test_is_upcoming(zone):

    t = zone.start_time - timedelta(minutes=10)

    assert zone.is_upcoming(t)


def test_is_completed(zone):

    t = zone.end_time + timedelta(minutes=1)

    assert zone.is_completed(t)


def test_is_not_completed(zone):

    t = zone.start_time

    assert not zone.is_completed(t)


def test_dataclass_is_frozen(zone):

    with pytest.raises(Exception):
        zone.symbol = "BTCUSD"