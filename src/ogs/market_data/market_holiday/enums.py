"""
OGS Smart Money AI

MarketHoliday Enums
"""

from __future__ import annotations

from enum import Enum


class MarketHolidayType(Enum):
    """
    Market holiday classification.
    """

    UNKNOWN = "UNKNOWN"

    NATIONAL = "NATIONAL"

    EXCHANGE = "EXCHANGE"

    BANK = "BANK"

    RELIGIOUS = "RELIGIOUS"

    PUBLIC = "PUBLIC"

    SPECIAL_TRADING = "SPECIAL_TRADING"

    HALF_DAY = "HALF_DAY"

    EMERGENCY = "EMERGENCY"

    CUSTOM = "CUSTOM"


class MarketHolidayStatus(Enum):
    """
    Market holiday status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"