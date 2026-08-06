"""
===========================================================

OGS Smart Money AI

Kill Zone Collection Tests

===========================================================
"""

from datetime import datetime, timedelta

import pytest

from ogs.smart_money.kill_zones import (
    KillZone,
    KillZoneSeries,
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
def series():

    return KillZoneSeries(
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


def test_length(series):

    assert len(series) == 4


def test_append(series):

    zone = make_zone(
        KillZoneType.ASIAN,
        SessionType.ASIA,
        KillZoneStatus.UPCOMING,
    )

    series.append(zone)

    assert len(series) == 5


def test_latest(series):

    latest = series.latest()

    assert len(latest) == 1

    assert latest[0].zone is KillZoneType.LONDON_CLOSE


def test_latest_two(series):

    latest = series.latest(2)

    assert len(latest) == 2

    assert latest[0].zone is KillZoneType.NEW_YORK

    assert latest[1].zone is KillZoneType.LONDON_CLOSE


def test_active(series):

    active = series.active()

    assert len(active) == 1

    assert active[0].active


def test_by_zone(series):

    result = series.by_zone(
        KillZoneType.LONDON
    )

    assert len(result) == 1

    assert result[0].zone is KillZoneType.LONDON


def test_by_session(series):

    result = series.by_session(
        SessionType.EUROPE
    )

    assert len(result) == 2


def test_by_status(series):

    result = series.by_status(
        KillZoneStatus.UPCOMING
    )

    assert len(result) == 2


def test_empty_series():

    series = KillZoneSeries()

    assert len(series) == 0


def test_empty_active():

    series = KillZoneSeries()

    assert series.active() == []


def test_empty_latest():

    series = KillZoneSeries()

    assert series.latest() == []


def test_iteration(series):

    count = 0

    for _ in series:

        count += 1

    assert count == 4