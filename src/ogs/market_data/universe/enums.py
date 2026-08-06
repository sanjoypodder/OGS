"""
OGS Smart Money AI

Universe Enums
"""

from __future__ import annotations

from enum import Enum


class UniverseType(Enum):
    """
    Universe classification.
    """

    UNKNOWN = "UNKNOWN"

    EXCHANGE = "EXCHANGE"

    INDEX = "INDEX"

    SECTOR = "SECTOR"

    INDUSTRY = "INDUSTRY"

    WATCHLIST = "WATCHLIST"

    SCREENER = "SCREENER"

    PORTFOLIO = "PORTFOLIO"

    AI = "AI"

    CUSTOM = "CUSTOM"


class UniverseStatus(Enum):
    """
    Universe status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"