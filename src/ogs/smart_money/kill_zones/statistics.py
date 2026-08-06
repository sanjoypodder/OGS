"""
OGS Smart Money AI
------------------

Kill Zone Statistics

Provides statistical information about a collection
of Kill Zone objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from .collection import KillZoneSeries
from .domain import KillZone
from .enums import (
    KillZoneStatus,
    KillZoneType,
    SessionType,
)


class KillZoneStatistics:
    """
    Statistics for Kill Zone collections.
    """

    def __init__(
        self,
        series: KillZoneSeries,
    ) -> None:

        self._series = series

    @property
    def count(self) -> int:
        return len(self._series)

    @property
    def active_count(self) -> int:
        return sum(
            zone.active
            for zone in self._series
        )

    @property
    def upcoming_count(self) -> int:
        return sum(
            zone.status == KillZoneStatus.UPCOMING
            for zone in self._series
        )

    @property
    def completed_count(self) -> int:
        return sum(
            zone.status == KillZoneStatus.COMPLETED
            for zone in self._series
        )

    @property
    def asian_count(self) -> int:
        return sum(
            zone.zone == KillZoneType.ASIAN
            for zone in self._series
        )

    @property
    def london_count(self) -> int:
        return sum(
            zone.zone == KillZoneType.LONDON
            for zone in self._series
        )

    @property
    def new_york_count(self) -> int:
        return sum(
            zone.zone == KillZoneType.NEW_YORK
            for zone in self._series
        )

    @property
    def london_close_count(self) -> int:
        return sum(
            zone.zone == KillZoneType.LONDON_CLOSE
            for zone in self._series
        )

    @property
    def asia_session_count(self) -> int:
        return sum(
            zone.session == SessionType.ASIA
            for zone in self._series
        )

    @property
    def europe_session_count(self) -> int:
        return sum(
            zone.session == SessionType.EUROPE
            for zone in self._series
        )

    @property
    def america_session_count(self) -> int:
        return sum(
            zone.session == SessionType.AMERICA
            for zone in self._series
        )

    @property
    def average_duration_minutes(self) -> float:

        if len(self._series) == 0:
            return 0.0

        return (
            sum(
                zone.duration_minutes
                for zone in self._series
            )
            / len(self._series)
        )

    @property
    def latest(self) -> KillZone | None:

        if len(self._series) == 0:
            return None

        return self._series.last

    @property
    def oldest(self) -> KillZone | None:

        if len(self._series) == 0:
            return None

        return self._series.first

    @property
    def current_active(self) -> KillZone | None:

        for zone in self._series:

            if zone.active:
                return zone

        return None