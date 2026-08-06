"""
OGS Smart Money AI
------------------

Session Engine Domain

Immutable Session domain object.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .enums import (
    SessionState,
    SessionType,
    TimeZoneType,
    TradingDay,
)


@dataclass(frozen=True, slots=True)
class Session:
    """
    Immutable trading session.
    """

    symbol: str

    session: SessionType

    state: SessionState

    trading_day: TradingDay

    timezone: TimeZoneType

    start_time: datetime

    end_time: datetime

    active: bool = False

    tradable: bool = False

    @property
    def duration_seconds(self) -> float:
        """
        Session duration in seconds.
        """
        return (self.end_time - self.start_time).total_seconds()

    @property
    def duration_minutes(self) -> float:
        """
        Session duration in minutes.
        """
        return self.duration_seconds / 60

    @property
    def duration_hours(self) -> float:
        """
        Session duration in hours.
        """
        return self.duration_minutes / 60

    def contains(
        self,
        timestamp: datetime,
    ) -> bool:
        """
        Return True if timestamp falls within the session.
        """
        return self.start_time <= timestamp <= self.end_time

    def is_open(
        self,
        timestamp: datetime,
    ) -> bool:
        """
        Return True if session is active at timestamp.
        """
        return self.contains(timestamp)

    def is_closed(
        self,
        timestamp: datetime,
    ) -> bool:
        """
        Return True if session has ended.
        """
        return timestamp > self.end_time

    def is_upcoming(
        self,
        timestamp: datetime,
    ) -> bool:
        """
        Return True if session has not started yet.
        """
        return timestamp < self.start_time

    def is_tradable(self) -> bool:
        """
        Return whether trading is allowed.
        """
        return self.tradable