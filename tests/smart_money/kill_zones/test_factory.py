"""
===========================================================

OGS Smart Money AI

Kill Zone Factory Tests

===========================================================
"""

from datetime import datetime, timedelta

import pytest

from ogs.smart_money.kill_zones import (
    KillZone,
    KillZoneFactory,
    KillZoneStatus,
    KillZoneType,
    SessionType,
    TimeZoneType,
)


@pytest.fixture
def start():
    return datetime(2026, 1, 1, 7, 0, 0)


@pytest.fixture
def end(start):
    return start + timedelta(hours=3)


def test_create_valid_zone(start, end):

    zone = KillZoneFactory.create(
        symbol="XAUUSD",
        zone=KillZoneType.LONDON,
        session=SessionType.EUROPE,
        status=KillZoneStatus.ACTIVE,
        start_time=start,
        end_time=end,
        timezone=TimeZoneType.UTC,
        active=True,
    )

    assert isinstance(zone, KillZone)


def test_symbol(start, end):

    zone = KillZoneFactory.create(
        "BTCUSD",
        KillZoneType.NEW_YORK,
        SessionType.AMERICA,
        KillZoneStatus.UPCOMING,
        start,
        end,
    )

    assert zone.symbol == "BTCUSD"


def test_zone(start, end):

    zone = KillZoneFactory.create(
        "EURUSD",
        KillZoneType.LONDON,
        SessionType.EUROPE,
        KillZoneStatus.ACTIVE,
        start,
        end,
    )

    assert zone.zone is KillZoneType.LONDON


def test_session(start, end):

    zone = KillZoneFactory.create(
        "GBPUSD",
        KillZoneType.LONDON,
        SessionType.EUROPE,
        KillZoneStatus.ACTIVE,
        start,
        end,
    )

    assert zone.session is SessionType.EUROPE


def test_status(start, end):

    zone = KillZoneFactory.create(
        "XAUUSD",
        KillZoneType.ASIAN,
        SessionType.ASIA,
        KillZoneStatus.COMPLETED,
        start,
        end,
    )

    assert zone.status is KillZoneStatus.COMPLETED


def test_timezone_default(start, end):

    zone = KillZoneFactory.create(
        "XAUUSD",
        KillZoneType.ASIAN,
        SessionType.ASIA,
        KillZoneStatus.ACTIVE,
        start,
        end,
    )

    assert zone.timezone is TimeZoneType.UTC


def test_active_flag(start, end):

    zone = KillZoneFactory.create(
        "XAUUSD",
        KillZoneType.NEW_YORK,
        SessionType.AMERICA,
        KillZoneStatus.ACTIVE,
        start,
        end,
        active=True,
    )

    assert zone.active


def test_invalid_symbol(start, end):

    with pytest.raises(ValueError):

        KillZoneFactory.create(
            "",
            KillZoneType.LONDON,
            SessionType.EUROPE,
            KillZoneStatus.ACTIVE,
            start,
            end,
        )


def test_invalid_end_time(start):

    with pytest.raises(ValueError):

        KillZoneFactory.create(
            "XAUUSD",
            KillZoneType.LONDON,
            SessionType.EUROPE,
            KillZoneStatus.ACTIVE,
            start,
            start,
        )


def test_end_before_start(start):

    with pytest.raises(ValueError):

        KillZoneFactory.create(
            "XAUUSD",
            KillZoneType.LONDON,
            SessionType.EUROPE,
            KillZoneStatus.ACTIVE,
            start,
            start - timedelta(minutes=5),
        )


def test_multiple_creation(start, end):

    for _ in range(25):

        zone = KillZoneFactory.create(
            "XAUUSD",
            KillZoneType.LONDON,
            SessionType.EUROPE,
            KillZoneStatus.ACTIVE,
            start,
            end,
        )

        assert isinstance(zone, KillZone)


def test_return_type(start, end):

    zone = KillZoneFactory.create(
        "EURUSD",
        KillZoneType.ASIAN,
        SessionType.ASIA,
        KillZoneStatus.UPCOMING,
        start,
        end,
    )

    assert type(zone).__name__ == "KillZone"