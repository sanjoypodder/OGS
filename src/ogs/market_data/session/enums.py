"""
OGS Smart Money AI

Session Enums
"""

from __future__ import annotations

from enum import Enum


class SessionType(Enum):
    """
    Trading session type.
    """

    UNKNOWN = "UNKNOWN"

    REGULAR = "REGULAR"

    PRE_MARKET = "PRE_MARKET"

    POST_MARKET = "POST_MARKET"

    PRE_OPEN = "PRE_OPEN"

    AUCTION = "AUCTION"

    HOLIDAY = "HOLIDAY"

    MAINTENANCE = "MAINTENANCE"

    EXTENDED = "EXTENDED"

    CONTINUOUS = "CONTINUOUS"


class SessionStatus(Enum):
    """
    Session status.
    """

    UNKNOWN = "UNKNOWN"

    OPEN = "OPEN"

    CLOSED = "CLOSED"

    PAUSED = "PAUSED"

    HALTED = "HALTED"

    COMPLETED = "COMPLETED"