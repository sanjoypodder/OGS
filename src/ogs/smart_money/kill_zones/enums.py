"""
OGS Smart Money AI
------------------

Kill Zone Enums

Defines enumeration types for ICT Kill Zones and
Trading Sessions.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from enum import Enum, unique


@unique
class KillZoneType(Enum):
    """
    ICT Kill Zone Types.
    """

    ASIAN = "Asian"

    LONDON = "London"

    NEW_YORK = "New York"

    LONDON_CLOSE = "London Close"

    CUSTOM = "Custom"


@unique
class SessionType(Enum):
    """
    Trading Session Types.
    """

    ASIA = "Asia"

    EUROPE = "Europe"

    AMERICA = "America"

    CUSTOM = "Custom"


@unique
class KillZoneStatus(Enum):
    """
    Current Kill Zone Status.
    """

    UPCOMING = "Upcoming"

    ACTIVE = "Active"

    COMPLETED = "Completed"


@unique
class TimeZoneType(Enum):
    """
    Supported Time Zones.
    """

    UTC = "UTC"

    GMT = "GMT"

    IST = "Asia/Kolkata"

    NEW_YORK = "America/New_York"

    LONDON = "Europe/London"

    TOKYO = "Asia/Tokyo"

    CUSTOM = "Custom"