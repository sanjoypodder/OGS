"""
OGS Smart Money AI

CorporateEvent Enums
"""

from __future__ import annotations

from enum import Enum


class CorporateEventType(Enum):
    """
    Corporate event classification.
    """

    UNKNOWN = "UNKNOWN"

    EARNINGS = "EARNINGS"

    DIVIDEND = "DIVIDEND"

    STOCK_SPLIT = "STOCK_SPLIT"

    REVERSE_SPLIT = "REVERSE_SPLIT"

    BONUS = "BONUS"

    RIGHTS = "RIGHTS"

    MERGER = "MERGER"

    ACQUISITION = "ACQUISITION"

    SPIN_OFF = "SPIN_OFF"

    LISTING = "LISTING"

    DELISTING = "DELISTING"

    BUYBACK = "BUYBACK"

    IPO = "IPO"

    FPO = "FPO"

    NAME_CHANGE = "NAME_CHANGE"

    SYMBOL_CHANGE = "SYMBOL_CHANGE"

    CUSTOM = "CUSTOM"


class CorporateEventStatus(Enum):
    """
    Corporate event status.
    """

    UNKNOWN = "UNKNOWN"

    SCHEDULED = "SCHEDULED"

    ANNOUNCED = "ANNOUNCED"

    ACTIVE = "ACTIVE"

    COMPLETED = "COMPLETED"

    CANCELLED = "CANCELLED"

    ARCHIVED = "ARCHIVED"