"""
OGS Smart Money AI

Position Enums
"""

from enum import Enum


class PositionSide(Enum):
    """
    Position direction.
    """

    LONG = "LONG"
    SHORT = "SHORT"
    UNKNOWN = "UNKNOWN"


class PositionStatus(Enum):
    """
    Position lifecycle status.
    """

    OPEN = "OPEN"
    PARTIALLY_CLOSED = "PARTIALLY_CLOSED"
    CLOSED = "CLOSED"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"