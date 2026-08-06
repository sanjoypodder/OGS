"""
===========================================================

OGS Smart Money AI

Kill Zone Validator Tests

===========================================================
"""

from datetime import datetime, timedelta

import pytest

from ogs.smart_money.kill_zones import (
    KillZone,
    KillZoneStatus,
    KillZoneType,
    KillZoneValidator,
    SessionType,
    TimeZoneType,
)


@pytest.fixture
def validator():
    return KillZoneValidator()


@pytest.fixture
def valid_zone():

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


def test_valid_zone(validator, valid_zone):

    assert validator.validate(valid_zone)


def test_empty_symbol(validator, valid_zone):

    zone = KillZone(
        symbol="",
        zone=valid_zone.zone,
        session=valid_zone.session,
        status=valid_zone.status,
        start_time=valid_zone.start_time,
        end_time=valid_zone.end_time,
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_none_zone(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=None,
        session=valid_zone.session,
        status=valid_zone.status,
        start_time=valid_zone.start_time,
        end_time=valid_zone.end_time,
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_none_session(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=valid_zone.zone,
        session=None,
        status=valid_zone.status,
        start_time=valid_zone.start_time,
        end_time=valid_zone.end_time,
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_none_status(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=valid_zone.zone,
        session=valid_zone.session,
        status=None,
        start_time=valid_zone.start_time,
        end_time=valid_zone.end_time,
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_none_timezone(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=valid_zone.zone,
        session=valid_zone.session,
        status=valid_zone.status,
        start_time=valid_zone.start_time,
        end_time=valid_zone.end_time,
        timezone=None,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_none_start_time(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=valid_zone.zone,
        session=valid_zone.session,
        status=valid_zone.status,
        start_time=None,
        end_time=valid_zone.end_time,
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_none_end_time(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=valid_zone.zone,
        session=valid_zone.session,
        status=valid_zone.status,
        start_time=valid_zone.start_time,
        end_time=None,
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_end_before_start(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=valid_zone.zone,
        session=valid_zone.session,
        status=valid_zone.status,
        start_time=valid_zone.start_time,
        end_time=valid_zone.start_time - timedelta(minutes=1),
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_zero_duration(validator, valid_zone):

    zone = KillZone(
        symbol=valid_zone.symbol,
        zone=valid_zone.zone,
        session=valid_zone.session,
        status=valid_zone.status,
        start_time=valid_zone.start_time,
        end_time=valid_zone.start_time,
        timezone=valid_zone.timezone,
        active=valid_zone.active,
    )

    assert not validator.validate(zone)


def test_validator_multiple_calls(validator, valid_zone):

    for _ in range(10):
        assert validator.validate(valid_zone)


def test_validator_returns_bool(validator, valid_zone):

    result = validator.validate(valid_zone)

    assert isinstance(result, bool)