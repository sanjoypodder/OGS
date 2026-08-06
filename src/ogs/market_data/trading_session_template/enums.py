"""
OGS Smart Money AI

TradingSessionTemplate Enums
"""

from __future__ import annotations

from enum import Enum


class TradingSessionTemplateType(Enum):
    """
    Trading session template classification.
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


class TradingSessionTemplateStatus(Enum):
    """
    Trading session template status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"