"""
OGS Smart Money AI

Calendar Enums
"""

from __future__ import annotations

from enum import Enum


class CalendarType(Enum):
    """
    Trading calendar day type.
    """

    UNKNOWN = "UNKNOWN"

    TRADING_DAY = "TRADING_DAY"

    HOLIDAY = "HOLIDAY"

    WEEKEND = "WEEKEND"

    HALF_DAY = "HALF_DAY"

    SPECIAL_SESSION = "SPECIAL_SESSION"

    MAINTENANCE = "MAINTENANCE"


class CalendarStatus(Enum):
    """
    Trading availability.
    """

    UNKNOWN = "UNKNOWN"

    OPEN = "OPEN"

    CLOSED = "CLOSED"