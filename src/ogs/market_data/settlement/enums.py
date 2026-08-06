"""
OGS Smart Money AI

Settlement Enums
"""

from __future__ import annotations

from enum import Enum


class SettlementType(Enum):
    """
    Settlement classification.
    """

    UNKNOWN = "UNKNOWN"

    CASH = "CASH"

    PHYSICAL = "PHYSICAL"

    NET = "NET"

    GROSS = "GROSS"

    DELIVERY = "DELIVERY"

    CUSTOM = "CUSTOM"


class SettlementStatus(Enum):
    """
    Settlement status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"


class SettlementCycle(Enum):
    """
    Settlement cycle.
    """

    UNKNOWN = "UNKNOWN"

    T0 = "T+0"

    T1 = "T+1"

    T2 = "T+2"

    T3 = "T+3"

    CUSTOM = "CUSTOM"


class SettlementMethod(Enum):
    """
    Settlement method.
    """

    UNKNOWN = "UNKNOWN"

    DVP = "DVP"

    RVP = "RVP"

    FOP = "FOP"

    BOOK_ENTRY = "BOOK_ENTRY"

    CUSTOM = "CUSTOM"