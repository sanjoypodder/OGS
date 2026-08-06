"""
OGS Smart Money AI
------------------

Kill Zone Analyzer

Detects ICT Kill Zones based on timestamps.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from datetime import datetime, time

from ogs.smart_money.base.analyzer import BaseAnalyzer

from .collection import KillZoneSeries
from .domain import KillZone
from .enums import (
    KillZoneStatus,
    KillZoneType,
    SessionType,
    TimeZoneType,
)


class KillZoneAnalyzer(
    BaseAnalyzer,
):
    """
    Analyzer for ICT Kill Zones.
    """

    DEFAULT_TIMEZONE = TimeZoneType.UTC

    KILL_ZONES = {

        KillZoneType.ASIAN: (
            time(0, 0),
            time(3, 0),
            SessionType.ASIA,
        ),

        KillZoneType.LONDON: (
            time(7, 0),
            time(10, 0),
            SessionType.EUROPE,
        ),

        KillZoneType.NEW_YORK: (
            time(12, 0),
            time(15, 0),
            SessionType.AMERICA,
        ),

        KillZoneType.LONDON_CLOSE: (
            time(15, 0),
            time(17, 0),
            SessionType.EUROPE,
        ),
    }

    def analyze(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> KillZoneSeries:
        """
        Analyze a timestamp and determine
        the active ICT Kill Zone.
        """

        series = KillZoneSeries()

        current = timestamp.time()

        for zone_type, (
            start,
            end,
            session,
        ) in self.KILL_ZONES.items():

            start_dt = datetime.combine(
                timestamp.date(),
                start,
            )

            end_dt = datetime.combine(
                timestamp.date(),
                end,
            )

            if start <= current <= end:

                status = KillZoneStatus.ACTIVE

                active = True

            elif current < start:

                status = KillZoneStatus.UPCOMING

                active = False

            else:

                status = KillZoneStatus.COMPLETED

                active = False

            series.append(

                KillZone(

                    symbol=symbol,

                    zone=zone_type,

                    session=session,

                    status=status,

                    start_time=start_dt,

                    end_time=end_dt,

                    timezone=self.DEFAULT_TIMEZONE,

                    active=active,
                )

            )

        return series

    def active(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> KillZone | None:
        """
        Return the currently active Kill Zone.
        """

        series = self.analyze(
            symbol,
            timestamp,
        )

        for zone in series:

            if zone.active:
                return zone

        return None

    def upcoming(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> list[KillZone]:
        """
        Return upcoming Kill Zones.
        """

        series = self.analyze(
            symbol,
            timestamp,
        )

        return [
            zone
            for zone in series
            if zone.status is KillZoneStatus.UPCOMING
        ]

    def completed(
        self,
        symbol: str,
        timestamp: datetime,
    ) -> list[KillZone]:
        """
        Return completed Kill Zones.
        """

        series = self.analyze(
            symbol,
            timestamp,
        )

        return [
            zone
            for zone in series
            if zone.status is KillZoneStatus.COMPLETED
        ]