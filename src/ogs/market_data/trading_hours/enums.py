"""
OGS Smart Money AI

TradingHours Enums
"""

from __future__ import annotations

from enum import Enum


class TradingHoursType(Enum):
    """
    Trading session classification.
    """

    UNKNOWN = "UNKNOWN"

    REGULAR = "REGULAR"

    PRE_MARKET = "PRE_MARKET"

    POST_MARKET = "POST_MARKET"

    OVERNIGHT = "OVERNIGHT"

    AUCTION = "AUCTION"

    EXTENDED = "EXTENDED"

    SPECIAL = "SPECIAL"

    CUSTOM = "CUSTOM"


class TradingHoursStatus(Enum):
    """
    Trading hours status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"