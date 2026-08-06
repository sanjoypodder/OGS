"""
OGS Smart Money AI

Watchlist Enums
"""

from __future__ import annotations

from enum import Enum


class WatchlistType(Enum):
    """
    Watchlist classification.
    """

    UNKNOWN = "UNKNOWN"

    PERSONAL = "PERSONAL"

    SYSTEM = "SYSTEM"

    SMART_MONEY = "SMART_MONEY"

    PORTFOLIO = "PORTFOLIO"

    SCREENER = "SCREENER"

    CUSTOM = "CUSTOM"


class WatchlistStatus(Enum):
    """
    Watchlist status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"