"""
OGS Smart Money AI

Exchange Enums
"""

from enum import Enum


class ExchangeStatus(Enum):
    """
    Exchange operational status.
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    HALTED = "HALTED"
    MAINTENANCE = "MAINTENANCE"
    UNKNOWN = "UNKNOWN"


class TradingSession(Enum):
    """
    Trading session.
    """

    PRE_MARKET = "PRE_MARKET"
    REGULAR = "REGULAR"
    POST_MARKET = "POST_MARKET"
    AUCTION = "AUCTION"
    CLOSED = "CLOSED"