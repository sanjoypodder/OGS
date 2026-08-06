"""
OGS Smart Money AI

Portfolio Enums
"""

from enum import Enum


class PortfolioType(Enum):
    """
    Portfolio type.
    """

    LIVE = "LIVE"
    PAPER = "PAPER"
    BACKTEST = "BACKTEST"
    DEMO = "DEMO"
    UNKNOWN = "UNKNOWN"


class PortfolioStatus(Enum):
    """
    Portfolio status.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CLOSED = "CLOSED"
    SUSPENDED = "SUSPENDED"
    UNKNOWN = "UNKNOWN"