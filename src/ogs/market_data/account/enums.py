"""
OGS Smart Money AI

Account Enums
"""

from enum import Enum


class AccountType(Enum):
    """
    Trading account type.
    """

    LIVE = "LIVE"
    PAPER = "PAPER"
    DEMO = "DEMO"
    BACKTEST = "BACKTEST"
    UNKNOWN = "UNKNOWN"


class AccountStatus(Enum):
    """
    Account status.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"
    CLOSED = "CLOSED"
    UNKNOWN = "UNKNOWN"