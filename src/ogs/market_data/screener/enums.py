"""
OGS Smart Money AI

Screener Enums
"""

from __future__ import annotations

from enum import Enum


class ScreenerType(Enum):
    """
    Screener classification.
    """

    UNKNOWN = "UNKNOWN"

    PERSONAL = "PERSONAL"

    SYSTEM = "SYSTEM"

    SMART_MONEY = "SMART_MONEY"

    TECHNICAL = "TECHNICAL"

    FUNDAMENTAL = "FUNDAMENTAL"

    AI = "AI"

    CUSTOM = "CUSTOM"


class ScreenerStatus(Enum):
    """
    Screener status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"