"""
OGS Smart Money AI
------------------

Market Data - Timeframe Domain

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

from .enums import TimeframeType


_DURATION_MAP = {
    TimeframeType.M1: timedelta(minutes=1),
    TimeframeType.M5: timedelta(minutes=5),
    TimeframeType.M15: timedelta(minutes=15),
    TimeframeType.M30: timedelta(minutes=30),
    TimeframeType.H1: timedelta(hours=1),
    TimeframeType.H4: timedelta(hours=4),
    TimeframeType.D1: timedelta(days=1),
    TimeframeType.W1: timedelta(weeks=1),
    TimeframeType.MN1: timedelta(days=30),
}


@dataclass(frozen=True, slots=True)
class Timeframe:
    """
    Immutable timeframe domain object.
    """

    value: TimeframeType

    @property
    def duration(self) -> timedelta:
        """
        Return timeframe duration.
        """
        return _DURATION_MAP[self.value]

    @property
    def minutes(self) -> int:
        """
        Return duration in minutes.
        """
        return int(self.duration.total_seconds() // 60)

    @property
    def seconds(self) -> int:
        """
        Return duration in seconds.
        """
        return int(self.duration.total_seconds())

    @property
    def label(self) -> str:
        """
        Display label.
        """
        return self.value.value

    @property
    def is_intraday(self) -> bool:
        """
        True if timeframe is below one day.
        """
        return self.value in {
            TimeframeType.M1,
            TimeframeType.M5,
            TimeframeType.M15,
            TimeframeType.M30,
            TimeframeType.H1,
            TimeframeType.H4,
        }

    @property
    def is_daily_or_higher(self) -> bool:
        """
        True for D1 and above.
        """
        return self.value in {
            TimeframeType.D1,
            TimeframeType.W1,
            TimeframeType.MN1,
        }