"""
OGS Smart Money AI
------------------

Kill Zone Domain

Immutable domain object representing an ICT Kill Zone.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .enums import (
    KillZoneStatus,
    KillZoneType,
    SessionType,
    TimeZoneType,
)


@dataclass(
    frozen=True,
    slots=True,
)
class KillZone:
    """
    Represents a single ICT Kill Zone.
    """

    symbol: str

    zone: KillZoneType

    session: SessionType

    status: KillZoneStatus

    start_time: datetime

    end_time: datetime

    timezone: TimeZoneType

    active: bool = False

    @property
    def duration_seconds(self) -> float:
        """
        Duration of the Kill Zone in seconds.
        """
        return (
            self.end_time -
            self.start_time
        ).total_seconds()

    @property
    def duration_minutes(self) -> float:
        """
        Duration of the Kill Zone in minutes.
        """
        return self.duration_seconds / 60.0

    @property
    def duration_hours(self) -> float:
        """
        Duration of the Kill Zone in hours.
        """
        return self.duration_minutes / 60.0

    def contains(
        self,
        timestamp: datetime,
    ) -> bool:
        """
        Returns True if timestamp falls
        inside the Kill Zone.
        """
        return (
            self.start_time
            <= timestamp
            <= self.end_time
        )

    def is_upcoming(
        self,
        timestamp: datetime,
    ) -> bool:
        """
        True if Kill Zone has not started.
        """
        return timestamp < self.start_time

    def is_completed(
        self,
        timestamp: datetime,
    ) -> bool:
        """
        True if Kill Zone has finished.
        """
        return timestamp > self.end_time