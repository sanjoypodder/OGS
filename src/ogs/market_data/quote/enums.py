"""
OGS Smart Money AI

Quote Enumerations
"""

from enum import Enum


class QuoteType(Enum):
    """
    Quote source type.
    """

    LIVE = "LIVE"
    HISTORICAL = "HISTORICAL"
    SIMULATED = "SIMULATED"
    PAPER = "PAPER"
    UNKNOWN = "UNKNOWN"


class QuoteStatus(Enum):
    """
    Quote status.
    """

    ACTIVE = "ACTIVE"
    STALE = "STALE"
    HALTED = "HALTED"
    CLOSED = "CLOSED"
    UNKNOWN = "UNKNOWN"