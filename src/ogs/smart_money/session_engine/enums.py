"""
OGS Smart Money AI
------------------

Session Engine Enums

Defines trading sessions and session states.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from enum import Enum


class SessionType(str, Enum):
    """
    ICT Trading Sessions.
    """

    ASIAN = "Asian"

    LONDON = "London"

    NEW_YORK = "New York"

    LONDON_CLOSE = "London Close"

    CUSTOM = "Custom"


class SessionState(str, Enum):
    """
    Current session state.
    """

    PRE_OPEN = "Pre Open"

    ACTIVE = "Active"

    CLOSING = "Closing"

    CLOSED = "Closed"


class TradingDay(str, Enum):
    """
    Trading weekdays.
    """

    MONDAY = "Monday"

    TUESDAY = "Tuesday"

    WEDNESDAY = "Wednesday"

    THURSDAY = "Thursday"

    FRIDAY = "Friday"

    SATURDAY = "Saturday"

    SUNDAY = "Sunday"


class TimeZoneType(str, Enum):
    """
    Supported time zones.
    """

    UTC = "UTC"

    GMT = "GMT"

    IST = "IST"

    NEW_YORK = "America/New_York"

    LONDON = "Europe/London"

    TOKYO = "Asia/Tokyo"

    CUSTOM = "Custom"