"""
OGS Smart Money AI

Trade Enums
"""

from enum import Enum


class TradeSide(Enum):
    """
    Trade direction.
    """

    BUY = "BUY"
    SELL = "SELL"
    UNKNOWN = "UNKNOWN"


class TradeStatus(Enum):
    """
    Trade execution status.
    """

    PENDING = "PENDING"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    UNKNOWN = "UNKNOWN"