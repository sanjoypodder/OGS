"""
OGS Smart Money AI

Contract Enums
"""

from __future__ import annotations

from enum import Enum


class ContractType(Enum):
    """
    Contract category.
    """

    UNKNOWN = "UNKNOWN"

    SPOT = "SPOT"

    FUTURE = "FUTURE"

    OPTION = "OPTION"

    PERPETUAL = "PERPETUAL"

    CFD = "CFD"

    FORWARD = "FORWARD"

    SWAP = "SWAP"


class OptionType(Enum):
    """
    Option type.
    """

    NONE = "NONE"

    CALL = "CALL"

    PUT = "PUT"


class SettlementType(Enum):
    """
    Settlement type.
    """

    UNKNOWN = "UNKNOWN"

    CASH = "CASH"

    PHYSICAL = "PHYSICAL"


class ExerciseStyle(Enum):
    """
    Exercise style.
    """

    UNKNOWN = "UNKNOWN"

    AMERICAN = "AMERICAN"

    EUROPEAN = "EUROPEAN"

    BERMUDAN = "BERMUDAN"


class ContractStatus(Enum):
    """
    Trading status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    EXPIRED = "EXPIRED"

    SUSPENDED = "SUSPENDED"

    DELISTED = "DELISTED"

    SETTLED = "SETTLED"