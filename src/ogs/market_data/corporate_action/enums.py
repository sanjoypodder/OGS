"""
OGS Smart Money AI

CorporateAction Enums
"""

from __future__ import annotations

from enum import Enum


class CorporateActionType(Enum):
    """
    Corporate Action Type.
    """

    UNKNOWN = "UNKNOWN"

    STOCK_SPLIT = "STOCK_SPLIT"

    REVERSE_SPLIT = "REVERSE_SPLIT"

    BONUS = "BONUS"

    DIVIDEND = "DIVIDEND"

    SPECIAL_DIVIDEND = "SPECIAL_DIVIDEND"

    RIGHTS = "RIGHTS"

    BUYBACK = "BUYBACK"

    MERGER = "MERGER"

    DEMERGER = "DEMERGER"

    SPIN_OFF = "SPIN_OFF"

    SYMBOL_CHANGE = "SYMBOL_CHANGE"

    FACE_VALUE_CHANGE = "FACE_VALUE_CHANGE"


class CorporateActionStatus(Enum):
    """
    Corporate Action Status.
    """

    UNKNOWN = "UNKNOWN"

    ANNOUNCED = "ANNOUNCED"

    EFFECTIVE = "EFFECTIVE"

    COMPLETED = "COMPLETED"

    CANCELLED = "CANCELLED"