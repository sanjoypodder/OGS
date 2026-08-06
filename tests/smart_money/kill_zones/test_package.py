"""
===========================================================

OGS Smart Money AI

Kill Zones Package Tests

===========================================================
"""

from ogs.smart_money.kill_zones import (
    KillZone,
    KillZoneAnalyzer,
    KillZoneFactory,
    KillZoneSeries,
    KillZoneStatistics,
    KillZoneValidator,
    KillZoneType,
    SessionType,
    KillZoneStatus,
    TimeZoneType,
)


def test_imports():

    assert KillZone is not None

    assert KillZoneAnalyzer is not None

    assert KillZoneFactory is not None

    assert KillZoneSeries is not None

    assert KillZoneStatistics is not None

    assert KillZoneValidator is not None


def test_enums():

    assert KillZoneType.ASIAN.value == "Asian"

    assert SessionType.ASIA.value == "Asia"

    assert KillZoneStatus.ACTIVE.value == "Active"

    assert TimeZoneType.UTC.value == "UTC"